---
id: kb:computing:prop-http-503-retry-after-is-may-not-must
type: 命题
title: "An HTTP 503's Retry-After is a MAY, not a MUST, and the specification does not require 503 when a server is overloaded"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "must a 503 response carry Retry-After", or "what status code should an overloaded server return"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.6.4 and §15.6.2**; this entry states those two sections' text only, **and has not checked [CACHING] §4.2.2's list of cacheable status codes**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP503的Retry-After是MAY而非MUST且过载时不必用503.md`](HTTP503的Retry-After是MAY而非MUST且过载时不必用503.md).**

## Statement

**For 503 (Service Unavailable), `Retry-After` is a MAY, not a MUST; and the specification does not require a server to return 503 when it is overloaded.**

RFC 9110 §15.6.4 states (short quote):

> The 503 (Service Unavailable) status code indicates that the server is currently
> unable to handle the request due to a **temporary** overload or **scheduled** maintenance,
> which will likely be alleviated after some delay. The server **MAY** send a
> **`Retry-After`** header field (Section 10.2.3) to suggest an appropriate amount of
> time for the client to wait before retrying the request.

The same section's note (short quote):

> **Note:** The existence of the 503 status code **does not imply that a server has to use
> it when becoming overloaded**. Some servers might **simply refuse the connection**.

### 503's definition is narrow: only "temporary overload" and "scheduled maintenance"

§15.6.4's definition lists exactly two situations — **temporary overload** and
**scheduled maintenance** — and requires "which will likely be alleviated after some
delay". **"Any old server error" is not inside 503's definition** — that is 500.

### Contrast: 501 explicitly says it is cacheable; 503 does not

§15.6.2 (`501 Not Implemented`) closes with:

> A 501 response is **heuristically cacheable**; i.e., unless otherwise indicated
> by the method definition or explicit cache controls (see Section 4.2.2 of [CACHING]).

**§15.6.4 contains no corresponding sentence for 503.**

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.6.4** (definition of 503, the MAY for `Retry-After`, the note that overload does not require 503) and **§15.6.2** (501's "heuristically cacheable") | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · "A 503 must carry Retry-After" does not hold at the specification level (not yet attacked)

- **Claim**: **`Retry-After` is a MAY for 503, not a MUST** — **a 503 without `Retry-After` does not violate the specification**
- **Premise**: §15.6.4 says "The server **MAY** send a `Retry-After` header field … **to suggest** an appropriate amount of time" (ev-054)
- **Reasoning**:
  1. This is "what a standard or official document specifies" — exactly what the [computing](../README.en.md) discipline collects
  2. **MAY is the weakest permission level in RFC 2119** — the specification says the server **may** send one **to suggest** a wait, not that it must
  3. Exactly opposite to [401's MUST for `WWW-Authenticate`](HTTP401必须带WWW-Authenticate头部且401与403的分工不是没登录对没权限.en.md) and [304's MUST for the `ETag`-class list](HTTP304响应必须带上原200会发的缓存头部且不能含正文或trailer.en.md): **those use MUST, this one uses MAY**
  4. Criterion: **"a 503 must carry `Retry-After`" is a common misretelling**; the specification says MAY, and the purpose is "**suggest**", not obligation
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · "Overload does not require 503" is the specification's own note (not yet attacked)

- **Claim**: **the specification does not require a server to return 503 when overloaded** — it explicitly allows refusing the connection outright
- **Premise**: §15.6.4's Note: "The existence of the 503 status code **does not imply that a server has to use it when becoming overloaded**. Some servers might **simply refuse the connection**." (ev-054)
- **Reasoning**:
  1. This is a **note** — **the specification itself is warning readers against over-reading it**
  2. So "**overload = 503**" is not the specification's obligation but one permitted option: **refusing the connection (not even accepting the TCP) is equally conformant**
  3. The note's placement is telling: **it sits immediately after 503's definition** — the specification writes 503, then adds at once "do not assume overload must use it"
  4. Same shape as [410's "not necessary to mark all permanently unavailable resources"](HTTP410表示很可能永久消失拿不准就应当用404.en.md): **in both places the specification hands the discretion back**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.6.4 and §15.6.2 only; it does not guarantee the behaviour of any specific server.** "`Retry-After` is a MAY" is the specification's requirement, not a measured fact. Also: **this entry has not checked [CACHING] §4.2.2's list of cacheable status codes**, so **it cannot claim "503 is not cacheable"** — only that §15.6.4 lacks the sentence §15.6.2 has for 501. Also: **this entry has not checked RFC 9110 §10.2.3 (the `Retry-After` field itself)**, nor **how older RFCs (7230–7235) worded 503**.
- **Author**: @hpleapfrog · 2026-10-13
- **To be added**: [CACHING] §4.2.2's list of cacheable status codes; RFC 9110 §10.2.3; RFC 7230–7235's wording of 503; measured presence of `Retry-After` in real-world 503 responses from mainstream servers

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Any HTTP tutorial tells you "503 means service unavailable and should carry Retry-After"; none tells you the specification uses MAY rather than MUST, and none tells you the specification's own note says a server may skip 503 entirely when overloaded and simply refuse the connection.**
>
> The latter two are each a single sentence in the specification, and almost never survive retelling:
> **"MAY, not MUST" determines whether a 503 without `Retry-After` is a violation;
> "overload does not require 503" is the specification warning readers against over-reading it — and in the same document, 401 and 304 use MUST while 503 uses MAY.**
>
> **This library's mission is to remove noise and store real information.**
> "503 means service unavailable and should carry Retry-After" is noise — tutorials all cover it.
> "`Retry-After` is a MAY whose purpose is to suggest; an overloaded server may simply refuse the connection; and 501 is the one that is explicitly cacheable" — these sit inside a few MAY and Note sentences of RFC 9110 §15.6.4 and §15.6.2, **and are what this library should hold**.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-13 | Entry created; an instance filling the "remaining individual codes of RFC 9110 §15.2–§15.6" gap in "What is still missing" | ev-054 registered; topic selected by discipline boundary | @hpleapfrog |
