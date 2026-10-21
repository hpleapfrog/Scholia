---
id: kb:physics:path-electrostatics
type: 路径
title: "Intro electrostatics (high school)"
status: 有效
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  水平档: 年级水平（OL）
  目标: from "charges exert forces" to "an electric field stores energy", and to tell potential energy apart from potential
  条件: students already know conservation of mechanical energy (this path borrows its analogy)
outcomes:
  - o1: use **conservation and transfer of charge** to explain charging by friction and by induction, and say what charge quantisation means
  - o2: estimate the force between two point charges with Coulomb's law, and state its inverse-square and point-charge premises
  - o3: say that **field strength is the force per unit charge**, and explain why the field does not depend on a test charge
  - o4: use the gravitational-potenial analogy to distinguish **electric potential energy** from **electric potential**
  - o5: say that a capacitor stores charge and energy, and that its value is set by geometry and dielectric
edges:
  先修:
    - "[mechanical energy](../concepts/conservation-of-mechanical-energy.en.md)"
  支持: []
  攻击: []
evidence: [ev-083, ev-084, ev-085, ev-086, ev-087, ev-175]
license: CC-BY-SA-4.0
---

> **English version of [`静电学入门-高中.md`](静电学入门-高中.md).**

## Sequence

| # | Step | Entry | Covers |
|---|---|---|---|
| 1 | Charge: two kinds, transferable, conserved | [charge](../concepts/electric-charge.en.md) | o1 |
| 2 | The force between charges: Coulomb's law | [Coulomb's law](../concepts/coulombs-law.en.md) | o2 |
| 3 | The "medium" of the force: field and field strength | [electric field strength](../concepts/electric-field.en.md) | o3 |
| 4 | Energy in the field: potential energy and potential | [electric potential energy and potential](../concepts/electric-potential-energy.en.md) | o4 |
| 5 | Storing charge and energy: capacitance | [capacitance](../concepts/capacitance.en.md) | o5 |

> [!WARNING]
> **Every step here links straight to a `concept` — this chain has no methods at all.**
>
> The other three physics paths attach a `method` to each step (a `[BL]` / `[OL]` / `[AL]`
> textbook classroom practice). This chain is newly added and **nobody has distilled methods for it**.
> So it is a **concept order**, not a **teaching plan** — anyone planning a lesson from it must invent
> the "how". That difference has to be said out loud, not left to look like the other paths.

## Self-check

### Machine-checked (`tools/kbcheck.py`)

- **Prerequisite gaps**: `charge` (none) → `Coulomb's law` (charge) → `field strength` (Coulomb) →
  `potential energy / potential` (field strength · **mechanical energy**) → `capacitance`
  (potential energy · field strength). `mechanical energy` is outside this path and is declared above
  in `edges.先修` as an **external prerequisite**.
- **Outcome coverage**: `o1`–`o5` covered, **5/5**.

### Human judgement

- **Contraindication conflicts**: **not applicable** — the path contains no `method`, so there is no
  "who this is not for" to check. This is not "no conflict"; it is **no object to check**.

## Argument

### P1 · The order comes from `先修` edges, not from my teaching judgement

- **Claim**: ordering "charge → Coulomb's law → field strength → potential energy → capacitance"
  achieves o1–o5
- **Premise**: the five prerequisite edges are declared in each concept's front-matter and the path
  order matches them exactly; per-concept content rests on ev-083/084 (charge) · ev-085 (Coulomb) ·
  ev-086 (field strength) · ev-087 (potential) · ev-175 (capacitance)
- **Reasoning**: prerequisite edges encode "what must come first"; each step's outcome is the
  concept's own defining target; the potential-energy step is the only cross-chain dependency,
  hence the declared external prerequisite
- **Evidence**: ev-083 · ev-084 · ev-085 · ev-086 · ev-087 · ev-175
- **Attacked**:
  - **No methods means no classroom practice.** This path answers "what to teach first", **not
    "how to teach it"** — unlike [forces and motion](forces-and-motion-hs.en.md), where every step
    carries a textbook-tagged practice
  - **A valid order is not effective teaching**
  - **No durations, no pre/post tests, no diagnostic step** — the other paths insert one step that
    breaks a known misconception; this one cannot, because **the library has no electrostatics
    misconception entries yet** (a gap, not an omission by choice)
- **Attribution**: @hpleapfrog · 2026-10-21
- **To add**: one method per concept; electrostatics misconceptions (e.g. "a field needs a test charge to exist")

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created: the electrostatic chain of the 37 new concepts, as one path | order from the five concepts' `先修` edges; content from ev-083–087 and ev-175 | @hpleapfrog |
