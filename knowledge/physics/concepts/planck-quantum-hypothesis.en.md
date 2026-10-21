---
id: kb:physics:planck-quantum-hypothesis
type: 知识点
title: "Planck's quantum hypothesis"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who know waves and the electromagnetic spectrum and need to understand why blackbody radiation forced physicists to quantize energy
  条件: covers the blackbody spectrum, the failure of classical wave theory (the ultraviolet catastrophe), Planck's E = nhf, and how photon energy varies with frequency only; the photoelectric effect, wave-particle duality, atomic energy levels, and the Bohr model are not built here
edges:
  先修: ["[Waves](waves.en.md)", "[The electromagnetic spectrum](electromagnetic-spectrum.en.md)"]
  支持: []
  攻击: []
evidence: [ev-168]
license: CC-BY-SA-4.0
---

> **English version of [`普朗克量子假设.md`](普朗克量子假设.md).**

> [!TIP]
> **After reading this entry you should** be able to state the two regularities of the blackbody spectrum as temperature rises, explain why classical wave theory fails at short wavelengths, and use `E = hf` to compare photons of different frequencies

## Definition

A **blackbody** is an ideal object that absorbs and re-emits all radiation incident on it; the textbook models it with a small hole in the wall of an oven. Heat the blackbody and plot the intensity of its radiation against wavelength and you get the **blackbody spectrum**.

The textbook reads two empirical regularities off the graph:

- **As temperature rises, the total radiated energy increases** — the area under the curve grows with temperature;
- **The peak moves toward shorter wavelengths and higher frequencies** — at `3,000 K` the peak is near `1000 nm` (infrared), at `4,000 K` it is in the yellow-green, and at `6,000 K` it covers the whole visible range and appears white.

The curve predicted by classical wave theory **diverges at short wavelengths**: the textbook writes the classical formula as `I = 2kT/λ²` and says it predicts "an infinite amount of energy quickly emitted at the shortest wavelengths" at any temperature. The measured curve instead falls after its peak; this contradiction is called the **ultraviolet catastrophe**.

**Planck's quantum hypothesis**: the energy of blackbody radiation can take only discrete values

`E = nhf`

where `n` is a non-negative integer (0, 1, 2, …), `h = 6.626×10⁻³⁴ J·s` is Planck's constant, and `f` is the frequency. The higher the frequency, the more energy one quantum carries; at a fixed total energy, high-frequency quanta are less likely to occur, so the short-wavelength end does not grow without bound.

The textbook's photon-energy examples:

- `580 nm` visible light: `E = hc/λ = 3.43×10⁻¹⁹ J`; a 100 W bulb with 10% of its energy in visible light at an average wavelength of `580 nm` emits about `2.92×10¹⁹` photons per second
- `2000 nm` infrared light: `9.95×10⁻²⁰ J`
- `500 nm` visible light: `3.98×10⁻¹⁹ J`

> [!IMPORTANT]
> **The textbook's classical formula is wrong, and this entry does not use it.**
>
> The source writes `I = 2kT/λ²` and says intensity falls with wavelength by an "inverse-square" relation. The Rayleigh–Jeans law goes as `∝ T/λ⁴` per wavelength and `∝ Tν²` per frequency; `2kT/λ²` has dimensions of `J/m²` and is not a spectral intensity per unit wavelength either. The qualitative conclusion the textbook wants — classical theory diverges at short wavelengths and disagrees with experiment — does not depend on that wrong exponent, but the formula itself cannot be cited.

> [!IMPORTANT]
> **The glossary defines the "ultraviolet catastrophe" as a "misconception"; that is a defect in the source.**
>
> The glossary says `misconception that blackbodies would radiate high frequency energy at a much higher rate than energy radiated at lower frequencies`. The ultraviolet catastrophe is the name of a **failed prediction** of classical theory (the Rayleigh–Jeans law), not a misconception about blackbodies themselves; a blackbody of course does not actually radiate infinite energy.

