---
id: kb:physics:kp-speed-of-sound
type: 知识点
title: "Speed of sound and frequency"
status: 有效
author: "@hpleapfrog"
created: 2026-10-05
updated: 2026-10-18
scope:
  学科: 物理
  学段: 高中
  范围: acoustics

edges:
  先修: ["[波](waves.en.md)"]
  支持: []
  攻击: []
evidence: [ev-027]
license: CC-BY-SA-4.0
---

> **English version of [`声速与频率.md`](声速与频率.md).**

> [!TIP]
> **After reading this entry you should** be able to explain that the speed of sound is finite and measurable, and point out that the speed of sound depends on the medium, not on the frequency

## Definition

**Sound is a mechanical wave** and must propagate through a **medium** — no medium, no sound.
More precisely: sound is a **disturbance of matter transmitted outward from its source**. The vibrating source
compresses the surrounding air and releases it again, creating alternating **compressions** and **rarefactions** —
the longitudinal-wave versions of crests and troughs.

**The speed of sound is a finite, measurable quantity**, and it is **far less than the speed of light**.

The speed of sound is fixed by **two properties of the medium together**: its **rigidity** (compressibility, for gases) and its **density**.

- the more **rigid** (harder to compress), the higher the speed of sound; the more **dense**, the lower
- solids are both dense and rigid; on balance sound is usually **faster** in them; gases are compressible, so it is slow
- hence: very high in glass, aluminum, and steel; very low in rubber

| Medium | Speed of sound `v` (m/s) |
|---|---|
| Air (0 °C) | 331 |
| Helium | 965 |
| Water (20 °C) | 1480 |
| Human tissue | 1540 |
| Vulcanized rubber | 54 |
| Steel | 5960 |

> [!IMPORTANT]
> **Do not explain the speed of sound by density alone.** (ev-027)
> The textbook warns that students flip-flop between "rigidity" and "density":
> solids are **denser** than gases (which would slow sound down) but far more **rigid** (which speeds it up),
> and **the outcome depends on the combination**. Memorising only "dense means slow" or "rigid means fast"
> will misfire whenever two media are compared.

**Frequency and wavelength** — for every wave:

```
v = f λ
```

- the **wavelength** is the distance between adjacent identical parts of the wave; for sound, between adjacent **compressions**
- the **frequency is set by the source**: a tuning fork vibrating at some frequency produces sound waves at that same frequency
- the speed of sound is **nearly independent of frequency**. The textbook's neat argument: in a stadium, the low and high
  instruments of a distant band always arrive **together** — if high frequencies travelled faster, the low instruments would lag
- in a given medium at fixed temperature and humidity `v` is constant, so `f` and `λ` are **inversely related**: higher frequency, shorter wavelength
- crossing into another medium, `f` stays the same (the wave is a driven oscillation keeping its source frequency), `v` changes, so `λ` must change: **higher speed, longer wavelength for a given frequency**

> [!NOTE]
> **How long are audible wavelengths?** (ev-027 worked example)
> With `v = 348.7 m/s` over the audible range 20 Hz – 20,000 Hz:
> `λ_max = 348.7 ÷ 20 ≈ 17 m` (longer than a classroom), `λ_min = 348.7 ÷ 20,000 ≈ 0.017 m` (about 2 cm).
> Two perceived quantities worth pairing with this: **loudness** tracks amplitude, **pitch** tracks frequency.

> [!NOTE]
> **Echolocation: turning "the speed of sound is finite" into a ruler.** (ev-027)
> Bats, dolphins and whales emit a sound and listen for its echo: **the round-trip time times the speed of sound
> is twice the distance**; the tiny delay between the two ears gives the direction. Humans copied the principle into
> SONAR (depth sounding, submarine detection), radar (using radio echoes instead), and the parking sensors on some cars —
> all of them just "constant speed ⇒ time works as a ruler".

## Relations

| Object | Entry | Note |
|---|---|---|
| **prerequisite** | [wave](waves.en.md) | "sound is a mechanical wave and needs a medium" — the starting point of this knowledge point |
| teaching method | [speed of sound and frequency · BL: first establish "mechanical waves need a medium"](../methods/sound-bl-mechanical-wave.en.md) | prerequisite concept |
| teaching method | [speed of sound and frequency · AL: estimating the speed of sound with "see the lightning first, hear the thunder later"](../methods/sound-al-thunder-lag.en.md) | derive a finite speed from an everyday phenomenon |

> [!TIP]
> **"See the lightning first, hear the thunder later" is natural evidence.**
> The textbook uses this everyday phenomenon to have students derive for themselves that "the speed of sound is finite and far less than the speed of light" —
> no instrument is needed, only a real thunderstorm (or fireworks).

## Argument

### K8 · Why listed separately (no attack yet)

- **Claim**: speed of sound and frequency deserves to be a separate knowledge point
- **Premise**: the textbook devotes a separate section to it and gives three tiers of teaching hints (ev-027)
- **Reasoning**: it has an independent prerequisite (classification and properties of waves) and an independent experimental path (estimating the speed of sound)
- **Evidence**: ev-027
- **Attacked**: together with "properties of waves" and "interference of sound" it belongs to acoustics; the boundaries may overlap
- **Attribution**: @hpleapfrog · 2026-10-05

## Change log

| Date | Action | Basis | Who |
|---|---|---|---|
| 2026-10-05 | established the entry (#8 batch conversion · batch 1) | Issue #8 | @hpleapfrog |
| 2026-10-05 | **attached the `先修` edge** — the teaching-method entry had always said "first establish that mechanical waves need a medium"; now the graph has this edge | 本库缺口修复 | @hpleapfrog |
| 2026-10-18 | learner half expanded: compressions/rarefactions, speed set by rigidity × density together, `v = f λ` and the inverse relation, audible-wavelength example, echolocation | weak-entry expansion · m54331 re-read (ev-027) | @hpleapfrog |
