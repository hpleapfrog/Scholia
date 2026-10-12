---
id: kb:computing:prop-rfc-keywords-require-uppercase
type: 命题
title: "In an RFC, MUST / SHOULD / MAY carry normative meaning only when written in all capitals"
status: 暂定确认
author: "@hpleapfrog"
created: 2026-10-12
updated: 2026-10-12
scope:
  学科: 计算机 · 标准与规范
  学段: 不限
  适用: when you need to check "does the must / should in this RFC count as a requirement"
  条件: **applies to the BCP 14 pairing (RFC 2119 + RFC 8174)**; this entry only states what BCP 14 says, **and judges the compliance of no specific RFC**
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-052, ev-053]
license: CC-BY-SA-4.0
---

> **English version of [`RFC要求关键词只有全大写才成立.md`](RFC要求关键词只有全大写才成立.md).**

## Statement

IETF's **BCP 14** consists of two documents: **RFC 2119** (1997), which defines the five keywords,
and **RFC 8174** (2017), which adds the capitalisation condition. Together they say:

> The words have the meanings specified herein **only when they are in all capitals**.
> When these words are **not capitalized**, they have their **normal English meanings**
> and are not affected by this document. (RFC 8174 §2)

How RFC 9110 §2.2 cites this:

> …interpreted as described in BCP 14 [RFC2119] [RFC8174] **when, and only when,
> they appear in all capitals**, as shown here. (RFC 9110 §2.2)

The strength of the five keywords (RFC 2119 §1–§5):

| Keyword | Strength | Definition (short quote) |
|---|---|---|
| `MUST` / `MUST NOT` | **absolute** | "an **absolute requirement**" / "an **absolute prohibition**" |
| `SHOULD` / `SHOULD NOT` | **deviable with care** | deviation is allowed, but "**the full implications must be understood and carefully weighed**" |
| `MAY` | **genuinely optional** | "an item is **truly optional**"; implementations must still be prepared to interoperate |

> [!IMPORTANT]
> **A lowercase `must` in a specification is not a requirement, and a lowercase `should` is not a recommendation.**
>
> RFC 8174 puts it more strongly: these words "**can be used as defined here, but using them is not
> required**", and "**a lot of normative text does not use them and is still normative**".
>
> In other words: **capitalisation is not necessary for normativeness, and lowercase is not a marker of non-normativeness.**
> Whether a sentence is a requirement is decided by **where it sits in the specification and how it is worded**,
> **not by the case of these few words**.

## Basis

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-052 | **官方文件** | **高** | [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.txt), BCP 14, 1997-03, **§1–§5** | official public specification · **cite section numbers and short quotes only; no full text reproduced** |
| ev-053 | **官方文件** | **高** | [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.txt), BCP 14, 2017-05, **§2** (OLD / NEW comparison) | official public specification · **cite section numbers and short quotes only; no full text reproduced** |

## Argument

### A1 · The condition is written into the specification itself (no attack yet)

- **Claim**: this set of keywords in RFCs carries normative meaning **only in all capitals**
- **Premise**: RFC 8174 §2 separates the two cases with "**only when they are in all capitals**" and
  "**not capitalized … normal English meanings**"; RFC 9110 §2.2 adopts the new wording
  "when, and only when, they appear in all capitals" (ev-053, ev-054)
- **Reasoning**:
  1. this is "**what the specification says**" — exactly what the [computing](../README.en.md) subject collects
  2. it is **falsifiable by the reader**: open §2 and §2.2 of the two RFCs and read them
  3. the existence of RFC 8174 is itself proof that **this really did cause confusion** —
     its title is literally "Ambiguity of Uppercase vs Lowercase"
- **Evidence**: ev-052, ev-053, ev-054
- **Attacked by**: see A2

### A2 · This entry claims BCP 14's rule only, and judges no specific RFC (no attack yet)

- **Claim**: this entry claims "**BCP 14 says so**", **not "a given sentence in a given RFC is therefore void"**
- **Premise**: RFC 8174 itself states that normative text "**does not require the use of these key words**" —
  text that omits them is still normative (ev-053)
- **Reasoning**:
  1. that is: **a lowercase `must` does not constitute a requirement, but the sentence it sits in may still be one** —
     you have to read the surrounding wording and position, not just the case
  2. deciding "**is this sentence a requirement**" requires reading that RFC end to end,
     and **this repo has never made that kind of sentence-level judgement**
  3. so this entry **cannot be used to support "the lowercase must in RFC 9110 can be ignored"**
- **Evidence**: ev-053
- **Attacked by**: **this repo has checked the actual usage of lowercase `must` in no specific RFC whatsoever.**
  "Is the lowercase must in this RFC actually a requirement" — **this repo has not investigated a single instance.**
  Also: **this repo has not checked whether BCP 14 is still IETF's current Best Current Practice**,
  nor whether any later document amends RFC 2119 or 8174.
- **Attribution**: @hpleapfrog · 2026-10-12
- **To be added**: the current status of BCP 14 at RFC Editor; an instance analysis of lowercase `must` in at least one concrete RFC

## Why this counts as real information rather than noise

> [!IMPORTANT]
> **The body of an RFC never says "these words only count in capitals" — that sentence lives in a different RFC.**
>
> What you can see while reading an RFC is **a sentence containing "must"**;
> what the specifications write down is **two documents jointly deciding how strong that sentence is**.
>
> **This repo's mission is to strip noise and hold true information.**
> That contrast is the test: **the literal text in front of you, this repo need not repeat;
> what is invisible on the page yet written in the standards is what belongs here.**
> "Is this sentence actually a hard requirement" — the question has no answer anywhere in the body of any RFC,
> while BCP 14 turned it into a checkable rule.

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-12 | Entry created; **the subject's first `命题`**, and the second object in the computing subject | topic chosen against the subject boundary after ev-052 and ev-053 were registered | @hpleapfrog |
