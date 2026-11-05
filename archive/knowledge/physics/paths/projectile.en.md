---
id: kb:physics:path-projectile
type: 路径
title: "Projectile motion (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-22
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: split a horizontal throw into two straight-line motions, and solve for time and range
  条件: students know speed and velocity (not taught here)
outcomes:
  - o1: state the criterion "if velocity and acceleration are not collinear, the path curves"
  - o2: resolve a horizontal throw into uniform horizontal motion and vertical free fall, and say the two are independent
  - o3: get the flight time from the vertical component, then the range from the horizontal one
edges:
  先修:
    - "[speed and velocity](../concepts/speed-and-velocity.en.md)"
  支持: []
  攻击: []
evidence: [ev-163]
license: CC-BY-SA-4.0
---

> **English version of [`抛体运动-高中.md`](抛体运动-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Acceleration first: when does a path curve | [acceleration](../concepts/acceleration.en.md) | o1 |
| 2 | Horizontal throw: split it into two directions | [projectile motion](../concepts/projectile-motion.en.md) | o2, o3 |

> [!WARNING]
> **Two steps, no methods**, and step 1 is a **review of a concept that lives in another path**
> (`acceleration` belongs to "intro kinematics"). The library has only `projectile motion` on this
> line: **the condition for curved motion and the resolution of motion into components have no entries**,
> so this path stops at horizontal throws.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `acceleration` (speed & velocity) → `projectile motion` (speed & velocity ·
  acceleration). `speed and velocity` is an external prerequisite.
- **Outcome coverage**: `o1`–`o3` covered, **3/3** (step 2 covers o2 and o3).

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · Criterion first, then the split

- **Claim**: the two steps achieve o1–o3
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-163
- **Reasoning**: "why the path curves" is the precondition for projectile motion — without it only
  formulas remain; the split (uniform horizontal + free-fall vertical) is the only main line, so step 2
  covers both o2 and o3
- **Evidence**: ev-163
- **Attacked**:
  - **Step 1 borrows a concept from another path**: it is not an "own" step, so the reader jumps out once
  - **Incomplete**: the condition for curved motion, the resolution into components and oblique throws
    have no entries
  - **No methods, durations or diagnostic step**
- **Attribution**: @hpleapfrog · 2026-10-22
- **To add**: curved-motion condition · resolution of motion · oblique throw, with their methods

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-22 | Entry created: the last concept that belonged to no path | prerequisite "speed & velocity · acceleration"; content from ev-163 | @hpleapfrog |
