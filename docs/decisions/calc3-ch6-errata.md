# 数学学科与「一章 200 条」的达成

> English: [calc3-ch6-errata.en.md](calc3-ch6-errata.en.md)

## 结论

2026-10-20，本库新增「数学」学科（`id` 前缀 `math`，目录 `knowledge/mathematics/`），
并导入 OpenStax《Calculus Volume 3》第 6 章（Vector Calculus）**全部 308 条**
Approved / Textbook 勘误。项目最小目标「一本教材的一章——200 条勘误，跑通 0→200」
在此达成：**同一章 308 条 ≥ 200**。

这是**结构改动**，与《University Physics Volume 1》第 1–5 章的 200 条批次分开记录
（见 [errata-200-scope.md](errata-200-scope.md)）。没有把微积分改标成物理或科学，
没有删改目标，也没有把 `Not An Error` / `Duplicate` 算进来。

## 数据（2026-10-20 快照）

- **书**：Calculus Volume 3（OpenStax，book id 76）；**第 6 章** Vector Calculus。
- **API**：`https://openstax.org/apps/cms/api/errata/?book_title=Calculus%20Volume%203&format=json`
  （公开筛选页 `https://openstax.org/errata/?book=Calculus%20Volume%203`）。
- **筛选**：`resolution = Approved` 且 `resource = Textbook` 且 `location` 含 `Chapter 6`；
  308 条即该章全部符合条件的记录。
- **快照**：[`evidence/calc3-ch6-errata-308.json`](../../evidence/calc3-ch6-errata-308.json)，
  SHA-256 `180047c8a52ff3944e04e4791638ff46609d6b7fbb1e3be00ca14439542671d3`。
- **证据**：`ev-152`（出版社勘误表 · 高 · 全文）。
- **构成**：Typo 138 · 答案/计算 78 · 事实性错误 53 · 被接受的教学建议 36 ·
  Other 2 · Broken link 1。**其中 36 条是教学建议**，不是「正文写错」；每条的性质栏照样标明。
- **状态**：308 条均为 Approved；Completed 306 / Reviewed 2；**298 条 archived**
  （不再出现在公开筛选列表，永久页与 API 仍可核验），305 条有 `corrected_date`。
  记录创建时间从 2016-12-08 到 2026-05-04。
- **许可**：教材为 **CC BY-NC-SA 4.0**（[`osbooks-calculus-bundle/LICENSE`](https://github.com/openstax/osbooks-calculus-bundle/blob/main/LICENSE)）；
  本库只存定位与短引用，不上传教材原文或扫描页。

## 结构改动

1. [`tools/kbcheck.py`](../../tools/kbcheck.py)：`SUBJECT_SLUGS`（`math`）、`SUBJECT_DIRS`
   （`mathematics`）、`SUBJECT_NOTES` / `SUBJECT_NOTES_EN`、`SUBJECT_ORDER`、`SUBJECT_EN`。
2. [`tools/new_entry.py`](../../tools/new_entry.py)：学科表与帮助文本加入「数学」。
3. [`docs/RULES.md`](../RULES.md)：`R-SCHEMA-11` 的 `id` 前缀表加入「数学→math」
   （[English](../RULES.en.md)）。
4. 新目录 `knowledge/mathematics/` 与中英 README、308 对条目（616 个文件）。
5. [`tools/import_openstax_errata.py`](../../tools/import_openstax_errata.py)：从写死物理
   改为 `up1` / `calc3` 两个 profile；补 `Broken link → 链接失效` 映射。
6. 证据登记 `ev-152` 与快照。

**回归**：用 `up1` profile 重生成已有的 200 条，400 个中英文件的 SHA-256 与改动前
**逐字节一致**；`--verify` 仍为 200/200。**复核**：`calc3 --verify` 为 308/308
（中英条目、引用与快照一致、README 登记），见下文「可复算」。

## 每条主张什么

每条只主张「出版方已记录并接受该勘误」，并给出出版方应更正的内容；**不主张当前网页版
仍显示错误文本**，也不主张本库独立复核过正文。308 条中 36 条是教学建议、2 条 Other、
1 条 Broken link——它们不是同一类「错误」，条目的性质栏逐条区分。

## 可复算

```bash
python tools/import_openstax_errata.py --profile calc3 \
    --snapshot evidence/calc3-ch6-errata-308.json --verify
```

输出：`校验 308 条：中英条目 308/308 · 引用与快照一致 308/308 · README 登记 308/308`。
导入器默认 dry-run；`--write` 按文件名幂等，可重复运行。快照、条目与 README 行之间的
对应关系不依赖手工抄写。

## 后果

1. **最小目标达成**：同一章 308 条 ≥ 200，且 0→200 的路径（快照 → 导入 → 中英条目 →
   证据登记 → 学科 README → `kbcheck`）可复算。此前跨五章的 200 条批次仍如实保留。
2. **「5 分钟录入」仍未回答。** 批量导入绕过逐条人工论证；它适用于「出版方已审核的勘误」
   这类来源权威型条目，不能证明普通知识点的录入成本。
3. **`已确证` 仍为 0。** 需要一名非作者的独立复核，单贡献者状态下无法诚实产生。
4. **数学学科目前只覆盖这一章。** 学科说明与 README 都写明了范围；不要把「数学学科存在」
   误读为覆盖整个微积分，更不要把它当作教材质量的一般结论。
