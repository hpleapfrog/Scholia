---
id: kb:computing:prop-http-501-not-implemented
type: 命题
title: HTTP 501 表示服务器不支持所需功能，且默认可缓存
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想分清 501、503、405 各自在说什么、或核对「501 该不该缓存」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.6.2（501 定义与缓存）与 §15.6.4（503 对照）、§15.5.6（405 对照）**；本条只陈述各节原文，**未核对任何具体服务端何时返回 501**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**501（Not Implemented）表示服务器不支持完成请求所需的功能**；
它最适当的场合是「服务器**不认识请求方法**，且**任何资源**都不支持它」。501 默认可缓存。

RFC 9110 §15.6.2 原文（短引用）：

> The 501 (Not Implemented) status code indicates that the server does
> not support the functionality required to fulfill the request.  This
> is the appropriate response when the server does not recognize the
> request method and is not capable of supporting it for any resource.

> A 501 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

与 §15.6.4 对照（短引用）：

> The 503 (Service Unavailable) status code indicates that the server
> is currently unable to handle the request due to a temporary overload
> or scheduled maintenance …

### 405、501、503 的三方分工

| 码 | 说的是谁 | 规范里的关键表述 |
|---|---|---|
| **405** | **目标资源**不支持这个方法（服务器**认识**该方法） | 见 [405 条目](HTTP405响应必须带Allow头部且默认可缓存.md) |
| **501** | **服务器**不具备所需功能（**任何资源**都不支持该方法） | `does not support the functionality required` |
| **503** | 服务器**暂时**处理不了（过载 / 计划维护） | `currently unable` · `temporary` |

**405 与 501 的分界在「资源 vs 服务器」；501 与 503 的分界在「缺能力 vs 缺时间」。**

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.6.2**（501 定义、最适当场合、启发式可缓存）、**§15.6.4**（503 对照）、**§15.5.6**（405 对照） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 「任何资源都不支持」是 501 的规范性限定词（尚无攻击）

- **主张**：501 的最适当场合是「方法不被认识，且对**任何资源**都无支持能力」；
  若只是**某个资源**不支持（而服务器认识该方法），那是 405 的场合
- **前提**：§15.6.2 原文 `is not capable of supporting it for any resource`（ev-054）；
  §15.5.6 的 405 定义以「目标资源不支持」为界（ev-054，见 405 条目）
- **推理**：`for any resource` 这个词组把 501 从「资源级」拉开到「服务器级」——
  两个条目互补而不重复，也是本库把这三个码放在一张表里的原因
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 「适当的响应」不是 MUST（尚无攻击）

- **主张**：规范定义了 501 的语义与最适当场合，**不等于「实现必须在该场合返回 501」**
- **前提**：§15.6.2 用 `This is the appropriate response when …`——描述**适当性**而非 MUST（ev-054）
- **推理**：
  1. 「适当的响应」与「必须的响应」在规范里是不同强度的表述；
     实际服务端对未知方法的处理各不相同（本条**未做实测**）
  2. 「501 默认可缓存」是规范的默认值，**不是实现的义务**——
     与 [204](HTTP204响应不能含正文也不能含trailer且默认可缓存.md)、[405](HTTP405响应必须带Allow头部且默认可缓存.md) 是同一类情况
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.6.2 的原文，不保证任何具体服务端的行为。**
  另外：**旧版 RFC 7231 对 501 的表述是否相同，本库未核。**
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：主流服务器对未知请求方法的实测；RFC 7231 §6.6.2 的对照

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **教程只会说「501 = 未实现」；规范还写着三件转述里见不到的事：**
>
> - 它的**最适当场合有明确条件**——「任何资源都不支持」才归 501（只差一个资源的是 405）；
> - 它**默认可缓存**；
> - 与 503 的分工是「**缺能力 vs 缺时间**」——一个不支持，一个稍后再来。
>
> 核对这三条，用的是 §15.6.2 的两段原文——这才是本库该装的。

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；填补「还缺什么」中「其余具体码」缺口——501 与 503 的分工 | ev-054 已登记，核毕 §15.6.2、§15.6.4 与 §15.5.6 | @hpleapfrog |
