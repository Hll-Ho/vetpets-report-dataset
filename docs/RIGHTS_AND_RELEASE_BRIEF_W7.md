# B4 — W7 权利与发布形态 brief（rev3，已签发）

- 工单：`W7-REL-001`｜阶段：B4｜状态：`signed`（rev3，2026-11-13）
- 签发依据：B4 rev2 裁定书（`B4_rev2_upstream_license_confirmed`）+ rev3 事实补全裁定（`VA1_full_filelist_correction`）；v1 为同日早间"许可未确证"版本
- **未冻结、不铸 DOI**；本文件不触发任何对外发布动作
- 域（经 B3 裁定收窄）：①license 矩阵 ②同意范围 brief ③DICOM gated 与否 ④PNG-only 双轨 ⑤`split` 是否发布
- 前置事实源：`REDACTION_MANIFEST_W7_DRAFT.md` §1/§8、`W7_REL_001_INTEGRITY_CHECK.md` §5、`W7_REL_001_PHASE_A_REPORT.md` A3/B 段、`CLAIM_DRAFT_W7.md` §6/§7/§10、Zenodo API `records/19051776`

**修订日志**

| 版本 | 日期 | 变更 |
|---|---|---|
| rev1 | 2026-11-13 | 初稿，状态 `draft_pending_signature`；上游许可"未确证"，方案 A 判为不可接受 |
| **rev2** | 2026-11-13 | F2 上游许可确证 `cc-by-4.0`（Zenodo API 核验，阻断项解除）；L1/L2 转为**可继承再分发**（署名强制 + 修改标注）；方案 A 解禁；推荐 B 理由改为**溯源卫生**；R3 注销（`discharged_by_fact_update`）并替换为 V-A1；STOP1 删除、STOP2 改署名向；§4/§8 改写；V-A1 执行结果见 §14 |
| **rev3** | 2026-11-13 | V-A1 事实补全：上游 **8 个文件全量枚举**（五包 RX_1…RX_5 + 3 个伴生文件），五包字节和 40,755,807,501 ≈ 40.8 GB 与页面标称吻合；**撤销"3 包"口径**（截断误读）与 **V-A1-1**（本地 5 目录 ↔ 上游 5 包，1:1）；更正 RX_5 md5（`6ac1853c…` 为条目 UUID 前缀，非校验和）；弃用 "v2" 称谓（`relations.version = [{index:1, is_last:true}]`）；V-A1 拆为 a/b/c 三层，a 层 3/3 命中（§14.1）；§11 新增 V-A1-a 不匹配 STOP |

---

## 0｜边界声明（本文件不做的四件事）

1. **不提供法律意见**；只做事实认定与权利分层，法律定性由裁决方决定是否外询。
2. **不替上游授权**；本项目对上游层的作为限于 CC BY 4.0 允许的再分发，不附加额外限制。
3. **不改动任何已冻结件**：rubric v1.1（`fd7ede2d…`）、claim（`30c3e021…`）、脱敏 manifest（`d0c4c789…`）零改动。
4. **不做 scrub 决定**：S-01…S-13 已由 B3 终版，本文件不重开。

---

## 1｜事实核查记录（rev3，2026-11-13）

