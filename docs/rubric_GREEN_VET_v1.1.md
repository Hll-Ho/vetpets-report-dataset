# GREEN-vet-v1.1 — Judge Rubric (frozen)

- **Version**: v1.1
- **Status**: `frozen` — 2026-11-13。13 条全部签发（4 条带修正令，已逐字落实）；§10 八项回放全过（§12）。未冻结前不得铸 DOI，现已解除该前置。
- **Supersedes**: v1.0（SHA `5bb824b7e0e8f74b339c8d2204d80999ce742820e39e83d7864d99a4f72b3157`）
- **Scope**: 仅前瞻适用于 W7。W6 rubric v1.0 与全部 W6 读数（63P/47F、101/110、κ=0.8359、预注册 69.09%）不变。
- **Governing ruling**: W7-REL-001 Phase A 裁定书（2026-11-13），裁决 1 方向判线 + 候选 v2 a–i。
- **Methodology**: 同 v1.0（GREEN, Ostmeier et al. 2024）；无参考报告，grounding = GT labels + species/projection；不提供图像；仅评文本层临床正确性。

---

## 0｜条文索引（逐条签发用）

| Clause | 主题 | 来源 | 签发（2026-11-13） |
|---|---|---|---|
| V11-01 | 方向判线（三族） | 裁定书裁决 1 | 签发＋修正 ①② |
| V11-02 | Tier × 方向行为矩阵 | 裁定书观察 + DOC-01 | 签发＋修正 ③ |
| V11-03 | 豁免仅及 omission；contradiction 追踪 GT 成员 | CAND-d / DOC-01 | 签发 |
| V11-04 | hallucination 收窄为正向断言 + 非评估类 carve-out | CAND-e | 签发（张力维持 1.0） |
| V11-05 | per-(type,class) 去重（schema 强制） | CAND-f | 签发 |
| V11-06 | 投照位词表与 DV/VD/LL/RL 四向映射 | CAND-g / LN-01 | 签发＋修正 ④ |
| V11-07 | 重复对单计 + 双口径 | CAND-h | 签发＋修正 ⑤ |
| V11-08 | verdict 仅由 E 决定 | CAND-i | 签发 |
| V11-09 | ALV/BRC 单投影分布语句 | CAND-a | 签发（P1 写入） |
| V11-10 | validator `nof_conflict` 边界 | CAND-b | 签发（P7 写入） |
| V11-11 | 研究层单标签案例最低信息标准 | CAND-c | 签发（P4 = 选项 i） |
| V11-12 | 全局正常性断言的计数口径 | 本草案新增 | 签发＋修正 ⑥ |
| V11-13 | 输出 schema 校验 | CAND-f | 签发 |

---

## 1｜方向判线（V11-01，核心新增条文）

> 三族是**功能定义**；下列短语表**仅为示例（non-exhaustive）**。唯一判据：该表达是否**保留特定发现可能存在的可能性**。生成措辞会漂移，未列入示例表的新短语按功能归类，不因表外而逃逸判线（修正令 ①）。方向判线管辖 contradiction 与 omission 的读取；hallucination 另见 V11-04。

### Family A — possibility-preserving（存活）

示例：`cannot be excluded` / `cannot be ruled out` / `may be present` / `possible` / `not reliably assessed on this view`（当用于保留某个具体发现的可能性时）。

- 方向 = **存活**（possibly present）。
- 计分：**0**。既不构成 contradiction，也不构成 omission（视为已提及）。
- 先例维持：R-009（interstitial cannot be excluded）、R-072（cannot be excluded as artifact）。

### Family B — absence-asserting（缺席）

示例：`no definite … abnormality` / `without definite …` / `appear(s) unremarkable` / `no significant …` / `no evidence of …` / `unremarkable`。

- 方向 = **缺席**（absent）。确定性限定词（`definite` / `apparent` / `grossly`）只量化确定性，**不改变方向**。
- 计分：**当且仅当该类 ∈ 有效 GT → contradiction 1.5**（触发器 1：存在真值发现时断言正常/无异常）；该类 ∉ GT → **0（正确阴性）**。

