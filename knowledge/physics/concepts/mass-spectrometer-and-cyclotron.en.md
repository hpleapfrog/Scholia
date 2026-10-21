---
id: kb:physics:mass-spectrometer-and-cyclotron
type: 知识点
title: "Mass spectrometers and cyclotrons"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know the Lorentz force and the electric field and want to understand how a magnetic field measures mass or accelerates particles repeatedly
  条件: covers only the crossed-field velocity selector, magnetic mass separation, and the qualitative principles of the cyclotron and the synchrotron/linear accelerator; no quantitative relativistic accelerators, beam optics, MRI, or CRT magnetic deflection
edges:
  先修: ["[Lorentz force](lorentz-force.en.md)", "[Electric field](electric-field.en.md)"]
  支持: []
  攻击: []
evidence: [ev-182]
license: CC-BY-SA-4.0
---

> **English version of [`质谱仪与回旋加速器.md`](质谱仪与回旋加速器.md).**

> [!TIP]
> **After reading this entry you should** be able to explain how a mass spectrometer first selects a speed with crossed electric and magnetic fields and then separates ions by mass (strictly, by mass-to-charge ratio), and why a cyclotron can keep accelerating particles with a fixed-frequency alternating voltage — and when that "fixed frequency" fails

## Definition

### The velocity selector: crossed electric and magnetic fields

Send a charged particle perpendicularly through a uniform electric field and a uniform magnetic field that are perpendicular to each other. The electric force `qE` and the Lorentz force `qvB` point in opposite directions; when they are equal in magnitude the particle feels no transverse net force and passes straight through (ev-182):

`qE = qvB` ⇒ `v = E/B`

- only particles whose speed is exactly `E/B` get through; faster or slower ones are pushed off the axis by the transverse force
- `q` cancels from the equation, so the selected speed is **independent of charge magnitude, mass, and the sign of the charge** — for the same direction of incidence, any charge with speed `E/B` passes (the Section Summary in ev-182 says `any charge`)
- changing `E` or `B` changes the selected speed; this is why the device is called a velocity selector or **velocity filter**

> The velocity selector screens speed only, not mass. Measuring mass needs the magnetic stage that follows.

### The mass spectrometer: separating masses with a magnetic field

A mass spectrometer measures the **mass** of ions; most mass spectrometers use magnetic fields to do so (ev-182). One relatively simple design has three stages (ev-182):

1. **Ion source**: like an electron gun, it gives the ions their charge, accelerates them to some speed `v`, and forms them into a beam
2. **Velocity selector**: the crossed fields above let through only ions with speed `E/B`
3. **Uniform magnetic-field region**: only a magnetic field; ions enter perpendicularly and move in circles whose radius follows `r = mv/(qB)` (see [Lorentz force](lorentz-force.en.md))

With `v`, `q`, and `B` fixed, **the radius is proportional to the mass**: `r ∝ m` (ev-182). Strictly, a mass spectrometer measures the **mass-to-charge ratio** `m/q`; because `q` always comes in integer multiples of the electron charge and the charge state can be determined, the mass follows (ev-182).

The applications the textbook gives (ev-182): chemistry and biology laboratories identify substances by mass-to-charge ratio; medicine uses mass spectrometers to measure the concentration of isotope tracers; large biological molecules such as proteins are usually broken into smaller fragments first, and recently whole virus particles have been analysed; a gas chromatograph or a high-performance liquid chromatograph often provides an initial separation before the sample enters the spectrometer.

### The cyclotron: accelerating particles while they go round

In a cyclotron the magnetic field makes the particles move in circles, and the electric field accelerates them only in the gap between two D-shaped metal boxes (the **Dees**). The alternating voltage has a fixed frequency; the particle crosses the gap twice per revolution and is accelerated twice per revolution (ev-182). As its energy grows, both its speed and its orbital radius grow: the path is an **outward spiral**, and the particle is extracted at the edge (ev-182).

The key fact is that **the period is independent of speed** (ev-182):

`T = 2πm / (qB)`, `f = qB / (2πm)`, `ω = qB / m`

These follow from `r = mv/(qB)` and `T = 2πr/v`; the derivation is K2 of [Lorentz force](lorentz-force.en.md). The textbook asks the reader to show `T = 2πm/(qB)` and notes that it is independent of speed, radius, and hence energy (ev-182). Because the period is constant, the supply can stay at a **fixed frequency** in step with the particle, giving it a push at every gap crossing.

