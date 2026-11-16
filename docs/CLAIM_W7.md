# B2 — W7 发布 Claim（已签发）

- 工单：`W7-REL-001`｜阶段：B2｜状态：`signed`（2026-11-13 条件签发，三要素已落实）｜尚未用于任何公开页面
- 依据：Phase A 裁定 4；B2/B3 签发裁定书裁决 1；B1 rubric v1.1（SHA `fd7ede2d…`）已冻结
- 语言：英文为**拟发布文本**，中文为执行说明与依据；签发后英文段落原样进入 Zenodo / Hugging Face card 与论文

---

## 1｜数据集身份（拟发布表述）

> **W7-VetXRay-Report** is a **model-generated** thoracic-radiograph report dataset: 7,695 cases, each pairing a single radiographic projection with a synthetic radiology-style report produced by a large language model that was conditioned **only on the ground-truth label set** (plus species and projection), **not on the image**. It contains **no original clinical reports** and **no reference reports** (reference-report coverage = 0). Ground truth comes from the source VetXRay label set (18 classes).

中文说明：三处不可省略——`model-generated`、`label-conditioned (not image-conditioned)`、`no reference reports`。任何对外文本删去其一即视为 claim 漂移。

## 2｜规模与构成（已核）

| 项 | 数值 | 来源 |
|---|---|---|
| 发布案例 | 7,695 | `full_cases_7695.csv` |
| 来源影像 | 9,973（本地副本）；DICOM 池 10,234 文件全量 header 扫描 0 失败 | W1 manifest / 完整性检查 §5.3 |
| 受试者 | 3,218 个 `patient_id`（不发布） | `full_cases_7695.csv` |
| 投影 | LL 4,459 / DV 2,431 / VD 805 | 同上 |
| 物种（主 fold 7,657） | dog 5,998；cat 1,659（含 felina 8 归一） | 同上 |
| 物种（补充 fold 38） | 未标注 33；其他物种 5（猪 3、野兔 2） | 同上 |
| 标签数分布 | 1 类 6,324 / 2 类 1,222 / 3 类 133 / 4 类 16 | 同上 |
| 单投影 | 每例仅 1 个投照位 | 同上 |

标签频次（发布集）：NOF 3,922、CMG 1,737、ALV 1,036、BRC 696、PLE 464、MAS 438、INT 392、PTX 161、PLM 124、MGE 105、FB 74、HRN 31、TRC 19、DPH 10、FRX 9、PMD 6、PDR 6、CFR 1。

## 3｜生成协议（必须与 card 一致）

| 项 | 值 |
|---|---|
| 生成模型 | GLM-5.3-Flash（`model-generated`） |
| 条件输入 | `case_id`（仅作行标识）、`species`、`projection`、`gt_labels` |
| 未发送字段 | 图像、图像特征、`patient_id`、原始报告 |
| 采样参数 | temperature 0.3；top_p 1.0；max_tokens 2,000 |
| prompt | `prompt_v1.2`（SHA `0945b813…`），含 “GT labels from data/labels.csv; predictions are out of scope” |
| 语言 | 英文报告文本（findings + impression） |

拟发布表述：

> Reports were generated with GLM-5.3-Flash at temperature 0.3, top-p 1.0, max-tokens 2,000, using a frozen prompt (v1.2) that receives only the case identifier, species, projection and the ground-truth label set. The image was never provided to the generator. Consequently the reports describe the **labels**, not the pixels; they are not reconstructions of any original report.

## 4｜真值与层级

- 18 类标签，分四层：trusted（NOF/CMG/ALV/PLE/PTX/FB）、marginal（BRC/MAS/PLM）、research（INT/MGE/HRN）、non-evaluable（TRC/DPH/FRX/PMD/PDR/CFR）。
- non-evaluable 类在单投影上不可靠评估，评分中的处置见 rubric v1.1 §2（V11-02），**不表示这些标签在源数据中无效**。
- NOF 为“无发现”标签；与其它类共现时按 finding precedence 去掉 NOF。

## 5｜评测协议与读数（双读数，禁语硬约束）

**定位（裁决 1）**：card 的 evaluation 章节以**错误族分解表**为核心科学内容；两个一致率只是它的两行汇总，不是卖点本身。

### 5.1 预注册主门：**未通过**

> The pre-registered primary gate was **not met**: agreement between model verdicts and adjudicated human verdicts on the 110-case human-scored subset was **76/110 (69.09%)**, Cohen's κ = **0.3750**, against a pre-registered threshold of 80%.

- 出处：`review_scores_normalized_v1_asSubmitted.json`（SHA `7f9fe015…`），只读快照。
- 公开文本只能写“未通过”，**不得**写“接近通过”“修正后通过”“门达标”。

### 5.2 并列读数：**三要素强制**（签发条件）

内部术语「协议修正读数」保留于 CHANGELOG / manifest，不改历史件；**公开英文只用 “post-adjudication consensus agreement”**，`protocol-corrected` **禁入任何公开文本**。

| 要素 | 强制要求 |
|---|---|
| ① 基数标注 | 任何公开一致率必须带基数（110 或 unique-100）；91.00% 与 91.82% 各自标注，不得互换混用 |
| ② 伴随限定语 | 91.82% 每次出现，同句或紧邻脚注必须带 “post-adjudication consensus — not a gate pass”；缺限定语的任何出现 = 终验不通过 |
| ③ 排序与位置 | 摘要与 card 头部**只允许**预注册读数（76/110 = 69.09%，κ = 0.3750，80% 门未过）＋错误族分解；91.82% **仅可**出现在 evaluation 章节，且必须携带完整分解并引用 W7 候选 v2 |

