---
id: kb:physics:light-interference-and-diffraction
type: 知识点
title: "Light interference and diffraction"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned refraction and need to understand double-slit and single-slit patterns, diffraction gratings, and the resolution limit
  条件: covers only the basics of wave optics — Huygens's principle, double-slit and single-slit interference, diffraction gratings, circular-aperture diffraction, and the Rayleigh criterion; polarization, coherence length and coherence time, the quantitative double-slit intensity formula, thin-film interference, and the quantum account of single-photon interference are not built here
edges:
  先修: ["[Waves](waves.en.md)", "[Refraction of light](refraction.en.md)"]
  支持: []
  攻击: []
evidence: [ev-171, ev-172]
license: CC-BY-SA-4.0
---

> **English version of [`光的干涉与衍射.md`](光的干涉与衍射.md).**

> [!TIP]
> **After reading this entry you should** be able to locate double-slit and grating maxima with `d sinθ = mλ`, locate single-slit minima with `D sinθ = mλ`, use `θ = 1.22λ/D` to explain why a larger aperture resolves more detail, and explain roughly what it means that interference and diffraction are two descriptions of one thing

## Definition

**When light's wave behavior shows**: light travels in straight lines and acts like a ray when it meets objects much larger than its wavelength; when it meets objects about as large as the wavelength, interference and diffraction become pronounced. **Interference is the identifying behavior of a wave** — waves from two slits (or more) overlap on a screen, adding constructively (bright) where the path difference is an integer number of wavelengths and destructively (dark) where it is a half-integral number. **Diffraction** is the bending of a wave around the edges of an opening into the geometric shadow; the narrower the opening (the closer to the wavelength), the stronger the bending.

**Wavelength in a medium**: when light passes from vacuum into a medium of refractive index `n`, the frequency `f` stays the same and the wavelength becomes

`λ_n = λ/n`

Color follows frequency, so it does not change in water, but the wavelength shrinks (green `550 nm` light is about `414 nm` in water).

**Huygens's principle**: every point on a wavefront can be treated as a new source emitting spherical wavelets that travel forward at the wave speed `v`, covering `s = vt` after time `t`; the new wavefront is the envelope of all the wavelets. To find where light goes after passing an opening, add the wavelets point by point.

**Double-slit interference** (Young, 1801): two closely spaced slits split one beam into two coherent sources. The path difference from the two slits to a point on the screen is `d sinθ` (`d` is the slit separation, `θ` is measured from the central axis, and the screen is far away). Hence

- constructive: `d sinθ = mλ`, `m = 0, ±1, ±2, …`
- destructive: `d sinθ = (m + ½)λ`, `m = 0, ±1, ±2, …`

`m` is the order. The textbook uses He-Ne laser light with `d = 0.0100 mm` and the third bright line at `10.95°` to recover `633 nm`, and notes that this is how interference patterns measure wavelength. Fringe intensity decreases with angle, but the textbook only describes this qualitatively.

**Single-slit diffraction**: a slit of width `D` produces a wide, bright central maximum with dimmer and narrower secondary maxima on either side. The minima are at

`D sinθ = mλ`, `m = ±1, ±2, …` (`m` cannot be 0)

For a nearby screen or small angles one may use `Dy/L = mλ` (`L` is the slit-to-screen distance and `y` the distance from the center to the minimum); the textbook writes only the first minimum as `Dy/L = λ`. The central maximum is twice as wide as a secondary maximum. From `550 nm` light with its second minimum at `45.0°` the textbook recovers `D = 1.56 μm`.

**Diffraction grating**: many evenly spaced parallel slits (spacing `d`). The bright-line condition is the same as for two slits,

`d sinθ = mλ`

but the more slits there are, the narrower and brighter the bright lines and the darker the gaps, so a grating separates wavelengths far better than two slits. With white light the center (`m = 0`) stays white and higher orders spread white light into a band from violet to red. Scratching glass with a sharp tool makes a transmission grating; the spiral groove of a CD and the microstructures of opal and butterfly wings are reflection gratings, and their iridescence comes from constructive interference of different wavelengths at different angles. The textbook uses `520 nm` light and `d = 5,000 nm` (about 2,000 lines per millimeter) to put the first-order line at `5.97°`.

**The diffraction limit of resolution**: the pattern of a circular aperture of diameter `D` is a central bright spot surrounded by dark rings, with the first minimum at

`θ = 1.22 λ/D`

