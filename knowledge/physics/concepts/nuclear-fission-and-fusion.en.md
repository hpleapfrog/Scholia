---
id: kb:physics:nuclear-fission-and-fusion
type: 知识点
title: "Nuclear fission and fusion"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "binding energy and mass defect" and need to understand why fission and fusion both release energy, what a chain reaction and critical mass are, and how the Sun shines
  条件: covers the liquid-drop model, chain reactions and critical mass, the `E = mc²` energy ledger, the `BE/A` iron peak, the proton–proton chain, and the qualitative principles of pressurised water reactors and tokamaks; reactor neutron kinetics, fission-product decay heat, breeder reactors, inertial confinement fusion, quantitative plasma confinement, and nuclear-weapon design are out of scope
edges:
  先修: ["[Binding energy and mass defect](binding-energy-and-mass-defect.en.md)", "[Atomic nucleus](atomic-nucleus.en.md)"]
  支持: []
  攻击: []
evidence: [ev-185, ev-186]
license: CC-BY-SA-4.0
---

> **English version of [`核裂变与核聚变.md`](核裂变与核聚变.md).**

> [!TIP]
> **After reading this entry you should** be able to explain why fission and fusion both release energy (the two sides of the iron peak), what a chain reaction and critical mass mean, how `200 MeV` per fission and the Sun's `26.7 MeV` p-p chain follow from a mass difference, and why fusion requires the nuclei to overcome the Coulomb barrier

## Definition

### Fission: a heavy nucleus split by a neutron

**Nuclear fission** is the splitting of a heavy nucleus into two medium-mass nuclei. The textbook describes neutron-induced fission with the **liquid-drop model** (ev-185):

1. A neutron is absorbed by the heavy nucleus, which is left excited
2. The nucleus elongates like a struck drop of liquid; as it stretches, the nucleons are no longer tightly packed, the **short-range strong force** weakens, and the **long-range Coulomb repulsion** wins
3. The nucleus breaks in the middle into two medium-mass nuclei, releasing several neutrons and energy

