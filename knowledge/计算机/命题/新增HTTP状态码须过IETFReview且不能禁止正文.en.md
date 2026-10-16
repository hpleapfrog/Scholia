---
id: kb:computing:prop-http-status-code-registration-requires-ietf-review
type: 命题
title: "Adding an HTTP status code requires IETF Review, and the specification forbids new codes from disallowing content"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "what procedure does adding an HTTP status code require", or "can a status code forbid a message body"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §16.2**; this entry states that section's text only, **and has not verified RFC 8126 §4.8's definition of IETF Review**"
edges:
  先修: []
  支持: [kb:computing:prop-http-status-code-list-lives-in-iana]
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`新增HTTP状态码须过IETFReview且不能禁止正文.md`](新增HTTP状态码须过IETFReview且不能禁止正文.md).**

## Statement

**"IETF Review" as written in the IANA registry is not a vague phrase — RFC 9110 §16.2.1 turns it into a hard requirement.**

§16.2.1 "Status Code Registry" states (short quote):

> A registration **MUST** include the following fields:
>
> * Status Code (3 digits)
> * Short Description
> * Pointer to specification text
>
> Values to be added to the HTTP status code namespace require **IETF Review** (see [RFC8126], Section 4.8).

### Three constraints on new codes

§16.2.2 "Considerations for New Status Codes" lists the conditions a new code must satisfy:

| Constraint | Text | Meaning |
|---|---|---|
| **Must fall under a §15 category** | "New status codes are required to fall under one of the categories defined in Section 15." | You cannot invent a sixth class — only 1xx/2xx/3xx/4xx/5xx |
| **Cannot disallow content** | "new status codes **cannot disallow content**, although they can mandate a zero-length content." | You may require an empty body, but you may not forbid having one |
| **Early drafts should not allocate numbers** | "early drafts can use a notation such as **`4NN`**, or **`3N0` … `3N9`**" | Use `4NN`-style notation until consensus exists, to avoid consuming a number prematurely |

### Default scope is a single request

§16.2.2 also governs scope (short quote):

> By default, a status code applies **only to the request corresponding to the response it occurs within**. If a status code applies to a larger scope of applicability … this **must be explicitly specified**.

That is: **even after registration, clients are not obliged to treat a new code as applying to the whole resource** — unless the defining document says so explicitly.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§16.2.1** (registration fields and IETF Review) and **§16.2.2** (constraints on new codes) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · "IETF Review" is a hard gate, not a recommendation (not yet attacked)

- **Claim**: to add a number to the HTTP status-code namespace, **you must pass IETF Review**; this is not "registration is recommended" but a requirement the specification writes in **MUST** and **require**
- **Premise**: §16.2.1 states "A registration **MUST** include…" and "Values … **require** IETF Review" (ev-054)
- **Reasoning**:
  1. This is "what a standard or official document specifies" — exactly what the [computing](../README.en.md) discipline collects
  2. The registry's line "Registration procedure: IETF Review" **is not the registry's own rule**; it **quotes RFC 9110 §16.2.1** — the two are one requirement, not two independent gates
  3. This also explains why `104` went through the **temporary** registration path: it did not pass IETF Review, so it carries an `expires` date (see [The complete list of HTTP status codes lives in the IANA registry, not in RFC 9110](HTTP状态码的完整清单在IANA注册表不在RFC9110里.en.md))
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry states RFC 9110 §16.2 only, and has not verified RFC 8126 (not yet attacked)

- **Claim**: this entry states **what RFC 9110 §16.2 actually says**
- **Premise**: RFC 9110 §16.2.1 points to RFC 8126 §4.8 for the definition of IETF Review, but **the text of RFC 8126 §4.8 has not been read** (ev-054)
- **Reasoning**:
  1. What review process "IETF Review" entails, how many approvals it needs, how long it takes — **RFC 9110 §16.2 only writes "require IETF Review" and does not elaborate**
  2. Therefore this entry **cannot answer "how hard is IETF Review"**
  3. Likewise, §16.2.2 uses **ought to** in several places ("ought to avoid allocating", "ought to explain", "ought to specify") — **these are recommendations, not MUSTs**. This entry labels them "constraints" **by the specification's own modality**: the three hard constraints in the table use "are required to" / "cannot", while the softer "ought to explain the request conditions" requirements **are out of scope here**
- **Evidence**: ev-054
- **Attacked by**: **This library has read RFC 9110 §16.2 only, not RFC 8126 §4.8.** "The specific bar for IETF Review" is unanswerable here. Also: the latter half of §16.2.2 has requirements about **declarations of heuristic cacheability** and **implied association with an identified resource** (§6.4.2) — this entry **takes only the three hardest constraints** and does not expand on the rest.
- **Author**: @hpleapfrog · 2026-10-12
- **To be added**: RFC 8126 §4.8 text; clause-by-clause verification of the second half of §16.2.2 (cacheability and resource association)

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Any tutorial on "how to register an HTTP status code" will tell you to "submit for IETF Review", but none will tell you the specification forbids new codes that disallow a message body.**
>
> The latter is a **counter-intuitive compatibility constraint**: the specification does not allow a new code's definition to say "I forbid a message body", because that would break existing parsers — **existing parsers do not know your new code; they will try to read a body by default**.
>
> **This library's mission is to remove noise and store real information.**
> "Go through IETF Review" is process common sense; tutorials cover it.
> "A new code cannot disallow content, but may require it to be empty" — this sits inside one long sentence of RFC 9110 §16.2.2, **almost never appears in secondary writing**, and it determines whether a new code definition can pass review at all.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; fills the "RFC 9110 §16.2 registration procedure" gap flagged in the previous entry's **To be added** | ev-054 registered; topic selected by discipline boundary | @hpleapfrog |
