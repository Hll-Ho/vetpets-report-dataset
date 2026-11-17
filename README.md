# vetpets-report-dataset

Companion repository for **W7-VetXRay-Report**: 7,695 de-identified veterinary thoracic radiographs (PNG) with label-conditioned, model-generated radiology reports, plus the full evaluation artifact chain.

**Dataset DOI:** [10.5281/zenodo.24200927](https://doi.org/10.5281/zenodo.24200927)

## What is in this repository

| Path | Content |
|---|---|
| `docs/RELEASE_MANIFEST.md` | Every published file with byte size and SHA256 |
| `docs/REPRODUCIBILITY.md` | What can and cannot be reproduced, and how to adapt the scripts |
| `docs/manifest_7695.csv` | `case_id`, species, projection, ground-truth labels (7,695 rows) |
| `docs/bundle_index.json` | Image chunk → case range mapping, with per-chunk SHA256 |
| `docs/redaction_log.jsonl` | Per-case redaction decisions for the 770-case audit sample |
| `docs/rubric_GREEN_VET_v1.1.md` | Frozen report-quality rubric (error taxonomy, direction rules) |
| `docs/DADJ_ERRATA_REGISTER.md` | Adjudication disagreement register, with corrections |
| `docs/CLAIM_W7.md` | Claim text and prohibited-phrase table |
| `docs/RIGHTS_AND_RELEASE_BRIEF_W7.md` | Licensing basis and release scope |
| `docs/MANUAL_REVIEW_110_PROTOCOL.md`, `manual_review_110.csv`, `manual_review_110_result.json` | De-identification manual review of all 110 evaluation texts |
| `docs/b3_report.json`, `vp1_result.json`, `replay_v11_result.json` | Verification outputs |
| `scripts/` | Build and replay scripts (MIT) |

Dataset payload (images, report texts) is hosted on Zenodo and is not duplicated here.

## Usage

Download `reports_7695.jsonl` and `manifest_7695.csv` from the [Zenodo record](https://doi.org/10.5281/zenodo.24200927), then load the reports without any hub dependency:

```python
from datasets import load_dataset

ds = load_dataset("json", data_files="reports_7695.jsonl", split="train")
print(ds[0]["case_id"], ds[0]["content"]["report_findings"])
```

Image chunks are independent ZIP archives of `<case_id>.png`; join them to the manifest on `case_id`:

```python
import zipfile, pandas as pd

manifest = pd.read_csv("manifest_7695.csv")          # case_id, species, projection, gt_labels
with zipfile.ZipFile("W7-VetXRay-Report_images_chunk01.zip") as z:
    with z.open("W4-00001.png") as f:
        png_bytes = f.read()
```

## Composition

- 7,695 cases · projections LL 4,459 / DV 2,431 / VD 805
- Species: dog 5,998 · cat 1,659 · unknown 33 · other 5
- Labels per case: 1 → 6,324 · 2 → 1,222 · 3 → 133 · 4 → 16

Reports were generated from **ground-truth labels only** (never from images), with a fixed prompt (`prompt v1.2`, SHA256 `0945b813…`), temperature 0.3, top-p 1.0, max 2,000 tokens. Reports are model output and are not clinical records.

## Evaluation readout

Pre-registered primary readout: raw agreement between the model judge and human reviewers was **76/110 = 69.09%** (Cohen's κ = 0.3750). The pre-registered 80% threshold was **not met**.

Post-adjudication consensus agreement is **101/110 = 91.82%** (κ = 0.8359); on the 100 unique cases it is **91/100 = 91.00%**. This figure is descriptive only, is reported alongside its 34-case adjudication breakdown, and is **not a gate pass**.

## Licensing

- **Dataset artifacts** (images, reports, manifests, rubric, documentation): CC BY 4.0.
- **Code in `scripts/`**: MIT.

## Upstream attribution

Contains data derived from: Banzato, T., Burti, S., Zotti, A., & Wodzinski, M., *VetXRay – A Dataset of 9,882 Manually Annotated Canine and Feline Thoracic Radiographs with Lesion and Image Quality Annotations*, Zenodo, DOI 10.5281/zenodo.19051776 (concept DOI 10.5281/zenodo.18999729), licensed under CC BY 4.0.

Images were re-encoded to PNG from the upstream DICOM distribution, all DICOM headers were stripped, and file names were replaced with case identifiers before release; modifications are noted per CC BY 4.0 §3(a). The 7,695 images released here are a subset of the 9,882 annotated radiographs in the upstream record (40.8 GB of source archives); this is not a full mirror.

## Intended use and limits

Intended for evaluation of report generation, hallucination detection, and de-identification methods. Not for diagnosis, triage, or any clinical decision. The dataset carries no clinical labels beyond the upstream annotations, and pixel-level burned-in annotation screening was limited to a 50-image visual spot check.
