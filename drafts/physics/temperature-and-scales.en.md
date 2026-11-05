---
id: kb:physics:temperature-and-scales
type: 知识点
title: "Temperature and temperature scales"
status: 待审
author: "AI（DeepSeek V4.1 Flash Free）· 待 @hpleapfrog 复核 · 2026-11-05"
created: 2026-11-05
updated: 2026-11-05
scope:
  学科: 物理
  学段: 高中
  适用: students who can read a thermometer and need to distinguish temperature, heat, and thermal equilibrium, and to convert among Celsius, Fahrenheit, and Kelvin
  条件: covers the operational definition of temperature, thermal equilibrium and the zeroth law, the three scales and their conversions, and absolute zero only; heat capacity, heat calculations, heat-conduction equations, and the statistical-physics definition of temperature are out of scope
edges:
  先修: []
  支持: []
  攻击: []
evidence: [ev-196]
license: CC-BY-SA-4.0
---

> **English version of [`温度与温标.md`](温度与温标.md).**

> [!TIP]
> **After reading this entry you should** be able to say that temperature is what a thermometer reads at thermal equilibrium, not "heat stored in a body"; use the zeroth law to explain why two thermometers can be compared; convert among `°C`, `°F`, and `K`; and explain why the gas laws accept only Kelvin temperature.

## Definition

**Temperature** is the quantity a thermometer reads when it is in thermal equilibrium with the object. The textbook states the operational definition outright: `Temperature is literally defined as what we measure on a thermometer.` This is not circular — it anchors temperature to the procedure "bring the thermometer into thermal equilibrium with the system."

**Heat** is **energy transferred because of a temperature difference**, not a substance stored in a body. The textbook writes `Heat is the transfer of energy due to a temperature difference.` Heat is measured in joules (J), and it is a process quantity.

**Thermal equilibrium**: when two systems are in thermal contact, energy is transferred as heat from the hotter one to the colder one until their temperatures are equal; if they are then isolated from everything else, the net heat flow stops. **Thermal contact** means energy can be exchanged as heat; it does not require mechanical contact — radiation also transfers heat.

**Zeroth law**: if A is in thermal equilibrium with B, and B is in thermal equilibrium with C, then A is in thermal equilibrium with C. This guarantees that two bodies in equilibrium with the same thermometer have the same temperature, so thermometers can be compared. The textbook compares it to the transitive property of equality and notes that it was discovered after the first and second laws but is logically more basic — hence "zeroth."

A **temperature scale** is a ruler for temperature. The textbook presents three:

| Event (1 atm) | Celsius `°C` | Fahrenheit `°F` | Kelvin `K` |
|---|---:|---:|---:|
| Freezing point of water | 0 | 32 | 273.15 |
| Boiling point of water | 100 | 212 | 373.15 |
| Absolute zero | −273.15 | −459.67 | 0 |
| Room temperature (textbook example) | 25 | 77 | 298 (textbook rounding; exact 298.15) |

Conversions:

`T_F = (9/5) T_C + 32`

`T_C = (5/9)(T_F − 32)`

`T_K = T_C + 273.15`

`T_F = (9/5)(T_K − 273.15) + 32`

A **temperature difference** converts differently: `ΔT_F = (9/5) ΔT_C`, while `ΔT_K = ΔT_C`. "A rise of 5 °C" equals "a rise of 9 °F", but the point "5 °C" equals "41 °F". Confusing a temperature point with a temperature difference is the most common conversion error.

> [!IMPORTANT]
> **Temperature is not heat, and it is not internal energy.**
>
> In the same section the textbook calls `thermal energy` "the average kinetic energy of the particles," and also says internal energy is "the sum of the kinetic and potential energies" of atoms and molecules. Those are not the same quantity:
> internal energy `U` is a state function; heat `Q` is a process quantity; temperature `T` is an intensive quantity. Treating `thermal energy` as a strict thermodynamic quantity leads to "higher temperature means more heat," which is false.
>
> A bucket of warm water and a spoon of boiling water: the boiling water is hotter, but the bucket has far more mass and can release more heat while cooling to room temperature. **Temperature sets the direction of heat flow, not the amount of heat.**

> [!WARNING]
> **Absolute zero is not "the temperature at which a gas would have zero volume."**
>
> The glossary of the textbook's gas chapter defines absolute zero as "temperature at which the volume of a gas would be zero according to Charles's law." That is an **extrapolation of the ideal-gas model**, not an accessible physical state: every real gas liquefies or solidifies long before 0 K.
>
> The temperature chapter says absolute zero is where "there is no molecular motion to produce thermal energy." That is also too strong: quantum mechanics gives a zero-point energy, and zero-point motion remains at 0 K. This entry keeps only the weaker, safer half of both statements: **0 K is the theoretical lowest temperature and is unreachable; it is not a state in which all motion stops.**

> [!NOTE]
> **Three conditions for a thermometer reading.**
>
> 1. The thermometer is in **thermal contact** with the system and has reached **thermal equilibrium**; the thermometer itself must not become a significant heat source or sink.
> 2. The thermometer has been **calibrated** against fixed points; different scales are only different rulers for the same physical quantity.
> 3. The thermometer has a **finite response time**; moved from ice water to hot water, it does not jump instantly — it records its own sensor coming into equilibrium with the surroundings.

> [!NOTE]
> **The post-2019 kelvin definition (added here; not in m54287).**
>
> The SI now defines the kelvin by fixing the Boltzmann constant: `k_B = 1.380649×10⁻²³ J/K`. The triple point of water at `273.16 K` is no longer the defining point but a conventional value; `273.15 K` remains the usual ice-point convention. The textbook's "freezing point 273.15 K, boiling point 373.15 K" is accurate enough at high-school precision.

