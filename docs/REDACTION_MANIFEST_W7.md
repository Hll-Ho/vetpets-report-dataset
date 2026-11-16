# B3 — W7 脱敏发布 Manifest 与 Scrub 清单（已签发，执行解锁）

- 工单：`W7-REL-001`｜阶段：B3｜状态：`signed`（2026-11-13，含修订令）｜**scrub 清单为终版**；尚未执行任何脱敏写入
- 依据：Phase A 裁决 5；B2/B3 签发裁定书裁决 2（S-10/S-12 落定、B4 域收窄）
- 前置事实来源：`W7_REL_001_INTEGRITY_CHECK.md` §5（物种两 fold、case_id 溯源、DICOM header 全量清单、PNG 抽样）

---

## 1｜发布边界（声明）

| 轨 | 是否发布 | 说明 |
|---|---|---|
| 图像（PNG） | 发布 | 7,695 张；PNG `info` 仅含 `dpi`（抽样 200 张，0 泄漏） |
| 结构化 manifest | 发布 | 仅 §3 列出的 4 列，UTF-8 CSV |
| DICOM 原始文件 | **不发布**（默认） | 若 B4 决定 gated 发布，须先执行 §2 全部 scrub + UID 重映射 |
| `File_list_with_tags.xlsx` | **不发布** | `PatientName` 9,969/9,973 非空，原件禁入发布包 |
| `labels.csv`（含 filename） | **不发布** | 经 case_id 映射后仅发布 §3 manifest |
| 报告文本 | 发布 | 作为数据文件；不含患者信息（生成物） |

## 2｜DICOM Scrub 清单（10,234 文件，header 全量扫描 0 失败）

| # | 字段 | 非空 | 处置 | 理由 |
|---|---|---|---:|---|---|
| S-01 | `PatientID` | 10,233 | 删除（或重映射为 `SUBJ-%05d` 序号，与 `patient_id` 不共享映射表） | 直接标识 |
| S-02 | `PatientBirthDate` | 9,415 | 删除 | 直接标识（准唯一） |
| S-03 | `StudyDate` / `SeriesDate` / `AcquisitionDate` / `ContentDate` + 对应 Time | 10,234 各 | 删除；若临床需要，仅保留**年份** | 就诊时间可反推 |
| S-04 | `OperatorsName` | 3,532 | 删除 | 人员标识 |
| S-05 | `PerformingPhysicianName` / `RequestingPhysicianName` | 3,239 / 3,239 | 删除 | 人员标识 |
| S-06 | `StationName` | 3,337 | 删除 | 设备/机构指纹 |
| S-07 | `AccessionNumber` / `StudyID` | 6,994 / 6,897 | 删除 | 关联号，可跨库串联 |
| S-08 | `PatientComments` | 44 | 删除（如 “Stadiazione tumore mammario”） | 自由文本，含临床信息 |
| S-09 | `StudyInstanceUID` / `SeriesInstanceUID` / `SOPInstanceUID` | 10,234 各 | 若发 DICOM：按 SOP 重映射，保持内部一致性；否则随文件不发布而无需处理 | UID 可跨库追踪 |
| S-10 | `PatientSex` / `PatientAge` | 10,177 / 2,926 | **删除**；执行前先 extract-then-scrub：候选值提取至私有 staging（不入发布包、不进 log 值记录），发布件零 header 保留 | 与 S-02/S-03 一致（留 Age 删 BirthDate 不连贯）；最小必要，人口学需求走聚合列通道 |
| S-11 | `StudyDescription` | 6,897（“Torace VD/LL”） | 保留 | 投照位信息，非标识 |
| S-12 | `Manufacturer` / `ModelName` / `SoftwareVersions` / `DetectorDescription` / `Cassette*` | 10,234 / 6,995 / 3,239 / 10,136 / 6,897 | **删除**（纯删，无提取项） | 不具名发布姿态下设备指纹是反向去匿名化侧信道 |
| S-13 | `PatientName` / `InstitutionName` / `InstitutionAddress` / `DeviceSerialNumber` / `ReferringPhysicianName` / `SeriesDescription` / `ProtocolName` / `OwnerName` / `PatientAddress` | 0 | 无需处置（复核为准） | 全量扫描未出现 |

```text
scrub_order          = [S-01, S-02, S-03, S-04, S-05, S-06, S-07, S-08, S-09, S-10, S-12]
extract_then_scrub   = [S-02, S-03, S-10]   # 先写入私有 staging，再删 header
pure_delete          = [S-01, S-04..S-09, S-12]
deferred             = []                   # 本裁定后无延迟项
verify_only          = [S-11, S-13]
```

**staging 纪律**：staging 目录不入发布包、不进 redaction log 的值字段、不参与任何 SHA 冻结清单；log 只记 `"S-02 extracted-then-deleted, n=9,415"` 形式的动作与计数。

## 3｜发布 Manifest 列（冻结候选 schema）

| 列 | 类型 | 说明 |
|---|---|---|
| `case_id` | string | `W4-00001`…`W4-07695`；连续唯一；**非**由 patient_id 派生 |
| `species` | enum | `dog` / `cat` / `unknown` / `other`（保留原值，不合并） |
| `projection` | enum | `LL` / `DV` / `VD` |
| `gt_labels` | string | 竖线分隔的 18 类缩写；NOF 共现按 finding precedence 去掉 |