The textbook's two numerical examples (ev-182, recomputed here):

- a proton in `B = 1.20 T` has a cyclotron frequency of `18.3 MHz`
- a 25.0-MeV proton in `1.20 T` has an orbital radius of `60.2 cm`

If the Dees have maximum radius `R`, the maximum kinetic energy follows from `v_max = qBR/m` (this library's derivation):

`K_max = q²B²R² / (2m)`

### Synchrotrons, linear accelerators, and the limit of "fixed frequency"

The cyclotron's fixed frequency holds only in the **non-relativistic** regime. Near the speed of light the momentum is `p = γmv`, so the period becomes `T = 2πγm/(qB)` and grows with energy; a fixed-frequency voltage then falls out of step with the particle (this library's addition; the textbook does not develop this layer).

A **synchrotron** solves this by **raising both the frequency of the alternating voltage and the magnetic field strength** during acceleration, so that the particles travel faster and faster on a fixed-radius orbit (ev-182). The field must grow with energy to hold high-energy particles on the same radius, so high-energy synchrotrons use superconducting magnets and become very large (ev-182). A magnetic field bending a charged particle makes it radiate; this is **synchrotron radiation**. Linear accelerators line up the accelerating tubes in a straight line precisely to avoid the synchrotron-radiation loss that is especially severe for electrons on curved paths (ev-182).

