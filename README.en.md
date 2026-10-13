# Scholia

> **A source-traceable knowledge base for AI and humans.**
> Every entry carries three things — **its source**, **its status**, and **the rebuttals against it**.
>
> 中文 → [**README.md**](README.md)

---

## Start here

| You are | Start |
|---|---|
| Someone who wants to learn | [**START.md**](START.md) — topic index · how to read an entry · what's here and what's not |
| **An AI agent** working in this repo | [**AGENTS.md**](AGENTS.md) — hard rules · how to edit · how to run checks |
| **An AI / program** reading content | [**llms.txt**](llms.txt) + parse [**index.json**](index.json) — what must not be quoted, each entry's real source |
| Wiring it into an agent | [`tools/scholia_mcp.py`](tools/scholia_mcp.py) — zero-dependency read-only MCP server |
| Curious how it's built | keep reading |

---

## Mission: remove noise, keep what's traceable

**Noise is not "wrong things" — it is "things you cannot trace."** An unsourced claim is
more dangerous than a sourced mistake: the latter can be fixed; the former, you don't even
know where to start.

| It does **not** | It **does** |
|---|---|
| ❌ Decide "what is true" | ✅ Attach **evidence and rebuttals** to every claim |
| ❌ Let a majority or an authority rule | ✅ Compute status from **evidence grade + rebuttal structure**, by rules |
| ❌ Claim to be reliable | ✅ Make **checkability** visible: who signed it · where it came from · who attacked it · whether it survived |

**This is not a manifesto — it has already run three times:** data fabricated to demo the
format nearly got quoted as evidence (voided, ID kept); an attribution claim with n=2 from a
single source was downgraded to `失据` (unsupported); a claim boasting 15 supporting edges was
found to come entirely from one book. **All three were caught by the mechanism, not by luck.**

## What this is

Textbooks contain mistakes; teachers tell you about them by word of mouth. Scholia
institutionalizes that. The protocol layer answers only three questions — **who signed this?
where did it come from? what does it conflict with?** — and **never** answers "what is true."
Truth is decided by each reader. The knowledge graph is one; a textbook is that graph
projected for one reader.

**Three commitments:**

1. **Voting cannot decide truth.** A minority with hard evidence is not erased by numbers.
2. **Knowledge must converge; teaching methods must coexist.** Ranking methods is dogma.
3. **Exitable.** Anyone can fork away with full history, without anyone's permission.

**Minimal goal:** finish one chapter of one textbook — 200 errata, the full path from 0 to 200.
Not "backing up human knowledge."

## Format & checks

**One concept = one `.md` file**: `front-matter` holds what machines need, the body what
humans need; GitHub renders it natively, and argument graphs are drawn with Mermaid.
Full spec in [FORMAT.md](FORMAT.md); the rule registry is [docs/RULES.md](docs/RULES.md).

```bash
python tools/kbcheck.py     # zero-dependency, offline; run once before committing
```

It checks two levels: **per-file** (front-matter, status validity, duplicate ids, broken links
and anchors, required sections and their order, non-empty evidence, stage/level/date/author
values, medical disclaimer block) and **graph** (prerequisite acyclicity, attack-edge anchors,
path gaps, goal coverage — an uncovered outcome is a hard failure). **Every rule is verified
with an injected error, not just written down.** A read-only **CI**
([`.github/workflows/kbcheck.yml`](.github/workflows/kbcheck.yml)) runs it on every PR.

## Contributing

| You want to | Where | Affects conclusions? |
|---|---|---|
| Ask, discuss method, share rough ideas | **Discussions** | ❌ **No** |
| Report a suspected error, submit a method | **Issue** (template) | Indirectly |
| Actually change the knowledge | **PR** | ✅ **The only channel that can** |

Two guardrails: **`status` may only be written by the PR author, by the rules** (writing
`已确证`/confirmed needs an independent non-author review); **👍 only ranks attention, never decides.**

## License & disclaimer

| Part | License |
|---|---|
| Knowledge content (`knowledge/` `evidence/` `README.md` `CONTRIBUTING.md`) | **CC BY-SA 4.0** (commercial OK; derivatives stay open) |
| Code (`tools/`) and format spec (`FORMAT.md`) | **MIT** |

Attribution: see each entry's `author` field and the commit history; keeping a link back to
this repository satisfies attribution.

> [!CAUTION]
> - **This is not a textbook, and not a teaching prescription.** "Confirmed" (`已确证`) does not
>   mean absolutely correct — **and there are currently none** (see below).
> - **`争议` (disputed) is an honest outcome, not a defect.** All teaching methods are
>   conditional; always check the contraindications field.
> - **Never upload textbook text or scanned pages** — only locators, short quotes, and original
>   summaries. Facts are not copyrightable; expression is.
> - **Medical entries carry a population qualifier and a disclaimer block**; relay them together.
> - **Sources are vetted too**: registering evidence requires "who publishes it · which version, and when did it take effect ·
>   was it made up for this citation" — **a link that opens is not the same as a source that is true**
>   (see the [evidence threshold](evidence/README.en.md)).
> - Provided "as is", with no warranty.

## Status

<!-- kbcheck:begin -->
| | |
|---|---|
| 对象 / Objects | **129** —— 教法 methods 45 · 知识点 concepts 23 · 命题 claims 44 · 误解 misconceptions 8 · 资源 resources 8 · 路径 paths 1 |
| 学科 / Subjects | 物理 Physics 86 · 生活 Life 5 · 医学 Medicine 2 · 地理 Geography 6 · 科学 Science 1 · 交通 Transport 4 · 计算机 Computing 13 · 经济 Economics 8 · 法律 Law 4 |
| 证据 / Evidence | 55（含作废 / void 5） |
| 已确证 / Confirmed | **0** |
<!-- kbcheck:end -->

Sources: OpenStax *Physics* (**CC BY**) · Utah Grade-7 Science · publisher errata · AASM clinical
guideline · randomized controlled trials.
Closed issues / PRs: see [merged pull requests](https://github.com/hpleapfrog/Scholia/pulls?q=is%3Apr+is%3Amerged) (**no hard-coded numbers — they drift**).

> [!NOTE]
> **The table above is generated by `kbcheck.py`** (the single source is [`index.json`](index.json));
> it is **never hand-written** — a hand-written number drifts, and a drifting number is an assertion.

> [!IMPORTANT]
> **Nothing is "confirmed" yet.** That needs an **independent non-author review**, and there is
> currently one contributor. **The rules are being followed, not missing.**

## Open questions (the important ones)

1. **Can entry cost drop below 5 minutes?** ← **decides the project's survival** (most entries
   are 30–60-minute full objects, the opposite of the "start from single errata" advice).
2. `已确证` / `争议` / `已推翻` **have never been used** — a single contributor cannot produce them
   honestly; this is not a gap code can fill.
3. Prerequisites outside the subject cannot be expressed ([Issue #17](https://github.com/hpleapfrog/Scholia/issues/17), waiting for 3–5 cases); there is no way to express "advanced".
4. Support-edge independence cannot be computed (sources are free text); goal coverage counts
   "whether", not "how well".

## Layout

```
knowledge/         knowledge objects: concepts · claims · methods · misconceptions · paths · resources
evidence/          evidence index and reproducible raw data
docs/RULES.md      rule registry (mechanically enforced vs. human-reviewed)
docs/decisions/    the "why" behind rules — cases, incidents, inferences (moved out, not deleted)
tools/             kbcheck.py (validator) · scholia_mcp.py (MCP server)
```
