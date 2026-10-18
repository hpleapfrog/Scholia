---
id: kb:computing:prop-http-405-must-include-allow-header
type: 命题
title: "An HTTP 405 response MUST carry an Allow header, and is heuristically cacheable by default"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "should a 405 response carry an Allow header", or "is a 405 response cacheable by default"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.5.6**; this entry states that section's text only, **and has not tested whether any specific server implementation honours that MUST**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP405响应必须带Allow头部且默认可缓存.md`](HTTP405响应必须带Allow头部且默认可缓存.md).**

## Statement

**A 405 (Method Not Allowed) response MUST carry an `Allow` header listing the target resource's currently supported methods.**

RFC 9110 §15.5.6 states (short quote):

> The origin server **MUST** generate an **Allow** header field in a 405 response
> containing a list of the target resource's currently supported methods.

The same section also specifies the caching behaviour (short quote):

> A 405 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

### How 405 divides from 501

§15.5.6 defines 405 as "**the origin server knows the method, but the target resource does not support it**";
§15.6.2 defines 501 as "**the origin server does not know the method**".
Both concern a method being rejected, but **the responsible party differs** — 405 points at the resource, 501 at the server.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.5.6** (definition of 405 and the Allow requirement), **§15.6.2** (definition of 501, for contrast) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · The `Allow` header is a MUST-level requirement, not a recommendation (not yet attacked)

- **Claim**: when an origin server generates a 405 response, it **MUST** generate an `Allow` header, and that header **MUST** list the methods the target resource currently supports
- **Premise**: §15.5.6 states "The origin server **MUST** generate an **Allow** header field" (ev-054)
- **Reasoning**:
  1. This is "what a standard or official document specifies" — exactly what the [computing](../README.en.md) discipline collects
  2. **MUST is the strongest requirement level in RFC 2119** (see [MUST / SHOULD / MAY in an RFC carry normative meaning only when written in all capitals](rfc-keywords-require-uppercase.en.md)) — this is not "it is recommended to include it" but "omitting it is a violation of the specification"
  3. Practical consequence: **many servers return 405 without `Allow`**, leaving the client **no way to learn which methods the resource does support** — that is the implementation violating the specification, not the specification permitting the omission
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry does not guarantee that any specific implementation honours the MUST (not yet attacked)

- **Claim**: this entry states **what the specification requires of a 405 response**, **not that "any specific server actually sends `Allow`"**
- **Premise**: §15.5.6 writes the requirement in MUST (ev-054), but **this entry has tested no server**
- **Reasoning**:
  1. A specification's MUST and an implementation's compliance are two different things — **this repo has no mechanism for implementation testing**
  2. Likewise, "405 is cacheable by default" is the specification's default, **not an implementation's obligation** — the same situation as [204 being cacheable by default](http-204-cannot-contain-content-or-trailers.en.md)
  3. Therefore this entry **cannot be used to claim that "a 405 response I received without an Allow header is normal"**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.5.6 only; it does not guarantee the behaviour of any specific server.** "Cacheable by default" is the specification's default, not an implementation's obligation. Also: **this entry has not checked how older RFCs (7230–7235) worded 405** — whether they too wrote the same MUST, this repo does not know.
- **Author**: @hpleapfrog · 2026-10-12
- **To be added**: RFC 7230–7235's wording of 405; measured presence of `Allow` in real-world 405 responses from mainstream servers

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Any HTTP tutorial tells you "405 means the method is not allowed"; none tells you the specification requires the response to carry an `Allow` header, in MUST.**
>
> The latter is a single sentence in the specification, and almost never survives retelling:
> **it determines whether a 405 response is "complete" — without `Allow`, the client has no way to know which method to retry with.**
>
> **This library's mission is to remove noise and store real information.**
> "405 means the method is not allowed" is noise — tutorials all cover it.
> "A 405 response MUST carry an `Allow` header listing the supported methods" — this sits inside one MUST sentence of RFC 9110 §15.5.6, **and is what this library should hold**.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; second instance filling the "individual codes of RFC 9110 §15.2–§15.6" gap in "What is still missing" | ev-054 registered; topic selected by discipline boundary | @hpleapfrog |
