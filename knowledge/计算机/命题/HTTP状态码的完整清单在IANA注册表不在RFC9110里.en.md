---
id: kb:computing:prop-http-status-code-list-lives-in-iana
type: 命题
title: "The complete list of HTTP status codes lives in the IANA registry, not in RFC 9110"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "is this HTTP status code standard", or "is this RFC the complete status-code table"
  条件: "**applies to the 2025-09-15 version of the IANA registry**; this entry states that version's contents only, **and has verified no earlier or later version**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054, ev-057]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP状态码的完整清单在IANA注册表不在RFC9110里.md`](HTTP状态码的完整清单在IANA注册表不在RFC9110里.md).**

## Statement

**§15 of RFC 9110 is not the complete status-code table.** The full list lives in IANA's
**"Hypertext Transfer Protocol (HTTP) Status Code Registry"**, which states of itself:

| Item | Value |
|---|---|
| Registration procedure | **IETF Review** |
| Reference | **RFC 9110, Section 16.2.1** |
| Last Updated | **2025-09-15** |

RFC 9110 §15.1 concedes as much (short quote):

> **Additional status codes, outside the scope of this specification**, have been specified for use in HTTP.
> All such status codes **ought to be registered** within the "Hypertext Transfer Protocol (HTTP) Status Code Registry"…

### Codes in the registry that are not in RFC 9110 (the main ones)

| Code | Name | Source |
|---|---|---|
| `102` | Processing | RFC 2518 |
| `103` | Early Hints | RFC 8297 |
| `104` | Upload Resumption Supported | draft-ietf-httpbis-resumable-upload-05 (**temporary registration**, see below) |
| `207` | Multi-Status | RFC 4918 |
| `208` | Already Reported | RFC 5842 |
| `226` | IM Used | RFC 3229 |
| `423` | Locked | RFC 4918 |
| `424` | Failed Dependency | RFC 4918 |
| `425` | Too Early | RFC 8470 |
| `428` / `429` / `431` / `511` | Precondition Required / Too Many Requests / Request Header Fields Too Large / Network Authentication Required | all RFC 6585 |
| **`451`** | **Unavailable For Legal Reasons** | **RFC 7725** |

### Three entries easy to misread

| Code | How the registry writes it | Meaning |
|---|---|---|
| `306` | **`(Unused)`** | RFC 9110 §15.4.7: **"no longer used, and the code is reserved"** (defined in an earlier version, now retired and reserved) |
| `418` | **`(Unused)`** | from the April 1 RFC 2324, reserved because it was deployed too often — see [418 is not a status code in the specification](../误解/418不是规范里的状态码.en.md) |
| `104` | **"TEMPORARY - registered 2024-11-13, extension registered 2025-09-15, expires 2026-11-13"** | **a code with an expiry date**. After that date it may be removed |

> [!IMPORTANT]
> **`104` is a status code with a use-by date.**
>
> The registry gives it three dates and an `expires`.
> That is: **the answer to "is 104 a standard code" depends on when you ask.**
>
> This is an instance, inside the computing subject, of the [economics](../../经济/README.en.md) subject's rule that
> "**timeliness is the main point of attack**" — **this repo records the 2025-09-15 version of the registry**,
> and the entry itself says it changes on 2026-11-13.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-057 | **官方文件** | **高** | [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml), **last updated 2025-09-15**, **the whole table** | official public registry · **cite entries and short quotes only; no full table reproduced** |
| ev-054 | **官方文件** | **高** (for a claim of this kind) | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.1** ("Additional status codes, outside the scope of this specification") | official public specification · **cite section numbers and short quotes only; no full text reproduced** |

## Argument

### A1 · The complete list is the registry, not any single RFC (no attack yet)

- **Claim**: to decide whether a status code is standard, **consult the registry, not RFC 9110**
- **Premise**: the registry lists every entry in 100–599 with its Reference; RFC 9110 §15.1 itself says status codes "outside the scope of this specification" ought to be registered there (ev-057, ev-054)
- **Reasoning**:
  1. this is "**what a specification or official documentation says**" — exactly what the [computing](../README.en.md) subject collects
  2. it is **falsifiable by the reader against the registry, entry by entry**
  3. **it fixes the boundary of the previous claim (an unrecognized code is handled as `x00`)**:
     "unrecognized" does not mean "nonexistent" — `451` is not in RFC 9110, yet it is a registered standard code.
     A client implementing only RFC 9110 §15 **would handle `451` as `400`**, which the specification permits, **but that does not make `451` non-standard**
- **Evidence**: ev-054, ev-057
- **Attacked by**: see A2

### A2 · This entry states the 2025-09-15 registry only (no attack yet)

- **Claim**: this entry states "**what the registry held on 2025-09-15**",
  **not "what the registry holds now"**
- **Premise**: the registry carries its own `Last Updated 2025-09-15`, and the `104` entry states **expires 2026-11-13** (ev-057)
- **Reasoning**:
  1. registries change: new codes are added, temporary codes expire. **This repo has no version-detection mechanism**
  2. `104`'s expiry is **under a year after this entry was written**,
     and after that date **this entry's wording about 104 may simply be wrong**
  3. so this entry **cannot support "the registry still reads like this today"**
- **Evidence**: ev-057
- **Attacked by**: **this repo read one version of the registry, 2025-09-15.**
  What earlier versions said, and **whether the registry has been updated since this entry was written**, this repo has no idea.
  Also: **this repo verified only §15.1 and the preamble of §15 of RFC 9110** —
  the registration procedure in §16.2 was unread at the time of writing; it was verified the same day in
  [Adding an HTTP status code requires IETF Review, and the specification forbids new codes from disallowing content](新增HTTP状态码须过IETFReview且不能禁止正文.en.md),
  where "IETF Review"'s source and the three hard constraints are now traceable.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: any registry update after 2025-09-15; RFC 8126 §4.8's definition of IETF Review

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Every HTTP tutorial appends a status-code table; none of them writes out "the authoritative version of this table is elsewhere".**
>
> What you see in a tutorial is a table that **looks closed**;
> what the specification holds is that **the table is open, has its own registration body, and that some codes are not even in the same RFC**.
>
> **This repo's mission is to strip noise and hold true information.**
> That contrast is the test: **the meaning of individual codes, this repo need not repeat;**
> **"how the table itself is maintained, and where to find its current version" is what belongs here.**
> "Is `451` a standard code" — the question has no answer in RFC 9110 (it is not in that section),
> while the registry lists it with its source: **RFC 7725.**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; the subject's fourth `命题` | topic chosen against the subject boundary after ev-057 was registered | @hpleapfrog |
| 2026-10-12 | The "§16.2 registration procedure" item under **To be added** has been filled by a new entry written the same day; **Attacked by** updated in step | ev-054 registered; topic chosen against the subject boundary | @hpleapfrog |
