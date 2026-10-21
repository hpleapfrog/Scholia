# Scholia

> **A source-traceable knowledge base for AI and humans.**
> Every entry carries three things — **its source**, **its status**, and **the rebuttals against it**.
>
> 中文 → [**README.md**](README.md)

---

## Start here

| You are | Start |
|---|---|
| Someone who wants to learn | [**START.md**](START.en.md) — topic index · how to read an entry · what's here and what's not |
| **An AI agent** working in this repo | [**AGENTS.md**](AGENTS.md) — hard rules · how to edit · how to run checks |
| **An AI / program** reading content | [**llms.txt**](llms.txt) + parse [**index.json**](index.json) — what must not be quoted, each entry's real source |
| Wiring it into an agent | [`tools/scholia_mcp.py`](tools/scholia_mcp.py) — zero-dependency read-only MCP server |
| **Adding an entry** (contributor) | [`templates/`](templates/README.en.md) + `python tools/new_entry.py` — one command gives you a valid skeleton |
| **Building your own** (personal) | [`templates/`](templates/README.en.md) — copy the skeletons; no fork, no network |
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

> [!NOTE]
> **2026-10-20: the minimal goal is met.**
> The repository added a "mathematics" subject and ingested **all 308** Approved / Textbook errata
> in **Chapter 6** (Vector Calculus) of OpenStax *Calculus Volume 3* — **308 entries in a single
> chapter, ≥ 200**. The earlier 200-entry batch from Chapters 1–5 of *University Physics Volume 1*
> spans five chapters and remains recorded as-is in the
> [decision record](docs/decisions/errata-200-scope.en.md); the math batch's source, composition and
> structural change are in the [new decision record](docs/decisions/calc3-ch6-errata.en.md).

## Format & checks

**One concept = one `.md` file**: `front-matter` holds what machines need, the body what
humans need; GitHub renders it natively, and argument graphs are drawn with Mermaid.
Full spec in [FORMAT.md](FORMAT.en.md); the rule registry is [docs/RULES.md](docs/RULES.en.md).

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
| 对象 / Objects | **718** —— 教法 methods 46 · 知识点 concepts 71 · 命题 claims 579 · 误解 misconceptions 9 · 资源 resources 8 · 路径 paths 5 |
| 事件 / Events | **2** —— 顶层 `events/`，与对象**分开**（无论证、无真值） |
| 学科 / Subjects | 物理 Physics 342 · 生活 Life 8 · 医学 Medicine 8 · 地理 Geography 6 · 科学 Science 1 · 交通 Transport 4 · 计算机 Computing 29 · 经济 Economics 8 · 法律 Law 4 · 数学 Mathematics 308 |
| 证据 / Evidence | 188（含作废 / void 5） |
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

1. **Can a bilingual entry drop below 5 minutes?** ← **decides the project's survival**. **The unit of that
   "5 minutes" is now fixed** (2026-10-20, by the author): **one bilingual pair** — Chinese body + English
   translation + both registers — **not** one language. [`templates/`](templates/README.en.md)
   and `tools/new_entry.py` are in place (structure to the script, content to the human). The first trial
   ([area under a velocity–time graph](knowledge/physics/claims/velocity-time-graph-area.en.md)) left only a
   total: about 12 minutes — **2.4× the fixed budget**. The second (2026-10-20,
   [HTTP 451 refuses access for legal reasons](knowledge/computing/claims/http-451-legal-unavailable.en.md))
   was **stamped per phase**: **13 min 16 s of wall clock for the bilingual pair — at most 2.6× the budget,
   not met**. Inside that, topic selection → Chinese body finished took **4 min 9 s** (an uninterrupted
   segment); the **9 min 7 s** from there to the finished index went almost entirely to the **bilingual
   parallel structure, evidence registration and index counts**; the skeleton took **319 ms** and full
   validation **2.2 s** — **the toolchain is not the bottleneck** (reproduced). **But that 9 min 7 s contains
   one session interruption** (its completion timestamp was backfilled), so "at most 8 min 16 s to cut" is an
   upper bound and the pure-work multiple is **unmeasured**. **Whatever has to go, it lives only in the
   parallel structure** — and this round falsified one of
   this library's own assumptions: **"P7→P9 is pure structural copying, so it can be scripted wholesale" is
   only half true**. The subject index tables come in **7 header shapes**, and 4 of them carry columns
   (`证据等级`, `位置`+`错误类型`, `目标`+`自检`, `禁忌`) that are **content, not formatting**; the evidence
   register is split into **3 batch blocks** and its `定位` column is a hand-written reading record — the
   column that caught this round's wrong title.
   **Human timing remains unmeasured**: agent timing logs "283 lines read" as 17 seconds, which is not true
   of a person. A third trial on 2026-10-21 split P7→P9 into four stamps: **3 min 44 s of agent wall clock**,
   with a bilingual tail of **61 s** — but the source was small, the topic was chosen by the repository, and
   the English page was an immediate translation, so **this is not a passing reading**; it proves only that the
   four phases can be timed and that the toolchain is still not the bottleneck. Phase data, findings and the
   remaining compression scope → [decision record](docs/decisions/entry-cost-phases.en.md)
