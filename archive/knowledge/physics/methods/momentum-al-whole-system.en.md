---
id: kb:physics:method-momentum-al-whole-system
type: 教法
title: "Conservation of momentum · Advanced: are there perfectly isolated systems on Earth"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: students who can already write p = mv and are about to learn the conditions of conservation
  条件: the definition of momentum has already been taught
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../claims/textbook-tiered-guidance.en.md#a3)"]
  攻击: []
knowledge_point: ["[Conservation of momentum](../concepts/conservation-of-momentum.en.md)"]
evidence: [ev-046]
license: CC-BY-SA-4.0
---

> **English version of [`动量守恒-AL-守恒只能对整体说.md`](动量守恒-AL-守恒只能对整体说.md).**

## Method

The textbook's `[AL]` hint contains **a single move: back “the system” into a corner.**

### 1 · First, take precautions

> `Caution students that momentum is only conserved when the entire system affected`
> `is taken into account.`

**“`Caution`” is strong wording** — the textbook expects students to go wrong here:
**compute only one object, then declare “momentum is not conserved”.**

### 2 · Explain “isolated system” clearly, then ask for examples

> `Explain isolated system.`
> `Ask students to give examples of isolated systems.`

### 3 · Then ask three follow-ups in a row

> `Ask them if these are perfectly isolated.`
> `Would it be possible to have perfectly isolated systems on Earth?`

**These three follow-ups are the core of the whole hint, and the textbook gives no answer.**

| Follow-up question | Where the student needs to get to |
|---|---|
| “are these **perfectly** isolated?” | no — air, friction and gravity are all there |
| “can there be **perfectly** isolated systems **on Earth**?” | **no** |

### 4 · Then what is the conservation law good for

**This is the next sentence students will naturally ask, and the answer is inside the follow-ups themselves:**

Momentum conservation is not a **criterion** for “holds **only** under perfect isolation”,
but an **account** of “under what approximation it holds”.

**Whether a collision may be handled with momentum conservation is decided by “whether the impulse of the external forces at the instant of collision is far smaller than the impulse of the internal forces”** —
in a one-second collision the impulse of air resistance can be ignored; in a one-minute slide, it cannot.

## Conditions of use

| Dimension | Value |
|---|---|
| tier | **AL** (textbook marker `[AL]`) |
| prerequisite | the definition of momentum; knowing the word “system” |
| cognitive load | medium-high — **it is not teaching computation, it is teaching the conditions of applicability** |

## Contraindications

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| students who have not yet formed the concept of “system” | all three follow-ups circle “who counts as included”; without the concept of a system there is nothing to ask about | **strong** — inferred from the nature of the method |
| students who only want to learn how to plug numbers into a formula | this method **gives no formula at all**; everything is spent delimiting the conditions of applicability | **medium** |
| students outside this (AL) tier | the textbook marks this paragraph `[AL]`; the `[OL]` tier has only the one hint “first ask about the word conservation” | **medium** — the marker clearly sets the range, but “not marked” is still not “not applicable”, only **untested** |

## Risks

| Where it can go wrong | Why |
|---|---|
| the follow-ups stopping at “it is not perfectly isolated” | **that is only half the story.** You must also get to “so conservation is an **approximation**, and the question is when this approximation is good enough” |
| teaching it as “the law of conservation of momentum has limitations” | the textbook's wording is `momentum is only conserved **when the entire system** is taken into account` — **this is about usage, not a limitation**. The law is not wrong; the person using it failed to include everything |
| giving the answer away yourself | the textbook asks three questions in a row **and gives no answer**. Handing over the answer cancels the “back it into a corner” step |
| forgetting the opening `Caution` | that is the textbook's warning about **misuse**: **compute only one object and then say “not conserved”** |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-046 | textbook (full text) | low | OpenStax《Physics》Chapter 8 · Conservation of Momentum, [m54202](https://github.com/openstax/osbooks-physics/blob/main/modules/m54202/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the AL tier (no attack yet)

- **Claim**: this is the method the textbook designates for advanced students
- **Premise**: the Teacher Support of m54202 marks the above hint with `[AL]` (ev-046)
- **Reasoning**: the tier marker is the textbook's designation for that paragraph
- **Evidence**: ev-046
- **Attacked**: **“designated by the textbook” ≠ “measured effective”**;
  moreover **step 4 (the “conservation is an approximation” wrap-up) was added by this repo** —
  the textbook asked only three questions and **gave no conclusion**. This is flagged in `Method`.
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: **this hint is only 430 characters** (one of the two sections with the least tiered content in the whole chapter);
  this repo expanded it into four steps, **and the expansion is explanation, not textbook text**

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 7) | Issue #8 | @hpleapfrog |
