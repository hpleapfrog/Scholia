---
id: kb:physics:method-refraction-bl-geometry
type: 教法
title: "Refraction · below grade level: patch the geometry first, then derive n > 1"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 初中至高中
  水平档: 低于年级水平（BL）
  适用: students whose concept of an angle is shaky, or who plug numbers into formulas without looking at what they mean
  条件: none
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../claims/textbook-tiered-guidance.en.md#a3)"]
  攻击: []
knowledge_point: ["[Refraction of light](../concepts/refraction.en.md)"]
evidence: [ev-038]
license: CC-BY-SA-4.0
---

> **English version of [`折射-BL-几何前提与n大于1.md`](折射-BL-几何前提与n大于1.md).**

## Method

The textbook's `[BL]` hints **do not touch the law of refraction**; they only fill in two things that come earlier.

### 1 · Get "angle" straight first

> `An angle is the measure of the separation of two lines or rays originating from a single`
> `point. The length of the lines is not relevant.`

**That last sentence is the key**: when students draw diagrams they link "the size of an angle" to "how long the lines are drawn".
The textbook singles this out and denies it.

> [!IMPORTANT]
> **This hint also appeared once in the "reflection of light" module** (ev-026) — different wording, same content.
>
> | Module | Exact wording |
> |---|---|
> | Reflection (m54357) | `angles are numbers that tell how far two straight lines are spread apart` |
> | **Refraction (m54365)** | `An angle is the measure of the separation of two lines or rays originating from a single point` |
>
> **The textbook told the same thing once in each of two places.** This is evidence that "the geometric angle" is a **real and recurring prerequisite**
> (and also evidence that this repo lacks that node, see [refraction of light](../concepts/refraction.en.md)).

### 2 · `n > 1` must be **derived**, not memorized

> `Be sure students understand that if c is always greater than v, n must always be greater`
> `than one. Demonstrating division using numbers that can be divided easily can reinforce`
> `student understanding.`

**The method has two steps**:

1. **Logic**: light is fastest in a vacuum ⇒ `c > v` ⇒ `c / v > 1`
2. **Numerical example**: **deliberately pick numbers that divide evenly** to do the division, so students see for themselves that `n` is always greater than 1

**The design of the second step is deliberate** — "divides evenly" means **students need not be distracted by arithmetic**,
and attention stays entirely on "the result is bigger than 1".

### 3 · One equation, three quantities: knowing two is enough

> `If an equation has two variables and a constant, such as n=c/v, the value of only one`
> `variable is needed to find the other.`

**This fills in the "solving equations" layer**: `n = c / v` has three symbols, but `c` is a constant,
so **one variable suffices to find the other**.

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **BL** (textbook tag `[BL]`) |
| Prerequisites | the concept of an angle (**this repo has no corresponding node yet**); can do division |
| Cognitive load | low — the textbook deliberately **sidesteps the law of refraction** and only fills in prerequisites |

## Contraindications

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| students who can already use the law of refraction fluently | this method **does not do the law of refraction**; for them it is a pure waste of time | **strong** — follows from the nature of the method |
| students **outside** this tier (BL) | the textbook tags exactly that passage `[BL]`; the OL and AL tiers get different suggestions | **medium** — the tag clearly draws the scope, but "not tagged" still ≠ "does not apply", it is merely **untested** |

## Risks

| Where it can go wrong | Why |
|---|---|
| telling "an angle has nothing to do with segment length" without a counterexample | students **will still** make this mistake when drawing. The textbook specifically denies it, showing it expects students already think this way |
| telling `n > 1` as "remember that refractive indices are all greater than 1" | the textbook's wording is `Be sure students understand that **if** c is always greater than v, **then** …` — **it is a piece of reasoning, not a fact** |
| going through the "divides evenly" example carelessly | picking numbers that divide evenly is **there to keep attention on the conclusion**; swapping in hard numbers ruins that step |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-038 | textbook (full text) | low | OpenStax《Physics》Chapter 16 · Refraction, [m54365](https://github.com/openstax/osbooks-physics/blob/main/modules/m54365/index.cnxml) | **CC BY 4.0** |
| ev-026 | textbook (full text) | low | OpenStax《Physics》Chapter 16 · Reflection, [m54357](https://github.com/openstax/osbooks-physics/blob/main/modules/m54357/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the BL tier (no attack yet)

- **Claim**: this is the method the textbook specifies for below-grade-level students
- **Premise**: the Teacher Support of m54365 tags each of the above lines with `[BL]` (ev-038)
- **Reasoning**: a tier tag is the textbook's designation for that passage
- **Evidence**: ev-038, ev-026
- **Attacked**: **"the textbook specifies it" ≠ "measured to be effective"**;
  moreover both items of evidence **come from the same publisher**, so by `FORMAT.md` §6 they **are not independent evidence**
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 4) | Issue #8 | @hpleapfrog |