| # | 核查项 | 结论 | 证据 |
|---|---|---|---|
| F1 | 本地副本 license 元数据 | 未发现——**不再构成阻断**：权利由上游记录继承 | `data/` 全目录扫描无 `LICENSE`/`README`/许可声明；仅有 `Image_upload.py`（上游包内同名示例脚本，无许可头） |
| F2 | 上游 Zenodo 记录与许可 | **已确证：CC BY 4.0，open access；8 个文件全量枚举（§1.1）** | Zenodo API `https://zenodo.org/api/records/19051776`：`license.id = cc-by-4.0`、`access_right = open`；record 19051776 为 concept `18999729` 的**唯一已发布版本**（`relations.version = [{index:1, is_last:true}]`；`revision:4` 是记录修订次数，非数据集版本），DOI `10.5281/zenodo.19051776`，concept DOI `10.5281/zenodo.18999729`；作者 Banzato T. / Burti S. / Zotti A. / Wodzinski M.（University of Padua 等）；资源类型 dataset；**`files[]` 8 项，字节和 40,755,807,501 ≈ 40.8 GB**（与页面标称 "Files (40.8 GB)" 吻合，见 §1.1）；检索日期 2026-11-13 |
| F3 | 本地同意文书 / 伦理批号 / IACUC 记录 | 未发现——**同意义务由上许可条款吸收** | `data/`、`outputs/W1` 无相关文件；兽医影像不涉个人数据 |
| F4 | 发布目标平台 | 已确证 | `code.md` W7 行：Zenodo DOI + HF 镜像 + GitHub |
| F5 | 待发布内容与规模 | 已确证 | 7,695 PNG + 4 列 manifest + 7,695 份生成报告 + rubric/DADJ/errata + 脚本（B3 §7） |
| F6 | 物种构成 | 犬猫 7,657 / 7,695（99.5%），33 未标注 + 5 其他 | 完整性检查 §5.1 |

> **关键认定（rev2）**：上游许可**已确证为 CC BY 4.0**（`license.id=cc-by-4.0`，`access_right=open`）。L1/L2 的再分发合法性来自上游；**署名、许可链接与"标注修改"为强制义务**（CC BY 4.0 §3(a)），且**不得附加额外限制**（§2(a)(5)(B)）。rev1 的"未确证"仅作为检索史保留。
>
> **检索史备注**：Phase A 与 rev1 的两次"未定位"是关于**那两次检索**的陈述，不是关于世界的陈述；本次换查询词并经 API 校验后命中。

---

### 1.1｜上游文件全量枚举（rev3，API `files[]` 全文）

| # | 文件 | 字节 | MD5 |
|---|---|---|---|
| 1 | `RX_1.zip` | 6,287,527,959 | `53f107be7efb2c34ad69695b2c793b4e` |
| 2 | `RX_2.zip` | 7,497,976,894 | `c8f69d88086fbf77ba8cfd628ecc7f37` |
| 3 | `RX_3.zip` | 9,508,136,662 | `b39e3f1d438e84670a3b06e7850112de` |
| 4 | `RX_4.zip` | 10,578,017,068 | `383f54c5000499eb24c975bd4981ad0f` |
| 5 | `RX_5.zip` | 6,884,148,918 | `8949ed8d6ef01dd50a60e664d0e3fd24` |
| 6 | `Image upload.py` | 3,843 | `eb20afca83b2aa1ef6a0c3adbc2ae126` |
| 7 | `Image upload.ipynb` | 5,380 | `510538550ac2d81af15260905a5e6506` |
| 8 | `File list with tags.xlsx` | 419,755 | `45c46fd5af3e562dadeeafc198c9a628` |

- **枚举完整性证明**：五包字节和 **40,755,807,501 ≈ 40.76 GB**，与页面标称 "Files (40.8 GB)" 吻合 → 枚举无截断。
- **口径更正（rev2 → rev3）**：rev2 所称"RX_2/4/5.zip 三包"为**截断视图误读**；上游实为**五包**（RX_1…RX_5）。
- **md5 转录更正**：rev2 记录的 RX_5 `6ac1853c…` 是文件条目 **UUID 前缀**（`6ac1853c-f981-4ccf-b4b6-c786310d1032`），**不是校验和**；正确值为 `8949ed8d6ef01dd50a60e664d0e3fd24`。
- **版本称谓**：弃用 "v2"；该记录是 concept `18999729` 的**唯一已发布版本**（`index:1, is_last:true`）。

---

## 2｜权利分层矩阵（layer-wise rights）

