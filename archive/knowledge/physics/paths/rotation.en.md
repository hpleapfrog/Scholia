---
id: kb:physics:path-rotation
type: 路径
title: "Rotation (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-22
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: translate rotation into the linear quantities, and use them on a rigid body once
  条件: students know acceleration, uniform circular motion and force analysis
outcomes:
  - o1: state angular displacement, angular velocity and angular acceleration, and convert between angular and linear quantities
  - o2: use `τ = rF sinθ` to judge the magnitude and direction of a torque, and explain why door handles sit far from the hinge
edges:
  先修:
    - "[acceleration](../concepts/acceleration.en.md)"
    - "[uniform circular motion](../concepts/uniform-circular-motion.en.md)"
    - "[force (HS)](../concepts/force.en.md)"
  支持: []
  攻击: []
evidence: [ev-088]
license: CC-BY-SA-4.0
---

> **English version of [`转动-高中.md`](转动-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Rotational kinematics: linear quantities → angular ones | [angular acceleration and rotational kinematics](../concepts/rotational-kinematics.en.md) | o1 |
| 2 | Torque: what actually makes things turn | [torque](../concepts/torque.en.md) | o2 |

> [!WARNING]
> **Two steps, no methods** — the shortest path in the library, and it **covers only the first half
> of rotation**. Moment of inertia, conservation of angular momentum and rigid-body dynamics
> **have no entries yet**.
> As it stands this is closer to "finding a place for two existing concepts" than to a complete chain.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `rotational kinematics` (acceleration · circular motion) → `torque`
  (force · rotational kinematics). Three external prerequisites declared.
- **Outcome coverage**: `o1`–`o2` covered, **2/2**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · Two steps, with the order fully forced

- **Claim**: "rotational kinematics → torque" achieves o1–o2
- **Premise**: prerequisite edges in each concept's front-matter; both concepts rest on ev-088
- **Reasoning**: torque's front-matter requires rotational kinematics, so the order has no freedom
- **Evidence**: ev-088
- **Attacked**:
  - **The path is incomplete**: moment of inertia and conservation of angular momentum are missing, so
    it stops at torque. **I will not dress a two-step path up as complete**
  - **Both concepts share one evidence entry (ev-088)**: same chapter, but that is not two independent supports
  - **No methods, durations or diagnostic step**
- **Attribution**: @hpleapfrog · 2026-10-22
- **To add**: moment of inertia · angular momentum conservation · rigid-body dynamics, plus their methods

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-22 | Entry created | order from two concepts' `先修` edges; content from ev-088 | @hpleapfrog |
