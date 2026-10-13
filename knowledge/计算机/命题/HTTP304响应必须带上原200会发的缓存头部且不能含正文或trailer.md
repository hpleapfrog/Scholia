---
id: kb:computing:prop-http-304-must-carry-cache-headers-and-no-body
type: 命题
title: HTTP 304 响应必须带上原 200 会发的缓存头部，且不能含正文或 trailer
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「304 响应该带哪些头部」、或「304 响应能不能有正文」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.4.5**；本条只陈述该节原文，**未核对 [CACHING] §4.3.4 对缓存的另行要求**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**304（Not Modified）响应必须带上原 200 响应会发的那组缓存相关头部，且不能含正文或 trailer。**

RFC 9110 §15.4.5 原文（短引用）：

> The server generating a 304 response **MUST** generate any of the following header fields
> that would have been sent in a 200 (OK) response to the same request:
>
> * **Content-Location, Date, ETag, and Vary**
> * **Cache-Control and Expires** (see [CACHING])

同节末段（短引用）：

> A 304 response is terminated by the end of the header section; it
> **cannot contain content or trailers**.

### 304 的语义：把客户端重定向到它自己的缓存

§15.4.5 开头解释了 304 到底在说什么（短引用）：

> The 304 (Not Modified) status code indicates that a conditional GET or HEAD request has
> been received and **would have resulted in a 200 (OK) response if it were not for the fact
> that the condition evaluated to false**. In other words, there is no need for the server to
> transfer a representation of the target resource because the request indicates that the client …
> **already has a valid representation**; the server is therefore **redirecting the client to
> make use of that stored representation as if it were the content of a 200 (OK) response**.

### 头部应尽量少

§15.4.5 还规定了反方向的约束（短引用）：

> a sender **SHOULD NOT** generate representation metadata other than the above listed fields
> unless said metadata exists for the purpose of **guiding cache updates** (e.g., `Last-Modified`
> might be useful if the response does not have an `ETag` field).

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.4.5**（304 定义、MUST 头部清单、正文限制、头部精简要求） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 必带的头部是规范列死的清单，不是建议（尚无攻击）

- **主张**：生成 304 的服务器**必须**带上原 200 会发的
  `Content-Location`、`Date`、`ETag`、`Vary`、`Cache-Control`、`Expires` 这组头部
- **前提**：§15.4.5 明写 "**MUST** generate any of the following header fields"（ev-054）
- **推理**：
  1. 这属于「**标准与官方文档规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. **MUST 是 RFC 2119 里的最高强度词**——这不是"建议带上"，
     而是"不带上就是违反规范"
  3. 实际后果：**一个 304 如果不带 `ETag` 或 `Cache-Control`，
     客户端就无法判断缓存还能用多久**——这是实现违反规范
  4. 规范同时给了**反向约束**（SHOULD NOT）：
     除了那组头部和"用于指导缓存更新"的字段，**不该多发别的**——
     **304 的设计目标就是把传输量压到最小**
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 与 204 同型的「不能含正文或 trailer」（尚无攻击）

- **主张**：304 响应**不能含正文，也不能含 trailer**——
  与 [204](HTTP204响应不能含正文也不能含trailer且默认可缓存.md) 是同一条约束
- **前提**：§15.4.5 末段明写 "it **cannot contain content or trailers**"（ev-054）
- **推理**：
  1. 两个码（一个 2xx 一个 3xx）共用同一条句式，说明这是**规范对"没有正文可传"这类
     响应的一致要求**，不是 204 的特例
  2. 但**304 的语义比 204 强**：204 是"请求成功了、没东西给你"，
     304 是"**你自己已经有那份东西了**，别找我要"——
     304 是**唯一一个把「内容在客户端缓存里」写进语义的状态码**
  3. 所以 304 的头部比 204 更关键：**204 可以什么都不带，304 必须带上那组头部**
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.4.5 的原文，不保证任何具体服务端的行为。**
  「MUST 带那组头部」是规范的要求，不是实现的实测。
  另外：**本条未核对 [CACHING] §4.3.4 对缓存收到 304 后的另行要求**，
  也**未核对旧版 RFC（7230–7235）对 304 的表述**。
- **署名**：@hpleapfrog · 2026-10-13
- **待补**：[CACHING] §4.3.4；RFC 7230–7235 对 304 的表述；主流服务端 304 响应带 `ETag` 的实测

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一篇 HTTP 教程都会告诉你「304 表示内容没变」，但不会告诉你规范用 MUST 要求它必须带 `ETag`、`Cache-Control` 那组头部，而且不能有正文。**
>
> 后两条都是规范里的一句话，转述里几乎见不到：
> **「必须带那组头部」决定了一条 304 是不是完整的；
> 「不能有正文」与 204 同型，说明这是规范对"没正文可传"响应的一致要求。**
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 「304 表示内容没变」是噪音——教程都在讲；
> 「304 必须带那组缓存头部、不能含正文或 trailer、且应当把头部压到最少」——
> 这几条藏在 RFC 9110 §15.4.5 的几句 MUST 与 SHOULD NOT 里，**才是本库该装的。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-13 | 建立条目；填补「还缺什么」中「RFC 9110 §15.2–§15.6 其余各具体码」缺口的一例 | ev-054 登记入库后按学科边界选题 | @hpleapfrog |
