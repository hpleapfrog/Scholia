---
id: kb:physics:path-quantum-and-atoms
type: 路径
title: "Quantum ideas and atoms (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: from "energy comes in lumps" to "atoms have discrete levels", and why wave–particle duality cannot be avoided
  条件: students know waves and the electromagnetic spectrum
outcomes:
  - o1: state Planck's hypothesis (energy exchanged in quanta of hν) and what problem it solved
  - o2: use the photon picture to explain the three photoelectric regularities (threshold, instantaneity, intensity vs saturation current)
  - o3: state what wave–particle duality means, and why macroscopic objects show no wave behaviour
  - o4: use discrete levels to explain line spectra, and say what Bohr's model did and did not fix
edges:
  先修:
    - "[waves](../concepts/waves.en.md)"
    - "[electromagnetic spectrum](../concepts/electromagnetic-spectrum.en.md)"
  支持: []
  攻击: []
evidence: [ev-168, ev-169, ev-170, ev-035]
license: CC-BY-SA-4.0
---

> **English version of [`量子与原子-高中.md`](量子与原子-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Why energy must come in lumps | [Planck's quantum hypothesis](../concepts/planck-quantum-hypothesis.en.md) | o1 |
| 2 | Photoelectric effect: light knocks like particles | [photoelectric effect](../concepts/photoelectric-effect.en.md) | o2 |
| 3 | Light is both wave and particle | [wave–particle duality](../concepts/wave-particle-duality.en.md) | o3 |
| 4 | Why atoms emit only a few lines | [atomic structure](../concepts/atomic-structure.en.md) | o4 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> External prerequisites: waves and the electromagnetic spectrum — present in the library, absent from this path.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `Planck` (waves · spectrum) → `photoelectric` (Planck) → `duality`
  (photoelectric · waves) → `atomic structure` (Planck). Both external prerequisites declared.
- **Outcome coverage**: `o1`–`o4` covered, **4/4**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · First "quantisation is unavoidable", then "quantise the atom"

- **Claim**: "Planck → photoelectric → duality → atom" achieves o1–o4
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-168 (Planck) ·
  ev-169 (photoelectric) · ev-170 (duality) · ev-035 (atomic structure)
- **Reasoning**: Planck is the only entry with no prerequisite beyond waves/spectrum; the
  photoelectric effect is the hardest experimental evidence and immediately cashes the hypothesis;
  duality summarises the first two; atomic structure needs only `E = hν`, so **its last position is
  my choice** — light's quantum nature before the atom's discrete levels costs one less conceptual U-turn
- **Evidence**: ev-168 · ev-169 · ev-170 · ev-035
- **Attacked**:
  - **Step 4's position is my judgement** — the graph would allow it right after step 1
  - **No methods, durations or diagnostic step**
  - **"What Bohr did not fix" is one sentence in the library**; this path does not expand it
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: four methods; a misconception entry on "the photoelectric effect needs time to build up energy"

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from four concepts' `先修` edges; content from ev-168/169/170/035 | @hpleapfrog |
