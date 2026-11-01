# 决策记录

> **English: [README.en.md](README.en.md)**

> **规范（[FORMAT.md](../../FORMAT.md)）只写「规则」，本目录放开「为什么」。**
>
> 本库的规范里原本夹着大量案例、事故与推断过程。它们有价值——解释规则怎么来的、
> 防止重犯同样的错——但会让「规范」变得很长，而读者打开规范是来**查规则**的。
>
> 于是：**规则留在 `FORMAT.md`，理由搬到这里。**
> **搬、不删**——删掉痕迹才是真的丢信息（这是本库对待作废证据、编造的节号一贯的态度）。

| 文件 | 讲的是 |
|---|---|
| [readability-rules.md](readability-rules.md) | 面向学习者的三条规矩怎么来的；一次差点变成断言的测量 |
| [procedural-knowledge-boundary.md](procedural-knowledge-boundary.md) | 本库不装「流程」：三次探针、两条判据 |
| [level-marker-inference.md](level-marker-inference.md) | `水平档` 的展开式是**推断**，不是引用 |
| [argument-required-for-all-types.md](argument-required-for-all-types.md) | 为什么六种类型都必须有 `## 论证` |
| [status-and-liveness.md](status-and-liveness.md) | `失据` 的引入、「存活」零攻击、一条被删掉的检查 |
| [support-count-not-strength.md](support-count-not-strength.md) | 为什么「15 条支持」是错误写法；「算不出独立性」里**能算的那一半**（`R-GRAPH-06`）|
| [evidence-history.md](evidence-history.md) | 证据的事故：编出来的节号、`ev-002`、阶梯对物理不公平 |
| [events-are-not-propositions.md](events-are-not-propositions.md) | `事件` 与 `命题` 分开：为什么塞进命题会产生没有攻击点的假论证 |
| [three-machine-files.md](three-machine-files.md) | 机器入口拆成三份：省 token 靠「不读」，不靠「总和更小」 |
| [english-filenames-from-id.md](english-filenames-from-id.md) | 英文文件名从「同名」改成「由 `id` 派生」：为什么「同名」既让英文页用中文名、又让配对无法机械校验 |
| [errata-200-scope.md](errata-200-scope.md) | 200 条勘误为什么跨五章而不是「一章」：公开数据没有注册学科的单章达到 200 条 |
| [calc3-ch6-errata.md](calc3-ch6-errata.md) | 最小目标的达成：新增「数学」学科并导入 Calculus Volume 3 第 6 章 308 条；一次带回归的结构改动 |
| [coverage-is-not-strength.md](coverage-is-not-strength.md) | 覆盖度「有没有」之外的两层「够不够」；一次**假干净**的列序解析，以及专门盯这种形状的回归样本（退回旧实现 → 报平安的路径 4 条变 2 条） |
| [status-zero-is-auditable.md](status-zero-is-auditable.md) | `已确证` / `争议` / `已推翻` 全是 0：守卫让 0 变成**可核对的 0** |
| [out-of-library-prerequisites.md](out-of-library-prerequisites.md) | 库外前置攒到 7 例（Issue #17 的 3–5 例触发条件已过），schema 仍未动 |
| [external-prerequisites-field.md](external-prerequisites-field.md) | 库外前置终于有了字段：为什么是五项结构而非自由文本，七例如何迁入，机器只管声明形状与复发 |
| [entry-cost-phases.md](entry-cost-phases.md) | 录入成本分段实测：中文正文先完，超出的是双语与登记。**门槛单位已定为「双语一条」**（451 墙钟 13 分 16 秒，含一次中断 = 至多 2.6 倍，未达标）；第三次试测把双语尾部拆成四段（代理计时 61 秒，P1→P10 3 分 44 秒，不能当人类读数） |
| [gap-dashboard.md](gap-dashboard.md) | 缺口看板：四个出口共用**一个** `compute()`；什么算缺口、什么只归人判；`index.json` schema 5 的 `覆盖度` / `title_en` |
| [interface-selftest.md](interface-selftest.md) | `kbcheck` 看不见的三个接口：MCP 握手、`make_tasks --json`、`new_entry` 骨架；九条**真起进程**的检查（含复核包只排版、不替人回答） |
