---
id: kb:computing:prop-http-404-temporary-vs-permanent-non-disclosure
type: 命题
title: "An HTTP 404 does not say whether the lack is temporary or permanent, and is also used to avoid disclosing that a resource exists"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "what a 404 actually means", or "how to choose between 404 and 410"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.5.5** (with §15.5.4 for contrast); this entry states those sections' text only, **and has tested no specific server implementation**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP404不说明缺失是暂时还是永久且可用于不愿披露资源存在.md`](HTTP404不说明缺失是暂时还是永久且可用于不愿披露资源存在.md).**

## Statement

**404 (Not Found) judges the *current representation*: the origin server did not find a current representation for the target resource, or is not willing to disclose that one exists; and a 404 does not say whether the lack is temporary or permanent — when the condition is known to be likely permanent, the specification prefers 410.**

RFC 9110 §15.5.5 states (short quote):

> The 404 (Not Found) status code indicates that the origin server did
> not find a current representation for the target resource **or is not
> willing to disclose that one exists**.  A 404 status code does not
> indicate whether this lack of representation is **temporary or
> permanent**; the 410 (Gone) status code is preferred over 404 if the
> origin server knows, presumably through some configurable means, that
> the condition is likely to be permanent.

The same section also specifies the caching behaviour (short quote):

> A 404 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

### "Not willing to disclose" is not an isolated case: 403 may choose to answer 404 instead

§15.5.4 (the definition of 403) says outright (short quote):

> An origin server that wishes to "hide" the current existence of a
> forbidden target resource **MAY** instead respond with a status code of
> 404 (Not Found).

That is, a "404" may be "there genuinely is nothing" — or the origin server **choosing not to say**. The specification puts both cases under the same code.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.5.5** (definition of 404, its silence on temporary vs permanent, the relation to 410, heuristically cacheable), **§15.5.4** (a 403 may hide existence behind a 404, for contrast) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · 404's definition has two branches, and deliberately takes no position on "temporary vs permanent" (not yet attacked)

- **Claim**: 404 covers two judgements — (1) no current representation was found; (2) one exists but the server is not willing to disclose it; and it **does not distinguish** whether the lack is temporary or permanent
- **Premise**: §15.5.5 states `or is not willing to disclose that one exists` and `does not indicate whether this lack of representation is temporary or permanent` (ev-054)
- **Reasoning**:
  1. Tutorials often say 404 means "the resource does not exist" — the specification says the **current representation** was not found; and together with the MAY in §15.5.4, **a 403 may deliberately answer 404 to hide that the resource exists** — "not willing to disclose" is a branch written into the specification, not an implementation quirk
  2. The division of labour with 410 is in [the 410 entry](http-410-vs-404-permanence.en.md): **use 410 only when permanence is known to be likely; when unsure, use 404** — 404's non-commitment is part of the design
  3. "Heuristically cacheable" is the specification's default, not an implementation's obligation
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry guarantees no implementation behaviour and gives no criterion for "no longer exists" (not yet attacked)

- **Claim**: this entry states 404's normative definition and that section's cache default only; it **does not state why any specific server does or does not return a 404**
- **Premise**: §15.5.5 and §15.5.4 are specification text (ev-054); **this entry has tested no server**
- **Reasoning**:
  1. The gap between specification and implementation is especially common at 404 (unmatched routes, misconfigured reverse proxies and permission hiding all land there) — **this repo has no mechanism for implementation testing**
  2. Therefore this entry **cannot be used to claim that "a 404 I received is necessarily the specification's 'not found'"**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.5.5 and §15.5.4 only; it does not guarantee the behaviour of any specific server.** Also: **this entry has not checked how older RFCs (7230–7235) word 404**.
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: how RFC 7230–7235 word 404; measurements of mainstream servers answering 404 in place of 403 or permission hiding

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **"404 means the resource does not exist" is noise — every tutorial says it; "404's definition also carries a 'not willing to disclose' branch, and deliberately stays silent on temporary vs permanent" is what this library should hold.**
>
> The former, memorised, cannot explain "why the same 404 is sometimes a missing deployment and sometimes a refusal to let you look";
> the latter is the answer the specification wrote down.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; sweeps up the "remaining status codes on the protocol side" gap — 404's two-branch semantics and its silence on temporary vs permanent | ev-054 already registered; §15.5.5 verified (with §15.5.4) | @hpleapfrog |
