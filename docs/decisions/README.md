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
| [entry-cost-phases.md](entry-cost-phases.md) | 录入成本分段实测：4 分钟到的是中文正文，超出的花在双语与登记。**门槛单位已定为「双语一条」**（墙钟 13 分 16 秒，含一次中断 = 至多 2.6 倍，未达标） |
