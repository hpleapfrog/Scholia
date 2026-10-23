---
id: kb:physics:atomic-nucleus
type: 知识点
title: "Atomic nucleus"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Atomic structure" and need to separate Z / A / isotopes and see why the nucleus does not fly apart
  条件: covers the composition of the nucleus, nuclide notation, isotopes, and the strong nuclear force only; radioactive decay, binding energy and mass defect, and nuclear fission and fusion are separate entries
edges:
  先修: ["[Atomic structure](atomic-structure.en.md)"]
  支持: []
  攻击: []
evidence: [ev-158]
license: CC-BY-SA-4.0
---

> **English version of [`原子核.md`](原子核.md).**

> [!TIP]
> **After reading this entry you should** be able to write nuclide notation, separate `Z` / `A` / `N`, and use the balance between the strong nuclear force and the electromagnetic force to explain why the nucleus does not fly apart

## Definition

The **atomic nucleus** consists of protons and neutrons; the two are collectively called **nucleons**.

- the proton number `Z` is the **atomic number** and fixes the element: `Z = 6` is always carbon
- the neutron number `N`
- the **mass number** `A = Z + N`, the total number of nucleons (a count, not a mass)
- **nuclide notation**: `^{A}_{Z}X`, where `X` is the element symbol. The three hydrogen isotopes are `^{1}_{1}H`, `^{2}_{1}H`, and `^{3}_{1}H`
- **isotopes**: same `Z`, different `N`. The three hydrogens have nearly identical chemistry, but their nuclei differ greatly in mass and stability
- nuclear radius `r = r0 A^(1/3)` with `r0 = 1.2 fm`; the volume is proportional to `A`, which means the nucleons are tightly packed with almost no empty space
- the **strong nuclear force**: short range, attractive between **any two nucleons**, about 100 times stronger than the electromagnetic force at close range; the electromagnetic repulsion between protons is long range. A stable nucleus balances the two; with too many protons the electromagnetic force wins and the nucleus recovers balance through alpha decay

> [!IMPORTANT]
> **The mass number `A` is not a mass.**
>
> `A` is only the **number** of protons and neutrons — a dimensionless count. Atomic mass is a different quantity. The textbook's example:
> oxygen has mass number `A = 16`, but its atomic mass is `15.994915 u`. The two are close in most calculations,
> but they must not be mixed up in nuclear energy calculations.
>
> Also, isotopes have nearly identical chemistry while their nuclear stability can differ completely:
> `The three varieties of hydrogen have nearly identical chemistries, but the nuclei differ greatly in mass, stability, and other characteristics.`

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Atomic structure](atomic-structure.en.md) — the gold-foil experiment gives "the nucleus is tiny and dense"; this entry asks what the nucleus is made of and why it is stable |
| Follow-up | [Radioactive decay](radioactive-decay.en.md) — when the balance between the strong force and the electromagnetic force breaks, the nucleus decays to restore it |
| Follow-up | [Binding energy and mass defect](binding-energy-and-mass-defect.en.md) — the nucleus is lighter than its constituent nucleons, and the difference is the binding energy; the `BE/A` curve peaks near iron |
| Follow-up | [Nuclear fission and fusion](nuclear-fission-and-fusion.en.md) — heavy-nucleus fission and light-nucleus fusion both move toward the `BE/A` peak and therefore release energy |
| Recorded gap | **quarks and the Standard Model** are not built in this repo |

## Argument

### K1 · Why the nucleus does not fly apart from proton repulsion (no attack yet)

- **Claim**: a stable nucleus requires a short-range attractive strong nuclear force balanced against long-range electromagnetic repulsion
- **Premise**: the textbook notes that protons are all positive and should repel one another, and states `This force is known as the strong nuclear force`; its comparison table gives the strong force as `Very short range, essentially zero at 1 femtometer`, `Attractive`, `Attraction between any two nucleons`, and `100 times greater than the electromagnetic force`; it also says `The balancing of the electromagnetic force with the nuclear forces is what allows the nucleus to maintain its spherical shape.` (ev-158)
- **Reasoning**: the electromagnetic force acts only between protons and over a long range; the strong force acts between any two nucleons and is effective within about 1 fm. Adding neutrons adds attraction without adding repulsion, so heavy nuclei need more neutrons; with too many protons the electromagnetic force overcomes the strong force, and the nucleus sheds two protons and two neutrons through alpha decay. The textbook uses the alpha decay of uranium as the example
- **Evidence**: ev-158
- **Attacked**: the module's prose gives the strong-force range as `10–15 meters` — dimensionally wrong (it should be 10⁻¹⁵ m), while the same section's table says `essentially zero at 1 femtometer`. This entry follows 1 fm and records the source defect here. Also, "100 times" is an order-of-magnitude comparison at close range, not a statement that holds at every distance
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Isotopes: Z fixes the element, N fixes the nucleus (no attack yet)

- **Claim**: chemistry is dominated by `Z`; mass and nuclear stability depend on `N` as well
- **Premise**: the textbook defines an isotope as a variation in the number of neutrons, and says the three hydrogens `have nearly identical chemistries, but the nuclei differ greatly in mass, stability, and other characteristics`; its teaching note adds `the number of electrons is irrelevant to discussions of mass number, atomic number, and isotopes` (ev-158)
- **Reasoning**: chemistry is set by the electron arrangement, and the electron number is fixed by `Z`; neutrons carry no charge, so they do not change the chemistry, but they do change the nuclear mass and the balance between the strong force and the electromagnetic force. Hence `^{1}H` and `^{2}H` are stable while `^{3}H` (tritium) is radioactive; C-12 and C-13 are stable while C-14 is radioactive
- **Evidence**: ev-158
- **Attacked**: "Z fixes the element, N fixes the nucleus" is this repo's summary; the textbook gives the definition of `Z`, the definition of isotopes, and the three-hydrogen example, but does not state that sentence. It also does not discuss the small chemical differences between isotopes, saying only "nearly identical"
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 选必三 "atomic nucleus" chapter, attached after "atomic structure" | written after reading m54580 in full (ev-158) | @hpleapfrog |
| 2026-10-21 | Backfilled after "Binding energy and mass defect" and "Nuclear fission and fusion" were built: two follow-up relations added and both items removed from the gap table | new this round: ev-185/ev-186 | @hpleapfrog |
