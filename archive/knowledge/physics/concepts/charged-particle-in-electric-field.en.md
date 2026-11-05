---
id: kb:physics:charged-particle-in-electric-field
type: 知识点
title: "Motion of a charged particle in an electric field"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned electric field strength, potential difference, and energy conservation and need to understand acceleration and deflection of charged particles in a uniform electric field, and to solve electron-gun and deflection-plate problems
  条件: covers linear acceleration in a uniform field, projectile-like transverse deflection for a particle entering perpendicular to the field, and the electron volt; non-uniform fields, circular motion in a magnetic field, the quantitative treatment of relativistic corrections, the full structure of an oscilloscope, and fringing fields are not built here
edges:
  先修: ["[Electric potential energy and potential](electric-potential-energy.en.md)", "[Electric field strength](electric-field.en.md)", "[Projectile motion](projectile-motion.en.md)", "[Newton's second law](newtons-second-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-176, ev-177]
license: CC-BY-SA-4.0
---

> **English version of [`带电粒子在电场中的运动.md`](带电粒子在电场中的运动.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the speed after acceleration with `qU = ½mv²`, compute the transverse displacement and deflection angle with the projectile-motion formulas, and explain why the trajectory is a parabola rather than a circle

## Definition

**Force in a uniform field**: a potential difference `U` across two parallel metal plates produces (away from the edges) a uniform field of magnitude

`E = U/d`

where `d` is the plate separation; the field points from the positive to the negative plate. A charge `q` between the plates feels

`F = qE`

whose direction reverses with the sign of `q`. By Newton's second law,

`a = qE/m = qU/(md)`

For an electron (`q = −e`) the force is opposite to the field, so the electron is attracted toward the positive plate.

**Acceleration**: if a particle starts from rest and moves through a potential difference `U` along the field, the field does positive work and the kinetic energy increases. For an accelerating particle, take the energy gain as

`|q|U = ½mv²`

so

`v = √(2|q|U/m)`

A positive charge is accelerated when it moves from higher to lower potential; an electron is accelerated when it moves from lower to higher potential. Either way the energy gain is `|q|U`. The textbook's electron-gun example is exactly this: electrons that gain 25.0 keV have passed through a potential difference of 25.0 kV, because the electron's charge magnitude is `e`.

**Electron volt**: the energy gained by one fundamental charge moving through 1 V is one electron volt:

`1 eV = 1.60×10⁻¹⁹ J`

An electron through 100 V gains 100 eV; a doubly positive ion through 100 V gains 200 eV. `keV`, `MeV`, and `GeV` are `10³`, `10⁶`, and `10⁹` eV.

**Deflection**: a particle enters the region between the plates with speed `v₀` perpendicular to the field (plate length `L`, separation `d`, potential difference `U`). Along the field it has zero initial velocity and constant acceleration; perpendicular to the field it moves at constant velocity:

`t = L/v₀` (time between the plates)
`y = ½at² = qUL²/(2mdv₀²)` (transverse displacement on exit)
`tan θ = v_y/v₀ = at/v₀ = qUL/(mdv₀²) = 2y/L` (angle between the exit velocity and the incident direction)

The trajectory is a **parabola**, the same mathematical shape as projectile motion under gravity, which is why this is called "projectile-like" motion. The signs of `y` and `tan θ` follow the sign of `q`; if the incident velocity is not perpendicular to the field, decompose it along and perpendicular to the field first.

**Oscilloscope**: Chinese textbooks often use the oscilloscope as an application — an electron gun accelerates the electrons, deflection plates steer the beam transversely, and a fluorescent screen shows the landing point as a bright spot. The OpenStax material only mentions that electrons can be accelerated in an old television tube or an oscilloscope (m42324); it gives no quantitative formula for electrostatic deflection plates. The `y` and `tan θ` above are derived here from the uniform field, Newton's second law, and projectile motion, not taken from the textbook.

> [!IMPORTANT]
> **The trajectory is a parabola, not a circle.**
>
> The force exerted by a uniform electric field on a charge has constant magnitude and direction (a constant force), so the transverse acceleration is constant, `y ∝ t²`, and the trajectory is a parabola. Circular motion requires a force that is always perpendicular to the velocity and a constant speed; here the force direction is fixed and the speed is increasing, so neither condition holds. The textbook's Test Prep item offers "a section of a circle" as a wrong answer precisely because of this distinction.

> [!IMPORTANT]
> **Use the energy gain `|q|U` in the acceleration formula; do not be misled by the source's double negative.**
>
> m42324's electron example substitutes both `q = −1.60×10⁻¹⁹ C` and `V = −100 J/C` into `v = √(2qV/m)`. The two negatives multiply to a positive, and the value `5.93×10⁶ m/s` is correct, but a reader can easily misread it as "negative energy". The safe procedure is: first decide whether the particle is being accelerated, then use `|q|U = ½mv²`; the sign of the potential difference only tells you the direction of the energy change.

> [!IMPORTANT]
> **Relativity must be included at high speed.**
>
> Both `½mv²` and `v = √(2qU/m)` are non-relativistic results. The textbook explicitly warns that accelerating voltages much higher than 100 V make electrons fast enough that relativistic effects must be included. A 25 keV electron has the classical speed `v ≈ 9.4×10⁷ m/s ≈ 0.31c`, already about 4% above the relativistically correct value; at higher voltages the classical formula overestimates the speed by more.

> [!IMPORTANT]
> **A hidden textbook item says a fourfold range means "100% more mass"; the correct figure is 1500%.**
>
> m42326 contains a Test Prep item hidden inside an HTML comment: two particles with identical charge and initial velocity enter the uniform field from the same point, and the second strikes the positive plate four times as far away as the first; the answer says the second has "100% more mass". But for transverse deflection, striking the same plate means the transverse displacement `y` is the same, and `x = v₀√(2my/(qE))`, so `x ∝ √m`. Four times the range therefore means sixteen times the mass, i.e. 1500% more, not 100%. "100% more mass" (twice the mass) would give only `√2 ≈ 1.41` times the range.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electric potential energy and potential](electric-potential-energy.en.md) — `U` is the potential difference, `qU` is the work done by the field, and energy conservation gives the acceleration formula |
| Prerequisite | [Electric field strength](electric-field.en.md) — `F = qE` and the uniform-field relation `E = U/d` are the source of the acceleration and deflection |
| Prerequisite | [Projectile motion](projectile-motion.en.md) — constant velocity perpendicular to the field plus constant acceleration along it is exactly the mathematical structure of projectile motion |
| Prerequisite | [Newton's second law](newtons-second-law.en.md) — `a = F/m = qE/m` |
| Related | [Mass spectrometers and cyclotrons](mass-spectrometer-and-cyclotron.en.md) — electric acceleration in the ion source and the accelerating gap, followed by magnetic confinement and cyclotron/synchrotron acceleration |
| Recorded gap | **Motion in a non-uniform field**, **quantitative relativistic corrections**, **the full structure of an oscilloscope (electrostatic versus magnetic deflection, focusing and aberrations)**, **fringing fields of deflection plates**, **beam focusing and emittance**, and **the complete theory of accelerators** are not built here; **motion in a magnetic field** is covered by [Lorentz force](lorentz-force.en.md) |
| Related technology | Electron guns, oscilloscopes, cathode-ray tubes, particle accelerators |

## Arguments

### K1 · The acceleration formula follows from energy conservation (no attacks yet)

- **Claim**: a charged particle accelerated from rest through a potential difference `U` reaches `v = √(2|q|U/m)`
- **Premises**: the electric force is conservative; gravity is neglected (for electrons and ions the electric force is far larger); non-relativistic motion; the textbook's electron-acceleration example and the definition of the electron volt (ev-176)
- **Reasoning**: the field does work `W = |q|U`, and the work–energy theorem gives `W = ½mv² − 0`, hence `v = √(2|q|U/m)`. Numerical check: an electron through 100 V has `v = √(2 × 1.60×10⁻¹⁹ × 100 / 9.11×10⁻³¹) = 5.93×10⁶ m/s`, matching the textbook. For the 25.0 keV electron gun, `v = √(2 × 2.5×10⁴ × 1.60×10⁻¹⁹ / 9.11×10⁻³¹) ≈ 9.4×10⁷ m/s`, about `0.31c`, consistent with the warning that 25 keV needs a relativistic correction
- **Evidence**: ev-176
- **Attacked by**: applies only in the non-relativistic regime; neglecting gravity is not always valid at extreme energies or for very low charge-to-mass ratios; the textbook writes both `q` and `V` as negative, which is easy to misread; `U` must be the potential difference the particle actually crosses, not the supply voltage
- **Author**: @hpleapfrog · 2026-10-21

### K2 · Transverse deflection is projectile-like motion (no attacks yet)

- **Claim**: a charged particle entering a uniform field perpendicular to it follows a parabola with `y = qUL²/(2mdv₀²)` and `tan θ = qUL/(mdv₀²)`
- **Premises**: the field between the plates is `E = U/d`; `F = qE`; a constant force means constant transverse acceleration and constant longitudinal velocity; fringing fields and gravity are neglected; the textbook's electron gun and `E = V_AB/d` (ev-177)
- **Reasoning**: `a = qE/m = qU/(md)` and `t = L/v₀`, so `y = ½at² = qUL²/(2mdv₀²)`; on exit `v_y = at = qUL/(mdv₀)` and `tan θ = v_y/v₀ = qUL/(mdv₀²) = 2y/L`. Numerical check: for an electron with `v₀ = 1.0×10⁷ m/s`, `E = 1.0×10⁴ V/m`, and `L = 0.020 m`, `t = 2.0×10⁻⁹ s`, `a = 1.76×10¹⁵ m/s²`, `y = 3.5×10⁻³ m`, `tan θ = 0.351`, and `θ ≈ 19.3°`. Mass-scaling check: for fixed `y`, `x = v₀√(2my/(qE)) ∝ √m`, so four times the range means sixteen times the mass — the textbook's hidden item claiming "100% more" is wrong (ev-177)
- **Evidence**: ev-177
- **Attacked by**: the formulas assume a strictly uniform field and neglect fringing fields, gravity, and any deviation from perpendicular incidence; at high speed `m` must be the relativistic mass (or the classical formulas must be abandoned); the textbook gives no deflection formula, so `y` and `tan θ` here are derived rather than quoted
- **Author**: @hpleapfrog · 2026-10-21

### K3 · The electron gun's field and force can be checked (no attacks yet)

- **Claim**: a 25.0 keV electron gun with 4.00 cm plate separation has a field of `6.25×10⁵ V/m` and exerts 0.313 N on a 0.500 μC charge
- **Premises**: the electron is singly charged, so 25.0 keV corresponds to 25.0 kV; `E = U/d`; `F = qE`; the textbook's electron-gun example (ev-177)
- **Reasoning**: `E = 25.0×10³ V / 0.0400 m = 6.25×10⁵ V/m`; `F = 0.500×10⁻⁶ C × 6.25×10⁵ V/m = 0.313 N`, matching the textbook
- **Evidence**: ev-177
- **Attacked by**: `E = U/d` gives an average field, not a uniform one near the edges; treating all of the 25.0 keV as lost potential energy assumes zero initial kinetic energy and no collisions; a 0.500 μC charge is macroscopic and would significantly distort the original field, so the textbook's "force is the same everywhere" holds only when the charge's own field is neglected
- **Author**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; the last piece of Compulsory-3 "energy in an electrostatic field" is filled in and priority 17 is complete | ev-176/ev-177 after reading m42324/m42326 in full; the deflection formulas are derived here from projectile motion and Newton's second law, not taken from the textbook | @hpleapfrog |
