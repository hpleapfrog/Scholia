---
id: kb:physics:total-internal-reflection
type: 知识点
title: "Total internal reflection"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned refraction and Snell's law and need to understand the critical angle, the conditions for total internal reflection, and phenomena such as optical fibers and diamond sparkle
  条件: covers only the critical angle, the conditions for total internal reflection, and its applications (optical fibers, endoscopes, diamond, corner reflectors); dispersion and the rainbow, thin-film interference, evanescent waves and the Goos–Hänchen shift, and the quantitative Fresnel reflectance are not built here
edges:
  先修: ["[Refraction of light](refraction.en.md)"]
  支持: []
  攻击: []
evidence: [ev-173]
license: CC-BY-SA-4.0
---

> **English version of [`全反射.md`](全反射.md).**

> [!TIP]
> **After reading this entry you should** be able to compute the critical angle with `sin θ_c = n₂/n₁` (for `n₁ > n₂`), state the two conditions that total internal reflection requires, and explain why an optical fiber makes its core index higher than its cladding and why diamond sparkles more than glass

## Definition

When light travels from a medium of index `n₁` toward a medium of index `n₂`, the law of refraction is

`n₁ sin θ₁ = n₂ sin θ₂`

with both angles measured from the normal. If `n₁ > n₂` (light going from the denser to the less dense medium), then `θ₂ > θ₁`: the refracted ray bends away from the normal. As the incident angle grows the refracted angle grows too, but **the refracted angle can reach at most 90°** — beyond that there is no refracted ray at all.

The **critical angle** `θ_c` is defined as the incident angle that makes the refracted angle exactly 90°. Setting `θ₂ = 90°` and `sin 90° = 1`, Snell's law gives

`n₁ sin θ_c = n₂`, that is `sin θ_c = n₂/n₁` (only for `n₁ > n₂`)

**Total internal reflection**: when the incident angle is **greater than** the critical angle, there is no refracted ray at the boundary and all the light is reflected back into medium 1. The textbook's wording is that "all the light is reflected back into medium 1".

Total internal reflection requires two conditions together:

1. light travels from the denser to the less dense medium (`n₁ > n₂`);
2. the incident angle exceeds the critical angle (`θ₁ > θ_c`).

If `n₁ < n₂`, then `n₂/n₁ > 1`, no critical angle exists, and total internal reflection cannot occur. At `θ₁ = θ_c` the refracted ray grazes along the boundary — the boundary case of "just able to get out".

Two useful values (the textbook's worked example and this entry's recomputation):

- water to air: `n₂/n₁ = 1.0003/1.333 = 0.7504`, so `θ_c = 48.63° ≈ 48.6°`;
- diamond to air: `n₂/n₁ = 1.0003/2.419 = 0.4135`, so `θ_c ≈ 24.4°`.

**Applications**:

- **Diamond sparkle**: the critical angle is only 24.4°, so most internal surfaces of a cut diamond satisfy `θ > θ_c`; light can leave only through a few facets. The cut deliberately makes light reflect internally many times and concentrates it at those exits, so a diamond sparkles more than glass.
- **Corner reflector**: a structure of two reflecting surfaces at a right angle sends light back close to its arrival direction. Bicycle and car reflector buttons and road signs use it; binoculars and submarine periscopes use totally reflecting prisms as "perfect mirrors".
- **Optical fibers**: the core index is greater than the cladding index, and light travels nearly along the axis, so it strikes the side wall at a large incident angle (`θ > θ_c`) and is totally reflected; light is thus confined to the core and follows bends. Telephone, internet, and cable-TV signals are transmitted this way.
- **Endoscope**: a bundle of fibers goes into a body cavity, light goes in and images come out, and doctors use it to examine, take biopsies, or remove polyps.

> [!IMPORTANT]
> **The textbook prints the "fixed value" of the speed of light in vacuum as `2.9972458×10⁸ m/s`, one 9 short.**
>
> The source writes `c = 2.9972458×10⁸ m/s ≈ 3.00×10⁸ m/s`. The exact value is `2.99792458×10⁸ m/s`. This entry uses only the three-digit `3.00×10⁸ m/s` and does not quote the erroneous digits.

> [!IMPORTANT]
> **"Two mutually perpendicular reflecting surfaces send light back exactly parallel" holds only in two dimensions.**
>
> The textbook says `two mutually perpendicular reflecting surfaces` return light `exactly parallel to the direction from which it came`, `independent of the angle of incidence`. That is true for rays lying in the plane perpendicular to the line where the mirrors meet; but if the ray has any component along that line, the component survives both reflections and the outgoing direction is not antiparallel to the incoming one. A three-dimensional retroreflector needs **three** mutually perpendicular faces (a corner cube), which is exactly what bicycle and car reflector buttons are. This entry follows the three-face statement and treats the two-dimensional case as a geometric model only.

