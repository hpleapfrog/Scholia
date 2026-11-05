---
id: kb:physics:gas-laws-and-ideal-gas-equation
type: 知识点
title: "Gas laws and the ideal-gas equation"
status: 待审
author: "AI（DeepSeek V4.1 Flash Free）· 待 @hpleapfrog 复核 · 2026-11-05"
created: 2026-11-05
updated: 2026-11-05
scope:
  学科: 物理
  学段: 高中
  适用: students who know pressure and temperature and need to handle `p-V-T-n` calculations and to recognise differences between Chinese and English law names
  条件: covers pressure and its units, Boyle's law, Charles's law (isochoric), Gay-Lussac's law (isobaric), Avogadro's law, the combined gas law and the ideal-gas equation, and STP and molar volume; the real-gas van der Waals equation, quantitative Dalton partial pressures, gas diffusion and effusion, and critical phenomena and phase diagrams are out of scope
edges:
  先修: ["[Temperature and temperature scales](temperature-and-scales.en.md)"]
  支持: []
  攻击: []
evidence: [ev-198]
license: CC-BY-SA-4.0
---

> **English version of [`气体实验定律与理想气体状态方程.md`](气体实验定律与理想气体状态方程.md).**

> [!TIP]
> **After reading this entry you should** be able to write `pV = nRT` and `p₁V₁/T₁ = p₂V₂/T₂`, convert correctly between `°C` and `K`, and explain why the Chinese "查理定律" and the English `Charles's law` are not the same law.

## Definition

### Pressure and its units

Gas pressure is the force per unit area exerted by molecules colliding with the container walls:

`p = F/A`

The SI unit is the pascal (Pa), `1 Pa = 1 N/m²`. Common units:

| Unit | Relation to Pa |
|---|---:|
| standard atmosphere `atm` | `1 atm = 101,325 Pa` |
| torr | `1 torr = (1/760) atm ≈ 133.322 Pa` |
| millimetre of mercury `mmHg` | `1 mmHg ≈ 1 torr` (the two are no longer exactly equal) |
| bar | `1 bar = 100,000 Pa` (exact) |
| pound per square inch `psi` | `1 psi ≈ 6,894.76 Pa` |
| inch of mercury `inHg` | `1 inHg = 3,386 Pa` (textbook rounding) |

Textbook conversion: `29.2 inHg = 742 torr = 0.976 atm = 98.9 kPa = 989 mbar`. Recomputing: `29.2 × 25.4 = 741.68 mm`; `741.68/760 = 0.9759 atm`; `0.9759 × 101.325 = 98.88 kPa`; `98.88 × 10 = 988.8 mbar`. The textbook's rounding agrees.

> [!NOTE]
> **Absolute pressure and gauge pressure (added here; m68750 does not use the word `gauge`).**
>
> An open-end manometer measures the difference between the gas pressure and atmospheric pressure: `p_gas − p_atm = ρgh`. If an instrument uses atmospheric pressure as its zero, its reading is the **gauge pressure** `p_gauge`; adding atmospheric pressure gives the **absolute pressure**:
>
> `p_abs = p_gauge + p_atm`
>
> The `p` in the gas laws must be the absolute pressure. Substituting gauge pressure directly into `pV = nRT` gives badly wrong results at low pressure or in vacuum problems.

### Four state variables and four empirical laws

A fixed amount of gas is described by four quantities: pressure `p`, volume `V`, temperature `T`, and amount of substance `n`. Each of the four empirical laws holds two of these fixed and relates the other two:

| Chinese name | Fixed | Relation | English name (as used in m68751) |
|---|---|---|---|
| Boyle's law (玻意耳定律) | `T`, `n` | `pV = constant`, `p₁V₁ = p₂V₂` | Boyle's law |
| Charles's law (查理定律) | `V`, `n` | `p/T = constant`, `p₁/T₁ = p₂/T₂` | Amontons's law / Gay-Lussac's law |
| Gay-Lussac's law (盖-吕萨克定律) | `p`, `n` | `V/T = constant`, `V₁/T₁ = V₂/T₂` | Charles's law |
| Avogadro's law (阿伏伽德罗定律) | `p`, `T` | `V/n = constant`, `V₁/n₁ = V₂/n₂` | Avogadro's law |

> [!WARNING]
> **Chinese and English law names cannot be mapped person-to-person.**
>
> The common Chinese high-school usage is:
>
> - **查理定律** = isochoric change, `p/T = constant`
> - **盖-吕萨克定律** = isobaric change, `V/T = constant`
>
> The English usage in m68751 is the opposite:
>
> - `Charles's law` = isobaric change, `V/T = constant`
> - `Amontons's law` or `Gay-Lussac's law` = isochoric change, `p/T = constant`
>
> So translating English `Charles's law` literally as "查理定律" swaps the two laws. The attribution of Gay-Lussac is not fully uniform in English either: some books call `p/T` Gay-Lussac, some call `V/T` Gay-Lussac, and some use the name for the combination. **This entry labels the English names as m68751 uses them and the Chinese names as Chinese high-school usage uses them; they are not a word-for-word correspondence.**
>
> **To be checked**: this library has not yet obtained a citable locator in the PEP (人教版) textbook. The Chinese naming above is organized from common Chinese high-school usage, not read directly from registered evidence. Until a textbook locator is in hand, it is not treated as established fact; see the gap table on this page.

