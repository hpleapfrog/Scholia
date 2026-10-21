---
id: kb:physics:radioactive-decay
type: 知识点
title: "Radioactive decay"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Atomic nucleus" and need to write the three decay equations and use half-life in estimates
  条件: covers alpha, beta-minus, and gamma decay, conservation laws, and half-life only; beta-plus, electron capture, and the antineutrino distinction are out of scope, and binding energy, fission/fusion, and medical applications have their own entries
edges:
  先修: ["[Atomic nucleus](atomic-nucleus.en.md)"]
  支持: []
  攻击: []
evidence: [ev-158, ev-159]
license: CC-BY-SA-4.0
---

> **English version of [`放射性衰变.md`](放射性衰变.md).**

> [!TIP]
> **After reading this entry you should** be able to write the alpha / beta / gamma decay equations, check them with conservation of mass number and charge, and estimate the number of nuclei left from a half-life

## Definition

**Radioactive decay** is the alteration of a nucleus through the emission of particles or energy; a substance that undergoes it is radioactive. The textbook calls the emission itself radioactivity and the alteration of nuclear structure radioactive decay.

| Type | Emits | `A` | `Z` | Equation | Typical range |
|---|---|---|---|---|---|
| **α** | alpha particle (2 protons + 2 neutrons, a He-4 nucleus) | −4 | −2 | `^{A}_{Z}X → ^{A−4}_{Z−2}Y + ^{4}_{2}He` | a sheet of paper / a few cm of air |
| **β⁻** | electron + neutrino | unchanged | +1 | `^{A}_{Z}X → ^{A}_{Z+1}Y + e + ν` | a thin aluminum plate / tens of cm of tissue |
| **γ** | photon | unchanged | unchanged | `^{A}_{Z}X* → ^{A}_{Z}X + γ` | several cm of lead / meters of concrete |

- **conservation**: mass number and charge are conserved in all three decays. For alpha decay the textbook says `The mass number of the new element and the alpha particle together equal the mass number of the original element. Also, the net charge of all particles involved remains the same before and after the transmutation.`; for beta decay it says `the mass number and charge in all beta-decay reactions are conserved`
- **what beta decay is**: a neutron turns into a proton, an electron, and a neutrino (or the reverse); for β⁻, `A` is unchanged and `Z` increases by 1
- **gamma decay**: an excited nucleus drops to the ground state and emits a photon; `A` and `Z` are both unchanged — this is a change of energy state, not of element
- **half-life** `t½`: the time for the number of original nuclei to halve. Each half-life halves what remains:
  `N = N0 (1/2)^(t/t½) = N0 e^(−λt)`, with `λ = ln2 / t½ ≈ 0.693 / t½`
- **activity** `R = ΔN/Δt = λN`; unit Bq (one decay per second), and `1 Ci = 3.70×10^10 Bq`
- carbon-14 has a half-life of 5,730 years and is used for radiometric dating

> [!IMPORTANT]
> **A half-life is not a countdown for each nucleus.**
>
> The textbook says `Nuclear decay is an example of a purely statistical process.`
> Each nucleus has a 50 percent chance of surviving one half-life;
> `Even if it happens to survive hundreds of half-lives, it still has a 50 percent chance of surviving through one more.`
> Therefore:
>
> - after two half-lives about **1/4** remains, not zero;
> - a nucleus that has "been around" for a long time is not more eager to decay;
> - a half-life is a statistical law for a **large number** of nuclei; a single nucleus has no definite lifetime.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Atomic nucleus](atomic-nucleus.en.md) — knowing that the nucleus is made of protons and neutrons is what makes the changes in `A` and `Z` readable |
| Related | [Binding energy and mass defect](binding-energy-and-mass-defect.en.md) — the energy released in alpha decay is the mass difference between parent and daughter; the β+ electron bookkeeping is still missing |
| Related | [Ionizing radiation in medicine](ionizing-radiation-in-medicine.en.md) — PET uses the two `0.511 MeV` photons from β⁺ annihilation; the full β⁺ equation and energy accounting are still missing |
| Recorded gap | **the full β⁺ decay equation and energy accounting**, **electron capture**, **the antineutrino distinction** are not built in this repo |

