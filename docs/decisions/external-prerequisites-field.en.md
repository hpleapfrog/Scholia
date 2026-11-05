# Out-of-library prerequisites finally have a field: the five-part `外部先修` structure and the seven-case migration

> Closes item 3 of "Open questions that matter" in [README](../../README.en.md).
> The pre-review counts, verbatim quotes and three options are in
> [seven out-of-library prerequisites](out-of-library-prerequisites.en.md);
> field notes in [Issue #17](https://github.com/hpleapfrog/Scholia/issues/17).
> Recorded 2026-10-29.

## The decision

Add an **optional** front-matter field, `外部先修`, **separate from** `edges.先修`:

```yaml
外部先修:
  - 名称: 几何中的角
    标识: angle
    学科: 数学
    学段: 初中
    来源: ev-026
```

It declares "**to understand this, you first need X**", where **X has no node in this library**.
It is therefore **not a graph edge**: it takes no part in the `先修` acyclicity check, does not enter
`objects[].先修`, and does not mean the library owns X.

## Why not free text

Option 1 in Issue #17 said "a free-text field". The implementation uses **five structured subfields**
instead, because free text solves "it got written down" but not these three problems:

| Problem | Consequence of free text | Consequence of structured fields |
|---|---|---|
| **The same prerequisite recurs** | "角", "几何中的角", "angle" are three strings; you cannot count "four entries need it" | `标识: angle` groups and counts; ≥2 objects triggers "consider building a node" |
| **Where did this prerequisite come from** | no place for a source; "the textbook says it is a prerequisite" is unverifiable | every item requires a `来源: ev-###`, reusing `R-EVID-01` for existence and voiding |
| **Chinese/English alignment** | translating the name makes the two sides unequal; not translating reads badly | `名称` may be translated; `标识` / `学科` / `学段` / `来源` must match and can be checked |

Put differently: **free text records "someone mentioned it"; structured fields record "who mentioned it,
where, and across how many entries".** The latter is exactly what Issue #17 lacked — the seven cases
were found by manual grep in the first place.

## The five subfields

| Subfield | Rule | Why |
|---|---|---|
| `名称` | human-readable, translatable | the body and the index are read by people |
| `标识` | `[a-z0-9][a-z0-9-]*`, unique within an entry, reused across entries | **the only countable key**; Chinese names, English names and aliases are all unstable |
| `学科` | free text; a subject not registered here is only a **warning** | an out-of-library prerequisite may legitimately come from an unregistered subject; do not block it outright |
| `学段` | enum: 小学 / 初中 / 高中 / 大学 / 不限 | same enum as `scope.学段`; no second vocabulary |
| `来源` | **one** registered `ev-###` | one declaration maps to one verifiable source; list several sources by writing several declarations |

> `来源` is deliberately not an array: an array mixes "one declaration" with "a set of evidence",
> and no rule here can yet judge whether that set is independent. Keep it one-to-one; extend when
> a real need appears.

## The seven-case migration (8 declarations / 4 keys)

| `标识` | Name | Subject · stage | Entries | Source |
|---|---|---|---|---|
| `angle` | the geometric angle | Mathematics · junior secondary | [Reflection](../../knowledge/physics/concepts/reflection-of-light.en.md) · [reflection BL method](../../knowledge/physics/methods/reflection-bl-geometry.en.md) · [Refraction](../../knowledge/physics/concepts/refraction.en.md) · [refraction BL method](../../knowledge/physics/methods/refraction-bl-geometry.en.md) | `ev-026` / `ev-038` |
| `inverse-trig` | inverse trigonometric functions | Mathematics · senior secondary | [Refraction](../../knowledge/physics/concepts/refraction.en.md) | `ev-038` |
| `vector` | vectors and vector addition | Mathematics · senior secondary | [Force (senior)](../../knowledge/physics/concepts/force.en.md) · [Acceleration](../../knowledge/physics/concepts/acceleration.en.md) | `ev-041` / `ev-039` |
| `angular-velocity-vector` | vector direction of angular velocity (right-hand rule) | Physics · senior secondary | [Uniform circular motion](../../knowledge/physics/concepts/uniform-circular-motion.en.md) | `ev-080` |

- **`angle` in 4 entries, `vector` in 2** — exactly the shape "recurrence ⇒ consider a node" is meant to catch.
- The English editions migrated in step; `名称` is translated, while `标识` / `学科` / `学段` / `来源`
  match the Chinese original.
- The existing prose **stays**: the field answers "was it declared", the body answers "why this one".
  They are not duplicates; deleting the prose would turn the migration into information loss.

## What the machine does and does not police

**Policed (`R-SCHEMA-20`, blocking)**:

- `外部先修:` declared with no list items;
- a list item missing one of the five subfields, an unknown subfield, or a repeated subfield in one item;
- `标识` not matching `[a-z0-9][a-z0-9-]*`, or repeated within one entry;
- `学段` outside the enum;
- `来源` not a single `ev-###`.

**Policed (`R-EVID-01`, blocking)**: `来源` points at a non-existent or voided evidence id.

**Hints (non-blocking)**:

- the same `标识` in ≥2 objects → "consider building a node";
- the same `名称` with different `标识` → possibly one prerequisite written as two keys;
- `学科` not registered here → confirm it is not a typo.

**Not policed (`M-12`, human judgement)**:

- whether the prerequisite is **truly required**;
- whether to **build a concept node** for it;
- whether "progression / follow-up" is a prerequisite.

> [!IMPORTANT]
> **A recurrence hint is not a command to create a node.** `angle` appearing 4 times is a strong
> signal, but building the node requires its scope, evidence and bilingual body — none of which
> counting can supply. The machine turns "four people mentioned it" into a checkable fact; the
> decision remains human.

## Surface area

| Location | Change |
|---|---|
| `tools/kbcheck.py` | field parsing, `R-SCHEMA-20`, the out-of-library branch of `R-EVID-01`, bilingual comparison, index generation |
| `index.json` | `schema_version` 3 → 4; per-object `外部先修`; top-level grouping by `标识` |
| `citations.json` | `schema_version` 1 → 2; each citation carries resolved out-of-library sources |
| `tools/scholia_mcp.py` | new `scholia_external_prereqs` tool; search and entry briefs include out-of-library prerequisites |
| `tools/new_entry.py` | repeatable `--external-prereq`; the scaffold emits a valid block |
| `tools/make_tasks.py` | new `external` task group (recurring keys become work items) |
| `tools/verify_rules.py` | 6 injected samples: missing subfield, bad `标识`, empty declaration, recurrence, bad source, bilingual mismatch |
| six templates | `{{EXTERNAL_PREREQS}}` placeholder |
| `FORMAT` / `CONTRIBUTING` / `llms` / `README` / `AGENTS` | field semantics, self-check item, AI reading contract, tool list |

## What remains unresolved

- **"Progression / follow-up" is still unmodelled.** It is not an out-of-library prerequisite:
  one is a deeper layer of the same topic, the other is where to go after finishing. The three
  existing instances stay in prose; whether they become a fourth edge kind needs another decision.
- **The migration covers the seven known cases only.** Other prerequisite remarks may exist in
  bodies without having been grepped; new entries are prompted by the checklist and `new_entry`,
  while old entries get updated on their next edit.
- **Building the node is still human work.** This field produces a list of "consider building a
  node", not the node itself.

## Verification

- `python tools/kbcheck.py` passes; `index.json` / `citations.json` / `docs/RULES.md` are regenerated
  by `--write-index`.
- Full `python tools/verify_rules.py`: 55/55 samples fire (covering 44 rules; **a snapshot from
  that time** — current numbers are in [`docs/RULES.en.md`](../RULES.en.md)).
- `python tools/verify_rules.py --only R-SCHEMA-20`: 4/4 samples fire; the new branches under
  `--only R-EVID-01` and `--only R-BILING-02` also fire.
- Measured recurrence: `angle` appears in 4 entries, `vector` in 2.
