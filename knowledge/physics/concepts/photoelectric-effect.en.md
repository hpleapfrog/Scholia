---
id: kb:physics:photoelectric-effect
type: 知识点
title: "The photoelectric effect"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned Planck's quantum hypothesis and need to understand how the photon model explains the five experimental properties of the photoelectric effect
  条件: covers the external photoelectric effect only — the five experimental properties, Einstein's photon model, `KE_max = hf − BE` and the threshold frequency, the retarding-voltage apparatus, and applications; wave-particle duality, Compton scattering, atomic energy levels, and the Bohr model are not built here
edges:
  先修: ["[Planck's quantum hypothesis](planck-quantum-hypothesis.en.md)"]
  支持: []
  攻击: []
evidence: [ev-169]
license: CC-BY-SA-4.0
---

> **English version of [`光电效应.md`](光电效应.md).**

> [!TIP]
> **After reading this entry you should** be able to state the five experimental properties of the photoelectric effect, compute the maximum kinetic energy of a photoelectron with `KE_max = hf − BE`, and use the threshold frequency to decide whether light of a given wavelength can eject electrons from a given material

## Definition

Light striking certain materials can eject electrons from them; this is the **photoelectric effect**, and the ejected electrons are **photoelectrons**. The textbook's apparatus is an evacuated photoelectric tube: light falls on a metal plate, the ejected electrons are collected by a collector wire and measured as a current, and an adjustable retarding voltage between the wire and the plate is used to measure the electrons' energy.

The textbook lists five experimental properties (monochromatic light, all photons of energy `hf`):

1. **There is a threshold frequency `f₀`**: for a given material, light below `f₀` ejects no electrons regardless of intensity;
2. **There is no delay**: electrons are ejected as soon as the light strikes the material;
3. **The number of electrons is proportional to intensity**: the number ejected per unit time is proportional to the intensity;
4. **The maximum kinetic energy is independent of intensity**: raising intensity increases the number of electrons but not the energy of each;
5. **Energy conservation**: the maximum kinetic energy of a photoelectron equals the photon energy minus the electron's binding energy in the material

`KE_max = hf − BE`

`BE` is the **binding energy**, also called the **work function** of the material. It can also be written `BE = hf₀`, where `f₀` is the threshold frequency. The textbook plots `KE_max` against `f`: for `f < f₀` there are no electrons; above `f₀` the graph is a straight line whose slope is `h`, so the graph can be used to measure Planck's constant.

The textbook's worked example: a `420 nm` violet photon has `E = hc/λ = 4.74×10⁻¹⁹ J = 2.96 eV`; calcium has a binding energy of `2.71 eV`, so the maximum kinetic energy is `2.96 − 2.71 = 0.25 eV`. The corresponding threshold wavelength is `458 nm` — light longer than blue (red light, for example) cannot eject electrons from calcium.

> [!IMPORTANT]
> **The textbook calls `E = hf` "the energy of a photon or photoelectron"; that is wrong.**
>
> The source writes `the energy of a photon or photoelectron to be E = hf`. `hf` is the energy of the **photon**; a photoelectron's maximum kinetic energy is `hf − BE`, smaller than `hf` by one binding energy. This entry's formula `KE_max = hf − BE` agrees with the textbook's own property 5, but that definition sentence cannot be cited.

> [!IMPORTANT]
> **The textbook has several symbol and unit slips, and this entry uses the correct forms.**
>
> The worked example writes the eV conversion of `4.74×10⁻¹⁹ J` as `4.74×10⁻¹⁹ J⋅s` (joule-seconds is a unit of action, not energy); the Key Equations write the threshold-frequency subscript as a capital `O` (`BE = hf_O`) while the body uses `f₀`; an exercise says `bonding energy` for binding energy. The worked-example discussion also says the electron is stopped by a `0.26 eV` retarding potential, while the same section computes a maximum kinetic energy of `0.25 eV` — the two should be equal, so `0.26` versus `0.25` is a slip in the source.

> [!IMPORTANT]
> **"The electron number depends only on intensity and on no other characteristic" holds only at fixed frequency.**
>
> The textbook sentence assumes all photons have the same frequency and that the frequency is above threshold. Change the frequency (still above threshold) and the number of electrons ejected from the same material can differ; change the material and both the threshold and the binding energy differ. This library reads property 3 as the idealized statement "for one monochromatic beam on one material, the electron number is proportional to intensity", not as a universal law.

> [!IMPORTANT]
> **The textbook calls photoconductive cells and solar cells "applications of the photoelectric effect"; strictly they are two other effects.**
>
> The **external photoelectric effect** is what this entry covers: electrons are ejected from the material into vacuum. A **photoconductive cell** works by the **internal photoelectric effect** (photo-generated carriers raise the conductivity), and a **solar cell** works by the **photovoltaic effect** (a potential difference appears across a PN junction); neither requires electrons to leave the material. The movie-soundtrack pickup is likewise a photoconductive cell. Grouping them in one section as "light produces electricity" is fine as an engineering tour, but explaining them with this entry's five properties would be wrong — this entry lists them only as related technologies.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Planck's quantum hypothesis](planck-quantum-hypothesis.en.md) — `E = hf` and "energy is exchanged in discrete portions" are the premises of the photon model |
| Recorded gap | **`KE_max = eV_s` (the quantitative relation between retarding voltage and maximum kinetic energy)**: the textbook's apparatus measures electron energy with a retarding voltage but never writes this equation; the **data treatment of the `KE_max–f` graph whose slope gives `h`**, **wave-particle duality of light**, **Compton scattering**, and **atomic energy levels and the Bohr model** are not built in this library |
| Related technology | Photoelectric tubes, photoconductive cells, solar cells, movie soundtracks — the first shares this entry's mechanism; the latter two belong to the internal photoelectric effect and the photovoltaic effect |

