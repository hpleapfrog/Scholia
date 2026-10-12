---
id: kb:computing:prop-http-status-code-list-lives-in-iana
type: 命题
title: HTTP 状态码的完整清单在 IANA 注册表，不在 RFC 9110 里
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「某个 HTTP 状态码是不是标准的」、或「这份 RFC 是不是完整的状态码表」时
  条件: "**适用于 IANA 注册表 2025-09-15 版**；本条只陈述该版注册表的内容，**未核对任何更早或更晚的版本**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054, ev-057]
license: CC-BY-SA-4.0
---

## 陈述

**RFC 9110 的 §15 不是完整的状态码表。** 完整清单在 **IANA 的
「Hypertext Transfer Protocol (HTTP) Status Code Registry」**，注册表自己写明：

| 项 | 值 |
|---|---|
| 注册程序 | **IETF Review** |
| 参考 | **RFC 9110, Section 16.2.1** |
| Last Updated | **2025-09-15** |

RFC 9110 §15.1 也承认了这一点（短引用）：

> **Additional status codes, outside the scope of this specification**, have been specified for use in HTTP.
> All such status codes **ought to be registered** within the "Hypertext Transfer Protocol (HTTP) Status Code Registry"…

### 注册表里不在 RFC 9110 中的码（举其要者）

| 码 | 名称 | 出处 |
|---|---|---|
| `102` | Processing | RFC 2518 |
| `103` | Early Hints | RFC 8297 |
| `104` | Upload Resumption Supported | draft-ietf-httpbis-resumable-upload-05（**临时注册**，见下） |
| `207` | Multi-Status | RFC 4918 |
| `208` | Already Reported | RFC 5842 |
| `226` | IM Used | RFC 3229 |
| `423` | Locked | RFC 4918 |
| `424` | Failed Dependency | RFC 4918 |
| `425` | Too Early | RFC 8470 |
| `428` / `429` / `431` / `511` | Precondition Required / Too Many Requests / Request Header Fields Too Large / Network Authentication Required | 均 RFC 6585 |
| **`451`** | **Unavailable For Legal Reasons** | **RFC 7725** |

### 三个容易读错的条目

| 码 | 注册表怎么写 | 含义 |
|---|---|---|
| `306` | **`(Unused)`** | RFC 9110 §15.4.7：**"no longer used, and the code is reserved"**（旧版定义过，已停用并保留） |
| `418` | **`(Unused)`** | 出自愚人节 RFC 2324，因被部署得太多而保留——见[418 不是规范里的状态码](../误解/418不是规范里的状态码.md) |
| `104` | **"TEMPORARY - registered 2024-11-13, extension registered 2025-09-15, expires 2026-11-13"** | **这是一个会过期的码**。到期后它可能被移除 |

> [!IMPORTANT]
> **`104` 是一个带到期日的状态码。**
>
> 注册表给它写了三个日期和一个 `expires`。
> 也就是说：**判断「104 是不是标准码」这个问题，答案取决于你什么时候问。**
>
> 这是[经济](../../经济/README.md)学科那条「**时效是主要攻击点**」规则
> 在计算机学科的一个实例——**本库记录的是 2025-09-15 那一版的注册表**，
> 而这个条目自己写明了 2026-11-13 会变。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-057 | **官方文件** | **高** | [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)，**Last Updated 2025-09-15**，**整张表** | 官方公开注册表 · **仅引用条目与短引用，不转载整表** |
| ev-054 | **官方文件** | **高**（对该类主张而言） | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.1**（"Additional status codes, outside the scope of this specification"） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 完整清单是注册表，不是任何一份 RFC（尚无攻击）

- **主张**：要判断某个状态码是否标准，**查注册表，不要查 RFC 9110**
- **前提**：注册表列出 100–599 全部条目及其 Reference；RFC 9110 §15.1 自己说
  有"outside the scope of this specification"的状态码应当注册进该表（ev-057, ev-054）
- **推理**：
  1. 这属于「**规范与官方文档规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. 它**可被读者点开注册表逐条核对**
  3. **上一条命题（未识别码按 `x00` 处理）的边界由此确定**：
     「未识别」不等于「不存在」——`451` 不在 RFC 9110 里，但它是注册在案的标准码。
     一个只实现了 RFC 9110 §15 的客户端**会把 `451` 当成 `400` 处理**，
     这是规范允许的，但**不等于 `451` 不标准**
- **证据**：ev-054, ev-057
- **被攻击**：见 A2

### A2 · 本条只陈述 2025-09-15 那一版注册表（尚无攻击）

- **主张**：本条声明的是「**2025-09-15 版注册表里有什么**」，
  **不声明「现在注册表里有什么」**
- **前提**：注册表自己标了 `Last Updated 2025-09-15`，
  且 `104` 条目明写 **expires 2026-11-13**（ev-057）
- **推理**：
  1. 注册表会变：新码会加进来，临时码会到期。**本库没有版本探测机制**
  2. `104` 的到期日**在本条目写下之后不到一年**，
     到期后**本条目关于 104 的表述可能就错了**
  3. 所以本条**不能被用来支持「截至今天注册表仍是这样」**
- **证据**：ev-057
- **被攻击**：**本库只读了 2025-09-15 一版注册表。**
  更早的版本写了什么、以及**本条目写下之后注册表是否已更新**，本库一概不知。
  另外：**本库只核了 RFC 9110 §15.1 与 §15 前言**，
  §16.2 的注册流程原文**没有读**——注册表说参考 §16.2.1，但那一节写了什么本库没核。
- **署名**：@hpleapfrog · 2026-10-12
- **待补**：RFC 9110 §16.2 注册流程原文；注册表在 2025-09-15 之后的更新

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一份 HTTP 教程都会附一张状态码表，但不会写出「这张表的权威版本在别处」。**
>
> 你在教程里能看到的是一张**看起来封闭**的表；
> 规范里写的是**这张表是开放的、有独立的注册机构、并且有些码连 RFC 都不在同一份里**。
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 这个对比就是判据：**具体码的含义，本库不必重复；
> 「这张表本身是怎么维护的、到哪里查它的当前版本」才是本库该装的。**
> 「`451` 是不是标准码」——这个问题在 RFC 9110 里找不到答案（它不在那一节），
> 而注册表把它连同出处一起列着：**RFC 7725。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-12 | 建立条目；本学科第四条 `命题` | ev-057 登记入库后按学科边界选题 | @hpleapfrog |
