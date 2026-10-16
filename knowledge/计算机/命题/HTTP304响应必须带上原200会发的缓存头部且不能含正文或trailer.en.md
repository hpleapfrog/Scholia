---
id: kb:computing:prop-http-304-must-carry-cache-headers-and-no-body
type: 命题
title: "An HTTP 304 response MUST carry the cache headers a 200 would have sent, and may contain neither content nor trailers"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "which headers a 304 response should carry", or "may a 304 response have a body"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.4.5**; this entry states that section's text only, **and has not checked the separate requirements [CACHING] §4.3.4 places on caches**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP304响应必须带上原200会发的缓存头部且不能含正文或trailer.md`](HTTP304响应必须带上原200会发的缓存头部且不能含正文或trailer.md).**

## Statement

**A 304 (Not Modified) response MUST carry the set of cache-related header fields that a 200 response would have sent, and may contain neither content nor trailers.**

RFC 9110 §15.4.5 states (short quote):

> The server generating a 304 response **MUST** generate any of the following header fields
> that would have been sent in a 200 (OK) response to the same request:
>
> * **Content-Location, Date, ETag, and Vary**
> * **Cache-Control and Expires** (see [CACHING])

The closing paragraph of the same section (short quote):

> A 304 response is terminated by the end of the header section; it
> **cannot contain content or trailers**.

### The semantics of 304: redirecting the client to its own cache

§15.4.5 opens by explaining what a 304 actually says (short quote):

> The 304 (Not Modified) status code indicates that a conditional GET or HEAD request has
> been received and **would have resulted in a 200 (OK) response if it were not for the fact
> that the condition evaluated to false**. In other words, there is no need for the server to
> transfer a representation of the target resource because the request indicates that the client …
> **already has a valid representation**; the server is therefore **redirecting the client to
> make use of that stored representation as if it were the content of a 200 (OK) response**.

### Headers should be kept to a minimum

§15.4.5 also imposes the opposite constraint (short quote):

> a sender **SHOULD NOT** generate representation metadata other than the above listed fields
> unless said metadata exists for the purpose of **guiding cache updates** (e.g., `Last-Modified`
> might be useful if the response does not have an `ETag` field).

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.4.5** (definition of 304, the MUST list of headers, the body restriction, the header-minimisation requirement) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · The required headers are a closed list in the specification, not a recommendation (not yet attacked)

- **Claim**: a server generating a 304 **MUST** carry the headers `Content-Location`, `Date`, `ETag`, `Vary`, `Cache-Control` and `Expires` that a 200 would have sent
- **Premise**: §15.4.5 states "**MUST** generate any of the following header fields" (ev-054)
- **Reasoning**:
  1. This is "what a standard or official document specifies" — exactly what the [computing](../README.en.md) discipline collects
  2. **MUST is the strongest requirement level in RFC 2119** — this is not "it is recommended to include them" but "omitting them is a violation of the specification"
  3. Practical consequence: **a 304 without `ETag` or `Cache-Control` leaves the client unable to tell how long the cache stays valid** — that is the implementation violating the specification
  4. The specification also imposes the **opposite** constraint (SHOULD NOT): beyond that list and fields that "guide cache updates", **nothing else should be sent** — **the design goal of 304 is to minimise what is transferred**
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · The same "may not contain content or trailers" as 204 (not yet attacked)

- **Claim**: a 304 response may contain **neither content nor trailers** — the same constraint as [204](HTTP204响应不能含正文也不能含trailer且默认可缓存.en.md)
- **Premise**: the closing paragraph of §15.4.5 states "it **cannot contain content or trailers**" (ev-054)
- **Reasoning**:
  1. Two codes (one 2xx, one 3xx) sharing the same sentence pattern shows this is **the specification's consistent requirement for responses with nothing to transfer**, not a 204 special case
  2. But **304's semantics are stronger**: 204 is "the request succeeded, there is nothing to give you"; 304 is "**you already have that representation yourself, stop asking me for it**" — 304 is **the only status code whose meaning puts the content in the client's cache**
  3. So a 304's headers matter more than a 204's: **a 204 may carry nothing, a 304 must carry that list**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.4.5 only; it does not guarantee the behaviour of any specific server.** "MUST carry that list" is the specification's requirement, not a measured fact about implementations. Also: **this entry has not checked [CACHING] §4.3.4's separate requirements on caches receiving a 304**, nor **how older RFCs (7230–7235) worded 304**.
- **Author**: @hpleapfrog · 2026-10-13
- **To be added**: [CACHING] §4.3.4; RFC 7230–7235's wording of 304; measured presence of `ETag` in real-world 304 responses from mainstream servers

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Any HTTP tutorial tells you "304 means the content has not changed"; none tells you the specification requires it, in MUST, to carry `ETag` and `Cache-Control`, and forbids it from having a body.**
>
> The latter two are each a single sentence in the specification, and almost never survive retelling:
> **"must carry that list" determines whether a 304 is complete;
> "may not contain content" matches 204, showing this is the specification's consistent rule for responses with nothing to transfer.**
>
> **This library's mission is to remove noise and store real information.**
> "304 means the content has not changed" is noise — tutorials all cover it.
> "A 304 must carry that cache list, may contain neither content nor trailers, and should keep headers to a minimum" — these sit inside a few MUST and SHOULD NOT sentences of RFC 9110 §15.4.5, **and are what this library should hold**.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-13 | Entry created; an instance filling the "remaining individual codes of RFC 9110 §15.2–§15.6" gap in "What is still missing" | ev-054 registered; topic selected by discipline boundary | @hpleapfrog |
