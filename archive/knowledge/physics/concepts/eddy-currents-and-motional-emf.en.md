---
id: kb:physics:eddy-currents-and-motional-emf
type: 知识点
title: "Eddy currents and motional emf"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know "Electromagnetic induction" and "Lorentz force" and need to compute the emf of a rod cutting magnetic field lines and explain electromagnetic damping
  条件: covers the two derivations of `ε = Bℓv` and the qualitative mechanism of eddy currents and magnetic damping only; quantitative eddy-current loss, skin depth, electromagnetic driving, engineering design of eddy-current brakes, and quantitative Hall-effect calculations are not built
edges:
  先修: ["[Electromagnetic induction](electromagnetic-induction.en.md)", "[Lorentz force](lorentz-force.en.md)"]
  支持: []
  攻击: []
evidence: [ev-193]
license: CC-BY-SA-4.0
---

> **English version of [`涡流与动生电动势.md`](涡流与动生电动势.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the emf of a rod cutting magnetic field lines with `ε = Bℓv`, justify it by both the `F = qvB` route and the `ε = ΔΦ/Δt` route, and explain why eddy currents damp motion and why slots or an insulator nearly remove the damping

## Definition

**Motional emf** is the emf produced when a conductor and a magnetic field move relative to each other. When `B`, the conductor's length `ℓ`, and the velocity `v` are mutually perpendicular:

`ε = Bℓv`

The textbook offers two routes to the same result:

- **Lorentz-force route**: the charges in the conductor move with it at `v` and feel `F = qvB` along the conductor. Charge accumulates at the ends until the electric force balances the magnetic force: `qE = qvB`, i.e. `E = vB`; the potential difference is `ε = Eℓ = Bℓv`
- **Faraday route**: the conductor sweeps an area `ΔA = ℓΔx`, so `ΔΦ = BΔA` and `ε = ΔΦ/Δt = BℓΔx/Δt = Bℓv`

The direction follows from Lenz's law or the right-hand rule; in the textbook's slider circuit, with the rod moving right and the field into the page, the induced current is counterclockwise and the rod's top end is positive. Relative motion is what matters: either the conductor or the field may be moving.

When the three are not mutually perpendicular the general form is `ε = Bℓv sinθ` (`θ` is the angle between `v` and `B`, or between `ℓ` and `B`, depending on which pair is perpendicular). The textbook's body gives only the perpendicular case; the general form appears only in an exercise.

**Eddy currents** are induced current loops inside a conductor. As a conductor enters or leaves a field its flux changes, and the magnetic force on the eddy currents **opposes the relative motion** — this is **magnetic damping**:

- entering the field: flux increases, and the induced current is directed so that the force on the loop points backward; leaving the field: flux decreases, the current reverses, and the force still points backward
- **completely inside a uniform field** the flux does not change: no eddy current and no damping
- a slotted metal plate breaks the large loop into small ones whose currents oppose one another and cancel; in an insulator the eddy currents are extremely small
- the damping force falls as the speed falls, so it **cannot bring an object completely to rest** — eddy-current brakes on trains and roller coasters only slow the vehicle, and friction brakes must finish the stop

Orders of magnitude: a `1.0 m` rod at `3.0 m/s` in the Earth's field gives `ε = 5.0×10⁻⁵ × 1.0 × 3.0 = 150 μV`; a `20 km` tether at `7.80 km/s` through `5.00×10⁻⁵ T` gives a maximum `7.80 kV` (about `5 kV` in practice, because the velocity was not perpendicular to the field).

> [!IMPORTANT]
> **The equivalence of the two routes is supplied by this library.**
>
> The textbook says the magnetic force on moving charges "produces `emf = Bℓv`" and that this is the same expression as for the Hall effect, but it **never writes the charge-separation balance `qE = qvB`** — that derivation belongs to this entry (K1). The textbook also does not distinguish the motional emf **along the conductor's length** from the Hall voltage **across its width**: both are written `B×length×v` with different lengths. It calls the Hall effect only one aspect of induction.

> [!IMPORTANT]
> **Eddy currents are not "only where there is motional emf".**
>
> The textbook's glossary defines an eddy current as "caused by motional emf", yet its own body says a motional emf arises when the conductor moves **or when the magnetic field moves relative to the conductor**. More generally, a stationary conductor in a time-varying field (a transformer core) also carries eddy currents. This entry reads an eddy current as an induced current loop in a conductor and does not restrict it to flux cutting.

> [!NOTE]
> **Four source problems and how this entry handles them.**
>
> 1. **The body gives only `ε = Bℓv` under the perpendicular condition**, while an exercise asks for `ε = Bℓv sinθ`; this entry adds the general form in the Definition and notes where it comes from.
> 2. **The tethered-satellite energy does not balance**: the exercise gives `5.00 kV × 10.0 A = 50 kW`, but its (b) `2.81×10⁸ J` comes from `F = IℓB = 10.0 N` times `7.80 km/s` times `3600 s`, i.e. `78 kW` — a factor of `1.56`. This entry keeps the force calculation and the order of magnitude but does not treat that energy chain as self-consistent.
> 3. **"The base of the pot needs to be ferromagnetic ... for induction to work" is too strong**: eddy currents arise in any conductor; ferromagnetism is a coupling and efficiency condition for common cooktops, which the textbook does not develop. This entry says only that common induction cooktops require a ferromagnetic base, not that physics requires one.
> 4. **"Drag is proportional to speed" is not derived**; the textbook states it only in an application. K2 marks it as an unproved idealization.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electromagnetic induction](electromagnetic-induction.en.md) — `ε = −NΔΦ/Δt` and Lenz's law give the Faraday route and the direction; the slider-circuit special case `ε = Bvℓ` already appears there. "Induction depends on change" appears here as: a rod completely inside a uniform field has no eddy current, only at the boundaries |
| Prerequisite | [Lorentz force](lorentz-force.en.md) — `F = qvB` is the microscopic explanation of motional emf; without it the formula can only be memorized |
| Related | [Transformer](transformer.en.md) — a time-varying flux also drives eddy-current losses in the iron core, which is not built here; this entry treats eddy currents and damping in a solid conductor only |
| Recorded gap | **Quantitative eddy-current loss (resistivity, frequency, skin depth)**, **electromagnetic driving (induction motors, linear motors)**, **engineering design of eddy-current brakes**, **quantitative relation between Hall voltage and carrier sign**, and **spatial variation of the Earth's field and tethered-satellite engineering** are not built in this repo |

