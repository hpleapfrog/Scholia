---
id: kb:computing:prop-http-205-reset-document-view-no-content
type: 命题
title: "HTTP 205 requires the user agent to reset the 'document view', and the server MUST NOT generate content"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "what 205 is for", or "can a 205 carry content"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.3.6**; this entry states that section's text only, **and has checked no specific user agent's reset behaviour**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP205要求重置文档视图且不得生成正文.md`](HTTP205要求重置文档视图且不得生成正文.md).**

## Statement

**205 (Reset Content) indicates that the server has fulfilled the request and desires that the user agent reset the "document view" — the one that caused the request to be sent — to its original state as received from the origin server; and since no further content is intended, the server MUST NOT generate content in a 205 response.**

RFC 9110 §15.3.6 states (short quote):

> The 205 (Reset Content) status code indicates that the server has
> fulfilled the request and **desires that the user agent reset the
> "document view"**, which caused the request to be sent, to its
> original state as received from the origin server.

The same section explains the intended use (short quote):

> This response is intended to support a common **data entry use case**
> where the user receives content that supports data entry (a form,
> notepad, canvas, etc.), enters or manipulates data in that space,
> causes the entered data to be submitted in a request, and then the
> data entry mechanism is **reset for the next entry** …

And the hard prohibition on content (short quote):

> Since the 205 status code implies that no additional content will be
> provided, a server **MUST NOT generate content** in a 205 response.

### The division of labour with 204

[The 204 entry](http-204-cannot-contain-content-or-trailers.en.md) covers "there is no content for you";
205 goes further: **not only is there no content — the client is asked to clear the "input interface" it holds back to its original state**.
It is the protocol-level expression of "clear the form after submitting it".

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.3.6** (definition of 205, intended use, prohibition on generating content) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · 205 is the only code that asks the client to reset its interface (not yet attacked)

- **Claim**: 205's combined semantics = the request is fulfilled + **please reset the document view** + no content may be generated; the last is MUST NOT-level
- **Premise**: the quotations of §15.3.6 (ev-054)
- **Reasoning**:
  1. Retellings often lump 205 in with "roughly the same as 204", but the specification gives it a clear and unique purpose: **clearing the form in a data entry scenario**
  2. "Reset to the original state" is an expectation the server places on the **user agent** — this is 205's core distinction from other 2xx codes
  3. "MUST NOT generate content", like [204](http-204-cannot-contain-content-or-trailers.en.md), is a hard requirement (MUST NOT)
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry does not guarantee that the user agent actually resets anything (not yet attacked)

- **Claim**: this entry states the specification's definition of 205, **not that "a browser or client really performed the reset"**
- **Premise**: §15.3.6 says the server "desires that the user agent reset", but gives no guarantee of implementation consistency (ev-054)
- **Reasoning**:
  1. The boundaries of "document view" and "original state" (form values? canvas? scroll position?) are not itemised in the specification — **this repo has no mechanism for implementation testing**
  2. Therefore this entry **cannot be used to claim that "a page which received a 205 was certainly cleared"**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.3.6 only; it does not guarantee the behaviour of any specific user agent.** Also: **whether older RFC 7231 §6.3.6 words it the same way has not been checked.**
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: comparison with RFC 7231 §6.3.6; measurements of mainstream browsers' reset behaviour on 205

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **"205 = reset content" is noise; "its normative purpose is clearing the form in a data entry scenario, and the server MUST NOT send content" is what this library should hold.**
>
> Knowing this, 205 stops being "204's twin brother" —
> **it is a code that carries an action requirement for the client.**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; sweeps up the "remaining status codes on the protocol side" gap — 205's reset semantics and the prohibition on content | ev-054 already registered; §15.3.6 verified | @hpleapfrog |
