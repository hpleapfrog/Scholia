---
id: kb:physics:thermodynamic-second-law
type: 知识点
title: "Second law of thermodynamics"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done the first law and need to judge which processes can happen spontaneously
  条件: covers total entropy and the direction of spontaneous processes only; heat-engine efficiency, the Carnot cycle, and the statistical interpretation of entropy are out of scope
edges:
  先修: ["[First law of thermodynamics](thermodynamic-first-law.en.md)"]
  支持: []
  攻击: []
evidence: [ev-157]
license: CC-BY-SA-4.0
---

> **English version of [`热力学第二定律.md`](热力学第二定律.md).**

> [!TIP]
> **After reading this entry you should** be able to state that total entropy never decreases in a spontaneous process, separate the **entropy of the system** from **total entropy**, and explain why a refrigerator does not violate the second law

## Definition

The **second law of thermodynamics** fixes the direction of spontaneous processes: the **total entropy** of the system plus the environment increases or remains constant, and never decreases.

```
ΔS_tot = ΔS_syst + ΔS_envir > 0
```

- the textbook's sentence is
  `The second law of thermodynamics states that the total entropy of a system either increases or remains constant in any spontaneous process; it never decreases.`
- **Entropy** `S` measures disorder: `Entropy is a measure of the disorder of a system.` The more disordered a system and the higher its entropy, the less of its energy is available to do work
- `ΔS = Q/T`, where `Q` is the heat transferred during the process and `T` is the **absolute temperature** (K) — not degrees Celsius
- unit: J/K
- immediate consequence: heat flows spontaneously from hot to cold, never the reverse —
  `heat transfers energy spontaneously from higher- to lower-temperature objects, but never spontaneously in the reverse direction.`
- the textbook's formula writes `> 0`, while the same module's statement of the law says total entropy "increases or remains constant", which allows equality. **The textbook does not say when equality holds**; this entry records both forms rather than supplying a condition

> [!IMPORTANT]
> **"The entropy of the system went down" does not mean "the second law was broken".**
>
> The textbook says plainly:
> `it actually is possible for the entropy of one part of the universe to decrease, as long as the total change in entropy of the universe increases.`
> A refrigerator moves heat out of its cold compartment, so the compartment's entropy falls; but the compressor does work and dumps still more heat into the room, so the environment's entropy rises by more and total entropy still increases.
> The textbook's keyword is **spontaneously**:
> `The key word here is spontaneously. If we do work on a system, it is possible to transfer energy by heat from a colder to hotter object.`
> — a **non-spontaneous** cold-to-hot transfer needs work, so it does not violate the second law.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [First law of thermodynamics](thermodynamic-first-law.en.md) — the first law keeps the energy ledger; the second law gives the direction the ledger allows |
| Recorded gap | **Heat engines and efficiency (Carnot cycle)**, **the statistical interpretation of entropy (microstates)**, **free energy** are not built in this repo |

## Argument

### K1 · The second law cannot be derived from the first (no attack yet)

- **Claim**: energy conservation allows far more processes than actually happen spontaneously; the second law is a separate constraint
- **Premise**: the first law `ΔU = Q − W` (ev-156); the second law's total-entropy statement and the direction of heat flow (ev-157)
- **Reasoning**: suppose heat flowed spontaneously from a cold object to a hot one — energy would still be conserved and the first law's books would balance. But with `ΔS = Q/T`, the cold object loses Q and its entropy falls by `Q/T_cold`, while the hot object gains Q and its entropy rises by `Q/T_hot`; since `T_cold < T_hot`, `Q/T_cold > Q/T_hot`, so total entropy **falls**. The first law does not forbid this; the second law does. The textbook states that heat never goes the other way on its own and puts the reason in entropy
- **Evidence**: ev-156, ev-157
- **Attacked**: **"the second law cannot be derived from the first" is this repo's wording**; the textbook states the two laws separately and uses heat flow as an example, but does not write that sentence. The entropy arithmetic above is the repo's completion from `ΔS = Q/T`; the textbook gives only the qualitative argument.
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · Local entropy decrease and the total-entropy ledger (no attack yet)

- **Claim**: the entropy of a system can fall as long as the environment's entropy rises by more; the second law constrains the total of system plus environment
- **Premise**: the textbook's sentence `it actually is possible for the entropy of one part of the universe to decrease, as long as the total change in entropy of the universe increases.`, together with `ΔS_tot = ΔS_syst + ΔS_envir > 0` and the examples of picking up marbles, smelting iron ore into a bridge, and the sun lowering the entropy of local systems on Earth (ev-157)
- **Reasoning**: to test a process against the second law, draw the boundary wide enough to **include whatever supplies the work**. A refrigerator's compartment loses entropy, but the compressor consumes work and the surroundings gain more entropy; treating only the compartment as "the system" produces the illusion that entropy fell. The textbook makes `spontaneously` the keyword: a cold-to-hot heat transfer **needs work**, so it is non-spontaneous and outside the ban
- **Evidence**: ev-157
- **Attacked**: the textbook explains refrigerator-type processes only qualitatively and **gives no quantitative refrigerator example**; "the environment's entropy rises by more" is the repo's qualitative inference from `ΔS = Q/T`, not the textbook's calculation. The quantitative part is recorded as a gap
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; second node of the 选必三 "laws of thermodynamics" chapter; the entropy of the system is kept separate from total entropy | written after reading m54306 in full (ev-157) | @hpleapfrog |
