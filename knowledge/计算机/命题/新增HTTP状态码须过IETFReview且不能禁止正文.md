---
id: kb:computing:prop-http-status-code-registration-requires-ietf-review
type: 命题
title: 新增 HTTP 状态码须过 IETF Review，且规范明令新码不能禁止正文
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「新增一个 HTTP 状态码要走什么程序」、或「状态码能不能规定不带正文」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§16.2**；本条只陈述该节原文，**未核对 RFC 8126 §4.8 对 IETF Review 的具体定义**"
edges:
  先修: []
  支持: [kb:computing:prop-http-status-code-list-lives-in-iana]
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**IANA 注册表写的「IETF Review」不是一个模糊说法——RFC 9110 §16.2.1 把它写成了硬性要求。**

§16.2.1《Status Code Registry》原文（短引用）：

> A registration **MUST** include the following fields:
>
> * Status Code (3 digits)
> * Short Description
> * Pointer to specification text
>
> Values to be added to the HTTP status code namespace require **IETF Review** (see [RFC8126], Section 4.8).

### 三条对新码本身的约束

§16.2.2《Considerations for New Status Codes》逐条列出了新码必须满足的条件：

| 约束 | 原文 | 含义 |
|---|---|---|
| **必须落在 §15 已定义的类别里** | "New status codes are required to fall under one of the categories defined in Section 15." | 不能发明第六类——只能是 1xx/2xx/3xx/4xx/5xx 之一 |
| **不能禁止正文** | "new status codes **cannot disallow content**, although they can mandate a zero-length content." | 可以规定"正文必须为空"，但不能规定"不许有正文" |
| **早期草案不该占号** | "early drafts can use a notation such as **`4NN`**, or **`3N0` … `3N9`**" | 未达成共识前用 `4NN` 这类记法，避免过早消耗具体编号 |

### 默认只对单次请求生效

§16.2.2 还规定了作用域（短引用）：

> By default, a status code applies **only to the request corresponding to the response it occurs within**. If a status code applies to a larger scope of applicability … this **must be explicitly specified**.

也就是说：**一个新码即使注册成功，客户端也没有义务把它理解为「对整个资源生效」**——
除非定义文档里明说了。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§16.2.1**（注册字段与 IETF Review）与 **§16.2.2**（新码约束） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 「IETF Review」是硬性门槛，不是建议（尚无攻击）

- **主张**：想把一个数字加进 HTTP 状态码命名空间，**必须过 IETF Review**；
  这不是"建议注册"，而是规范用 **MUST** 和 **require** 写死的
- **前提**：§16.2.1 明写 "A registration **MUST** include…" 与
  "Values … **require** IETF Review"（ev-054）
- **推理**：
  1. 这属于「**标准与官方文档规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. 注册表里那行 "Registration procedure: IETF Review" **不是注册表自己的规定**，
     而是**照抄 RFC 9110 §16.2.1 的要求**——两者是一回事，不是两道独立关卡
  3. 这也解释了为什么 `104` 走的是**临时注册**（Temporary）路径：
     它没过 IETF Review，所以带了 `expires` 到期日（见
     [HTTP 状态码的完整清单在 IANA 注册表，不在 RFC 9110 里](HTTP状态码的完整清单在IANA注册表不在RFC9110里.md)）
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条只陈述 RFC 9110 §16.2，未核对 RFC 8126（尚无攻击）

- **主张**：本条陈述的是 **RFC 9110 §16.2 原文写了什么**
- **前提**：RFC 9110 §16.2.1 在引用 IETF Review 时指向 RFC 8126 §4.8，
  但 **RFC 8126 §4.8 的原文本库没有读**（ev-054）
- **推理**：
  1. "IETF Review" 具体意味着什么样的审查流程、需要多少人同意、
     要多长时间——**RFC 9110 §16.2 只写了"require IETF Review"，没有展开**
  2. 所以本条**不能回答「IETF Review 具体有多难」**
  3. 同理，§16.2.2 里有些用词是 **ought to**（"ought to avoid allocating"、
     "ought to explain"、"ought to specify"）——**这些是建议，不是 MUST**。
     本条把它们标为"约束"是**按规范语气分级**的：表格里的三条硬性约束用的是
     "are required to" / "cannot"，而后面的"应当解释触发条件"类要求**不在本条范围内**
- **证据**：ev-054
- **被攻击**：**本库只读了 RFC 9110 §16.2，没读 RFC 8126 §4.8。**
  「IETF Review 的具体门槛」本条答不了。另外：§16.2.2 后半段还有关于
  **可缓存性声明**（heuristically cacheable）与**内容与资源的隐含关联**
  （implied association with an identified resource，§6.4.2）的要求，
  本条**只取了前三条最硬的约束**，其余未展开。
- **署名**：@hpleapfrog · 2026-10-12
- **待补**：RFC 8126 §4.8 原文；§16.2.2 后半段（缓存性与资源关联）逐条核对

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一篇「怎么注册 HTTP 状态码」的教程都会告诉你"提交 IETF Review"，但不会告诉你规范明令禁止"不带正文"的新码。**
>
> 后者是一个**反直觉的兼容性约束**：规范不允许新码把"我不允许正文"写进定义，
> 因为这会破坏已有解析器——**已有解析器不知道你这个新码，它们默认会尝试读正文**。
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 「走 IETF Review」是流程常识，教程会讲；
> 「新码不能禁止正文，但可以要求正文为空」——这条藏在 RFC 9110 §16.2.2 的一句长句里，
> **转述里几乎见不到**，而它决定了一个新码定义能不能通过审查。

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-12 | 建立条目；填补上一条「待补」中「RFC 9110 §16.2 注册流程原文」的缺口 | ev-054 登记入库后按学科边界选题 | @hpleapfrog |