## Argument

### K1 · The three decays are told apart by what is conserved and what changes (no attack yet)

- **Claim**: the three decays are not three isolated facts; all conserve mass number and charge, and differ only in how they change `A` and `Z`
- **Premise**: the textbook gives the three decay equations and states that in alpha decay the mass numbers of the new element and the alpha particle add up to the parent's mass number and the net charge is unchanged; for beta decay it states `the mass number and charge in all beta-decay reactions are conserved` (ev-158)
- **Reasoning**:
  1. alpha: two protons + two neutrons leave → `A − 4`, `Z − 2`; the new element moves two places down the periodic table (uranium → thorium), which the textbook calls transmutation
  2. β⁻: a neutron → proton + electron + neutrino → `A` unchanged, `Z + 1`; the nucleus gains one positive charge and the emitted electron carries −1, so charge balances
  3. gamma: excited nucleus → ground state + photon → both `A` and `Z` unchanged; only the energy state changes
  4. conservation lets you recover an unknown nucleus: in the textbook's Cs-137 → Ba-137 example, the daughter's `Z = 56` fixes the parent's `Z = 55`
- **Evidence**: ev-158
- **Attacked**: the textbook writes the beta products as `e + ν` and does not distinguish the antineutrino; for β⁺ it says only `may also emit a positron` and gives no equation. This entry covers β⁻ only; the full β⁺ equation and threshold are still missing ([ionizing radiation in medicine](ionizing-radiation-in-medicine.en.md) uses only the annihilation photons), and the antineutrino is not distinguished either. Also, the alpha-decay energy example substitutes `Δm = 0.0005631 u` as `0.005631 u`, a factor of 10; this entry does not use that number
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · The half-life is a statistical law, not the lifetime of one nucleus (no attack yet)

- **Claim**: the half-life describes the statistics of a large number of nuclei; a single nucleus decays at a random time, and the surviving fraction falls as `1/2^n` without reaching exactly zero
- **Premise**: the textbook defines the half-life as the time for half the original nuclei to decay, calls nuclear decay `a purely statistical process`, and says each nucleus still has a 50 percent chance of surviving the next half-life; it gives `N = N0 e^(−λt)`, `λ = ln2 / t½`, and activity `R = λN` (ev-159)
- **Reasoning**: the exponential law is the expected behaviour of a large sample; the textbook compares it to coin flipping and stresses that no matter what happened before, the next half-life is still 50 percent — decay has no memory. Activity `R = λN` falls as `N` falls, so the "radioactivity" of a sample is not constant either. Carbon-14 dating uses exactly this: after an organism dies it stops taking in C-14, and the remaining fraction falls with the half-life
- **Evidence**: ev-159
- **Attacked**: the textbook does not discuss statistical fluctuations in small samples — `N = N0 e^(−λt)` is an expectation, and with very few nuclei the actual number left will deviate; nor does it explain why a single nucleus decays randomly, treating it only as a statistical fact. This entry does not supply a quantum explanation on the textbook's behalf
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; second node of the 选必三 "atomic nucleus" chapter, following "atomic nucleus" and placing the three decays and the half-life under one statistical law | written after reading m54580 and m63183 in full (ev-158/ev-159) | @hpleapfrog |
| 2026-10-21 | Backfilled after "Binding energy and mass defect" and "Nuclear fission and fusion" were built: one related relation added and both items removed from the gap table | new this round: ev-185/ev-186 | @hpleapfrog |
| 2026-10-21 | Backfilled after "Ionizing radiation in medicine" was built: one related relation added; "medical applications" removed from the gap table, and the β⁺ gap reworded as "full equation and energy accounting" | new this round: ev-187/ev-188/ev-189 | @hpleapfrog |
