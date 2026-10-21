---
id: kb:physics:path-momentum
type: 路径
title: "Momentum and collisions (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: compute impulse with the momentum theorem, decide when momentum is conserved, and solve a collision with conservation plus energy
  条件: students know Newton's second law and conservation of mechanical energy
outcomes:
  - o1: state momentum and impulse, and use the momentum theorem to link force × time to change in velocity
  - o2: decide when a system's momentum is conserved (zero net external force / internal force dominates)
  - o3: tell elastic from inelastic collisions, and solve one collision with momentum conservation plus energy
  - o4: state the criterion that a perfectly inelastic collision loses the most mechanical energy
edges:
  先修:
    - "[Newton's second law](../concepts/newtons-second-law.en.md)"
    - "[mechanical energy](../concepts/conservation-of-mechanical-energy.en.md)"
  支持: []
  攻击: []
evidence: [ev-045, ev-046, ev-047]
license: CC-BY-SA-4.0
---

> **English version of [`动量与碰撞-高中.md`](动量与碰撞-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Momentum and impulse: force accumulating over time | [momentum and impulse](../concepts/momentum-impulse.en.md) | o1 |
| 2 | Conservation of momentum: when momentum alone suffices | [conservation of momentum](../concepts/conservation-of-momentum.en.md) | o2 |
| 3 | Collisions: conservation plus energy | [elastic and inelastic collisions](../concepts/elastic-inelastic-collisions.en.md) | o3, o4 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> Two external prerequisites: Newton's 2nd (where the theorem comes from) and mechanical energy
> (the criterion for classifying collisions).

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `momentum & impulse` (Newton's 2nd) → `conservation` (momentum & impulse) →
  `collisions` (conservation · mechanical energy). Both external prerequisites declared.
- **Outcome coverage**: `o1`–`o4` covered, **4/4** (step 3 covers o3 and o4).

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · Build the quantity, then the condition, then combine

- **Claim**: "momentum & impulse → conservation → collisions" achieves o1–o4
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-045 · ev-046 · ev-047
- **Reasoning**: the momentum theorem is where the concept comes from, so it comes first; conservation
  answers "when can I stop computing forces"; collisions are the only place where conservation and
  energy are combined, so they come last
- **Evidence**: ev-045 · ev-046 · ev-047
- **Attacked**:
  - **Here the order is fully forced by the prerequisite edges** — which also means this path
    **cannot be reordered to fit different students**
  - **No methods, durations or diagnostic step**
  - **"If momentum is conserved, ignore energy" is the classic misuse**, and the library has no entry for it
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: three methods; a misconception entry on momentum vs mechanical energy

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from three concepts' `先修` edges; content from ev-045/046/047 | @hpleapfrog |