| 层 | 内容 | 权利来源 | 本项目能否授权 | 现状 |
|---|---|---|---|---|
| **L1** | 上游影像：7,695 PNG（派生自 10,234 DICOM） | 上游 Zenodo record 19051776（**CC BY 4.0**） | **能**——按上游同条款再分发（继承 CC BY 4.0），**署名强制** | 许可已确证（F2） |
| **L2** | 上游标签：18 类 GT、`species`、`projection` | 同 L1（标注为上游贡献） | **能**——同上，署名强制 | 随 L1 |
| **L3** | 生成报告：7,695 份（GLM-5.3-Flash，标签条件） | 本项目 + 生成服务条款 | **能**（附 AI 生成声明） | prompt v1.2 SHA 已固化 |
| **L4** | 评测工件：rubric v1.1、DADJ + errata、评测协议、manifest 编排 | 本项目 | **能** | 已冻结 / 已签发 |
| **L5** | 代码：`build_release_b3.py`、`replay_v11.py` 等 | 本项目 | **能** | 待签发 MIT |

> **派生件与修改标注**：PNG 为上游 DICOM 的派生件，**必须声明修改**（CC BY 4.0 §3(a)）：①重编码为 PNG；②header 剥离以去标识（S-01…S-12）；③`case_id` 重编号。修改声明文本见 §8.3。
>
> **可加限制禁止**：本项目不得对上游层施加比 CC BY 4.0 更严格的条件（如禁止商用、要求单独授权）；gated 发布若含额外审批门槛，只能施加于本项目自有层或仅作运营手段，不得表述为许可条件。

---

## 3｜License 矩阵与三方案

| 方案 | L1 + L2（影像/标签） | L3（生成报告） | L4（评测工件） | L5（代码） | 评级 | 前置 |
|---|---|---|---|---|---|---|
| **A 全面开放（单层）** | CC BY 4.0 | CC BY 4.0 | CC BY 4.0 | MIT | **可行**（继承上游 CC BY 4.0；rev1 的"不可接受"评级已撤销） | 无 |
| **B 分层开放**（推荐） | 继承 CC BY 4.0 + 署名 + 修改声明 | CC BY 4.0 | CC BY 4.0 | MIT | **推荐**：法律上不必要，**溯源卫生上必要** | 无（V-A1 已过） |
| **C 仅自有层** | 不发布 | CC BY 4.0 | CC BY 4.0 | MIT | 可行但自伤：放弃配对卖点 | 需改写 claim §5 |

**推荐 B 的理由（rev2 改写）**：不再是法律阻断，而是**溯源卫生**——上游层（影像 + 标签）与自有层（报告 / rubric / 裁定链 / 代码）权利来源不同；分层署名可避免下游混淆"哪些是我们贡献的、哪些继承自 VetXRay"，且**成本≈0**。

- rev1 的硬性前置（"查证完成前不得签署 L1/L2"）**已删除**——查证已完成。
- 方案 A 与 B 的差别仅是呈现方式，**不是许可有效性**；两者在 CC BY 4.0 下均合法。

---

## 4｜同意范围 brief

**事实四条（可核）**

1. 数据非本项目采集；本地为上游公开数据集的镜像副本（F1/F2）。
2. 上游为 CC BY 4.0 开放获取（`access_right=open`）——权利与义务由许可条款承载。
3. 兽医临床影像不落入人体受试者保护法规的"个人数据"范围；本地亦无同意文书与伦理批号（F3）。
4. 本项目未获得任何**额外**同意，**上游许可亦不要求**。

**结论**：本项目不代上游声明同意范围；公开文本只声明"按 CC BY 4.0 再分发 + 未获额外同意"。

**拟用英文句（签发版）**

> Images and labels are redistributed under CC BY 4.0, as licensed by the upstream VetXRay record (DOI: 10.5281/zenodo.19051776); no additional consent was obtained by this project, and none is required by the upstream license terms.

---

## 5｜DICOM 是否 gated 发布 → **否**（不变）

理由四条：

