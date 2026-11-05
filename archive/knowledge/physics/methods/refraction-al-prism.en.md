---
id: kb:physics:method-refraction-al-prism
type: 教法
title: "Refraction · Advanced: a prism disperses light, why does window glass not"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: students who can already use n = c/v and the law of refraction and are about to understand dispersion
  条件: can already compute with sine / arcsine
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../claims/textbook-tiered-guidance.en.md#a3)"]
  攻击: []
knowledge_point: ["[refraction of light](../concepts/refraction.en.md)"]
evidence: [ev-038]
license: CC-BY-SA-4.0
---

> **English version of [`折射-AL-棱镜为何分光.md`](折射-AL-棱镜为何分光.md).**

## Method

### 1 · Pose a contrast that can only be answered with the same set of formulas

> `Ask students to try to explain why a prism separates white light into a rainbow of colors,`
> `but a window pane does not.`
> `If they cannot explain it, show them a ray diagram of light transmitted through a flat`
> `sheet of glass.`

**Note the fallback the textbook provides**: if students cannot answer, **it does not hand over the
answer — it shows a ray diagram**.

| | Prism | Window glass |
|---|---|---|
| the two surfaces | **not parallel** (they meet at an angle) | **parallel** |
| refraction of each colour | each time it crosses a surface it **spreads out a little more**; the two deflections **add in the same direction** | the second deflection **cancels** the first |
| after exiting | the colours are **separated** | **recombined into one beam**, parallel to the incident direction |

**The same `n` and the same law of refraction, and the two pieces of glass behave differently — the only difference is geometry.**

### 2 · First make sine clear at the level of a right triangle

> `The trigonometric function sine (sin) for a given angle is the ratio of the side of a right`
> `triangle opposite that angle to the hypotenuse of that triangle.`

**This is what the textbook adds for the AL tier** — meaning that at the OL tier it **assumed**
students already knew it.

### 3 · Line the five special angles up into a pattern

> `Show why the values sin 0°, sin 30°, sin 45°, sin 60°, and sin 90° can be expressed in the`
> `form ½√0, ½√1, ½√2, ½√3, ½√4.`
> `Show that the numerical values of these expressions are 0, 0.5, 0.707, 0.866, and 1.00.`

**The use of this form**: students do not have to memorize five separate numbers; they only need to
remember **filling 0 through 4 into the root, one after another**.

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **AL** (textbook marker `[AL]`) |
| Prerequisites | the law of refraction; sine and arcsine; **how to read a ray diagram** |
| Cognitive load | high — holding on to **the geometry of two surfaces** and **the per-colour deflection** at the same time |

## Contraindications

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| **students who cannot yet use the law of refraction to compute a two-surface problem** | the prism's answer is **the superposition of two deflections** — computing one is not enough | **strong** — inferred from the nature of the practice |
| students who have not yet formed the concept "white light is a mixed light" | this practice explains **why the colours separate**, which presupposes that they **were different to begin with** | **medium** |
| students **outside this tier** (AL) | the textbook marks exactly this passage `[AL]`; the BL and OL tiers get different suggestions | **medium** — the marker explicitly delimits the range, but "not marked" still does not mean "does not apply", only **untested** |

## Risks

| Where it can go wrong | Why |
|---|---|
| the answer is given away directly | the textbook's way is **let students try to explain first**, and only show the ray diagram if they cannot — **that diagram is a hint, not the answer** |
| saying "a prism can change the colour of light" | the prism **does not change any single colour**; it only **separates what was mixed together**. This is the commonest wrong statement about dispersion |
| "window glass does not refract" | window glass **refracts all the same**; it is just that **the two deflections point in opposite directions and cancel each other**. Teaching it as "does not refract" overturns the law already learned |
| the five special angles become pure memorization burden | what the textbook gives is a **structure** (`½√n`), not five isolated values |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-038 | textbook (full text) | low | OpenStax《Physics》 Chapter 16 · Refraction, [m54365](https://github.com/openstax/osbooks-physics/blob/main/modules/m54365/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the AL tier (no attack yet)

- **Claim**: this is the practice the textbook designates for advanced students
- **Premise**: the Teacher Support of m54365 marks each of the items above `[AL]` (ev-038)
- **Reasoning**: the tier marker is the textbook's designation for that passage
- **Evidence**: ev-038
- **Attacked**: **"textbook-designated" ≠ "measured to be effective"**;
  and the textbook's original `show them a ray diagram` **points at a figure in the main text**,
  which this entry **has not copied** (a copyright red line, see `CONTRIBUTING.md`) —
  implementers need to go to the corresponding place in the textbook themselves
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 4) | Issue #8 | @hpleapfrog |