> [!IMPORTANT]
> **Planck quantized the energy exchanged by radiators, not "light consists of photons".**
>
> In the blackbody section the textbook already speaks of each frequency of light carrying a fixed amount of energy; treating light itself as made of photons is the further step Einstein takes when explaining the photoelectric effect in the next section. This entry uses `E = hf` as the energy of one energy quantum and leaves "light consists of photons" to the [photoelectric effect](photoelectric-effect.en.md).

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Waves](waves.en.md) — `f`, `λ`, and `v = fλ` are needed to read the blackbody graph's axis and "the peak moves to higher frequency" |
| Prerequisite | [The electromagnetic spectrum](electromagnetic-spectrum.en.md) — locating a peak in the infrared, visible, or ultraviolet first requires knowing where the bands are |
| Follow-up | [The photoelectric effect](photoelectric-effect.en.md) — applies `E = hf` to one photon interacting with one electron, yielding `KE_max = hf − BE` and the threshold frequency |
| Recorded gap | **The quantitative Wien displacement law `λ_max T = 2.898×10⁻³ m·K`**, the **Stefan–Boltzmann law**, the **correct Rayleigh–Jeans law and the Planck spectrum formula**, and **wave-particle duality of light** are not built in this library; the textbook module also does not derive the Planck spectrum |

## Arguments

### K1 · The two regularities of the blackbody spectrum and the failure of classical wave theory (no attacks yet)

- **Claim**: The blackbody spectrum has a peak at every temperature; as temperature rises the total radiation increases and the peak moves toward shorter wavelengths and higher frequencies. Classical wave theory cannot describe both regularities and predicts unlimited growth at short wavelengths, opposite to experiment.
- **Premises**: The textbook's readings of the `3,000 K`, `4,000 K`, and `6,000 K` curves; its statement that the classical formula "quickly emits an infinite amount of energy" at short wavelengths and its naming of the contradiction the ultraviolet catastrophe; its classical formula `I = 2kT/λ²` (ev-168)
- **Reasoning**: The classical formula diverges as `λ → 0`, while the measured curve falls after its peak; the two run in opposite directions at short wavelengths, so classical theory cannot be patched by adjusting parameters — the assumption about energy exchange has to change
- **Evidence**: ev-168
- **Attacked**: The textbook's classical formula is itself wrong — the exponent of `λ` should be `−4` (per wavelength), not `−2`, and the dimensions do not work out; the glossary also calls the ultraviolet catastrophe a "misconception". The textbook is therefore a source only for the **qualitative conclusion** that classical theory fails at short wavelengths, not for the Rayleigh–Jeans formula
- **Signed by**: @hpleapfrog · 2026-10-21

### K2 · Planck's hypothesis: radiation energy comes only in `E = nhf` (no attacks yet)

- **Claim**: Blackbody radiation exchanges energy in units of `hf`; `h = 6.626×10⁻³⁴ J·s`, `n = 0, 1, 2, …`
- **Premises**: The textbook writes `E = nhf`, explains with a "coins through a funnel" analogy that low-frequency quanta are more likely and that higher temperature admits more high-frequency quanta, and says the work won the 1918 Nobel Prize in Physics (ev-168)
- **Reasoning**: At a fixed total energy, fewer high-priced high-frequency quanta can be emitted, which suppresses the short-wavelength end; a higher temperature supplies more total energy, the number of high-frequency quanta grows, and the peak shifts left. This is the mechanism the textbook uses to explain the shape of the blackbody curve
- **Evidence**: ev-168
- **Attacked**: The textbook says Planck "proposed quantization of atomic and molecular energy levels", but Planck's hypothesis concerns the energy exchange of the radiators; applying quantization to atomic energy levels is Bohr's later step. The "coins in a funnel" is an analogy, not a derivation; the real Planck spectrum requires a statistical sum over oscillator energies, which the module never gives
- **Signed by**: @hpleapfrog · 2026-10-21

### K3 · Photon energy grows with frequency and shrinks with wavelength (no attacks yet)

- **Claim**: `E = hf = hc/λ`; the shorter the wavelength and the higher the frequency of a beam, the greater the energy of one quantum
- **Premises**: The textbook compares `2000 nm` infrared (`9.95×10⁻²⁰ J`) with `500 nm` visible light (`3.98×10⁻¹⁹ J`) and computes an emission rate of `2.92×10¹⁹` photons/s for a 100 W bulb at `580 nm` (ev-168)
- **Reasoning**: `h` and `c` are constants, so `E` is proportional to `f` and inversely proportional to `λ`; this explains why a blue photon carries more energy than a red one, and an ultraviolet or X-ray photon more still
- **Evidence**: ev-168
- **Attacked**: The 100 W bulb example treats all visible light as monochromatic `580 nm`; a real incandescent bulb has a continuous spectrum, so `2.92×10¹⁹` is only an order-of-magnitude estimate. The textbook substitutes an "average wavelength" for the distribution without giving an error range
- **Signed by**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 选必三 "atomic structure and wave-particle duality" chapter, attached after waves and the electromagnetic spectrum | Written after reading m54566 in full for ev-168 | @hpleapfrog |