with `θ` in radians. **The Rayleigh criterion**: two point sources are just resolvable when the center of one pattern falls on the first minimum of the other, so the smallest resolvable angular separation is `1.22λ/D`. The shorter the wavelength and the larger the aperture, the higher the resolution. The textbook uses a `633 nm` He-Ne beam `1.00 mm` in diameter to get `7.72×10⁻⁴ rad = 0.0442°`. Every lens or mirror is limited this way: a telescope by the diameter of its primary mirror, the eye by the pupil. **Perfect resolution does not exist** — however large the aperture or short the wavelength, the image is always blurred to some degree.

> [!IMPORTANT]
> **The textbook says a CD has "1,600 grooves in a millimeter", contradicting its own 1,600 nm pitch.**
>
> The source writes `they are extremely narrow—1,600 in a millimeter`, while the same passage gives the groove pitch as `1,600 nm`. A 1,600 nm pitch is 625 grooves per millimeter, not 1,600. This entry uses the `1,600 nm` pitch (consistent with the usual CD track pitch) and does not use the "1,600 per millimeter" density.

> [!IMPORTANT]
> **The textbook's Concept Items print the Rayleigh criterion as `θ = λ/D`, dropping the 1.22.**
>
> The same module's body text, Key Equations, and the correct choice in the same Concept Items all write `θ = 1.22λ/D`. `λ/D` is the angular position of a single slit's first minimum; the first minimum of a **circular aperture** of diameter `D` is at `1.22λ/D`, and the extra 1.22 comes from the circular geometry. This entry always uses `1.22λ/D` for resolution and `λ/D` for a single slit, never mixing the two.

> [!IMPORTANT]
> **The two modules give different visible ranges.**
>
> m54369 writes `380 to 750 nm` and m54371 writes `380–780 nm`. Both are approximate textbook endpoints; this entry follows `380–750 nm` and, when citing m54371's 780 nm, only notes the difference without treating either endpoint as a precise physical boundary.

> [!IMPORTANT]
> **m54369's teacher note contains two slips.**
>
> The source writes `Note that the sign of an angle is always ≥ 1`: the range of the sine is `0 ≤ sinθ ≤ 1`, and in single-slit diffraction `θ` runs from `0°` to `90°`, so `sinθ` never exceeds 1; the source wrote "sign" for "sine". The same note also misspells `λ` as `lamda`. This entry uses the correct statements.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Waves](waves.en.md) — wavelength, frequency, interference, and diffraction are the conceptual basis of wave optics |
| Prerequisite | [Refraction of light](refraction.en.md) — `n = c/v` is the origin of the refractive index in `λ_n = λ/n` |
| Recorded gap | **Polarization**, **coherence length and coherence time**, the **quantitative double-slit intensity formula**, **thin-film interference**, the **quantum account of single-photon interference**, and the **Abbe resolution formula and concrete telescope/microscope parameters** are not built in this library; the textbook modules give only the qualitative statement that interference intensity falls off with angle |
| Related technology | Laser readout and tracking in CD/DVD drives, grating spectroscopes and monochromators, DIC microscopy, wavelength selection in optical-fiber devices |
| Neighboring entry | [Wave-particle duality](wave-particle-duality.en.md) — interference and diffraction are the evidence for wave behavior, while photon momentum and the photoelectric effect are the evidence for particle behavior |

## Arguments

### K1 · Double-slit maxima satisfy `d sinθ = mλ`, which can be inverted to measure wavelength (no attacks yet)

- **Claim**: Two coherent slits give a path difference `d sinθ` at a point on the screen; an integer number of wavelengths gives constructive interference and a half-integral number gives destructive interference, so the `m`th bright line satisfies `d sinθ = mλ` and measuring `θ` gives `λ`
- **Premises**: Young's 1801 double-slit experiment; with a distant screen the angle `θ` is nearly the same for both slits; the He-Ne example (`d = 0.0100 mm`, `m = 3`, `θ = 10.95°` → `633 nm`) (ev-171)
- **Reasoning**: Both slits are illuminated by the same wavefront and emit in-phase wavelets; the path difference to a point on the screen is `d sinθ`. At `mλ` crest meets crest and at `(m + ½)λ` crest meets trough. Substituting `0.0100 mm × sin 10.95° / 3` gives `6.33×10⁻⁴ mm = 633 nm`, matching the known He-Ne wavelength, so the formula and the distant-screen approximation work under these conditions
- **Evidence**: ev-171
- **Attacked**: The formula assumes infinitely narrow slits, monochromatic light, an infinitely distant screen, and a slit separation much larger than the wavelength; a finite slit width modulates the fringes with a single-slit envelope, and the module only says intensity falls off with angle; the `Dy/L` form of the single-slit result relies on a small-angle approximation and must return to `sinθ` at large angles
- **Signed by**: @hpleapfrog · 2026-10-21

