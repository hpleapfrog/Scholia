---
id: kb:physics:binding-energy-and-mass-defect
type: 知识点
title: "Binding energy and mass defect"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "atomic nucleus" and need to understand how `E = mc²` turns a mass difference into nuclear energy
  条件: covers binding energy, mass defect, the `BE/A` curve, and the iron peak; β+ atomic-mass corrections, the nuclear shell model, semi-empirical mass formulas, and systematic nuclear-reaction Q-value calculations are out of scope
edges:
  先修: ["[Atomic nucleus](atomic-nucleus.en.md)"]
  支持: []
  攻击: []
evidence: [ev-185, ev-186]
license: CC-BY-SA-4.0
---

> **English version of [`结合能与质量亏损.md`](结合能与质量亏损.md).**

> [!TIP]
> **After reading this entry you should** be able to convert a mass defect `Δm` into a binding energy `BE` (`1 u = 931.5 MeV/c²`), explain why the `BE/A` curve peaks near iron, and state clearly why "mass defect" does not mean that mass vanishes

## Definition

### Binding energy: the energy needed to take a nucleus apart

The **binding energy** (BE) of a nucleus is the energy required to completely disassemble it into separate protons and neutrons; conversely, assembling those nucleons from far apart releases the same amount of energy (ev-186).

- Pulling the nucleus apart does positive work on the system; with the separated nucleons at rest, their total rest mass is larger than before by `BE/c²`
- A bound system is therefore **lighter** than its parts: the more it is lighter, the more tightly it is bound
- Binding energy is not "a store of energy inside the nucleus"; it is a measure of **how much energy must be paid to take the nucleus apart**
- More nucleons means a larger BE; to compare how tightly different nuclei are bound, divide by the nucleon number to get the **binding energy per nucleon**, `BE/A`

### Mass defect and `E = mc²`

For a nucleus with `Z` protons and `N` neutrons and nuclear mass `m_nucleus`:

`Δm = (Z m_p + N m_n) − m_nucleus`

`BE = Δm c²`

`Δm` is the **mass defect**. It is more convenient to use neutral atomic masses (ev-186):

`BE = {[Z m(1H) + N m_n] − m(^{A}_{Z}X)} c²`

- `m(1H)` is the mass of a hydrogen **atom** and `m(^{A}_{Z}X)` is the **atomic** mass of the neutral atom
- Both sides contain `Z` electrons, so the electron masses cancel; the electrons' own binding energy is of order eV, far below the MeV scale of nuclear binding, and is neglected
- Conversion: `1 u = 931.5 MeV/c²`, so `BE[MeV] = Δm[u] × 931.5`

The textbook's alpha-particle example (ev-186, recomputed here):

| Quantity | Value |
|---|---|
| `m(4He)` | `4.002602 u` |
| `m(1H)` | `1.007825 u` |
| `m_n` | `1.008665 u` |
| `Δm = 2m(1H) + 2m_n − m(4He)` | `0.030378 u` |
| `BE = Δm × 931.5` | `28.30 MeV` (the textbook gives `28.3 MeV`) |
| `BE/A = BE/4` | `7.07 MeV/nucleon` |

### The `BE/A` curve and the iron peak

`BE/A` is not constant. The curve given in the textbook (ev-186):

- averages about `8 MeV/nucleon`
- reaches its maximum near `A ≈ 60` (around iron)
- is lower at both the light and the heavy ends
- has several spikes at magic-number nuclei (such as the especially tight `4He`, `12C`, and `56Fe`)

The textbook's explanation (ev-186): the strong nuclear force is a **short-range** attraction while the Coulomb force is a **long-range** repulsion.

- In a light nucleus, each added nucleon can attract almost every other nucleon, so `BE/A` rises with `A`
- In a heavy nucleus, an added nucleon attracts only its neighbours, while an added proton feels the Coulomb repulsion of **all** protons; the attraction saturates while the repulsion keeps accumulating, so `BE/A` falls again
- This is why stable nuclei above `A > 40` have more neutrons than protons: an extra neutron adds attraction without adding repulsion

A few readings from the textbook exercises (ev-186): `2H` is `1.112 MeV/nucleon`, `12C` `7.680`, `14C` `7.520`, and `209Bi` `7.848`. These agree with the curve.

