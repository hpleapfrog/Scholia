---
id: kb:physics:path-gravitation
type: 路径
title: "Gravitation and the sky (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: state what each of Kepler's three laws asserts, and make one order-of-magnitude estimate with the law of gravitation
  条件: students already know circular motion and centripetal force (not part of this path)
outcomes:
  - o1: state what each of Kepler's three laws asserts (orbit, area, period)
  - o2: estimate the gravitational force between two bodies with F = GmM/r²
  - o3: explain "two people attract each other — why don't we feel it" via order of magnitude
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-031, ev-037]
license: CC-BY-SA-4.0
---

> **English version of [`万有引力与天体-高中.md`](万有引力与天体-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Where the three laws came from: observation to regularity | [Kepler's laws · OL: historical context](../methods/kepler-ol-historical-context.en.md) | o1 |
| 2 | **Diagnostic**: are G and g the same thing? | [misconception: confusing G and g](../misconceptions/g-vs-g.en.md) | o2 |
| 3 | From "law" to "force": why an inverse-square force is required | [gravitation · OL: history and causation](../methods/gravitation-ol-history.en.md) | o2, o3 |

> [!NOTE]
> **Why step 2 sits in the middle**: step 3's formula contains both `G` and `g`. Separate
> "a universal constant" from "an acceleration at Earth's surface" before writing it down,
> or students will substitute one for the other.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `Kepler's laws` (none) → `law of universal gravitation` (Kepler's laws).
  **No gap.**
- **Outcome coverage**: `o1`–`o3` covered, **3/3**.

### Human judgement

- **Contraindication conflicts**: both methods mark only "outside this level (weak)" →
  **no conflict with the OL profile**, but the **evidence is weak**.

## Argument

### P1 · The order follows the textbook's causal chain (observation → law → force)

- **Claim**: teaching Kepler's laws (phenomena) before the law of gravitation (cause) achieves o1–o3
- **Premise**: the `先修` edge of `law of universal gravitation` is `Kepler's laws`; both methods are
  `[OL]`-tagged textbook passages (ev-031 / ev-037)
- **Reasoning**: the textbook's own route through this chapter is "regularity first, cause second";
  the prerequisite edge agrees, so sorting by it preserves that chain
- **Evidence**: ev-031 · ev-037
- **Attacked**:
  - **o3 (order-of-magnitude explanation) is `[AL]` material in the textbook**, while this path uses
    `[OL]` steps. I listed it as an outcome on the judgement that OL students should manage it —
    **with no direct evidence for that level**
  - **No durations, no pre/post tests**
- **Attribution**: @hpleapfrog · 2026-10-18
- **To add**: whether o3 is realistic at OL needs classroom data

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; absorbs the hand-written "gravitation and the sky" order from START.md | prerequisite edges from two concepts' front-matter; methods from two `[OL]` passages | @hpleapfrog |
