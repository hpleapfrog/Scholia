---
id: kb:physics:path-magnetism-and-induction
type: 路径
title: "Magnetism and electromagnetic induction (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: from "a magnetic field exerts forces on currents and moving charges" to "a changing flux generates current", and decide the direction of the induced current
  条件: students know field strength, resistance and Ohm's law, uniform circular motion
outcomes:
  - o1: describe a magnetic field with flux density, and say why field lines close on themselves unlike electric field lines
  - o2: find the direction of the magnetic force on a current and compute `F = BIL`
  - o3: find the direction of the Lorentz force and explain circular motion in a uniform field
  - o4: use `Φ = BS` and "changing flux" to state when induction occurs
  - o5: use Lenz's law to decide the induced current direction, and say exactly what is being opposed
  - o6: tell motional from induced EMF, and explain why self-induction "lags one step"
  - o7: use the Lorentz force to explain the division of labour between a mass spectrometer and a cyclotron: one measures mass, the other accelerates repeatedly
edges:
  先修:
    - "[field strength](../concepts/electric-field.en.md)"
    - "[resistance and Ohm's law](../concepts/resistance-and-ohms-law.en.md)"
    - "[uniform circular motion](../concepts/uniform-circular-motion.en.md)"
  支持: []
  攻击: []
evidence: [ev-160, ev-161, ev-192, ev-193]
license: CC-BY-SA-4.0
---

> **English version of [`磁场与电磁感应-高中.md`](磁场与电磁感应-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Magnetic field: invisible, but computable | [magnetic field](../concepts/magnetic-field.en.md) | o1 |
| 2 | The field's force on a current | [magnetic force on a current](../concepts/ampere-force.en.md) | o2 |
| 3 | The field's force on a moving charge | [Lorentz force](../concepts/lorentz-force.en.md) | o3 |
| 4 | Flux: counting the lines through a surface | [magnetic flux](../concepts/magnetic-flux.en.md) | o4 |
| 5 | Induction: only change makes current | [Faraday's law](../concepts/electromagnetic-induction.en.md) | o4, o5 |
| 6 | Motional vs induced: two kinds of EMF | [eddy currents and motional EMF](../concepts/eddy-currents-and-motional-emf.en.md) | o6 |
| 7 | Self-induction: current cannot jump | [self and mutual inductance](../concepts/self-and-mutual-inductance.en.md) | o6 |
| 8 | Instruments: weighing mass and accelerating repeatedly | [mass spectrometer and cyclotron](../concepts/mass-spectrometer-and-cyclotron.en.md) | o7 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> Three external prerequisites: field strength (the language of fields), resistance and Ohm's law
> (magnitude of the induced current), uniform circular motion (the particle's orbit).

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `magnetic field` (field strength) → `ampere force` / `flux` (magnetic field) →
  `Lorentz force` (magnetic field · circular motion) → `Faraday` (flux · Ohm's law) →
  `eddy & motional` (Faraday · Lorentz) → `self-inductance` (Faraday). Three external prerequisites declared.
- **Outcome coverage**: `o1`–`o7` covered, **7/7** (step 5 covers o4 and o5; steps 6–7 share o6; step 8 covers o7).

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · Force first, then flux, then "change generates current"

- **Claim**: the seven steps achieve o1–o6
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-160 (field, forces) ·
  ev-161 (flux, induction) · ev-193 (motional EMF) · ev-192 (self/mutual inductance)
- **Reasoning**: the first three answer "what does the field push on"; flux turns the field into a
  countable quantity and is the only door into induction; both induction branches need extra concepts
  (Lorentz force, changing current) and so follow the law
- **Evidence**: ev-160 · ev-161 · ev-192 · ev-193
- **Attacked**:
  - **Ampere before Lorentz is my call**: macroscopic "force on a current" before microscopic "force on a
    charge" — measurable first, explanation second. The reverse is equally valid
  - **Seven steps is long**: six outcomes and seven steps make this closer to a chapter than to a lesson
  - **No methods, durations or diagnostic step**
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: seven methods; a misconception entry on "Lenz's law opposes the cause, not the change"

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from seven concepts' `先修` edges; content from ev-160/161/192/193 | @hpleapfrog |
| 2026-10-22 | **One step added**: mass spectrometer and cyclotron (o7); coverage 6/6 → **7/7** — which makes the "eight steps is long" critique sharper | it belonged to no path; its prerequisite (Lorentz force) sits inside this chain | @hpleapfrog |