### Family C — directionless modal limitation（无方向）

示例：`cannot be reliably assessed on a single projection` / `limited on one view` / `would require orthogonal or dedicated views`。

- 方向 = **无**。单独出现**不触发**任何错误。
- 与 Family B 的缺席结论并存时，**不豁免**该结论（即“全局正常 + 单投影受限”仍按 Family B 计 contradiction）。

### Rule 3 接线（修正令 ②）

Rule 3（不因加限定扣分）的保护范围 = **Family A 存活语 + 同一方向内的措辞与强度**。它**不把 Family B 的缺席结论转换为沉默**，**不豁免 contradiction**，也不使 Family C 的限度语吸收同句中的缺席断言。

---

## 2｜Tier × 方向行为矩阵（V11-02）

| Tier | 正向正确提及 | 缺席方向结论（**仅当该类 ∈ 有效 GT**） | 缺席陈述（该类 ∉ GT） | Family A 存活语 | 纯沉默 |
|---|---|---|---|---|---|
| trusted | 0 | contradiction 1.5 | 0（正确阴性） | 0（视为已提及） | omission 1.0 |
| marginal | 0 | contradiction 1.5 | 0（正确阴性） | 0（视为已提及） | omission 1.0 |
| research | 0 | contradiction 1.5 | 0（正确阴性） | 0 | 0 |
| non-evaluable | hallucination 1.0（任何正向提及；GT 成员身份不 rescue） | contradiction 1.5 | 0（正确阴性） | 0 | 0 |

- 类 ∉ GT：正向断言 → hallucination 1.0（仅非评估类不受 GT 成员身份影响）；缺席陈述 / Family A / 沉默 → 0（正确阴性）。
- **R-040 / R-044 判式由此行直接兑现**：GT=NOF，报告否认 PMD/DPH（∉ GT）→ 0。
- 非评估类：正向 1.0；缺席（∈ GT）1.5；缺席（∉ GT）0；Family A 0；纯沉默 0。**不再使用 v1.0 的绝对“never mention”措辞**，改由本矩阵机械执行。
- 四行对称：正向 1.0（仅非评估类）｜缺席 ∈GT 1.5 / ∉GT 0｜存活语 0｜沉默 0（trusted/marginal 为 omission 1.0）。
- 同一 (type, class/topic) 只计一次；contradiction 与 omission 不叠加。

---

## 3｜错误分类（权重冻结）

| Error type | Definition | Weight |
|---|---|---:|
| `hallucination` | A positive assertion that a finding is present when that finding is not in the effective ground truth. Negative statements, Family A possibility-preserving language, Family C limitation language, and clinically correct mentions of research-tier classes are **not** hallucinations. A hedged positive assertion (“appears to show X”) **is** a positive assertion: the hedge modifies degree, not existence; where an assertive sentence carries a limitation clause, the clause is severable and the assertive core is scored independently (P5). For non-evaluable classes, any **positive** mention is a hallucination (1.0) regardless of GT membership; an absence-asserting denial of a non-evaluable GT class is scored as contradiction (1.5) instead, never both. | 1.0 |
| `omission` | A GT class of tier trusted or marginal is neither stated nor hedged（Family A 存活语视为已提及）. **Tier exemption is omission-only.** Never applies to research-tier classes, non-evaluable classes, or NOF dropped by precedence. | 1.0 |
| `contradiction` | An absence-asserting statement (Family B) while the effective ground truth contains at least one finding; or an explicit denial of a GT member. The tier of the denied class does not matter: contradiction tracks GT membership (DOC-01). Denying a class outside GT is a correct negative (0). Do not also count omission for the same class. A single global normality assertion is counted once per case (V11-12). | 1.5 |
| `attribute_error` | A clinically material attribute contradicts the provided context: wrong species, or a named projection/side contradicting `projection`. Projection lexicon: **DV=dorsoventral, VD=ventrodorsal, LL=left lateral, RL=right lateral**; DV and VD are distinct projections, not spelling variants — writing “ventrodorsal” for a DV header is a contradiction. Merely recommending extra views is not an error. **Side (P2)**: when the header carries no side (e.g. a lateral projection without LL/RL), a report naming left or right is **not** an attribute error — absence of information is not a contradiction; finding-level assertions in that sentence are still scored by the normal rules. | 0.5 |
| `unsupported_claim` | A clinically material claim not grounded in labels or context: an extra diagnosis outside the vocabulary, or asserted severity/measurement/lobar localization presented as fact. **Pattern-distribution clause (P1, ALV and BRC only)**: on a single projection, distribution language read as a description of what is visible on that view (“diffuse to patchy”, “across the visible lung fields on this view”) is not an error solely because multi-lobe extent cannot be verified without orthogonal views, and no hedge is required for that reading; an explicitly unscoped extent assertion that presupposes orthogonal views (“extends throughout all lung lobes”, “involves all lung lobes”) is scored 0.5. The clause is an error only when the stated distribution conflicts with the visible anatomy or the GT label. INT is **not** covered by this clause; it follows the tier rules. Generic technique statements, negative statements, and recommendations are not errors. At most one per case. | 0.5 |

