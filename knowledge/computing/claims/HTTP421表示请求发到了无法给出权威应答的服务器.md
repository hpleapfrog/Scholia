---
id: kb:computing:prop-http-421-misdirected-request-retry
type: 命题
title: HTTP 421 表示请求发到了无法给出权威应答的服务器，且代理不得生成它
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: 收到过 421、或在写客户端/代理需要知道「421 该不该重试、代理能不能生成它」时
  条件: "**适用于 RFC 9110（STD 97，2022-06）§15.5.20**；本条只陈述该节原文，**未核对任何具体客户端或代理的实现**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

## 陈述

**421（Misdirected Request）表示请求被发到了一个无法（或不愿）为目标 URI 给出权威应答的服务器。**
收到 421 的客户端**可以换一条连接重试——即使请求方法不是幂等的**；而**代理不得生成 421**。

RFC 9110 §15.5.20 原文（短引用）：

> The 421 (Misdirected Request) status code indicates that the request
> was directed at a server that is unable or unwilling to produce an
> authoritative response for the target URI.

> A client that receives a 421 (Misdirected Request) response **MAY** retry
> the request, whether or not the request method is idempotent, over a
> different connection, such as a fresh connection specific to the
> target resource's origin, or via an alternative service [ALTSVC].

> A proxy **MUST NOT** generate a 421 response.

### 「可重试」与幂等性的关系

平时「重试」要过幂等性这一关（见
[HTTP 方法的安全性与幂等性由规范分类决定](HTTP方法的安全性与幂等性由规范分类决定.md)），
而 421 是规范**明确写下**的例外：`whether or not the request method is idempotent`。

## 依据

| 编号 | 类型 | 等级 | 定位 | 许可 |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt)，STD 97，2022-06，**§15.5.20**（421 定义、客户端重试许可、代理禁令） | 官方公开规范 · **仅引用章节号与短引用，不转载全文** |

## 论证

### A1 · 421 的「可重试」是不要求幂等的规范例外（尚无攻击）

- **主张**：客户端收到 421 可以换连接重试，**无论请求方法是否幂等**
- **前提**：§15.5.20 原文 `MAY retry the request, whether or not the request method is idempotent`（ev-054）
- **推理**：
  1. 一般重试要按方法幂等性判断；421 针对的是「**请求被发到了无权应答的服务器**」——
     典型情况是请求尚未被正确处理，换连接重发一般不会造成重复副作用
  2. **注意：「请求尚未被正确处理」是本库的解读，规范只给了许可，没有写理由**
- **证据**：ev-054
- **被攻击**：见 A2

### A2 · 本条不保证客户端会自动重试，也不覆盖代理「原样转达」的问题（尚无攻击）

- **主张**：本条陈述的是 421 的**规范含义**与客户端/代理的**规范许可**，
  不是「任何客户端都会自动换连接重试」
- **前提**：§15.5.20 对客户端是 MAY、对代理是 MUST NOT（ev-054）
- **推理**：
  1. MAY 意味着**可以不**重试——自动与否是实现选择
  2. MUST NOT 禁止的是代理**生成** 421（421 面向的是源服务器与其权威范围），
     代理收到上游的 421 如何处理，规范此节未展开——**「原样转达」之类的说法本库不写**
  3. 相关实现机制（连接合并、alternative services）本库未测试
- **证据**：ev-054
- **被攻击**：**本条只陈述 RFC 9110 §15.5.20 的原文，不保证任何具体客户端或代理的行为。**
  另外：**421 在旧规范（RFC 7231 / RFC 7540 时代）中的来历，本库未核。**
- **署名**：@hpleapfrog · 2026-10-18
- **待补**：421 的历史（连接合并背景）；主流客户端收到 421 后的实测行为

## 为什么这条算「真实信息」而不是「噪音」

> [!IMPORTANT]
> **「421 是什么」在教程里都少见，这两个规范要点几乎没人转述：**
>
> - **客户端 MAY 换连接重试，且不要求幂等**——收到 421 时，重发是规范允许的，不是「赌一把」；
> - **代理 MUST NOT 生成 421**——写代理时的行为准则：这个码不归代理发。
>
> **本库的使命是「去除噪音、存放真实信息」**——这两句就藏在 §15.5.20 的 MAY 与 MUST NOT 里。

## 变更记录

| 日期 | 操作 | 依据 | 谁 |
|---|---|---|---|
| 2026-10-18 | 建立条目；填补「还缺什么」中「其余具体码」缺口——421 的重试规定 | ev-054 已登记，核毕 §15.5.20 | @hpleapfrog |