拟发布文本（仅限 evaluation 章节）：

> **Post-adjudication consensus agreement — not a gate pass.** After adjudicating 34 reviewer–judge disagreements (human_under_flag 24; judge_over_flag 8; rubric_ambiguity 1; judge_missed 1; direction adopted from the judge in 25 cases and from the human reviewer in 9), agreement between the judge and the adjudicated human verdicts is **101/110 (91.82%)**, κ = 0.8359 (63 PASS / 47 FAIL; TP 55 / FN 8 / FP 1 / TN 46; unique-100 basis: **91/100 = 91.00%**). The path to this figure includes 25 adjudications that adopted the judge's own direction, so it is **not** independent evidence of judge quality and is **not** a pass of the pre-registered gate. The error-family decomposition is the primary result; the two agreement figures are summary rows beneath it (candidate register: W7-CANDIDATES-v2, SHA `1d12419d…`).

**错误族分解表（card 正文核心）**

| 错误族 | 计数 | 含义 |
|---|---:|---|
| `human_under_flag` | 24 | 人工漏报，judge flag 正确 |
| `judge_over_flag` | 8 | judge 过度 flag |
| `rubric_ambiguity` | 1 | rubric 歧义，双方均无责 |
| `judge_missed` | 1 | judge 漏报 |
| **合计** | **34** | 方向采纳：judge 25 / human 9 |

- 出处：DADJ `57bd40c9…`（summary 已核）；`review_scores_normalized_v1.json` `dc754050…`；回放 `replay_v11_result.json` `e6712179…`。
- 基数纪律（V11-07）：unique-100 的同一读数为 68.00%（raw）→ 91.00%（post-adjudication），必须与 110 基数并列标注，禁止只给一个百分数。

### 5.3 禁语清单（公开工件硬约束）

| 禁语 | 替代写法 |
|---|---|
| “0.8 逐例分数门槛 / per-case 0.8 score threshold” | 逐例 verdict 只由 E=0 决定；score 为描述性 |
| “judge 漏 17 例” | 人工标记 17 例中判定命中所否 14、漏 3（R-001/R-031/R-082） |
| “gate passed / 门通过” | “pre-registered gate not met”；并列读数用 “post-adjudication consensus agreement” |
| `protocol-corrected`（公开文本） | `post-adjudication consensus agreement`（内部术语不改历史件） |
| 91.82% 缺少 “not a gate pass” 限定语 | 同句或紧邻脚注强制携带 |
| 任何未标基数的百分数 | 百分数后必须标 unique-100 或 continuity-110 |
| 把 91.82% / 91.00% 混用或互换 | 各自标基数，分别出现 |

## 6｜用途边界

> **Intended use**: benchmarking text-level clinical correctness of report-generation systems on label-conditioned veterinary thoracic-radiograph reports; rubric research; error-taxonomy development.
>
> **Not intended for**: clinical decision support, diagnosis, triage, or any patient-care use. The reports are synthetic and label-derived; the dataset is not a diagnostic device and carries no regulatory clearance.

## 7｜局限（必须随 claim 一同发布）

1. **无参考报告**：无法计算任何以参考报告为真值的指标（BLEU/ROUGE 类对比不适用）。
2. **标签条件生成**：文本与图像之间没有因果通路；图像仅作为发布件配对存在。
3. **单投影**：无法支持需要正交位的结论（分布范围、气胸定量、部分骨折）。
4. **层级制度**：6 类 non-evaluable 不进入评分；3 类 research 可被合规省略。
5. **物种覆盖**：主 fold 仅犬猫；38 例补充 fold 含未标注与其他物种，分析时应分层或排除。
6. **标签噪声**：GT 继承源数据集标注，未做临床复核；`patient_id` 级聚合未发布，无法做受试者级重抽样分析。
7. **评测规模**：人工评分子集 110 例（95 犬 / 15 猫），置信区间宽；不得外推为总体性能。

## 8｜拟发布短版 claim（卡片用）

> **W7-VetXRay-Report** — 7,695 single-projection veterinary thoracic-radiograph cases with **model-generated** reports (GLM-5.3-Flash) conditioned **only on ground-truth labels**, species and projection; **no images were shown to the generator** and **no original reports exist**. The pre-registered agreement gate (80%) was **not met** (76/110 = 69.09%, κ = 0.3750). Evaluation is organized around an error-family decomposition of 34 adjudicated disagreements (human_under_flag 24 / judge_over_flag 8 / rubric_ambiguity 1 / judge_missed 1); a post-adjudication consensus reading (**not a gate pass**) is reported in the evaluation section only. Text-level rubric evaluation only; not for clinical use.

## 9｜签发栏

| 项 | 状态 |
|---|---|
| 数据集身份三要素（model-generated / label-conditioned / no reference reports） | ✅ 签发 |
| 规模与构成表 | ✅ 签发 |
| 生成协议（模型、参数、prompt SHA、未发送字段） | ✅ 签发 |
| 双读数表述与禁语清单（三要素 ①②③ 已落实） | ✅ 签发（2026-11-13） |
| 用途边界与局限 7 条 | ✅ 签发 |
| 短版 claim（头部仅预注册读数 + 分解表） | ✅ 签发（2026-11-13） |

## 10｜待决 / 依赖

- **B4**：license 与 gated 级别未定 → §8 短版 claim 的发布条件留空（B4 域已收窄为 license 矩阵 / 同意范围 brief / DICOM gated 与否 / PNG-only 双轨）。
- **A3**：related-work 只查未写 → 引用条目在 C9 交叉引用统一回填。
- 物种补 fold 的表述方式（分层 vs 排除）需在 B3 manifest 字段确定后回填 §2 注脚。