2. `已确证` / `争议` / `已推翻` are **all 0**. This is **still not a gap code can fill** — what is missing is
   **people** (a reviewer, a defender). But code can make the **zero auditable**: `R-SCHEMA-19` now checks
   each status's structural precondition (`已确证` needs **≥2 distinct handles** across `author` + changelog;
   `争议` needs **≥2 arguments and ≥1 inbound `攻击` edge**; `已推翻` needs an **attack that is citable**,
   otherwise write `失据`). Measured: the corpus has 4 `攻击` edges, and all four attacked entries already
   satisfy "≥2 arguments" — the only thing absent is **an opponent for the attack**. The signature census is
   the same fact from the other side: `@hpleapfrog` 1,379 times, the other three handles only in historical
   changelog rows. → [decision record](docs/decisions/status-zero-is-auditable.en.md)
3. Prerequisites outside the subject cannot be expressed ([Issue #17](https://github.com/hpleapfrog/Scholia/issues/17)):
   **the count has grown from 1 to 7** — "angle in geometry" ×4 (reflection, its teaching method, refraction,
   its teaching method), "vector" ×2 (force, acceleration), "vector direction of angular velocity" ×1
   (uniform circular motion); "progression" has 3 instances and the body text even grew a `后续` convention
   on its own — **the "wait for 3–5 cases" trigger has passed**. Recommended: **option 1** of Issue #17
   (an optional `外部先修` field; machine-check "was it declared" and "does the same name recur").
   **A schema change needs its own review and was not made this round**: what is delivered here is an input
   to that review, not its outcome. → [decision record](docs/decisions/out-of-library-prerequisites.en.md)
4. Support-edge independence cannot be computed; goal coverage counts "whether", not "how well".
   **Both sentences were split into a computable half and a human half.** `R-GRAPH-06` computes **the same
   source identifier** (measured: `教材内建分组教学变体#a3` has **42 support edges · 21 pieces of evidence ·
   1 source identifier** — the line "the same source repeated 26 times" has grown to 42, still from one book);
   `R-GRAPH-07` computes **redundancy and reading depth** (all 15 learning outcomes are covered, but
   **11 of them, 73%, are taught exactly once**). **Cross-source independence still belongs to `M-03`.**
   This item also produced one **falsely clean** lesson: the first version parsed the sequencing table by
   column position and reported an unreadable path as "no redundancy problem". That branch now has **two**
   injected samples, the second one pushing the 覆盖 column off the end of the table, and reverting to the
   first implementation measurably dropped **the paths reporting single-step coverage from 4 to 2** →
   [support-count](docs/decisions/support-count-not-strength.en.md) ·
   [coverage](docs/decisions/coverage-is-not-strength.en.md)

## Layout

```
knowledge/         knowledge objects: concepts · claims · methods · misconceptions · paths · resources
evidence/          evidence index and reproducible raw data
docs/RULES.md      rule registry (mechanically enforced vs. human-reviewed)
docs/decisions/    the "why" behind rules — cases, incidents, inferences (moved out, not deleted)
tools/             kbcheck.py (validator) · scholia_mcp.py (MCP server)
```
