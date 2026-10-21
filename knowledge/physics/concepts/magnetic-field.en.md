---
id: kb:physics:magnetic-field
type: 知识点
title: "Magnetic field"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know "Electric field strength" and need field lines, magnetic flux density, and the magnetic field of a current
  条件: covers poles and dipoles, field lines, the tesla, fields of currents, and Earth's field only; Ampere force and Lorentz force are separate entries, and magnetic flux is not built
edges:
  先修: ["[Electric field strength](electric-field.en.md)"]
  支持: []
  攻击: []
evidence: [ev-160]
license: CC-BY-SA-4.0
---

> **English version of [`磁场.md`](磁场.md).**

> [!TIP]
> **After reading this entry you should** be able to draw the field lines of a bar magnet and of a straight wire, use the right-hand rule for the field of a current, and explain "the field is stronger where the lines are denser" and "Earth's magnetic south pole lies near the geographic North Pole"

## Definition

A **magnetic field** is the field around a magnet or a current through which magnetic forces act; its strength and direction are described by the **magnetic flux density** `B`, measured in **tesla** (T).

- **magnetic pole**: the part of a magnet that exerts the strongest force. Like poles repel and unlike poles attract
- **magnetic dipole**: cut a bar magnet in half and each half still has a north and a south pole; the same holds down to the atomic scale. The textbook: `no experiment has ever found any object with a single magnetic pole, from the smallest subatomic particle such as electrons to the largest objects in the universe such as stars.`
- **field lines**: their direction is defined as the direction in which the north pole of a compass needle points. Outside the magnet they run from N to S and **continue inside the magnet back to N, forming closed loops**; the denser the lines, the stronger the field
- **Earth's field**: the magnetic pole near the geographic North Pole is a **magnetic south pole**, which is why the north pole of a compass points geographically north
- **field of a current**: Oersted found that a current-carrying wire deflects a compass needle. For an infinitely long straight wire `B = μ0 I / (2πr)`; inside a long solenoid `B = μ0 N I / ℓ`, with `μ0 = 4π×10⁻⁷ T·m/A` the permeability of free space
- **definition of the tesla**: the textbook defines it through the force on a moving charge — `the Tesla, is the magnetic field required to produce a 1 N force on a 1 C charge moving at 1 m/s in a direction perpendicular to the field`

> [!IMPORTANT]
> **Magnetic field lines close on themselves; electric field lines do not.**
>
> The textbook states `Magnetic field lines never stop, so the field lines actually penetrate the magnet to form complete loops`.
> Electric field lines start on positive charge and end on negative charge (or run to infinity) — **the textbook does not say this in this section**;
> it is this repo's contrast, added so that "closed" has something to mean. See the "Attacked" line of K1.
>
> One more thing that is easy to read backwards: **the pole near the geographic North Pole is a magnetic south pole**. The textbook says
> `the magnetic pole of Earth that is close to the geographic North Pole must be a magnetic south pole!`

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electric field strength](electric-field.en.md) — the textbook introduces the magnetic field by analogy with the electric field, and this entry reads field lines the same way |
| Follow-up | [Ampere force](ampere-force.en.md) — a current-carrying wire in a field; the field becomes measurable through a force |
| Follow-up | [Lorentz force](lorentz-force.en.md) — a moving charge in a field; the microscopic origin of the Ampere force |
| Recorded gap | **Magnetic flux**, **magnetic materials and magnetization curves**, and **the unified electromagnetic field (Maxwell's equations)** are not built in this repo |

## Argument

### K1 · Closed field lines and the absence of magnetic monopoles (no attack yet)

- **Claim**: magnets are always dipoles; magnetic field lines have no start or end and can only close
- **Premise**: the textbook says that after cutting a magnet `Each half of the bar magnet has a north pole and a south pole`, and that `no experiment has ever found any object with a single magnetic pole`; it also says `Magnetic field lines never stop, so the field lines actually penetrate the magnet to form complete loops` (ev-160)
- **Reasoning**: if a single pole (magnetic charge) existed, field lines could start there and end on another pole, as electric field lines do. Experiments find no single pole, and field lines must close, so the two facts support each other: the magnetic field has no "source", only dipoles
- **Evidence**: ev-160
- **Attacked**: the textbook says "**no experiment has found one yet**", not that none can exist; this entry treats it as an empirical fact, not a proven theorem. Also, "electric field lines run from positive to negative charge" is a contrast from outside this section — the textbook only states that magnetic lines close, and does not make this comparison here
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Currents produce magnetic fields, with one right-hand rule (no attack yet)

- **Claim**: magnetic fields do not come only from magnets; a current also has a field, and the same right-hand rule gives its direction
- **Premise**: the textbook records that Oersted `found that a compass needle was deflected by a current-carrying wire`; for a straight wire `The magnetic field lines form concentric circles around the wire`, and `with your right thumb pointed in the direction of the current, the magnetic field will be in the direction in which your right fingers curl`; for a solenoid the fingers curl with the current and the thumb points along the field inside (ev-160)
- **Reasoning**: the field of a straight wire forms concentric circles, with `B ∝ I/r`; a solenoid adds the contributions of every loop, giving a nearly uniform field inside with `B ∝ NI/ℓ`. The two uses of the right-hand rule mirror each other: thumb-current/fingers-field for the straight wire, fingers-current/thumb-field for the solenoid
- **Evidence**: ev-160
- **Attacked**: `B = μ0I/(2πr)` holds only for an **infinitely long** straight wire, and `B = μ0NI/ℓ` only **deep inside a long** solenoid; the textbook states the formulas without stressing these conditions, and this entry records them. The textbook does not derive either formula
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 选必二 "Ampere force and Lorentz force" chapter, providing the field concept for both | written after reading m54465 in full (ev-160) | @hpleapfrog |