> [!NOTE]
> **Source faults and this library's additions** (ev-182)
>
> 1. m42718 says `The Van de Graaff (named after the Dutch physicist)`, but Van de Graaff was an American physicist, born in Tuscaloosa, Alabama, in 1901; this library checked Britannica and the Encyclopedia of Alabama. This entry does not repeat the "Dutch physicist" claim.
> 2. An AP question in m42718 asks for the first hint that conservation of mass and conservation of energy had to be combined. The key gives `(c)` (Yukawa's theory) but adds the note `though this comes from Einstein's special relativity`; that explanation does not fit option (c) and, by its own wording, points to (d) `They were always related`.
> 3. A Critical Thinking answer in m42388 writes the electron mass as `9.11×10⁻¹¹ kg` instead of `9.11×10⁻³¹ kg` (the MathML exponent is −11), so its radius and time come out with the wrong exponents; with the correct mass, `r ≈ 1.42×10³ m` and `t ≈ 2.85×10⁻⁵ s` — the coefficient 2.85 is right, the exponent is not.
> 4. The LHC figures in m42718 are from around 2010 (3.5 TeV per beam, 7 TeV per collision, "CERN hopes to double the beam energy in 2014"); this entry cites them as historical data only.
> 5. Most exercises in m42388 practise fields of currents, the Hall effect, and MHD; only the 25.0-MeV proton and the cyclotron-frequency problems relate directly to mass spectrometers and cyclotrons. The exercises in m42375 are closer to this section.
>
> **Supplied here, not by the textbook**: `K_max = q²B²R²/(2m)`, `r = (m/q)(E/B²)` (when both regions use the same magnetic field), the isotope semicircle separation `2Δr`, and the reasoning that relativistic mass increase makes a fixed frequency fail. The textbook gives only `v = E/B`, the proportionality `r ∝ m`, and the qualitative cyclotron description.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Lorentz force](lorentz-force.en.md) — `r = mv/(qB)` and `T = 2πm/(qB)` are the entire quantitative basis of the mass spectrometer and the cyclotron |
| Prerequisite | [Electric field](electric-field.en.md) — the `qE` in the velocity selector and the accelerating field in the ion source |
| Related | [Motion of charged particles in an electric field](charged-particle-in-electric-field.en.md) — the ion source and the accelerating gap use the same electric acceleration and electron-gun ideas |
| Recorded gap | **quantitative treatment of the relativistic cyclotron (synchrocyclotron)**, **beam focusing and emittance**, **engineering of RF cavities and superconducting magnets**, **quantitative MRI/NMR**, **quantitative CRT magnetic deflection**, and **the Hall effect and MHD generators** are not built here |

## Argument

### K1 · The velocity selector is independent of charge magnitude, mass, and sign (sign independence is this library's reasoning)

- **Claim**: the speed admitted by the crossed fields is `v = E/B`; the condition contains neither `q` nor `m`, and holds for any charge with the same direction of incidence
- **Premises**: the textbook writes that the crossed electric and magnetic fields produce "forces in opposite directions on the ions", that only ions with balanced forces go straight, and that `qE = qvB` with `q` cancelled gives `v = E/B`; the Section Summary calls the device a velocity filter and states the condition for `any charge` (ev-182)
- **Reasoning**: both forces are proportional to `q`, so `q` cancels and the mass never appears. For a fixed velocity direction, replacing `q` by a negative value reverses both `qE` and `qv × B`, so the two forces stay opposite — positive and negative charges can pass at the same time, provided they move in the same direction. A particle whose speed is not `E/B` feels a transverse net force and is pushed away from the slit
- **Evidence**: ev-182
- **Attacked by**: **"positive and negative charges can both pass" is this library's inference from the cancellation of `q`; the textbook only writes `any charge` and does not discuss sign**; it also gives no slit geometry, fringing fields, or velocity spread — a real selector admits a narrow band of speeds, not one exact value
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Mass spectrometer: with `v`, `q`, and `B` fixed, radius is proportional to mass (the separation formula is this library's derivation)

- **Claim**: in the uniform-field region the radius is `r = mv/(qB)`; with `v`, `q`, and `B` fixed, `r ∝ m`, so measuring the radius measures the mass-to-charge ratio; isotopes starting from the same point separate by `2Δr` after a semicircle, with `Δr/r = Δm/m`
- **Premises**: the textbook says that once the velocity selector fixes `v`, "the radius of the path r is simply proportional to the mass m" in the magnetic region, and notes that `q` is in multiples of the electron charge so the charge state can be determined; the m42375 exercise gives a separation of `0.173 m` for oxygen-16 and oxygen-18 (ev-182)
- **Reasoning**: substituting `v = E/B` into `r = mv/(qB)`, and assuming the same `B` in both regions, gives `r = (m/q)(E/B²)`, so the radius is fixed by the mass-to-charge ratio and the fields. For one charge state, `Δr/r = Δm/m`; two paths starting together and traversing a semicircle land `2Δr` apart. With the textbook's numbers, oxygen-16 has `r = 0.693 m` and oxygen-18 has `r = 0.779 m`, so `2Δr = 0.173 m`, matching the answer
- **Evidence**: ev-182
- **Attacked by**: **`r = (m/q)(E/B²)` and the `2Δr` formula are this library's combination of two textbook statements; the textbook gives only the qualitative "r is proportional to m"**; a real instrument also relies on calibration and detectors, and the textbook does not discuss resolution, peak shape, or the ambiguity from mixed charge states
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · A cyclotron uses a fixed frequency; a synchrotron must tune frequency and field (the relativistic limit is this library's addition)

- **Claim**: non-relativistically `T = 2πm/(qB)` is independent of speed, so a fixed-frequency alternating voltage accelerates the particle once per half turn; the maximum kinetic energy is `K_max = q²B²R²/(2m)`; near the speed of light the period grows with `γ`, the fixed frequency fails, and a synchrotron must raise both the frequency and the field
- **Premises**: the textbook says a cyclotron uses fixed-frequency alternating fields and the particles spiral outward; the particle crosses the gap between the Dees twice per revolution and is accelerated twice; in a synchrotron "the frequency of the alternating voltage and the magnetic field strength are increased" to keep the radius fixed; the m42388 exercise asks the reader to show that `T`, `f`, and `ω` are independent of speed, radius, and energy (ev-182)
- **Reasoning**: eliminating `v` from `T = 2πr/v` and `r = mv/(qB)` gives `T = 2πm/(qB)`, independent of speed, so a fixed frequency stays in step. Two accelerations per revolution at `qV` each add `2qV` per turn; the radius grows with speed, and at `R` the speed is `v_max = qBR/m`, so `K_max = q²B²R²/(2m)`. Relativistically `p = γmv`, so `T = 2πγm/(qB)` grows with energy and a fixed-frequency voltage falls out of step — hence the synchrotron tunes frequency and field together
- **Evidence**: ev-182
- **Attacked by**: **`K_max`, `γ`, and "the fixed frequency fails" are supplied by this library; the textbook only says that a synchrotron tunes frequency and field, without explaining why**; the derivation ignores the gap transit time and the field phase, and `K_max` assumes the particle stays on the ideal orbit
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Action | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; adds the last missing "cyclotron, mass spectrometer, velocity selector" gap of Elective-2 chapter 1, turning the chapter 🟢; also corrects the old note in "Lorentz force" that listed the period as missing | written after reading m42375/m42718/m42388 in full, ev-182 | @hpleapfrog |
