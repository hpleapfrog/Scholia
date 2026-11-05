---
id: kb:computing:prop-http-202-no-async-status-resend
type: 命题
title: "HTTP 202 does not promise the request will ever be processed, and HTTP has no facility for re-sending a final status code afterwards"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "is 202 just 'accepted, please wait'", or "how will the client be told the result of the task later"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.3.3**; this entry states that section's text only, **and has checked no specific task queue or API implementation**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP202不承诺请求终会被处理且HTTP无法事后补发最终状态码.md`](HTTP202不承诺请求终会被处理且HTTP无法事后补发最终状态码.md).**

## Statement

**202 (Accepted) indicates the request has been accepted for processing but the processing has not been completed; it "might or might not eventually be acted upon"; and HTTP has no way to re-send a final status code from an asynchronous operation afterwards.**

RFC 9110 §15.3.3 states (short quote):

> The 202 (Accepted) status code indicates that the request has been
> accepted for processing, but the processing has not been completed.
> The request **might or might not eventually be acted upon**, as it
> might be disallowed when processing actually takes place.  **There is
> no facility in HTTP for re-sending a status code from an asynchronous
> operation.**

The same section also gives a direction on "how to let the user learn the result" (short quote):

> The 202 response is **intentionally noncommittal**.  Its purpose is to
> allow a server to accept a request for some other process …
> The representation sent with this response **ought to** describe the
> request's current status and point to (or embed) a **status monitor**
> that can provide the user with an estimate of when the request will
> be fulfilled.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.3.3** (definition of 202, no promise of processing, no asynchronous re-send facility, the status-monitor suggestion) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · 202 has three layers, and the third decides asynchronous design (not yet attacked)

- **Claim**: (1) accepted; (2) **it may never actually be carried out**; (3) **HTTP has no mechanism for re-sending a final status code from an asynchronous operation** — the result can only travel over a separate channel (such as the "status monitor" the specification suggests)
- **Premise**: §15.3.3 states `might or might not eventually be acted upon` and `no facility in HTTP for re-sending a status code from an asynchronous operation` (ev-054)
- **Reasoning**:
  1. Tutorials often say "202 = the request succeeded and is being processed in the background" — the specification does not even guarantee it will be acted upon (valid at acceptance, possibly disallowed when it actually runs) and says outright that there is no re-send facility
  2. Therefore "the task finally succeeded / failed" must be expressed by a **separately designed query or notification channel**; the direction the specification gives is for the 202 representation to embed or point to a status monitor
  3. This is why a common architecture (submit a task, get a 202, poll another resource) is **not an implementation's invention but something the specification forces**
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · The "status monitor" is an ought to, not a MUST (not yet attacked)

- **Claim**: this entry does not treat "a 202 must carry status-tracking information" as a hard requirement — the specification uses `ought to`, and what a "monitor" looks like is undefined
- **Premise**: §15.3.3 writes `ought to describe … and point to (or embed)` (ev-054)
- **Reasoning**:
  1. In the RFC 2119 system, `ought to` does not carry the strength of "must" (see [MUST / SHOULD / MAY in an RFC carry normative meaning only when written in all capitals](rfc-keywords-require-uppercase.en.md); this is not even a capitalised SHOULD)
  2. Therefore this entry **cannot be used to claim that "a 202 without a status monitor is a violation"**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.3.3 only; it does not guarantee the behaviour of any specific task queue or API.** Also: **whether older RFC 7231 §6.3.3 words it the same way has not been checked.**
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: comparison with RFC 7231 §6.3.3; measurements of the 202 + polling pattern in mainstream task APIs (record the pattern only, no judgement of merit)

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **"202 = accepted, processing" is noise; "HTTP explicitly says there is no facility for re-sending a final status code afterwards" is what this library should hold.**
>
> That one sentence explains why an asynchronous API must carry its own second channel to fetch results —
> **not a matter of style, but the protocol's capability boundary.**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; sweeps up the "remaining status codes on the protocol side" gap — 202's non-commitment and the absence of any asynchronous re-send | ev-054 already registered; §15.3.3 verified | @hpleapfrog |