---

## 4｜Rules

1. Evaluate findings and impression together; a statement repeated in both is counted once.
2. At most one error per (type, class/topic) per case. Do not double count omission + contradiction: use contradiction only. Output validation MUST reject duplicate `(type, class)` pairs.
3. Do not penalize hedging style, wording, length, structure, or the presence/absence of recommendations. **Protection scope (修正令 ②)** = Family A possibility-preserving language + phrasing/intensity **within a given direction**. This rule does **not** convert a Family B absence-asserting conclusion into silence, does **not** exempt a contradiction, and does **not** let Family C limitation language absorb an absence assertion in the same sentence (V11-01).
4. Use only the provided labels and context. Do not import outside clinical knowledge about the patient.
5. A report that correctly mentions every effective ground-truth class and makes no other material error has ZERO errors.
6. **Duplicate pairs and dual basis (V11-07 / P3)**: the 110-case packet **retains** the 10 duplicate pairs (W6 comparability + intra-rater QA asset); a pair is never two independent observations. **Primary agreement = unique-100**; the 110-case figure is reported in parallel as a **continuity series**. Any published agreement rate must state its base.
7. **Verdict = `PASS` iff `weighted_error_sum = 0`.** `score` is descriptive only and never feeds the verdict. No per-case score cutoff exists.
8. **Global normality assertion counting (V11-12)**: a single global normality statement is counted **once per case** (E = 1.5), not once per GT class. **Class assignment (修正令 ⑥)**: `class` = the GT class the statement itself names or most directly denies; a global statement **does not inherit** classes already assigned to other statements (prevents a dedup collision with an explicit class-level denial); if unresolvable → `GLOBAL`. Single-class GT (e.g. R-042 / TRC) falls back to that class, leaving W6 records undisturbed.

---

## 5｜Validator 边界（V11-10）

`nof_conflict` 仅在报告作出 **patient-state assertion**（断言患者/检查“正常/无异常”）且 GT 非空时触发。**Family B 的全局正常性断言属于 patient-state assertion**（同时触发 validator 与 GREEN contradiction）；**类级阴性陈述不算**（如 “no pleural effusion”，属类级陈述，只走 GREEN 评分）。以下**不触发**：

- Family C 评估限度声明（“cannot be reliably assessed on this view”）——单独出现不触发；
- Family A 存活语——单独出现不触发；
- 类级负向陈述（如 “no pleural effusion”）当 PLE ∉ GT —— 属正确阴性；
- 对 GT 成员的类级否认 —— 归 GREEN contradiction，不走 `nof_conflict`。

同一边界分别适用于 `report_findings` 与 `report_impression`；触发必须能定位到具体语句。

