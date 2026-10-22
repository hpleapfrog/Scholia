---
id: kb:physics:path-circuits
type: 路径
title: "Intro circuits (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-22
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: handle series/parallel circuits with Ohm's law and power relations, and say what "the source has internal resistance" means
  条件: students have finished electrostatics (charge · potential energy and potential)
outcomes:
  - o1: compute current, voltage or resistance with Ohm's law, and state when it applies
  - o2: tell series from parallel, compute equivalent resistance, and explain current/voltage division
  - o3: compute power and work with `P = UI` and `W = UIt`, and keep J and W apart
  - o4: state Joule's law and when electrical work is **not** equal to heat
  - o5: use the closed-circuit form to explain why terminal voltage drops as current rises
  - o6: use the chain "electrical work → other forms of energy" to explain efficiency, and say what "saving energy" actually saves
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-016, ev-018, ev-165, ev-166, ev-167, ev-178, ev-179]
license: CC-BY-SA-4.0
---

> **English version of [`电路入门-高中.md`](电路入门-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Resistance and Ohm's law | [resistance and Ohm's law](../concepts/resistance-and-ohms-law.en.md) | o1 |
| 2 | Electric power: energy per unit time | [electric power](../concepts/electric-power.en.md) | o3 |
| 3 | Series and parallel: equivalent resistance | [series and parallel](../concepts/series-and-parallel-circuits.en.md) | o2 |
| 4 | Work and Joule's law: where work ≠ heat | [electric work and Joule's law](../concepts/electric-work-and-joule-law.en.md) | o4 |
| 5 | Closed circuit: the source has resistance | [closed-circuit Ohm's law and internal resistance](../concepts/closed-circuit-ohms-law.en.md) | o5 |
| 6 | Where the energy goes: efficiency and sustainability | [energy resources and sustainability](../concepts/energy-resources-and-sustainability.en.md) | o6 |

> [!WARNING]
> **Every step links to a concept; there are no methods.** This is a **concept order**, not a
> teaching plan — unlike [forces and motion](forces-and-motion-hs.en.md), whose steps carry
> textbook-tagged classroom practices.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `resistance & Ohm` (none) → `power` / `series & parallel` (resistance) →
  `work & Joule` (power · resistance) → `closed circuit` (resistance · series · power).
  **All prerequisites sit inside the path; none external.**
- **Outcome coverage**: `o1`–`o6` covered, **6/6**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — the path contains no `method`.

## Argument

### P1 · The order comes from prerequisite edges, with two judgement calls

- **Claim**: the five steps above achieve o1–o5
- **Premise**: prerequisite edges are in each concept's front-matter; content rests on
  ev-016 / ev-018 / ev-165 / ev-166 / ev-167 / ev-178 / ev-179
- **Reasoning**: `power` and `series & parallel` both only require `resistance`, so **their order is
  my choice** — power first (single loop) before series/parallel (multiple loops); `work & Joule`
  needs power, so it follows; `closed circuit` needs series/parallel, so it comes last
- **Evidence**: ev-016 · ev-018 · ev-165 · ev-166 · ev-167 · ev-178 · ev-179
- **Attacked**:
  - **Steps 2 and 3 could be swapped** — the graph does not constrain them
  - **No methods, no durations, no pre/post tests**: none of the five concepts has a method entry
  - **No diagnostic step**: the library has no circuit misconceptions yet
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: five methods; misconception entries on voltage/current division

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created | order from the five concepts' `先修` edges; content from ev-016/018/165/166/167/178/179 | @hpleapfrog |
| 2026-10-22 | **One step added**: energy resources and sustainability (o6); coverage 5/5 → **6/6** | it belonged to no path; its prerequisite sits inside this chain | @hpleapfrog |
