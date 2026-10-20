# 200 条勘误为什么不是「一章」

> English: [errata-200-scope.en.md](errata-200-scope.en.md)

## 结论

2026-10-20，本库录入了 OpenStax《University Physics Volume 1》第 1–5 章的
**200 条** Approved / Textbook 勘误。规模目标「0 → 200」第一次达到。

**但「一章 200 条」没有达成。** 公开的 OpenStax 勘误数据里，**注册学科没有任何一章达到 200 条**。
本库选择**不伪造**：没有把微积分教材改标成物理，没有把 `Not An Error` / `Duplicate` 算进来，
也没有把「一章」偷偷改写成「一本书」。

## 数据（2026-10-20 快照）

OpenStax 公开勘误 API：`https://openstax.org/apps/cms/api/errata/?format=json`
（115 本书，30,155 条记录；其中 `Approved` 20,169 条）。按
`resolution = Approved` 且 `resource = Textbook` 统计，单章最大值：

| 教材 | 最大单章 | 说明 |
|---|---|---|
| Calculus Volume 3 | **308**（第 6 章） | 数学；**本批未采用**（同日另立结构改动，见[后续记录](calc3-ch6-errata.md)） |
| Biology 2e | 55（第 29 章） | 科学类；单章仍不到 200 |
| University Physics Volume 1 | 51（第 2、3 章） | 物理；本批来源 |
| Chemistry 2e | 46（第 1 章） | 科学类 |
| College Physics 2e | 32（第 13 章） | 物理 |

> **这批为什么没有直接用 Calculus Volume 3 第 6 章？**
> 它确实有 308 条，但它是数学教材；当时本库的学科表没有「数学」（`tools/kbcheck.py` 的
> `SUBJECT_SLUGS`），而改学科表不在这次内容批次的范围内。把微积分标成「物理」或「科学」，
> 会让学科统计和 `id` 前缀一起失真——那比数字不达标更糟。
>
> **2026-10-20 同日，本库以单独的结构改动新增了数学学科，并导入该章 308 条**；
> 见 [calc3-ch6-errata.md](calc3-ch6-errata.md)。本批仍按跨五章如实记录。

## 这一批究竟是什么

- **范围**：University Physics Volume 1 **第 1–5 章的全部** Approved / Textbook 勘误
  （31 + 51 + 51 + 48 + 19 = 200）。
- **来源**：每条都有公开永久链接 `https://openstax.org/errata/<id>`；脱敏快照
  [`evidence/openstax-up1-errata-200.json`](../../evidence/openstax-up1-errata-200.json)，
  SHA-256 `2cdba573f779d571cbc34e500fbbc96d61b6e75c3d97c1b365c6e399c1f89da7`。
- **证据**：`ev-150`（出版社勘误表 · 高 · 全文）。
- **构成**：Typo 75 · 答案/计算 49 · 被接受的教学建议 42 · 事实性错误 25 ·
  未分类 5 · 其他 4。**其中 42 条是教学建议**，不是「正文写错」；每条的性质栏照样标明。
- **状态**：200 条均为 Completed / Approved；**196 条已 archived**（公开筛选列表不再显示，
  永久页与 API 仍可核验），193 条有 corrected_date。
- **抽查**：2026-10-20 在浏览器打开 archived 记录 #3502 与 #28659，永久页可达，位置、类型、
  说明与生成条目一致。这是可达性抽查，不是独立内容复核。
- **流程**：快照 → [`tools/import_openstax_errata.py`](../../tools/import_openstax_errata.py)
  → 200 对中英条目 + 学科 README 登记行。`--verify` 可离线逐条核对引用文本、中英配对与
  README 登记（当前 200/200）；这一步是**可复算**的，不是手抄。

## 后果

1. **本批跨五章，不冒充「一章」。** 项目层面的「一章 200 条」已于同日由数学批次达成
   （[calc3-ch6-errata.md](calc3-ch6-errata.md)）；这里保留的是本批的真实范围，不用它去凑目标。
2. **「5 分钟录入」仍未回答。** 批量导入绕过了逐条人工论证；它适用于「出版方已审核的勘误」
   这类来源权威型条目，不能证明普通知识点的录入成本。
3. **每条只主张「出版方已记录并接受该勘误」。** 200 条中 196 条已 archived，不再出现在公开筛选列表里，
   但永久页与 API 仍可核验；条目没有主张「当前网页版仍显示错误文本」。
4. **没有用非勘误充数。** `Not An Error`（3,789 条）、`Duplicate`（3,345 条）与
   Tutor / assessment 记录都排除在外。

## 后续（已于 2026-10-20 同日完成）

本库按这里的建议，以**单独的结构改动**增加「数学」学科（`SUBJECT_SLUGS` / `SUBJECT_DIRS` /
文档 / `RULES` / `new_entry`），再用同一个导入器的 `calc3` profile 导入 Calculus Volume 3
第 6 章全部 308 条。改动、回归与复核记录见 [calc3-ch6-errata.md](calc3-ch6-errata.md)；
本批 200 条文件未受影响（`up1` 重生成后 400 个文件哈希逐字节不变）。