### K2 · Single-slit minima satisfy `D sinθ = mλ`, and the central maximum is twice as wide as a secondary one (no attacks yet)

- **Claim**: For a slit of width `D`, the `m`th minimum (`m` a nonzero integer) is at `D sinθ = mλ`; the central maximum lies between the two first minima and is twice as wide as a secondary maximum
- **Premises**: The textbook's pairing argument, in which two rays `D/2` apart differ by `λ/2` when `D sinθ = λ` and cancel; the `550 nm`, `m = 2`, `45.0°` → `1.56 μm` example (ev-171)
- **Reasoning**: At `D sinθ = λ`, every ray in the upper half of the slit has a partner in the lower half differing by `λ/2`, so the whole slit cancels and the first minimum appears. The central maximum runs from `−λ/D` to `+λ/D`, an angular width of `2λ/D`, while a secondary maximum between adjacent minima is only `λ/D` wide, hence half as wide. Substituting `2 × 550 nm / sin 45.0°` gives `1.56 μm`
- **Evidence**: ev-171
- **Attacked**: The textbook's `Dy/L = λ` states only the first minimum and must be written `mλ` for higher orders; the `45.0°` example cannot use the small-angle approximation, and the textbook correctly uses `D sinθ` rather than `Dy/L`; the module gives no single-slit intensity formula, and statements such as the central maximum being six times higher appear only in a figure note
- **Signed by**: @hpleapfrog · 2026-10-21

### K3 · A grating separates wavelengths: `d sinθ = mλ`, and higher orders spread farther (no attacks yet)

- **Claim**: A grating of many evenly spaced slits produces narrow bright lines at `d sinθ = mλ`; at a given order `θ` grows with `λ`, so white light is spread into a spectrum; the 1,600 nm grooves of a CD form a reflection grating
- **Premises**: The grating equation; the statement that grating lines are narrower and brighter than double-slit fringes; the `520 nm`, `d = 5,000 nm` (about 2,000 lines per millimeter) → `5.97°` example; the 1,600 nm CD groove pitch and the rainbow (ev-172)
- **Reasoning**: Every slit sends a wavelet in the same direction, and at `d sinθ = mλ` all their contributions add in phase. The more slits `N`, the narrower the constructive direction (width roughly proportional to `1/N`), which is why grating lines are sharper than double-slit fringes. With `d` fixed, `sinθ ∝ λ`, so red light at a given order has a larger `θ` than blue, spreading white light into a spectrum; at `m = 0`, `θ = 0` for every wavelength, so the center stays white
- **Evidence**: ev-172
- **Attacked**: The grating equation assumes normal incidence, infinitely narrow slits, and monochromatic light; real gratings have missing orders, blaze angles, and polarization dependence; the textbook writes the CD groove density as "1,600 per millimeter", contradicting the 1,600 nm pitch; the textbook does not derive the `1/N` width, so this entry states it only as an order-of-magnitude remark
- **Signed by**: @hpleapfrog · 2026-10-21

### K4 · Diffraction sets a resolution floor of `θ = 1.22λ/D` (no attacks yet)

- **Claim**: For a circular aperture or lens of diameter `D`, two point sources closer than `1.22λ/D` cannot be resolved; shorter wavelengths and larger apertures give higher resolution
- **Premises**: The circular-aperture pattern of a central maximum and dark rings with the first minimum at `1.22λ/D`; the Rayleigh criterion (one pattern's central maximum on the other's first minimum); the `633 nm`, `1.00 mm` → `7.72×10⁻⁴ rad = 0.0442°` example (ev-172)
- **Reasoning**: Each point source forms a diffraction pattern. When the patterns overlap and one central maximum falls inside the other's central spot, the combined pattern has a single peak and the detector cannot tell that there are two sources; taking the first minimum's angular position as the smallest resolvable separation gives `1.22λ/D`. A smaller `λ` or a larger `D` makes this angle smaller and resolves finer detail
- **Evidence**: ev-172
- **Attacked**: The Rayleigh criterion is a convention rather than a hard threshold, and it assumes two equal-intensity sources, a circular aperture, no aberrations, and no atmospheric turbulence; real systems are also limited by aberrations, scattering, and detector noise. The textbook's Concept Items print the expression as `θ = λ/D` (missing 1.22), contradicting the body text; for a single slit the first minimum really is at `λ/D`, and the two cases must not be mixed. The module also gives neither the Abbe formula nor numbers for a specific telescope
- **Signed by**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-21 | Entry created; fills in the interference and diffraction part of 选必一 chapter 4 "Light", attached after waves and refraction | Written after reading m54369 and m54371 in full for ev-171 and ev-172 | @hpleapfrog |
