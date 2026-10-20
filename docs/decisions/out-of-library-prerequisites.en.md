# Seven out-of-library prerequisites: Issue #17's trigger has been met, and the schema still was not changed

> Open item: [README](../../README.en.md), item 3 of "Open questions that matter".
> Field notes: [Issue #17](https://github.com/hpleapfrog/Scholia/issues/17)
> ("`先修` cannot express a prerequisite that lives outside the subject"). Recorded 2026-10-20.

Issue #17 ends with: **"leave this open. Once this kind of prerequisite accumulates 3–5 cases,
decide whether to change the structure. Do not design ahead of a real need."**

This section does two things: it **counts** the cases, and it explains **why the schema still was not
touched**.

## Seven cases (all quoted from entries that already exist in this library)

| # | Entry | The prerequisite it needs | Whose subject | How it is expressed today |
|---|---|---|---|---|
| 1 | [Reflection of light](../../knowledge/physics/concepts/reflection-of-light.en.md) | the geometric meaning of "angle" | Mathematics (junior-secondary geometry) | a WARNING in the body: "this concept has a prerequisite that is geometry, not physics"; `先修: []` |
| 2 | [Reflection · BL teaching method](../../knowledge/physics/methods/reflection-bl-geometry.en.md) | same | same | a row in the 关联 table: `先修｜"angle" in geometry`; `条件: the student has learned the concept of angle` |
| 3 | [Refraction](../../knowledge/physics/concepts/refraction.en.md) | angle **and inverse trigonometry** (`sin⁻¹` is not a power) | Mathematics | "the library lacks a 'geometric angle' prerequisite node" + "the 先修 edge cannot be attached" |
| 4 | [Refraction · BL teaching method](../../knowledge/physics/methods/refraction-bl-geometry.en.md) | the concept of angle | Mathematics | `先修｜angle (**no such node in this library yet**); being able to do division` |
| 5 | [Force (senior secondary)](../../knowledge/physics/concepts/force.en.md) | **vectors and vector addition** | Mathematics | WARNING: "'vector' is a prerequisite of this section, and it is not physics' — it belongs to mathematics", plus why the node does not exist |
| 6 | [Acceleration](../../knowledge/physics/concepts/acceleration.en.md) | vectors (the textbook's `[AL]` note: `See how much memory students remember about vectors`) | Mathematics | mentioned in prose only; nothing to link to |
| 7 | [Uniform circular motion](../../knowledge/physics/concepts/uniform-circular-motion.en.md) | **the vector direction of angular velocity (right-hand rule)** | Mathematics / competition-level physics | a 关联 row: `前置缺口｜not developed in this library` |

**The trigger condition has been passed**, and these are not seven copies of one sentence: the same "angle"
is written separately in **four** entries — reflection, the reflection teaching method, refraction, the
refraction teaching method (the textbook states the **same `[BL]` note twice**, in `ev-026` and `ev-038`).
**Recurrence is itself evidence that a node is warranted** — an inference already written into
[Refraction](../../knowledge/physics/concepts/refraction.en.md) that nobody acted on.

## "Progression" is growing the same way

| Entry | Relation | Status quo |
|---|---|---|
| [Inertia](../../knowledge/physics/concepts/inertia.en.md) | junior-secondary "forces and motion" → senior-secondary inertia: **progression, not prerequisite** | the author ruled "therefore no edge"; the reason lives in the body |
| [Forces and motion (junior)](../../knowledge/physics/concepts/forces-and-motion-jhs.en.md) | reference frame / speed & velocity: "an obvious progression relation" | unresolved: whether `先修` may cross stages has no precedent |
| [Uniform circular motion](../../knowledge/physics/concepts/uniform-circular-motion.en.md) | two `后续` rows: angular acceleration & rotational kinematics, torque | **the body already grew a `后续` convention on its own** — it simply never entered the schema |

> [!NOTE]
> A mechanical entry point already exists **and has never fired**: `check_graph` warns on `先修` edges whose
> stage sets are disjoint, and the warning text asks exactly "confirm this is a conceptual prerequisite,
> not a **progression** relation". The corpus has 23 `先修` edges and **0 of them trigger the warning** —
> not because cross-stage relations are absent, but because entries like
> [Inertia](../../knowledge/physics/concepts/inertia.en.md) that were judged "progression" **choose not to
> build the edge**. **So the moment that judgement is made, the machine stops seeing it**: the warning's
> input is a human brain, its output is "no edge" — and "no edge" is **exactly the same shape** as
> "nobody ever considered this".

## The three options, evaluated (numbered as in Issue #17)

| Option | Content | Assessment |
|---|---|---|
| **1** | add `外部先修` (free text), separate from `edges.先修` | **Recommended.** Smallest change; machine-checkable for "**was it declared**" without pretending to police content; the seven cases migrate directly |
| 2 | add a new object type "capability" next to `知识点` | **Cost exceeds benefit.** As an object it would need `依据`, `论证` and a bilingual twin — while the source for "can read an angle in geometry" is **a `[BL]` note inside a physics textbook**. Building that node means switching the collection target to maths textbooks |
| 3 | accept that this is just a remark, prose only | **What already happens** — the problem is that it is **unqueryable**: the seven cases above were found by manual grep, and the next person will not know there are seven |

The mechanical part of option 1 is narrow, and worth stating precisely — what it can and cannot police:

```
can police:   declaring 外部先修 without a stage/source → error
              the same name recurring in ≥2 entries (e.g. "angle", 4 times) → hint "consider building a node"
cannot police: whether the prerequisite is real or correctly placed — still a judgement, belongs with M-03
```

**That second "can police" line lands exactly on this section's seven cases**: "angle" would fire 4 times,
"vector" twice.

## Why the schema still was not changed

- **Schema changes require separate review** (this library's constraint: structural/format changes need
  their own approval and are not mixed into content batches). This round only supplies **the counts, the
  verbatim quotes, the option evaluation and the mechanical scope** as input to that review.
- **A schema change revalidates all 674 objects** and rewrites seven bodies into fields —
  that is a **structural change**, not content completion; committing them together hides what changed.
- If approved, the suggested order: add `外部先修` as an **optional field** (format checked, not
  mandatory), migrate the seven cases, only then discuss whether `进阶` / `后续` becomes a fourth edge kind.

> [!IMPORTANT]
> **This round did not close open item 3.** It moved it from "1 case, leave it hanging" to
> "7 cases, criteria in hand, waiting for one review". The difference between those states is not a
> percentage of progress — it is **whether a decision can be made at all**: deciding in the first state is
> guessing; deciding in the second has a basis.
