---
id: kb:computing:prop-http-206-partial-content-header-duties
type: 命题
title: "An HTTP 206's Content-Length is not the complete resource length (the complete length is in Content-Range), and the server MUST generate the cache and validator headers a 200 would have sent"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "what length a 206's Content-Length is", "does a 206 need cache headers", or "what a client must inspect on a 206"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.3.7 (with §15.3.7.1–§15.3.7.2)**; this entry states that text only, **and has not checked the full details of §14 (the range-request machinery)**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP206的Content-Length不是完整资源长度且必须补齐200会发的头.md`](HTTP206的Content-Length不是完整资源长度且必须补齐200会发的头.md).**

## Statement

**206 (Partial Content) means the server is fulfilling a range request with one or more parts; its Content-Length is the number of octets of this message only (usually not the complete representation's length) — the complete length sits in each Content-Range; and the server MUST also generate the cache and validator headers a 200 would have sent.**

RFC 9110 §15.3.7 states (short quote):

> The 206 (Partial Content) status code indicates that the server is
> successfully fulfilling a **range request** for the target resource by
> transferring one or more parts of the selected representation.

Two obligations that are often overlooked (short quote):

> A client **MUST** inspect a 206 response's Content-Type and Content-Range
> field(s) to determine what parts are enclosed and whether additional
> requests are needed.
>
> A server that generates a 206 response **MUST** generate the following
> header fields … if the field would have been sent in a 200 (OK)
> response to the same request: Date, Cache-Control, ETag, Expires,
> Content-Location, and Vary.

On lengths (short quote):

> A Content-Length header field present in a 206 response indicates the
> number of octets in the content **of this message**, which is usually
> **not the complete length** of the selected representation.  Each
> Content-Range header field includes information about the selected
> representation's **complete length**.

And the caching behaviour (short quote):

> A 206 response is **heuristically cacheable**; i.e., unless otherwise
> indicated by explicit cache controls (see Section 4.2.2 of [CACHING]).

### The hard requirements for single-range and multipart

- Single range (§15.3.7.1): the server **MUST** generate a Content-Range field (short quote);
- Multipart (§15.3.7.2): the server **MUST** use `multipart/byteranges`, the outer HTTP header **MUST NOT** carry Content-Range (it appears inside each part),
  and a server **must not** generate a multipart response to a request that asked for a single range (short quote:
  `A server MUST NOT generate a multipart response to a request for a single range`).

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.3.7** (definition of 206, client and server obligations, the meaning of Content-Length, heuristically cacheable), **§15.3.7.1** (single range), **§15.3.7.2** (multipart) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · In a 206, Content-Length and Content-Range each govern their own length (not yet attacked)

- **Claim**: a 206's Content-Length = the number of octets of **this message** (usually just a part); the complete length is in Content-Range (e.g. the 47022 in `bytes 21010-47021/47022`)
- **Premise**: the length passage of §15.3.7 and the examples of §15.3.7.1 (ev-054)
- **Reasoning**:
  1. "Content-Length is simply the resource size" is a common retelling — inside a 206 it **precisely fails**; a download manager or a resumable-transfer implementation that gets this wrong will miscompute the total progress
  2. The specification also requires the server to **supply the headers a 200 would have sent** (ETag, Cache-Control, Vary, etc.) — this makes a 206 cacheable and revalidatable rather than a one-off fragment
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry does not expand the range-request machinery (not yet attacked)

- **Claim**: the formats and negotiation for Range / If-Range are in §14, and the details of multipart/byteranges in §14.6 — **this entry has not checked those sections**, only the obligations inside §15.3.7 et al.
- **Premise**: §15.3.7 references `Section 14` in several places (ev-054)
- **Reasoning**:
  1. Therefore this entry **cannot be used to claim** behavioural rules such as "whether a server should satisfy a given Range request"
  2. "A client MUST inspect Content-Type and Content-Range" is a hard requirement on clients — it also means a 206 response **must be self-describing**, not assumed to map one-to-one onto the request
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.3.7–§15.3.7.2 only; it does not guarantee the behaviour of any specific implementation.**
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: §14.2 / §14.6 (Range and multipart/byteranges); measurements of 206 headers from mainstream CDNs and static servers

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **"206 = partial content" is noise; "Content-Length is not the full length, the full length is in Content-Range, and the cache headers a 200 would send MUST be supplied" is what this library should hold.**
>
> Resumable downloads, download verification and cache revalidation all stand on these three points —
> **get any one wrong and the symptoms are nowhere on a tutorial's fault list.**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; sweeps up the "remaining status codes on the protocol side" gap — 206's length semantics and header obligations | ev-054 already registered; §15.3.7–§15.3.7.2 verified | @hpleapfrog |
