---
id: kb:physics:kp-electric-potential-energy
type: 知识点
title: "Electric potential energy and electric potential"
status: 待审
author: "@hpleapfrog"
created: 2026-10-18
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  适用: students who can keep electric field strength and potential energy apart, and have done conservation of mechanical energy (the idea of potential energy)
  条件: introduced by analogy with gravitational potential energy; no capacitors or charged particles in fields (separate entries)
edges:
  先修: ["[Electric field](electric-field.en.md)", "[Conservation of mechanical energy](conservation-of-mechanical-energy.en.md)"]
  支持: []
  攻击: []
evidence: [ev-087]
license: CC-BY-SA-4.0
---

> **English version of [`电势能与电势.md`](电势能与电势.md).**

> [!TIP]
> **After reading this entry you should** be able to tell "electric potential energy" and "electric potential" apart, and compute with `U_E = k q₁q₂ / r` and `V = U_E / q`

## Definition

**Electric potential energy** `U_E`: the work a charge can do **by virtue of its position in an electric field** — the same logic as gravitational potential energy.

```
U_E = k q₁ q₂ / r      (two point charges a distance r apart)
```

- as with gravitational potential energy, **only differences are fully meaningful**: pick a reference (often infinity) and compare every other position with it
- opposite charges attract ⇒ `U_E` is **negative**, and more negative the closer they are — the minus sign is not "energy vanishing", it is a bookkeeping convention

**Electric potential** `V` factors out "per unit charge":

```
V = U_E / q          (unit J/C, called the "volt" V)
V = k q / r          (around a point charge)
```

- potentials of several charges **add directly** (scalars — one vector step fewer than fields)
- the potential difference between two points is the **voltage** `ΔV`; in a uniform field `ΔV = −E (x_f − x_i)`, and inversely `E = ΔV / Δx` (unit `V/m`)
- **positive** charges move from high to low potential; **negative** charges the other way

> [!IMPORTANT]
> **"Electric potential energy" and "electric potential" are not two names for the same thing.**
>
> The textbook tells teachers explicitly: `Emphasize the difference between electric potential energy and electric potential.
> Although the latter seems to be shorthand for the former, the two terms have different meanings.`
>
> | | what it is | unit |
> |---|---|---|
> | potential energy `U_E` | energy the charge **actually has** (scales with the charge) | J |
> | potential `V` | energy **per unit charge** (what remains when the probe charge is divided out) | J/C = V |
>
> This is a repeat of the "force → electric field" cut: **divide the probe object out, and the remainder belongs to space.**

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electric field](electric-field.en.md) — potential is defined in imitation of `E = F / q`, the same "divide by the probe charge" strategy |
| Prerequisite | [Conservation of mechanical energy](conservation-of-mechanical-energy.en.md) — "potential energy matters only as a difference" is carried over from gravitational potential energy |
| Recorded gap | **Capacitance** (PEP B3 §10.4) and **charged particles in electric fields** (§10.5) are not built yet |

## Argument

### K1 · Why potential energy and potential share one entry (no attack yet)

- **Claim**: the two are in one entry not to save files, but because the textbook and the classroom teach them together
- **Premise**: in the **same section** the textbook first defines potential energy, then defines potential by the same strategy, in the words
  `The same Strategy is used here with electric potential energy: We now define the electric potential V, which is the electric potential energy per unit charge.` (ev-087)
- **Reasoning**: they form a "total → per unit" pair; splitting them would leave the key distinction "the roles of `E` and `V`" without a home
- **Evidence**: ev-087
- **Attacked**: **"potential difference" and "the relation between potential and field strength" are subsections of the same textbook section** — this node does not build separate nodes for them.
  That is a trade-off, not complete coverage. If later teaching methods need a finer cut, revisit this.
- **Attribution**: @hpleapfrog · 2026-10-18

### K2 · Why there are two prerequisites (no attack yet)

- **Claim**: potential energy presupposes both "electric field" (the field) and "conservation of mechanical energy" (potential energy)
- **Premise**: the section's Teacher Support asks teachers to review the concept of potential energy first (`Review the concept of potential energy as being the potential an object has to do work by virtue of its position…`, ev-087);
  and `ΔV = −E Δx` ties potential difference directly to field strength
- **Reasoning**: without the habit of "potential energy is bookkept as a difference", the minus sign in `U_E = k q₁q₂ / r` cannot be understood —
  a cognitive dependency, not chapter order
- **Evidence**: ev-087
- **Attacked**: no attacks yet
- **Attribution**: @hpleapfrog · 2026-10-18

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-18 | Entry created; fourth node of the electrostatics chapter, the electrostatic segment of the energy thread | written after reading m54426 in full (ev-087) | @hpleapfrog |
