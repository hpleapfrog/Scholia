---
id: kb:physics:kp-conservation-of-mechanical-energy
type: 知识点
title: "Conservation of mechanical energy"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  范围: energy

edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-028]
license: CC-BY-SA-4.0
---

> **English version of [`机械能守恒.md`](机械能守恒.md).**

> [!TIP]
> **After reading this entry you should** be able to explain the interconversion of kinetic and potential energy, and to point out that frictional heat is an apparent counterexample to "conservation of energy"

## Definition

**Mechanical energy** is the sum of kinetic and potential energy:

```
kinetic energy KE = ½ m v²          potential energy PE = m g h
```

- **kinetic energy** is "the energy of motion"; **potential energy** is **stored** energy —
  "potential" means available, not that it *has to* or *will* be used
- the two convert into each other: going up, KE becomes PE (slower); coming down, PE becomes KE (faster)
- roller coaster: the work done to haul the car to the top of the first hill equals the PE it gains; on the plunge PE→KE
  with **maximum speed at the low point**; climbing again, KE turns back into PE
- units: work and energy are both measured in **joules** — "energy is the capacity to do work", so the dimensions coincide

**The law of conservation of energy**: **energy is neither created nor destroyed**.
In a closed system the total is constant; in terms of kinetic and potential energy:

```
KE₁ + PE₁ = KE₂ + PE₂
```

- a "**closed system**" means no energy is lost to the surroundings through friction or air resistance. For **dense falling objects**
  that is a good approximation; for a roller coaster it introduces some inaccuracy (the textbook's own caveat)
- **frictional heating is not a counterexample**: friction destroys no energy — it turns **macroscopic kinetic energy into
  kinetic energy at the atomic level**, which is what heat is. The textbook lists this as the **standard explanation** for apparent violations
- one consequence that cancels mass: when all the PE becomes KE, `m g h = ½ m v²` loses its `m` and gives
  `v² = 2 g h` — many problems **need no mass at all**

> [!NOTE]
> **Two textbook examples — check the books balance.** (ev-028)
>
> - a 10 kg rock falls from a 20 m cliff; at 10 m above the ground:
>   `PE₂ = 10 × 9.80 × 10 = 980 J`, total energy `= 1960 J`,
>   so `KE₂ = 1960 − 980 = 980 J` — exactly what the potential energy gave up
> - a child weighing 300 N at the top of a 3 m slide: `PE = 300 × 3 = 900 J`;
>   a 0.2 kg apple arriving with 10 J of PE: `v = √(2 × 10 ÷ 0.2) = 10 m/s`

> [!IMPORTANT]
> **The ledger for "slowing down naturally": the missing mechanical energy is booked as heat.**
>
> The textbook's note for advanced students: stopping at "because there is friction" is not enough — go **microscopic**.
> The energy friction removes is macroscopic kinetic energy turned into kinetic energy of atoms.
> One textbook problem is exactly this ledger: a cyclist coasts down one hill and up another until she stops,
> and **stops lower than she started** — the difference `m g (h₁ − h₂)` is the energy that became heat (warming the tyres).

## Relations

| Object | Entry | Note |
|---|---|---|
| teaching method | [conservation of mechanical energy · BL: energy is not the same thing as force and power](../methods/mech-energy-bl-units.en.md) | sort out the dimensions first |
| teaching method | [conservation of mechanical energy · OL: using frictional heat to dispel "slowing down on its own"](../methods/mech-energy-ol-friction-heat.en.md) | the misconception tagged by the textbook is dispelled here |
| misconception | [a moving object will "naturally" slow down](../misconceptions/objects-slow-naturally.en.md) | a misconception the textbook explicitly names |

> [!IMPORTANT]
> **This knowledge point forms a pair of tension with "inertia".**
> Inertia says "an object maintains its state of motion", while everyday observation says "objects stop by themselves".
> **The gap between the two is filled by friction** — and that is exactly the misconception the textbook asks students to dispel.

## Argument

### K9 · Why listed separately (no attack yet)

- **Claim**: conservation of mechanical energy deserves to be a separate knowledge point
- **Premise**: the textbook gives it its own section, and names a misconception in the teaching hints (ev-028)
- **Reasoning**: the textbook tags a misconception and a molecular-level explanation for it, showing it has an independent teaching goal
- **Evidence**: ev-028
- **Attacked**: it is in the same chapter as "work", "power" and "simple machines"; listing it separately may be over-fine-grained
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 1) | Issue #8 | @hpleapfrog |
| 2026-10-18 | learner half expanded: KE/PE formulas and conversion, `KE₁ + PE₁ = KE₂ + PE₂` and the closed system, the microscopic ledger of frictional heat, `v² = 2gh`, textbook examples | weak-entry expansion · m54273 re-read (ev-028) | @hpleapfrog |