1. B3 §1 已默认不发布；无输出消费者。
2. `S-09` UID 重映射**未实现、未验证**（无脚本、无二次复核路径），签 gated 等于签一个不存在的流程。
3. gated 需要请求—审批—留痕机制，W7 无承载（C 阶段无此模块）。
4. DICOM 的再识别面严格大于 PNG（私有标签、像素域设备指纹），而基准用途（文本层评测）不需要 DICOM。

> 注：许可确证后，DICOM 的阻碍已从"权利"转为"工程与最小必要"；结论不变。若将来需要，作为 **W8+ 独立工单**。

---

## 6｜PNG-only 双轨 → 保留 A 轨，B 轨不立项（不变）

| 轨 | 内容 | 判定 |
|---|---|---|
| **A（唯一发布轨）** | PNG（7,695，metadata 全量扫描仅 `dpi`）+ `manifest_7695.csv`（4 列）+ 生成报告 + rubric/DADJ/errata + 脚本 | ✅ 保留 |
| **B（DICOM gated）** | scrub 后 DICOM + UID 重映射 | ❌ 不立项（见 §5） |

---

## 7｜`split` 是否随 manifest 发布 → **不发布**（不变）

1. `manifest_7695.csv` 列 schema 已在 B3 冻结为 4 列，加列需重开 schema。
2. 发布 W6 评测划分会泄漏评测切分，并诱导第三方在该划分上调参（与"数据集不做排行榜"的用途边界冲突）。
3. 无用途收益：使用者可按 `case_id` 自行派生划分。

→ 若后续确有需要，作为**独立 artifact**（不由本次包携带），且必须标注"非评测划分"。

---

## 8｜拟发布 license 元数据（rev3 签发文本）

### 8.1 Zenodo 记录字段

```text
Title:            W7-VetXRay-Report — 7,695 label-conditioned, model-generated
                  veterinary thoracic-radiograph reports
Resource type:    Dataset
License:          cc-by-4.0        # 数据集整体（分层说明写入 description，见 8.3）
Access right:     open
Related identifiers: isDerivedFrom → 10.5281/zenodo.19051776 (VetXRay, CC BY 4.0)
```

> **单记录单许可**：Zenodo 每条记录只允许一个 license。代码（MIT）不进本记录，走 GitHub；若必须同记录发布代码，须整体保留 CC BY 4.0，不得双许可并列。

### 8.2 Hugging Face dataset card 前置字段

```yaml
license: cc-by-4.0
license_name: cc-by-4.0
license_link: https://creativecommons.org/licenses/by/4.0/
# Applies to the dataset as a whole. Layer split and attribution: see
# "Rights and provenance" below. Code lives in GitHub under MIT.
```

### 8.3 Attribution 块（拟入 dataset card 与 Zenodo description，英文）

> **Contains data from:** Banzato, T., Burti, S., Zotti, A., & Wodzinski, M., *VetXRay – A Dataset of 9,882 Manually Annotated Canine and Feline Thoracic Radiographs with Lesion and Image Quality Annotations*, Zenodo, DOI 10.5281/zenodo.19051776 (concept DOI 10.5281/zenodo.18999729), licensed under CC BY 4.0. Images re-encoded to PNG from the upstream DICOM distribution with all DICOM headers stripped for de-identification (modifications noted per CC BY 4.0 §3(a)).
>
> **Rights and provenance.** Images and labels are redistributed under CC BY 4.0 as licensed by the upstream VetXRay record. The project-created layers — the `case_id` mapping, the structured manifest, the model-generated reports, the evaluation rubric, the adjudication register and all evaluation code — are released by this project under CC BY 4.0 (text and artifacts) and MIT (code). The reports were generated by GLM-5.3-Flash from ground-truth labels alone; they are not clinical records and no original reports exist.
>
> **Mirror status.** This release mirrors the upstream record 19051776. Auxiliary files (loader script, tag spreadsheet) are MD5-verified against the upstream record; bundle MD5s are recorded from the upstream API.
>
> （若 V-A1-b 五包流式 md5 执行通过，本句升级为 `all eight upstream files MD5-verified`。）

### 8.4 GitHub 仓库

