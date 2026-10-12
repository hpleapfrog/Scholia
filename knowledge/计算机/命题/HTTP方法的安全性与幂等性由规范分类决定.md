---
id: kb:computing:prop-http-method-safety-idempotency
type: 命题
title: HTTP 方法的安全性与幂等性由规范分类决定，且「安全」不等于「无副作用」
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 想核对「GET / POST / PUT / DELETE 各自是什么性质、能不能自动重试」时
  条件: **仅适用于 RFC 9110（2022-06）§9.2 的分类**；本条只陈述规范的分类，**不涉及任何具体框架或客户端的实现行为**
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

RFC 9110 §9.2 把 HTTP 方法分成两个**正交**的性质：

| 性质 | 规范里的定义 | 属于这一类的方法 |
|---|---|---|
| **safe（安全）** | "the client does not request, and does not expect, **any state change** on the origin server" | **`GET` · `HEAD` · `OPTIONS` · `TRACE`** |
| **idempotent（幂等）** | "the intended effect … of **multiple identical requests** … is the same as the effect for **a single** such request" | **`PUT` · `DELETE` · 以及全部 safe 方法** |

原文（短引用）：

> Of the request methods defined by this specification, the `GET`, `HEAD`, `OPTIONS`, and `TRACE` methods are defined to be **safe**.（§9.2.1）
>
> Of the request methods defined by this specification, `PUT`, `DELETE`, and **safe request methods** are **idempotent**.（§9.2.2）

推论：**`POST` 既不 safe，也不 idempotent**——它不在任何一张名单里。

> [!IMPORTANT]
> **「safe」不等于「没有副作用」。这是本条最容易被读错的地方。**
>
> §9.2.1 明文写了：safe 的定义 "**does not prevent an implementation from including
> behavior that is potentially harmful**"，重要的是 "**the client did not request that
> additional behavior and cannot be held accountable for it**"。
>
> 规范自己举了两个例子：
> 服务器把请求写进访问日志（"the log storage might become full and cause the server to fail"），
> 以及点击广告触发计费（"will often have the side effect of charging an advertising account"）——
> **两者都发生在 safe 方法上，规范仍判定为 safe。**
>
> **判据是「客户端有没有请求这个行为」，不是「有没有发生状态变化」。**

### 幂等性与自动重试

§9.2.2 规定了自动重试的边界：

| 角色 | 规定 |
|---|---|
| 客户端 | "**SHOULD NOT** automatically retry a request with a non-idempotent method"，除非另有手段知道语义其实幂等，或能检测原请求从未生效 |
| **代理** | "**MUST NOT** automatically retry non-idempotent requests" |
| 客户端（再） | "SHOULD NOT automatically retry a failed automatic retry" |

注意其中的关键词是 **大写** 的 `SHOULD NOT` / `MUST NOT`——它们的强度由
[RFC 要求关键词只有全大写才成立](RFC要求关键词只有全大写才成立.md)决定。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高**（对该类主张而言） | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§9.2.1 / §9.2.2**（本库核了原文；全文 10785 行，其余章节未核） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 分类是规范写死的，不是约定俗成（尚无攻击）

- **主张**：哪些方法 safe、哪些 idempotent，是**规范的明文分类**，不是社区习惯
- **前提**：§9.2.1 与 §9.2.2 各用一句话点名了具体方法（ev-054）
- **推理**：
  1. 这属于「**规范规定了什么**」——正是[计算机](../README.md)学科收的东西
  2. 它**可被读者逐条证伪**：点开 RFC 9110 的 §9.2 即可
  3. `POST` 的「两不属」是**结构性推论**（不在任一名单），
     不是规范单独为它写的一句话——这本身值得记下来
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条只陈述规范的分类，不判断任何实现（尚无攻击）

- **主张**：本条声明的是「**规范怎么分类**」，**不声明「某个客户端/服务器实际怎么做」**
- **前提**：§9.2.2 自己承认了实现可以有规范之外的行为——
  "a server is free to log each request separately, retain a revision control history,
  or implement **other non-idempotent side effects** for each idempotent request"（ev-054）
- **推理**：
  1. 也就是说：**一个 idempotent 请求，服务器仍然可以对每次调用产生非幂等副作用**
     ——幂等性约束的是**客户端请求的预期效果**，不是服务器的全部行为
  2. 「某个框架的 PUT 重试了会不会重复写」**要看那个框架的实现**，
     本库**没有核对任何框架**
  3. 所以本条**不能被用来支持「用 PUT 就一定安全」**
- **证据**：ev-054
- **被攻击**：**本库没有核对任何具体客户端、代理或框架对这三条规定的实现。**
  「curl / 某浏览器 / 某 HTTP 库 在连接断开时会不会自动重试 POST」——
  **这个问题本库一条都没查。** 另外：**本库只核了 §9.2 三节**，
  §9.3 各方法的完整定义、§15 状态码均未核。
- **署名**：@hpleapfrog · 2026-10-12
- **待补**：至少一个主流客户端的重试行为实测；§9.3 方法定义逐条核对

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **任何一份 HTTP 教程都会列出方法表格，但不会写出「安全 ≠ 无副作用」。**
>
> 你在浏览器开发者工具里能看到的是 **一个 GET 请求和它的响应**；
> 规范里写的是 **这个方法在协议层被赋予了什么性质、因此谁可以拿它自动做事**。
>
> **本库的使命是「去除噪音、存放真实信息」。**
> 这个对比就是判据：**请求长什么样，本库不必重复；
> 规范给它定了什么性、由此谁被允许做什么，才是本库该装的。**
> 「爬虫抓 GET 算不算安全」——这个问题在任何开发者工具里都找不到答案，
> 而规范把答案写成了一个可查的分类，**并且明确说日志写满磁盘也算 safe**。

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-12 | 建立条目；本学科第二条 `命题` | ev-054 登记入库后按学科边界选题 | @hpleapfrog |
