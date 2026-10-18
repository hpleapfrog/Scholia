---
id: kb:computing:prop-http-404-temporary-vs-permanent-non-disclosure
type: 命题
title: HTTP 404 不说明缺失是暂时还是永久，「不愿披露资源存在」也用它
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「404 到底表示什么」「404 与 410 怎么选」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.5.5**（并对照 §15.5.4）；本条只陈述该节原文，**未核对任何具体服务端实现**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**404（Not Found）的判定对象是「当前表示」：源服务器没找到目标资源的当前表示，或者不愿披露它存在；且 404 不说明缺失是暂时还是永久——确知很可能永久时，规范更偏好 410。**

RFC 9110 §15.5.5 原文（短引用）：

> The 404 (Not Found) status code indicates that the origin server did
> not find a current representation for the target resource **or is not
> willing to disclose that one exists**.  A 404 status code does not
> indicate whether this lack of representation is **temporary or
> permanent**; the 410 (Gone) status code is preferred over 404 if the
> origin server knows, presumably through some configurable means, that
> the condition is likely to be permanent.

同节还规定了缓存行为（短引用）：

> A 404 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

### 「不愿披露」不是孤例：403 也可以选择改报 404

§15.5.4（403 的定义）明说（短引用）：

> An origin server that wishes to "hide" the current existence of a
> forbidden target resource **MAY** instead respond with a status code of
> 404 (Not Found).

也就是说，「404」既可能是「真没有」，也可能是源服务器**主动选择不说**——
规范把这两种情况放在同一个码里。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.5.5**（404 定义、对暂时/永久不表态、与 410 的关系、启发式可缓存）、**§15.5.4**（403 可用 404 隐藏存在，对照） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 404 的定义有两个分支，且刻意不对「暂时/永久」表态（尚无攻击）

- **主张**：404 覆盖两种判定——① 没找到当前表示；② 找到了但不愿披露；
  并且它**不区分**缺失是暂时还是永久
- **前提**：§15.5.5 原文 `or is not willing to disclose that one exists` 与
  `does not indicate whether this lack of representation is temporary or permanent`（ev-054）
- **推理**：
  1. 教程常把 404 说成「资源不存在」——规范说的是「**当前表示**没找到」；
     且配合 §15.5.4 的 MAY，**403 也可以主动改报 404 来隐藏资源存在**——
     「不愿披露」是规范写明的分支，不是实现怪癖
  2. 与 410 的分工见 [410 条目](HTTP410表示很可能永久消失拿不准就应当用404.md)：
     **确知很可能永久才用 410，拿不准就用 404**——404 的「不表态」是设计的一部分
  3. 「启发式可缓存」是规范的默认值，不是实现的义务
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条不保证实现行为，也不给出「何时算不复存在」的判据（尚无攻击）

- **主张**：本条只陈述 404 的规范定义与该节的缓存默认值，
  **不陈述「任何具体服务端为什么返回或不返回 404」**
- **前提**：§15.5.5 与 §15.5.4 均为规范文本（ev-054），本条**没有实测任何服务端**
- **推理**：
  1. 规范与实现的差距在 404 上尤其常见（路由未命中、反代误配、权限隐藏都可能殊途同归）；
     本库没有实现测试的机制
  2. 所以本条**不能被用来主张「我收到的 404 一定是规范意义上的『没有』」**
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.5.5 与 §15.5.4 的原文，不保证任何具体服务端的行为。**
  另外：**本条未核对旧版 RFC（7230–7235）对 404 的表述**。
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：RFC 7230–7235 对 404 的表述；主流服务端把 403/权限隐藏改报 404 的实测

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **「404 表示资源不存在」是噪音——教程都在讲；「404 的定义里还有『不愿披露』分支，且刻意不说暂时还是永久」才是本库该装的。**
>
> 前者背下来也解释不了「为什么同一个 404，有时是没部署，有时是不让你看」；
> 后者才是规范写下的答案。

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；清尾「还缺什么」中「协议侧剩余状态码」缺口——404 的双分支语义与暂久不表态 | ev-054 已登记，核毕 §15.5.5（对照 §15.5.4） | @hpleapfrog |
