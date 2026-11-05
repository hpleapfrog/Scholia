---
id: kb:computing:prop-http-503-retry-after-is-may-not-must
type: 命题
title: HTTP 503 的 Retry-After 是 MAY 而非 MUST，且服务器过载时规范并不要求必须用 503
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「503 响应必须带 Retry-After 吗」、或「服务器过载时该返回什么状态码」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.6.4 与 §15.6.2**；本条只陈述该两节原文，**未核对 [CACHING] §4.2.2 的可缓存状态码清单**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**503（Service Unavailable）的 `Retry-After` 是 MAY，不是 MUST；服务器过载时，规范并不要求必须返回 503。**

RFC 9110 §15.6.4 原文（短引用）：

> The 503 (Service Unavailable) status code indicates that the server is currently
> unable to handle the request due to a **temporary** overload or **scheduled** maintenance,
> which will likely be alleviated after some delay. The server **MAY** send a
> **`Retry-After`** header field (Section 10.2.3) to suggest an appropriate amount of
> time for the client to wait before retrying the request.

同节附注（短引用）：

> **Note:** The existence of the 503 status code **does not imply that a server has to use
> it when becoming overloaded**. Some servers might **simply refuse the connection**.

### 503 的定义是窄的：只覆盖「临时过载」与「计划内维护」

§15.6.4 的定义只列了两种情形：**temporary overload** 与 **scheduled maintenance**，
并要求 "which will likely be alleviated after some delay"。
**「随便一个服务端错误」不属于 503 的定义范围**——那是 500。

### 对照：501 反而显式写了可缓存，503 没有

§15.6.2（`501 Not Implemented`）末段明写：

> A 501 response is **heuristically cacheable**; i.e., unless otherwise indicated
> by the method definition or explicit cache controls (see Section 4.2.2 of [CACHING]).

**§15.6.4 对 503 没有对应的句子。**

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.6.4**（503 定义、`Retry-After` 的 MAY、过载时不必用 503 的附注）与 **§15.6.2**（501 的 heuristically cacheable） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 「503 必须带 Retry-After」在规范层面站不住（尚无攻击）

- **主张**：**`Retry-After` 对 503 是 MAY，不是 MUST**——
  一个不带 `Retry-After` 的 503 **不违反规范**
- **前提**：§15.6.4 原话是 "The server **MAY** send a `Retry-After` header field
  … **to suggest** an appropriate amount of time"（ev-054）
- **推理**：
  1. 这属于「**标准与官方文档规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. **MAY 是 RFC 2119 里最低强度的许可词**——
     规范说的是「可以发来**建议**一个等待时长」，不是「必须发」
  3. 与 [401 必带 `WWW-Authenticate`](HTTP401必须带WWW-Authenticate头部且401与403的分工不是没登录对没权限.md)
     和 [304 必带 `ETag` 那组头部](HTTP304响应必须带上原200会发的缓存头部且不能含正文或trailer.md)
     **正好相反**：那两处用的是 **MUST**，此处用的是 **MAY**
  4. **判据**：**「503 必须带 Retry-After」是一条常见的错误转述**；
     规范的原话是 MAY，而且用途是 "**suggest**"（建议），不是义务
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 过载时「不必用 503」是规范自己的附注（尚无攻击）

- **主张**：**服务器过载时，规范并不要求必须返回 503**——
  规范明说可以**直接拒绝连接**
- **前提**：§15.6.4 的 Note 原文："The existence of the 503 status code
  **does not imply that a server has to use it when becoming overloaded**.
  Some servers might **simply refuse the connection**."（ev-054）
- **推理**：
  1. 这是一条**附注（Note）**——**规范自己在提醒读者不要过度解读**
  2. 于是**「过载 = 503」不是规范的义务，而是规范允许的一种做法**：
     **拒绝连接（连 TCP 都不接）同样是合规的**
  3. 这条附注的位置很说明问题：**它紧跟在 503 的定义之后**——
     规范写完 503，立刻补一句「别以为过载就得用它」
  4. 与 [410 的「不必标记所有永久不可用资源」](HTTP410表示很可能永久消失拿不准就应当用404.md)同型：
     **规范在两个地方都主动交回了裁量权**
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.6.4 与 §15.6.2 的原文，不保证任何具体服务端的行为。**
  「`Retry-After` 是 MAY」是规范要求，不是实测。
  另外：**本条未核对 [CACHING] §4.2.2 的可缓存状态码清单**，
  因此**不能主张「503 不可缓存」**——只是 §15.6.4 没有像 §15.6.2 对 501 那样写
  "heuristically cacheable"。
  另外：**本条未核对 RFC 9110 §10.2.3（`Retry-After` 字段本身）的语法**，
  也**未核对旧版 RFC（7230–7235）对 503 的表述**。
- **署名**：@hpleapfrog · 2026-10-13
- **待补**：[CACHING] §4.2.2 的可缓存状态码清单；RFC 9110 §10.2.3；RFC 7230–7235 对 503 的表述；主流服务端 503 响应带 `Retry-After` 的实测

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一篇 HTTP 教程都会告诉你「503 表示服务不可用，应当带 Retry-After」，但不会告诉你规范用的是 MAY 而不是 MUST，也不会告诉你规范附注说过载时可以连 503 都不用、直接拒绝连接。**
>
> 后两条都是规范里的一句话，转述里几乎见不到：
> **「MAY 而非 MUST」决定了一个不带 `Retry-After` 的 503 是不是违规；
> 「过载时不必用 503」则是规范自己在提醒读者别过度解读——同一份规范里，401 和 304 用的是 MUST，503 用的是 MAY。**
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 「503 表示服务不可用，应当带 Retry-After」是噪音——教程都在讲；
> 「`Retry-After` 是 MAY、用途是 suggest、过载时可直接拒绝连接、501 反而显式可缓存」——
> 这几条藏在 RFC 9110 §15.6.4 与 §15.6.2 的几句 MAY / Note 里，**才是本库该装的。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-13 | 建立条目；填补「还缺什么」中「RFC 9110 §15.2–§15.6 其余各具体码」缺口的一例 | ev-054 登记入库后按学科边界选题 | @hpleapfrog |
