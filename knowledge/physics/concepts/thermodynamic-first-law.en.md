---
id: kb:physics:thermodynamic-first-law
type: 知识点
title: "First law of thermodynamics"
status: 待审
author: "@hpleapfrog"
created: 2026-10-21
updated: 2026-10-21
scope:
  学科: 物理
  学段: 高中
  适用: students who have done "Work and power" and "Conservation of mechanical energy" and are meeting heat and work in one energy ledger for the first time
  条件: covers only `ΔU = Q − W` for a closed system, with the OpenStax sign convention (Q positive for net heat in, W positive for net work done by the system); heat engines, cyclic processes, and heat capacity are out of scope
edges:
  先修: ["[Work and power](work-and-power.en.md)", "[Conservation of mechanical energy](conservation-of-mechanical-energy.en.md)"]
  支持: []
  攻击: []
evidence: [ev-156]
license: CC-BY-SA-4.0
---

> **English version of [`热力学第一定律.md`](热力学第一定律.md).**

> [!TIP]
> **After reading this entry you should** be able to write `ΔU = Q − W`, say what the sign of `Q` and of `W` each means, and explain why two completely different processes can give the same `ΔU`

## Definition

The **first law of thermodynamics** is energy conservation kept as a ledger that includes heat: for a **closed system**, the change in internal energy equals the net heat transferred into the system minus the net work done by the system.

```
ΔU = Q − W
```

- `ΔU`: change in internal energy, in J. Internal energy `U` is the sum of the kinetic and potential energies of the system's atoms and molecules; the textbook says
  `The internal energy U of a system depends only on the state of the system, and not how it reached that state.` — it is fixed by the state (P, V, T), not by the path
- `Q`: net heat in. `Q > 0` means net heat flows into the system; `Q < 0` means net heat flows out
- `W`: net work done **by** the system. `W > 0` means the system does net work on the outside; `W < 0` means the outside does net work on the system
- all three are energies in joules; only `ΔU` can be stored — `Both Q and W represent energy in transit; only ΔU represents an independent quantity of energy capable of being stored.`
- at constant pressure, a gas does work `W = PΔV`

> [!IMPORTANT]
> **The same problem can differ by a minus sign between conventions.**
>
> This entry follows the main text's convention: `ΔU = Q − W`, where `W` is the work done **by** the system. The textbook itself notes that Sal uses another convention:
> `Note that Sal uses the equation ΔU=Q+W, where W is the work done on the system, whereas we use W to represent work done by the system.`
> So in `ΔU = Q + W`, `W` is the work done **on** the system. Both equations state the same law; only the positive direction of `W` differs. The error comes from **mixing the conventions**, not from choosing one.

## Relations

| Relation | Entry |
|---|---|
| Prerequisite | [Work and power](work-and-power.en.md) — `W = Fd` is where `W = PΔV` comes from; [Conservation of mechanical energy](conservation-of-mechanical-energy.en.md) — first learn to keep an energy ledger in a closed system, then the first law adds heat to the same ledger |
| Follow-up | [Second law of thermodynamics](thermodynamic-second-law.en.md) — the first law balances the books, not the direction of the process |
| Recorded gap | **Internal energy (microscopic definition)**, **heat capacity and specific heat**, **heat engines and efficiency** are not built in this repo; "heat" as a mode of energy transfer has no node of its own |

## Argument

### K1 · Internal energy is fixed by the state; Q and W are process quantities (no attack yet)

- **Claim**: `ΔU` is fixed by the initial and final states, while `Q` and `W` vary from process to process
- **Premise**: after defining the first law, the textbook writes `The internal energy U of a system depends only on the state of the system, and not how it reached that state.`, and gives two worked examples with completely different Q/W pairs but the same `ΔU = 9.00 J` (ev-156)
- **Reasoning**:
  1. first example: net heat in 15.00 J, net work out 6.00 J, `ΔU = 15.00 − 6.00 = 9.00 J`
  2. second example: net heat out 150.00 J, work done on the system 159.00 J, `ΔU = −150.00 − (−159.00) = 9.00 J`
  3. the textbook's discussion says `Two different processes produce the same change in a system... its final state is related to internal energy, not how that energy was acquired.` — `ΔU` is locked by the endpoints, while `Q` and `W` are the bookkeeping along the path
- **Evidence**: ev-156
- **Attacked**: **the textbook does not use the label "state function"** — its sentence only says that internal energy depends on the state and not on how it was reached; "状态量" is this repo's transcription. Also, the two examples only show that two different Q/W pairs give the same `ΔU`; they **do not prove** it holds for every path. The textbook states it as a property of internal energy.
- **Attribution**: @hpleapfrog · 2026-10-21

### K2 · The sign convention is not part of the law (no attack yet)

- **Claim**: `ΔU = Q − W` and `ΔU = Q + W` are not two laws but two bookkeeping conventions for the same law
- **Premise**: the main text uses `W` for work done by the system and notes `if W is positive, then there is net work done by the system`; it also notes that Sal's `W` is work done on the system (ev-156)
- **Reasoning**: replacing `W` with `−W` turns one equation into the other; `ΔU` and every physical conclusion stay the same. What produces wrong answers is **mixing the two conventions in one equation**, not choosing one of them
- **Evidence**: ev-156
- **Attacked**: no attacks yet
- **Attribution**: @hpleapfrog · 2026-10-21

## Change log

| Date | Change | Basis | By |
|---|---|---|---|
| 2026-10-21 | Entry created; first node of the 选必三 "laws of thermodynamics" chapter, attached to the energy thread "work and power → conservation of mechanical energy" | written after reading m54305 in full (ev-156) | @hpleapfrog |
