# Three statuses never used: the zero is now an auditable zero

> Open item: [README](../../README.en.md), item 2 of "Open questions that matter".
> Status rules: [FORMAT.md](../../FORMAT.en.md) §6; why "empty surviving set" had to be split in two lives in
> [the introduction of `失据`](status-and-liveness.md). Recorded 2026-10-20.

`已确证` / `争议` / `已推翻` have **never been used**. This used to be written as "not a gap that code can
fill" — a correct judgement, but with a form that invites the reading **"so leave it"**: a reader cannot
tell **"the rules blocked it"** apart from **"nobody looked"**. This record separates the two and
machine-checks the half that can be machine-checked.

## Status census (674 objects)

| Status | Count | What honestly producing it requires | What is missing: people or code |
|---|---|---|---|
| `暂定确认` | 51 | an argument exists and is unattacked | — |
| `有效` | 86 | the verdict for misconception / resource / path types | — |
| `待审` | 532 | nobody has ever argued it | content volume |
| `需复审` | 3 | an attack landed with an edge | review |
| `失据` | 2 | it was argued, and that argument was knocked down | — |
| **`已确证`** | **0** | **one independent reviewer who is not the author** | **people** (AI may not serve: M-07) |
| **`争议`** | **0** | **two surviving arguments with opposite conclusions** | **people** (someone must defend the attacked argument) |
| **`已推翻`** | **0** | **a surviving attack plus a claim with the opposite conclusion** | **people** |

The signature census is the other half of the same fact: across `author` fields and 变更记录 rows,
`@hpleapfrog` appears **1,379 times**, while `@alice` appears once, `@bob` once, `@carol` twice —
**and those three exist only inside historical changelog rows** (the example entries were cleaned on
2026-10-05; see the ⚠️ section of
[类比选择与学段相关](../../knowledge/physics/claims/analogy-by-stage.en.md)).
**"Single contributor" is not rhetoric; it is a count.**

## Why "there are attacks" is not "there is a dispute"

The corpus contains **4** `攻击` edges, landing on argument anchors of **4** entries:

| Attacked argument | Attacker | Attacker status | Current status of the attacked entry |
|---|---|---|---|
| `功与功率.md#k15` | [attack: work and power criterion](../../knowledge/physics/claims/attacks/work-power.en.md) | 暂定确认 | 需复审 |
| `教材内建分组教学变体.md#a1` | [attack: built-in tiered variants](../../knowledge/physics/claims/attacks/tieredguidance.en.md) | 暂定确认 | 需复审 |
| `运动物体自然慢下来.md#m1` | [attack: objects slow naturally](../../knowledge/physics/claims/attacks/slownaturally.en.md) | 暂定确认 | 需复审 |
| `类比选择与学段相关.md#a1` | [two samples cannot attribute](../../knowledge/physics/claims/analogy-stage-attribution-invalid.en.md) | 待审 | **失据** |

**All four attacked entries satisfy the "≥2 arguments" structural precondition for `争议`** —
which means what separates them from `争议` is not formatting but
**the attacks have no opponent**:

```
争议 requires: surviving set non-empty AND survivors contradicting each other
What we have:  every attacker survives (nobody counter-attacked)
               ⇒ no opposite conclusion inside the surviving set
```

`类比选择与学段相关` is the only entry where this chain ran to the end: A1 knocked down, A2 without
evidence ⇒ surviving set empty ⇒ and because the cause was "it was argued and lost", it became `失据`,
not `待审`. **That is the first time this library actually executed "attack → compute survival → set
status", and this record is where it stopped.**

### There are 2 `失据` entries, but only one of them was caused by an attack

| Entry | The road to `失据` | Inbound `攻击` edge? |
|---|---|---|
| [analogy by stage](../../knowledge/physics/claims/analogy-by-stage.en.md) | its argument was knocked down by **another proposition's attack** | ✅ yes |
| [Ohm's law](../../knowledge/physics/claims/ohm-law.en.md) | its A1 basis `ev-002` was judged **fabricated data and voided** — **no attacker, it collapsed on its own** | ❌ no |

> [!NOTE]
> **`失据` needs no opponent.** This matters for open item 2: it shows that
> **"a negative status" can be produced entirely by a single contributor plus evidence re-checking**,
> while `争议` / `已推翻` structurally require **a second pair of hands**. In other words, the strictest
> consequence this library can honestly produce today is `失据`; the two higher cells are not "not written
> yet" — they **require somebody to carry the opposing position**.

## What was added: `R-SCHEMA-19`

Code cannot produce a status, but it can make **"edit one field and get a high-status label"** a CI
failure. Three guards, each with its own reason:

| Status | Mechanical precondition | Why this one |
|---|---|---|
| `已确证` | **≥2 distinct `@` handles** across `author` + 变更记录 | if an independent review really happened, it left a signature; **an `已确证` without a trace is a self-assertion** |
| `争议` | the entry has **≥2 arguments** AND **≥1 inbound `攻击` edge** | with one argument, the correct outcome of being attacked is `失据` / `需复审` — **calling that `争议` fabricates a conflict** |
| `已推翻` | **≥1 inbound `攻击` edge whose attacker is citable** | if the attacker is itself `失据` / `待审`, **only the support was removed — write `失据`** |

> [!IMPORTANT]
> **Guards do not create statuses. They make the zero auditable.**
> The three `0`s now mean: **no entry can bypass the preconditions and be labelled a higher status** —
> so a reader who sees `0` can be sure it is **the result of a rule holding**, not of nobody watching.
> This is the library's standing demand about visible gaps: **making a gap visible is honesty; relaxing
> the rule is concealment** (see the end of [FORMAT.md](../../FORMAT.en.md) §6).

**Self-test**: all three guards have injected samples
(`sample_schema19_confirmed` / `_disputed` / `_overturned` in
[`tools/verify_rules.py`](../../tools/verify_rules.py)), so [docs/RULES.md](../RULES.en.md) marks them ✅
"someone verified that it fails" rather than "only a check function exists".

## Still open

- [ ] Invite one real reviewer (the only front door to `已确证`)
- [ ] Get a **defender** for an attacked argument (the only front door to `争议`)
- [ ] One person writing both the attack and the defence **does not count** — those are two directions of
      the same pair of hands
