---
id: kb:computing:prop-http-1xx-interim-responses
type: 命题
title: "HTTP 1xx responses are interim: they MUST NOT be sent to an HTTP/1.0 client, cannot contain content or trailers, and a client MUST be able to parse one even if it MAY ignore it"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "what 100 / 101 are", "must a client handle a 1xx", or "does a proxy forward 1xx"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.2 (class rules), §15.2.1 (100) and §15.2.2 (101)**; this entry states that text only, **and has not checked the linked details of §10.1.1 (Expect) or §7.8 (Upgrade)**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP1xx是临时响应且不得发给HTTP10客户端.md`](HTTP1xx是临时响应且不得发给HTTP10客户端.md).**

## Statement

**1xx responses are interim — issued before the request's action is complete: they cannot contain content or trailers; a client MUST be able to parse one (even if it does not expect it) but MAY ignore it; a proxy MUST forward them (except those the proxy itself asked to be generated); and they MUST NOT be sent to an HTTP/1.0 client.**

The four rules of RFC 9110 §15.2 (short quote):

> Since HTTP/1.0 did not define any 1xx status codes, a
> server **MUST NOT** send a 1xx response to an HTTP/1.0 client.
>
> A 1xx response is terminated by the end of the header section; it
> **cannot contain content or trailers**.
>
> A client **MUST** be able to parse one or more 1xx responses received
> prior to a final response, even if the client does not expect one.  A
> user agent **MAY** ignore unexpected 1xx responses.
>
> A proxy **MUST** forward 1xx responses unless the proxy itself requested
> the generation of the 1xx response.

### The two members RFC 9110 defines: 100 and 101

How 100 (Continue) fits together (§15.2.1, short quote):

> When the request contains an Expect header field that includes a
> 100-continue expectation, the 100 response indicates that the server
> **wishes to receive the request content** … The client **ought to**
> continue sending the request and discard the 100 response.

The hard requirement of 101 (Switching Protocols) (§15.2.2, short quote):

> The server **MUST** generate an Upgrade header field in the response
> that indicates which protocol(s) will be in effect after this response.

The same section also says (short quote):

> It is assumed that the server will only agree to switch protocols
> when it is advantageous to do so.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.2** (1xx class rules), **§15.2.1** (100), **§15.2.2** (101) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · 1xx carries four rules "nobody usually mentions" (not yet attacked)

- **Claim**: a 1xx cannot contain content or trailers; a client MUST be able to parse one (and MAY ignore it); a proxy MUST forward them; and they MUST NOT be sent to an HTTP/1.0 client — all four are specification text, two of them MUST-level
- **Premise**: the quotations of §15.2 (ev-054)
- **Reasoning**:
  1. Retellings usually cover only "100 continues, 101 upgrades" — never **the restrictions on the recipient** (the HTTP/1.0 prohibition) or **intermediaries' duty** (a proxy MUST forward)
  2. Together the four rules define 1xx's special status: it is **not** a final response but an out-of-band signal about connection and request progress
  3. "MUST be able to parse, MAY ignore" is a robustness requirement on clients — an unseen 1xx must not be allowed to break the connection
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry does not expand the full Expect / Upgrade machinery (not yet attacked)

- **Claim**: the full linkage of 100 with `Expect: 100-continue`, and of 101 with `Upgrade`, lives in §10.1.1 and §7.8 — **this entry has not checked those sections**, only the parts appearing in §15.2.x
- **Premise**: §15.2.1 itself points the details at `Section 10.1.1` (ev-054)
- **Reasoning**:
  1. Therefore this entry **cannot be used to claim** detailed rules such as "when a server must wait for 100-continue"
  2. The protocol switch that follows a 101 (what runs on the connection afterwards) is defined by the protocol being switched to, not by this entry
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.2–§15.2.2 only; it does not guarantee the behaviour of any specific client, proxy or server.**
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: §10.1.1 (Expect) and §7.8 (Upgrade); measurements of mainstream proxies forwarding 1xx

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **"100 continues, 101 switches protocols" is noise; "1xx MUST NOT go to an HTTP/1.0 client, cannot carry content, MUST be parseable by clients and MUST be forwarded by proxies" is what this library should hold.**
>
> These four rules are the practical boundary when writing middleware and clients — **the specification has already assigned the responsibilities; the retellings never show them.**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; sweeps up the "remaining status codes on the protocol side" gap — the interim-response rules and 100 / 101 | ev-054 already registered; §15.2–§15.2.2 verified | @hpleapfrog |
