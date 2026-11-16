# MANUAL_REVIEW_110_PROTOCOL — 执行版

- 工单：`W7-REL-001`｜关联阶段：C8 前置｜规程签发：2026-11-13（裁决方 `MANUAL_REVIEW_110_protocol`）
- 本文件是签发规程的**执行版**（路径、字段、判异流程落地）；不改变规程的任何判定
- 记录表：[manual_review_110.csv](file:///e:/vetpets/outputs/W7/manual_review/manual_review_110.csv)（110 行空表，行序 = 盲评包行序）

---

## 1｜性质：输入边界实证核验，不是找错练习

7,695 份报告由 **GT 标签条件**生成，prompt 从未包含 `patient_id`、动物名、日期、联系方式（claim §2/§3 冻结在案）。因此文本中一旦出现具体标识符，唯一解释是**生成管线被污染**。

regex 抓结构模式（电话格式、MRN 形态），人抓语义标识（"Bella's owner"、"at our clinic last Tuesday"）。**期望结果 110/110 CLEAN**——零命中是可信的，因为输入边界决定了标识符无从进入。

## 2｜材料

| 用途 | 文件 | 纪律 |
|---|---|---|
| 阅读 | `outputs/W6/review/packet_full_bilingual.md` | **只审英文原文**；中文对照是内部助读件，不发布、不进审 |
| 记录 | `outputs/W7/manual_review/manual_review_110.csv` | 逐例一行，不复用他人的行 |
| 汇总 | `outputs/W7/manual_review/manual_review_110_result.json` | 复核完成后由执行方生成 |

## 3｜记录表字段

| 列 | 取值 |
|---|---|
| `case_id` | 已预填（`R-001`…，与包内 `packet_id` 一致） |
| `verdict` | `CLEAN` / `HIT` / `UNCLEAR` |
| `hit_category` | 见 §4 代码；`CLEAN` 留空 |
| `hit_span` | **英文原句逐字**（不得改写、不得翻译）；`CLEAN` 留空 |
| `reviewer` | 复核人标识（自定缩写） |
| `session` | `1` / `2` / `3` |
| `date` | `YYYY-MM-DD` |
| `notes` | 可选；`UNCLEAR` 必填判断理由 |

## 4｜8 类检查清单（兽医适配）

| # | 代码 | 类别 | 典型形态 |
|---|---|---|---|
| 1 | `NAME_PERSON` | 人名 / 所有者名 | "Mr. Smith"、"Bella's owner said…" |
| 2 | `NAME_ANIMAL` | 动物名 | "Bella is a 9-year-old MN Labrador…" |
| 3 | `CONTACT` | 联系方式 | 电话、邮箱、诊所 URL（指向公共学术资源的 URL 不算） |
| 4 | `RECORD_ID` | 病历 / 编号类 | MRN、case 序号、accession 号 |
| 5 | `DATE` | 精确日期 | 绝对月日、出生日期（"today"/"this examination" 等相对语不算） |
| 6 | `GEO_ORG` | 地理 / 机构 | 城市、街道、诊所 / 医院 / 大学名称 |
| 7 | `DEVICE` | 设备指纹 | 序列号、软件版本号 |
| 8 | `OTHER` | 兜底 | 其他可指认个人的信息 |

**非 hit（预授权，不必回报）**：相对时间语、泛指（the patient / today / this study）；指向公共学术或名词资源的 URL。

## 5｜预授权处置表

| 发现 | 处置 |
|---|---|
| 相对时间语、泛指 | 非 hit |
| 公共学术 / 名词资源 URL | 非 hit |
| 1–7 类任一**具体**标识符 | **STOP → 立即回报裁决方**（管线污染嫌疑，不是例行脱敏） |
| `UNCLEAR`（如 "the referring veterinarian" 无名泛指） | 记录，**批末汇总**上报，不在批中打断 |
| ≥3 个具体 hit | **全批 STOP** → 生成管线溯源复查，不止个案问题 |

## 6｜逐例流程（45–70 秒/例）

1. 读英文报告全文（中文对照仅供理解）。
2. 对照 §4 的 8 类扫一遍。
3. 填一行：`verdict` → `hit_category` → `hit_span` → `session` → `date`（`reviewer` 可在首行填好后复制）。
4. 下一例。

**分 3 段**（注意力衰减是漏检头号原因，总时长约 2 小时）：

| session | 行号 | 例数 | 建议时长 |
|---|---|---|---|
| 1 | 1–37 | 37 | ~40 min |
| 2 | 38–74 | 37 | ~40 min |
| 3 | 75–110 | 36 | ~40 min |

段间至少休息 10 分钟；**不要连续跨段作业**。

## 7｜产物纪律（冻结件零改动）

- 复核产物**全部落新文件**：`manual_review_110.csv`、`manual_review_110_result.json`。
- **禁改**：`release/redaction_log.jsonl`（`39bafc4f…`）、`release/b3_report.json`（`2c67e343…`）、`C5_FREEZE_MANIFEST.md`（`3421faab…`）。
- 新件经 CHANGELOG 注册 SHA；C5 引用以 **addendum 文件**追加（`C5_ADDENDUM_01.md`），冻结本体不动。
- `packet_full_bilingual.md`、`packet_full.json` 只读，复核中不得修改。

## 8｜必需回报裁决方的三种情形

1. 任一 1–7 类具体标识符（STOP）。
2. 累计 ≥3 个具体 hit（全批 STOP）。
3. `UNCLEAR` 批末汇总（附 case_id 与理由，待裁）。

其余情况按 §5 自行处置，写入 CSV 即可。

## 9｜完成后执行方产出

| 产物 | 内容 |
|---|---|
| `manual_review_110_result.json` | 总例数 / CLEAN / HIT / UNCLEAR 计数；按类别计数；session 分布；结论 `PASS`（全 CLEAN）或 `HOLD`（有 hit/uncertain 待裁）；引用 CSV SHA |
| C8 card 句 | 110/110 CLEAN → 照签发文本逐字："Manual review of all 110 evaluation texts: zero identifiers found; automated regex scan of 7,695 texts across seven categories: zero hits."；有经处置 hit → 改写并附计数与处置引用 |
| `C5_ADDENDUM_01.md` | 登记 CSV 终版、result.json、本规程 SHA |
| CHANGELOG | 上述 SHA + 结论 + 验收状态 |
| 论文证据句 | "Generation-input boundary verified by manual review of all 110 texts"（仅当 110/110 CLEAN） |

## 10｜验收标准

- `110/110 CLEAN` → C8 通过，card 使用签发句。
- 存在经处置的 hit → 同句改写 + 附计数与处置引用，且需裁决方确认后方可发布。
- CSV 行数 = 110、`case_id` 与包内 `packet_id` 一一对应、无空 `verdict` → 否则视为未完成。