---

## 6｜研究层单标签最低信息标准（V11-11，P4 = 选项 i）

- **选项 (i)（签发采纳）**：GT 仅含研究层类别（INT/MGE/HRN）的案例，**从 detector/validator gate 中排除**，但**保留 GREEN 资格**；在 pack 中标记 `non_discriminating`。
- 选项 (ii)（未采纳，留档）：保留全部 gate 资格，仅在 gate 定义中显式说明此类案例的 PASS 不携带 detector 信息。

---

## 7｜Score 与 Output

- `weighted_error_sum` E = 所有错误权重之和。
- `D = max(1, number of effective ground-truth classes)`（NOF 优先规则之后；NOF-only 案例 D=1）。
- `score = max(0, 1 − E / D)`，保留 4 位小数；**描述性字段**。
- `verdict = PASS iff E = 0, else FAIL`。

输出 schema 同 v1.0；新增校验：拒绝重复 `(type, class)`，`verdict` 必须与 E 一致，`score` 不参与 verdict 判定。

---

## 8｜v1.0 → v1.1 diff 摘要

| 位置 | v1.0 | v1.1 | Clause |
|---|---|---|---|
| contradiction | “Asserts normality…; or explicitly denies…” 无方向分类 | 增加 Family A/B/C 方向判线；全局正常性按 Family B 计 1.5 | V11-01 |
| 层级豁免 | 仅条文，未说明是否及于 contradiction | 豁免仅及 omission；contradiction 追踪 GT 成员 | V11-03 |
| hallucination | “Includes mentioning any non-evaluable class” | 收窄为正向断言；负向/存活/限度语/研究层正确提及不计；非评估类正向提及仍 1.0；“appears to show” 算正向 | V11-04 |
| 去重 | Rule 2 文字存在，输出未强制 | schema 层拒绝重复 (type,class)；一语句描述多类至多 1 个 hallucination | V11-05/13 |
| attribute_error | “projection/side 矛盾” | 增加 DV/VD/LL/RL 四向词表；DV↔ventrodorsal 不享拼写豁免；无侧别时写 left/right 不计 | V11-06 |
| 重复对 | 未规定 | 保留 110；primary = unique-100，110 为 continuity series；公开数字须标基数 | V11-07 |
| verdict | 隐含 E=0 | 显式写入 Rule 7；score 不参与判定；无逐例分数线 | V11-08 |
| ALV 分布 | 未规定 | ALV/BRC 单投影分布按“可见范围”读、无强制 hedge；未限定范围的 extent 断言 0.5；INT 不适用 | V11-09 |
| validator | patient-state 与限度语未分 | 仅 patient-state 触发；Family B 全局正常算 patient-state；类级阴性不算 | V11-10 |
| 研究层单标签 | 未规定 | 选项 (i)：排除出 detector/validator gate，标 `non_discriminating`，保留 GREEN | V11-11 |
| 多标签全局正常 | 未规定 | 每案只计一次，class 指向最直接否认的 GT 类；不继承其他陈述的类 | V11-12 |

### 8.1 修正令落实记录（冻结前逐字核对表）

| 修正令 | 内容 | 落实位置 |
|---|---|---|
| ① | 三族以功能定义，短语表仅为示例 | §1 引言 + 三族各段 “示例：” |
| ② | Rule 3 显式接线：保护范围 = Family A + 同方向措辞；不转缺席为沉默、不豁免 contradiction | §1 Rule 3 接线 + §4 Rule 3 |
| ③ | 矩阵单元格内嵌“仅当该类 ∈ 有效 GT”；∉GT 缺席陈述 = 0 写成矩阵行 | §2 表头与新增列、R-040/R-044 行 |
| ④ | P2 写入 V11-06：header 无侧别时写 left/right 不计 | §3 attribute_error |
| ⑤ | 双口径写入 V11-07：保留 110、primary = unique-100、基数标注 | §4 Rule 6 + §10 第 5 项 |
| ⑥ | V11-12 class 指派细则：不继承他陈述类、不可解 = GLOBAL | §4 Rule 8 |