## Arguments

### K1 · The five experimental properties and the failure of the classical wave model (no attacks yet)

- **Claim**: For a given material there is a threshold frequency; electrons are ejected without delay; the electron number is proportional to intensity; the maximum kinetic energy is independent of intensity; and the maximum kinetic energy grows linearly with frequency, `KE_max = hf − BE`
- **Premises**: The textbook's statement of the five properties and its "classical wave model / photon model" table; the reading of the threshold and the slope `h` from the `KE_max–f` graph (ev-169)
- **Reasoning**: If light were a continuous wave, a large enough intensity should be able to accumulate the energy needed to eject an electron, so there should be no threshold, electrons should not appear "immediately", and greater intensity should produce faster electrons; all three contradict experiment. If light consists of photons of energy `hf` and one photon is absorbed by one electron, then the threshold (`hf < BE`, so no number of photons can pool energy into one electron), the absence of delay, and intensity changing only the number of portions rather than the energy per portion all follow naturally
- **Evidence**: ev-169
- **Attacked**: The textbook's property 3 says the electron number is "proportional to intensity and to no other characteristic", which holds only at one frequency on one material; the module also never writes the quantitative relation between retarding voltage and maximum kinetic energy `KE_max = eV_s`, so "measure the energy with a retarding voltage" remains an apparatus description without a formula
- **Signed by**: @hpleapfrog · 2026-10-21

### K2 · Einstein's photon model: `KE_max = hf − BE` and the threshold frequency (no attacks yet)

- **Claim**: One photon gives all its energy `hf` to one electron; the electron spends `BE` escaping the material and keeps the rest as maximum kinetic energy; `BE = hf₀`, so no photoelectrons appear for `f < f₀`
- **Premises**: The textbook's `KE_max = hf − BE` and `BE = hf₀`; the 420 nm violet-light/calcium example (`2.96 eV − 2.71 eV = 0.25 eV`, threshold `458 nm`); the silver and sodium exercises (ev-169)
- **Reasoning**: `h` and `BE` are constants for a given material, so `KE_max` grows linearly with `f` and is independent of intensity; the line meets the horizontal axis at `f₀ = BE/h`. The 420 nm example sits just above threshold, so the kinetic energy is only `0.25 eV`; at longer wavelengths the photon energy falls below `2.71 eV`, the formula gives a negative kinetic energy, and no electrons can be ejected
- **Evidence**: ev-169
- **Attacked**: The worked-example discussion places a `0.26 eV` retarding voltage next to a computed `0.25 eV` maximum kinetic energy, but the two should be equal; the textbook also uses `BE` and "work function" interchangeably without saying they are two names for one quantity. `BE = hf₀` holds only for an electron escaping directly from the surface — electrons deeper inside the material need more energy, which is exactly why the quantity is `KE_max` and not "the kinetic energy"
- **Signed by**: @hpleapfrog · 2026-10-21

### K3 · Applications: electric eyes, photoconductive cells, movie soundtracks, and solar cells (no attacks yet)

- **Claim**: The photoelectric effect and its close relatives support everyday technologies such as automatic streetlights, the electric eyes that stop elevator doors and turn on faucets, movie-soundtrack pickups, and solar cells
- **Premises**: The textbook's applications section: photoconductive cells gain free electrons and holes under light and their conductivity rises; the varying width of the soundtrack film changes the light reaching the photocell, the current changes with it, and the changing current becomes sound; solar (photovoltaic) cells convert light into current; the solar-energy physicist career passage (ev-169)
- **Reasoning**: These devices share the pattern "light → electrical signal" but take different routes: a photoelectric tube uses the external photoelectric effect (electrons into vacuum), a photoconductive cell uses the internal photoelectric effect (conductivity change), and a solar cell uses the photovoltaic effect (junction potential). Grouping them under "applications of the photoelectric effect" is acceptable as an engineering tour; as physics, they must be distinguished
- **Evidence**: ev-169
- **Attacked**: The textbook does not distinguish the external photoelectric effect, the internal photoelectric effect, and the photovoltaic effect, so a reader may think photoconductive cells and solar cells also obey `KE_max = hf − BE` and the threshold frequency; the soundtrack pickup is explicitly a "photocell plus photoconductive circuit", an internal effect. This entry lists them only as technology, not as evidence for the five properties
- **Signed by**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Entry created; attached after Planck's quantum hypothesis as the second node of the 选必三 "atomic structure and wave-particle duality" chapter | Written after reading m54559 in full for ev-169 | @hpleapfrog |