```text
LICENSE              → MIT（L5 代码）
THIRD_PARTY_NOTICES  → 上游 VetXRay 出处 + DOI 10.5281/zenodo.19051776 + CC BY 4.0 全文链接
DATA_LICENSE.md      → 分层说明（§2 分层表 + §8.3 两段 + 修改声明）
```

---

## 9｜裁决记录（rev2 签 R1–R4；rev3 补 V-A1）

| # | 事项 | 裁决 | 状态 |
|---|---|---|---|
| R1 | 方案选择 | **B（分层开放）**，理由＝溯源卫生 | ✅ 已签 |
| R2 | 代码 license | **MIT** | ✅ 已签 |
| R3 | 上游查证失败默认动作 | **注销**（`discharged_by_fact_update`）——前提已证伪 | ✅ 已注销 |
| R4 | L3 报告 license 表述 | **CC BY 4.0 + AI 生成声明** | ✅ 已签 |
| V-A1 | 镜像版本对账（发布前必过） | a 强制层 3/3 md5 命中；c 结构层 5↔5；b 可选未执行 | ✅ 通过（§14） |

---

## 10｜分支不变性检查（三方案下相同）

| 决定 | 在 A / B / C 下是否相同 | 状态 |
|---|---|---|
| DICOM 不发布（§5） | 相同 | ✅ 已定 |
| `split` 不发布（§7） | 相同 | ✅ 已定 |
| `patient_id` / `filename` / 聚合列不发布 | 相同（B3 已定） | ✅ 已定 |
| L4 / L5 由本项目授权 | 相同（只差 license 类型） | ✅ 已定 |
| **上游层必须署名 + 附 CC BY 4.0 链接 + 标注修改** | 相同（法定） | ✅ 已定 |
| 发布文本不得将上游层表述为本项目原创 | 相同 | ✅ 已定 |

---

## 11｜STOP 条件（rev3）

1. 任何发布文本**漏署名**、未附 CC BY 4.0 许可链接，或未声明修改（重编码 / header 剥离 / 重编号）→ **STOP**。
2. 任何发布文本把上游层表述为**本项目原创**，或对上游层附加额外限制 → **STOP**。
3. 任何发布文本出现 B2 禁语（"0.8 逐例门槛"、"judge 漏 17 例"、"门通过"）→ **STOP**。
4. **V-A1-a 任一 md5 不匹配**（`Image upload.py` / `File list with tags.xlsx`）→ **STOP**：意味着本地副本与上游不同源，须回到溯源裁决，不得发布。
5. 声称"校验和级一致 / checksum-verified"而 V-A1 未提供对应层的 md5 对账 → **STOP**。
6. 实际 license 元数据与本文件签发版不一致 → **STOP**。
7. 发布前 API 复核发现上游许可已变更 → **STOP**。

---

## 12｜与 C5 / C7 / C9 的接口

- **C5**：本文件签发版 SHA 与 B3 两件（manifest、redaction log）同批入冻结清单（五件收全）。
- **C7**：DOI 元数据的 license 字段只能取 §8 文本，不得临场改写；`isDerivedFrom` 关系必须写入。
- **C9**：A3 对照表回填引用日期时，须同时引用 §1 F2 的 API 核验记录（2026-11-13）与 V-A1 的镜像状态。

---

## 13｜签发栏

| 项 | 状态 |
|---|---|
| §1 事实表（F2 已确证） | ✅ 签发 |
| §2 三层矩阵 + 派生件修改标注 | ✅ 签发 |
| §3 方案选择（R1＝B，理由溯源卫生） | ✅ 签发 |
| §4 同意范围 brief 与英文句 | ✅ 签发 |
| §5 DICOM 不发布 | ✅ 签发 |
| §6 PNG-only 单轨 | ✅ 签发 |
| §7 `split` 不发布 | ✅ 签发 |
| §8 license 元数据与 Attribution 块 | ✅ 签发 |
| §9 R2 / R3（注销）/ R4 | ✅ 签发 |
| §14 V-A1 对账（a/b/c 三层，rev3） | ✅ 通过（V-A1-1 已撤销） |

