---
id: kb:physics:statistical-interpretation-of-entropy
type: 知识点
title: "Statistical interpretation of entropy"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done the second law of thermodynamics and want to know why entropy increases
  条件: covers macrostates and microstates, the equal-probability assumption, `S = k ln W`, and the coin-toss and gas examples; the derivation of Boltzmann's formula, its equivalence with `ΔS = Q/T`, free energy, information entropy, and fluctuation theorems are out of scope
edges:
  先修: ["[Second law of thermodynamics](thermodynamic-second-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-184]
license: CC-BY-SA-4.0
---

> **English version of [`熵的统计解释.md`](熵的统计解释.md).**

> [!TIP]
> **After reading this entry you should** be able to separate a **macrostate** from a **microstate**, use `S = k ln W` and `ΔS = k ln(W_f/W_i)` to compute an entropy difference, and explain why "entropy never decreases" is a statistical certainty for macroscopic systems rather than a logical ban at the microscopic level

## Definition

### Macrostates and microstates

A **macrostate** is an overall property of a system; it does not specify the state of every part. A **microstate** is a detailed description of every element of the system (ev-184).

Take five coins. Counting only heads and tails gives six macrostates: 5 heads 0 tails, 4 heads 1 tail, 3 heads 2 tails, 2 heads 3 tails, 1 head 4 tails, and 0 heads 5 tails. Each particular sequence of heads and tails is a microstate (ev-184):

| Macrostate | Number of microstates `W` |
|---|---|
| 5 heads, 0 tails | 1 |
| 4 heads, 1 tail | 5 |
| 3 heads, 2 tails | 10 |
| 2 heads, 3 tails | 10 |
| 1 head, 4 tails | 5 |
| 0 heads, 5 tails | 1 |
| **Total** | **32** |

- 3 heads and 2 tails has 10 microstates while 5 heads has 1, so the former is ten times as probable (ev-184)
- the count rests on one **crucial assumption**: every microstate is equally probable. The textbook stresses that if the coins are asymmetric (like loaded dice), the assumption fails and the analysis is wrong (ev-184)
- the two most orderly outcomes, 5 heads and 5 tails, account for only 2 of the 32 microstates; 3 heads 2 tails and its reverse account for 20; starting from 5 heads, 30 of the 32 outcomes are less orderly (ev-184)

### One hundred coins

With 100 coins there are `2^100 = 1.27×10^30` microstates (ev-184):

- 100 heads or 100 tails each have **1** microstate
- 99 heads and 1 tail has **100** microstates
- 50 heads and 50 tails has `1.0×10^29` microstates, about **8%** of all microstates
- the probability of landing between 45 and 55 heads is about **73%**, and between 40 and 60 about **96%** (ev-184)
- tossing once per second, you would wait about `2×10^22` years to see 100 heads or 100 tails — a trillion times the age of the universe (ev-184)

So "an orderly state becomes less orderly on the next toss" is not an absolute law but an overwhelming probability: there are vastly more disorderly microstates than orderly ones.

### Gases: macrostates, microstates, and "all the atoms in one corner"

For a gas, the macrostate corresponds to volume, temperature, and pressure; the microstate corresponds to the position and velocity of every atom (ev-184). `1.0 cm³` of an ideal gas at `1.0 atm` and `0°C` contains about `2.7×10^19` atoms (ev-184), so every macrostate corresponds to an immense number of microstates.

- the most common and most disorderly macrostate has the atoms distributed randomly in space with a Maxwell–Boltzmann distribution of speeds in random directions — the state with the most microstates (ev-184)
- a very orderly macrostate would have all the atoms in one corner with identical velocities — it has very few microstates and is therefore exceedingly unlikely (ev-184)
- work from outside can compress the gas into a corner and lower its entropy locally, but the universe's total entropy rises; once the constraint is removed the gas quickly spreads out and almost never returns to the corner (ev-184)

### The Boltzmann relation

The textbook gives (ev-184):

```
S = k ln W
```

- `k = 1.38×10^-23 J/K` is the **Boltzmann constant**
- `W` is the **number of microstates** corresponding to a macrostate
- `ln` is the natural logarithm
- entropy is directly related to the probability of the macrostate: the more microstates and the more probable the macrostate, the greater its entropy (ev-184)
- the entropy difference between two states is `ΔS = S_f − S_i = k ln(W_f/W_i)`

The textbook's example: start with 100 coins at 60 heads and 40 tails (`W_i = 1.4×10^28`) and toss to the most likely 50 heads and 50 tails (`W_f = 1.0×10^29`) (ev-184):

```
ΔS = k ln(W_f/W_i)
   = 1.38×10^-23 × ln(1.0×10^29 / 1.4×10^28)
   ≈ 2.7×10^-23 J/K
```

The reverse entropy decrease (−2.7×10^-23 J/K) has a probability of about 1 in 90; going from 50/50 to the most orderly 100 heads decreases entropy by `−92×10^-23 J/K` (that is, `−9.2×10^-22 J/K`), with a probability of about 1 in 10^30 (ev-184). The textbook's ice example: if `1.00 kg` of ice at `0°C` froze spontaneously, the environment's entropy would fall by `1.22×10^3 J/K` — a decrease of that size is "an utter impossibility" (ev-184).

The textbook also says Boltzmann **proved** that `S = k ln W` is equivalent to the thermodynamic definition `ΔS = Q/T`; the proof is not given in the textbook (ev-184).

### The statistical statement of the second law

Extending the count to macroscopic systems gives the microscopic explanation of the second law (ev-184):

- entropy increases or stays constant in every process; an entropy decrease is not absolutely impossible, only so improbable that it has **never been observed** in a macroscopic system
- the textbook's sentence is: `Entropy can decrease, but for any macroscopic system, this outcome is so unlikely that it will never be observed.`
- the second law is therefore a **statistical law**: it says "overwhelmingly certain", not "logically necessary"

> [!NOTE]
> **Errors and approximations in the source** (ev-184)
>
> 1. in the five-coin table the "3 heads, 2 tails" row claims 10 microstates but lists only the five sequences `HTHTH, THTHH, HTHHT, THHTH, THHHT` and then **repeats the same five**. The count 10 is right, but five sequences are missing (`TTHHH`, `HTTHH`, `HHTTH`, `HHTHT`, `HHHTT`); the "2 heads, 3 tails" row lists ten distinct sequences correctly.
> 2. the sentence `Boltzmann proved that this expression for s is equivalent...` uses a lowercase `s` where the surrounding text uses uppercase `S`; this is a typo in the source.
> 3. "about a 1 in 90 chance" of the reverse entropy decrease: recomputing `C(100,60)/2^100 = 1.08%`, this is the probability of landing **exactly in the 60-heads-40-tails macrostate** (about 1 in 92); the ratio of the two macrostates' microstate counts, `W_60/W_50 = 1.4/10 ≈ 1/7.3`, is a different quantity. The textbook does not distinguish absolute probability from the relative probability of two macrostates, so a reader can easily take 1 in 90 for the latter.
> 4. "a `ΔS` of `10^-21 J/K` corresponds to about a 1 in 10^30 chance": with `ΔS/k = ln(W_i/W_f)`, `10^-21 / 1.38×10^-23 = 72.5` and `e^72.5 ≈ 3.0×10^31`, i.e. about 1 in 3×10^31 — about 30 times smaller than 1 in 10^30. The textbook's "about" does not cover that gap; this entry records the recomputed value.
> 5. the example's `2.7×10^-23 J/K` uses the table's rounded `W_i = 1.4×10^28`; with the exact `C(100,60) = 1.375×10^28` the result is `2.75×10^-23 J/K`, the difference coming from rounding in the table.
>
> **Supplied here, not in the textbook**: `ΔS = k ln(W_f/W_i)` follows by subtracting `S = k ln W` at the two states (the textbook gives `S = k ln W` and only one numerical example); the normalised form "probability = W / total number of microstates" and the conversion "probability of an entropy decrease ≈ `e^(−ΔS/k)`" are this library's additions. The textbook gives no proof that `S = k ln W` equals `ΔS = Q/T`.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Second law of thermodynamics](thermodynamic-second-law.en.md) — `ΔS = Q/T` and "total entropy never decreases" give the macroscopic law; this entry gives its statistical explanation in microstate counts |
| Related | [Heat engines and the Carnot cycle](heat-engine-and-carnot-cycle.en.md) — entropy conservation around a reversible cycle gives `Q_c/Q_h = T_c/T_h`, the interface between the microscopic and macroscopic pictures of the Carnot efficiency |
| Recorded gap | **Derivation of `S = k ln W`**, **proof of its equivalence with `ΔS = Q/T`**, **free energy**, **information entropy**, **fluctuation theorems and quantitative estimates of entropy-decrease probabilities in macroscopic systems**, **combinatorial counting of gas microstates** are not built in this repo |

## Argument

### K1 · A macrostate's probability is set by its number of microstates (the textbook's count, with equal probability assumed)

- **Claim**: if every microstate is equally probable, a macrostate's probability is proportional to its number of microstates `W`; more microstates means a more probable macrostate and greater entropy
- **Premise**: the textbook defines macrostates and microstates, lists the six macrostates of five coins with `1/5/10/10/5/1` microstates, and says `all of these conclusions are based on the crucial assumption that each microstate is equally probable`; if the assumption fails, `the analysis will be erroneous` (ev-184)
- **Reasoning**: treat the 32 microstates as equally likely, each with probability 1/32; 3 heads 2 tails has 10 microstates, so its probability is 10/32; 5 heads has 1, so its probability is 1/32. For 100 coins, `2^100 = 1.27×10^30`, 50 heads 50 tails has `1.0×10^29` microstates and a probability of about 8%, while 100 heads has 1 microstate and a probability of about 1/1.27×10^30. The textbook extends "the most disorderly macrostate is the most probable" to a gas: the random distribution with a Maxwell–Boltzmann speed distribution has far more microstates than "all atoms in one corner"
- **Evidence**: ev-184
- **Attacked**: **the equal-probability assumption is introduced as a premise, not derived from dynamics**; the textbook only says it must hold or the analysis fails. The five-coin table also has a listing error (the five sequences of the 3-heads row are repeated, see NOTE), although the count `W = 10` is right. The textbook says "W is proportional to the probability"; strictly, `P = W/Ω`, with the total number of microstates `Ω` as the normalising constant, which the textbook never writes down
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · `S = k ln W` and entropy differences (the formula is given, the equivalence is not proved)

- **Claim**: entropy is given by `S = k ln W`, and the entropy difference between two states is `ΔS = k ln(W_f/W_i)`; this statistical entropy difference is of the same order as the thermodynamic one
- **Premise**: the textbook gives `S = k ln W`, `k = 1.38×10^-23 J/K`, the definition of `W`, and the 100-coin example from 60/40 to 50/50 with `ΔS = 2.7×10^-23 J/K`; it also says Boltzmann proved it equivalent to `ΔS = Q/T` (ev-184)
- **Reasoning**: `S = k ln W` is a state function, so subtracting gives `ΔS = k ln(W_f/W_i)`. With the textbook's table: `W_i = 1.4×10^28`, `W_f = 1.0×10^29`, giving `2.7×10^-23 J/K`; from 50/50 to 100/0, `W_f = 1`, giving `−9.2×10^-22 J/K` (the textbook writes `−92×10^-23`); for ten coins from 5/5 (252) to 2/8 (45), the result is `−2.38×10^-23 J/K`, matching the textbook's exercise answer, which also says 5/5 is 5.6 times as likely (`252/45`)
- **Evidence**: ev-184
- **Attacked**: **the textbook says Boltzmann proved the equivalence but gives no proof**; `S = k ln W` defines the **statistical entropy**, and equating it with the thermodynamic entropy `ΔS = Q/T` requires a statistical-mechanics argument that this library does not supply. The textbook's "1 in 90" is the absolute probability of landing exactly at 60/40, not the ratio of the two macrostates' microstate counts (see NOTE). The claim that "`10^-21 J/K` corresponds to 1 in 10^30" recomputes to about 1 in 3×10^31, roughly 30 times off. The constant `k` and the reference point (`S = 0` at `W = 1`) are conventions, not derived results
- **Attribution**: @hpleapfrog · 2026-10-21

### K3 · Why the second law is statistical (the textbook's coin and gas arguments; the macroscopic extrapolation is its assertion)

- **Claim**: entropy increases because disorderly macrostates have overwhelmingly more microstates; an entropy decrease in a macroscopic system "has never been observed", so the second law is statistical rather than an absolute ban
- **Premise**: the textbook's 30/32, the 100-coin 8%/73%/96%, `2×10^22` years, the gas with `2.7×10^19` atoms, and `Entropy can decrease, but for any macroscopic system, this outcome is so unlikely that it will never be observed.`; the textbook also calls the second law "a law saying that it is impossible, which has never been observed to be violated" (ev-184)
- **Reasoning**: for `N ~ 10^19` atoms, the uniform state has astronomically more microstates than "all atoms in one corner"; from `ΔS = k ln(W_f/W_i)`, the probability of an entropy decrease `ΔS` is about `e^(−ΔS/k)`. For `ΔS ~ 1 J/K`, `ΔS/k ~ 7×10^22`, an unimaginably small probability. "Entropy never decreases" therefore appears at macroscopic scales as a statistically overwhelming law; the coin examples scale the same logic down to a countable system
- **Evidence**: ev-184
- **Attacked**: **the textbook gives no quantitative fluctuation estimate for a gas**, only coins and the qualitative "corner" picture; "never observed" is empirical, not a theorem. Poincaré recurrence in principle allows a system to return to a low-entropy state, but the recurrence time grows exponentially with particle number, which the textbook does not discuss; nor does it discuss why the universe started in a low-entropy state. This entry repeats the textbook's statistical argument and does not upgrade it to a proof
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; fills the statistical-interpretation-of-entropy gap of the 选必三 "laws of thermodynamics" chapter; `ΔS = k ln(W_f/W_i)`, normalisation, and the absolute-versus-relative reading of "1 in 90" are labelled as this library's additions | written after reading m42238 in full (ev-184) | @hpleapfrog |
