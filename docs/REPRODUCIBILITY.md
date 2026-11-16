# Reproducibility notes

Release: **W7-VetXRay-Report** v1.0.0 (2026-11-13) · reserved DOI `10.5281/zenodo.24200927`

This page tells a verifier what can be checked from the release alone, what cannot, and what to change before running the three included build scripts.

## 1. What is checkable from the release alone

| Check | How |
|---|---|
| File integrity | `sha256sum` each file, compare with `RELEASE_MANIFEST.md` |
| Bundle integrity | three volumes, each ≤ 10 GB; compare with `RELEASE_MANIFEST.md` |
| Manifest structure | `manifest_7695.csv`: 7,695 rows, 4 columns (`case_id`, `species`, `projection`, `gt_labels`) |
| Image ↔ case pairing | every archive member is named `<case_id>.png`; the 7,695 names are exactly the 7,695 `case_id` values in the manifest (1:1, no mapping table needed) |
| Report coverage | `reports_7695.jsonl`: 7,695 lines, one `case_id` each, matching the manifest |
| Redaction sampling | `redaction_log.jsonl`: 770 rows, `action` ∈ {`kept`, `flagged`}, no original values |
| Evaluation arithmetic | `replay_v11_result.json` recomputes the reported agreement figures from `replay_v11.py` |

## 2. What cannot be reproduced from the release alone

`replay_v11.py`, `build_release_b3.py` and `build_bundles.py` are published as **audit artifacts**, not as a one-command reproduction pipeline. Their inputs are sealed and are **not** part of this release:

| Script | Sealed inputs |
|---|---|
| `replay_v11.py` | blind-review packet, answer key, human scores, adjudication register |
| `build_release_b3.py` | case master table (contains `patient_id` and source file names), full report set, source images |
| `build_bundles.py` | case master table, source image directory |

Those inputs are retained internally for audit and can be provided to a verifier under a data-use agreement. They are withheld because they contain subject-level identifiers or evaluation material whose publication would compromise the design (see the release brief).

## 3. Adapting the scripts

The scripts contain local absolute paths as module-level constants. Script bodies are **not** modified (their SHA256 values are registered in the manifest); a verifier adapting them should change only the constants below.

| Script | Constant (line) | Meaning |
|---|---|---|
| `replay_v11.py` | `BASE` (18) | directory of the sealed review inputs |
| `replay_v11.py` | `OUT` (19) | output directory for the recomputation result |
| `build_release_b3.py` | `W7` (18) | output root |
| `build_release_b3.py` | `CASES` (20) / `REPORTS` (21) / `IMAGES` (22) | sealed inputs |
| `build_bundles.py` | `ROOT` (14) | project root; `CASES`, `IMGDIR`, `OUTDIR` derive from it |

`build_bundles.py` is the only script that needs no sealed table beyond the case master: the images themselves are published, so a verifier holding the case master can rebuild the three volumes byte-for-byte and confirm the registered SHA256 values.

## 4. Environment

Python 3 with `pandas` and `Pillow`; archives are written with the standard-library `zipfile` in `ZIP_STORED` mode (images are already compressed), so bundle bytes depend only on input order and member names, both of which are fixed by `build_bundles.py`.
