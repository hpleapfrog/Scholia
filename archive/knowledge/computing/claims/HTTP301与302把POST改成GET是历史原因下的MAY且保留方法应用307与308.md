---
id: kb:computing:prop-http-301-302-post-to-get-is-historical-307-forbids-method-change
type: 命题
title: HTTP 301/302 把 POST 改成 GET 是「历史原因」下的 MAY，规范要求保留方法时应改用 307/308
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「301/302 会把 POST 变成 GET 吗」、或「要保留请求方法该用哪个码」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.4.2、§15.4.3、§15.4.4、§15.4.8、§15.4.9**；本条只陈述该五节原文，**未核对 [CACHING] §4.2.2 的可缓存状态码清单**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**301 与 302 把 POST 改成 GET 是「历史原因」下的 MAY，不是规范的义务；要保留请求方法，规范指向 307 与 308。**

RFC 9110 §15.4.2（`301`）附注（短引用）：

> **Note:** **For historical reasons**, a user agent **MAY** change the request method
> from POST to GET for the subsequent request. If this behavior is undesired, the
> **308 (Permanent Redirect)** status code can be used instead.

§15.4.3（`302`）附注（短引用）：

> **Note:** **For historical reasons**, a user agent **MAY** change the request method
> from POST to GET for the subsequent request. If this behavior is undesired, the
> **307 (Temporary Redirect)** status code can be used instead.

### 307 明写 MUST NOT 改方法

§15.4.8 原文（短引用）：

> The 307 (Temporary Redirect) status code indicates that the target resource resides
> temporarily under a different URI and the user agent **MUST NOT change the request method**
> if it performs an automatic redirection to that URI.

### 303 的设计本身就是「换成 GET/HEAD 去取」

§15.4.4 原文（短引用）：

> A user agent can perform a **retrieval request** targeting that URI
> (**a GET or HEAD request** if using HTTP), which might also be redirected, and present
> the eventual result as an answer to the original request. Note that the new URI in
> the Location header field is **not considered equivalent** to the target URI.

### 规范成对指路：301↔308，302↔307

两条附注给出的替换方案是**成对**的：**不想让 301 把 POST 改成 GET → 用 308；
不想让 302 把 POST 改成 GET → 用 307。**

### 一处不对称：308 的正文没有那句 MUST NOT

**§15.4.8（307）写了 "MUST NOT change the request method"，
§15.4.9（308）的正文没有对应句子**——308 只写了永久 URI 语义、`Location` 与可缓存。
**但 §15.4.2（301）的附注把 308 指定为「不想改方法时的替代方案」**，
所以 308 的意图清楚，只是正文未复述。

### 缓存的写法也不对称

**§15.4.2（301）与 §15.4.9（308）明写 "heuristically cacheable"；
§15.4.3（302）、§15.4.4（303）、§15.4.8（307）没有对应句子。**
（本条**不主张** 302/303/307 不可缓存——[CACHING] §4.2.2 未核。）

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.4.2**（301 与历史原因附注、可缓存）、**§15.4.3**（302 与历史原因附注）、**§15.4.4**（303 的 retrieval request）、**§15.4.8**（307 的 MUST NOT 改方法）、**§15.4.9**（308 与可缓存） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 「301/302 必然把 POST 变成 GET」在规范层面不准确（尚无攻击）

- **主张**：**301/302 改方法是 MAY，且规范自己标注为「历史原因」**；
  **要保证不改方法，应改用 307/308**
- **前提**：§15.4.2 与 §15.4.3 两条附注都以 "**For historical reasons**" 开头，
  并用 "**MAY** change"、"**If this behavior is undesired** … can be used instead"（ev-054）
- **推理**：
  1. 这属于「**标准与官方文档规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. **转述里的「301/302 会把 POST 变成 GET」把 MAY 说成了必然**——
     规范说的是**允许**，而且是**历史包袱**下的允许
  3. 更重要的判据：**规范给出了明确的替代方案**——
     **不想让方法被改，就用 307（临时）或 308（永久）**
  4. 与 [503 的 `Retry-After` 是 MAY](HTTP503的Retry-After是MAY而非MUST且过载时不必用503.md) 同型：
     **规范用 MAY 表示允许，转述把它说成义务或必然**
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 303 与 307/308 的分工不是「临时 vs 永久」（尚无攻击）

- **主张**：**303 与 307/308 的分工是「是否换一个可单独标识、可书签、可缓存的资源来作答」**，
  不是「临时 vs 永久」
- **前提**：§15.4.4 明写 303 是为了把 POST 的输出**作为一个可 separately identified、
  bookmarked、cached 的资源**提供，并说 Location 的 URI **not considered equivalent**
  to the target URI（ev-054）
- **推理**：
  1. **303 的 Location 指向的不是「同一个资源的新地址」，而是「另一个用来作答的资源」**——
     这与 301/302/307/308 的「资源搬了家」语义不同
  2. 所以**「303 = 临时重定向」是误读**：303 根本不承诺「同一个资源、临时在别处」
  3. 规范对 303 的措辞是 "can perform a **retrieval request**"——
     **它要求换一个 GET/HEAD 去取，而不是「把原请求原样重发」**
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.4.2–§15.4.9 五个小节的原文，不保证任何具体客户端或服务端的行为。**
  「301/302 的 MAY」是规范措辞，不是实测。
  另外：**本条未核对 [CACHING] §4.2.2 的可缓存状态码清单**，
  因此**不主张 302/303/307 是否可缓存**；
  **§15.4.9（308）正文确实没有 "MUST NOT change the request method" 这句**，
  本条如实记录这一不对称，**不替规范补全**。
  另外：**本条未核对旧版 RFC（7230–7235）对 301/302 的表述**，
  也**未核对 [RFC 7231] 中「历史原因」指的具体是什么**。
- **署名**：@hpleapfrog · 2026-10-13
- **待补**：[CACHING] §4.2.2 的可缓存状态码清单；RFC 7230–7235 对 301/302/303 的表述；「历史原因」的具体所指

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一篇 HTTP 教程都会告诉你「301/302 会把 POST 变成 GET，307/308 保留方法」，但不会告诉你规范把 301/302 的改方法写成 MAY 且标注为「历史原因」，也不会告诉你 307 用的是 MUST NOT 而 308 的正文没有那句。**
>
> 后三条都是规范里的措辞，转述里几乎见不到：
> **「MAY + 历史原因」说明 301/302 改方法是历史包袱而非设计目标；
> 「307 是 MUST NOT，308 正文没这句」是规范文本的不对称；
> 「303 指向的不是同一个资源」则拆掉了「303 = 临时重定向」这个误读。**
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 「301/302 变 GET，307/308 保留」是噪音——教程都在讲；
> 「改方法是 MAY 且属历史原因、307 是 MUST NOT、308 正文无此句、303 指向另一个资源」——
> 这几条藏在 RFC 9110 §15.4.2–§15.4.9 的附注与 MUST NOT 里，**才是本库该装的。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-13 | 建立条目；填补「还缺什么」中「RFC 9110 §15.2–§15.6 其余各具体码」缺口的一例（301/302/303/307/308 五码合一条） | ev-054 登记入库后按学科边界选题 | @hpleapfrog |
