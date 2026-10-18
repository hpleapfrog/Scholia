---
id: kb:computing:prop-http-reserved-deprecated-codes
type: 命题
title: "HTTP 402 is 'reserved for future use', 305 is deprecated and 306 is unused: three registered codes with no semantics"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "can 402 actually be used", "what 305 is", or "why 306 is in the registry"
  条件: "**applies to RFC 9110 (STD 97, 2022-06) §15.5.3, §15.4.6 and §15.4.7**; this entry states those three sections' text only, **and has checked no specific implementation**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054]
license: CC-BY-SA-4.0
---

> **English version of [`HTTP402是保留待用305已废弃306保留不用.md`](HTTP402是保留待用305已废弃306保留不用.md).**

## Statement

**In the specification, 402 has nothing but one sentence — "reserved for future use"; 305 was deprecated in the previous revision; 306 is no longer used and the code is reserved. All three remain in the registry, but the specification defines no behaviour to follow for any of them.**

RFC 9110 §15.5.3 in full is one sentence (short quote):

> The 402 (Payment Required) status code is **reserved for future use**.

§15.4.6 (short quote):

> The 305 (Use Proxy) status code was defined in a previous version of
> this specification and is **now deprecated** (Appendix B of [RFC7231]).

§15.4.7 (short quote):

> The 306 status code was defined in a previous version of this
> specification, **is no longer used, and the code is reserved**.

### "Being in the registry" is not the same as "having semantics in the specification"

All three still occupy registry entries (306 is marked (Unused) in the registry; see [the IANA entry](http-status-code-list-lives-in-iana.en.md)) — but the three quotations above are RFC 9110's **entire** treatment of them. Any story beyond those quotations ("402 is for charging money", "305 is how you route through a proxy") is not in this specification.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-054 | **Official document** | **High** | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.txt), STD 97, 2022-06, **§15.5.3** (402 is one sentence), **§15.4.6** (305 deprecated), **§15.4.7** (306 no longer used and reserved) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · The three codes have "placeholder" in common, not "functionality" (not yet attacked)

- **Claim**: the specification's statements for 402 / 305 / 306 are "reserved for future use / deprecated / no longer used and reserved" — none of the three **defines any implementable semantics**, unlike codes such as 404 or 410 that come with explicit behaviour requirements
- **Premise**: the quotations of §15.5.3, §15.4.6 and §15.4.7 are their entire text (ev-054)
- **Reasoning**:
  1. This is "what a standard and official document stipulates" — exactly what [computing](../README.en.md) collects; retellings such as "402 means payment is required" or "306 is proxy switching" have **no source** in the specification
  2. Registration and semantics are two different things: being in the registry only says who owns the code point; **new semantics must come in through the registration procedure** (see [adding a status code requires IETF Review](http-status-code-registration-requires-ietf-review.en.md)) — until then, 402 is only "reserved"
  3. This is also how the registry governs: **reserve rather than delete**, keeping the slot for the future
- **Evidence**: ev-054
- **Attacked by**: see A2

### A2 · This entry does not forecast 402's future, nor check 305's old semantics (not yet attacked)

- **Claim**: this entry states only what the current RFC 9110 says about the three codes; it does **not** state "whether 402 will ever be enabled" or "the full rules of the old 305"
- **Premise**: §15.4.6 points 305's old semantics at `Appendix B of [RFC7231]` — **that appendix is unchecked here** (ev-054)
- **Reasoning**:
  1. Whether 402 is ever enabled depends on later specifications and the registration procedure; this entry cannot forecast it
  2. Therefore this entry **cannot be used to claim that "receiving a 402 in future is normal" or "the old 305 worked this way"**
- **Evidence**: ev-054
- **Attacked by**: **This entry states the text of RFC 9110 §15.5.3, §15.4.6 and §15.4.7 only; it guarantees no implementation behaviour and predicts no registry change.**
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: RFC 7231 Appendix B (305's old semantics); 402's enablement status (per the latest registry revision)

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **Explanations like "402 is payment", "305 is a proxy" are everywhere; open the specification and the three passages are nearly blank.**
>
> Remembering "they are all registered, and none has semantics" is steadier than remembering any retelling —
> **how the specification defines them: read the quotations; the quotations are just these sentences.**

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; sweeps up the "remaining status codes on the protocol side" gap — the three placeholder codes 402 / 305 / 306 | ev-054 already registered; §15.5.3, §15.4.6, §15.4.7 verified | @hpleapfrog |
