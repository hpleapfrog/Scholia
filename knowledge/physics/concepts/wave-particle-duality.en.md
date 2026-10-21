---
id: kb:physics:wave-particle-duality
type: 知识点
title: "Wave-particle duality"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned the photoelectric effect and need to understand that light is both wave-like and particle-like, and that matter also has wave properties
  条件: covers photon momentum `p = h/λ`, the Compton effect, wave-particle duality of light, and the de Broglie relation for matter waves only; the Compton wavelength-shift formula, experimental evidence such as electron diffraction, the uncertainty principle, and the quantitative Bohr model and hydrogen spectrum are not built here
edges:
  先修: ["[The photoelectric effect](photoelectric-effect.en.md)", "[Waves](waves.en.md)"]
  支持: []
  攻击: []
evidence: [ev-170]
license: CC-BY-SA-4.0
---

> **English version of [`波粒二象性.md`](波粒二象性.md).**

> [!TIP]
> **After reading this entry you should** be able to compute photon momentum with `p = h/λ`, explain why the Compton effect needs both energy conservation and momentum conservation, and explain that "wave-particle duality" does not mean "light is sometimes a wave and sometimes a particle" but that two models each describe part of the same radiation

## Definition

The **momentum of a photon** is given by the de Broglie relation

`p = h/λ`

where `h` is Planck's constant and `λ` is the wavelength. The momentum of a visible photon is very small: a `500 nm` photon has `p = 1.33×10⁻²⁷ kg·m/s`. The textbook uses it for three comparisons:

- an electron with the same momentum moves at about `1,460 m/s` (far below the speed of light, so classical formulas apply);
- that electron's kinetic energy is `9.64×10⁻²⁵ J = 6.02×10⁻⁶ eV`;
- the same photon's energy is `E = hc/λ = 3.98×10⁻¹⁹ J = 2.48 eV`, about five orders of magnitude larger.

From `E = hc/λ` and `p = h/λ` it follows that, for a photon, `E = pc`.

**The Compton effect**: X-rays scattered by electrons in a material lose energy (their wavelength grows). The textbook treats this as a **collision** between a photon and an electron at rest and finds that **both energy and momentum are conserved**. Compton observed it in 1923; the textbook says the work won him the Nobel Prize in Physics (the year is wrong; see below). The textbook explains why X-rays are used: the shorter the wavelength, the larger the photon momentum, and the effect is only noticeable when such a photon collides with the lightest particle, the electron.

**Wave-particle duality**: electromagnetic radiation is wave-like — it shows interference and diffraction — and particle-like — its energy and momentum are discrete and its interactions are concentrated in individual portions. The textbook says everyday observations show one kind of property at a time, **never both simultaneously**; but this does not mean light "chooses" to be a wave or a particle — the two models describe different sides of the same radiation.

The textbook extends this to matter: photons have wave-particle duality, and photons and matter both obey momentum conservation, so it asks whether matter also has wave properties; the answer is yes. The **de Broglie wavelength** is

`λ = h/p`

where `p = mv` (non-relativistic). The textbook mentions matter-wave applications only in an exercise (electron microscopes resolve finer detail than light microscopes) and gives no experimental evidence such as electron diffraction.

> [!IMPORTANT]
> **The textbook dates Compton's Nobel Prize to 1929; the year was 1927.**
>
> The source writes `Arthur Compton was awarded the Nobel Prize in 1929`. Compton shared the 1927 Nobel Prize in Physics with C. T. R. Wilson for discovering the scattering effect that bears his name. This entry does not use 1929.

> [!IMPORTANT]
> **One textbook exercise writes the de Broglie wavelength relation as `p = hλ`, which is wrong.**
>
> The Test Prep item says `The wavelength of a particle is called the de Broglie wavelength, and it can be found with the equation p = hλ`. The wavelength follows from `λ = h/p`; the body, the Section Summary, and the Key Equations all write `p = h/λ`. This entry uses only the correct forms `λ = h/p` and `p = h/λ`.