### Combined gas law and the ideal-gas equation

Combining the four laws gives the **combined gas law** for a fixed amount of gas (`n` constant):

`p₁V₁/T₁ = p₂V₂/T₂`

Writing it with `n` included gives the **ideal-gas equation of state**:

`pV = nRT`

where `R` is the molar gas constant:

- `R = 8.314 J mol⁻¹ K⁻¹`
- `R = 8.314 kPa L mol⁻¹ K⁻¹`
- `R = 0.08206 L atm mol⁻¹ K⁻¹`

The three values are the same constant in different units. When choosing `R`, the units of `p`, `V`, and `T` must match it; this is one of the most common sources of error in gas calculations.

The ideal-gas equation also gives density and molar mass:

`ρ = m/V = pM/(RT)`

`M = mRT/(pV)`

where `m` is the gas mass and `M` the molar mass. These are algebraic rearrangements, not new laws.

### Standard conditions and molar volume

The textbook's standard temperature and pressure (STP) are `273.15 K` and `1 atm`. At these conditions, one mole of an ideal gas occupies

`V_m = RT/p = (0.082057 × 273.15)/1 = 22.414 L`

The textbook writes "about `22.4 L`." Note: IUPAC changed the standard pressure from `1 atm` to `1 bar` in 1982. At `1 bar` and `273.15 K`,

`V_m = (8.314 × 273.15)/100 = 22.711 L`

So "22.4 L" belongs only to the old `1 atm` STP; with the new `1 bar` standard, write "22.7 L." The difference is about 1.3%.

> [!IMPORTANT]
> **Every ratio formula requires thermodynamic temperature.**
>
> The `T` in `p/T`, `V/T`, and `pV/T` is kelvin temperature. Celsius can be used only for a **temperature difference**, not for a ratio. The textbook states at the gas laws: `temperatures must be on the kelvin scale for any gas law calculations`.
>
> Example: a spray can warms from `24 °C` to `50 °C`, and its pressure rises from `360 kPa` to what?
>
> `p₂ = p₁ T₂/T₁ = 360 × (50 + 273.15)/(24 + 273.15) = 360 × 323.15/297.15 = 391.5 kPa`
>
> To two significant figures, `390 kPa` (the textbook answer). If Celsius were used by mistake, `360 × 50/24 = 750 kPa`, nearly double.

