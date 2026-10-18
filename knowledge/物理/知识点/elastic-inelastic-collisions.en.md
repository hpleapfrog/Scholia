---
id: kb:physics:kp-elastic-inelastic-collisions
type: 知识点
title: "Elastic and inelastic collisions"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-05
scope:
  学科: 物理
  学段: 高中
  范围: conservation of momentum
edges:
  先修: ["[知识点：动量守恒定律](conservation-of-momentum.en.md)", "[知识点：机械能守恒](conservation-of-mechanical-energy.en.md)"]
  支持: []
  攻击: []
evidence: [ev-047]
license: CC-BY-SA-4.0
---

> **English version of [`弹性碰撞与非弹性碰撞.md`](弹性碰撞与非弹性碰撞.md).**

> [!TIP]
> **After reading this entry you should** be able to judge whether a collision is elastic or inelastic,
> and to explain clearly that "conservation of momentum" and "conservation of kinetic energy" are **not the same thing** in collisions.

## Definition

| | momentum `p = mv` | kinetic energy `E_k = ½mv²` |
|---|---|---|
| **elastic collision** `elastic` | **conserved** | **conserved** |
| **inelastic collision** `inelastic` | **conserved** | **decreases** |
| **perfectly inelastic collision** `perfectly inelastic` | **conserved** | decreases the most (**the bodies stick together after colliding**) |

> [!IMPORTANT]
> **The point of this entry is not the definitions but the difference between these two quantities:**
>
> **Momentum is conserved in both kinds of collision; kinetic energy is conserved only in elastic collisions.**
>
> Why does it hold "in both kinds of collision" while kinetic energy does not? Go back to the conditions on both sides (see
> [conservation of momentum](conservation-of-momentum.en.md) and [conservation of mechanical energy](conservation-of-mechanical-energy.en.md)):
>
> - **momentum**: conserved as long as the system is free of external forces — at the **instant** of collision, the impulse of external forces is far smaller than the impulse of internal forces, so it holds approximately
> - **kinetic energy**: if there is **deformation, heating, or sound** in the collision, non-conservative forces do work and **mechanical energy is no longer conserved**
>
> **The word "inelastic" refers precisely to "energy got away", not to "momentum is no longer conserved".**

> [!NOTE]
> **The textbook's `[OL]` hint starts from here (ev-047):**
>
> > `Review the concept of internal energy.`
> > `Ask students what they understand by the words elastic and inelastic.`
>
> **Note the order**: first review **internal energy**, then ask students what they understand by "elastic".
>
> **Everyday "elastic"** means "can it bounce back" (like a spring or a rubber band);
> **"elastic collision" in physics** means "**whether kinetic energy is lost**" —
> two steel balls colliding can be elastic, while a piece of plasticine hitting a wall is **the least elastic**.
> **Everyday language misleads here**, so the textbook asks first, then corrects.

## Relations

| Object | Entry | Note |
|---|---|---|
| prerequisite · knowledge point | [conservation of momentum](conservation-of-momentum.en.md) | the one that holds in both kinds of collision |
| prerequisite · knowledge point | [conservation of mechanical energy](conservation-of-mechanical-energy.en.md) | the one that holds only in elastic collisions |
| related · knowledge point | [conservation of mechanical energy](conservation-of-mechanical-energy.en.md) | its "friction generates heat" section is exactly where the energy goes in an inelastic collision |

> [!TIP]
> **This entry is the terminus of this repo's "force × time" main line, and also where the two conservation lines meet.**
>
> ```
> force × displacement → work → conservation of mechanical energy ─┐
>                                                                   ├→ collision: momentum is always conserved, kinetic energy depends
> force × time → impulse → conservation of momentum ─┘
> ```
>
> **The reason "collision" is a classic problem is that it falls on both lines at once.**

## Argument

### K24 · Why listed separately (no attack yet)

- **Claim**: elastic/inelastic collisions deserve to be a separate knowledge point
- **Premise**: the textbook devotes a section to it, containing **4 teaching hints** (2 of them tiered) and **9 terms** (ev-047)
- **Reasoning**:
  1. it introduces **a matched pair of terms** (`elastic` / `inelastic`) plus one extreme case (`perfectly inelastic`); this terminology is used repeatedly beyond this chapter (molecular collisions, scattering)
  2. it is **the intersection of the two conservation lines** — its `先修` points to both the momentum line and the mechanical-energy line
  3. the textbook chooses to start from **students' everyday understanding** and correct it, showing it expects this to be a point **where misconceptions occur**
- **Evidence**: ev-047
- **Attacked**: **it is the entry with the least tiered content in this repo (211 characters, 4 hints)**; the textbook puts most of its content into **worked examples and calculations**, and this repo does not treat worked examples as sources
- **Response**: **this is the weakest part of the entry, recorded honestly.** The `Definition` section here **uses only the terminology the textbook gives and that one `[OL]` hint**, and **adds no calculation examples on the textbook's behalf**. **Whether a node deserves to exist is judged by the relations it carries** — this entry's `先修` connects to both conservation lines at once, and **no other node in the graph can occupy that position**.
- **Attribution**: @hpleapfrog · 2026-10-05
- **To be added**: worked collision-calculation examples (no source in this repo); **angular momentum** (not built)

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 7) | Issue #8 | @hpleapfrog |
