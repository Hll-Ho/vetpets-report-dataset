# RELEASE MANIFEST — W7-VetXRay-Report v1.2

- Release date：publication date（本地组装 2026-11-13；v1.1 2026-11-14 复核终版；v1.2 2026-11-15 分卷改 16×≈1 GB）
- Reserved DOI：`10.5281/zenodo.24200927`
- License：CC BY 4.0（数据集整体）；评测代码另行以 MIT 发布
- 文件命名：影像卷成员一律为 `<case_id>.png`，与 `manifest_7695.csv` 的 `case_id` 一一对应
- 本文件自身不入本表（自指不可能）；其 SHA256 记录于项目 CHANGELOG

---

## 1｜影像卷（16）

| 文件 | 字节 | SHA256 |
|---|---|---|
| `W7-VetXRay-Report_images_chunk01.zip` | 1,004,660,889 | `369da4f0776559dec3de26672217e9e415f4cc027d1920b97bd51f892651e9df` |
| `W7-VetXRay-Report_images_chunk02.zip` | 1,003,238,962 | `8ed40d19b71d74ab2e457fd89eddfb9fed936bb0042d4f52d435f22a841e9774` |
| `W7-VetXRay-Report_images_chunk03.zip` | 1,005,136,906 | `7584ebe1c86939f9093155775f7ba0324b7834f63811c78c305dbc35f404bbb6` |
| `W7-VetXRay-Report_images_chunk04.zip` | 1,003,873,271 | `fffb74f3efedc831dcbdbeb8b898ca931971ca22526851bf92cb277793734372` |
| `W7-VetXRay-Report_images_chunk05.zip` | 1,004,967,265 | `75bfbc6e61f60e61d40332a1ce20a83906771d9ce3631456bbcf41379e56ec69` |
| `W7-VetXRay-Report_images_chunk06.zip` | 1,002,058,321 | `bca0380e3cca1234cbbf1405fb29f3aec0bd951ad3d9c356e620bf8333c2b6ed` |
| `W7-VetXRay-Report_images_chunk07.zip` | 1,004,505,890 | `5f08af7a6359bff77edfbb85cfce6484f52e278b3cc53765d631cb973862cc8b` |
| `W7-VetXRay-Report_images_chunk08.zip` | 1,004,953,805 | `0a32532fc6763eb1f4fd326099af51c61a436cc4c8c241a5fdfde84f62ff2870` |
| `W7-VetXRay-Report_images_chunk09.zip` | 1,005,229,615 | `f2549809ff8142c7863858c2cdf3b799c4b649e4dc51acbab8f0de8f1fb58e1d` |
| `W7-VetXRay-Report_images_chunk10.zip` | 1,003,450,947 | `75d10c16eaebdcdc7b5b4436c5bd10c524fc3b274869f48f3381fa80c06022f5` |
| `W7-VetXRay-Report_images_chunk11.zip` | 1,003,574,437 | `dcb161cad0069a09a9db0b0efa6d5a9b722735b8bea72ab14f2c4d675c7b85d2` |
| `W7-VetXRay-Report_images_chunk12.zip` | 1,004,209,724 | `69c21aef39f44de287c5f2295962666757c5d031d3f6f6b9194926f02fc7df55` |
| `W7-VetXRay-Report_images_chunk13.zip` | 1,005,251,313 | `59745979c0ef6565aab942921b78e6eafbbccb919b7eb37e3cdbd998e7487975` |
| `W7-VetXRay-Report_images_chunk14.zip` | 1,003,958,820 | `1daf8f31d45735269f5adc7973bb042e2e7e8aac1ec11633452946e24a3d5ec0` |
| `W7-VetXRay-Report_images_chunk15.zip` | 1,005,266,195 | `d7361419d0dee8cc7d281d1c5b68479e33b8d75a91264f84a46bf56f502ba6e8` |
| `W7-VetXRay-Report_images_chunk16.zip` | 1,024,935,529 | `cf6a1af515074e697548ca3b0eee6c2de8605a69f41480055eb2e381a82b0e14` |

