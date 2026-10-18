---
id: kb:computing:prop-http-method-safety-idempotency
type: 命题
title: "An HTTP method's safety and idempotency are set by the specification, and 'safe' does not mean 'free of side effects'"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "what GET / POST / PUT / DELETE actually are, and whether they may be retried automatically"
  条件: "**applies only to the classification in RFC 9110 §9.2 (2022-06)**; this entry states the specification's classification only, **and covers no framework's or client's implementation behaviour**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP方法的安全性与幂等性由规范分类决定.md`](HTTP方法的安全性与幂等性由规范分类决定.md).**

## Statement

RFC 9110 §9.2 sorts HTTP methods along **two orthogonal** properties:

| Property | Definition in the specification | Methods in this class |
|---|---|---|
| **safe** | "the client does not request, and does not expect, **any state change** on the origin server" | **`GET` · `HEAD` · `OPTIONS` · `TRACE`** |
| **idempotent** | "the intended effect … of **multiple identical requests** … is the same as the effect for **a single** such request" | **`PUT` · `DELETE` · and all safe methods** |

The source (short quotes):

> Of the request methods defined by this specification, the `GET`, `HEAD`, `OPTIONS`, and `TRACE` methods are defined to be **safe**. (§9.2.1)
>
> Of the request methods defined by this specification, `PUT`, `DELETE`, and **safe request methods** are **idempotent**. (§9.2.2)

Corollary: **`POST` is neither safe nor idempotent** — it appears on neither list.

> [!IMPORTANT]
> **"Safe" does not mean "no side effects". This is the part most easily misread.**
>
> §9.2.1 says in terms: the definition of safe "**does not prevent an implementation from including
> behavior that is potentially harmful**"; what matters is "**the client did not request that
> additional behavior and cannot be held accountable for it**".
>
> The specification supplies two of its own examples:
> a server appending every request to an access log ("the log storage might become full and cause the server to fail"),
> and selecting an advertisement triggering a billing charge ("will often have the side effect of charging an advertising account") —
> **both happen on a safe method, and the specification still calls them safe.**
>
> **The test is "did the client request that behaviour", not "did a state change occur".**

### Idempotency and automatic retries

§9.2.2 sets the boundary for automatic retries:

| Role | Rule |
|---|---|
| Client | "**SHOULD NOT** automatically retry a request with a non-idempotent method", unless it has some means to know the semantics are actually idempotent, or to detect that the original request was never applied |
| **Proxy** | "**MUST NOT** automatically retry non-idempotent requests" |
| Client (again) | "SHOULD NOT automatically retry a failed automatic retry" |

Note that the keywords here are **capitalised** — their strength is settled by
[RFC requirement keywords only hold in all capitals](rfc-keywords-require-uppercase.en.md).

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **官方文件** | **高** (for a claim of this kind) | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§9.2.1 / §9.2.2** (this repo verified the source text; the document is 10,785 lines and the rest was not checked) | official public specification · **cite section numbers and short quotes only; no full text reproduced** |

## Argument

### A1 · The classification is written down, not folklore (no attack yet)

- **Claim**: which methods are safe and which are idempotent is **the specification's explicit classification**, not community habit
- **Premise**: §9.2.1 and §9.2.2 each name the methods in a single sentence (ev-054)
- **Reasoning**:
  1. this is "**what the specification says**" — exactly what the [computing](../README.en.md) subject collects
  2. it is **falsifiable by the reader**: open §9.2 of RFC 9110 and read it
  3. `POST`'s "belongs to neither" is a **structural consequence** (it is on no list),
     not a sentence the specification wrote specifically about it — and that is worth recording in its own right
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry states the specification's classification only, and judges no implementation (no attack yet)

- **Claim**: this entry claims "**how the specification classifies them**", **not "what a given client or server actually does"**
- **Premise**: §9.2.2 concedes in terms that a server may do more than the classification implies —
  "a server is free to log each request separately, retain a revision control history,
  or implement **other non-idempotent side effects** for each idempotent request" (ev-054)
- **Reasoning**:
  1. that is: **an idempotent request can still produce non-idempotent side effects on each call** —
     idempotency constrains **the client's intended effect**, not everything the server does
  2. "will a framework's PUT double-write on retry" **depends on that framework's implementation**,
     and **this repo has verified no framework**
  3. so this entry **cannot be used to support "using PUT is therefore safe"**
- **Evidence**: ev-054
- **Attacked by**: **this repo has verified the implementation of these three rules by no client, proxy or framework.**
  "Will curl / some browser / some HTTP library auto-retry a POST after the connection drops" —
  **this repo has not investigated a single case.** Also: **this repo verified three sections only** —
  the full method definitions in §9.3 and the status codes in §15 were not checked.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: a measured retry behaviour of at least one mainstream client; a section-by-section check of §9.3

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every HTTP tutorial lists the methods, but none of them writes out "safe ≠ free of side effects".**
>
> What you can see in a browser's developer tools is **a GET request and its response**;
> what the specification writes down is **what property the protocol assigns to that method,
> and therefore who is allowed to act on it automatically**.
>
> **This repo's mission is to strip noise and hold true information.**
> That contrast is the test: **what a request looks like, this repo need not repeat;
> what property it has been assigned and who may therefore act on it is what belongs here.**
> "Is it safe for a crawler to fetch a GET" — the question has no answer in any developer tools,
> while the specification wrote the answer down as a checkable classification,
> **and said in terms that a log filling the disk still counts as safe**.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; the subject's second `命题` | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
