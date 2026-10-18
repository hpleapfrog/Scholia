---
id: kb:computing:prop-http-414-uri-too-long
type: 命题
title: "An HTTP 414 response means the target URI is longer than the server is willing to interpret, and is heuristically cacheable by default"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "what exactly makes a 414", or "is a 414 telling me the client did something wrong"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.5.15**; this entry states that section's text only, **and has not checked at which length threshold any specific server returns 414**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP414表示目标URI过长且默认可缓存.md`](HTTP414表示目标URI过长且默认可缓存.md).**

## Statement

**A 414 (URI Too Long) response means the server is refusing to service the request because the target URI is longer than the server is willing to interpret.**

RFC 9110 §15.5.15 states (short quote):

> The 414 (URI Too Long) status code indicates that the server is
> refusing to service the request because the target URI is longer than
> the server is willing to interpret.

The same section names three typical causes (short quote):

> This rare condition is only likely to occur when a client has improperly
> converted a POST request to a GET request with long query information,
> when the client has descended into an infinite loop of redirection …

And the caching behaviour (short quote):

> A 414 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

### The most common cause is "the client turned a POST into a GET"

Of the three causes, the first is worth remembering:
**stuffing what belongs in a request body into a GET query string** — the specification's own word is `improperly converted`.
The usual retelling only says "the URL was too long"; the specification points at **how the request was constructed**.
The other two are an **infinite redirect loop** (a redirected URI prefix pointing at a suffix of itself) and **attack probing**.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.5.15** (definition of 414, three typical causes, heuristically cacheable) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · "A GET carrying a long query" is a cause named by the specification, not folklore (not yet attacked)

- **Claim**: a POST improperly converted into a GET with a long query string is the first cause named in §15.5.15;
  the redirect loop and attack probing are the other two
- **Premise**: §15.5.15 states `only likely to occur when a client has improperly converted a POST request to a GET request with long query information` (ev-054)
- **Reasoning**: the specification calls 414 a `rare condition` and lists three checkable scenarios —
  this is the specification's own text, not a community rule of thumb
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry gives no length threshold and guarantees no implementation behaviour (not yet attacked)

- **Claim**: this entry states the **definition and typical causes** of 414, **not that "any URI past N characters should get a 414"**
- **Premise**: §15.5.15 says `longer than the server is willing to interpret` — **the threshold is set by the server** (ev-054)
- **Reasoning**:
  1. the specification gives no number; servers and intermediaries each set their own limits
  2. in practice, over-long URIs are often handled by intermediaries in **other** ways (a different 4xx, or a dropped connection) — **this sentence is the repo's observation, not tested**
  3. therefore this entry **cannot be used to claim that "a 414 I received is what the specification required some server to return"** — it only states what 414 means normatively
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.5.15 only; it does not guarantee any specific implementation, and offers no threshold number.** Also: **whether older RFC 7231 words 414 the same way has not been checked.**
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: measured URI length limits of mainstream servers and proxies; comparison with RFC 7231 §6.5.12

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **"414 = URL too long" is everywhere; "it is cacheable by default, and its most common cause is a POST improperly turned into a GET" is almost nowhere.**
>
> The former is noise; the latter steers the debugging: **look at how the request was built first (why is something that should be a POST sitting in the query string?), not at the server.**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; fills the "situations 414 applies to" item of the "remaining individual codes" gap | ev-054 already registered; §15.5.15 verified | @hpleapfrog |