合计 16,089,271,889 B；每卷约 1 GB（最小 1,002,058,321 B，最大 1,024,935,529 B）；成员 7,695 个，分卷为**独立可解压 zip**，无需拼接；成员名一律 `<case_id>.png`。

> 分卷方案于 2026-11-15 由 3×≤10 GB 改为 16×≈1 GB：原方案单卷过大，弱网环境下无法在上传窗口内完成且不支持断点续传。内容零变更，仅切分粒度不同。

## 2｜数据文件（4）

| 文件 | 字节 | SHA256 | 说明 |
|---|---|---|---|
| `manifest_7695.csv` | 167,433 | `ca206ea8788326c75ae777dda6a4d8d12fafe6eba66060f15b63a6e3d1ff520a` | 7,695 行 × 4 列 |
| `reports_7695.jsonl` | 11,681,449 | `93ab0faca283b27682e85d33dbed4a4e7407a49d703384844638b1d7057832e6` | 7,695 份报告全文 |
| `redaction_log.jsonl` | 170,062 | `39bafc4fa206f9c873e3ac0c9cbba1ab891c49443c85ada4936641c9c72e78ec` | 770 例抽样记录，不含原值 |
| `bundle_index.json` | 4,522 | `5844055fcd3668751d4c0d652068c1835dc076a530ee10a33e654cbcfdf714a1` | 分卷 → case 区间与条数 |

## 3｜规范与声明（5）

| 文件 | 字节 | SHA256 |
|---|---|---|
| `rubric_GREEN_VET_v1.1.md` | 21,673 | `fd7ede2ddb9a28fe8b165cd75342c46cf3d7abfcbd398d4fa321b43ef5f1296f` |
| `DADJ_ERRATA_REGISTER.md` | 3,025 | `09c5cf682b7b5b13b16439557da7a53264d87d167c0e26d3c0fdfe556c447fb1` |
| `REDACTION_MANIFEST_W7.md` | 8,771 | `d0c4c7890398a82fad855d802727f267882c007e4673fcaa706d2a0a3a5796d8` |
| `CLAIM_W7.md` | 10,423 | `30c3e021ba2cc88df1665ce5c4dea6f5c5a227f805ea1372ff2b94d39ec4675f` |
| `RIGHTS_AND_RELEASE_BRIEF_W7.md` | 19,417 | `1cae93a88bc283178be3b451e8c1621bd1b00d61bd587f1fdc7fd4d1e11c1779` |

## 4｜复核记录（3）

| 文件 | 字节 | SHA256 | 状态 |
|---|---|---|---|
| `MANUAL_REVIEW_110_PROTOCOL.md` | 5,698 | `a09d8696ae09ca7dbb3749eed998bb3ecb9e70afa9438b0b6880e31410c59681` | issued |
| `manual_review_110.csv` | 3,587 | `e570447bde936c14bdac6bb7f43089c4a1c21e3a8a8a354a8458cf934c082f91` | completed（110 / 110 CLEAN） |
| `manual_review_110_result.json` | 2,136 | `5ed3fe7654a5ec9069ee7e0e643794b8de687ed1eea2502de11a52d0ef5843f1` | completed（PASS） |

## 5｜脚本与证据（6）

| 文件 | 字节 | SHA256 |
|---|---|---|
| `replay_v11.py` | 17,365 | `b6d1d1b0b1303cf0d5f722ad7d6e36f6ef194f8da2d2bb4c642d802d788e7970` |
| `replay_v11_result.json` | 9,793 | `e671217909db9fc37d68897e3328110d3c05c2f78c0fc92993f776813d377bf0` |
| `build_release_b3.py` | 6,434 | `1490e76fef42e7db16026a3b1f0898e55811ae597d271c4348b98120c957a7fe` |
| `b3_report.json` | 837 | `2c67e34379ff4b568faa669022a41ddcdfbd4dc3eedce55edc9d2cc47365fe29` |
| `build_bundles.py` | 3,438 | `e8236f6a108be871f32fbcaad01bb0f0066c6d5a073d8dfb269c7af2ca2c07bb` |
| `vp1_result.json` | 1,041 | `35fb7db02c0aff2643bef6b6b0eef23fe70726a27bd7c7b2712d0a9b90f26e45` |

