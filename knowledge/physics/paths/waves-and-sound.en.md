---
id: kb:physics:path-waves-and-sound
type: 路径
title: "Waves and sound (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: handle sound and electromagnetic waves with the wavelength–frequency–speed relation, and say "a wave carries energy, not matter"
  条件: none — this is the library's entry point into waves
outcomes:
  - o1: state `v = λf` and that wave speed is set by the medium
  - o2: use "the medium sets the speed" to explain how sound speed depends on medium and temperature
  - o3: order the electromagnetic spectrum by frequency, and say why visible light is a narrow slice
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-033, ev-034, ev-027, ev-030]
license: CC-BY-SA-4.0
---

> **English version of [`波与声-高中.md`](波与声-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Waves: energy travels, matter does not | [waves](../concepts/waves.en.md) | o1 |
| 2 | Speed of sound: why you see lightning before thunder | [speed of sound and frequency](../concepts/speed-of-sound.en.md) | o2 |
| 3 | The spectrum: visible light is a narrow slice | [electromagnetic spectrum](../concepts/electromagnetic-spectrum.en.md) | o3 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> This path has **no external prerequisite**: `waves` is where the library's wave material starts
> (the optics and quantum paths both declare it as an external prerequisite).

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `waves` (none) → `speed of sound` (waves) → `spectrum` (waves).
  **No gap, no external prerequisite.**
- **Outcome coverage**: `o1`–`o3` covered, **3/3**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · Build the wave quantities, then split into sound and electromagnetic waves

- **Claim**: "waves → speed of sound → spectrum" achieves o1–o3
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-033 / ev-034 (waves) ·
  ev-027 (sound) · ev-030 (spectrum)
- **Reasoning**: `waves` has no prerequisite and is the common premise, so it comes first; sound and the
  spectrum are mutually independent, and **their order is my choice** — sound first (lightning and thunder
  are everyday experience), then the spectrum, which introduces ordering across many orders of magnitude
- **Evidence**: ev-033 · ev-034 · ev-027 · ev-030
- **Attacked**:
  - **Steps 2 and 3 could be swapped** — the graph does not constrain them
  - **Three steps cover only the outer layer of wave physics**: interference, diffraction and Doppler
    live in their own entries, and this path **does not promise** them
  - **No methods, durations or diagnostic step**
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: three methods; binding the existing misconception entry "the wave pushes matter along"
  to this path

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from three concepts' `先修` edges; content from ev-033/034/027/030 | @hpleapfrog |
