---
id: kb:computing:resource-rfc9110
type: 资源
title: "RFC 9110, HTTP Semantics (IETF, STD 97)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  资源类型: standard body specification (plain text)
  适用: when you need to check "what the specification says about HTTP methods, status codes and field semantics"
  条件: **applies only to RFC 9110 published in 2022-06**; this repo only verified §2.2 and §9.2 — the remaining sections were not checked
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`RFC-9110-HTTP语义.md`](RFC-9110-HTTP语义.md).**

## Locator

| Item | Value |
|---|---|
| Document | **RFC 9110 · HTTP Semantics** |
| Publisher | IETF |
| Category | **STD 97 · Standards Track** (Internet Standard) |
| Published | **2022-06** |
| Authors | R. Fielding (Adobe) · M. Nottingham (Fastly) · J. Reschke (greenbytes) |
| Obsoletes | RFC 2818 · 7230 · 7231 · 7232 · 7233 · 7235 · 7538 · 7615 · 7694; updates RFC 3864 |
| Structure | 19 chapters + 2 appendices, **10,785 lines total** |
| Official text | <https://www.rfc-editor.org/rfc/rfc9110.txt> |
| Verification depth | **partial** — this repo verified four passages verbatim: the requirements-notation clause in §2.2, safe methods in §9.2.1, idempotent methods in §9.2.2 and **the status-code rules in the preamble to §15**; **the individual codes of §15.2–§15.6 and the remaining sections were not checked** |

> [!IMPORTANT]
> **The structure of this document is itself a piece of information.**
>
> RFC 9110 separates **semantics** from the **HTTP/1.1 messaging syntax**:
> "HTTP/1.1" is defined by **three documents together** — RFC 9110 + `HTTP Caching` + `HTTP/1.1` (the messaging syntax).
> So "what HTTP/1.1 specifies" **is not in any single RFC** — this is the most common locating error when reading the HTTP specifications.

### The four places this repo verified

| Section | Content | Locator |
|---|---|---|
| §2.2 | requirements notation | "…interpreted as described in BCP 14 [RFC2119] [RFC8174] **when, and only when, they appear in all capitals**" |
| §9.2.1 | safe methods | "the `GET`, `HEAD`, `OPTIONS`, and `TRACE` methods are defined to be **safe**" |
| §9.2.2 | idempotent methods | "`PUT`, `DELETE`, and **safe request methods** are idempotent" |
| preamble to §15 | status-code rules | "the **first digit** … defines the class" / "**not required to understand … all registered status codes**" / "Values outside the range **100..599 are invalid**" |

### Licence and citation boundary

> [!CAUTION]
> **This repo does not reproduce the text of RFC 9110.**
>
> Copyright rests with the IETF Trust (BCP 78). **Locator, section numbers and short quotes only.**
> The document is 10,785 lines and this repo verified three sections of it —
> the stated verification depth is **partial**, not full text, and that limit is written into the locator table above.

## How to use

### What this text can and cannot support

| Can | Cannot |
|---|---|
| "**Which class a given method belongs to**" — safe / idempotent / cacheable, §9.2 is explicit | "**How an actual server implements it**" — the specification defines semantics only, not implementations |
| "**Which documents define HTTP/1.1**" — §2.5 says it is the combination of three | "**The messaging syntax of HTTP/2 or HTTP/3**" — those live in other RFCs, not registered here |
| "**How an unrecognized status code is handled**" — the preamble to §15 is explicit | "**The definitions of specific codes such as `204` / `451`**" — §15.2–§15.6 were not checked |
| "**Requirement keywords only hold in all capitals**" — §2.2, verbatim | "**The numeric value of a given requirement**" — this repo verified §2.2 and §9.2 only |

## Argument

### R3 · Why it is worth entering the resource layer (no attack yet)

- **Claim**: RFC 9110 deserves a place in this repo's resource layer
- **Premise**: it is an IETF STD 97 (Internet Standard, **the highest tier in the IETF**),
  with a number, a publication date and publicly accessible official text;
  this repo verified three sections verbatim (ev-054)
- **Reasoning**:
  1. it clears the bar for `资源`: **official locator + accessible + citable sections**
  2. it is the **spine source** for "what the specification says" in the
     [computing](../README.en.md) subject — HTTP is the most-referenced protocol here by a wide margin
  3. "**semantics and syntax live in separate documents**" is itself scarce information:
     almost every online retelling of "the HTTP/1.1 specification" treats the three documents as one
- **Evidence**: ev-054
- **Attacked**: **this repo verified four passages out of 10,785 lines** — §2.2, §9.2.1, §9.2.2 and the preamble to §15.
  That means this entry **cannot support any concrete claim about the individual status codes of §15.2–§15.6,
  §13 conditional requests or §8 representation metadata** — this repo has not read a line of those.
  The general rules from the preamble to §15 are usable, but **questions such as "why may `204` not carry content" are not among them**.
  Also: **this repo has not checked whether RFC 9110 has been updated or amended since**,
  nor has it consulted the RFC Editor's status page for this document.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: a code-by-code check of §15.2–§15.6; the errata list for RFC 9110

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | verification depth widened from "three sections" to "four passages", adding the preamble to §15; "What is still missing" rewritten to match | ev-054 already registered; §15 preamble extended against the priority named in the subject README | @hpleapfrog |
| 2026-10-12 | Entry created; the subject's second `资源` | topic chosen against the subject boundary after ev-054 was registered | @hpleapfrog |