## 6｜本包自述（2）

| 文件 | 字节 | SHA256 | 说明 |
|---|---|---|---|
| `NAME_MAPPING.csv` | 2,368 | `b7402daa768b35dd83685b538e4428381bc9bfacd6969f1c8cb38b81b71d46c5` | 冻结档案名 → 发布名，含改名记录 |
| `REPRODUCIBILITY.md` | 3,213 | `c94f6ab66b0bd37930763db59a2c115f9e2f8af278676737f31bcac89d5ce82a` | 可验证项 / 不可复现项 / 路径适配 |

---

## 7｜校验

```bash
# 将下表存为 SHA256SUMS 后执行
sha256sum -c SHA256SUMS
```

```text
369da4f0776559dec3de26672217e9e415f4cc027d1920b97bd51f892651e9df  W7-VetXRay-Report_images_chunk01.zip
8ed40d19b71d74ab2e457fd89eddfb9fed936bb0042d4f52d435f22a841e9774  W7-VetXRay-Report_images_chunk02.zip
7584ebe1c86939f9093155775f7ba0324b7834f63811c78c305dbc35f404bbb6  W7-VetXRay-Report_images_chunk03.zip
fffb74f3efedc831dcbdbeb8b898ca931971ca22526851bf92cb277793734372  W7-VetXRay-Report_images_chunk04.zip
75bfbc6e61f60e61d40332a1ce20a83906771d9ce3631456bbcf41379e56ec69  W7-VetXRay-Report_images_chunk05.zip
bca0380e3cca1234cbbf1405fb29f3aec0bd951ad3d9c356e620bf8333c2b6ed  W7-VetXRay-Report_images_chunk06.zip
5f08af7a6359bff77edfbb85cfce6484f52e278b3cc53765d631cb973862cc8b  W7-VetXRay-Report_images_chunk07.zip
0a32532fc6763eb1f4fd326099af51c61a436cc4c8c241a5fdfde84f62ff2870  W7-VetXRay-Report_images_chunk08.zip
f2549809ff8142c7863858c2cdf3b799c4b649e4dc51acbab8f0de8f1fb58e1d  W7-VetXRay-Report_images_chunk09.zip
75d10c16eaebdcdc7b5b4436c5bd10c524fc3b274869f48f3381fa80c06022f5  W7-VetXRay-Report_images_chunk10.zip
dcb161cad0069a09a9db0b0efa6d5a9b722735b8bea72ab14f2c4d675c7b85d2  W7-VetXRay-Report_images_chunk11.zip
69c21aef39f44de287c5f2295962666757c5d031d3f6f6b9194926f02fc7df55  W7-VetXRay-Report_images_chunk12.zip
59745979c0ef6565aab942921b78e6eafbbccb919b7eb37e3cdbd998e7487975  W7-VetXRay-Report_images_chunk13.zip
1daf8f31d45735269f5adc7973bb042e2e7e8aac1ec11633452946e24a3d5ec0  W7-VetXRay-Report_images_chunk14.zip
d7361419d0dee8cc7d281d1c5b68479e33b8d75a91264f84a46bf56f502ba6e8  W7-VetXRay-Report_images_chunk15.zip
cf6a1af515074e697548ca3b0eee6c2de8605a69f41480055eb2e381a82b0e14  W7-VetXRay-Report_images_chunk16.zip
369da4f0776559dec3de26672217e9e415f4cc027d1920b97bd51f892651e9df  W7-VetXRay-Report_images_chunk01.zip
8ed40d19b71d74ab2e457fd89eddfb9fed936bb0042d4f52d435f22a841e9774  W7-VetXRay-Report_images_chunk02.zip
7584ebe1c86939f9093155775f7ba0324b7834f63811c78c305dbc35f404bbb6  W7-VetXRay-Report_images_chunk03.zip
fffb74f3efedc831dcbdbeb8b898ca931971ca22526851bf92cb277793734372  W7-VetXRay-Report_images_chunk04.zip
75bfbc6e61f60e61d40332a1ce20a83906771d9ce3631456bbcf41379e56ec69  W7-VetXRay-Report_images_chunk05.zip
bca0380e3cca1234cbbf1405fb29f3aec0bd951ad3d9c356e620bf8333c2b6ed  W7-VetXRay-Report_images_chunk06.zip
5f08af7a6359bff77edfbb85cfce6484f52e278b3cc53765d631cb973862cc8b  W7-VetXRay-Report_images_chunk07.zip
0a32532fc6763eb1f4fd326099af51c61a436cc4c8c241a5fdfde84f62ff2870  W7-VetXRay-Report_images_chunk08.zip
f2549809ff8142c7863858c2cdf3b799c4b649e4dc51acbab8f0de8f1fb58e1d  W7-VetXRay-Report_images_chunk09.zip
75d10c16eaebdcdc7b5b4436c5bd10c524fc3b274869f48f3381fa80c06022f5  W7-VetXRay-Report_images_chunk10.zip
dcb161cad0069a09a9db0b0efa6d5a9b722735b8bea72ab14f2c4d675c7b85d2  W7-VetXRay-Report_images_chunk11.zip
69c21aef39f44de287c5f2295962666757c5d031d3f6f6b9194926f02fc7df55  W7-VetXRay-Report_images_chunk12.zip
59745979c0ef6565aab942921b78e6eafbbccb919b7eb37e3cdbd998e7487975  W7-VetXRay-Report_images_chunk13.zip
1daf8f31d45735269f5adc7973bb042e2e7e8aac1ec11633452946e24a3d5ec0  W7-VetXRay-Report_images_chunk14.zip
d7361419d0dee8cc7d281d1c5b68479e33b8d75a91264f84a46bf56f502ba6e8  W7-VetXRay-Report_images_chunk15.zip
cf6a1af515074e697548ca3b0eee6c2de8605a69f41480055eb2e381a82b0e14  W7-VetXRay-Report_images_chunk16.zip
369da4f0776559dec3de26672217e9e415f4cc027d1920b97bd51f892651e9df  W7-VetXRay-Report_images_chunk01.zip
8ed40d19b71d74ab2e457fd89eddfb9fed936bb0042d4f52d435f22a841e9774  W7-VetXRay-Report_images_chunk02.zip
7584ebe1c86939f9093155775f7ba0324b7834f63811c78c305dbc35f404bbb6  W7-VetXRay-Report_images_chunk03.zip
fffb74f3efedc831dcbdbeb8b898ca931971ca22526851bf92cb277793734372  W7-VetXRay-Report_images_chunk04.zip
75bfbc6e61f60e61d40332a1ce20a83906771d9ce3631456bbcf41379e56ec69  W7-VetXRay-Report_images_chunk05.zip
bca0380e3cca1234cbbf1405fb29f3aec0bd951ad3d9c356e620bf8333c2b6ed  W7-VetXRay-Report_images_chunk06.zip
5f08af7a6359bff77edfbb85cfce6484f52e278b3cc53765d631cb973862cc8b  W7-VetXRay-Report_images_chunk07.zip
0a32532fc6763eb1f4fd326099af51c61a436cc4c8c241a5fdfde84f62ff2870  W7-VetXRay-Report_images_chunk08.zip
f2549809ff8142c7863858c2cdf3b799c4b649e4dc51acbab8f0de8f1fb58e1d  W7-VetXRay-Report_images_chunk09.zip
75d10c16eaebdcdc7b5b4436c5bd10c524fc3b274869f48f3381fa80c06022f5  W7-VetXRay-Report_images_chunk10.zip
dcb161cad0069a09a9db0b0efa6d5a9b722735b8bea72ab14f2c4d675c7b85d2  W7-VetXRay-Report_images_chunk11.zip
69c21aef39f44de287c5f2295962666757c5d031d3f6f6b9194926f02fc7df55  W7-VetXRay-Report_images_chunk12.zip
59745979c0ef6565aab942921b78e6eafbbccb919b7eb37e3cdbd998e7487975  W7-VetXRay-Report_images_chunk13.zip
1daf8f31d45735269f5adc7973bb042e2e7e8aac1ec11633452946e24a3d5ec0  W7-VetXRay-Report_images_chunk14.zip
d7361419d0dee8cc7d281d1c5b68479e33b8d75a91264f84a46bf56f502ba6e8  W7-VetXRay-Report_images_chunk15.zip
cf6a1af515074e697548ca3b0eee6c2de8605a69f41480055eb2e381a82b0e14  W7-VetXRay-Report_images_chunk16.zip
ca206ea8788326c75ae777dda6a4d8d12fafe6eba66060f15b63a6e3d1ff520a  manifest_7695.csv
93ab0faca283b27682e85d33dbed4a4e7407a49d703384844638b1d7057832e6  reports_7695.jsonl
39bafc4fa206f9c873e3ac0c9cbba1ab891c49443c85ada4936641c9c72e78ec  redaction_log.jsonl
5844055fcd3668751d4c0d652068c1835dc076a530ee10a33e654cbcfdf714a1  bundle_index.json
fd7ede2ddb9a28fe8b165cd75342c46cf3d7abfcbd398d4fa321b43ef5f1296f  rubric_GREEN_VET_v1.1.md
09c5cf682b7b5b13b16439557da7a53264d87d167c0e26d3c0fdfe556c447fb1  DADJ_ERRATA_REGISTER.md
d0c4c7890398a82fad855d802727f267882c007e4673fcaa706d2a0a3a5796d8  REDACTION_MANIFEST_W7.md
30c3e021ba2cc88df1665ce5c4dea6f5c5a227f805ea1372ff2b94d39ec4675f  CLAIM_W7.md
1cae93a88bc283178be3b451e8c1621bd1b00d61bd587f1fdc7fd4d1e11c1779  RIGHTS_AND_RELEASE_BRIEF_W7.md
a09d8696ae09ca7dbb3749eed998bb3ecb9e70afa9438b0b6880e31410c59681  MANUAL_REVIEW_110_PROTOCOL.md
e570447bde936c14bdac6bb7f43089c4a1c21e3a8a8a354a8458cf934c082f91  manual_review_110.csv
5ed3fe7654a5ec9069ee7e0e643794b8de687ed1eea2502de11a52d0ef5843f1  manual_review_110_result.json
b6d1d1b0b1303cf0d5f722ad7d6e36f6ef194f8da2d2bb4c642d802d788e7970  replay_v11.py
e671217909db9fc37d68897e3328110d3c05c2f78c0fc92993f776813d377bf0  replay_v11_result.json
1490e76fef42e7db16026a3b1f0898e55811ae597d271c4348b98120c957a7fe  build_release_b3.py
2c67e34379ff4b568faa669022a41ddcdfbd4dc3eedce55edc9d2cc47365fe29  b3_report.json
e8236f6a108be871f32fbcaad01bb0f0066c6d5a073d8dfb269c7af2ca2c07bb  build_bundles.py
35fb7db02c0aff2643bef6b6b0eef23fe70726a27bd7c7b2712d0a9b90f26e45  vp1_result.json
b7402daa768b35dd83685b538e4428381bc9bfacd6969f1c8cb38b81b71d46c5  NAME_MAPPING.csv
c94f6ab66b0bd37930763db59a2c115f9e2f8af278676737f31bcac89d5ce82a  REPRODUCIBILITY.md
```

## 8｜说明

- 本清单只列发布件，不含任何内部路径、不含 `case_id` → 源文件名的映射。
- `manual_review_110.csv` 与 `manual_review_110_result.json` 为复核终版：110/110 CLEAN，零标识符（八类全 0）；v1.0 的空白模板 SHA 不再列入本表，历史值见 CHANGELOG。
- 引用裁定分歧登记（DADJ）时必须同时引用同版本的 `DADJ_ERRATA_REGISTER.md`——两份文件版本锁定。
