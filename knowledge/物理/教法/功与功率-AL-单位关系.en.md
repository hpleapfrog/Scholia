---
id: kb:physics:method-work-al-unit-relations
type: 教法
title: "Work and power · Advanced: deriving from the units why we buy kilowatt-hours"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  水平档: 进阶（AL）
  适用: students who can do unit conversions and need to connect the formulas to the bill
  条件: none
edges:
  先修: []
  支持: ["[命题：教材内建分组教学变体](../命题/教材内建分组教学变体.md#a3)"]
  攻击: []
knowledge_point: ["[work and power](../知识点/功与功率.md)"]
evidence: [ev-036]
license: CC-BY-SA-4.0
---

> **English version of [`功与功率-AL-单位关系.md`](功与功率-AL-单位关系.md).**

## Method

**No new physics is taught; just walk the derivation chain of the three units through, then land it on an electricity bill.**

Textbook original (short quotation):

> `If W = fd and work can be expressed in J, then P = W/t = fd/t so power can be expressed in
> units of N·m/s. Also explain that we buy electricity in kilowatt-hours because, when power is
> multiplied by time, the time units cancel, which leaves work or energy.`

**Derivation chain:**

```
W = f·d          → joule J = N·m
P = W/t = f·d/t  → watt W = N·m/s
P × t            → time cancels out, back to work / energy
```

**So a "kilowatt-hour" is a unit of energy, not of power.**

The textbook has one more `[AL]` item in the same section: remind students that the
**gravitational acceleration in `W = PE = mgh` is a constant**, so the potential energy computed
from the work done by gravity is also constant; whereas **other forces (such as holding a stone up
by hand) are not necessarily constant** — this is **making an implicit assumption explicit**.

## Conditions of use

| Dimension | Value |
|---|---|
| Level tier | **AL** (textbook marker `[AL]`) |
| Prerequisites | can do unit conversions; knows `W = fd` and `P = W/t` |
| Cognitive load | medium — the load is in **the direction of the unit chain**, not in new concepts |

## Contraindications

**Who or what situations does it not apply to?**

| Who or situation it does not apply to | Basis | Strength |
|---|---|---|
| students who have not yet established `W = fd` | the whole derivation chain starts from it | **medium** — inferred from the practice |
| students outside this tier | the textbook gives **different practices** for each tier, and does not declare this practice transferable across tiers | **weak** — untested |

## Risks

| Where it can go wrong | Why |
|---|---|
| students take a "kilowatt-hour" to be power | this is exactly what this practice is there to block. **A "kilowatt" is power; a "kilowatt-hour" is power times time = energy** |
| saying only "the time cancels out" without "why you are allowed to multiply" | the textbook lands on **power multiplied by time gives energy**. If it is just a unit game, students still do not understand why the bill is calculated by it |
| taking the constant g in `W = mgh` for granted | the textbook's `[AL]` **specifically** wants this implicit assumption exposed. Skip it and students apply the wrong formula when they meet a non-constant force |

## Evidence

| ID | Type | Grade | Locator | Licence |
|---|---|---|---|---|
| ev-036 | textbook (full text) | low | OpenStax《Physics》 Chapter 9, [m54271](https://github.com/openstax/osbooks-physics/blob/main/modules/m54271/index.cnxml) | **CC BY 4.0** |

## Argument

### M1 · Designated by the textbook for the AL tier (no attack yet)

- **Claim**: this is the practice the textbook designates for advanced students
- **Premise**: the Teacher Support of m54271 marks each of the items above `[AL]` (ev-036)
- **Reasoning**: the tier marker is the textbook's designation for that level
- **Evidence**: ev-036
- **Attacked**: **"textbook-designated" ≠ "measured to be effective"**; and unit derivation is a **mechanical operation of low cognitive load** — labelling it AL **does not fully match the meaning of "advanced"** — I keep this attack below
- **Attribution**: @hpleapfrog · 2026-10-05

> [!NOTE]
> **The words in the "Attacked" line above are meant seriously, not as boilerplate.**
>
> Unit derivation is in essence **symbol manipulation**; it does not require greater abstract ability.
> The textbook putting it under `[AL]` is more likely explained by **lesson scheduling**
> (basic students do not study it yet) than by **cognitive load**.
>
> **This is exactly why a tier marker cannot be read directly as evidence of a "difficulty level" —**
> it is an **authoring suggestion**, and its motive may be more than one. This entry does not write it
> as "the AL tier is harder".

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 3) | Issue #8 | @hpleapfrog |
