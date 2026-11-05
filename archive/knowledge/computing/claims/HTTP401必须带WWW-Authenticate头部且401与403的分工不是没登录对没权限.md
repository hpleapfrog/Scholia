---
id: kb:computing:prop-http-401-vs-403-must-carry-www-authenticate
type: 命题
title: HTTP 401 必须带 WWW-Authenticate 头部，且 401 与 403 的分工不是「没登录 vs 没权限」
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「401 和 403 到底怎么区分」、或「401 响应能不能不带 WWW-Authenticate」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.5.2 与 §15.5.4**；本条只陈述该两节原文，**未核对任何具体框架的 401/403 实现**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**401（Unauthorized）响应必须带 `WWW-Authenticate` 头部；401 与 403 的分工不是「没登录 vs 没权限」。**

RFC 9110 §15.5.2 原文（短引用）：

> The 401 (Unauthorized) status code indicates that the request has not
> been applied because it **lacks valid authentication credentials** for the target
> resource. The server generating a 401 response **MUST** send a **`WWW-Authenticate`**
> header field (Section 11.6.1) containing **at least one challenge applicable to the
> target resource**.

RFC 9110 §15.5.4 原文（短引用）：

> The 403 (Forbidden) status code indicates that the server **understood the request
> but refuses to fulfill it**. … If authentication credentials were provided in the
> request, the server considers them **insufficient** to grant access. The client
> **SHOULD NOT** automatically repeat the request with the same credentials. The client
> **MAY** repeat the request with new or different credentials. **However, a request might
> be forbidden for reasons unrelated to the credentials.**

### 401 的「Unauthorized」是历史用词，不是语义

§15.5.2 的定义说的是 **"lacks valid authentication credentials"（缺少有效的认证凭据）**——
这是**认证（authentication）**失败，不是**授权（authorization）**被拒。
规范自己的措辞是 "the 401 response **indicates that authorization has been refused
for those credentials**"——也就是说 401 **也**可能表示凭据被拒，
但那是因为**凭据本身无效**，而不是「你是谁、你能做什么」的授权判断。

### 403 可以与凭据完全无关

§15.5.4 明写：

> **However, a request might be forbidden for reasons unrelated to the credentials.**

规范还给出了 403 之外的另一个选项（短引用）：

> An origin server that wishes to "**hide**" the current existence of a forbidden
> target resource **MAY instead respond with a status code of 404 (Not Found)**.

### 两个码对客户端的要求不同

| 码 | 客户端行为 |
|---|---|
| **401** | 用户代理 **MAY** 用**新的或替换的** `Authorization` 头部重复请求 |
| **403** | 客户端 **SHOULD NOT** 用**相同**凭据自动重复；**MAY** 用**新的或不同的**凭据重复 |

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.5.2**（401 定义、`WWW-Authenticate` 的 MUST 要求、与 Authorization 头部的关系）与 **§15.5.4**（403 定义、与凭据无关的禁止、可用 404 隐藏存在） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 「401 = 没登录，403 = 没权限」在规范层面站不住（尚无攻击）

- **主张**：401 与 403 的**分工不是「有没有登录」**
  ——**401 是「认证凭据缺失或无效」，403 是「服务器拒绝执行」**，
  而且 **403 明确允许与凭据完全无关**
- **前提**：§15.5.2 的 401 定义是 "lacks valid authentication credentials"；
  §15.5.4 的 403 定义是 "**understood** the request but **refuses** to fulfill it"，
  并明写 "might be forbidden for reasons **unrelated to the credentials**"（ev-054）
- **推理**：
  1. 这属于「**标准与官方文档规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. 转述里的「401 = 没登录，403 = 登录了但没权限」**把「认证」和「授权」当成了两个码的分界**，
     但规范的分界是「**服务器拒绝执行的理由是否与凭据有关**」
  3. 于是**「403 = 你没权限」是最常见的误读**：一个 403 可以是因为
     **IP 在黑名单上、请求方法被禁、资源在维护、或者只是服务器不给你看**——
     **与你是谁、你带着什么凭据无关**
  4. 反过来也成立：**401 可以在你已经带了凭据时出现**——
     规范原话 "If the request included authentication credentials, then the 401
     response indicates that authorization has been refused for those credentials"
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 401 必带 WWW-Authenticate，这是一条可判定的硬约束（尚无攻击）

- **主张**：生成 401 的服务器**必须**带 `WWW-Authenticate` 头部，
  且其中**至少一个 challenge 适用于目标资源**
- **前提**：§15.5.2 明写 "**MUST** send a `WWW-Authenticate` header field … containing
  **at least one challenge applicable to the target resource**"（ev-054）
- **推理**：
  1. **MUST 是 RFC 2119 里的最高强度词**——不带这个头部的 401 **违反规范**
  2. 这给出了一个**可直接核对的判据**：
     **一个 401 响应如果没有 `WWW-Authenticate` 头部，它就不是规范意义上的 401**
  3. 与 [304 必带 `ETag` 那组头部](HTTP304响应必须带上原200会发的缓存头部且不能含正文或trailer.md)同型：
     **规范给某个码列了 MUST 级的头部清单，转述里几乎见不到**
  4. 实际后果：**缺少 `WWW-Authenticate` 的 401 会让客户端无法知道该用哪种认证方案**——
     这是实现违反规范，不是「401 语义变了」
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.5.2 与 §15.5.4 的原文，不保证任何具体框架或服务端的行为。**
  「401 必带 `WWW-Authenticate`」是规范要求，不是实测。
  另外：**本条未核对 11.6.1（`WWW-Authenticate` 字段本身）的语法**，
  也**未核对旧版 RFC（7230–7235）对 401/403 的表述**。
- **署名**：@hpleapfrog · 2026-10-13
- **待补**：RFC 9110 §11.6.1；RFC 7230–7235 对 401/403 的表述；主流框架 401 响应是否带 `WWW-Authenticate` 的实测

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一篇 HTTP 教程都会告诉你「401 是没登录，403 是没权限」，但不会告诉你规范要求 401 必须带 `WWW-Authenticate` 头部，也不会告诉你 403 明确允许与凭据完全无关。**
>
> 后两条都是规范里的一句话，转述里几乎见不到：
> **「必带 `WWW-Authenticate`」给了一个可直接核对的判据——不带这个头部的 401 不是规范意义上的 401；
> 「403 可以与凭据无关」则拆掉了「403 = 你没权限」这个最常见的误读。**
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 「401 没登录，403 没权限」是噪音——教程都在讲；
> 「401 必带 `WWW-Authenticate`、403 可以与凭据无关、403 之外还能用 404 隐藏存在」——
> 这几条藏在 RFC 9110 §15.5.2 与 §15.5.4 的几句 MUST / SHOULD NOT / MAY 里，**才是本库该装的。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-13 | 建立条目；填补「还缺什么」中「RFC 9110 §15.2–§15.6 其余各具体码」缺口的一例 | ev-054 登记入库后按学科边界选题 | @hpleapfrog |