## Argument

### K1 · The Lorentz-force route and the Faraday route give the same `Bℓv` (no attack yet)

- **Claim**: motional emf can be explained either by the microscopic force `qvB` on the conductor's charges or by the flux-change Faraday law, and both give `ε = Bℓv`
- **Premise**: the textbook writes that moving charges feel `F = qvB`, that opposite charges move in opposite directions and "produce `emf = Bℓv`", then derives the same result from Faraday's law with `ΔA = ℓΔx` and `v = Δx/Δt` (ev-193); the charge-separation balance `qE = qvB` is a derivation supplied here
- **Reasoning**: in the laboratory frame the charges move with the rod and the magnetic force pushes them along it; the field from the accumulated charge eventually balances the magnetic force, `E = vB`, and integrating along the rod gives `Bℓv`. In the rod's rest frame the charges are still and the field moves at `−v`; the moving field produces an electric field that again gives `E = vB`. The two routes are two descriptions of one physical fact
- **Evidence**: ev-193
- **Attacked**: the textbook places the Hall effect and motional emf side by side without the balance derivation and without noting that the two "lengths" differ: the Hall voltage is across the conductor's width, the motional emf along its length. Its "unification of forces" box mentions the relation between moving electric and magnetic fields but does not develop a frame transformation
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Eddy-current damping comes from Lenz's law and acts on both entry and exit (no attack yet)

- **Claim**: when a conductor enters or leaves a field, the magnetic force on its eddy currents opposes the motion; inside a uniform field there is no eddy current
- **Premise**: the textbook analyses a metal pendulum swinging between magnet poles: on entry the flux increases and the induced current is counterclockwise, so only the side inside the field feels a force to the left; on exit the flux decreases, the current is clockwise, and the force is still to the left; once fully inside a uniform field the flux is constant and there is no current; a slotted plate's small loops cancel, and an insulating bob is almost unaffected (ev-193)
- **Reasoning**: Lenz's law requires the induced current's field to oppose the change in flux. On entry it opposes the increase; on exit it opposes the decrease; in both cases the magnetic force on the current points opposite to the motion, so damping appears at both boundaries. Inside a uniform field there is no flux change, hence no induced current and no damping
- **Evidence**: ev-193
- **Attacked**: the textbook says the drag "is proportional to speed" without deriving it; the actual eddy-current distribution, resistivity, and frequency all affect the force, and the cancellation in a slotted plate is described only qualitatively. This entry does not treat "proportional to speed" as proved
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · Applications of eddy currents are a set of trade-offs (no attack yet)

- **Claim**: magnetic damping is useful in balances, waste sorting, metal detectors, and vehicle brakes, but each application has a limit
- **Premise**: the textbook lists: a balance uses magnetic damping to stop swinging quickly, and the damping falls to zero at zero speed so sensitivity is preserved; waste sorting exploits the fact that eddy currents occur only in conductors, separating all metals rather than only ferromagnetic ones; a metal detector uses eddy currents to change the secondary coil's current; train and roller-coaster brakes are smooth and unaffected by weather but cannot stop the vehicle completely; an induction cooktop heats the pot by eddy currents, and common cooktops require a ferromagnetic base (ev-193)
- **Reasoning**: a damping force that falls with speed is good at removing energy quickly but bad at a final lock-up; eddy currents occur only in conductors, so they separate metal from non-metal but not one metal from another; eddy-current heating needs no flame, but the pot material and its coupling to the cooktop set the efficiency
- **Evidence**: ev-193
- **Attacked**: the textbook gives two mechanisms for metal detectors — m42420 says the metal changes the coil's self-inductance, m42404 says eddy currents change the secondary current — and does not reconcile them; its "must be ferromagnetic" for induction cooktops does not separate physical necessity from engineering practice. This entry marks both as unchecked rather than supplying a causal story on the textbook's behalf
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; new node in the 选必二 "electromagnetic induction" chapter, attached after "Electromagnetic induction" and "Lorentz force" | written after reading m42400 / m42404 in full (ev-193) | @hpleapfrog |
