---
id: kb:computing:miscon-http-418-is-real
type: 误解
title: "Treating 418 as a normative HTTP status code"
status: 有效
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: anyone who believes "418 I'm a teapot" is one of the standard HTTP status codes
  条件: "**applies to RFC 9110 (2022-06) and the 2025-09-15 version of the IANA registry**; both label 418 as `(Unused)`"
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-054, ev-057]
license: CC-BY-SA-4.0
---

> **English version of [`418不是规范里的状态码.md`](418不是规范里的状态码.md).**

## Statement

Many people treat **`418 I'm a teapot`** as one of HTTP's standard status codes, on the grounds that "it is everywhere". **It is not.**

Both normative sources label it **`(Unused)`**:

| Source | How it is written |
|---|---|
| **IANA registry** (2025-09-15) | `418` · Description = **`(Unused)`** · Reference = RFC 9110 §15.5.19 |
| **RFC 9110 §15.5.19** | the heading itself is **`418 (Unused)`**, with the body explaining why it was reserved |

The source text of RFC 9110 §15.5.19 (short quote):

> **[RFC2324] was an April 1 RFC** that lampooned the various ways HTTP was abused;
> one such abuse was the definition of an application-specific 418 status code,
> **which has been deployed as a joke often enough for the code to be unusable for any future use.**

Unpacked, three steps:

1. **RFC 2324 is an April 1 RFC**, satirising the various ways HTTP gets abused
2. one of those satires was **defining an application-specific 418**
3. the joke **was deployed so often** that **the code can no longer be used for any real purpose**

### Reserved is not permanent: 418 can be re-assigned when 4NN is exhausted

The latter half of the same section carries three more sentences, **and almost none of them survive retelling** (short quote):

> Therefore, the 418 status code is **reserved** in the IANA HTTP Status Code Registry.
> This indicates that the status code **cannot be assigned to other applications currently**.
> **If future circumstances require its use (e.g., exhaustion of 4NN status codes), it can be
> re-assigned to another use.**

Unpacked, three points:

1. 418 is **reserved** in the IANA registry — so **appearing in the registry does not make it an available code**
2. it **currently** cannot be assigned to other applications — **"currently" is a word with a time limit**
3. **if future circumstances require it (e.g., exhaustion of 4NN), it can be re-assigned to another use**

> [!IMPORTANT]
> **418's status is "reserved for now", not "retired for good".**
>
> **"cannot be assigned … currently" and "can be re-assigned" are two halves of the same passage** — the specification says both that it may not be used now **and** that it may be taken up for something else later.
>
> So "418 is a teapot forever" **does not hold at the specification level**:
> **418 is merely "unused for now", waiting on a use that may come later.**
> This point was absent when the entry was created (2026-10-12) and was added on 2026-10-13 —
> **the missing piece was exactly this half of the passage.**

> [!IMPORTANT]
> **418 was reserved precisely because it became too popular.**
>
> The specification does not say "the joke is tired"; it says **"deployed as a joke often enough for the code to be unusable"** —
> **the volume of use is what burned the code.**
>
> So "it is everywhere" **is not evidence that it is a standard code; it is the reason it is not.**
> The causation runs the other way, and that is exactly why this misconception does not correct itself.

## Frequency

> [!WARNING]
> **This entry has no quantitative data.**
>
> This repo has **not counted** how many documents, libraries or tutorials treat 418 as a standard code.
> "It is everywhere" is a qualitative observation, **not a measurement**.
>
> The only verifiable basis right now is **both normative sources labelling it `(Unused)`**.
> That proves "418 is not a standard code", **but it does not prove "how many people believe it is"** —
> **the two are not the same thing, and the former must not be passed off as the latter.**

## Why record it

> [!WARNING]
> This misconception **is extremely hard to correct from within**, because it comes with what looks like evidence:
> **"I have seen it in a lot of places."**
>
> And RFC 9110's causation runs the other way — **you have seen it often because it was deployed as a joke often.**
>
> Worse: **many HTTP libraries really do return 418** (as a wry placeholder),
> so the observation **"a server really did return 418" is also insufficient** to show it is standard.
> Falsifying this misconception **requires going back to the specification and the registry**;
> observational evidence fails here.

## Argument

### M1 · Two independent normative sources both mark it (Unused) (no attack yet)

- **Claim**: 418 **is not** a status code in the specification; it is a reserved code
- **Premise**: the 2025-09-15 IANA registry writes `418`'s Description as `(Unused)` and points the Reference at RFC 9110 §15.5.19; that section's heading is itself `418 (Unused)` (ev-057, ev-054)
- **Reasoning**:
  1. this is "**what a specification or official documentation says**" — exactly what the [computing](../README.en.md) subject collects
  2. it is **falsifiable by the reader against the registry and the RFC, verbatim**
  3. **two independent publishing bodies reach the same conclusion** (IANA and the IETF), and the IANA Reference points straight at the corresponding RFC section, so the two cross-check
- **Evidence**: ev-054, ev-057
- **Attacked by**: see M2

### M2 · This entry judges no specific implementation that returns 418 (no attack yet)

- **Claim**: this entry states "**418 is not in the specification**", **not "my server may not return 418"**
- **Premise**: RFC 9110 itself says the code **"has been deployed as a joke often enough"** — that is, **large-scale deployment does exist** (ev-054)
- **Reasoning**:
  1. some framework or API returning 418 **is a fact**, and this entry does not deny it
  2. but **"deployment exists" and "the specification defines it" are two different things**:
     the preamble to §15 states that status codes are extensible and that an unrecognized code is handled as the class's `x00`,
     so a service returning 418 **is equivalent at the protocol level to returning 400**
  3. so this entry **cannot support "a service returning 418 is non-conformant"** —
     under the preamble to §15, its behaviour is **interpretable**
- **Evidence**: ev-054, ev-057
- **Attacked by**: **this repo has verified no specific library or framework that returns 418.**
  "Which library returns 418, and when" — **this repo has not investigated a single case.**
  Also: **this repo has not read RFC 2324 itself**, only RFC 9110's retelling of it.
  What else RFC 2324 says, and whether any later April 1 RFC exists, **this repo has no idea.**
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the text of RFC 2324; a measured list of implementations that return 418

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-13 | added the latter half of §15.5.19's "reserved is not permanent": 418 may be re-assigned when 4NN is exhausted; the corresponding gap in "What is still missing" is now filled | ev-054 already registered; §15.5.19 re-read in full | @hpleapfrog |
| 2026-10-12 | Entry created; **the subject's first `误解`**, and the first `误解` in this repo outside physics | topic chosen against the subject boundary after ev-057 was registered | @hpleapfrog |
