---
id: kb:physics:kp-electric-field
type: 知识点
title: "Electric field"
status: 待审
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  适用: students who have done Coulomb's law and are meeting the concept of a "field"
  条件: covers the definition of the field, the field of a point charge, and field lines; potential and potential energy are separate entries
edges:
  先修: ["[Coulomb's law](coulombs-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-086]
license: CC-BY-SA-4.0
---

> **English version of [`电场强度.md`](电场强度.md).**

> [!TIP]
> **After reading this entry you should** be able to state that "electric field = force per unit charge", draw the simplest field-line map, and see why a neutral object can only be attracted, never repelled

## Definition

The **electric field**, proposed by Faraday, is a distribution of "**force per unit charge**" that a charge creates in the space around it:

```
E = F / q_test
```

- a **test charge** `q_test` is **positive** and **small enough** not to disturb the charge distribution it is probing
- `E` is a **vector field**: its direction is the force direction on a **positive** test charge; unit `N/C`
- the field is produced by the source charge and is **independent of the test charge** — remove the test charge and the field still exists

For a **point charge** `Q` (or a uniformly charged sphere seen from outside), the magnitude is:

```
E = k |Q| / r²      (r from the source to the point of interest)
```

Joining the arrows at every point gives the **field lines**: they start at **positive** charges (pointing outward) and end at **negative** charges (pointing inward); denser lines mean a stronger field; and **field lines never cross**. The fields of several charges **add as vectors** — the textbook's superposition.

> [!IMPORTANT]
> **A neutral object can be attracted, but never repelled.**
>
> Coulomb's law only talks about charged objects — so why can a comb pick up **uncharged** paper bits?
> Because the paper is **polarized**: charge shifts to the far side, so the near side is opposite and the far side is like,
> attraction beats repulsion, and the net effect is **attraction**.
>
> The textbook closes with a science-fiction multiple choice: a villain tries to push a **neutral** hero away with a radial electric field — this is impossible,
> because `an electrically neutral body can be attracted but not repelled` (ev-086).

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Coulomb's law](coulombs-law.en.md) — `E = k|Q|/r²` follows from Coulomb's law plus the definition of the field |
| Follow-up | [Electric potential energy and electric potential](electric-potential-energy.en.md) — from "force per unit charge" to "energy per unit charge" |
| Recorded gap | **"Preventing and using static electricity" (shielding etc.)** is not built yet |

## Argument

### K1 · Why the field is defined separately (no attack yet)

- **Claim**: the electric field strips "force" off the test charge and leaves a quantity belonging to space itself
- **Premise**: the textbook defines `E = F / q_test` and states `If the test charge is removed from the electric field, the electric field still exists` (ev-086)
- **Reasoning**:
  1. the Coulomb force changes with the test charge (`F = qE`), while `E` does not — this is exactly what "independent of the probe" means for a field
  2. the field of a point charge, `E = k|Q|/r²`, contains **no test charge at all** — the step where `q_test` cancels is
     given by the textbook as a formula, but its meaning is not spelled out
- **Evidence**: ev-086
- **Attacked**: **the reading "q_test cancels" is this repo's inference, not a textbook sentence** — the textbook only says the field survives removing the test charge.
- **Attribution**: @hpleapfrog · 2026-10-18

### K2 · The three rules of field lines (no attack yet)

- **Claim**: "from positive to negative, density shows strength, never crossing" all follow from the definition
- **Premise**: the textbook states the three rules and supplies several field maps (ev-086)
- **Reasoning**: the field at a point is a **single vector** (one direction); two lines through the same point would give two directions — "no crossing" is a direct consequence of single-valuedness;
  "from positive to negative" comes from the force direction on a positive test charge
- **Evidence**: ev-086
- **Attacked**: no attacks yet
- **Attribution**: @hpleapfrog · 2026-10-18

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; third node of the electrostatics chapter, connecting the "force" and "energy" threads | written after reading m54428 in full (ev-086) | @hpleapfrog |
