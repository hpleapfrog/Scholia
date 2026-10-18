---
id: kb:physics:method-acceleration-al-rate
type: 教法
title: "Acceleration · Advanced: reading a tongue-twister of a sentence with 'the rate of change of a rate of change'"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: students who can already compute acceleration but treat "increasing / decreasing" as a single-layer concept
  条件: already introduced to the distinction between vectors and scalars
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/textbook-tiered-guidance.en.md#a3)"]
  攻击: []
knowledge_point: ["[acceleration](../知识点/acceleration.en.md)"]
evidence: [ev-039]
license: CC-BY-SA-4.0
---

> **English version of [`加速度-AL-矢量与增减之增.md`](加速度-AL-矢量与增减之增.md).**

## Method

### 1 · First check whether the vectors are still there

> `See how much students remember about vectors. What does a vector arrow represent?`
> `Ask them to name some quantities that are vectors and some that are scalars.`

**This is the first item of this section's AL** — the textbook treats "vector / scalar" as a
prerequisite that **needs checking back on**, not something already behind us.

### 2 · Take a tongue-twister of an everyday sentence as the target

> `See if students can use the concept of acceleration to understand confusing statements such`
> `as "a decrease in the rate of increase."`
> `For example, use the concept of acceleration to analyze the statement "the rate of increase`
> `in the cost of health care is decreasing." If the increase in the cost is defined as positive,`
> `then the acceleration in the cost of health care would be negative.`

**The value of this practice: it carries the two layers of rate of change outside physics, letting
students use the tool they just learned to work through a sentence in Chinese.**

| What that sentence says | What it corresponds to in physics |
|---|---|
| "medical costs **are rising**" | velocity is positive |
| "**the rate of increase is falling**" | **acceleration is negative** |
| "costs **are still rising**" | velocity is **still positive** |

**The conclusion is counterintuitive**: **costs are still rising, yet the acceleration is already negative.**
Students must split "rising / falling" and "rising fast / rising slow" into two layers before they
can read that sentence.

### 3 · Along the way, string the base units together

> `Review all the base units of the metric system. Explain how these units are interrelated.`
> `For example, show how length is defined by time.`

**"Length is defined by time" is true in modern metrology** (the metre is defined from the speed of
light and the second) — the textbook uses it to show that **units are not independent of one another**.

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **AL** (textbook marker `[AL]`) |
| Prerequisites | vectors and scalars; the definition of acceleration |
| Cognitive load | medium-high — the difficulty is **mapping a physical quantity onto the two-layer structure of everyday language** |

## Contraindications

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| **students who have not yet told vectors from scalars** | the textbook puts "check the vectors" first in this section's AL — **it is a prerequisite** | **strong** (the textbook lists it first) |
| students who have not yet mastered the base units and rely on memorizing formulas | the second practice draws on the relations among units | **medium** |
| students **outside this tier** (AL) | the textbook marks exactly this passage `[AL]`; the BL and OL tiers get different suggestions | **medium** — the marker explicitly delimits the range, but "not marked" still does not mean "does not apply", only **untested** |

## Risks

| Where it can go wrong | Why |
|---|---|
| the economics example gets treated as a physics problem | **its job is language analysis**; it lands on "two layers of rate of change". Running numbers through it loses its function |
| taught as "'the growth rate is falling' means it has fallen" | **exactly the opposite**: costs **are still rising**. The whole point of this practice is that contrast |
| the vector check is skipped | the textbook puts it first, showing **it expects students to forget**. Skipping it means building everything after it on sand |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-039 | textbook (full text) | low | OpenStax《Physics》 Chapter 3 · Acceleration, [m54123](https://github.com/openstax/osbooks-physics/blob/main/modules/m54123/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the AL tier (no attack yet)

- **Claim**: this is the practice the textbook designates for advanced students
- **Premise**: the Teacher Support of m54123 marks each of the items above `[AL]` (ev-039)
- **Reasoning**: the tier marker is the textbook's designation for that passage
- **Evidence**: ev-039
- **Attacked**: **"textbook-designated" ≠ "measured to be effective"**;
  and **that economics example sentence sits in a US context** (medical costs), so
  **adapting it to Chinese students' context requires rewriting** —
  a **concrete instance** of what this repo's [coverage comparison](../覆盖度/README.md) records as
  "the source of the teaching methods is one American textbook"
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 5) | Issue #8 | @hpleapfrog |
