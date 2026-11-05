---
id: kb:computing:prop-http-414-uri-too-long
type: 命题
title: HTTP 414 表示目标 URI 过长，且默认可缓存
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「414 什么情况才算」「414 是不是在说客户端写错了什么」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.5.15**；本条只陈述该节原文，**未核对任何具体服务端在什么长度阈值上返回 414**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**414（URI Too Long）表示服务器拒绝处理请求，因为目标 URI 比它愿意解释的长度更长。**

RFC 9110 §15.5.15 原文（短引用）：

> The 414 (URI Too Long) status code indicates that the server is
> refusing to service the request because the target URI is longer than
> the server is willing to interpret.

同节点名的三种典型成因（短引用）：

> This rare condition is only likely to occur when a client has improperly
> converted a POST request to a GET request with long query information,
> when the client has descended into an infinite loop of redirection …

以及缓存行为（短引用）：

> A 414 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

### 414 最常见的成因是「客户端把 POST 写成了 GET」

三种成因里，第一种最值得记住：
**把本应放进请求体的大段信息塞进了 GET 的查询串**——规范用的词是 `improperly converted`（不当转换）。
常见转述只说「URL 太长了」，而规范把矛头指向**请求构造的方式**。
另外两种是**重定向死循环**（重定向后的 URI 前缀指回自己的后缀）与**攻击探测**。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.5.15**（414 定义、三种典型成因、启发式可缓存） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 「用 GET 带长查询参数」是规范点名的首因，不是社区经验（尚无攻击）

- **主张**：POST 被不当转换为带长查询串的 GET，是 §15.5.15 点名的首因；
  重定向死循环与攻击探测是另外两种
- **前提**：§15.5.15 原文 `only likely to occur when a client has improperly converted a POST request to a GET request with long query information`（ev-054）
- **推理**：规范用 `rare condition` 定性 414 的稀少性，并给出三种可核对的场景——
  这是规范文本本身，不是经验总结
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条不给出长度阈值，也不保证实现行为（尚无攻击）

- **主张**：本条只陈述 414 的**定义与典型成因**，**不陈述「超过 N 个字符就该返回 414」**
- **前提**：§15.5.15 用 `longer than the server is willing to interpret` 表述——**阈值由服务器自定**（ev-054）
- **推理**：
  1. 规范没有给出任何具体数字；不同服务器与中间层各有各的限额
  2. 实际系统里，过长的 URI 常被中间层用**别的**方式处理（如更大的 4xx 或直接断开）——
     **这一条是本库的经验观察，未做实测**
  3. 所以本条**不能被用来主张「我收到的 414 是规范要求某服务器返回的」**——它只说明 414 的规范含义
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.5.15 的原文，不保证任何具体实现的行为，也不提供阈值数字。**
  另外：**旧版 RFC 7231 对 414 的表述是否相同，本库未核。**
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：主流服务器与代理的 URI 长度限额实测；RFC 7231 §6.5.12 的对照

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **「414 = URL 太长」到处都看得到；「它默认可以被缓存、且最常见的成因是把 POST 不当改写成 GET」几乎见不到。**
>
> 前者是噪音；后者决定排查方向：**先看请求构造（为什么本该 POST 的东西在查询串里），而不是先怀疑服务器。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；填补「还缺什么」中「其余具体码」缺口——414 的适用场景与成因 | ev-054 已登记，核毕 §15.5.15 | @hpleapfrog |
