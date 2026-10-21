---
id: kb:physics:polarization
type: 知识点
title: "Polarization of light"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned transverse waves and refraction and need to understand the direction of polarization, Malus's law, Brewster's angle, and applications of polarization
  条件: covers only linear polarization, polarizing filters and Malus's law, polarization by reflection and Brewster's law, polarization by scattering, optical activity, birefringence, and liquid-crystal displays; circular and elliptical polarization, Stokes parameters, and the quantitative Fresnel reflection coefficients are not built here
edges:
  先修: ["[Waves](waves.en.md)", "[Refraction of light](refraction.en.md)"]
  支持: []
  攻击: []
evidence: [ev-174]
license: CC-BY-SA-4.0
---

> **English version of [`光的偏振.md`](光的偏振.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the intensity after a polarizing filter with `I = I₀ cos²θ`, compute Brewster's angle with `tan θ_b = n₂/n₁`, and explain why polarizing sunglasses cut glare from water and why skylight is partially polarized

## Definition

Light is an electromagnetic wave: its electric and magnetic fields are both perpendicular to the direction of propagation, so it is a **transverse wave**. **Polarization** is the attribute that a wave's oscillations have a definite direction relative to the direction of propagation. For an electromagnetic wave, **the direction of polarization is defined to be the direction of the electric field**.

- **Unpolarized light**: composed of many waves whose polarization directions are random. Sunlight and light from an incandescent lamp are approximately unpolarized.
- **Polarizing filter**: passes only the electric-field component parallel to its **axis**. If the incident light is already polarized and the electric field makes an angle `θ` with the axis, the transmitted amplitude is `E cos θ`; intensity is proportional to amplitude squared, so

`I = I₀ cos²θ` (Malus's law)

Here `I₀` is the intensity of the **incident polarized light**. If the incident light is unpolarized, one ideal polarizing filter transmits `½I₀` — averaging `cos²θ` over all directions gives `⟨cos²θ⟩ = ½`. Two filters with perpendicular axes transmit nothing; rotating the second from parallel to perpendicular makes the transmitted light go from bright to dark.

> [!IMPORTANT]
> **The `I₀` in Malus's law is the intensity of polarized light; the law cannot be applied directly to unpolarized light.**
>
> The textbook goes from "the first filter polarizes the light along its axis" straight to `I = I₀cos²θ` and **never states explicitly that unpolarized light loses half its intensity at the first filter**. That `½` is not in the source; this entry derives it by averaging `cos²θ`. In problems with several filters, decide at each step whether the incident light is unpolarized or already polarized.

**Polarization by reflection**: when light strikes a water or glass surface at an angle, the reflected light becomes partially polarized, with the component parallel to the surface (perpendicular to the plane of incidence) dominating. When the angle of incidence equals **Brewster's angle** `θ_b`, the reflected light is **completely polarized**, with its vibrations parallel to the surface:

`tan θ_b = n₂/n₁`

where `n₁` is the medium in which the incident and reflected light travel and `n₂` is the medium forming the reflecting interface. The textbook's values: air to water `θ_b = 53.1°`; air to crown glass `θ_b = 56.7°`.

**Polarization by scattering**: when light is scattered by air molecules, the electrons oscillate perpendicular to the incident direction and reradiate. Viewed perpendicular to the original ray, the scattered light is completely polarized perpendicular to that ray; in other directions it is only partially polarized. This is why rotating polarizing sunglasses while looking at the blue sky shows bright and dark changes.

**Optical activity**: substances such as sugar water, insulin, and collagen rotate the plane of polarization of light passing through them. The rotation depends on the substance, its concentration, the path length, and the wavelength. Measuring the rotation angle is a standard way to determine sugar concentration. Glass and plastic also become optically active when stressed (stress birefringence), which enables photoelastic stress analysis.

**Birefringence**: crystals such as calcite split an unpolarized beam into two beams, each with a definite polarization. The ray that obeys Snell's law is called the **ordinary ray**; the one that does not is the **extraordinary ray**. Another class of **dichroic** materials preferentially absorbs one of the two polarizations — this is how polarizing filters work.

**Liquid-crystal displays (LCDs)**: a liquid crystal rotates the polarization of light passing through it by about 90°, and an applied voltage switches that rotation off. Sandwiched between two polarizing filters with perpendicular axes, each pixel becomes a voltage-controlled light valve; adding red, green, and blue color filters gives a color display.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Waves](waves.en.md) — only transverse waves can be polarized; a longitudinal wave (such as sound in air) has no polarization direction |
| Prerequisite | [Refraction of light](refraction.en.md) — Brewster's law uses the index of refraction `n`, and the critical-angle and total-internal-reflection discussion also rests on Snell's law |
| Related · sibling entries | [Reflection of light](reflection-of-light.en.md), [Total internal reflection](total-internal-reflection.en.md), [Light interference and diffraction](light-interference-and-diffraction.en.md) — all belong to 选必一 chapter 4 "Light"; this entry fills its last gap |
| Recorded gap | **Circular and elliptical polarization**, **Stokes parameters and Jones matrices**, **degree of polarization and the quantitative description of partial polarization**, **the s- and p-components of the Fresnel reflection coefficients**, **the quantitative laws of optical activity (specific rotation)**, **birefringent wave plates and retardance**, **continuum models of liquid crystals and their voltage response**, **extinction ratio and angular dependence of polarizing filters**, and **single-photon polarization and quantum measurement** are not built in this library |
| Related technology | Polarizing sunglasses, photographic polarizing filters, LCD displays, sugar-concentration measurement, photoelastic stress analysis, polarization control in lasers |

## Arguments

### K1 · Malus's law comes from projecting the electric-field component (no attacks yet)

- **Claim**: polarized light of intensity `I₀` passing through an ideal polarizing filter has intensity `I = I₀cos²θ`, where `θ` is the angle between the incident polarization direction and the filter axis
- **Premises**: the filter axis passes only the parallel component; the transmitted amplitude is the incident amplitude times `cos θ`; wave intensity is proportional to amplitude squared; the textbook's account and its 90% reduction example (ev-174)
- **Reasoning**: let the incident field amplitude be `E`. The component along the axis is `E cos θ`, and the perpendicular component is absorbed. Since `I ∝ E²`, `I/I₀ = (E cos θ / E)² = cos²θ`. The textbook's example: a 90.0% intensity reduction means `I = 0.100I₀`, so `cos θ = √0.100 = 0.3162` and `θ = 71.6°`. Two further checks agree: `cos²45° = 0.500` (reduced to 50%) and `cos²18.4° = 0.900` (reduced to 90%)
- **Evidence**: ev-174
- **Attacked**: the formula assumes fully polarized incident light and an ideal filter (no absorption, infinite extinction ratio). Real filters absorb and leak, and `I₀` is the intensity incident on that filter, not the intensity of the source. For unpolarized light one must first average to get `½I₀`, a step the textbook does not write out
- **Signed by**: @hpleapfrog · 2026-10-21

### K2 · Brewster's angle makes the reflected light completely polarized (no attacks yet)

- **Claim**: for light travelling from `n₁` toward an interface with `n₂`, when the angle of incidence satisfies `tan θ_b = n₂/n₁`, the reflected light is completely polarized and the reflected and refracted rays are perpendicular
- **Premises**: Snell's law `n₁ sin θ₁ = n₂ sin θ₂`; at Brewster's angle the reflected and refracted rays make 90°, so `θ_b + θ₂ = 90°`; the textbook's statement of Brewster's law and its two worked examples (ev-174)
- **Reasoning**: substitute `θ₂ = 90° − θ_b` into Snell's law: `n₁ sin θ_b = n₂ sin(90° − θ_b) = n₂ cos θ_b`; dividing both sides by `n₁cos θ_b` gives `tan θ_b = n₂/n₁`. Numerical checks: air to water `tan θ_b = 1.333/1.00 = 1.333`, `θ_b = 53.1°`; air to crown glass `tan θ_b = 1.520/1.00 = 1.520`, `θ_b = 56.7°`; the reverse direction, water to crown glass, gives `tan θ_b = 1.520/1.333 = 1.140`, `θ_b = 48.8°`; crown glass to water gives `tan θ_b = 1.333/1.520 = 0.877`, `θ_b = 41.2°`. The two angles for opposite directions are complementary, since `arctan x + arctan(1/x) = 90°`
- **Evidence**: ev-174
- **Attacked**: this holds only at **exactly** `θ_b`; at other angles the reflected light is only **partially** polarized, which is why rotating sunglasses produces bright and dark changes rather than complete black. The order of `n₁` and `n₂` is easy to reverse; a rough interface, a coating, or absorption makes the complete polarization only approximate. The textbook writes only "It can be shown" and gives no derivation. This entry derives the law from the equivalent condition that the reflected and refracted rays are perpendicular; that condition itself follows rigorously from the vanishing of the p-component Fresnel reflection coefficient, which is not built in this library
- **Signed by**: @hpleapfrog · 2026-10-21

### K3 · Polarizing filters "sift" light by angle, so an inserted middle filter can change the result (no attacks yet)

- **Claim**: with several polarizing filters in series, each passes only the projection of the current polarization direction onto its axis; inserting a third filter between two crossed filters can let light through
- **Premises**: Malus's law; a polarizing filter does not change the polarization direction of the light it transmits (the transmitted light is polarized along that filter's axis); the textbook's 45° and three-filter examples (ev-174)
- **Reasoning**: let the intensity after the first filter be `I₁`. A second filter at `θ` gives `I₂ = I₁cos²θ`, and the transmitted light is polarized along the second axis; a third at `φ` relative to the second gives `I₃ = I₂cos²φ`. For two crossed filters (`θ = 90°`), `I₂ = 0`. Insert a middle filter at 45° to both: the 45° filter transmits `0.5I₁`, and the third filter (still 45° from the middle, 90° from the original direction) transmits `0.5I₁ × 0.5 = 0.25I₁`, the textbook's 25.0%. For orientations `θ` and `90° − θ`, `I + I′ = I₁(cos²θ + sin²θ) = I₁`
- **Evidence**: ev-174
- **Attacked**: the derivation assumes ideal filters that do not change the polarization direction; a real middle filter absorbs, so 25% is only an upper bound. The textbook sets this as a proof exercise but does not discuss losses in the filters themselves
- **Signed by**: @hpleapfrog · 2026-10-21