---

## 9｜待决点落定表（P1–P7，2026-11-13 裁定）

| ID | 裁定 | 依据 |
|---|---|---|
| P1 | ALV+BRC；无强制 hedge；未限定范围的 extent 断言（“extends throughout all lung lobes” 类）→ unsupported_claim@0.5；INT 不适用（走 tier 规则） | 视野限定逻辑对 trusted/marginal 模式类同等成立；INT 有自身 tier 制度，叠加会打架 |
| P2 | 不计 attribute_error；该句 finding 级断言仍按正常规则评分 | attribute_error 定义是“与提供上下文矛盾”，header 缺侧别是信息缺失 |
| P3 | 保留 110 + 双口径：primary = unique-100，110 = continuity series，公开数字强制标基数 | 修正令 ⑤ |
| P4 | 选项 (i)：排除出 detector/validator gates，标 `non_discriminating`，GREEN 保留 | 沉默即可通过的 gate 测不了任何东西；与 R-074 分支 (ii) 应然态闭环 |
| P5 | “appears to show X” = 正向断言；句内限度语可分割，断言核心独立评分 | 存活语说“可能存在”，后者说“看起来就在”，方向为正 |
| P6 | 每案一次（E=1.5），不按类计 | 全局陈述是一个言语行为、一个 topic；按类计会使 E 随 \|GT\| 膨胀 |
| P7 | 类级阴性不算 patient-state；Family B 全局正常性断言算；Family A/C 单独出现不触发 | `nof_conflict` 的对象是“病人/检查整体正常”主张 |

### 9.1 张力裁定（非评估类 ∈ GT 的正确正向提及）

**维持 1.0。** 理由：tier 制度存在的理由就是单投影无法可靠评估这些类别；GT 标签来自更全面的检查，报告从单投影正向断言该类是过度解读模态。错误类型是“断言不可评估之物”，不是“与 GT 不符”。GT 成员身份**不 rescue** 正向提及（1.0 照计），也**不加重**缺席陈述（1.5 仅由 ∈ GT 决定）。矩阵因此四行对称。

连带确认：research 层“须临床正确”的可操作化不新增规则——具体性冲突已由现有 `unsupported_claim` 触发器覆盖（severity / measurement / extra-dx），且 Rule 4 禁外部知识。

---

## 10｜验收回放（冻结前执行；结果见 §12）

1. 110 例全量重算：每例 verdict 与 W6 认证集逐一一致（63P/47F、101/110=91.82%、κ=0.8359 实算复现）。
2. 六例复核：R-003 / R-031 / R-042 / R-063 / R-073 / R-074 verdict 一致；R-031 E=0.5 / score=0.75；R-003 FAIL；无同类别 omission+contradiction 并存。
3. 输出零重复 `(type,class)`；R-083 hallucination ≤1。
4. 17 例人工投照位标记全部被 V11-06 词表复现；R-082 FAIL。
5. 双口径并列产出：unique-100（primary）与 110（continuity series），基数标注齐全。
6. 所有 E>0 案例均为 FAIL（含描述性 score 较高者）；无逐例分数线。
7. hallucination evidence 无以否定词开头的条目；无对研究层正确提及计的 hallucination；无 Family A/C 语言计的 hallucination。
8. 非评估族回放：R-042/R-063/R-073 = 1.5；R-040/R-044 = 0；存活语例（R-009/R-072）= 0。

---

## 11｜签发栏