- Neutrons released by fission can induce further fissions, producing a **chain reaction**: `1 → 2 → 4 → 8 → …` (the textbook's example)
- The minimum mass that can sustain a self-sustaining chain reaction is the **critical mass**. It depends on the nuclide, the geometry, and whether a neutron reflector surrounds the fuel; `235U` and `239Pu` fission more easily than the far more abundant `238U`, and `239Pu` has the smallest critical mass (ev-185)
- A reactor uses a **moderator** (water) to slow the neutrons and **control rods** to absorb the surplus, holding the chain reaction self-sustaining but not runaway; a pressurised water reactor uses high-pressure water as both moderator and coolant, and the heat raises steam to drive a turbine (ev-185)
- The textbook says that if the reactor overheats and boils the water away, the moderator is lost and the chain reaction stops — an inherent safety feature of a PWR, though the textbook also warns that it "can be overwhelmed in extreme circumstances" and that radioactive fission products keep generating heat after shutdown (ev-185)

> Why moderation helps: `235U` has a far larger fission cross-section for **slow neutrons** than for fast neutrons. The textbook only says the neutrons "must be slowed"; this library records the cross-section explanation as an addition (see K2).

### The energy ledger of fission: `E = mc²`

The textbook gives two facts (ev-185):

- an average fission releases about `200 MeV`
- the fission products have slightly **less mass** than the original nucleus

`E = mc²` connects the two: the missing mass leaves as energy.

- `200 MeV` per fission corresponds to `Δm = 200 MeV / c² ≈ 0.2147 u` (converted here)
- `235U` has an atomic mass of about `235.04 u`, so only about `0.091%` of the mass is converted to energy in each fission (converted here)
- The textbook's 1 kg `235U` example: `1000/235.04 = 4.25 mol`, about `2.56×10^24` nuclei; multiplying by `200 MeV` gives `8.21×10^13 J` (recomputed here), about 14,000 barrels of crude oil or 600,000 gallons of gasoline (ev-185)

### Fusion: light nuclei combining

**Nuclear fusion** is the combining of two light nuclei into a heavier one, releasing energy (ev-185).

- Fusion also releases energy, which looks contradictory at first; the answer is in the `BE/A` curve: nuclei with small `A` move toward the peak near `A ≈ 60`, so their `BE/A` increases and energy is released; nuclei with large `A` must instead move toward the peak by fission
- The main obstacle to fusion is the **Coulomb barrier**: two positively charged nuclei must come close enough for the short-range strong force to act. The remedy is to heat the fuel to a very high temperature so that thermal kinetic energy brings the nuclei close enough (ev-185)
- The Sun's **proton–proton chain** (p-p chain) turns four hydrogen nuclei into one helium nucleus; the net reaction is (ev-185):

`4 ^{1}H → ^{4}He + 2e⁺ + 2ν_e + 6γ`, releasing a net `26.7 MeV`

- The `26.7 MeV` includes the annihilation energy of the positrons and electrons; the four protons have a rest mass of about `4×938.8 MeV`, so about `0.711%` of the mass is converted to energy (converted here)
- The energy is produced in the solar core and takes about 32,000 years to diffuse to the surface; neutrinos interact so weakly that they escape in about 2 seconds (ev-185)
- The Sun has a negative-feedback thermostat: if the core gets hotter, the reaction rate rises, the interior expands and cools, and the rate falls again; the reverse happens if it cools (ev-185)

### The iron peak: the boundary between the two reactions

The textbook's `BE/A` curve peaks near `A ≈ 60` (around iron) (ev-185/ev-186):

- nuclei below the peak: fusion moves the products toward the peak and releases energy
- nuclei above the peak: fission moves the products toward the peak and releases energy
- iron is therefore the endpoint of ordinary stellar fusion: elements heavier than iron cannot be produced by ordinary fusion with a net release of energy, and require processes such as supernovae (the textbook only says iron is the boundary and the stellar endpoint; the supernova point is a standard addition)

The textbook also gives a per-kilogram comparison: fissioning 1 kg of `235U` yields about `8.21×10^13 J`, only about one fourth of the energy from fusing 1 kg of a deuterium–tritium mixture (ev-185). Recomputing here with `17.6 MeV` per D-T reaction gives about `3.38×10^14 J/kg`, about 4.1 times `235U`; a single fission releases about 11 times the energy of a single D-T fusion (`200 MeV` vs `17.6 MeV`), but fusion fuel has far fewer nucleons per kilogram, so fusion wins **per kilogram** (converted here; `17.6 MeV` is not in the textbook text)

### Reactors and fusion devices (qualitative)

- **Fission reactors**: a PWR uses high-pressure water as moderator and coolant, control rods regulate the neutron population, and steam drives a turbine; nuclear fuel has a far higher energy density than fossil fuel (ev-185)
- **Fusion reactors**: deuterium can be extracted from seawater and tritium bred from lithium; the fuel is heated into a plasma and confined by a magnetic field (tokamak), and the high-energy neutrons from fusion carry energy to the wall, where it becomes heat and then electricity (ev-185)
- The textbook presents fusion's advantages as abundant fuel, higher energy per unit mass, and none of the meltdown or long-lived-waste concerns of fission; it also admits that fusion devices have historically consumed more energy for control than they produced, and that facilities such as ITER are still at the research stage (ev-185)

> [!NOTE]
> **Source issues and what this library supplies** (ev-185/ev-186)
>
> 1. The body of m54574 calls fission `the splitting of an atomic bond`, while the glossary says `a nucleus splits`; fission splits a **nucleus**, not an "atomic bond". This library follows the glossary.
> 2. The Section Summary of m54574 explains fusion energy as "the combined nuclei are closer together, resulting in a decreased strong nuclear force", contradicting the body text ("the products have a larger `BE/A` and less mass per nucleon"). This library follows the body text and the `BE/A` curve; the correct statement is that **the products have a larger binding energy per nucleon**, not that the strong force decreases.
> 3. m54574 presents "water boils away → the chain reaction stops" as an inherent safety feature; this is roughly true for a PWR (negative void coefficient), but it cannot be generalised to every reactor type, and the textbook itself says it "can be overwhelmed in extreme circumstances". This library limits it to a qualitative description of a PWR.
> 4. The fusion-reactor section of m54574 is promotional in tone: ITER is described as "being constructed in southern France", and "exciting theoretical improvements" by Lockheed Martin and Lawrence Livermore are mentioned without a citation; "no meltdown and no long-lived waste" is also overstated (tritium and neutron activation still produce radioactivity). These are cited only as historical background.
> 5. m54574 says fusion yields "3 to 4 times" more energy per gram than fission; recomputing here with D-T gives about `4.1` times, while another sentence in the same module says "one fourth", consistent with 4.1. The difference is rounding and does not change the conclusion.
>
> **Supplied here, not in the textbook**: the `0.2147 u` and `0.091%` mass conversion per fission, the `0.711%` of the p-p chain, the `17.6 MeV` D-T reaction and the `4.1` per-kilogram ratio, the `k`-factor framing of the chain reaction, the explanation that the slow-neutron cross-section is much larger than the fast-neutron one, and quantum tunnelling through the Coulomb barrier. The textbook gives only `200 MeV`, `26.7 MeV`, "3 to 4 times", and the qualitative mechanisms (plus the 1 kg `235U` worked example).

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Binding energy and mass defect](binding-energy-and-mass-defect.en.md) — `200 MeV` and `26.7 MeV` are both `Δm c²`; the iron peak is the boundary between fission and fusion |
| Prerequisite | [Atomic nucleus](atomic-nucleus.en.md) — fission products are still nuclides, and the chain reaction is booked with `Z` and `A` |
| Related | [Radioactive decay](radioactive-decay.en.md) — most fission products are radioactive, and their decay heat is why a reactor must keep cooling after shutdown; not covered here |
| Recorded gap | **reactor neutron kinetics and criticality calculations**, **fission-product yields and decay heat**, **breeder reactors and spent-fuel reprocessing**, **inertial confinement fusion and ignition**, **quantitative tokamak plasma confinement**, **fusion Q value and energy gain**, and **nuclear-weapon physics** are not built |

