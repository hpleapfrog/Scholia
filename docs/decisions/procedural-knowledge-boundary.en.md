# What the repo does not hold: the boundary of procedural knowledge

> Rule: [FORMAT.md](../../FORMAT.en.md) "What the repo does **not** hold: procedural knowledge".
>
> **In one sentence**: of the six object types, none can hold "a step of operation". This is an **acknowledged boundary**, not a pending gap.

## How it was settled: three probes

### First two (taking the subway / flying) — both rejected by `check_path_steps`

Writing **"from entering to exiting the station"** (subway) and **"from check-in to arrival"** (flying) as `路径`:

| Probe | Steps that name no object |
|---|---|
| taking the subway | steps **3, 4** of 4 |
| flying | steps **2, 3, 4** of 4 |

**"Check-in → security → boarding" is an action sequence, and the repo has no object that represents "an action".**

### Third (a ventilator) — brought the second criterion

The question "**how is a ventilator adjusted**". Adjusting a ventilator is also procedural knowledge (set parameters → read feedback → adjust again),
**but it is not the same as the first two samples**:

| Sample | Process | Consequence of getting it wrong |
|---|---|---|
| taking the subway | enter → exit | wrong direction |
| flying | check-in → arrival | missed flight |
| **ventilator** | **adjust parameters** | **patient death** |

**The scarcity criterion does not apply here**: how to adjust a ventilator is **not "everywhere"** (it is scarce).
So by the first criterion alone, the repo **should** include it — and that would be wrong.

## Criterion 1: scarcity

This boundary is not an aesthetic preference; it has a statable criterion — **and the criterion comes from the cited regulation itself**:

| | Visible on-site | Not visible on-site |
|---|---|---|
| example | where check-in is, how to get through security, where the gate is | **why** involuntary refunds are free, **within how many days** a refund must arrive, **what rights you have** when overbooked |
| what the regulation says | 《公共航空运输旅客服务管理规定》**Article 28** requires airports to **set up signage guidance** in key areas | **no mechanism** guarantees passengers know |
| nature | **noise** — everywhere, and the regulation guarantees availability | **real information** — scarce, and no one is obliged to tell you |
| the repo's stance | **do not repeat** | **include it, with the source article number** |

**This matches the mission**: repeating what is everywhere only adds noise.

## Criterion 2: risk

**The repo cannot make the reader know "who this applies to".**
A "tidal volume 6 mL/kg" written here, followed by someone **without bedside data** —
**the repo can neither prevent it nor answer for it.**

| # | Criterion | What is not held |
|---|---|---|
| 1 | **scarcity** | procedures found everywhere (repeating them only adds noise) |
| 2 | **risk** | **procedures whose error is irreversible and whose audience the repo cannot bound** |

> **Criterion 2 excludes "procedures", not "conclusions".** The trial's **conclusion** that "low tidal volume reduces mortality" is still included
> (see [`knowledge/医学/`](../../knowledge/医学/README.en.md)) —
> **because a conclusion with a source can be checked, while an instruction will be followed.**

## If this boundary is to change later

**To add an object type that can hold "an action", you need:**

1. **A new sample, of a different shape from the existing three** (e.g. "a procedure that branches on a condition")
2. An explanation of **why `路径` cannot satisfy it**, not "the name looks more like it"
3. A clear idea of **how it is attacked** — every object in the repo must be able to answer "why do I say so",
   and **no one yet knows what the argument for an operation step looks like**

**Not accepted**: relaxing `路径` to allow inline steps. That would invalidate the definition "路径 = an arrangement of 知识点",
and `check_path_steps` is the mechanical version of exactly that definition.

> The full failure messages of the two probes are in [`knowledge/生活/README.md`](../../knowledge/生活/README.en.md).
