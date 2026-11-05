---
id: kb:computing:prop-http-205-reset-document-view-no-content
type: 命题
title: HTTP 205 要求重置「文档视图」，且服务器不得生成正文
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「205 是干什么用的」「205 能不能带正文」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.3.6**；本条只陈述该节原文，**未核对任何具体用户代理的重置行为**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**205（Reset Content）表示服务器已完成请求，并要求用户代理把「文档视图」重置回从源服务器收到时的原始状态；而且既然不打算再给内容，服务器就不得在 205 里生成正文。**

RFC 9110 §15.3.6 原文（短引用）：

> The 205 (Reset Content) status code indicates that the server has
> fulfilled the request and **desires that the user agent reset the
> "document view"**, which caused the request to be sent, to its
> original state as received from the origin server.

同节交代了设计用途（短引用）：

> This response is intended to support a common **data entry use case**
> where the user receives content that supports data entry (a form,
> notepad, canvas, etc.), enters or manipulates data in that space,
> causes the entered data to be submitted in a request, and then the
> data entry mechanism is **reset for the next entry** …

以及禁止正文的硬要求（短引用）：

> Since the 205 status code implies that no additional content will be
> provided, a server **MUST NOT generate content** in a 205 response.

### 与 204 的分工

[204 条目](HTTP204响应不能含正文也不能含trailer且默认可缓存.md) 管的是「没有内容要给你」；
205 更进一步：**不只没有内容，还要求客户端把手上那个"输入界面"清回原样**——
「提交表单后表单清空」的协议化表达。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.3.6**（205 定义、设计用途、不得生成正文） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 205 是唯一「要求客户端重置界面」的码（尚无攻击）

- **主张**：205 的组合语义 = 请求已完成 + **请把文档视图重置** + 不得带正文；
  最后一条是 MUST NOT 级
- **前提**：§15.3.6 引文（ev-054）
- **推理**：
  1. 转述里 205 常被并进「和 204 差不多」，但规范给了它一个明确且独特的目的：
     **数据录入场景的「清空表单」**
  2. 「重置到原始状态」是服务器对**用户代理**提出的动作期望——
     这是 205 区别于其他 2xx 的核心
  3. 「不得生成正文」与 [204](HTTP204响应不能含正文也不能含trailer且默认可缓存.md)
     一样属于硬要求（MUST NOT）
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条不保证用户代理真的会重置（尚无攻击）

- **主张**：本条陈述的是规范对 205 的定义，
  **不陈述「浏览器/客户端一定执行了重置动作」**
- **前提**：§15.3.6 说服务器「desires that the user agent reset」，
  但没有给出实现一致性的保证（ev-054）
- **推理**：
  1. 「文档视图」「原始状态」的边界（表单值？画布？滚动位置？）规范未逐项细化；
     本库没有实现测试的机制
  2. 所以本条**不能被用来主张「收到 205 的页面一定被清空了」**
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.3.6 的原文，不保证任何具体用户代理的行为。**
  另外：**旧版 RFC 7231 §6.3.6 的表述是否相同，本库未核。**
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：RFC 7231 §6.3.6 的对照；主流浏览器对 205 重置行为的实测

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **「205 = 重置内容」是噪音；「它的规范用途是数据录入场景的『清空表单』，且服务器不得带正文」才是本库该装的。**
>
> 知道这一点，205 就不再是「204 的孪生兄弟」——
> **它是一个带着客户端动作要求的码。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；清尾「还缺什么」中「协议侧剩余状态码」缺口——205 的重置语义与正文禁令 | ev-054 已登记，核毕 §15.3.6 | @hpleapfrog |