## Argument

### K1 · Fission and fusion both release energy because both move toward the `BE/A` peak (the iron-peak reasoning is organized here)

- **Claim**: nuclei below the peak release energy by fusion, nuclei above it by fission; the energy released equals the total binding energy of the products minus that of the reactants
- **Premises**: the textbook says `BE/A` is largest near `A ≈ 60` (around iron), that light nuclei release energy by fusion and heavy nuclei by fission, and that fusion products have a larger `BE/A` (ev-185); another module gives the `BE/A` curve, the iron peak, and `BE = Δm c²` (ev-186)
- **Reasoning**: the reaction energy is `Q = BE_products − BE_reactants = (m_reactants − m_products)c²`. A larger total binding energy for the products ⇔ a smaller total rest mass ⇔ energy release. For `A < 60`, fusion moves nucleons toward the peak; for `A > 60`, fission does. The textbook's `200 MeV` per fission divided by `236` nucleons gives about `0.85 MeV/nucleon`; the Sun's `26.7 MeV` divided by four protons gives `6.675 MeV/nucleon`. Both lie on the rising, light-nucleus side, consistent in order of magnitude with the `BE/A` curve
- **Evidence**: ev-185, ev-186
- **Attacked**: **the textbook gives only the qualitative shape of the curve and two total energies, not precise `BE/A` readings for `235U`, its fission products, or each step of the p-p chain, and it does not state `Q = ΔBE` as a rule**; `0.85` and `6.675 MeV/nucleon` are obtained here by dividing the textbook's total energies by the nucleon number, not taken from the text. Real fission products have a broad mass distribution, and `200 MeV` is an average, not the energy of every fission
- **By**: @hpleapfrog · 2026-10-21

