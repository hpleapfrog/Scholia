---
id: kb:computing:prop-http-206-partial-content-header-duties
type: 命题
title: HTTP 206 的 Content-Length 不是完整资源长度（全量在 Content-Range），且必须补齐 200 会发的缓存与校验头
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「206 里的 Content-Length 是什么长度」「206 要不要带缓存头」「客户端拿到 206 该检查什么」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.3.7（含 §15.3.7.1–§15.3.7.2）**；本条只陈述这些原文，**未核 §14（Range 请求机制）的完整细节**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**206（Partial Content）表示服务器正用一个或多个「片段」完成范围请求；其中 Content-Length 只是本条消息的字节数（通常不是完整表示的长度），完整长度在每个 Content-Range 里；服务器还必须补齐原本 200 会发的缓存与校验头。**

RFC 9110 §15.3.7 原文（短引用）：

> The 206 (Partial Content) status code indicates that the server is
> successfully fulfilling a **range request** for the target resource by
> transferring one or more parts of the selected representation.

两条常被忽略的义务（短引用）：

> A client **MUST** inspect a 206 response's Content-Type and Content-Range
> field(s) to determine what parts are enclosed and whether additional
> requests are needed.
>
> A server that generates a 206 response **MUST** generate the following
> header fields … if the field would have been sent in a 200 (OK)
> response to the same request: Date, Cache-Control, ETag, Expires,
> Content-Location, and Vary.

关于长度（短引用）：

> A Content-Length header field present in a 206 response indicates the
> number of octets in the content **of this message**, which is usually
> **not the complete length** of the selected representation.  Each
> Content-Range header field includes information about the selected
> representation's **complete length**.

以及缓存行为（短引用）：

> A 206 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by explicit cache controls (see Section 4.2.2 of [CACHING]).

### 单段与多段的硬要求

- 单段（§15.3.7.1）：服务器 **MUST** 生成 Content-Range（短引用）；
- 多段（§15.3.7.2）：**MUST** 用 `multipart/byteranges`，
  外层 HTTP 头里 **MUST NOT** 带 Content-Range（它出现在每个段里），
  且**不得**对「只请求一个范围」的请求生成 multipart（短引用：
  `A server MUST NOT generate a multipart response to a request for a single range`）。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.3.7**（206 定义、客户端与服务器义务、Content-Length 语义、启发式可缓存）、**§15.3.7.1**（单段）、**§15.3.7.2**（多段） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 206 的 Content-Length 与 Content-Range 各管各的长度（尚无攻击）

- **主张**：206 里 Content-Length = **本条消息**的字节数（通常只是片段）：
  完整长度在 Content-Range（如 `bytes 21010-47021/47022` 里的 47022）
- **前提**：§15.3.7 的长度段落与 §15.3.7.1 的样例（ev-054）
- **推理**：
  1. 「Content-Length 就是资源大小」是常见转述——在 206 里**恰恰不成立**；
     下载管理器/断点续传实现搞错这一条会算错总进度
  2. 规范还要求服务器**补齐 200 会发的头**（ETag、Cache-Control、Vary 等）——
     这让 206 可被缓存与再验证，而不是只当一次性片段
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条不展开范围请求机制（尚无攻击）

- **主张**：Range / If-Range 的格式与协商在 §14，multipart/byteranges 的细节在 §14.6——
  **本条未核那些章节**，只陈述 §15.3.7 系里的义务
- **前提**：§15.3.7 多处引用 `Section 14`（ev-054）
- **推理**：
  1. 所以本条**不能被用来主张**「服务器该不该满足某个 Range 请求」之类的行为规则
  2. 「客户端 MUST 检查 Content-Type 与 Content-Range」是规范对客户端的硬要求——
     也意味着一张 206 响应**必须自描述**，不能假设片段与请求一一对应
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.3.7–§15.3.7.2 的原文，不保证任何具体实现的行为。**
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：§14.2 / §14.6（Range 与 multipart/byteranges）的核读；主流 CDN 与静态服务器 206 头实测

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **「206 就是部分内容」是噪音；「CL 不是全量、全量在 Content-Range、必须补齐 200 的缓存头」才是本库该装的。**
>
> 断点续传、下载校验、缓存再验证都踩在这三条上——
> **写错任何一条，症状都不在教程的故障清单里。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；清尾「还缺什么」中「协议侧剩余状态码」缺口——206 的长度语义与头义务 | ev-054 已登记，核毕 §15.3.7–§15.3.7.2 | @hpleapfrog |
