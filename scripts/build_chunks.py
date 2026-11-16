"""把 7,695 张发布 PNG 重新分卷为 16 个各约 1 GB 的独立 zip（可单独解压，无需拼接）。"""
import csv
import hashlib
import json
import os
import zipfile

W7 = r"e:\vetpets\outputs\W7"
MANIFEST = os.path.join(W7, "release", "manifest_7695.csv")
CASES = r"e:\vetpets\outputs\W4\data\full_cases_7695.csv"
IMAGES = r"e:\vetpets\data\images"
OUT = os.path.join(W7, "release", "chunks")
TARGET = 1_000_000_000
N_CHUNKS = 16

os.makedirs(OUT, exist_ok=True)

rows = list(csv.DictReader(open(MANIFEST, encoding="utf-8")))
name_map = {r["case_id"]: r["filename"] for r in csv.DictReader(open(CASES, encoding="utf-8"))}
sizes = {}
for r in rows:
    p = os.path.join(IMAGES, name_map[r["case_id"]])
    sizes[r["case_id"]] = os.path.getsize(p)

total = sum(sizes.values())
target = -(-total // N_CHUNKS)  # 均分，向上取整
print("total", total, "target_per_chunk", target)

chunks, cur, cur_bytes = [], [], 0
for r in rows:
    cid = r["case_id"]
    sz = sizes[cid]
    if cur and cur_bytes + sz > target and len(chunks) < N_CHUNKS - 1:
        chunks.append(cur)
        cur, cur_bytes = [], 0
    cur.append(cid)
    cur_bytes += sz
chunks.append(cur)
print("chunks", len(chunks), [len(c) for c in chunks])

index = []
for i, ids in enumerate(chunks, 1):
    name = f"W7-VetXRay-Report_images_chunk{i:02d}.zip"
    path = os.path.join(OUT, name)
    h = hashlib.sha256()
    with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED, allowZip64=True) as z:
        for cid in ids:
            p = os.path.join(IMAGES, name_map[cid])
            z.write(p, arcname=f"{cid}.png")
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(8 << 20), b""):
            h.update(b)
    index.append({"bundle": name, "first_case": ids[0], "last_case": ids[-1],
                  "n_cases": len(ids), "bytes": os.path.getsize(path),
                  "sha256": h.hexdigest()})
    print(name, len(ids), ids[0], "->", ids[-1], os.path.getsize(path), h.hexdigest()[:12])

summary = {"scheme": "16 independent zip chunks, ZIP_STORED, arcname=<case_id>.png",
           "n_chunks": len(index), "n_cases": sum(x["n_cases"] for x in index),
           "total_bytes": sum(x["bytes"] for x in index), "chunks": index}
json.dump(summary, open(os.path.join(W7, "release", "bundle_index.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("index_written", os.path.getsize(os.path.join(W7, "release", "bundle_index.json")))
