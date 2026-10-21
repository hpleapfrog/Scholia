---
id: kb:computing:http-451-legal-unavailable
type: 命题
title: HTTP 451 因法律要求拒绝访问且不暗示资源存在与否
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-20
updated: 2026-10-20
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「451 到底是什么」「服务器要不要说明是哪条法律」「451 能不能当作资源不存在的证据」时
  条件: "**适用于 RFC 7725（Standards Track，2016-02，DOI 10.17487/RFC7725）§3–§6 原文**；`451` 在 IANA 注册表里的出处登记为 RFC 7725（**本库核的是 2025-09-15 那一版注册表**，见 ev-057）。本条**不主张**任何具体国家或平台的封锁行为用了 451"
edges:
  先修: []
  支持: ["[命题：完整清单在 IANA 注册表](HTTP状态码的完整清单在IANA注册表不在RFC9110里.md#a1)"]
  攻击: []
evidence: [ev-153, ev-054, ev-057]
license: CC-BY-SA-4.0
---

## 陈述

**451 只说明一件事：服务器因为收到法律要求而拒绝访问这个资源。它不说明资源存在还是不存在，客户端也不能依赖它一定出现——而它的定义不在 RFC 9110 里，在 RFC 7725。**

| 451 主张什么 | 451 **不**主张什么 |
|---|---|
| 拒绝访问是**法律要求的结果**（§3） | 资源**存在或不存在**（§3 原文：既不暗示存在也不暗示不存在） |
| 拒绝方**可能不是源服务器**（§3：ISPs、搜索引擎最直接） | 客户端**一定能绕过**（§3 承认 VPN / Tor 常常还能访问） |
| 响应**应当**说明是哪一方、哪条法律、适用于哪些人与资源（§3） | 这套说明**必须**写全（§3 用 SHOULD，不是 MUST） |
| 默认**可缓存**（§3） | 一定带上封锁方标识（§4 是 SHOULD + 一处 MUST，见下） |

> [!NOTE]
> **上面这张表是本库的归纳，不是 RFC 7725 的结构**——原文没有「主张 / 不主张」两栏。
> 每一格都能在下面找到对应的原文句子；**找不到的那一格就是脑补**，请照 `R-GRAPH-02` 的路子攻击它。

逐条对应原文（短引用，中文说明在前）：

拒绝的原因是法律要求（§3 第一句）：

> This status code indicates that the server is denying access to the
> resource as a consequence of a legal demand.

拒绝方可能不是源服务器（§3）：

> The server in question might not be an origin server.  This type of
> legal demand typically most directly affects the operations of ISPs
> and search engines.

响应体里应当写清「谁提的、依据哪条法、覆盖哪些人和哪些资源」（§3）：

> Responses using this status code SHOULD include an explanation, in
> the response body, of the details of the legal demand: the party
> making it, the applicable legislation or regulation, and what classes
> of person and resource it applies to.

**这一句划出了 451 与「资源找不到」之间的界线**（§3）：

> The use of the 451 status code implies neither the existence nor
> nonexistence of the resource named in the request.  That is to say,
> it is possible that if the legal demands were removed, a request for
> the resource still might not succeed.

默认缓存性（§3 末段）：

> A 451 response is cacheable by default, i.e., unless otherwise
> indicated by the method definition or explicit cache controls; see
> [RFC7234].

标识封锁方（§4）——**这里是唯一的 MUST**：

> When an entity blocks access to a resource and returns status 451, it
> SHOULD include a "Link" HTTP header field [RFC5988] whose value is a
> URI reference [RFC3986] identifying itself.  When used for this
> purpose, the "Link" header field **MUST** have a "rel" parameter whose
> value is "blocked-by".

同一节还写明这个头指向的是**实施**封锁的一方，不是**要求**封锁的一方（§4，短引用）：

> The intent is that the header be used to identify the entity actually
> implementing blockage, not any other entity mandating it.

客户端不能依赖它出现（§5）：

> Clients cannot rely upon the use of the 451 status code.  It is
> possible that certain legal authorities might wish to avoid
> transparency, and not only demand the restriction of access to
> certain resources, but also avoid disclosing that the demand was
> made.

### 为什么这条要单独记，而不是并进[那条注册表命题](HTTP状态码的完整清单在IANA注册表不在RFC9110里.md)

`451` 的定义文本只存在于 RFC 7725。**读 RFC 9110 读不出 451 的任何语义**——
§15.5 的小节列表末项是 `15.5.22. 426 Upgrade Required`（本库 2026-10-20 复算，见 A2）。
所以「451 是什么」与「451 是不是标准码」是**两个问题、两份来源**：

