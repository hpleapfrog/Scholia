---
id: kb:physics:molecular-kinetic-theory
type: 知识点
title: "Kinetic-molecular theory"
status: 待审
author: "AI（DeepSeek V4.1 Flash Free）· 待 @hpleapfrog 复核 · 2026-11-05"
created: 2026-11-05
updated: 2026-11-05
scope:
  学科: 物理
  学段: 高中
  适用: students who know the ideal-gas equation and temperature and need a microscopic model for gas pressure, temperature, and molecular speed distributions
  条件: covers the five postulates of the ideal-gas model, the collision explanation of pressure, average translational kinetic energy and `u_rms`, the Maxwell-Boltzmann distribution, and the model's limits; the real-gas equation of state, mean free path and transport coefficients, the full equipartition of rotational/vibrational degrees of freedom, and quantum degenerate gases are out of scope
edges:
  先修: ["[Temperature and temperature scales](temperature-and-scales.en.md)", "[Gas laws and the ideal-gas equation](gas-laws-and-ideal-gas-equation.en.md)"]
  支持: []
  攻击: []
evidence: [ev-197]
license: CC-BY-SA-4.0
---

> **English version of [`分子动理论.md`](分子动理论.md).**

> [!TIP]
> **After reading this entry you should** be able to explain gas pressure as molecules colliding with the walls, write `p = (1/3)(N/V)m u_rms²` and `u_rms = √(3RT/M)`, and explain why lighter molecules move faster at the same temperature while their average translational kinetic energy is the same.

## Definition

The **kinetic-molecular theory (KMT)** is a microscopic model that explains the macroscopic properties of gases through molecular motion and collisions. The textbook separates it from the gas laws: the gas laws are empirical regularities, while KMT is a model that explains them.

The textbook gives five postulates (paraphrased here, with short quotes for the key phrases):

1. A gas consists of a large number of molecules in **continuous motion**, travelling in straight lines and changing direction only when they collide with other molecules or with the walls.
2. The **size of the molecules is negligible** compared with the distances between them.
3. Gas pressure results from **collisions between molecules and the container walls**.
4. Molecules exert **no attractive or repulsive forces** on each other or on the walls; collisions are **perfectly elastic** and lose no energy.
5. The **average kinetic energy of the molecules is proportional to the kelvin temperature**.

An **ideal gas** is a hypothetical gas that satisfies these postulates exactly. Real gases approximate it at **low pressure, high temperature, and low density**; at higher pressure or lower temperature, molecular volume and intermolecular forces can no longer be ignored.

Microscopic quantities:

- `N`: number of molecules; `N/V`: number density (not the amount of substance `n`)
- `m`: mass of one molecule; `M`: molar mass
- `u`: molecular speed; `u_rms = √(⟨u²⟩)`: root-mean-square speed
- `k_B = 1.380649×10⁻²³ J/K`: Boltzmann constant
- `R = N_A k_B = 8.314 J mol⁻¹ K⁻¹`: molar gas constant

### Why pressure is `p = (1/3)(N/V)m u_rms²`

Take a cubic box of side `L` containing `N` molecules of mass `m`. Consider one molecule with velocity component `u_x` along `x`.

- It collides elastically with the wall perpendicular to `x`: `u_x → −u_x`, so the magnitude of the momentum change is `2m u_x`.
- Between two successive collisions with the same wall it travels `2L`, so the time interval is `Δt = 2L/u_x`.
- Its average force on the wall is `F_1 = Δp/Δt = (2m u_x)/(2L/u_x) = m u_x²/L`.
- Summing over `N` molecules: `F = (m/L) Σ u_x²`.
- Molecular motion is isotropic: `⟨u_x²⟩ = (1/3)⟨u²⟩ = (1/3)u_rms²`.
- Therefore `F = (N m/(3L)) u_rms²`, and the pressure is

`p = F/L² = (1/3)(N/L³)m u_rms² = (1/3)(N/V)m u_rms²`

Substituting `⟨KE_trans⟩ = ½m u_rms²`:

`p = (2/3)(N/V)⟨KE_trans⟩`

Comparing with the ideal-gas equation `pV = N k_B T` (that is, `p = (N/V)k_B T`) gives

`⟨KE_trans⟩ = (3/2)k_B T`

For one mole:

`KE_avg = (3/2)RT`

and

`u_rms = √(3RT/M) = √(3k_B T/m)`

The derivation uses a cubic box, but the result is independent of the box shape; what it really assumes is **elastic collisions, no intermolecular forces, an isotropic velocity distribution, and a very large number of molecules**. **It is not a proof about real gases; it is a derivation inside the ideal-gas model.**