> [!CAUTION]
> **Absolute zero is not "the temperature at which a gas has zero volume."**
>
> The glossary of m68751 defines absolute zero as "temperature at which the volume of a gas would be zero according to Charles's law." That is an extrapolation of the ideal-gas model: real gases liquefy or solidify before 0 K, and 0 K is unreachable. For the modern definition of absolute zero see [Temperature and temperature scales](temperature-and-scales.en.md); this entry only stresses: **do not treat the extrapolated point `V→0` as a physical fact.**

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Temperature and temperature scales](temperature-and-scales.en.md) — the ratio laws require `T` in kelvin; the Celsius zero cannot enter a ratio directly |
| Follow-up | [Kinetic-molecular theory](molecular-kinetic-theory.en.md) — explains these empirical laws through molecular collisions and gives the microscopic relation between `u_rms` and temperature |
| Follow-up | Solids and liquids (not yet built in this library) — moves from the ideal gas to condensed phases with intermolecular forces |
| Follow-up | [First law of thermodynamics](../../archive/knowledge/physics/concepts/thermodynamic-first-law.en.md) — gas work `W = pΔV`, internal energy, and heat bookkeeping |
| Recorded gap | **Real gases and the van der Waals equation**, **compressibility factor `Z`**, **quantitative Dalton partial pressures**, **gas diffusion and effusion (Graham's law)**, and **critical temperature and phase diagrams** are not built; the Chinese textbook locator for the law names is also not in the library, as noted under "To be checked" above |

## Argument

### K1 · The four empirical laws are special cases of the ideal-gas equation (no attack yet)

- **Claim**: with two state variables fixed, `pV = nRT` reduces to Boyle's, Charles's, Gay-Lussac's, and Avogadro's laws
- **Premise**: m68751 presents the four laws separately and combines them into `pV = nRT`; m68750 gives the pressure definition and unit conversions (ev-198)
- **Reasoning**:
  - fix `T`, `n`: `pV = nRT = constant` → Boyle's law
  - fix `V`, `n`: `p = (nR/V)T` → `p/T = constant` → Charles's law (isochoric)
  - fix `p`, `n`: `V = (nR/p)T` → `V/T = constant` → Gay-Lussac's law (isobaric)
  - fix `p`, `T`: `V = (RT/p)n` → `V/n = constant` → Avogadro's law
- **Evidence**: ev-198
- **Attacked**: the textbook says "combining these four laws yields the ideal gas law" but does not show the combination. Each of the four laws supplies only a proportionality constant; by themselves they do not uniquely determine `R`. One must also assume that these constants are proportional to `n` and can be written as the same `nR`. That is a **modeling choice**, not pure logic. The textbook also does not state that each law holds only approximately at low pressure/high temperature
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

### K2 · Ratio calculations require kelvin temperature (no attack yet)

- **Claim**: `p/T`, `V/T`, and `pV/T` hold only when `T` is thermodynamic temperature; using Celsius gives systematic errors
- **Premise**: m68751 requires kelvin at every law and writes `temperatures must be on the kelvin scale for any gas law calculations`; the spray-can example gives `24 °C → 50 °C`, `360 kPa → 390 kPa`; the CO₂ example gives `0.300 L`, `10 °C → 30 °C`, `0.321 L` (ev-198)
- **Reasoning**: the Celsius zero is the freezing point of water, an arbitrary reference; a ratio law needs a true zero. Recomputing the spray can: `360 × 323.15/297.15 = 391.5 kPa`, or `390 kPa` to two significant figures. Recomputing CO₂: `0.300 × 303.15/283.15 = 0.3212 L`, matching the textbook's `0.321 L`. With Celsius, the spray can would give `750 kPa` and CO₂ would give `0.900 L` (actual about `0.321 L`), which is absurd
- **Evidence**: ev-198
- **Attacked**: the textbook glossary defines absolute zero as "the temperature at which the volume would be zero," which is circular; it uses Charles's law to define absolute zero and then uses absolute zero to explain Charles's law. The textbook also writes `25 °C` as `298 K` (dropping `.15`), harmless in most high-school problems but about a `0.05%` error in precise `pV = nRT` calculations. This entry keeps `.15` and rounds according to significant figures in the examples
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

### K3 · The ideal-gas equation is a limiting law, not a universal truth (no attack yet)

- **Claim**: `pV = nRT` is exact only as pressure tends to zero; real gases deviate at high pressure/low temperature
- **Premise**: m68751 calls the ideal gas `a hypothetical construct` and says the equation is `quite accurate for low pressures and moderate temperatures`; in the `153 atm` scuba example it adds `the assumption of ideal gas behavior is not very reasonable` (ev-198)
- **Reasoning**: real molecules have finite volume and attract one another. Define the compressibility factor `Z = pV/(nRT)`: for an ideal gas `Z = 1`; at low pressure `Z → 1`; at moderate pressure attraction makes `Z < 1`; at high pressure the repulsion of molecular volumes makes `Z > 1`. Thus `pV = nRT` is the `p → 0` limit, not an identity at all pressures (the `Z` details are added here; m68751 gives only the qualitative low-pressure/high-temperature boundary)
- **Evidence**: ev-198
- **Attacked**: the textbook says the ideal gas holds only at low pressure/high temperature, then uses a `153 atm` scuba tank as an example and adds only one sentence that the assumption is "not very reasonable." Students easily read "the example can be calculated" as "the equation holds universally." This entry writes the domain into `scope.条件` and uses `Z` as the entry point for judging deviation
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

### K4 · `22.4 L` belongs to `1 atm` STP, not to `1 bar` (no attack yet)

- **Claim**: one mole of ideal gas occupies `22.414 L` at `273.15 K`, `1 atm`, and `22.711 L` at `273.15 K`, `1 bar`
- **Premise**: m68751 writes `At STP, one mole of an ideal gas has a volume of about 22.4 L` and notes that IUPAC changed the standard pressure from `1 atm` to `1 bar` in 1982, while the textbook still uses the old definition (ev-198)
- **Reasoning**: `V_m = RT/p`. With `1 atm = 101,325 Pa`, `V_m = 8.314×273.15/101.325 = 22.414 L`; with `1 bar = 100,000 Pa`, `V_m = 8.314×273.15/100 = 22.711 L`. The difference is `0.297 L`, about `1.3%`
- **Evidence**: ev-198
- **Attacked**: the textbook says only "about 22.4 L," gives no value at `1 bar`, and does not warn that "STP" has different definitions at different institutions. A student using `22.4 L` under the new `1 bar` standard makes the molar volume about `1.3%` too small; in gas molar-mass or stoichiometry calculations, that error propagates directly into the result. This entry lists both values so that "22.4" is not treated as an unconditional constant
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-11-05 | Entry created; supplies the gas-law part of chapter 2 of elective-3, "gases, solids, and liquids", after temperature and scales | written after reading m68750 / m68751 in full (ev-198); `391.5 kPa`, `0.3212 L`, `22.414 L`, `22.711 L`, and the `29.2 inHg` unit conversion are recomputed here | AI (DeepSeek V4.1 Flash Free) |