> [!IMPORTANT]
> **"Polarization" has two different meanings in physics — do not conflate them.**
>
> Polarization of light concerns the **direction of the electric field's oscillation**; the polarization of a dielectric in an electric field is the **small separation of positive and negative charge** (often rendered in Chinese as 极化). They are not the same thing. The textbook explicitly warns: `This is not the same type of polarization as that discussed for the separation of charges`. Moreover, longitudinal waves cannot be polarized, so the correct answer to whether a sound wave can be polarized is **no** — which is exactly the textbook's conceptual question.

> [!IMPORTANT]
> **The textbook's Critical Thinking item is unrelated to polarization, and its answers are off by a factor of ten.**
>
> The module's only Critical Thinking item is a diffraction-grating problem (a 400.0 nm laser and `1,000` lines etched over `10.00 mm`), not a polarization problem. Its solution takes the grating spacing as `10⁻⁶ m`, but the stem gives `10.00 mm / 1,000 = 1.0×10⁻⁵ m`, so all four answers (a)–(d) are off by a factor of ten: the first-order angle should be `arcsin 0.0400 = 2.29°` (the textbook says 23.6°), the second-order angle `arcsin 0.0800 = 4.59°` (the textbook says 53.1°), the wavelength inferred from 23.9° should be `4.05 μm` (the textbook says 405 nm), and doubling the line spacing should give 1.15° (the textbook says 11.5°). The solution also writes `θ = 0.400 = 23.6°` for `θ = sin⁻¹(0.400)` and mixes in `10⁻⁶ cm` in part (c). This entry does not quote those numbers.

> [!IMPORTANT]
> **The prose statement that "the electric field is strong compared with the magnetic field" compares quantities with different units.**
>
> The original sentence is `The electric field is strong compared with the magnetic field and is more effective in exerting force on charges in the molecules`. In SI, `E = cB`, so the numerical value of the electric field in V/m is indeed far larger than that of the magnetic field in T, but the two have different dimensions and cannot be said to be "stronger" than each other. The force on an electron in a molecule comes mainly from the electric field because the electron's speed is far below `c`, not because the electric field is intrinsically stronger. This entry keeps only the conclusion that the electric field dominates the force on charges.

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Entry created; fills in the polarization part of 选必一 chapter 4 "Light", which now covers reflection, refraction, interference and diffraction, total internal reflection, and polarization | Written after reading m42522 in full for ev-174 | @hpleapfrog |
