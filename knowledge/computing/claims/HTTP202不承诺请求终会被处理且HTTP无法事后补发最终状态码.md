---
id: kb:computing:prop-http-202-no-async-status-resend
type: 命题
title: HTTP 202 不承诺请求终会被处理，且 HTTP 无法事后补发最终状态码
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「202 是不是就是『成功了，稍等』」「任务结果以后怎么通知客户端」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.3.3**；本条只陈述该节原文，**未核对任何具体任务队列或 API 实现**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**202（Accepted）表示请求已被受理但尚未处理完；它「可能被处理、也可能不被处理」；而且 HTTP 没有办法把一个异步操作后来的最终状态码补发回来。**

RFC 9110 §15.3.3 原文（短引用）：

> The 202 (Accepted) status code indicates that the request has been
> accepted for processing, but the processing has not been completed.
> The request **might or might not eventually be acted upon**, as it
> might be disallowed when processing actually takes place.  **There is
> no facility in HTTP for re-sending a status code from an asynchronous
> operation.**

同节对「怎么让用户知道结果」也给了方向（短引用）：

> The 202 response is **intentionally noncommittal**.  Its purpose is to
> allow a server to accept a request for some other process …
> The representation sent with this response **ought to** describe the
> request's current status and point to (or embed) a **status monitor**
> that can provide the user with an estimate of when the request will
> be fulfilled.

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.3.3**（202 定义、不保证处理、无异步补发机制、状态监视器建议） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 202 有三层含义，第三层决定异步设计（尚无攻击）

- **主张**：① 已受理；② **未必真的会被执行**；③
  **HTTP 没有从异步操作里回头补发最终状态码的机制**——
  结果只能靠另外的通道（如规范建议的「状态监视器」）
- **前提**：§15.3.3 原文 `might or might not eventually be acted upon` 与
  `no facility in HTTP for re-sending a status code from an asynchronous operation`（ev-054）
- **推理**：
  1. 教程常说「202 = 请求成功、后台处理中」——规范连「会被处理」都不担保
     （受理时合法、执行时可能被禁止），并明说**没有补发机制**
  2. 因此「任务最终成功/失败」必须由**另行设计的查询/通知通道**表达；
     规范给的方向是 202 的表示里附带或指向状态监视器
  3. 这决定了一个常见架构（提交任务返回 202 + 轮询另一个资源）**不是实现臆造，而是规范逼出来的**
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 「状态监视器」是 ought to，不是 MUST（尚无攻击）

- **主张**：本条不把「202 必须带状态跟踪信息」当成硬要求——
  规范用的是 `ought to`（应当），且「监视器」长什么样规范未定义
- **前提**：§15.3.3 用 `ought to describe … and point to (or embed)` 表述（ev-054）
- **推理**：
  1. RFC 2119 体系里 `ought to` 的强度与「必须」不同
     （参见 [MUST/SHOULD/MAY 全大写规则](RFC要求关键词只有全大写才成立.md)；
     这里甚至不是大写的 SHOULD）
  2. 所以本条**不能被用来主张「没有状态监视器的 202 是违规的」**
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.3.3 的原文，不保证任何具体任务队列或 API 的行为。**
  另外：**旧版 RFC 7231 §6.3.3 的表述是否相同，本库未核。**
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：RFC 7231 §6.3.3 的对照；主流任务 API 的 202 + 轮询模式实测（只登记模式，不评优劣）

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **「202 = 已接受、处理中」是噪音；「HTTP 明说无法事后补发最终状态码」才是本库该装的。**
>
> 这一句解释了异步 API 为什么必须自带「查结果」的第二通道——
> **不是风格问题，是协议能力边界。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；清尾「还缺什么」中「协议侧剩余状态码」缺口——202 的不承诺与无异步补发 | ev-054 已登记，核毕 §15.3.3 | @hpleapfrog |