---

## 14｜V-A1 镜像对账（rev3：三层核验）

| 层 | 内容 | 时间成本 | 状态 |
|---|---|---|---|
| **V-A1-a（强制）** | 本地伴生文件 md5 对账（`Image upload.py`、`File list with tags.xlsx`） | 秒级 | ✅ **3/3 命中**（§14.1） |
| **V-A1-b（可选，非阻断）** | 五包流式 md5（`curl -sL <links.self> \| md5sum`，不落盘） | ~40.8 GB 传输 | ⏸ 未执行（执行方自酌） |
| **V-A1-c（结构 + 计数链）** | 目录 ↔ 包 5↔5、影像 / 标注 / DICOM 计数 | 已完成 | ✅ 通过（§14.2） |

### 14.1 V-A1-a 逐项结果（2026-11-13）

| 本地文件 | 字节 | 本地 MD5 | 上游 MD5 | 结果 |
|---|---|---|---|---|
| `data/Image_upload.py` | 3,843 | `eb20afca83b2aa1ef6a0c3adbc2ae126` | `eb20afca83b2aa1ef6a0c3adbc2ae126` | ✅ |
| `data/File_list_with_tags.xlsx` | 419,755 | `45c46fd5af3e562dadeeafc198c9a628` | `45c46fd5af3e562dadeeafc198c9a628` | ✅ |
| `data/Image_upload.ipynb`（附加项） | 5,380 | `510538550ac2d81af15260905a5e6506` | `510538550ac2d81af15260905a5e6506` | ✅ |

- **标签溯源闭环完成**：counts（9,882）→ `File_list_with_tags.xlsx`（md5 命中上游）→ 上游记录 `files[]`。
- **红线说明**：上游公开的 `File list with tags.xlsx` 本身含 **9,969 个 `PatientName`**；本项目发布比上游更严——该文件禁入发布包（B3 §1）。attribution 义务不受影响。
- 三层文件（loader 脚本、标签表、notebook）全部逐字节同源，说明本地副本确为上游发布件副本，而非二次加工版本。

### 14.2 V-A1-c 结构对账

| 检查 | 结果 |
|---|---|
| 目录 ↔ 包 | 本地 RX_1…RX_5 **5 个目录** ↔ 上游 **5 个包**，**1:1 对应** |
| 影像计数 | 本地 9,973 ↔ 上游描述 9,973 |
| 标注计数 | dog 7,442 + cat 2,440 = **9,882** ↔ 记录标题 9,882 |
| DICOM 计数 | **10,234**（RX_1 2,267 / RX_2 2,571 / RX_3 2,625 / RX_4 1,671 / RX_5 1,100） |
| 获取日期 | DICOM mtime 2026-08-13；PNG 2026-11-02 |
| 本地包体 | 仅 `.motrix` 分片（14.7–19.7 MB，末 22 字节无 EOCD）→ 包级 md5 无法本地计算，故 b 层只能流式对账 |

### 14.3 更正与撤销记录（如实修正，不回写历史）

| 项 | rev2 记录 | rev3 更正 |
|---|---|---|
| RX_5 md5 | `6ac1853c…` | `8949ed8d6ef01dd50a60e664d0e3fd24`（原值实为条目 UUID 前缀） |
| 上游包数 | 3 包（RX_2/4/5.zip） | **5 包**（RX_1…RX_5）+ 3 个伴生文件 = **8 文件** |
| 版本称谓 | "v2" | 唯一已发布版本（`index:1, is_last:true`） |
| V-A1-1 | 本地 5 目录 vs 上游 3 包的结构差异 | **撤销**：5↔5 对应，来源疑问消解 |

**判定：V-A1 PASS（a + c）；b 未执行，非阻断。** mirror 句按 a 层回填（§8.3）；若日后执行 b 并通过，升级为 "all eight upstream files MD5-verified"。
