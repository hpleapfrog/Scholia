# Templates: pushing a bilingual entry toward the 5-minute budget

> 中文 → [**README.md**](README.md)

> [!IMPORTANT]
> **This folder answers the project's open question #1**: "can entry cost drop under 5 minutes?"
> **The author fixed the unit: one bilingual pair** (Chinese body + English twin + both registers).
> **This folder removes structural friction; it does not meet the budget.** The phased trial came in at
> **13 min 16 s per bilingual entry = 2.6× the budget**, while the skeleton took **319 ms** and validation
> **2.2 s** — **the toolchain was never the bottleneck**. The gap and the three ways out are in
> [phase-by-phase entry cost](../docs/decisions/entry-cost-phases.en.md).
> Until now almost every entry was a full 30–60 minute object — the opposite of the advice to
> "start from a single erratum", and the most likely way a single-contributor project dies.
>
> **Templates lower friction, not standards.** Every citation, argument and caveat still has to be written.

## Two ways

**One command (recommended):**

```bash
python tools/new_entry.py --type claim --subject 物理 --slug deceleration-not-a-term --title "「减速」不是物理术语"
```

It picks the folder by type, copies the matching template, fills `id` / `author` / `date` / `license`,
and prints what is still missing.

**Copy by hand:** open `命题.md` / `知识点.md` / …, copy the fenced block, save it as
`knowledge/<subject>/<type>/<title>.md`, and replace the `{{…}}` placeholders.

## Which template (don't pick wrong)

| What you have | Template | Goes in | Test |
|---|---|---|---|
| A **concept** | [知识点](知识点.md) | `concepts/` | it's "what it is"; no truth value |
| A **claim that can be false** | [命题](命题.md) | `claims/` | it **can be rebutted**, and you can say why it holds |
| A **way of teaching** | [教法](教法.md) | `methods/` | it answers "how to teach"; holds **conditionally** |
| A **common misunderstanding** | [误解](误解.md) | `misconceptions/` | "where many people go wrong", as an asset |
| A **learning order** | [路径](路径.md) | `paths/` | an arrangement of concepts; every step links to an entry |
| An **external resource** | [资源](资源.md) | `resources/` | it only says "where it is", never what it says |
| Something that **happened** | [事件](事件.md) | top-level `events/` | time and evidence only, **no claim to attack** |

**Folder names are English** (`knowledge/<subject>/claims/`); **filenames stay Chinese**
(`欧姆定律.md`) — paths must work as URLs, names must be readable by people ([FORMAT](../FORMAT.en.md) §2).

> When unsure, ask: **can this be rebutted?** If yes → `命题`. If no → concept, method,
> misconception, order or material.

## The English edition: filename derived from the `id`

Every entry also has an English edition. **Its filename is not "Chinese name + `.en.md`"** — it is
derived from the `id`:

```
id:  kb:physics:kp-frame-of-reference
zh:  knowledge/physics/concepts/参考系.md
en:  knowledge/physics/concepts/frame-of-reference.en.md
```

Rule: take the last segment of the `id` → drop the type prefix (`kp-` `prop-` `method-` `mis-`
`path-` `res-` `attack-`) → add `.en.md` → put it in the **same folder** as the Chinese original.

`python tools/new_entry.py` prints **that filename** when it finishes — just copy it.

The first line of an English page is fixed:

```markdown
> **English version of [`参考系.md`](参考系.md).**
```

> [!IMPORTANT]
> **A missing translation does not fail the check** (it is listed on every run), but a
> **filename not derived from the `id`** or **an English page linking to a Chinese page** does
> (`R-BILING-01` / `R-LINK-03`). Why: [decision record](../docs/decisions/english-filenames-from-id.en.md).

## Placeholders

| Placeholder | Fill with | Who |
|---|---|---|
| `{{ID}}` | `kb:<subject-slug>:<your-slug>` — stable across renames | script, from `--slug` |
| `{{TITLE}}` | human-readable title | script |
| `{{AUTHOR}}` | `@handle`, **never anonymous** | script (`--author`, default `@hpleapfrog`) |
| `{{DATE}}` | `YYYY-MM-DD` | script (today) |
| `{{EVIDENCE}}` | evidence id, e.g. `ev-073` — **register it in `evidence/README.md` first** | **you** |
| `{{SUBJECT}}` `{{STAGE}}` `{{LEVEL}}` | subject (optionally with a direction) · stage enum · level | script defaults, **you verify** |
| `{{APPLY}}` `{{CONDITION}}` | **for whom · under what conditions** (without these, every conclusion gets misused) | **you** |
| `{{KPATH}}` | relative path from a method back to its concept | **you** |

## What the checker will still block (on purpose)

| Error | Why |
|---|---|
| `evidence` id not in the index (`R-EVID-01`) | the template writes `ev-000` (a placeholder). Register a real source in [`evidence/README.md`](../evidence/README.en.md) |
| **not registered in the subject README** (`R-README-01`) | new entries must appear in `knowledge/<subject>/README.md` |
| `暂定确认` with unread evidence (`R-EVID-03`) | you can't "confirm" what you haven't read; write `待审` / `有效` honestly |

```bash
python tools/kbcheck.py
```

## Never downgrade content to pass the check

**Keep the section and write "no data yet"** — always better than deleting the section or loosening
the rule. Visible gaps are honest; loosened rules hide them.