| Clause | 签发（裁决方） | 日期 | 附令 |
|---|---|---|---|
| V11-01 方向判线 | ☑ | 2026-11-13 | ①② |
| V11-02 Tier × 方向矩阵 | ☑ | 2026-11-13 | ③ |
| V11-03 omission-only 豁免 | ☑ | 2026-11-13 | — |
| V11-04 hallucination 正向断言 | ☑ | 2026-11-13 | 张力维持 1.0 |
| V11-05 per-(type,class) 去重 | ☑ | 2026-11-13 | — |
| V11-06 投照位词表 | ☑ | 2026-11-13 | ④（P2） |
| V11-07 重复对权重 | ☑ | 2026-11-13 | ⑤（P3） |
| V11-08 verdict 仅由 E 决定 | ☑ | 2026-11-13 | — |
| V11-09 ALV/BRC 分布 | ☑ | 2026-11-13 | P1 |
| V11-10 validator 边界 | ☑ | 2026-11-13 | P7 |
| V11-11 研究层单标签 | ☑ | 2026-11-13 | P4 = (i) |
| V11-12 全局正常性计数 | ☑ | 2026-11-13 | ⑥（P6） |
| V11-13 schema 校验 | ☑ | 2026-11-13 | — |

签发来源：`W7-REL-001 B1 签发裁定书`（2026-11-13，13 条全签、4 条带修正令、P1–P7 全落定、回放通过即预授权冻结）。

**冻结预授权**：§10 八项回放全过 → 改名 v1.1 final → 计算 SHA → 记入 CHANGELOG 与 C5 冻结清单（与 DADJ errata register 同批），无需再签。任一漂移 → STOP。

---

## 12｜验收回放结果（2026-11-13，离线重算，0 次 API 调用）

执行器：`outputs/W7/replay_v11.py`；结果：`outputs/W7/replay_v11_result.json`。输入为 W6 冻结件（packet / answer_key / normalized / asSubmitted / DADJ），未重跑生成、未重跑 judge、未改动任何 W6 工件。

| 项 | 判据 | 结果 | 关键读数 |
|---|---|---|---|
| R1 | 110 例逐例 verdict 一致 | PASS | 110/110 一致；重算 63P/47F；101/110=91.82%；κ=0.8359；TP55/FN8/FP1/TN46 实算复现 |
| R2 | 六例不变；R-031 E=0.5/score=0.75；R-003 FAIL | PASS | 六例 verdict 与认证集一致；无同类别 omission+contradiction 并存 |
| R3 | 零重复 (type,class)；R-083 幻觉 ≤1 | PASS | 认证集重复对 0；R-083 W6 judge 3 条（ALV/BRC/INT）同一句 → V11-05 下有效值 1 |
| R4 | 17 例投照位全部复现；R-082 FAIL | PASS | 词表复现 17/17（均为 header DV、报告写 ventrodorsal）；17 例认证 verdict 全 FAIL |
| R5 | 双口径并列、基数标注 | PASS | unique-100：68.00%（68/100）→ 91.00%（91/100）；continuity-110：69.09%（76/110）→ 91.82%（101/110）；10 对重复对 verdict 两两相同 |
| R6 | E>0 一律 FAIL | PASS | E>0 共 47 例，全部 FAIL；其中最高描述性 score = 0.8333（R-033，FAIL） |
| R7 | 无否定开头证据 / 研究层误计 / Family A·C 误计 | PASS | 认证集三类违规均为 0；W6 judge 侧 5 条历史缺陷（R-040/R-044 否定开头；R-004/R-083/R-091 研究层）作为冻结记录留档 |
| R8 | 非评估族矩阵 | PASS | R-042/063/073 = 1.5（contradiction）；R-040/R-044 = 0；R-009 = 0 |

**口径说明（R8）**：R-072（Family A 先例 “cannot be excluded”）认证 E=0.5，来自无关的 `unsupported_claim`（“inflammatory airway disease”，DADJ-21），非存活语被判分；该例 direction errors（contradiction/omission）= 0。判据按“方向判线错误为 0”执行，未改任何条文。

**score 字段漂移**：0 例（除 DADJ 覆盖案例外，逐例 score 与 normalized 完全一致；R-071 的 D=1 勘误不影响 verdict）。

**结论**：§10 八项全过，冻结预授权生效。W6 认证数字（63P/47F、101/110=91.82%、κ=0.8359、预注册 69.09%）零扰动。
