---
id: kb:physics:path-optics
type: 路径
title: "Optics (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: from geometric optics to wave optics — state the total-internal-reflection conditions, and use interference and polarisation to show light is a wave
  条件: students know the basic quantities of waves and refraction
outcomes:
  - o1: state the two conditions for total internal reflection, and use the critical angle to explain optical fibre and "water as a mirror"
  - o2: use double-slit fringe spacing to infer wavelength, and tell interference from diffraction
  - o3: say polarisation shows light is a transverse wave, and give one thing a polariser does
edges:
  先修:
    - "[waves](../concepts/waves.en.md)"
    - "[refraction](../concepts/refraction.en.md)"
  支持: []
  攻击: []
evidence: [ev-171, ev-172, ev-173, ev-174]
license: CC-BY-SA-4.0
---

> **English version of [`光学-高中.md`](光学-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Total internal reflection: light cannot get out | [total internal reflection](../concepts/total-internal-reflection.en.md) | o1 |
| 2 | Interference and diffraction: light is a wave | [interference and diffraction](../concepts/light-interference-and-diffraction.en.md) | o2 |
| 3 | Polarisation: light is a transverse wave | [polarisation of light](../concepts/polarization.en.md) | o3 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> External prerequisites: waves and refraction — both exist in the library but **not in this path**.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `TIR` (refraction) → `interference & diffraction` (waves · refraction) →
  `polarisation` (waves · refraction). Both external prerequisites declared.
- **Outcome coverage**: `o1`–`o3` covered, **3/3**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · Close geometric optics, then two wave-optics steps

- **Claim**: "TIR → interference & diffraction → polarisation" achieves o1–o3
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-171 / ev-172
  (interference & diffraction) · ev-173 (TIR) · ev-174 (polarisation)
- **Reasoning**: TIR needs only refraction, so it closes geometric optics; the other two both need
  waves and are mutually unconstrained — I put interference first because fringe spacing is a
  **measurable quantity**, more concrete than polarisation
- **Evidence**: ev-171 · ev-172 · ev-173 · ev-174
- **Attacked**:
  - **The interference/polarisation order is my judgement**, not the graph's
  - **No methods, durations or diagnostic step**
  - **Wave–particle duality is not here**: it sits on the modern-physics side, and no declared bridge connects the two paths
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: three methods; a misconception entry on "polarisation shows light is longitudinal"

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from three concepts' `先修` edges; content from ev-171/172/173/174 | @hpleapfrog |
