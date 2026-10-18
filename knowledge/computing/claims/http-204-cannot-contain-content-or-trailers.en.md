---
id: kb:computing:prop-http-204-cannot-contain-content-or-trailers
type: 命题
title: "An HTTP 204 response may contain neither content nor trailers, and is heuristically cacheable by default"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "may a 204 response carry a body", or "is a 204 response cacheable by default"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.3.5**; this entry states that section's text only, **and has not checked how older RFCs (7230–7235) worded 204**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP204响应不能含正文也不能含trailer且默认可缓存.md`](HTTP204响应不能含正文也不能含trailer且默认可缓存.md).**

## Statement

**A 204 (No Content) response is terminated by the end of the header section — it may contain neither content nor trailers.**

RFC 9110 §15.3.5 states (short quote):

> A 204 response is terminated by the end of the header section; it
> **cannot contain content or trailers**.

The same section also specifies the caching behaviour (short quote):

> A 204 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by the method definition or explicit cache controls (see
> Section 4.2.2 of [CACHING]).

### What a 204 is allowed to carry

§15.3.5 illustrates the use of 204 with an example (short quote):

> if a 204 status code is received in response to a PUT request and the response contains an **ETag** field, then the PUT was successful and the ETag field value contains the entity tag for the new representation

That is: **a 204 carries no body, but it may carry header fields describing the new representation** —
`ETag` is the specification's own example.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.3.5** (definition of 204) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · "May not contain content" is the hard constraint; "may not contain trailers" is the second half of the same sentence (not yet attacked)

- **Claim**: a 204 response may contain **neither content nor trailers** — both halves are written in one sentence
- **Premise**: §15.3.5 states "it **cannot contain content or trailers**" (ev-054)
- **Reasoning**:
  1. This is "what a standard or official document specifies" — exactly what the [computing](../README.en.md) discipline collects
  2. "A 204 may not carry a body" is common knowledge; tutorials all say it. **"A 204 may not carry trailers either" is almost never mentioned** — trailers are HTTP/1.1 chunked-trailer fields; many implementations have never handled them, so **the sender attaches a trailer and the receiver silently drops it, neither side reporting an error**
  3. This sits in contrast with §16.2.2's "new codes cannot disallow content" (see [Adding an HTTP status code requires IETF Review](http-status-code-registration-requires-ietf-review.en.md)): **§16.2.2 forbids a new code from saying "I forbid a body", while 204 is an existing code whose own specification says "it cannot contain content"** — the two rules govern different things and do not conflict
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · "Cacheable by default" may not match implementations (not yet attacked)

- **Claim**: a 204 response is **cacheable by default** (heuristically cacheable), unless the method definition or explicit cache controls say otherwise
- **Premise**: §15.3.5 states "A 204 response is **heuristically cacheable**" (ev-054)
- **Reasoning**:
  1. **The counter-intuitive part**: a response with "no content" — why cache it? The specification's answer: what gets cached are **the header fields describing the new representation** (such as `ETag`, `Last-Modified`), not the body — **having no body does not mean having nothing cacheable**
  2. But **many HTTP implementations treat 204 as "nothing to do"**, neither caching nor reusing it, which differs from the specification's default — **the specification says cacheable by default, the implementation says no, and the implementation wins** (the protocol permits not caching)
  3. Therefore this entry **cannot be used to claim that any 204 response ought to be cached**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.3.5 only; it does not guarantee the actual behaviour of any specific client or server.** "Cacheable by default" is the specification's default, not an implementation's obligation. Also: **this entry has not checked how older RFCs (7230–7235) worded 204** — whether they too wrote "cannot contain trailers", this repo does not know.
- **Author**: @hpleapfrog · 2026-10-12
- **To be added**: RFC 7230–7235's wording of 204; measured caching behaviour of mainstream clients

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Any HTTP tutorial tells you "204 means no content"; none tells you it also may not carry trailers, and that it is cacheable by default.**
>
> The latter two are each a single sentence in the specification, and almost never survive retelling:
> **"may not carry trailers" determines the legal shape of a 204 in chunked-transfer scenarios;
> "cacheable by default" determines whether the `ETag` in a 204 gets reused.**
>
> **This library's mission is to remove noise and store real information.**
> "204 has no body" is noise — tutorials all cover it.
> "204 also may not carry trailers, and is cacheable by default" — these two sit inside two long sentences of RFC 9110 §15.3.5, **and are what this library should hold**.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; first instance filling the "individual codes of RFC 9110 §15.2–§15.6" gap in "What is still missing" | ev-054 registered; topic selected by discipline boundary | @hpleapfrog |