> [!IMPORTANT]
> **Mass defect does not mean that mass vanishes.**
>
> Taking a bound system apart converts the work done by the external force into the rest mass of the separated nucleons; conversely, when nucleons bind, the system emits part of its rest mass as kinetic energy, photons, and so on. If the emitted energy is kept in the same box, the box's total mass–energy is still conserved. What is "defective" is the **rest mass of the bound system**, not a piece of mass missing from the universe.
>
> Also, "the larger `BE/A`, the more stable" is an empirical rule of thumb, not a sufficient condition. Whether a nucleus can decay also depends on its mass difference to the **actual daughter**, on angular momentum, and on selection rules; `BE/A` only tells you how tightly it is bound.

> [!NOTE]
> **Source issues and what this library supplies** (ev-185/ev-186)
>
> 1. The Section Summary of m42640 says `The larger the BE/A, the more stable the nucleus`, reducing stability to a single index; this entry demotes it to a rule of thumb and states the boundary in the IMPORTANT block above.
> 2. m42640 says "the most common elements have the most tightly bound nuclei", but the most abundant element is hydrogen, whose nucleus is a single proton and has no binding energy for "separating protons and neutrons". The sentence is an overgeneralization.
> 3. The problem-solving strategy of m42640 says to adjust "0.511 MeV per electron" when using atomic masses in β+, without explaining that β+ involves **two** electrons (the emitted positron and the lost orbital electron); the atomic-mass calculation needs `1.022 MeV`. This entry does not use that sentence and records it as a gap.
> 4. The Section Summary of m54574 explains fusion energy as "the combined nuclei are closer together, resulting in a decreased strong nuclear force", contradicting the same module's body text ("the products have a larger `BE/A` and less mass per nucleon"); this library follows the body text and the `BE/A` curve, as detailed in [Nuclear fission and fusion](nuclear-fission-and-fusion.en.md).
>
> **Supplied here, not in the textbook**: the reaction-energy ledger `Q = ΔBE`, the comparison table of `BE/A` readings, and the statement that "mass defect is not disappearing mass". The textbook gives `BE = Δm c²`, the alpha-particle example, and a qualitative explanation of the `BE/A` curve, but does not write "energy release = increase in total binding energy" as a rule.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Atomic nucleus](atomic-nucleus.en.md) — `Z`, `A`, nuclide notation, and "a nucleus is made of protons and neutrons" are needed before writing `Δm` |
| Follow-up | [Nuclear fission and fusion](nuclear-fission-and-fusion.en.md) — the two sides of the iron peak release energy by fission and fusion; the `200 MeV` per fission and the Sun's `26.7 MeV` p-p chain are both `Δm c²` |
| Related | [Radioactive decay](radioactive-decay.en.md) — the energy released in alpha decay is also the mass difference between parent and daughter; the β+ electron bookkeeping is not covered here |
| Recorded gap | **quantitative shell model and magic numbers**, **semi-empirical mass formula (Bethe–Weizsäcker)**, **systematic nuclear-reaction Q-value calculations**, **β+/electron-capture atomic-mass corrections**, and **nucleosynthesis and elemental abundances** are not built |

## Argument

### K1 · Binding energy is the mass defect times `c²` (no attack yet)

- **Claim**: `BE = Δm c²`; with neutral atomic masses, `BE = {[Z m(1H) + N m_n] − m(^{A}_{Z}X)} c²`; the alpha particle's `0.030378 u` corresponds to `28.30 MeV`
- **Premises**: the textbook defines BE as "the energy required to completely disassemble the nucleus into separate protons and neutrons", says a bound system has less mass than its parts, gives `Δm=BE/c²`, the nuclear-mass and atomic-mass formulas, and `1 u = 931.5 MeV/c²`; the alpha example gives `4.002602 u`, `1.007825 u`, `1.008665 u`, `0.030378 u`, `28.3 MeV`, and `7.07 MeV/nucleon` (ev-186)
- **Reasoning**: pulling the nucleus apart puts work `BE` into the system, so the separated nucleons have a total rest mass larger by `BE/c²`; conversely, binding reduces the total rest mass by `Δm`, and that mass leaves as energy. With neutral atomic masses, both sides contain `Z` electrons, so the electron masses cancel; the remaining electron binding energy is of order eV and negligible against MeV-scale nuclear binding. Multiplying `Δm = 0.030378 u` by `931.5 MeV/u` gives `28.297 MeV`, i.e. `28.3 MeV` to three significant figures; dividing by `A = 4` gives `7.07 MeV/nucleon`
- **Evidence**: ev-186
- **Attacked**: **the textbook does not derive `E = mc²`, nor does it discuss how the "energy carries away equivalent mass" is booked in a closed system**; it uses `E = mc²` as a known relation. The atomic-mass formula also neglects electron binding energy (the textbook's own exercise computes the hydrogen electron's binding energy as `13.6 eV`, about `2.66×10^-5` of the electron rest mass `0.511 MeV`); this is an excellent approximation, not an exact equality
- **By**: @hpleapfrog · 2026-10-21

