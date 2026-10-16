---
id: kb:computing:prop-http-401-vs-403-must-carry-www-authenticate
type: 命题
title: "An HTTP 401 response MUST carry a WWW-Authenticate header, and the 401 / 403 division is not 'logged out vs no permission'"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-13
updated: 2026-10-13
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "how 401 and 403 are actually divided", or "may a 401 response omit WWW-Authenticate"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.5.2 and §15.5.4**; this entry states those two sections' text only, **and has not checked how any specific framework implements 401 / 403**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP401必须带WWW-Authenticate头部且401与403的分工不是没登录对没权限.md`](HTTP401必须带WWW-Authenticate头部且401与403的分工不是没登录对没权限.md).**

## Statement

**A 401 (Unauthorized) response MUST carry a `WWW-Authenticate` header field; and the division between 401 and 403 is not "logged out versus no permission".**

RFC 9110 §15.5.2 states (short quote):

> The 401 (Unauthorized) status code indicates that the request has not
> been applied because it **lacks valid authentication credentials** for the target
> resource. The server generating a 401 response **MUST** send a **`WWW-Authenticate`**
> header field (Section 11.6.1) containing **at least one challenge applicable to the
> target resource**.

RFC 9110 §15.5.4 states (short quote):

> The 403 (Forbidden) status code indicates that the server **understood the request
> but refuses to fulfill it**. … If authentication credentials were provided in the
> request, the server considers them **insufficient** to grant access. The client
> **SHOULD NOT** automatically repeat the request with the same credentials. The client
> **MAY** repeat the request with new or different credentials. **However, a request might
> be forbidden for reasons unrelated to the credentials.**

### "Unauthorized" in 401 is a historical name, not the semantics

§15.5.2 defines 401 as "**lacks valid authentication credentials**" — that is
**authentication** failure, not an **authorization** decision. The specification's own
wording is "the 401 response **indicates that authorization has been refused for those
credentials**" — so a 401 **can** mean the credentials were refused, but because the
credentials themselves are **invalid**, not because of "who you are / what you may do".

### 403 may have nothing to do with credentials

§15.5.4 states outright:

> **However, a request might be forbidden for reasons unrelated to the credentials.**

The specification also offers an option other than 403 (short quote):

> An origin server that wishes to "**hide**" the current existence of a forbidden
> target resource **MAY instead respond with a status code of 404 (Not Found)**.

### The two codes impose different client behaviour

| Code | Client behaviour |
|---|---|
| **401** | A user agent **MAY** repeat the request with a **new or replaced** `Authorization` header field |
| **403** | The client **SHOULD NOT** automatically repeat with the **same** credentials; it **MAY** repeat with **new or different** credentials |

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.5.2** (definition of 401, the MUST requirement for `WWW-Authenticate`, relation to the Authorization field) and **§15.5.4** (definition of 403, prohibition unrelated to credentials, 404 as a way to hide existence) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · "401 = logged out, 403 = no permission" does not hold at the specification level (not yet attacked)

- **Claim**: the 401 / 403 division is **not "have you logged in"** — **401 is "authentication credentials missing or invalid", 403 is "the server refuses to carry it out"**, and **403 explicitly allows reasons unrelated to credentials**
- **Premise**: §15.5.2 defines 401 as "lacks valid authentication credentials"; §15.5.4 defines 403 as "**understood** the request but **refuses** to fulfill it", and states outright "might be forbidden for reasons **unrelated to the credentials**" (ev-054)
- **Reasoning**:
  1. This is "what a standard or official document specifies" — exactly what the [computing](../README.en.md) discipline collects
  2. The retelling "401 = logged out, 403 = logged in but no permission" **makes authentication versus authorisation the boundary between the two codes**; the specification's boundary is "**whether the server's reason for refusing has anything to do with credentials**"
  3. So "**403 = you lack permission**" is the most common misreading: a 403 can be because **the IP is on a denylist, the method is disallowed, the resource is under maintenance, or the server simply will not show you** — **unrelated to who you are or what credentials you presented**
  4. The converse also holds: **a 401 can arrive when you have already sent credentials** — the specification's own words: "If the request included authentication credentials, then the 401 response indicates that authorization has been refused for those credentials"
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · 401 must carry WWW-Authenticate — a hard, directly checkable constraint (not yet attacked)

- **Claim**: a server generating a 401 **MUST** send a `WWW-Authenticate` header field containing **at least one challenge applicable to the target resource**
- **Premise**: §15.5.2 states "**MUST** send a `WWW-Authenticate` header field … containing **at least one challenge applicable to the target resource**" (ev-054)
- **Reasoning**:
  1. **MUST is the strongest requirement level in RFC 2119** — a 401 without that header **violates the specification**
  2. This yields a **directly checkable criterion**: **a 401 response without `WWW-Authenticate` is not a 401 in the specification's sense**
  3. Same shape as [304's MUST list of `ETag`-class headers](HTTP304响应必须带上原200会发的缓存头部且不能含正文或trailer.en.md): **the specification attaches a MUST-level header list to a code, and that almost never survives retelling**
  4. Practical consequence: **a 401 without `WWW-Authenticate` leaves the client unable to know which authentication scheme to use** — that is the implementation violating the specification, not "401's meaning has changed"
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.5.2 and §15.5.4 only; it does not guarantee the behaviour of any specific framework or server.** "A 401 must carry `WWW-Authenticate`" is the specification's requirement, not a measured fact. Also: **this entry has not checked §11.6.1 (the `WWW-Authenticate` field itself)**, nor **how older RFCs (7230–7235) worded 401 / 403**.
- **Author**: @hpleapfrog · 2026-10-13
- **To be added**: RFC 9110 §11.6.1; RFC 7230–7235's wording of 401 / 403; measured presence of `WWW-Authenticate` in real-world 401 responses from mainstream frameworks

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Any HTTP tutorial tells you "401 means not logged in, 403 means no permission"; none tells you the specification requires 401 to carry a `WWW-Authenticate` header, and none tells you 403 explicitly allows reasons unrelated to credentials.**
>
> The latter two are each a single sentence in the specification, and almost never survive retelling:
> **"must carry `WWW-Authenticate`" yields a directly checkable criterion — a 401 without that header is not a 401 in the specification's sense;
> "403 may be unrelated to credentials" dismantles the most common misreading, "403 = you lack permission".**
>
> **This library's mission is to remove noise and store real information.**
> "401 is logged out, 403 is no permission" is noise — tutorials all cover it.
> "A 401 must carry `WWW-Authenticate`; a 403 may be unrelated to credentials; and 404 may be used instead to hide existence" — these sit inside a few MUST / SHOULD NOT / MAY sentences of RFC 9110 §15.5.2 and §15.5.4, **and are what this library should hold**.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-13 | Entry created; an instance filling the "remaining individual codes of RFC 9110 §15.2–§15.6" gap in "What is still missing" | ev-054 registered; topic selected by discipline boundary | @hpleapfrog |
