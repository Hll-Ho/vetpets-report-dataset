# DADJ Errata Register

- **Register version**: v1.0
- **Effective date**: 2026-11-13
- **Governing ruling**: W7-REL-001 Phase A 裁定书（2026-11-13）裁决 3
- **Frozen source (immutable)**: `outputs/W6/review/adjudication_disagreements.json` SHA256 `57bd40c951ad135b58d71eef548351e7e76f13fc7c60fcb4f51b703e96fbaf23`；`adjudication_disagreements.md` SHA256 `db9edaea3af5db004bb309140ca04aa460149e2ff237082fc11079f7c59656b7`
- **Freeze status**: 本 register 随发布件同版本，列入 C5 冻结清单；DADJ 本体保持冻结、零改动。
- **Pairing rule**: 任何公开工件（README / Zenodo description / HF dataset card / 论文）引用 DADJ 时，必须同时链接本 register。

---

## ERR-01 — gate_decision 投照位漏判计数

| 项 | 内容 |
|---|---|
| 位置 | `adjudication_disagreements.json` → `self_checks.gate_decision`（第 1830 行）。`.md` 摘要（第 11–13 行）不含该句，不受影响 |
| 原文（逐字） | “主门（预注册，原始盲评一致率）69.09% < 80%，未过；双向偏差已定量化（人工漏 27 例无依据断言、**judge 漏 17 例投照位错并误报阴性/研究层**）；经逐例裁决（DADJ-01~34，2026-11-13）后共识一致率 91.82%（κ=0.836），作为协议修正后读数并列归档，不替代门判定。” |
| 更正 | “judge 漏 17 例投照位错” → “judge 投照位漏判 3 例——人工标记 17 例中命中 14 例，漏 R-001/R-031/R-082，仅 R-082 为 verdict 级；judge 误报阴性/研究层” |
| 依据 | 按判定级明细重算（`answer_key_full.json` + asSubmitted errors）。指针 → `manifest_adjudication_disagreements.json` `self_checks.gate_decision_correction`（manifest SHA256 `714d6dae63c97199bf21a992f6a29b44a6d419d6b9816da2ccc7efd26005e29a`） |
| 影响范围 | 仅叙事表述。不改变任何 verdict、score、E 值、DADJ 条目或已认证数字：63 PASS / 47 FAIL，101/110 = 91.82%，κ = 0.8359 |
| 状态 | **ACTIVE** |

---

## ERR-02 — 预留：DADJ-35 类增补

- 本条目为机制预留，**当前未触发**。R-074 经全文复核命中分支 (i)，CHG-05 维持，不存在 DADJ-35。
- 后续若出现 DADJ-35 类增补（如分支 (ii) 的 `judge_over_flag` 登记）：仅在本 register 追加条目，DADJ 本体不改；register 版本号递增，旧→新 SHA 记入 CHANGELOG。

---

## 禁语范围（与裁决 3 配套）

- 禁令约束**主张性公开文本**：claim、dataset card、README、论文。
- **豁免**：更正记录本身（before/after 字段、本 errata register）。它们的存在即更正行为的证据。
- 因此本 register 的 ERR-01 原文栏保留 “judge 漏 17 例投照位错” 不构成违规；主张性文本仍不得出现该表述。

---

## 冻结记录

- register 自身 SHA256 在冻结时记入 `outputs/W6/CHANGELOG.md` 与 C5 SHA 表；本文件不写入自指哈希。
- 追加原则：只增不改；每次追加产生新版本号与新 SHA，DADJ 两个源文件 SHA 保持不变。