| 问题 | 要去读哪里 | 本库的证据 |
|---|---|---|
| 451 **是什么意思**、响应该怎么写 | RFC 7725 §3–§5 | ev-153 |
| 451 **是不是注册过的码**、出处是谁 | IANA 注册表（RFC 7725 的 §6 写了它已登记） | ev-057 · ev-153 §6 |
| RFC 9110 里**有没有** 451 | RFC 9110 §15.5 小节列表 | ev-054 |

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-153 | 官方文件 | 高 | IETF / RFC Editor，**RFC 7725**《An HTTP Status Code to Report Legal Obstacles》（T. Bray, Textuality），Standards Track，2016-02，DOI 10.17487/RFC7725，**§1–§7 全文已核**（283 行 / 9,309 字节，SHA-256 `5817efa6…20b1`） | 官方公开规范 · **仅引用条款号与短引用，不转载全文** |
| ev-054 | 官方文件 | 高 | RFC 9110（STD 97）§15.5 小节列表，**2026-10-20 复算**：`rfc-editor.org/rfc/rfc9110.txt` 10,785 行、SHA-256 `21c1cdce…232a`，与 ev-054 登记时一致 | 官方公开规范 · 仅引用条款号与短引用 |
| ev-057 | 官方文件 | 高 | IANA HTTP Status Code Registry，Last Updated **2025-09-15**，`451 / Unavailable For Legal Reasons / RFC 7725` 那一行 | 官方公开注册表 · 仅引用条目 |

## 论证

### A1 · 语义直接来自规范文本（尚无攻击）

- **主张**：451 的四条规则（法律要求所致 · 不暗示存在与否 · SHOULD 说明法律细节 · 默认可缓存）与一条 MUST（`Link` 头的 `rel="blocked-by"`）如正文所列
- **前提**：ev-153 §3、§4、§5 的原文句子，正文已逐条引用
- **推理**：这些是**规范文本的直陈**，本条只做「按原文归集」，没有加推断；唯一的推断是把 §4 的 SHOULD/MUST 分开列——它对应原文里两个不同的助动词
- **证据**：ev-153
- **被攻击**：尚无攻击。**不要读本条为「服务器应当怎么做」**——RFC 7725 只定义状态码，不构成实施建议
- **署名**：@hpleapfrog · 2026-10-20

### A2 · 读 RFC 9110 读不出 451（尚无攻击）

- **主张**：`451` 不在 RFC 9110 定义的状态码里，因此关于它的任何语义都必须另找来源
- **前提**：① ev-054——RFC 9110 §15.5 的小节列表止于 `15.5.22. 426 Upgrade Required`，正文全文检索 `451` **命中 0 次**（2026-10-20 复算，同一 SHA-256 与行数）；② ev-153 §6 把 IANA 注册表的更新内容原文写出（`Code: 451 … Specification: RFC 7725`）
- **推理**：一份「标准清单」如果不包含 451，而 451 又确实是注册过的码，那么清单的**完备性在 RFC 9110 之外**——这正是[那条注册表命题](HTTP状态码的完整清单在IANA注册表不在RFC9110里.md)A1 主张的结构，本条给它一个**独立来源**（RFC 7725，而非 RFC 9110 或 IANA 表本身）的实例
- **证据**：ev-153 · ev-054 · ev-057
- **被攻击**：尚无攻击。**本条只主张 2022-06 版 RFC 9110 与 2016-02 版 RFC 7725 的文本状态**；后续版本若把 451 并入，本条的 A2 需要复审
- **署名**：@hpleapfrog · 2026-10-20

> [!IMPORTANT]
> **A2 是本库「支持」边的一个诚实样本**：它支撑的不是「451 很重要」，
> 而是「清单不在一份 RFC 里」这条结构主张。
> 按 `R-GRAPH-06`，一条支持边的强度取决于**它带来的证据是否是新来源**——
> 这一条带来的是 ev-153（RFC 7725），与该命题原有的 ev-054、ev-057 **不是同一份材料**。

## 怎么反驳它

- [ ] 找到 RFC 7725 之后**取代**它的文档（若有，本条的版本限定即失效）
- [ ] 证明 §15.5 的小节列表之外，RFC 9110 正文另有对 451 的定义或规范性引用
- [ ] 指出正文把 SHOULD 读成了义务（§3 的说明要求是 SHOULD，不是 MUST）

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-20 | 建立条目；登记 ev-153；按 §3–§6 归集四条规则与一条 MUST | ev-153 · ev-054 · ev-057 | @hpleapfrog |
| 2026-10-20 | 加一条 `支持` 边指向[注册表命题](HTTP状态码的完整清单在IANA注册表不在RFC9110里.md)的 A1；复算 RFC 9110 文本（行数与哈希与 ev-054 一致） | A2 | @hpleapfrog |
| 2026-10-20 | **订正本条的 RFC 7725 标题**：原先写成了凭记忆的版本（《An HTTP Status Code for Indicating Denials of Access…》），**不是原文标题**；按 ev-153 登记行与下载文件头部订正为《An HTTP Status Code to Report Legal Obstacles》 | ev-153 | @hpleapfrog |
