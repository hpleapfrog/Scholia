---
id: kb:physics:path-energy-work
type: 路径
title: "Work, power and mechanical energy (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  水平档: 不分档
  目标: decide whether a force does work, and handle a fall or a throw with conservation of mechanical energy
  条件: students have finished Newton's laws (vector addition, free-body analysis)
outcomes:
  - o1: decide whether a given force **does work** in a concrete situation (perpendicular force → no work)
  - o2: state the unit relation between work and power, and the conditions for `W = Fs` and `P = W/t`
  - o3: compute the speed in a fall or throw with conservation of mechanical energy
  - o4: say that with friction mechanical energy is **not** conserved, and where the energy went
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-036, ev-028]
license: CC-BY-SA-4.0
---

> **English version of [`功功率与机械能-高中.md`](功功率与机械能-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | "Does this force count as doing work?" | [work & power · OL: what counts](../methods/work-ol-what-counts.en.md) | o1 |
| 2 | How the units fit together (J and W) | [work & power · AL: unit relations](../methods/work-al-unit-relations.en.md) | o2 |
| 3 | Conservation of mechanical energy: first say what is conserved | [mechanical energy · BL: unit distinction](../methods/mech-energy-bl-units.en.md) | o3 |
| 4 | **Boundary**: friction — where did the energy go? | [mechanical energy · OL: friction and heat](../methods/mech-energy-ol-friction-heat.en.md) | o4 |

> [!NOTE]
> **Step 1 is the foundation of the whole path.** "You carry a box horizontally — do you do work on
> it?" Get that wrong and every energy calculation afterwards is wrong at the first step — and what
> it tests is not a formula but **the direction relation between displacement and force**.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: neither `work & power` nor `mechanical energy` declares a prerequisite,
  so the path needs **no external prerequisite**.
- **Outcome coverage**: `o1`–`o4` covered, **4/4**.

### Human judgement

- **Contraindication conflicts**: the four methods come from BL / OL / AL; each marks only
  "outside this level (weak)". The path is declared 「不分档」, so **by definition nothing conflicts**
  — which also means this path **has no profile**, and the check is nearly empty for it (see below).

## Argument

### P1 · "Judge first, compute second, then set the boundary"

- **Claim**: establishing "does this force do work" before the unit and conservation computation, and
  breaking conservation with friction last, achieves o1–o4
- **Premise**: the four steps are `[OL]` / `[AL]` / `[BL]` / `[OL]`-tagged textbook passages
  (ev-036 / ev-028); the two concepts have no prerequisite edges, so the order is not constrained by
  the graph
- **Reasoning**: conservation can only be used after knowing which forces do work (step 1); units
  come before computing (step 2); step 4 deliberately breaks conservation because students often read
  "conserved" as "always conserved"
- **Evidence**: ev-036 · ev-028
- **Attacked**:
  - **The order is entirely my judgement.** Neither concept has a prerequisite edge and the textbook
    never sequences them — **with no graph to lean on, this path has the weakest justification**
  - **"Any level" is a dodge.** The four steps span BL/OL/AL; stringing them into one path leaves me
    no profile to declare, so I wrote 「不分档」 — which removes the object of the contraindication check
  - **No durations, no pre/post tests**
- **Attribution**: @hpleapfrog · 2026-10-18
- **To add**: split this into a BL and an OL version (it currently mixes them); classroom data

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; absorbs the hand-written "energy" order from START.md | methods from four textbook passages across BL/OL/AL, hence 「不分档」 | @hpleapfrog |
