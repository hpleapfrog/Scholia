---
id: kb:computing:prop-http-1xx-interim-responses
type: 命题
title: HTTP 1xx 是临时响应：不得发给 HTTP/1.0 客户端，不能含正文或 trailer，客户端必须能解析但可以忽略
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「100 / 101 是什么」「客户端要不要处理 1xx」「代理转不转发 1xx」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.2（类别规则）、§15.2.1（100）、§15.2.2（101）**；本条只陈述这些原文，**未核 §10.1.1（Expect）与 §7.8（Upgrade）的联动细节**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**1xx 是「完成请求动作之前」的临时响应：不能含正文或 trailer；客户端必须能解析它（哪怕没预期），但可以忽略；代理必须转发（除自己要求生成的以外）；而且它不得发给 HTTP/1.0 客户端。**

RFC 9110 §15.2 的四条规则（短引用）：

> Since HTTP/1.0 did not define any 1xx status codes, a
> server **MUST NOT** send a 1xx response to an HTTP/1.0 client.
>
> A 1xx response is terminated by the end of the header section; it
> **cannot contain content or trailers**.
>
> A client **MUST** be able to parse one or more 1xx responses received
> prior to a final response, even if the client does not expect one.  A
> user agent **MAY** ignore unexpected 1xx responses.
>
> A proxy **MUST** forward 1xx responses unless the proxy itself requested
> the generation of the 1xx response.

### RFC 9110 定义的两个成员：100 与 101

100（Continue）的配合方式（§15.2.1，短引用）：

> When the request contains an Expect header field that includes a
> 100-continue expectation, the 100 response indicates that the server
> **wishes to receive the request content** … The client **ought to**
> continue sending the request and discard the 100 response.

101（Switching Protocols）的硬性要求（§15.2.2，短引用）：

> The server **MUST** generate an Upgrade header field in the response
> that indicates which protocol(s) will be in effect after this response.

同节还说（短引用）：

> It is assumed that the server will only agree to switch protocols
> when it is advantageous to do so.

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.2**（1xx 类别规则）、**§15.2.1**（100）、**§15.2.2**（101） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 1xx 有四条「平时没人提」的规矩（尚无攻击）

- **主张**：1xx 不能含正文/trailer；客户端必须能解析（可忽略）；代理必须转发；
  不得发给 HTTP/1.0 客户端——四者都是规范原文，其中两条是 MUST 级
- **前提**：§15.2 的引文（ev-054）
- **推理**：
  1. 转述通常只讲「100 续传、101 升级」，不会讲**发送对象的限制**（HTTP/1.0 禁令）
     与**中间件的义务**（代理必须转发）
  2. 这四条合起来定义了 1xx 的特殊地位：它**不是**最终响应，
     而是「连接与请求进度」的带外信号
  3. 「必须能解析、可以忽略」是给客户端的健壮性要求——
     不能因为没见过就把连接搞坏
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条不展开 Expect / Upgrade 的完整机制（尚无攻击）

- **主张**：100 与 `Expect: 100-continue`、101 与 `Upgrade` 的完整联动规则
  分别在 §10.1.1 与 §7.8——**本条未核那两节**，只陈述 §15.2.x 里出现的部分
- **前提**：§15.2.1 原文即把细节指向 `Section 10.1.1`（ev-054）
- **推理**：
  1. 因此本条**不能被用来主张**「服务器什么时候必须等 100-continue」之类的细节规则
  2. 101 之后的协议切换过程（连接上跑什么）由被切换的协议定义，不属本条
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.2–§15.2.2 的原文，不保证任何具体客户端/代理/服务端的行为。**
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：§10.1.1（Expect）与 §7.8（Upgrade）的核读；主流代理转发 1xx 的实测

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **「100 是继续、101 是切换协议」是噪音；「1xx 不得发给 HTTP/1.0、不能带正文、客户端必须能解析、代理必须转发」才是本库该装的。**
>
> 这四条是写中间件和客户端时的实测边界——**规范已经把责任分配好了，转述里见不到。**

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；清尾「还缺什么」中「协议侧剩余状态码」缺口——1xx 临时响应规则与 100/101 | ev-054 已登记，核毕 §15.2–§15.2.2 | @hpleapfrog |
