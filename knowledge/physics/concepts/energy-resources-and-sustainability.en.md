---
id: kb:physics:energy-resources-and-sustainability
type: 知识点
title: "Energy resources and sustainability"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have learned electric work and Joule's law and need to understand the world energy mix, renewable and nonrenewable sources, and the difference between "energy conservation" and the law of conservation of energy
  条件: covers the world energy mix (2020 table), the distinction between renewable and nonrenewable sources, the qualitative relation between energy and economic development, the difference between energy conservation and the law of conservation of energy, and the checking of data scope and year only; technical details of photovoltaics, wind, and nuclear power, quantitative carbon accounting, Chinese energy policy and the curriculum standard, and storage and grid dispatch are not built
edges:
  先修: ["[Electric work and Joule's law](electric-work-and-joule-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-180]
license: CC-BY-SA-4.0
---

> **English version of [`能源与可持续发展.md`](能源与可持续发展.md).**

> [!TIP]
> **After reading this entry you should** be able to distinguish renewable sources from fossil fuels, read the world energy mix in `EJ` and percentages, and explain why "energy conservation" and the law of conservation of energy are not the same thing

## Definition

**Renewable and nonrenewable sources**: the textbook defines renewable forms of energy as "those sources that cannot be used up, such as water, wind, solar, and biomass"; fossil fuels are oil, natural gas, and coal, which are nonrenewable. Nuclear energy is neither a fossil fuel nor renewable and has its own column in the energy table.

> [!NOTE]
> **"Cannot be used up" is the textbook's simplification.**
>
> Biomass can be depleted if it is consumed faster than it regrows; the more accurate criterion is the **comparison between regeneration rate and consumption rate**, not a literal "never runs out". This qualification is supplied by the library; the textbook does not expand on it.

**World energy mix**: the textbook's 2020 table gives world primary energy consumption as **557.1 EJ** (`1 EJ = 10¹⁸ J`, i.e. `5.571×10²⁰ J` in total), with

| Source | Consumption (EJ) | Share |
|---|---:|---:|
| Oil | 174.2 | 31.3% |
| Natural gas | 137.6 | 24.7% |
| Coal | 151.4 | 27.2% |
| Nuclear | 24.0 | 4.3% |
| Hydro | 38.2 | 6.9% |
| Other renewables | 31.7 | 5.7% |

Fossil fuels total `174.2 + 137.6 + 151.4 = 463.2 EJ`, or **83.1%**; renewables (hydro + other renewables) total `69.9 EJ`, or **12.6%**. The prose says "about 85% of our energy comes from nonrenewable fossil fuels", about two percentage points above the 2020 table's 83.1%, a difference of data year (ev-180).

**Growth and countries**: world energy consumption tripled in the past 50 years and might triple again in the next 30. The textbook's examples (of mixed data years): the U.S. has 4.25% of world population but consumes 21% of world oil production per year; Germany plans to meet 65% of its power and 30% of its overall energy needs with renewables by 2030; New Zealand gets about two-thirds of its electricity from hydro; the U.S. gets about 10% of its energy from renewables; China gets 2/3 of its energy from coal, imports over 1/3 of its oil, and has been the largest CO₂ emitter since 2009; India relies mainly on biomass and coal, with about 70% of its electricity from coal.

**Energy and economic development**: the textbook states that energy consumption per capita rises with GDP per capita, and that diversifying energy sources improves economic and grid resilience (renewable employment, faster recovery after disasters). These are the textbook's **qualitative judgments and policy examples**, not conclusions derived from physical laws.

**Energy conservation and the law of conservation of energy**: two easily confused ideas.

- **The law of conservation of energy**: the total energy of an isolated system remains constant. The textbook says it cannot be proved from more basic principles, but no exception has ever been found.
- **Energy conservation (the practice)**: reducing energy use through less activity (turning down thermostats, driving fewer kilometers) or through higher conversion efficiency (more efficient heaters, cars, CFLs).

**Why conserve if energy is conserved**: most energy transformations end as waste heat transferred to the environment and as forms of energy no longer useful for doing work. The textbook's phrase is "the potential for energy to produce useful work has been 'degraded' in the energy transformation". The energy has not disappeared, but its **ability to do work has fallen**; hence the focus on how much is used and how efficiently.

> [!IMPORTANT]
> **The law of conservation of energy is not the same as energy conservation.**
>
> A coal-fired plant at 35% efficiency still has 100% of the fuel's chemical energy (conservation), but only 35% becomes electrical energy and the rest, about 65%, mostly becomes waste heat. "Energy is conserved" does not imply "there is no need to conserve energy"; precisely because the ability to do useful work falls with every conversion, using less and converting more efficiently matters. One of the textbook's conceptual questions asks exactly this: 35% efficiency does not contradict conservation of energy.

> [!NOTE]
> **The table's column count and row sums are defective.**
>
> - Egypt's coal cell reads `0.0%` while the rest of the column is in EJ; taking it as 0.0, Egypt's components sum to `1.3 + 2.1 + 0 + 0 + 0.1 + 0.1 = 3.6 EJ`, not the total column's `3.7 EJ`.
> - The table declares `tgroup cols="10"` and has 10 `colspec` elements, but its header and each row contain only **8** cells.
> - **8 of the 11** country rows do not sum to their totals: Russia `28.7 vs 28.3`, Egypt `3.6 vs 3.7`, India `32.00 vs 31.99`, and most others differ by `0.1 EJ`. This looks like separate rounding of components and totals, but Russia's `0.4 EJ` is larger than rounding alone can explain.
>
> This entry uses only the world row and the stated country totals from this table, not sums of country components as independent data.

> [!NOTE]
> **The prose, the figure caption, and the 2020 table are not from the same year.**
>
> - The prose's "about 85% fossil", "the U.S. consumes 21% of world oil", and "China's coal is 2/3" disagree with the 2020 table's `83.1%`, `18.7%`, and `56.6%`.
> - The prose says "only 10% of the U.S. **electricity** is generated by renewable resources", while the Section Summary says "10% of its **energy**"; from the 2020 table, U.S. renewables `2.6 + 6.2 = 8.8 EJ` are **10.0%** of the `87.8 EJ` total, which is a **total-energy** share, not an electricity share.
> - Both the prose and the Section Summary call U.S. renewables "primarily/mostly hydroelectric", but in the 2020 table other renewables (`6.2 EJ`) already exceed hydro (`2.6 EJ`).
> - One figure caption is dated 2006 while the table is 2020.
> - Most of the exercise set is work-and-energy problems (push-ups, skiing, swimming, a toy gun, an elevator), unrelated to this section's energy mix; only the two Conceptual Questions match.
>
> These inconsistencies are recorded in ev-180; this entry states the scope and year whenever it quotes a number.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Electric work and Joule's law](electric-work-and-joule-law.en.md) — energy units, electricity cost, and "efficiency = useful energy / total energy"; every "consumption" figure in the energy mix is an amount of energy |
| Follow-up | [Second law of thermodynamics](thermodynamic-second-law.en.md) — the qualitative talk of "waste heat" and "degraded ability to do work" becomes quantitative as entropy only in elective-3; this entry uses the textbook's qualitative statement and introduces no entropy formula |
| Related | [Conservation of mechanical energy](conservation-of-mechanical-energy.en.md) — mechanical-energy conservation is the special case of energy conservation when only gravity or spring forces do work; this entry is about the broader law and its difference from "energy conservation" |
| Related | [Power transmission](power-transmission.en.md) — the line loss `P_loss = I²R_wire` is one concrete part of improving conversion and delivery efficiency |
| Related | [Closed-circuit Ohm's law and internal resistance](closed-circuit-ohms-law.en.md) — the source efficiency `R/(R+r)` is a microscopic example of energy utilisation, to be compared with macroscopic energy efficiency |
| Recorded gap | **Technical details of photovoltaics, wind, and nuclear power**, **quantitative carbon accounting**, **Chinese energy policy and the curriculum standard**, **unifying the scope and year of energy statistics**, and **storage and grid dispatch** are not built here |

## Arguments

### K1 · Fossil fuels still supply more than four-fifths of world energy (2020 table)

- **Claim**: according to the textbook's 2020 table, fossil fuels are 83.1% of world primary energy, oil is 31.3%, and renewables are 12.6%
- **Premises**: the world row's values are in EJ; components and total use the same scope; the shares are computed here by dividing components by the total
- **Reasoning**: `174.2 + 137.6 + 151.4 = 463.2 EJ`, so `463.2/557.1 = 83.1%`; oil is `174.2/557.1 = 31.3%`, inside the prose's "31–35%" range; renewables are `(38.2 + 31.7)/557.1 = 12.6%` and nuclear is `24.0/557.1 = 4.3%`. The four parts add to `83.1 + 12.6 + 4.3 = 100.0%` after rounding. For the U.S. row, renewables are `2.6 + 6.2 = 8.8 EJ`, and `8.8/87.8 = 10.0%`, matching the Section Summary's 10% (ev-180)
- **Evidence**: ev-180
- **Attacked by**: the table is for 2020 while the prose's "about 85%" and "21% of world oil" may come from earlier data; 8 country rows do not sum to their totals; whether "renewable" includes hydro and whether nuclear counts as low-carbon depends on the statistical convention; the mix changes year by year, so the 2020 shares are not constants
- **Author**: @hpleapfrog · 2026-10-21

### K2 · The law of conservation of energy and "energy conservation" are two different things

- **Claim**: the law of conservation of energy says the total energy of an isolated system is constant; energy conservation says to use less energy or convert it more efficiently — the two are not the same proposition
- **Premises**: the law holds for an isolated system; every practical use of energy turns part of it into waste heat; efficiency = useful energy / input energy
- **Reasoning**: a coal plant at 35% efficiency turns 35% of the input chemical energy into electrical energy and the other 65% mainly into waste heat; the total energy is still conserved, but not in a usable form. The textbook's learning objective therefore says "the inevitable conversion of energy to less useful forms makes it necessary to conserve energy resources" — not because energy disappears, but because the **ability to do useful work falls**. The Section Summary also states the two separately: energy can be neither created nor destroyed, yet the energy available to do work is always partly converted into less useful forms (ev-180)
- **Evidence**: ev-180
- **Attacked by**: the textbook uses only qualitative language and gives no entropy or exergy formulation; "waste heat" is still energy, so "wasting energy" must distinguish conservation of energy from loss of available work; the 35% figure is an assumption in a conceptual question, not a measurement of a particular plant
- **Author**: @hpleapfrog · 2026-10-21

### K3 · Energy consumption, economic development, and sustainability (the textbook's qualitative judgments)

- **Claim**: the textbook holds that energy consumption per capita rises with GDP per capita, that diversifying energy sources improves resilience, and that current consumption and production are not sustainable
- **Premises**: the textbook's 2020 table and country examples; GDP and energy statistics are comparable in scope; policy targets are read as targets for their stated year
- **Reasoning**: U.S. renewables are `10.0%` of total energy, matching the Section Summary; Germany's 2020 renewables are `2.4/12.1 = 19.8%`, not inconsistent with the "30% of overall energy by 2030" target (a future value); China's coal is `82.3/145.5 = 56.6%`, below the prose's older "2/3". The examples of Germany, New Zealand, the U.S., China, and India illustrate trends and policy differences, but they are **examples and judgments**, not necessary conclusions from physical laws (ev-180)
- **Evidence**: ev-180
- **Attacked by**: correlation between GDP per capita and energy per capita is not causation — economic structure, climate, and prices all matter; policy targets are not outcomes; "not sustainable" is a value judgment and a long-run trend judgment that depends on data year and assumptions; the country data are of mixed years
- **Author**: @hpleapfrog · 2026-10-21

## Changelog

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the last gap of "electrical energy and energy resources", completing priority 20 and turning the chapter 🟢 | ev-180 after reading m42154 in full; the world shares are recomputed here from the 2020 table; the `0.0%` cell, the column count and row-sum problems, and the differing data years between prose and table are recorded in ev-180 | @hpleapfrog |
