---
id: kb:physics:velocity-time-graph-area
type: 命题
title: Area under a velocity–time graph equals displacement
status: 待审
author: "@hpleapfrog"
created: 2026-10-20
updated: 2026-10-20
scope:
  学科: 物理
  学段: 高中
  适用: Students using a velocity–time graph to find displacement in one-dimensional motion
  条件: One-dimensional motion; velocity does not change sign; the area is taken between the line and the time axis. This entry only reports the formulation and use in §2.4 of the textbook
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-151]
license: CC-BY-SA-4.0
---

> **English version of [`速度—时间图的面积等于位移.md`](速度—时间图的面积等于位移.md).**

## Statement

In a one-dimensional **velocity–time graph**, the area between the line and the time axis represents the **displacement** over that time interval:

| Graph | Area rule | Displacement |
|---|---|---|
| Horizontal line (constant velocity) | `v · Δt` | `Δx = v Δt` |
| Straight line (constant acceleration) | trapezoid `(v₀ + v)/2 · Δt` | `Δx = v₀Δt + ½aΔt²` |
| Arbitrary curve (velocity does not change sign) | area under the curve (integral or counting squares) | displacement over the interval |

The last two rows are direct applications of the area relation; the textbook itself states only the area–displacement correspondence.

> The area under a velocity curve represents the displacement.
>
> The displacement is given by finding the area under the line in the velocity vs. time graph.
>
> — OpenStax *Physics*, §2.4 *Velocity vs. Time Graphs*

**Boundary**: this covers only motion whose velocity does not change sign. When velocity changes sign, area below the time axis must be treated as signed area; the textbook section does not develop this, and this entry does not add it.

## Basis

| Number | Type | Grade | Locator | License |
|---|---|---|---|---|
| ev-151 | textbook | low | OpenStax *Physics*, §2.4 Velocity vs. Time Graphs, [page](https://openstax.org/books/physics/pages/2-4-velocity-vs-time-graphs) | CC BY-NC-SA 4.0 · locators and short quotes only |

The grade "low" does not mean the text is unreliable; it means a **textbook statement is not independent evidence**. This entry only reports the textbook's formulation and worked-example use, both directly checkable in the source.

## Argument

### A1 · Textbook statement (no attack yet)

- **Claim**: OpenStax *Physics* §2.4 states that the area between a velocity–time line and the time axis is the displacement, and its worked example finds displacement by "the area under the line"
- **Premise**: the section says "The area under a velocity curve represents the displacement." and its example strategy says "The displacement is given by finding the area under the line in the velocity vs. time graph." (ev-151)
- **Reasoning**: this is a direct report of the textbook text; the claim is limited to that section's formulation and use, and does not assert a sign rule for reversing velocity
- **Evidence**: ev-151
- **Attacked**: no attack yet
- **Signed**: @hpleapfrog · 2026-10-20

## Why it is worth recording

Two readings on a velocity–time graph are commonly confused:

- **slope** → acceleration
- **area** → displacement

A student can memorize the formulas correctly and still misread the graph systematically when the two are swapped. This entry fixes the area–displacement correspondence on its own.

## Change log

| Date | Operation | Basis | Who |
|---|---|---|---|
| 2026-10-20 | Entry created | ev-151 registered; topic chosen within the subject boundary | @hpleapfrog |
