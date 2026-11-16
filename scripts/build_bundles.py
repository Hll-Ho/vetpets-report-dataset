"""C7 分卷打包（V-P1 修复后）：PNG 以 case_id.png 入卷，ZIP_STORED，卷上限 10 GB。

输入：outputs/W4/data/full_cases_7695.csv（case_id, filename）
输出：outputs/W7/release/bundles/W7-VetXRay-Report_images_part{N}.zip + bundle_index.json

V-P1 结论：7,695/7,695 文件名与上游 xlsx 同源 → 全部改名 case_id.png（打包时写入，不复制中间体）。
"""
import csv
import hashlib
import json
import os
import zipfile

ROOT = r"e:\vetpets"
CASES = os.path.join(ROOT, r"outputs\W4\data\full_cases_7695.csv")
IMGDIR = os.path.join(ROOT, r"data\images")
OUTDIR = os.path.join(ROOT, r"outputs\W7\release\bundles")
VOL_BYTES = 8_000_000_000  # 累计未压缩字节上限，保证 zip ≤ 10 GB


def sha256(path, buf=8 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(buf)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    with open(CASES, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    vols = []
    idx = 0
    cur_zip = None
    cur_bytes = 0
    cur_count = 0
    cur_first = None
    cur_last = None
    missing = 0
    names = set()

    def close_vol():
        nonlocal cur_zip, cur_bytes, cur_count, cur_first, cur_last
        if cur_zip is None:
            return
        cur_zip.close()
        path = cur_zip.filename
        vols.append({
            "file": os.path.basename(path),
            "bytes": os.path.getsize(path),
            "uncompressed_bytes": cur_bytes,
            "count": cur_count,
            "first_case": cur_first,
            "last_case": cur_last,
            "sha256": sha256(path),
        })
        print(f"closed {os.path.basename(path)} count={cur_count} bytes={os.path.getsize(path)}", flush=True)
        cur_zip = None
        cur_bytes = 0
        cur_count = 0
        cur_first = None
        cur_last = None

    for r in rows:
        src = os.path.join(IMGDIR, r["filename"])
        if not os.path.exists(src):
            missing += 1
            continue
        arc = r["case_id"] + ".png"
        if arc in names:
            raise SystemExit("duplicate arcname: " + arc)
        names.add(arc)
        size = os.path.getsize(src)
        if cur_zip is None or cur_bytes + size > VOL_BYTES:
            close_vol()
            idx += 1
            cur_zip = zipfile.ZipFile(
                os.path.join(OUTDIR, f"W7-VetXRay-Report_images_part{idx:02d}.zip"),
                "w", zipfile.ZIP_STORED, allowZip64=True)
        if cur_first is None:
            cur_first = r["case_id"]
        cur_last = r["case_id"]
        cur_zip.write(src, arcname=arc)
        cur_bytes += size
        cur_count += 1

    close_vol()
    total = sum(v["bytes"] for v in vols)
    out = {
        "packing": "V-P1 fixed: arcname = case_id.png",
        "volume_limit_bytes": 10_000_000_000,
        "volumes": vols,
        "volume_count": len(vols),
        "total_zip_bytes": total,
        "cases_packed": sum(v["count"] for v in vols),
        "missing_sources": missing,
        "arcname_duplicates": 0,
    }
    with open(os.path.join(OUTDIR, "bundle_index.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
