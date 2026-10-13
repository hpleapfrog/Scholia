---
id: kb:computing:prop-http-204-cannot-contain-content-or-trailers
type: 命题
title: HTTP 204 响应不能含正文也不能含 trailer，且默认可缓存
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「204 响应能不能带正文」、或「204 响应默认可不可以缓存」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.3.5**；本条只陈述该节原文，**未核对 RFC 7230–7235 等旧版对 204 的表述**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**204（No Content）响应由头部区结束即告终止——它不能含正文，也不能含 trailer。**

RFC 9110 §15.3.5 原文（短引用）：

> A 204 response is terminated by the end of the header section; it
> **cannot contain content or trailers**.

同节还规定了缓存行为（短引用）：

> A 204 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

### 204 允许带什么

§15.3.5 举的例子说明了 204 的用途（短引用）：

> if a 204 status code is received in response to a PUT request and the response contains an **ETag** field, then the PUT was successful and the ETag field value contains the entity tag for the new representation

也就是说：**204 不带正文，但可以带描述新表示的头部字段**——
`ETag` 是规范自己举的例子。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.3.5**（204 定义） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 「不能含正文」是硬约束，「不能含 trailer」是同一条句子里的第二半（尚无攻击）

- **主张**：204 响应**既不能含正文，也不能含 trailer**——两者写在同一句里
- **前提**：§15.3.5 明写 "it **cannot contain content or trailers**"（ev-054）
- **推理**：
  1. 这属于「**标准与官方文档规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. 「204 不能有正文」是常识，教程都会讲；**「204 也不能有 trailer」几乎没人提**——
     trailer 是 HTTP/1.1 的分块传输尾部字段，很多实现根本没处理过它，
     于是**发送方带了 trailer、接收方静默丢弃**，双方都没报错
  3. 这条与 §16.2.2「新码不能禁止正文」（见
     [新增 HTTP 状态码须过 IETF Review](新增HTTP状态码须过IETFReview且不能禁止正文.md)）
     形成对照：**§16.2.2 禁止新码"不许有正文"，而 204 是既有的码、规范自己规定它"不许有正文"**——
     两条规则管的是不同的东西，不矛盾
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 「默认可缓存」可能与实现不符（尚无攻击）

- **主张**：204 响应**默认可缓存**（heuristically cacheable），
  除非方法定义或显式缓存控制另有规定
- **前提**：§15.3.5 明写 "A 204 response is **heuristically cacheable**"（ev-054）
- **推理**：
  1. **反直觉点**：一个"没有正文"的响应，为什么还要缓存？
     规范的理由是：缓存的是**头部区里那些描述新表示的字段**（如 `ETag`、`Last-Modified`），
     不是正文——**没有正文不等于没有可缓存的信息**
  2. 但**很多 HTTP 实现把 204 当成"什么都不用做"**，既不缓存也不重用，
     这与规范的默认值不符——**规范说默认可缓存，实现说不缓存，实现赢**（协议允许不缓存）
  3. 所以本条**不能被用来主张"任何 204 响应都应当被缓存"**
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.3.5 的原文，不保证任何具体客户端或服务端的实际行为。**
  「默认可缓存」是规范的默认值，不是实现的义务。
  另外：**本条未核对旧版 RFC（7230–7235）对 204 的表述**——
  旧版是否也写了 "cannot contain trailers"，本库不知道。
- **署名**：@hpleapfrog · 2026-10-12
- **待补**：RFC 7230–7235 对 204 的表述；主流客户端对 204 缓存行为的实测

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一篇 HTTP 教程都会告诉你「204 表示没有正文」，但不会告诉你它也不能带 trailer、而且默认可缓存。**
>
> 后两者都是规范里的一句话，转述里几乎见不到：
> **「不能带 trailer」决定了分块传输场景下 204 的合法形态；
> 「默认可缓存」决定了一个 204 响应里的 `ETag` 会不会被复用。**
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 「204 没有正文」是噪音——教程都在讲；
> 「204 也不能带 trailer，且默认可缓存」——这两条藏在 RFC 9110 §15.3.5 的两句长句里，
> **才是本库该装的。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-12 | 建立条目；填补「还缺什么」中「RFC 9110 §15.2–§15.6 各具体码」缺口的第一例 | ev-054 登记入库后按学科边界选题 | @hpleapfrog |
