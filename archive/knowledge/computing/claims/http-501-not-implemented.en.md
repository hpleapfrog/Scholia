---
id: kb:computing:prop-http-501-not-implemented
type: 命题
title: "An HTTP 501 response means the server does not support the required functionality, and is heuristically cacheable by default"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to tell 501, 503 and 405 apart, or to check "should a 501 be cached"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.6.2 (501 and its caching) with §15.6.4 (503) and §15.5.6 (405) for contrast**; this entry states those sections' text only, **and has not checked when any specific server returns 501**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP501表示服务器不支持所需功能且默认可缓存.md`](HTTP501表示服务器不支持所需功能且默认可缓存.md).**

## Statement

**A 501 (Not Implemented) response means the server does not support the functionality required to fulfill the request**;
its most appropriate occasion is when "the server **does not recognize the request method** and is **not capable of supporting it for any resource**". A 501 is heuristically cacheable.

RFC 9110 §15.6.2 states (short quote):

> The 501 (Not Implemented) status code indicates that the server does
> not support the functionality required to fulfill the request.  This
> is the appropriate response when the server does not recognize the
> request method and is not capable of supporting it for any resource.

> A 501 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

Contrasted with §15.6.4 (short quote):

> The 503 (Service Unavailable) status code indicates that the server
> is currently unable to handle the request due to a temporary overload
> or scheduled maintenance …

### How 405, 501 and 503 divide the work

| Code | Who is speaking | Key wording in the specification |
|---|---|---|
| **405** | the **target resource** does not support the method (the server **knows** the method) | see the [405 entry](http-405-must-include-allow-header.en.md) |
| **501** | the **server** lacks the required functionality (**no resource** supports the method) | `does not support the functionality required` |
| **503** | the server is **temporarily** unable (overload / scheduled maintenance) | `currently unable` · `temporary` |

**405 vs 501 is "resource vs server"; 501 vs 503 is "lacking capability vs lacking time".**

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.6.2** (definition of 501, its most appropriate occasion, heuristically cacheable), **§15.6.4** (503 for contrast), **§15.5.6** (405 for contrast) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · "Not for any resource" is the qualifier that defines 501 (not yet attacked)

- **Claim**: the most appropriate occasion for 501 is "the method is not recognized and cannot be supported for **any resource**";
  if only **one particular resource** does not support it (while the server knows the method), that is the occasion for 405
- **Premise**: §15.6.2 states `is not capable of supporting it for any resource` (ev-054);
  §15.5.6 draws 405 at "the target resource does not support it" (ev-054; see the 405 entry)
- **Reasoning**: the phrase `for any resource` lifts 501 from resource level to server level —
  the two entries complement rather than repeat each other, which is why this library puts the three codes in one table
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · "The appropriate response" is not a MUST (not yet attacked)

- **Claim**: the specification defines the meaning and most appropriate occasion of 501, **not that "an implementation must return 501" on that occasion**
- **Premise**: §15.6.2 uses `This is the appropriate response when …` — describing appropriateness, not a MUST (ev-054)
- **Reasoning**:
  1. "appropriate" and "required" are different strengths of wording in a specification;
     how real servers handle unknown methods varies (this entry **has not tested any**)
  2. "501 is cacheable by default" is the specification's default, **not an implementation's obligation** —
     the same situation as [204](http-204-cannot-contain-content-or-trailers.en.md) and [405](http-405-must-include-allow-header.en.md)
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.6.2 only; it does not guarantee the behaviour of any specific server.** Also: **whether older RFC 7231 words 501 the same way has not been checked.**
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: measurement of mainstream servers on unknown request methods; comparison with RFC 7231 §6.6.2

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Tutorials only say "501 = not implemented"; the specification also writes three things retellings never carry:**
>
> - its **most appropriate occasion has a precise condition** — "no resource supports it" is 501 (one resource short of that is 405);
> - it is **heuristically cacheable**;
> - its division from 503 is "**lacking capability vs lacking time**" — one cannot, the other cannot right now.
>
> Checking those three takes §15.6.2's two paragraphs — which is exactly what this library should hold.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; fills the "501 / 503 division" item of the "remaining individual codes" gap | ev-054 already registered; §15.6.2, §15.6.4 and §15.5.6 verified | @hpleapfrog |
