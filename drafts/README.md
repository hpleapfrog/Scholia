# `drafts/` —— 还没进库的草稿

> **这里的东西不是知识对象。** 不进 `index.json`、不进 `docs/GAPS.md`、不被引用、
> 不被 `R-SCHEMA-*` 管。它只是**没写完或没核完的稿子**，放这儿是为了不丢，不是为了发布。

## 现在有什么

| 文件 | 是什么 | 卡在哪 |
|---|---|---|
| `physics/温度与温标.md` · `temperature-and-scales.en.md` | 物理知识点草稿 | 见下 |
| `physics/分子动理论.md` · `molecular-kinetic-theory.en.md` | 同上 | 见下 |
| `physics/气体实验定律与理想气体状态方程.md` · `gas-laws-and-ideal-gas-equation.en.md` | 同上 | 见下 |

## 为什么被移出来（2026-11-05）

三条草稿原本放在 `knowledge/physics/concepts/`，让 `python tools/kbcheck.py` 报 28 处问题
（缺证据登记、链接指向未建立的文件、学科 README 未登记、索引未重生成）。
**但真正的原因不是这些流程问题，是内容问题。**

草稿里有 **18 条英文引文**（反引号包起来、明确当作「教材原话」用的那种）。
把它们逐条与草稿自己指向的来源——OpenStax《College Physics 2e》第 13 章
（m42214 温度 · m42216 理想气体定律 · m42217 分子动理论）——比对：

> **0 条命中 / 18 条。** 阈值 0.92（近似逐字），最高的一条只有 0.84。

最接近的那一条，恰好说明了这类错误长什么样：

| | |
|---|---|
| 草稿写的 | `Temperature is literally defined as what we measure on a thermometer.` |
| 原文写的 | `Temperature is operationally defined to be what we measure with a thermometer.` |

意思接近，**但草稿把转述放进了引号**。在这套体系里，引号等于「原文如此」——
它比一个明显写错的句子更危险，因为**读起来完全像教材**，而没有任何一条现有规则会发现：
`R-EVID-*` 只查编号登记，`R-LINK-*` 只查链接可达，**它们都不打开来源**。

## 怎么复现

```bash
python tools/quote_check.py drafts/physics/温度与温标.md \
    --source .cache/cp13/m42214.cnxml --source .cache/cp13/m42216.cnxml \
    --source .cache/cp13/m42217.cnxml
```

`tools/quote_check.py` 就是这个缺口补上的工具：把条目里的引文逐条拿到来源正文里找，
找不到就报「最接近的原文句子 + 相似度」。**它只回答「这句话原文里有没有」，不回答「说得对不对」。**

## 要让它们进库，需要做什么

1. 逐条核对引文：原文没有的，**要么改成原文，要么去掉引号改成自己的话**；
2. 按 `templates/` 补 `## 论证`，并登记 `ev-###`（`核验深度` 照实写）；
3. 在 `knowledge/physics/README.md` 的表里登记，然后 `python tools/kbcheck.py --write-index`；
4. 跑一次 `python tools/quote_check.py <条目> --module <m#####>`，**引文全中才提交**。

## 这是第几次

本库记录过自己犯的错，这是第四次，也是第一次**发生在引号里面**：

| # | 错 | 在哪 |
|---|---|---|
| 1 | 40 个文件里的章节号是编出来的 | `evidence/README.md` |
| 2 | 一条「实验数据 · 等级高」的证据其实是作者构造的数据（`ev-002`） | 同上 |
| 3 | 一次「多国教材对比」结论因 n=2 无法归因，被判 `失据` | `llms.txt` |
| 4 | **18 条引文，原文里一句都没有** | 本页 |