> [!IMPORTANT]
> **The textbook has three further slips.**
>
> It misspells `indices` as `indicies` twice; the Section Summary says `total internal refraction` where it means reflection; and the Key Equations cell for `Snell's law in terms of speed` begins with a stray `>`. This entry uses the correct spellings and wording.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Refraction of light](refraction.en.md) — `n = c/v` and Snell's law are the starting point for deriving total internal reflection |
| Recorded gap | **Dispersion and the rainbow** (covered in the same chapter of m54365 but not built here), **prisms and the angle of minimum deviation**, **evanescent waves and the Goos–Hänchen shift**, **the Fresnel formulas and reflectance versus angle**, **numerical aperture, step-index versus graded-index fibers, and fiber modes**, and **polarization of light** are not built in this library |
| Related technology | Fiber-optic communications, medical endoscopes, diamond cutting, corner reflectors (bicycle and car reflector buttons, road signs, binoculars, periscopes) |

## Arguments

### K1 · The critical angle follows from Snell's law at `θ₂ = 90°` (no attacks yet)

- **Claim**: For light going from `n₁` to `n₂` with `n₁ > n₂`, the incident angle that makes the refracted angle 90° satisfies `sin θ_c = n₂/n₁`
- **Premises**: Snell's law `n₁ sin θ₁ = n₂ sin θ₂`; `sin 90° = 1`; water-to-air data `n₁ = 1.333`, `n₂ = 1.0003` and diamond-to-air `n₁ = 2.419` (ev-173)
- **Reasoning**: Substituting `θ₂ = 90°` into Snell's law gives `n₁ sin θ_c = n₂`, and dividing by `n₁` gives the result. Water to air: `1.0003/1.333 = 0.7504`, whose arcsine is `48.63°`; diamond to air: `1.0003/2.419 = 0.4135`, whose arcsine is `24.42°`. Both agree with the textbook's 48.6° and 24.4°
- **Evidence**: ev-173
- **Attacked**: The formula assumes a flat boundary, uniform indices on both sides, and no absorption; the critical-angle example uses `n_air = 1.0003` while the module's own table gives 1.000293, so rounding makes 48.63° versus 48.6°; the formula has a solution only when `n₁ > n₂`
- **Signed by**: @hpleapfrog · 2026-10-21

### K2 · Total internal reflection requires denser-to-rarer travel and an angle beyond the critical angle (no attacks yet)

- **Claim**: Total internal reflection happens only when `n₁ > n₂` and `θ₁ > θ_c`; then there is no refracted ray and all the incident energy returns to medium 1
- **Premises**: The refracted angle increases monotonically with the incident angle and is at most 90°; Snell's law; the textbook's statements that the ray bends away from the normal when `n₂ < n₁` and that all the light is reflected when `θ₁ > θ_c` (ev-173)
- **Reasoning**: From Snell's law, `sin θ₂ = (n₁/n₂) sin θ₁`. When `θ₁ > θ_c`, `(n₁/n₂) sin θ₁ > 1`, so `sin θ₂` cannot exceed 1: the equation has no real solution and no refracted ray exists, leaving the energy to return along the reflected direction. If `n₁ < n₂`, then `n₂/n₁ > 1`, the critical angle is undefined, and total internal reflection cannot occur
- **Evidence**: ev-173
- **Attacked**: The textbook states "no refracted ray" as a conclusion for an ideal interface; it does not discuss the evanescent wave near the critical angle or the Goos–Hänchen shift, nor does it give a reflectance curve. Real surfaces with roughness, absorption, and scattering spoil total internal reflection. This entry uses the ideal model and records these details as gaps
- **Signed by**: @hpleapfrog · 2026-10-21

### K3 · Applications of total internal reflection depend on the size of the critical angle (no attacks yet)

- **Claim**: The smaller the critical angle, the easier it is to confine light inside a totally reflecting structure; diamond's 24.4°, the core-cladding index difference of a fiber, and the right-angle geometry of a corner reflector all apply the critical-angle condition to guiding or retroreflecting light
- **Premises**: The critical-angle formula; diamond `n = 2.419` and 24.4°; a fiber core index above the cladding index; two (three in three dimensions) mutually perpendicular reflecting faces of a corner reflector; the textbook's application passages (ev-173)
- **Reasoning**: `θ_c` is set by `n₂/n₁`, so a larger `n₁` relative to `n₂` gives a smaller `θ_c`. Diamond's `θ_c = 24.4°` means light inside is totally reflected whenever it strikes an inner surface beyond 24.4°, and the cut makes light bounce repeatedly and exit through only a few faces, concentrating the sparkle. In a fiber the core index slightly exceeds the cladding index; light travels near the axis and strikes the side wall at angles close to 90°, far beyond the critical angle, so it is confined by total internal reflection and follows bends as long as the incident angle stays above `θ_c`
- **Evidence**: ev-173
- **Attacked**: The textbook says two perpendicular faces suffice to send light back "exactly parallel", but a three-dimensional retroreflector needs three mutually perpendicular faces; "perfect mirror" ignores end reflections, absorption, and scattering; bending loss, modal dispersion, and numerical aperture are not developed; and "the fiber is thin, so total internal reflection is easy" is too simple a causal story — the deciding factors are the incident angle and the core-cladding index difference, not the diameter itself
- **Signed by**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Entry created; attached after refraction, filling in the total-internal-reflection part of 选必一 chapter 4 "Light" | Written after reading m54365 in full for ev-173 | @hpleapfrog |
