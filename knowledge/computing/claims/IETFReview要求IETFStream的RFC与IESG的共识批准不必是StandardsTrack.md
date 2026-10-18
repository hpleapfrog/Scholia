---
id: kb:computing:prop-ietf-review-ietf-stream-rfc
type: 命题
title: IETF Review 要求 IETF Stream 的 RFC 与 IESG 的共识批准，不必是 Standards Track
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 看到「新值须经 IETF Review」时想知道它比 RFC Required / Standards Action 严在哪，或核对「IETF Review 是否要求 Standards Track」时
  条件: "**适用于 RFC 8126（BCP 26，2017-06）§4.8**（并对照 §4.7、§4.9、§4.11）；本条只陈述注册政策的门槛，**不陈述任何一次具体注册的实际经过，也不覆盖评审所需时间**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-089]
license: CC-BY-SA-4.0
---

## 陈述

**在 IETF Review 政策下，新值只能通过 IETF Stream 的 RFC 分配**——即经 IESG 以 AD 发起或工作组文档的方式推进、**经过 IETF Last Call**、并被 IESG **批准为「具有 IETF 共识」**的 RFC。**任何 RFC 类型都可以**，不必是 Standards Track。

RFC 8126 §4.8 原文（短引用）：

> With the IETF Review policy, new values are assigned only through
> RFCs in the IETF Stream -- those that have been shepherded through
> the IESG as AD-Sponsored or IETF working group documents …, have gone
> through IETF Last Call, and have been approved by the IESG as having
> IETF consensus.

同节的另两句（短引用）：

> Formerly called "IETF Consensus" in the first edition of this
> document.

> Unless otherwise specified, any type of RFC is sufficient (currently
> Standards Track, BCP, Informational, Experimental, or Historic).

§4.11 的严格度阶梯对相邻两档的概括（短引用）：

> 8. IETF Review
>    RFC publication, IETF Stream only, but need not be Standards
>    Track.
>
> 9. Standards Action
>    RFC publication, IETF Stream, Standards Track or BCP only.

### 三个相邻政策的分界

| 政策 | 发布流 | RFC 类型 |
|---|---|---|
| **RFC Required**（§4.7） | IETF / IRTF / IAB / Independent，**任意** | 任意类型 |
| **IETF Review**（§4.8） | **仅 IETF Stream** | **任意类型** |
| **Standards Action**（§4.9） | **仅 IETF Stream** | **仅 Standards Track 或 BCP** |

**两层门槛分开走：先把「发布流」收到 IETF，再把「RFC 类型」收到标准轨道。**
IETF Review 处在中间——它不要标准轨道，要的是**社区评审与 IESG 的共识判定**。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-089 | **官方文件** | **高** | [RFC 8126](https://www.rfc-editor.org/rfc/rfc8126.txt)，BCP 26，2017-06，**§4.8**（IETF Review 的定义与旧名）、**§4.7**（RFC Required 对照）、**§4.9**（Standards Action 对照）、**§4.11**（严格度阶梯） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · IETF Review 不要求 Standards Track（尚无攻击）

- **主张**：IETF Review 的门槛是「IETF Stream 的 RFC + IESG 按 IETF 共识批准」，
  **类型不限**；把 IETF Review 当成「标准轨道审批」是误读
- **前提**：§4.8`Unless otherwise specified, any type of RFC is sufficient`；
  §4.11 对第 8 档的概括 `need not be Standards Track`（ev-089）
- **推理**：
  1. 规范把两个要求分开写：「有评审与共识」与「走标准轨道」是**两条独立门槛**
  2. Standards Action（第 9 档）才是「IETF Stream + Standards Track 或 BCP」——
     如果 IETF Review 已经要求标准轨道，两个政策就没有区别了
- **证据**：ev-089
- **被攻击**：见 A2

### A2 · 本条只给政策门槛，不核「某次注册是否合规」（尚无攻击）

- **主张**：本条陈述政策的**规范定义**；不判断任何一次具体注册走了哪条路，也不给评审时长
- **前提**：§4.8 定义的是「新值分配」的条件；§4.11 另有政策选择的要求——
  选取尽可能宽松的政策、更严的政策要有论证（ev-089）
- **推理**：
  1. 「新值出现在 IETF Stream 的 RFC 里」是**可以从 RFC 出版记录核对**的流程事实；
     本条负责说清门槛，核对某次注册则是读者与注册表的工作
  2. RFC 9110 §16.2.1 对状态码注册要求的就是 IETF Review——
     本条正是那条命题缺的「门槛」一环（见
     [新增 HTTP 状态码须过 IETF Review，且规范明令新码不能禁止正文](新增HTTP状态码须过IETFReview且不能禁止正文.md)）
- **证据**：ev-089
- **被攻击**：**本库未核 RFC 8126 其余章节**（如 §3.4 Early Allocations、§4.13 Provisional Registrations、§5 Designated Experts），
  也未核 IETF 现行实践文件（如 IESG 的 AD 发起流程说明）与 §4.8 文本之间的差异。
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：RFC 8126 其余节；IETF 现行流程文件与 §4.8 的对照

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **「须经 IETF Review」这句话挂在大量注册表上，但门槛原文要翻到 BCP 26 §4.8 才看得到。**
>
> 最容易读错的恰好是两点：**IETF Review 不要求 Standards Track**（Informational、Experimental 等均可）；
> **Standards Action 才要求 Standards Track 或 BCP**。而 RFC Required 连 IETF Stream 都不要求。
> 三个政策并排看，差在哪一目了然——这正是转述里从来不给的三行。

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；填补「还缺什么」中「IETF Review 具体门槛」一项；核毕 RFC 8126 §4.8（并对照 §4.7 / §4.9 / §4.11） | 登记 ev-089（RFC 8126 全文） | @hpleapfrog |
