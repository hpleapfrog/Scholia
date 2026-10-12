---
id: kb:computing:prop-http-status-code-extensibility
type: 命题
title: 未识别的 HTTP 状态码按该类 x00 处理，超出 100–599 的按 5xx 处理，原因短语只是建议
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「收到一个不认识的 HTTP 状态码该怎么处理」、或「能不能靠 reason phrase 判断响应」时
  条件: **仅适用于 RFC 9110（2022-06）§15 前言**；本条只陈述总则，**§15.2–§15.6 各具体码的定义本库未逐条核**
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

RFC 9110 §15 前言写明了状态码的**可扩展性规则**。四条（短引用）：

| # | 规则 | 原文短引用 |
|---|---|---|
| 1 | **首位数字决定类别，后两位没有分类作用** | "The **first digit** of the status code defines the class of response. **The last two digits do not have any categorization role.**" |
| 2 | **客户端不必认识每一个码，但必须认识类别**；未识别码按该类 `x00` 处理 | "a client is **not required to understand the meaning of all registered status codes** … However, a client **MUST understand the class** of any status code … and **treat an unrecognized status code as being equivalent to the x00 status code of that class**" |
| 3 | **100..599 之外的值是非法的**；收到非法码按 `5xx` 处理 | "Values outside the range **100..599 are invalid**" … "A client that receives a response with an **invalid status code SHOULD process the response as if it had a 5xx** (Server Error) status code" |
| 4 | **原因短语只是建议**，可替换可省略 | "The reason phrases listed here are **only recommendations** — they **can be replaced by local equivalents or left out altogether** without affecting the protocol" |

规范给的例子（第 2 条）：

> if a client receives an unrecognized status code of **471**, it can see from the first digit that
> there was something wrong with its request and **treat the response as if it had received a 400
> (Bad Request)** status code.（§15 前言）

三条类别定义本身（首位数字）：

| 首位 | 类别 | 规范给的定义 |
|---|---|---|
| 1 | Informational | "The request was received, continuing process" |
| 2 | Successful | "The request was successfully received, understood, and accepted" |
| 3 | Redirection | "Further action needs to be taken in order to complete the request" |
| 4 | Client Error | "The request contains bad syntax or cannot be fulfilled" |
| 5 | Server Error | "The server failed to fulfill an apparently valid request" |

> [!IMPORTANT]
> **合起来是一句话：状态码的语义由「数字 + 首位类别」决定，不由字符串决定。**
>
> 第 4 条把 `Not Found` 这类 reason phrase 排除在协议之外——**它可替换、可省略、不影响协议**。
> 所以 **`if (reason === "Not Found")` 这类判断在协议层没有依据**；
> 而第 2 条意味着，**一个客户端只要实现了类别回退，就可以正确处理它从没见过的码**。
>
> 这两条一起说明：**HTTP 的状态码是可扩展的数字分类系统，不是一张封闭的字符串表。**

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高**（对该类主张而言） | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15 前言**（15 之前的状态码总则部分；本库核了原文；§15.2–§15.6 各具体码未逐条核） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 四条规则都写在总则里，不需要推断（尚无攻击）

- **主张**：未识别码按该类 `x00` 处理、非法码按 `5xx` 处理、reason phrase 只是建议
- **前提**：四条均为 §15 前言的明文，其中第 2、3 条还配了例子（471 → 400）与
  非法区间的界定（100..599）（ev-054）
- **推理**：
  1. 这属于「**规范规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. 它**可被读者点开 §15 前言逐句核对**
  3. **这三条是「可扩展性」得以成立的机制**：
     没有第 2 条，任何新码都会让旧客户端崩掉；
     没有第 3 条，`600+` 这类实现内部码会被误读成某个真实类别。
     规范**同时**给了回退规则和兜底规则，这是成对设计的
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条只陈述总则，没有核对任何具体码，也没有核对任何实现（尚无攻击）

- **主张**：本条声明的是「**总则怎么规定**」，
  **不声明「某个具体码是什么意思」、也不声明「某个客户端实际怎么做」**
- **前提**：§15.2–§15.6 逐个定义了 1xx–5xx 的具体码，
  而**本库只核了 §15 前言**（ev-054）
- **推理**：
  1. 「`418` 到底存不存在」「`451` 是什么意思」——**这些问题本库一条都没查**
  2. 「某个浏览器 / 某个 HTTP 库收到 `471` 会不会真的按 `400` 处理」——
     **本库没有核对任何实现**
  3. 所以本条**不能被用来支持「任何具体码的含义」**，
     也不能被用来支持「我的客户端已经实现了类别回退」
- **证据**：ev-054
- **被攻击**：**本库没有核对 §15.2–§15.6 里任何一个具体状态码的定义。**
  「`204` 为什么不能有正文」「`306` 为什么标着 Unused」——
  这些在规范里都有答案，**而本库一行都没读**。
  另外：**本库没有查 IANA 的 HTTP Status Code Registry**（§15.1 提到的那张表），
  也没有核对 §16.2 的注册流程。规范说未识别码按 `x00` 处理，
  但**哪些码已被注册、哪些还没有，本库不知道。**
- **署名**：@hpleapfrog · 2026-10-12
- **待补**：§15.2–§15.6 各具体码逐条核对；IANA HTTP Status Code Registry 的当前内容

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一份 HTTP 教程都会附一张状态码表，但不会写出「不认识的码按该类 x00 处理」。**
>
> 你在教程里能看到的是 **一张列着 200/404/500 的表格**；
> 规范里写的是 **这张表是开放的、客户端该怎样处理表外的码、以及为什么字符串不参与协议**。
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 这个对比就是判据：**具体码的含义，本库不必重复（到处都是，且本条也未核）；
> 决定「表外的码怎么办」的那套规则，才是本库该装的。**
> 「收到 471 该做什么」——这个问题在任何状态码表里都找不到答案，
> 而规范把它写成了一个可查的规则：**看首位，然后当 400 处理。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-12 | 建立条目；本学科第三条 `命题`；把 `ev-054` 的核验范围从三节扩到四节（新增 §15 前言） | ev-054 已登记，按学科 README「还缺什么」指明的优先项扩核 §15 | @hpleapfrog |