### Speed distribution: not every molecule moves at the same speed

The textbook gives the Maxwell-Boltzmann distribution: at a fixed temperature, molecular speeds are spread over a range; raising the temperature shifts the distribution to the right and broadens it; at the same temperature, lighter molecules have a larger `u_rms` and a peak further to the right.

From the Maxwell-Boltzmann distribution (added here; the textbook gives only the qualitative picture) one obtains three different "average" speeds:

- most probable speed: `u_p = √(2RT/M)`
- mean speed: `u_mean = √(8RT/(πM))`
- root-mean-square speed: `u_rms = √(3RT/M)`

They satisfy `u_p < u_mean < u_rms`. A high-school problem that says "average speed" usually means `u_mean`; if it gives kinetic energy, it means `u_rms`. **The three numbers are not interchangeable.**

> [!IMPORTANT]
> **"Same average translational kinetic energy at the same temperature" does not mean "every molecule has the same speed," nor "the total internal energy is the same."**
>
> For an ideal gas, `⟨KE_trans⟩ = (3/2)k_B T` concerns **translation** only. A diatomic molecule at room temperature also has two rotational degrees of freedom, each contributing `½k_B T` on average; its **total average energy** is therefore about `(5/2)k_B T`, larger than that of a monatomic molecule. Its **average translational kinetic energy** is still the same.
>
> The textbook writes `At a given temperature, all gases have the same KE_avg for their molecules`. Without the qualifier "translational," this reads as "all gases have the same total internal energy." This entry restores the qualifier.

> [!WARNING]
> **None of the five KMT postulates holds exactly for real gases.**
>
> Molecules have finite volume (postulate 2 fails); they exert dispersion, dipole, and hydrogen-bond forces (postulate 4 fails); collisions can be inelastic in rare cases (for example, by exciting rotation or vibration). KMT is valuable because at low pressure, high temperature, and low density these deviations are negligible, and the model unifies pressure, temperature, diffusion, and the gas laws with very few assumptions.
>
> **Do not confuse "the model explains" with "the model is true."** A model can be extremely useful and still wrong somewhere.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Temperature and temperature scales](temperature-and-scales.en.md) — postulate 5 uses kelvin temperature; Celsius cannot enter `⟨KE⟩ = (3/2)k_BT` directly |
| Prerequisite | [Gas laws and the ideal-gas equation](gas-laws-and-ideal-gas-equation.en.md) — the empirical regularities KMT is meant to explain; `pV = nRT` is the model's macroscopic counterpart |
| Follow-up | Solids and liquids (not yet built in this library) — drops "no intermolecular forces" and discusses intermolecular forces and condensed phases |
| Follow-up | [Second law of thermodynamics](../../knowledge/physics/concepts/thermodynamic-second-law.en.md) — the microscopic basis of macroscopic irreversibility |
| Follow-up | [Statistical interpretation of entropy](../../knowledge/physics/concepts/statistical-interpretation-of-entropy.en.md) — microstate counting, Boltzmann entropy, and temperature |
| Recorded gap | **The van der Waals equation and compressibility factor for real gases**, **mean free path and transport coefficients (diffusion, thermal conductivity, viscosity)**, **full equipartition of rotational/vibrational degrees of freedom**, **quantum degenerate gases**, and **plasmas** are not built; this entry stops at the ideal-gas model |

## Argument

### K1 · Pressure is the macroscopic face of molecules colliding with the walls (no attack yet)

- **Claim**: `p = (1/3)(N/V)m u_rms² = (2/3)(N/V)⟨KE_trans⟩`
- **Premise**: postulate 3 says pressure results from molecular collisions with the walls; postulate 1 says molecules are in continuous motion; postulate 4 says collisions are perfectly elastic (ev-197)
- **Reasoning**: an elastic collision with the wall changes the molecule's momentum by `2m u_x`; the time between collisions with the same wall is `2L/u_x`; the average force is `m u_x²/L`. Summing over `N` molecules and using isotropy `⟨u_x²⟩ = u_rms²/3` gives `p = (1/3)(N/V)m u_rms²`. Substituting `⟨KE_trans⟩ = ½m u_rms²` gives `p = (2/3)(N/V)⟨KE_trans⟩`
- **Evidence**: ev-197
- **Attacked**: the textbook gives only a verbal explanation and does not supply this derivation. It says the postulates `may be applied in a more quantitative fashion to derive these individual laws`, but the body explains the five gas laws only qualitatively; the only actual derivations are `u_rms` and Graham's law. This entry supplies the derivation and states its four assumptions: cubic box, elastic collisions, no interactions, and isotropy
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