## Relations

| Relation | Entry |
|---|---|
| Follow-up | [Kinetic-molecular theory](molecular-kinetic-theory.en.md) — connects temperature to the average translational kinetic energy of molecules; this entry gives only the operational definition, and the microscopic model is developed there |
| Follow-up | [Gas laws and the ideal-gas equation](gas-laws-and-ideal-gas-equation.en.md) — ratios such as `p/T` and `V/T` hold only when `T` is in kelvin |
| Follow-up | [First law of thermodynamics](../../archive/knowledge/physics/concepts/thermodynamic-first-law.en.md) — the bookkeeping of heat `Q`, work `W`, and internal energy `ΔU`; this entry distinguishes the concepts but does no energy calculation |
| Follow-up | [Statistical interpretation of entropy](../../archive/knowledge/physics/concepts/statistical-interpretation-of-entropy.en.md) — the statistical meaning of temperature, entropy, and absolute zero |
| Recorded gap | **The zeroth law** has no entry of its own; **heat capacity and heat calculations**, **quantitative conduction/convection/radiation**, **ITS-90**, **quantum degenerate temperatures**, and **negative absolute temperature** are not built. This entry stops at "what temperature is, how it is measured, and how scales convert" |

## Argument

### K1 · Temperature is an operational definition, made comparable by thermal equilibrium and the zeroth law (no attack yet)

- **Claim**: temperature is what a thermometer reads at thermal equilibrium; it is neither heat nor internal energy
- **Premise**: the textbook writes `Temperature is literally defined as what we measure on a thermometer.` and defines heat as `the transfer of energy due to a temperature difference`; the zeroth law guarantees "A at the same temperature as B, B at the same temperature as C ⇒ A at the same temperature as C" (ev-196)
- **Reasoning**: a thermometer reading is meaningful only when the thermometer and the object are in thermal equilibrium; the zeroth law turns "in equilibrium with the same thermometer" into a transitive relation, so two thermometers can be compared. Heat is a process quantity depending on the temperature difference, mass, and path; temperature is a state quantity independent of path. Neither can define the other
- **Evidence**: ev-196
- **Attacked**: the textbook's learning objective says `Explain that temperature is a measure of internal kinetic energy`, which is not the same sentence as the operational definition in the body. For an ideal gas, `T` is proportional to the average **translational** kinetic energy; for solids, liquids, and molecules with rotational/vibrational degrees of freedom, `T` is not simply "average kinetic energy." This entry treats the operational definition as the definition and leaves the microscopic correspondence to the kinetic-molecular-theory entry as a model result
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

### K2 · The kelvin is an absolute scale, and the gas laws require `K` (no attack yet)

- **Claim**: `T_K = T_C + 273.15`; ratios such as `p/T` and `V/T` hold only when `T` is thermodynamic temperature
- **Premise**: the textbook says the kelvin scale is absolute and its zero is the lowest possible temperature; the gas chapter states `temperatures must be on the kelvin scale for any gas law calculations` and computes `390 kPa` for a spray can warmed from `24 °C` to `50 °C` (ev-196, ev-198)
- **Reasoning**: the Celsius zero is the freezing point of water, an arbitrary reference. Substituting `24 °C` and `50 °C` directly into `p/T` gives the ratio `50/24`; in kelvin it is `323/297`. The former would inflate the pressure to about `750 kPa`, nearly twice the `390 kPa` result. A proportionality law needs a true zero, not a scale whose zero is the ice point
- **Evidence**: ev-196, ev-198
- **Attacked**: the glossary of the gas chapter defines absolute zero as "the temperature at which the volume of a gas would be zero according to Charles's law" — using an extrapolation of the ideal-gas model to define the zero of the scale is circular, and real gases liquefy before 0 K. The modern kelvin is defined through `k_B`, not through the volume of some gas. The temperature chapter's "lowest temperature ever created, `1.0×10⁻¹⁰ K`" is also a record from around 2020, not a permanent fact
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

### K3 · Heat is not temperature: a bucket of warm water and a spoon of boiling water (no attack yet)

- **Claim**: a hotter body does not necessarily "contain more heat"; heat is transferred energy, not something stored in a body
- **Premise**: the textbook's Teacher Support asks `what contains more heat—a bucketful of warm water or a spoonful of boiling water` and demands `Dispel any notions that heat content is solely dependent on temperature` (ev-196)
- **Reasoning**: let both cool to the same room temperature and compare the heat released: heat also depends on mass, material, and process. The bucket may contain hundreds of times more water than the spoon; even with a smaller temperature difference, its total released heat can be larger. Temperature tells us only the direction of heat flow: from hot to cold, until thermal equilibrium
- **Evidence**: ev-196
- **Attacked**: the textbook gives no heat formula and does not state the comparison condition "cool to the same room temperature"; without a fixed final state, the size of `Q` cannot be compared. The textbook also mixes `thermal energy` with "average kinetic energy," making "heat," "thermal energy," and "internal energy" harder to separate. This entry states the comparison condition and keeps only "temperature sets direction; mass and process set amount"
- **Attribution**: AI (DeepSeek V4.1 Flash Free) · 2026-11-05

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-11-05 | Entry created; serves as the temperature prerequisite for chapter 1 of elective-3, "kinetic-molecular theory", establishing the operational definition, thermal equilibrium, and scale conversions | written after reading m54287 / m54302 in full (ev-196) | AI (DeepSeek V4.1 Flash Free) |
