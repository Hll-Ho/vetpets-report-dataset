status: dormant — pending HF access

# Dataset Card — W7-VetXRay-Report

> **Status: dormant.** This card is prepared but not published to the Hugging Face Hub. Network access to `huggingface.co` is not available from the release environment (verified 2026-11-12). Nothing here is a pending obligation: the canonical release is the Zenodo record ([10.5281/zenodo.24200927](https://doi.org/10.5281/zenodo.24200927)) plus this repository. If HF access becomes available, this card can be published as-is; see "Path to publication" at the bottom.

## Dataset Summary

7,695 veterinary thoracic-radiograph cases, each pairing one image with a **model-generated** radiology-style report. Reports were conditioned **only on the ground-truth label set** (plus species and projection), **never on the image**. The dataset contains **no original clinical reports** and **no reference reports** (reference-report coverage = 0).

Companion to the canonical record: Zenodo DOI [10.5281/zenodo.24200927](https://doi.org/10.5281/zenodo.24200927), code at [github.com/Hll-Ho/vetpets-report-dataset](https://github.com/Hll-Ho/vetpets-report-dataset).

### Composition

- Projections: LL 4,459 / DV 2,431 / VD 805
- Species: dog 5,998 / cat 1,659 (main fold 7,657); 33 `unknown` and 5 `other` cases form a 38-case supplementary fold
- Labels per case: 1 → 6,324; 2 → 1,222; 3 → 133; 4 → 16
- 18-class vocabulary = 17 upstream finding categories + explicit `no_finding`

`no_finding` denotes absence of annotation in the source record, not verified normalcy. The 33 `unknown` / 5 `other` values are species annotations, not missing label sets.

### Generation protocol

GLM-5.3-Flash, temperature 0.3, top-p 1.0, max-tokens 2,000, frozen prompt v1.2 (SHA256 `0945b813…`). Input: case identifier, species, projection, ground-truth labels. No image input. Reports describe labels, not pixels.

## De-identification

All 7,695 report texts were screened automatically across seven identifier categories with zero hits; the 110-case scored subset additionally underwent full manual review across eight identifier categories, also with zero identifiers found. DICOM headers were replaced or removed, image file names were replaced with case identifiers, and manifest fields are limited to case identifier, species, projection and labels.

Pixel-level burned-in annotation screening was limited to a 50-image visual spot check; no full-pass OCR was performed.

## Evaluation readout

- Pre-registered primary readout: **76/110 = 69.09%** raw agreement, Cohen's κ = 0.3750. The pre-registered 80% threshold was **not met**.
- Post-adjudication consensus agreement: **101/110 = 91.82%** (κ = 0.8359); unique-100 basis **91/100 = 91.00%**. Reported with its 34-case adjudication breakdown (human_under_flag 24, judge_over_flag 8, rubric_ambiguity 1, judge_missed 1). This is descriptive only and is **not a gate pass**.

## Intended use

Benchmarking text-level clinical correctness of report-generation systems; rubric research; error-taxonomy development.

**Not intended for** clinical decision support, diagnosis, triage, or any patient-care use. Synthetic, label-derived text; no regulatory clearance; not a diagnostic device.

## Limitations

No reference reports; label-conditioned generation means no causal path between text and image; single projection only; six non-evaluable classes excluded from scoring; three research-tier classes may be omitted; species coverage mainly dogs and cats; ground-truth labels inherit source annotations without clinical re-review; the human-scored subset is 110 cases (95 dogs / 15 cats) with wide confidence intervals.

## Licensing

- Dataset (images, labels, reports, manifest, evaluation artifacts): **CC BY 4.0**
- Code: **MIT**

## Attribution

Contains data from: Banzato, Tommaso; Burti, Silvia; Zotti, Alessandro; Wodzinski, Marek, *VetXRay – A Dataset of 9,882 Manually Annotated Canine and Feline Thoracic Radiographs with Lesion and Image Quality Annotations*, Zenodo, DOI 10.5281/zenodo.19051776 (version published 2026-03-17; concept DOI 10.5281/zenodo.18999729), licensed under CC BY 4.0.

Images were re-encoded to PNG from the upstream DICOM distribution with all DICOM headers stripped for de-identification; modifications are noted per CC BY 4.0 §3(a). The 7,695 images released here are a subset of the 9,882 annotated radiographs in the upstream record (40.8 GB of source archives); this is not a full mirror. Auxiliary files are MD5-verified against the upstream record.

## Path to publication (if HF access becomes available)

1. Upload the 16 image chunks plus `reports_7695.jsonl` and `manifest_7695.csv` (payload list: `docs/RELEASE_MANIFEST.md` in the code repository).
2. Create the dataset repo with a dedicated, short-lived write token; revoke it immediately afterwards.
3. Use the Hub's official endpoint. Uploading through a mirror proxy is **not** acceptable for authenticated writes: a write token passing through a third-party relay is a credential exposure, regardless of the relay's convenience for public downloads.