### K2 · At the same temperature the average translational kinetic energy is the same, and `u_rms` scales as `√(1/M)` (no attack yet)

- **Claim**: `⟨KE_trans⟩ = (3/2)k_BT`; `u_rms = √(3RT/M)`; at the same temperature, lighter molecules have a larger `u_rms`
- **Premise**: the textbook gives `KE_avg = (3/2)RT` and `u_rms = √(3RT/M)`, with worked examples for `N₂` at `30 °C` and `O₂` at `−23 °C` (ev-197)
- **Reasoning**: solving `½m u_rms² = (3/2)k_BT` gives `u_rms`. For two gases at the same temperature, `u_rms1/u_rms2 = √(M₂/M₁)`. Recomputing: for `N₂`, `M = 0.02802 kg/mol`, `T = 303.15 K`, `u_rms = √(3×8.314×303.15/0.02802) = 519.5 m/s`; for `O₂`, `M = 0.03200 kg/mol`, `T = 250.15 K`, `u_rms = 441.4 m/s`. At `300 K`, the average translational kinetic energy per mole is `(3/2)×8.314×300 = 3.742 kJ/mol`, or `6.213×10⁻²¹ J` per molecule
- **Evidence**: ev-197
- **Attacked**: one textbook exercise answer says `The root mean square speed increases to 2 times its initial value; u_rms is proportional to KE_avg`. That is wrong: when the temperature doubles, `u_rms ∝ √T`, so it becomes `√2` times the initial value; `u_rms ∝ √(KE_avg)`, not proportional to `KE_avg`. The same module's Key Equations give `u_rms = √(3RT/M)`, contradicting that answer. This entry recomputes from the formula and records the answer as a source defect
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

### K3 · KMT is a model, not a proof of the gas laws (no attack yet)

- **Claim**: KMT explains the gas laws, but its postulates fail for real gases; the gas laws are empirical, and KMT is a model with a domain of validity
- **Premise**: the textbook itself says the gas laws `are empirical`, calls KMT `a simple microscopic model`, says `The test of the KMT and its postulates is its ability to explain and describe the behavior of a gas`, and limits the gas laws to `pressures less than about 1 or 2 atm` (ev-197)
- **Reasoning**: postulate 2 (no molecular volume) and postulate 4 (no intermolecular forces) fail at high pressure or low temperature; real gases have finite molecular volume and attraction, so `pV = nRT` is only a limiting law. KMT's success is a success of **explanation and unification**: one set of assumptions covers pressure, temperature, diffusion, and the gas laws. But "explains known regularities" is weaker than "predicts new phenomena"; explanatory power is not proof
- **Evidence**: ev-197
- **Attacked**: the textbook says the test of KMT is whether it can explain gas behaviour, which is not a falsifiable criterion — any sufficiently flexible model can explain known regularities after the fact. The textbook also claims the gas laws can be derived from the postulates, but the body gives only qualitative explanations. This entry separates "explanatory power" from "strength of evidence" and writes the model's limits into `scope.条件`
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

### K4 · Temperature fixes the speed distribution, not the speed of each molecule (no attack yet)

- **Claim**: at a fixed temperature a gas has a distribution of molecular speeds; raising the temperature shifts and broadens the distribution, but an individual molecule can still speed up or slow down in collisions
- **Premise**: the textbook gives the Maxwell-Boltzmann distribution and, in an exercise answer, writes `Any single molecule can speed up or slow down as it collides with other molecules. The average speed of all the molecules is constant at constant temperature.` (ev-197)
- **Reasoning**: temperature fixes the average energy of the distribution, not the energy of each molecule. Collisions redistribute energy among molecules; one molecule can be knocked from a low speed to a high speed and back. Macroscopically `u_rms`, `u_mean`, and `u_p` are stable; microscopically individual speeds change constantly
- **Evidence**: ev-197
- **Attacked**: the textbook sometimes uses "average speed" and `u_rms` interchangeably in the body and distinguishes them only at the formulas. For a broad distribution the three speeds can differ by about 10% (`u_rms/u_mean = √(3π/8) ≈ 1.085`); treating them as one number introduces a systematic error. This entry keeps them distinct and notes that the textbook gives no formulas for `u_p` and `u_mean`
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-11-05 | Entry created; supplies the core model of chapter 1 of elective-3, "kinetic-molecular theory", after temperature and the gas laws | written after reading m68758 in full (ev-197); the `u_rms` values for `N₂`/`O₂`, `3.742 kJ/mol`, and `6.213×10⁻²¹ J` are recomputed here | AI (DeepSeek V4.1 Flash Free) |
