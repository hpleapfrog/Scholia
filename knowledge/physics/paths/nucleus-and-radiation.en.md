---
id: kb:physics:path-nucleus-and-radiation
type: 路径
title: "Nucleus and radiation (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: explain decay and binding energy, and where nuclear energy and ionising radiation each come from
  条件: students have finished atomic structure (this path does not teach it)
outcomes:
  - o1: state what a nucleus is made of and the short-range nature of the nuclear force, and tell isotopes apart
  - o2: write α / β / γ decay equations and state the statistical meaning of half-life
  - o3: use the mass defect to explain binding energy, and locate the dividing line where light and heavy nuclei both release energy
  - o4: tell fission from fusion and explain why both move toward higher binding energy per nucleon
  - o5: explain how ionising radiation damages tissue, and name the three routes of protection
edges:
  先修:
    - "[atomic structure](../concepts/atomic-structure.en.md)"
  支持: []
  攻击: []
evidence: [ev-158, ev-159, ev-185, ev-186, ev-187, ev-188, ev-189]
license: CC-BY-SA-4.0
---

> **English version of [`原子核与辐射-高中.md`](原子核与辐射-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | What is inside a nucleus, and what holds it | [atomic nucleus](../concepts/atomic-nucleus.en.md) | o1 |
| 2 | Unstable nuclei change by themselves | [radioactive decay](../concepts/radioactive-decay.en.md) | o2 |
| 3 | Why nuclear reactions release energy | [binding energy and mass defect](../concepts/binding-energy-and-mass-defect.en.md) | o3 |
| 4 | Fission and fusion: two roads, one direction | [nuclear fission and fusion](../concepts/nuclear-fission-and-fusion.en.md) | o4 |
| 5 | Radiation and the body: dose, damage, protection | [ionising radiation in medicine](../concepts/ionizing-radiation-in-medicine.en.md) | o5 |

> [!WARNING]
> **Steps link to concepts; no methods.** A concept order, not a teaching plan.
> External prerequisite: atomic structure (taught in "quantum ideas and atoms", not here).

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `nucleus` (atomic structure) → `decay` (nucleus) → `binding energy` (nucleus) →
  `fission/fusion` (binding energy · nucleus) → `ionising radiation` (decay). One external prerequisite declared.
- **Outcome coverage**: `o1`–`o5` covered, **5/5**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — no `method` in the path.

## Argument

### P1 · What it is → how it changes → why it releases energy → what it does to people

- **Claim**: the five steps achieve o1–o5
- **Premise**: prerequisite edges in each concept's front-matter; content from ev-158 / ev-159 (nucleus,
  decay) · ev-185 / ev-186 (binding energy, reactions) · ev-187–189 (ionising radiation)
- **Reasoning**: `nucleus` is the only entry point; `decay` and `binding energy` both require only the
  nucleus, so **their order is mine** — the phenomenon first, the mechanism second; fission/fusion needs
  binding energy; ionising radiation could follow decay directly, but I put it last because it introduces
  dose and biological effect, i.e. application
- **Evidence**: ev-158 · ev-159 · ev-185 · ev-186 · ev-187 · ev-188 · ev-189
- **Attacked**:
  - **Steps 2 and 3 could be swapped** — the graph does not constrain them
  - **No methods, durations or diagnostic step**
  - **"Half-life is statistical" is a frequent misconception** and the library has no entry for it
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: five methods; misconception entries on half-life and on X-ray risk

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from five concepts' `先修` edges; content from ev-158/159/185/186/187/188/189 | @hpleapfrog |