> [!IMPORTANT]
> **In the `500 nm` example, part (c) uses a different speed from part (b), and the kinetic energy does not match the value substituted.**
>
> Part (b) gives `1,459.9 m/s ≈ 1,460 m/s`; part (c) substitutes `1,456 m/s` into `KE = ½mv²` and reports `9.64×10⁻²⁵ J`. Using `1,456 m/s` gives about `9.66×10⁻²⁵ J`. This entry cites only the order of magnitude and the conclusion (the electron's kinetic energy is about five orders of magnitude below the photon energy), not these figures as a precise worked example.

> [!IMPORTANT]
> **"Wave-particle duality" is not "light is sometimes a wave and sometimes a particle".**
>
> The textbook glossary writes `property of behaving like either a particle or a wave`, which invites reading light as switching between two identities; yet the module's own teacher support says explicitly `Light does not choose when to be like a particle and when to be like a wave`. This entry follows the teacher support: the wave model and the particle model each capture part of the same radiation, and which model is useful depends on the question and the experiment, not on light changing identity.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [The photoelectric effect](photoelectric-effect.en.md) — the photon model and `E = hf` are the premises of `p = h/λ` and the Compton collision picture |
| Prerequisite | [Waves](waves.en.md) — interference, diffraction, and the wavelength `λ` define the "wave-like" side |
| Recorded gap | **The Compton wavelength-shift formula `Δλ = (h/m_e c)(1 − cosθ)`**, **experimental evidence for matter waves such as electron diffraction and the Davisson–Germer experiment**, the **uncertainty principle**, the **quantitative Bohr model and hydrogen spectrum**, and the **statistical interpretation of matter waves (the Born rule)** are not built in this library; the textbook module does not give the quantitative Compton shift either |
| Related technology | Solar sails (Cosmos 1 · NanoSail-D · LightSail-1), electron microscopes, comet tails — the first two rely on photon momentum; the dust tail relies on radiation pressure while the ion tail relies on the solar wind |

## Arguments

### K1 · The Compton effect: photons carry momentum, and collisions conserve both energy and momentum (no attacks yet)

- **Claim**: X-rays scattered by electrons lose energy and gain wavelength; treating the scattering as a photon-electron collision, both energy and momentum are conserved
- **Premises**: The textbook's account of Compton's 1923 observation, `p = h/λ`, the comparison between a `500 nm` photon and an electron of the same momentum, and its statement that X-rays are used because their short wavelength gives a large momentum that matters against the lightest particle (ev-170)
- **Reasoning**: If the photon had no momentum, the recoil momentum gained by the electron would come from nowhere; only by giving the photon `p = h/λ` and constraining the collision with both energy and momentum conservation can the pair of observations — the scattered photon losing energy and the electron recoiling — be explained. The same relation explains why the Compton effect is hard to observe with visible light: `h/λ` is too small
- **Evidence**: ev-170
- **Attacked**: The module gives no Compton shift formula, only a qualitative account; calling the photon momentum relation "determined by de Broglie" is a historical simplification — for photons, `p = h/λ` follows from `E = pc` and `E = hf`, while de Broglie's contribution was extending `λ = h/p` to material particles; the Nobel year is also wrong (1929 instead of 1927). This entry therefore uses the module only as a qualitative source that the Compton effect exists and conserves both quantities
- **Signed by**: @hpleapfrog · 2026-10-21

### K2 · Wave-particle duality: two models describe the same radiation (no attacks yet)

- **Claim**: Light shows wave properties (interference, diffraction) and particle properties (discrete energy and momentum, concentrated interactions); neither model alone covers all experiments
- **Premises**: The textbook's parallel accounts of the double-slit interference pattern and the photon's discrete properties; its statement that everyday observations show one kind of property at a time; the teacher support line "light does not choose when to be like a wave and when to be like a particle" (ev-170)
- **Reasoning**: Interference and diffraction require phase and wavelength concepts; the photoelectric effect and Compton scattering require portions of energy and momentum. Both are observed reliably in different experiments and both can be computed, so "wave" and "particle" are not mutually exclusive metaphysical labels but two models with different domains of use
- **Evidence**: ev-170
- **Attacked**: The glossary's `either a particle or a wave` clashes with the body's teacher support and invites reading light as switching identity; the module also gives no criterion for when to use which model, only examples; for matter waves it asserts the conclusion and gives one exercise without experimental evidence such as electron diffraction. This entry limits "duality" to complementarity at the level of models and does not extend it to a subjective choice by light
- **Signed by**: @hpleapfrog · 2026-10-21

### K3 · One photon's momentum is tiny, but many photons can push macroscopic objects (no attacks yet)

- **Claim**: A `500 nm` photon has a momentum of only `1.33×10⁻²⁷ kg·m/s`, but many photons shining continuously on a large, low-mass reflecting surface deliver enough total impulse to produce a measurable acceleration; comet dust tails and solar sails are two kinds of evidence/application
- **Premises**: The textbook's observation that comet tails point away from the Sun, solar-sail proposals (Cosmos 1 · NanoSail-D · LightSail-1 with a `32 m²` sail), its statement that reflection reverses the momentum and doubles the impulse, and the module exercise with `1.30 kW/m²`, `0.100 kg/m²`, and 24 hours (ev-170)
- **Reasoning**: With intensity `I`, sail area `A`, and reflectivity near 1, the incident momentum per second is `IA/c` and the change after reflection is `2IA/c`, so the radiation pressure is `F = 2IA/c`. With `I = 1.30 kW/m²` and an areal density of `0.100 kg/m²`, the acceleration is about `8.7×10⁻⁵ m/s²` and the speed after one day is about `7.5 m/s` — consistent with the module exercise's `7.49 m/s`
- **Evidence**: ev-170
- **Attacked**: `F = 2IA/c` assumes perfect specular reflection, no absorption, and constant intensity and mass; real sails absorb and re-radiate and fall short of the ideal. The blue ion tail of a comet is produced by the solar wind, not photon momentum; the textbook says so, but readers easily attribute both tails to radiation pressure. The module exercise also mixes acceleration options (`m/s²`) with speed options (`m/s`), so the quantity asked for must be read carefully
- **Signed by**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Entry created; attached after the photoelectric effect and waves, completing the last node of the 选必三 "atomic structure and wave-particle duality" chapter | Written after reading m54552 in full for ev-170 | @hpleapfrog |
