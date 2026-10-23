---
id: kb:physics:heat-engine-and-carnot-cycle
type: 知识点
title: "Heat engines and the Carnot cycle"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done the first and second laws of thermodynamics and need to judge a heat engine's performance and its upper limit
  条件: covers heat engines, the cyclic ledger `W = Q_h − Q_c`, efficiency `Eff = 1 − Q_c/Q_h`, the Otto cycle, the Carnot cycle, and the Carnot efficiency `Eff_C = 1 − T_c/T_h`; heat-pump and refrigerator COPs, engineering details of real cycles, free energy, and the statistical interpretation of entropy are out of scope
edges:
  先修: ["[First law of thermodynamics](thermodynamic-first-law.en.md)", "[Second law of thermodynamics](thermodynamic-second-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-183]
license: CC-BY-SA-4.0
---

> **English version of [`热机与卡诺循环.md`](热机与卡诺循环.md).**

> [!TIP]
> **After reading this entry you should** be able to write one cycle of a heat engine as `W = Q_h − Q_c`, write its efficiency as `Eff = 1 − Q_c/Q_h`, use `Eff_C = 1 − T_c/T_h` to compute the ceiling between two reservoir temperatures, and explain why no real engine reaches either 100% or the Carnot efficiency

## Definition

### Heat engines and cyclic processes

A **heat engine** is a device that uses heat transfer to do work; gasoline and diesel engines, jet engines, and steam turbines are all heat engines (ev-183). It takes heat `Q_h` from a **hot reservoir**, does work `W`, and rejects heat `Q_c` into a **cold reservoir**; the two temperatures are `T_h` and `T_c` (ev-183).

Heat engines usually run in **cycles**: at the end of every cycle the working substance returns to its initial state, so its internal energy does not change (ev-183):

```
ΔU = 0  ⇒  0 = Q − W  ⇒  W = Q_h − Q_c
```

- the textbook writes `ΔE_int` for internal energy; this entry uses `ΔU` to match [First law of thermodynamics](thermodynamic-first-law.en.md)
- `Q_h` is the heat taken from the hot reservoir and `Q_c` the heat rejected into the cold reservoir; the textbook treats both as positive **magnitudes**, with the direction carried by the minus sign in `W = Q_h − Q_c` (ev-183)
- so the net work of a cyclic engine equals the net heat taken in: `W = Q_h − Q_c`

### Efficiency

The **efficiency** of a heat engine is its net work output divided by the heat taken from the hot reservoir (ev-183):

```
Eff = W / Q_h = (Q_h − Q_c) / Q_h = 1 − Q_c / Q_h
```

Efficiency reaches 1 (100%) only when `Q_c = 0`; the second expression of the second law says that is impossible in a cyclic process (ev-183). The textbook also notes that `Q_c` is usually "a very significant amount": waste heat is an unavoidable product of a heat engine (ev-183).

### The second expression of the second law

The textbook states the "heat into work" side of the second law as (ev-183):

> It is impossible in any system for heat transfer from a reservoir to completely convert to work in a cyclical process in which the system returns to its initial state.

In other words: **no cyclic heat engine can turn all the heat it takes from a reservoir into work**; at least some `Q_c` must be rejected to the cold reservoir.

### The Carnot cycle and the Carnot efficiency

In 1824 the French engineer **Sadi Carnot** (1796–1832), studying the steam engines of the early Industrial Revolution, devised a theoretical cycle now called the **Carnot cycle**: two **isothermal** and two **adiabatic** processes, using only **reversible** processes (ev-183). A heat engine that uses the Carnot cycle is a **Carnot engine**.

For a Carnot engine, the textbook says the ratio `Q_c/Q_h` equals the ratio of the **absolute temperatures** of the two reservoirs (ev-183):

```
Q_c / Q_h = T_c / T_h      (Carnot engine)
Eff_C = 1 − T_c / T_h
```

- `T_h` and `T_c` must be thermodynamic temperatures (K), not degrees Celsius
- the third form of the second law: between two given temperatures a Carnot engine has the greatest possible efficiency, and every engine using only reversible processes has that same maximum efficiency (ev-183)
- 100% efficiency would require `T_c = 0 K`, which is unattainable (ev-183)
- the ideal Carnot engine has the highest efficiency but **zero power**: reversible processes would have to run infinitely slowly, so it cannot do useful work in practice (ev-183)

Real cycles always contain irreversible processes — friction, turbulence — which increase `Q_c` and lower the efficiency; even an ideal engine loses part of its output work to friction and other dissipative processes in its transmission (ev-183).

### The Otto cycle: a model of the four-stroke gasoline engine

The textbook uses the **Otto cycle** to show how a four-stroke gasoline engine turns heat into work (ev-183):

| Path | Process | Corresponding stroke |
|---|---|---|
| AB | adiabatic compression, work done on the gas | compression stroke |
| BC | isochoric heat input `Q_h`, raising pressure and temperature | ignition and burning |
| CD | adiabatic expansion, work done by the gas | power stroke |
| DA | isochoric heat rejection `Q_c`, lowering temperature and pressure | exhaust and intake |

- the net work is the **area inside** the closed path on the `P–V` diagram (ev-183)
- the gas does more work along `CD` than the outside does on it along `AB`, so there is a net work output (ev-183)
- a hotter hot reservoir and a colder cold reservoir enlarge the enclosed area and raise the efficiency; the textbook uses this to connect efficiency with the reservoir temperatures and promises the absolute limit in the next section (ev-183)
- the textbook states explicitly that the true Otto-cycle paths **do not correspond exactly** to the four strokes of the engine (ev-183)

### Numerical examples (recomputed here)

**Coal-fired power station** (ev-183): each day it takes `Q_h = 2.50×10¹⁴ J` from burning coal and rejects `Q_c = 1.48×10¹⁴ J` into the environment.

- net work `W = 2.50×10¹⁴ − 1.48×10¹⁴ = 1.02×10¹⁴ J`
- efficiency `Eff = 1.02/2.50 = 0.408`, i.e. **40.8%**
- the fraction rejected to the environment is `1.48/2.50 = 59.2%`
- coal burned per day `2.50×10¹⁴ / 2.50×10⁶ = 1.0×10⁸ kg`; with `C + O₂ → CO₂`, 12 kg of carbon gives 44 kg of CO₂, so `1.0×10⁸ × 44/12 ≈ 3.7×10⁸ kg` of CO₂ per day (370,000 tonnes per day)
- if all the work became electricity, the average power would be `1.02×10¹⁴ / 86400 ≈ 1.18×10⁹ W`, i.e. **1180 MW**

**Pressurised-water reactor** (ev-183): hot side `300°C = 573 K`, cold side `27°C = 300 K`, Carnot efficiency `1 − 300/573 = 0.476`, i.e. **47.6%**; the textbook says real nuclear stations reach about 35% and coal, oil, and gas stations about 42%.

Values from the textbook's exercises (recomputed here): a cold reservoir at 200°C with a Carnot efficiency of 30.0% needs a hot reservoir at **403°C**; a Carnot efficiency of 42.0% with a cold reservoir at 27°C needs **244°C**, and a real engine that reaches only 0.700 of the Carnot efficiency needs **477°C**; two steam engines in series, 450°C → 270°C and 270°C → 150°C, give an overall efficiency of **41.5%**, the same as one Carnot engine from 450°C to 150°C; a 450°C source with a Carnot efficiency of 0.700 would need a cold reservoir at **−56.3°C**, below the freezing point of water, so that exercise's premise is unreasonable (ev-183).

> [!NOTE]
> **Wording problems in the source, and what this entry supplies** (ev-183)
>
> 1. after writing `W = Q_h − Q_c`, m42234 says `all Qs are positive. The direction of heat transfer is indicated by a plus or minus sign. For example, Qc is out of the system and so is preceded by a minus sign.` — it calls every `Q` positive and then says `Q_c` carries a minus sign, which contradicts itself. This entry treats `Q_h` and `Q_c` as positive magnitudes and carries the direction in the formula's minus sign; it does not repeat the second sentence.
> 2. m42234 says `in every imaginable cyclical process, it is absolutely necessary for heat transfer from the system to occur in order to get a net work output`, then gives only the heat rejection along `DA` as its example, although `BC` also transfers heat. What the sentence needs is **heat rejection** `Q_c`, not "no heat transfer at all".
> 3. m42235 opens by calling the drinking bird `an example of Carnot's engine` and says that, apart from the original wetting of its head, the bird is `a perpetual motion machine of sorts`. The analogy is popular rather than physical: the bird runs on **continuous evaporation** and on dipping its head to be rewetted, so it is neither a one-time energy input nor a Carnot engine between two fixed reservoirs. This entry does not repeat the claim.
> 4. in its "inventor's claim" exercise, m42235 says `the best-ever achieved of about 70%` without a source. This entry uses only the logic of the question — an actual efficiency of 96% of the Carnot value is far above what real engines reach — and does not treat 70% as a verified figure.
> 5. the Section Summary of m42235 says `Carnot cycles without heat loss may be possible at absolute zero`, which does not match the body text's statement that 100% efficiency requires `T_c = 0 K`; this entry follows the body text.
>
> **Supplied here, not in the textbook**: the derivation of `Q_c/Q_h = T_c/T_h` from entropy conservation around a reversible cycle (see K2). The textbook gives the ratio only as Carnot's result, without a derivation; K2 labels the entropy argument as this library's completion from `ΔS = Q/T`.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [First law of thermodynamics](thermodynamic-first-law.en.md) — over a full cycle `ΔU = 0`, so `W = Q_h − Q_c` is the first law applied to a cycle |
| Prerequisite | [Second law of thermodynamics](thermodynamic-second-law.en.md) — the second expression forbids `Q_c = 0`, which is why efficiency cannot reach 100% |
| Follow-up | [Statistical interpretation of entropy](statistical-interpretation-of-entropy.en.md) — counts microstates to explain why the second law is statistical and why the Carnot efficiency is a ceiling |
| Related | [Energy resources and sustainability](energy-resources-and-sustainability.en.md) — the quantitative example of plant efficiency, waste heat, and CO₂ emissions |
| Recorded gap | **Heat-pump and refrigerator COPs**, **quantitative real cycles (Diesel, Rankine, Brayton)**, **a rigorous proof of Carnot's theorem**, **the Otto-cycle compression-ratio formula**, **free energy** are not built in this repo |

## Argument

### K1 · The cyclic energy ledger: `W = Q_h − Q_c` and efficiency (given by the textbook, no attack yet)

- **Claim**: over one cycle `ΔU = 0`, so the net work is `W = Q_h − Q_c` and the efficiency is `Eff = 1 − Q_c/Q_h`
- **Premise**: the textbook says a cyclic process brings the system back to its initial state at the end of every cycle, so `ΔE_int = 0`; applying the first law `ΔE_int = Q − W` to the whole cycle gives `W = Q`, with `Q = Q_h − Q_c`; efficiency is defined as `Eff = W/Q_h` (ev-183)
- **Reasoning**: internal energy returns to its starting value, so the first law's ledger reduces to "heat in − heat out = work out". Substituting `W = Q_h − Q_c` into the definition gives `Eff = 1 − Q_c/Q_h`. Efficiency depends only on how much heat is rejected; the smaller `Q_c`, the higher the efficiency, and only `Q_c = 0` gives 1. The textbook's examples and exercise answers all recompute: `Q_h = 2.50×10¹⁴ J` and `Q_c = 1.48×10¹⁴ J` give 40.8%; `W = 10.0 kJ` and `Q_c = 8.50 kJ` give `Q_h = 18.5 kJ` and 54.1%; `W = 2.00×10⁸ J` at 5.00% efficiency gives `Q_h = 4.00×10⁹ J` and `Q_c = 3.80×10⁹ J`, or 0.667 barrels of fuel
- **Evidence**: ev-183
- **Attacked**: **the textbook does not discuss mechanical losses or pump work** — it treats `W` as net output but does not say how bearing friction or cooling pumps enter the ledger, and its power-station example treats the plant as an ideal cycle. Its sentence that "all Qs are positive" also contradicts itself (see NOTE). This library recomputes the arithmetic only; it does not supply an engineering model
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · The Carnot efficiency: `Q_c/Q_h = T_c/T_h` and `Eff_C = 1 − T_c/T_h` (asserted by the textbook, derived here from entropy)

- **Claim**: for a Carnot engine using only reversible processes, `Q_c/Q_h = T_c/T_h`, so `Eff_C = 1 − T_c/T_h`; between the same two temperatures no heat engine can be more efficient
- **Premise**: the textbook says the Carnot cycle consists of two isotherms and two adiabats and uses only reversible processes; `Q_c/Q_h` equals the ratio of the absolute temperatures of the reservoirs; `Eff_C = 1 − T_c/T_h`; real engines fall below the Carnot efficiency (ev-183)
- **Reasoning** (supplied here): treat one reversible cycle as taking `Q_h` at `T_h` and rejecting `Q_c` at `T_c`. Entropy is a state function, so after a full cycle the total entropy change is zero: `Q_h/T_h − Q_c/T_c = 0`, hence `Q_c/Q_h = T_c/T_h`. Substituting into `Eff = 1 − Q_c/Q_h` gives `Eff_C = 1 − T_c/T_h`. The argument uses `ΔS = Q/T` from [Second law of thermodynamics](thermodynamic-second-law.en.md) (ev-157)
- **Evidence**: ev-183 (the textbook's assertion), ev-157 (`ΔS = Q/T`)
- **Attacked**: **the textbook does not derive the ratio — it only writes "What Carnot found was..." — and the entropy-conservation argument above is this library's addition.** The argument assumes heat is taken in and rejected reversibly at constant `T_h` and `T_c` and that the working substance follows an ideal Carnot cycle. The textbook also does not prove Carnot's theorem (that all reversible engines between the same two temperatures have the same efficiency); it states it as the third form of the second law. "A Carnot engine has zero power" is only qualitative: there is no quantitative relation between infinite slowness and power
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · The Otto cycle and the `P–V` diagram: why efficiency depends on temperature (the textbook's qualitative argument, no attack yet)

- **Claim**: the net work of a cycle is the area inside the closed path on a `P–V` diagram; a hotter hot reservoir and a colder cold reservoir enlarge the area and raise the efficiency; this trend agrees with the Carnot ceiling
- **Premise**: the textbook describes the Otto cycle's AB adiabatic compression, BC isochoric heat input, CD adiabatic expansion, and DA isochoric heat rejection, and says the gas does more work along CD than the outside does on it along AB; the net work is the area inside the closed path; "The lower the temperature on the path AB, the less work has to be done to compress the gas... the higher the temperature along the path CD, the more work output there is"; it also says the true four-stroke paths do not correspond exactly to the Otto cycle (ev-183)
- **Reasoning**: `W_net = ∮ P dV`, which is the area enclosed by the curve on a `P–V` diagram. Lowering the temperature along AB reduces the work needed to compress the gas, and raising the temperature along CD increases the work produced during expansion; both enlarge the area, so efficiency rises with `T_h` and falls with `T_c`. The trend matches `1 − T_c/T_h`, but the Otto cycle's efficiency also depends on the compression ratio and stays below the Carnot ceiling at the same temperatures
- **Evidence**: ev-183
- **Attacked**: **the textbook gives no Otto efficiency formula** (for example `1 − r^(1−γ)` in terms of the compression ratio `r` and the specific-heat ratio `γ`) and makes no quantitative comparison with the Carnot efficiency; the `P–V` sketch is not to scale, and "area = net work" ignores friction and throttling losses. The textbook's statement that every cycle needs heat transfer to produce net work cites only the heat-rejection path, which is imprecise (see NOTE)
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the heat-engine-efficiency and Carnot-cycle gaps of the 选必三 "laws of thermodynamics" chapter; the Carnot ratio `Q_c/Q_h = T_c/T_h` is labelled as this library's derivation from entropy conservation | written after reading m42234/m42235 in full (ev-183) | @hpleapfrog |
