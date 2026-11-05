---
id: kb:physics:path-oscillations
type: 路径
title: "Mechanical oscillations (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: describe a spring oscillator and a pendulum with phase and energy, and say what sets the frequency of a forced oscillation
  条件: students know Newton's second law and free-body analysis
outcomes:
  - o1: state the SHM criterion (restoring force proportional and opposite to displacement) and the form of the equation
  - o2: use phase to say "where in the cycle", and state that period and amplitude are independent
  - o3: explain the kinetic/potential energy exchange and that total mechanical energy is conserved
  - o4: use the pendulum period formula to explain "period independent of mass", and state the small-angle approximation
  - o5: tell free, damped and forced oscillation apart, and state the resonance condition and its risk
edges:
  先修:
    - "[Newton's second law](../concepts/newtons-second-law.en.md)"
    - "[force (HS)](../concepts/force.en.md)"
  支持: []
  攻击: []
evidence: [ev-164, ev-190, ev-191]
license: CC-BY-SA-4.0
---

> **English version of [`机械振动-高中.md`](机械振动-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | SHM: where the restoring force comes from | [simple harmonic motion](../concepts/simple-harmonic-motion.en.md) | o1 |
| 2 | Phase and energy: where in the cycle | [phase and energy of SHM](../concepts/phase-and-energy-of-shm.en.md) | o2, o3 |
| 3 | The pendulum: an oscillator you can time | [simple pendulum](../concepts/simple-pendulum.en.md) | o4 |
| 4 | Damping and forcing: real-world oscillation | [damped and forced oscillation](../concepts/damped-and-forced-oscillation.en.md) | o5 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> This path also declares **two external prerequisites** (Newton's 2nd, force), which it does not teach.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `SHM` (Newton's 2nd) → `phase & energy` (SHM) → `pendulum`
  (SHM · force) → `damping & forcing` (phase & energy). Both external prerequisites are declared.
- **Outcome coverage**: `o1`–`o5` covered, **5/5** (step 2 covers o2 and o3).

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · Phenomenon → energy → concrete oscillator → boundary

- **Claim**: ordering "SHM → phase & energy → pendulum → damping/forcing" achieves o1–o5
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-164 (SHM/pendulum) ·
  ev-190 (phase & energy) · ev-191 (damping/forcing)
- **Reasoning**: prerequisites only force SHM first; steps 3 and 4 are unconstrained, and I put the
  pendulum before forced oscillation because the pendulum is a **concrete oscillator with a computable
  period**, while forced oscillation presupposes the notion of period
- **Evidence**: ev-164 · ev-190 · ev-191
- **Attacked**:
  - **The pendulum/forcing order is my judgement**, not the graph's
  - **Phase is hard at this level**: merging it with energy may pack too much — but splitting has no basis either
  - **No methods, durations or diagnostic step**
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: four methods; misconceptions on "period independent of amplitude" and "resonance is only harmful"

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from four concepts' `先修` edges; content from ev-164/190/191 | @hpleapfrog |
