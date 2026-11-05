---
id: kb:computing:prop-ietf-review-ietf-stream-rfc
type: 命题
title: "IETF Review requires an RFC in the IETF Stream approved by the IESG as having IETF consensus — Standards Track is not required"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you see "new values require IETF Review" and need to know how it is stricter than RFC Required / Standards Action, or to check "does IETF Review require Standards Track"
  条件: "**applies to RFC 8126 (BCP 26, 2017-06) §4.8** (with §4.7, §4.9 and §4.11 for contrast); this entry states the policy's bar only, **and does not describe how any particular registration actually went, nor how long a review takes**"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-089]
license: CC-BY-SA-4.0
---

> **English version of [`IETFReview要求IETFStream的RFC与IESG的共识批准不必是StandardsTrack.md`](IETFReview要求IETFStream的RFC与IESG的共识批准不必是StandardsTrack.md).**

## Statement

**Under the IETF Review policy, new values are assigned only through RFCs in the IETF Stream** — RFCs shepherded through the IESG as AD-sponsored or IETF working group documents, having **gone through IETF Last Call**, and **approved by the IESG as having IETF consensus**. **Any RFC type is sufficient**; Standards Track is not required.

RFC 8126 §4.8 states (short quote):

> With the IETF Review policy, new values are assigned only through
> RFCs in the IETF Stream -- those that have been shepherded through
> the IESG as AD-Sponsored or IETF working group documents …, have gone
> through IETF Last Call, and have been approved by the IESG as having
> IETF consensus.

Two more sentences from the same section (short quote):

> Formerly called "IETF Consensus" in the first edition of this
> document.

> Unless otherwise specified, any type of RFC is sufficient (currently
> Standards Track, BCP, Informational, Experimental, or Historic).

§4.11 summarises the two neighbouring rungs (short quote):

> 8. IETF Review
>    RFC publication, IETF Stream only, but need not be Standards
>    Track.
>
> 9. Standards Action
>    RFC publication, IETF Stream, Standards Track or BCP only.

### How the three neighbouring policies divide

| Policy | Stream | RFC type |
|---|---|---|
| **RFC Required** (§4.7) | IETF / IRTF / IAB / Independent, **any** | any type |
| **IETF Review** (§4.8) | **IETF Stream only** | **any type** |
| **Standards Action** (§4.9) | **IETF Stream only** | **Standards Track or BCP only** |

**The two bars tighten separately: first the stream (to the IETF), then the RFC type (to Standards Track).**
IETF Review sits in the middle — it does not demand Standards Track; it demands **community review and the IESG's consensus judgement**.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-089 | **Official document** | **High** | [RFC 8126](https://www.rfc-editor.org/rfc/rfc8126.txt), BCP 26, 2017-06, **§4.8** (the definition of IETF Review and its former name), **§4.7** (RFC Required, for contrast), **§4.9** (Standards Action, for contrast), **§4.11** (the strictness ladder) | Official public specification · **cites section numbers and short quotations only; does not reproduce the full text** |

## Argument

### A1 · IETF Review does not require Standards Track (not yet attacked)

- **Claim**: the bar of IETF Review is "an RFC in the IETF Stream approved by the IESG as having IETF consensus",
  with **no type restriction**; reading IETF Review as "Standards Track approval" is a misreading
- **Premise**: §4.8 `Unless otherwise specified, any type of RFC is sufficient`;
  §4.11's summary of rung 8, `need not be Standards Track` (ev-089)
- **Reasoning**:
  1. the specification states the two requirements separately: "review and consensus" and "Standards Track" are **two independent bars**
  2. Standards Action (rung 9) is the one demanding "IETF Stream + Standards Track or BCP" —
     were IETF Review to require Standards Track already, the two policies would be indistinguishable
- **Evidence**: ev-089
- **Attacked by**: see A2

### A2 · This entry gives the policy's bar only; it does not audit any particular registration (not yet attacked)

- **Claim**: this entry states the **normative definition** of the policy; it does not judge which path any particular registration took, and gives no review-duration figure
- **Premise**: §4.8 defines the conditions for "assigning new values"; §4.11 adds policy-selection requirements —
  pick the least strict policy that suits the registry, and justify anything stricter (ev-089)
- **Reasoning**:
  1. "the new value appears in an RFC in the IETF Stream" is a **process fact checkable against the RFC publication record**;
     this entry states the bar, while auditing a particular registration is the reader's and the registry's task
  2. RFC 9110 §16.2.1 requires IETF Review for status-code registrations —
     this entry supplies exactly the missing "bar" piece of that claim (see
     [adding an HTTP status code requires IETF Review, and the specification forbids new codes from disallowing content](http-status-code-registration-requires-ietf-review.en.md))
- **Evidence**: ev-089
- **Attacked by**: **the remaining sections of RFC 8126 are unchecked by this repo** (e.g., §3.4 Early Allocations, §4.13 Provisional Registrations, §5 Designated Experts),
  and so is any difference between current IETF practice documents (e.g., IESG statements on AD-sponsored work) and the §4.8 text.
- **Author**: @hpleapfrog · 2026-10-18
- **To be added**: the rest of RFC 8126; comparison against current IETF process documents

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **"Requires IETF Review" hangs on a large number of registries, yet the bar itself is only visible in BCP 26 §4.8.**
>
> The two things most often misread: **IETF Review does not require Standards Track** (Informational, Experimental and the rest are all sufficient);
> **Standards Action is the one requiring Standards Track or BCP**. And RFC Required does not even require the IETF Stream.
> Side by side, the three policies show exactly where they differ — the three lines a retelling never gives.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-18 | Entry created; fills the "what bar does IETF Review set" item of "What is still missing"; §4.8 verified (with §4.7 / §4.9 / §4.11 read for contrast) | ev-089 registered (RFC 8126 full text) | @hpleapfrog |
