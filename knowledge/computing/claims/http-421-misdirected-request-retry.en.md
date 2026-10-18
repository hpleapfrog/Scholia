---
id: kb:computing:prop-http-421-misdirected-request-retry
type: 命题
title: "An HTTP 421 means the request was misdirected; the client MAY retry on another connection, and a proxy MUST NOT generate it"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you have received a 421, or are writing a client/proxy and need to know "may a 421 be retried; may a proxy generate one"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.5.20**; this entry states that section's text only, **and has not checked the behaviour of any specific client or proxy**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP421表示请求发到了无法给出权威应答的服务器.md`](HTTP421表示请求发到了无法给出权威应答的服务器.md).**

## Statement

**A 421 (Misdirected Request) response means the request was directed at a server that is unable or unwilling to produce an authoritative response for the target URI.**
A client receiving a 421 **MAY retry over a different connection — even when the request method is not idempotent**; and **a proxy MUST NOT generate a 421**.

RFC 9110 §15.5.20 states (short quote):

> The 421 (Misdirected Request) status code indicates that the request
> was directed at a server that is unable or unwilling to produce an
> authoritative response for the target URI.

> A client that receives a 421 (Misdirected Request) response **MAY** retry
> the request, whether or not the request method is idempotent, over a
> different connection, such as a fresh connection specific to the
> target resource's origin, or via an alternative service [ALTSVC].

> A proxy **MUST NOT** generate a 421 response.

### "Retryable" versus idempotency

Ordinarily a retry must pass the idempotency test (see
[an HTTP method's safety and idempotency are set by the specification](http-method-safety-idempotency.en.md)),
and 421 is a **written** exception: `whether or not the request method is idempotent`.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.5.20** (definition of 421, the client retry permission, the proxy prohibition) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · The 421 retry permission is a written exception that does not require idempotency (not yet attacked)

- **Claim**: a client receiving a 421 may retry over a different connection **whether or not the method is idempotent**
- **Premise**: §15.5.20 states `MAY retry the request, whether or not the request method is idempotent` (ev-054)
- **Reasoning**:
  1. retries normally hinge on method idempotency; 421 is about a request **directed at a server with no authority to answer it** —
     typically the request has not been properly processed, so resending over another connection is unlikely to duplicate side effects
  2. **note: "has not been properly processed" is this repo's reading; the specification gives the permission without stating the reason**
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry does not promise that clients auto-retry, nor settle how a proxy relays a 421 (not yet attacked)

- **Claim**: this entry states the **normative meaning** of 421 and the **normative permissions** of clients and proxies,
  not that "any client will automatically retry on another connection"
- **Premise**: §15.5.20 gives the client a MAY and the proxy a MUST NOT (ev-054)
- **Reasoning**:
  1. a MAY means the client may also **not** retry — automatic behaviour is an implementation choice
  2. the MUST NOT forbids a proxy from **generating** a 421 (421 concerns origin servers and their authority);
     what a proxy should do with a 421 it receives from upstream is not covered by this section — **this entry does not invent a rule for it**
  3. related mechanisms (connection coalescing, alternative services) have not been tested here
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.5.20 only; it does not guarantee the behaviour of any specific client or proxy.** Also: **the origin of 421 in older specifications (the RFC 7231 / RFC 7540 era) has not been checked.**
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: the history of 421 (connection-coalescing background); measured behaviour of mainstream clients on receiving 421

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **"What is a 421" is already rare in tutorials, and these two specification points are almost never retold:**
>
> - **the client MAY retry on another connection, idempotency not required** — on receiving a 421, resending is permitted by the specification, not a gamble;
> - **a proxy MUST NOT generate a 421** — the behavioural rule when writing a proxy: this code is not the proxy's to emit.
>
> **This library's mission is to remove noise and store real information** — these two sentences sit in the MAY and MUST NOT of §15.5.20.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; fills the "421's retry rule" item of the "remaining individual codes" gap | ev-054 already registered; §15.5.20 verified | @hpleapfrog |
