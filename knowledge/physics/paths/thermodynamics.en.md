---
id: kb:physics:path-thermodynamics
type: 路径
title: "Thermodynamics (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-22
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: use the two laws to decide where energy goes, and say why efficiency has a ceiling
  条件: students know work and power, and conservation of mechanical energy
outcomes:
  - o1: use the first law (`ΔU = Q + W`) to separate the work and heat contributions of one process
  - o2: state both formulations of the second law and explain why they are equivalent
  - o3: use the statistical meaning of entropy to explain why isolated systems move to more probable states, and why "entropy = mess" is too crude
  - o4: use the Carnot cycle to show that the efficiency ceiling depends only on the two reservoir temperatures
edges:
  先修:
    - "[work and power](../concepts/work-and-power.en.md)"
    - "[mechanical energy](../concepts/conservation-of-mechanical-energy.en.md)"
  支持: []
  攻击: []
evidence: [ev-156, ev-157, ev-183, ev-184]
license: CC-BY-SA-4.0
---

> **English version of [`热学-高中.md`](热学-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | First law: bookkeeping for energy | [first law of thermodynamics](../concepts/thermodynamic-first-law.en.md) | o1 |
| 2 | Second law: why some processes never run backwards | [second law](../concepts/thermodynamic-second-law.en.md) | o2 |
| 3 | Entropy: turning irreversibility into a number | [statistical entropy](../concepts/statistical-interpretation-of-entropy.en.md) | o3 |
| 4 | Carnot cycle: where the efficiency ceiling comes from | [heat engines and the Carnot cycle](../concepts/heat-engine-and-carnot-cycle.en.md) | o4 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> Two external prerequisites: work and power (the `W` in the first law), mechanical energy
> (a special case of it).

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `first law` (work & power · mechanical energy) → `second law` (first law) →
  `entropy` (second law) → `Carnot` (first · second law). Both external prerequisites declared.
- **Outcome coverage**: `o1`–`o4` covered, **4/4**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · Bookkeeping, then direction, then the ceiling

- **Claim**: the four steps achieve o1–o4
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-156 (first law) ·
  ev-157 (second law) · ev-184 (entropy) · ev-183 (Carnot)
- **Reasoning**: the first law is conservation as bookkeeping and must come first; the second law answers
  "direction" and only makes sense once bookkeeping exists; entropy quantifies the second law, so it
  follows immediately; the Carnot cycle uses both laws, so it comes last
- **Evidence**: ev-156 · ev-157 · ev-183 · ev-184
- **Attacked**:
  - **Statistical entropy is deep for this level**: textbooks treat it as optional; this path makes it
    required — my judgement, on the grounds that without entropy the second law is only memorised
  - **No methods, durations or diagnostic step**
  - **No quantitative efficiency derivation**: the Carnot formula lives in the entry; the path only asks
    for the qualitative statement
- **Attribution**: @hpleapfrog · 2026-10-22
- **To add**: four methods; misconception entries on "entropy is just mess" and "heat cannot flow from
  cold to hot"

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-22 | Entry created | order from four concepts' `先修` edges; content from ev-156/157/183/184 | @hpleapfrog |
