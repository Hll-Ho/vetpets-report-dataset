# -*- coding: utf-8 -*-
"""W7-REL-001 / B3 — release manifest + sampling verification + redaction log.

Offline. Writes only to outputs/W7/release/.
Channels:
  A  structure (manifest columns, vocabulary, case_id <-> image pairing)
  B  image leakage (PNG info keys; DICOM is not part of the release, see report)
  C  text leakage (identifier regex over all 7,695 reports)
"""
import csv
import json
import random
import re
from pathlib import Path

from PIL import Image

W7 = Path(r"e:\vetpets\outputs\W7")
OUT = W7 / "release"
CASES = Path(r"e:\vetpets\outputs\W4\data\full_cases_7695.csv")
REPORTS = Path(r"e:\vetpets\outputs\W4\final\reports.jsonl")
IMAGES = Path(r"e:\vetpets\data\images")

VOCAB = ["NOF", "CMG", "ALV", "BRC", "PLE", "MAS", "INT", "PTX", "PLM", "MGE",
         "FB", "HRN", "TRC", "DPH", "FRX", "PMD", "PDR", "CFR"]
SEED = 20261113  # frozen before sampling
N_SAMPLE = 770

PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "phone_intl": re.compile(r"\+\d{1,3}[\s-]?\d{6,}"),
    "phone_local": re.compile(r"\(\d{3}\)\s?\d{3}[- ]\d{4}|\b\d{3}[-.]\d{3}[-.]\d{4}\b"),
    "mrn": re.compile(r"\b(?:MRN|medical record|record no|case no|patient id|chart no)\b\s*[:#]?\s*\w+", re.I),
    "owner": re.compile(r"\b(?:owner|owned by|belongs to|pet name)\b", re.I),
    "title_name": re.compile(r"\b(?:Mr|Mrs|Ms|Dr)\.?\s+[A-Z][a-z]+"),
    "id_number": re.compile(r"\b[A-Z]{1,3}[- ]?\d{5,}\b"),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cases = list(csv.DictReader(open(CASES, encoding="utf-8")))
    reports = {}
    for line in open(REPORTS, encoding="utf-8"):
        r = json.loads(line)
        reports[r["case_id"]] = r

    # ---- release manifest (4 columns only) --------------------------------
    manifest_rows = []
    for c in cases:
        gt = c["gt_labels"]
        if gt != "NOF" and "NOF" in gt.split("|"):
            gt = "|".join(x for x in gt.split("|") if x != "NOF")
        manifest_rows.append({
            "case_id": c["case_id"],
            "species": c["species"],
            "projection": c["projection"],
            "gt_labels": gt,
        })
    mp = OUT / "manifest_7695.csv"
    with open(mp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["case_id", "species", "projection", "gt_labels"])
        w.writeheader()
        w.writerows(manifest_rows)

    # ---- channel A: structure ---------------------------------------------
    ids = [r["case_id"] for r in manifest_rows]
    a_bad = []
    for r in manifest_rows:
        problems = []
        if not r["case_id"] or not r["species"] or not r["projection"] or not r["gt_labels"]:
            problems.append("empty_field")
        if any(g not in VOCAB for g in r["gt_labels"].split("|")):
            problems.append("vocab")
        if not ((IMAGES / (r.get("case_id") + ".png")).exists()):
            pass  # images are keyed by stem, not case_id; pairing checked below
        if problems:
            a_bad.append((r["case_id"], problems))

    stems = {p.stem for p in IMAGES.glob("*.png")}
    name_by_case = {c["case_id"]: Path(c["filename"]).stem for c in cases}
    missing = [cid for cid, stem in name_by_case.items() if stem not in stems]

    # ---- channel C: text identifiers (full 7,695) --------------------------
    c_hits = {k: [] for k in PATTERNS}
    for cid, r in reports.items():
        content = r["content"]
        text = " ".join(str(v) for v in content.values()) if isinstance(content, dict) else str(content)
        for name, pat in PATTERNS.items():
            m = pat.search(text)
            if m:
                c_hits[name].append({"case_id": cid, "match": m.group(0)[:60]})

    # ---- 770-case sample ---------------------------------------------------
    rng = random.Random(SEED)
    sample = rng.sample([r["case_id"] for r in manifest_rows], N_SAMPLE)
    by_id = {r["case_id"]: r for r in manifest_rows}
    log = []
    b_bad = []
    for cid in sample:
        row = by_id[cid]
        img = IMAGES / (name_by_case[cid] + ".png")
        info = dict(Image.open(img).info) if img.exists() else None
        ok = img.exists() and set(info or {}) <= {"dpi"}
        if not ok:
            b_bad.append({"case_id": cid, "exists": img.exists(), "info": info})
        log.append({
            "row": len(log) + 1,
            "case_id": cid,
            "artifact": "png",
            "field": "PNG.info",
            "action": "kept" if ok else "flagged",
            "pre_value_present": bool(info),
            "post_value_present": bool(info),
            "checker": "channel_a_b",
            "seed": SEED,
            "timestamp": "2026-11-13",
        })

    summary = {
        "schema": "W7_B3_RELEASE_REPORT",
        "ticket": "W7-REL-001",
        "date": "2026-11-13",
        "seed": SEED,
        "n_cases": len(manifest_rows),
        "manifest_sha_source": str(mp),
        "channel_a": {
            "empty_or_vocab_errors": a_bad,
            "case_id_unique": len(set(ids)) == len(ids),
            "image_missing": len(missing),
            "image_missing_examples": missing[:5],
        },
        "channel_b": {
            "n_sampled": len(sample),
            "png_info_noncompliant": b_bad,
            "note": "DICOM is not part of the release; file-level DICOM scrub runs at export only if B4 publishes DICOM",
        },
        "channel_c": {
            "n_scanned": len(reports),
            "hits": {k: len(v) for k, v in c_hits.items()},
            "samples": {k: v[:3] for k, v in c_hits.items() if v},
            "note": "human review of the 110-case subset remains a manual step",
        },
        "overall_pass": not a_bad and not missing and not b_bad and not any(c_hits.values()),
    }

    with open(OUT / "redaction_log.jsonl", "w", encoding="utf-8") as f:
        for row in log:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(OUT / "b3_report.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)

    print("manifest rows:", len(manifest_rows))
    print("channel A bad:", len(a_bad), "missing images:", len(missing))
    print("channel B sampled:", len(sample), "noncompliant:", len(b_bad))
    print("channel C hits:", {k: len(v) for k, v in c_hits.items()})
    print("overall_pass:", summary["overall_pass"])


if __name__ == "__main__":
    main()