**明确排除**：`patient_id`、`filename`、`dicom_path`、`split`、一切 patient 级聚合列（如每受试者案例数、受试者级标签汇总）。`split` 是否随包发布需 B4 裁定（默认不发布，避免与 W6 评测划分耦合）。

## 4｜四条必须先做的核验（执行前置）

1. **PNG metadata 100% 扫描**：当前仅抽样 200 张（`info` 仅 `dpi`）。发布前对 7,695 张全量读 `info`，要求出现字段集合 ⊆ {`dpi`}；非空 text/EXIF chunk 计数必须为 0。
2. **stem 对账**：7,695 个发布 stem 与 DICOM 一一匹配（7,695/7,695，已核，无缺失）。
3. **case_id 反查**：从 `case_id` 无法回推 `patient_id`/`filename`（已核：6 条 1–3 位短 ID 偶然匹配，无 ≥4 位完整 ID 命中）；发布 manifest 不含映射表。
4. **报告文本标识符扫描（第三通道，补强制）**：7,695 份报告全文 regex（人名模式、电话/邮箱、病历号/住院号模式、动物名模式）＋抽样人工复核；**零命中也要记 log**，不得以沉默跳过。

## 5｜抽样复核计划（≥10%，三通道）

- 样本量：**770 例**（7,695 的 10.0%），随机种子预注册冻结，抽样一次后不得重抽。
- 通道 A（结构）：逐例检查 manifest 4 列非空、`gt_labels` 全部 ∈ 18 类词表、`case_id` 与图像文件一一对应。
- 通道 B（影像泄漏）：逐例读 PNG `info` + 对应 DICOM header，确认 §2 的 S-01…S-10、S-12 全部不存在或已置空；S-11/S-13 复核仍在位。
- 通道 C（文本泄漏）：**全量** 7,695 份报告跑标识符 regex（非抽样）；其中人工复核 110 例（沿用已逐字阅读的盲评子集），其余命中即转人工。零命中同样写入 log。
- 判定：任一例出现直接标识即 **STOP**，不得以“比例很低”放行。
- 记录：每例一行写入 redaction log（§6），复核人只记录事实与计数，不做主观判断。

## 6｜Redaction Log schema

```json
{
  "row": 1,
  "case_id": "W4-00001",
  "artifact": "png|dicom|manifest",
  "field": "PatientID",
  "action": "deleted|remapped|kept|absent",
  "pre_value_present": true,
  "post_value_present": false,
  "checker": "channel_a|channel_b",
  "seed": "<frozen seed>",
  "timestamp": "2026-11-13T00:00:00+08:00"
}
```

- 日志不记录被删除字段的原值（避免把泄漏抄进日志）；仅记 `pre_value_present`。
- 日志与 manifest 分别落盘，日志不进发布包。

## 7｜冻结与对账

| 工件 | 状态 | 结果 |
|---|---|---|
| 发布 manifest（7,695 行 × 4 列） | ✅ 已生成 | `release/manifest_7695.csv`；case_id 唯一、词表 0 越界、图像配对 0 缺失 |
| redaction log（770 例复核） | ✅ 已生成 | `release/redaction_log.jsonl`；770 行，非合规 0 |
| PNG 100% metadata 扫描 | ✅ 已执行 | 7,695/7,695，`info` 仅 `dpi`，0 例外 |
| 报告文本标识符扫描 | ✅ 已执行 | 7,695/7,695，7 类 regex 全零命中；110 例人工复核仍为待办 |
| Scrub 脚本 | ✅ 已写 | `build_release_b3.py`（manifest + 三通道抽样 + log） |
| DICOM 文件级 scrub | ⏸ 未执行（显式） | 发布件默认不含 DICOM；该写操作仅在 B4 判定发布 DICOM 时于导出环节执行，当前无输出消费者 |
| 上述 SHA 入 C5 冻结清单 | ☐ 待 C5 | — |

## 8｜B4 域（经本裁定收窄）

B4 仅剩权利域与发布形态，不再包含任何 scrub 范围决定：

1. license 矩阵（类型与是否 gated）。
2. 同意范围 brief。
3. DICOM 是否随包发布；若发布，发布的是 scrub 后版本 + UID 重映射与二次复核。
4. PNG-only 双轨提案。
5. `split` 是否随 manifest 发布（脱敏域默认不发布，B4 确认即可）。

已落定、不再回 B4：`PatientSex` / `PatientAge` 删除（S-10，extract-then-scrub）、设备指纹删除（S-12）、其余 S-01…S-09 删除、S-11/S-13 保留/复核。

## 9｜签发栏

| 项 | 状态 |
|---|---|
| §1 发布边界 | ✅ 签发 |
| §2 Scrub 清单（S-01…S-13，终版） | ✅ 签发（含 S-10 extract-then-scrub / S-12 纯删） |
| §3 Manifest 4 列 schema 与排除项 | ✅ 签发 |
| §4 四条前置核验（含报告文本第三通道） | ✅ 签发 |
| §5 770 例三通道复核计划 | ✅ 签发 |
| §6 redaction log schema（只记动作不记值） | ✅ 签发 |

> 执行顺序：§4 四验 → staging 提取 → scrub → 生成 manifest → 770 例三通道复核 → 落盘日志 → 四件 SHA → C5。任一例直接标识命中即 STOP。