### K2 · Whether a chain reaction is self-sustaining depends on the neutron ledger; `k = 1` is critical (the `k` framing is supplied here)

- **Claim**: the average number `k` of neutrons produced by one fission and absorbed by the next generation determines the state of the reactor: `k < 1` subcritical, `k = 1` critical, `k > 1` supercritical; the critical mass is the minimum fuel mass that achieves `k = 1`
- **Premises**: the textbook describes the chain reaction `1 → 2 → 4 → 8 → …`, defines critical mass as "the minimum amount necessary for self-sustained fission", notes that some neutrons escape or are absorbed without causing fission, that the moderator slows neutrons and control rods absorb them, and that `235U` and `239Pu` fission more easily than `238U` (ev-185)
- **Reasoning**: divide the neutrons from each fission into those that induce another fission, those absorbed by control rods or structural material, and those that leak out. A chain reaction is self-sustaining only if the average number inducing another fission reaches 1; above 1 it grows as `k^n`. The critical mass depends on the neutron yield, the fission cross-section, geometric leakage, and any reflector, so it is not a fixed constant. Slowing the neutrons raises the fission cross-section of `235U`, so the same fuel reaches `k = 1` more easily; inserting control rods absorbs neutrons and pushes `k` below 1
- **Evidence**: ev-185
- **Attacked**: **the textbook gives no definition of `k`, no critical-mass numbers, and no discussion of delayed neutrons, temperature coefficients, or void coefficients**; "water boils away → the reaction stops" holds only for a PWR with a negative void coefficient and cannot be generalised to every reactor type. This entry only turns the textbook's qualitative description into a neutron ledger and does not cover reactor kinetics
- **By**: @hpleapfrog · 2026-10-21

### K3 · Fusion must first overcome the Coulomb barrier; the Sun relies on high temperature, high density, and quantum tunnelling (tunnelling is supplied here)

- **Claim**: two light nuclei must come within the range of the strong force to fuse, and the Coulomb repulsion forms a barrier; the solar core sustains the p-p chain through high temperature, high density, and quantum tunnelling
- **Premises**: the textbook uses the analogy of a potential-energy hill with a deep well in the middle, saying the nuclei need enough kinetic energy to climb the hill; fusion in the Sun occurs only where the core is hot enough and the particles are close enough; the p-p chain releases a net `26.7 MeV`; negative feedback keeps the Sun stable (ev-185)
- **Reasoning**: the Coulomb potential energy of two nuclei rises as they approach, and only when the kinetic energy is enough to climb the barrier (or tunnel through it) does the short-range strong force take over and release energy. Higher temperature means larger thermal kinetic energy and more nuclei able to climb the barrier; higher density means more frequent collisions. The solar core is about `1.5×10^7 K`, implying an average thermal energy of about `1.3 keV`, far below the MeV-scale Coulomb barrier between protons; the p-p chain proceeds through **quantum tunnelling** and the small high-energy tail (supplied here; the textbook does not mention tunnelling). Dividing `26.7 MeV` by the rest mass of four protons gives a mass conversion of about `0.711%`
- **Evidence**: ev-185
- **Attacked**: **the textbook does not mention quantum tunnelling, the Gamow factor, or the weak interaction in the first step of the p-p chain**; "hot enough" is qualitative. The `1.5×10^7 K` and `1.3 keV` are standard solar-model values supplied here, not textbook text; `0.711%` is converted here from the textbook's `26.7 MeV` and the proton rest mass, and is not given by the textbook
- **By**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the fission-and-fusion gap in Elective-3 "atomic nucleus", follows "Binding energy and mass defect" | written after reading m54574/m42640 in full (ev-185/ev-186) | @hpleapfrog |