### K2 · `BE/A` peaks near iron, and light nuclei release energy by fusion while heavy nuclei release it by fission (the quantitative comparison across the peak is supplied here)

- **Claim**: `BE/A` is highest near `A ≈ 60`; nuclei below the peak release energy by fusion, nuclei above it by fission; the energy released in a reaction equals the total binding energy of the products minus that of the reactants
- **Premises**: the textbook says `BE/A` averages about `8 MeV`, is largest near `A ≈ 60` (around iron), and is lower at both ends, and explains this with the short-range strong force and the long-range Coulomb force; another module says light nuclei release energy by fusion and heavy nuclei by fission, with iron as the boundary, and that fusion products have a larger `BE/A` (ev-185/ev-186)
- **Reasoning**: the reaction energy is `Q = BE_products − BE_reactants = −(m_products − m_reactants)c²`. A larger total binding energy for the products means a smaller total rest mass, and the difference is released. For light nuclei with `A < 60`, fusion moves nucleons toward the peak and `Q > 0`; for heavy nuclei with `A > 60`, fission moves them toward the peak and `Q > 0`. The textbook's `200 MeV` per fission divided by `236` nucleons gives about `0.85 MeV/nucleon`, the same order as the rise from `235U` (about `7.6 MeV/nucleon`) to the fission products (about `8.4–8.5 MeV/nucleon`) on the curve; the Sun's `26.7 MeV` p-p chain divided by four protons gives `6.675 MeV/nucleon`, also on the rising, light-nucleus side
- **Evidence**: ev-185, ev-186
- **Attacked**: **the textbook gives only the qualitative shape of the `BE/A` curve, not precise `BE/A` readings for `235U` and its fission products, and it does not state `Q = ΔBE` as a rule**; the values `7.6` and `8.4–8.5` above are approximate readings from common `BE/A` data, not textbook text. The "iron peak" is itself approximate: the maximum usually lies among `62Ni`, `58Fe`, and `56Fe` near `A ≈ 60`, not exactly at iron
- **By**: @hpleapfrog · 2026-10-21

### K3 · Stable heavy nuclei need more neutrons, a geometric consequence of short-range attraction and long-range repulsion (no attack yet)

- **Claim**: stable nuclei above `A > 40` have more neutrons than protons because Coulomb repulsion accumulates with proton number while nuclear attraction saturates at short range
- **Premises**: the textbook says stable nuclei above `A ≈ 40` have more neutrons than protons, and explains the fall of `BE/A` in heavy nuclei by the Coulomb repulsion of every added proton against the fact that nuclear attraction acts only on nearby nucleons (ev-186)
- **Reasoning**: Coulomb repulsion grows roughly as `Z²` (every pair of protons repels), while nuclear attraction grows roughly with `A` but saturates as the nucleus grows (each nucleon attracts only its neighbours). Adding a neutron increases `A` without increasing `Z`, so it raises the total attraction without raising the total repulsion; heavy nuclei therefore need `N > Z` to be stable, and the textbook notes that the effect becomes more pronounced for the heaviest nuclei
- **Evidence**: ev-186
- **Attacked**: the textbook gives no quantitative `N/Z` curve and does not discuss pairing, shell effects, or unstable nuclei; "`A > 40`" is a rough boundary, not a sharp threshold. The actual `N/Z` distribution of stable nuclei also requires the shell model and the β-stability line
- **By**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the binding-energy gap in Elective-3 "atomic nucleus", follows "Atomic nucleus", and serves as the prerequisite for "Nuclear fission and fusion" | written after reading m54574/m42640 in full (ev-185/ev-186) | @hpleapfrog |
