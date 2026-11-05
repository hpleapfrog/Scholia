---
id: kb:physics:path-forces-and-motion-hs
type: 路径
title: "Forces and motion (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: explain how force changes motion with Newton's three laws, and point out that an action–reaction pair acts on two different bodies
  条件: students can already describe position, velocity and acceleration (not part of this path; see "Intro kinematics")
outcomes:
  - o1: state that force is an **interaction between bodies**, not "the cause that maintains motion"
  - o2: use inertia to explain "with no force, a body keeps moving in a straight line at constant speed"
  - o3: make a quantitative estimate with F = ma in one concrete situation
  - o4: identify an action–reaction pair and say the two forces **act on two different bodies**
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-041, ev-025, ev-040, ev-042]
license: CC-BY-SA-4.0
---

> **English version of [`力与运动-高中.md`](力与运动-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | What a force is: pushes, pulls, and "single-body dynamics" | [force · OL: push/pull and single-body dynamics](../methods/force-ol-push-pull.en.md) | o1 |
| 2 | **Diagnostic**: do moving objects "naturally slow down"? | [misconception: moving objects naturally slow down](../misconceptions/objects-slow-naturally.en.md) | o1, o2 |
| 3 | Inertia: what happens when no force acts | [inertia · BL: definition](../methods/inertia-bl-definition.en.md) | o2 |
| 4 | How force relates to acceleration | [Newton's 2nd · OL: back to inertia and net force](../methods/newton2-ol-first-law.en.md) | o3 |
| 5 | One pair of forces, on two different bodies | [Newton's 3rd · OL: the support force when landing](../methods/newton3-ol-normal-force.en.md) | o4 |

> [!NOTE]
> **Step 2 is not optional.** After step 1 makes "force is an interaction" explicit, the belief most
> likely to survive is "no force means motion stops". Leave it standing and steps 3–4 are built on sand.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `force (HS)` (none) → `inertia` (force) → `Newton's 2nd` (inertia) →
  `Newton's 3rd` (Newton's 2nd). **All prerequisites sit inside the path — no gap.**
- **Outcome coverage**: `o1`–`o4` covered, **4/4**.

### Human judgement

- **Contraindication conflicts**: all three methods mark only "students outside this level (weak)"
  as contraindicated, which **does not match the OL profile** → no conflict. But the **evidence is
  weak**: it only says the textbook gave each level a different method.

## Argument

### P1 · The order comes from `先修` edges, not from a textbook teaching order

- **Claim**: ordering "force → inertia → Newton's 2nd → Newton's 3rd" achieves o1–o4
- **Premise**: the four prerequisite edges are declared in each concept's front-matter; the path's
  order matches them exactly; each step's method is a `[OL]` / `[BL]`-tagged textbook passage
  (ev-041 / ev-025 / ev-040 / ev-042)
- **Reasoning**: prerequisite edges encode "what must come first", so sorting nodes by them yields a
  valid teaching order; step 2's diagnostic precedes step 3 because it breaks the very belief
  inertia has to establish
- **Evidence**: ev-041 · ev-025 · ev-040 · ev-042
- **Attacked**:
  - **The textbook supplies parts, not an order.** Each method has a source; the ordering **is my
    own reading of the prerequisite graph** — the textbook never sequences anything for OL
  - **No durations, no pre/post tests.** This path gives no minutes because the textbook gives
    none — inventing a number would be fabrication
  - **"Valid order" ≠ "effective teaching"**
- **Attribution**: @hpleapfrog · 2026-10-18
- **To add**: classroom data; structured `禁忌` fields

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; absorbs the hand-written "force and Newton's laws" order from START.md | prerequisite edges from four concepts' front-matter; methods from four `[OL]`/`[BL]` textbook passages | @hpleapfrog |
