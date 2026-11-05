---
id: kb:physics:path-alternating-current
type: 路径
title: "Alternating current (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: explain how sinusoidal AC is generated, why RMS exists, and why a transformer changes voltage but not power
  条件: students know electromagnetic induction and uniform circular motion
outcomes:
  - o1: explain sinusoidal AC generation from a coil rotating uniformly in a field, and link peak to angular speed
  - o2: state the RMS definition (equivalent heating) and convert between 220 V and the peak
  - o3: say a transformer changes voltage and current but **not** power, and state the ideal assumptions
  - o4: say qualitatively that inductive reactance rises with frequency and capacitive falls, and what that does to AC
  - o5: explain high-voltage transmission as "step up to cut losses", and why the voltage cannot rise forever
edges:
  先修:
    - "[electromagnetic induction](../concepts/electromagnetic-induction.en.md)"
    - "[uniform circular motion](../concepts/uniform-circular-motion.en.md)"
    - "[self and mutual inductance](../concepts/self-and-mutual-inductance.en.md)"
    - "[capacitance](../concepts/capacitance.en.md)"
    - "[resistance and Ohm's law](../concepts/resistance-and-ohms-law.en.md)"
  支持: []
  攻击: []
evidence: [ev-162, ev-194, ev-195]
license: CC-BY-SA-4.0
---

> **English version of [`交变电流-高中.md`](交变电流-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | AC: spin a coil and it appears | [alternating current](../concepts/alternating-current.en.md) | o1 |
| 2 | RMS: why 220 V | [RMS values](../concepts/rms-values.en.md) | o2 |
| 3 | Transformer: voltage changes, power does not | [transformer](../concepts/transformer.en.md) | o3 |
| 4 | Reactance: AC's "resistance" | [reactance and impedance](../concepts/reactance-and-impedance.en.md) | o4 |
| 5 | Power to the home: why high voltage | [long-distance transmission](../concepts/power-transmission.en.md) | o5 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> This path has the **most external prerequisites (4)**: induction and circular motion explain
> "why sinusoidal"; self/mutual inductance and capacitance explain "why reactance".

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `AC` (induction · circular) → `RMS` (AC) → `transformer` (induction · AC) →
  `reactance` (AC · RMS · self/mutual · capacitance). Five external prerequisites declared (resistance for transmission losses).
- **Outcome coverage**: `o1`–`o5` covered, **5/5**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · How it is made → how it is measured → how it is used

- **Claim**: "AC → RMS → transformer → reactance" achieves o1–o4
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-162 (AC/transformer) ·
  ev-194 (RMS) · ev-195 (reactance)
- **Reasoning**: the RMS definition needs the waveform first (step 2); the transformer needs only
  "AC gives a changing flux" (step 3); reactance needs both RMS and two external concepts, so last
- **Evidence**: ev-162 · ev-194 · ev-195
- **Attacked**:
  - **Four external prerequisites is a real cost**: the path cannot open a chapter, only consolidate one
  - **No methods, durations or diagnostic step**
  - **"220 V is RMS (peak 311 V)"** is mentioned once in the library; this path does not carry that detail
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: four methods; a misconception entry on "RMS = average" (very common, currently missing)

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from four concepts' `先修` edges; content from ev-162/194/195 | @hpleapfrog |
| 2026-10-22 | **One step added**: long-distance transmission (o5); coverage 4/4 → **5/5** | it belonged to no path; its prerequisite (transformer) sits inside this chain | @hpleapfrog |
