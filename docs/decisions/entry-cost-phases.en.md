# Phase-by-phase entry cost: the Chinese text lands first; the bilingual bookkeeping is the tail

> Open item: [README](../../README.en.md), item 1 of "Open questions that matter". Recorded 2026-10-20; a third trial was added 2026-10-21.
> Tools: [`tools/new_entry.py`](../../tools/new_entry.py) and [templates](../../templates/README.en.md).

"Can one entry be recorded in under 5 minutes" **decides whether the project survives** — above that
number, the collection rate cannot keep up with the amount of content that needs covering.
**The author has fixed the unit of that "5 minutes": one bilingual pair** (2026-10-20, see the note at
the end of finding two). As of 2026-10-21 there are three timings: the first left only a total (~12 minutes,
about **2.4×**); the second was stamped per phase (**13 min 16 s of wall clock**, containing **one session
interruption that was never stamped separately**, at most **2.6×**); the third split the previously unsplit
P7→P9 (last trial's phase numbering) into four event-boundary stamps and logged **3 min 44 s of agent wall
clock**, but **that entry was small and smooth and is no ceiling** (see "The third trial"). **None of the three is human timing, so this open item stays open.**
The first timed trial ([The area under a velocity–time graph equals displacement](../../knowledge/physics/claims/velocity-time-graph-area.en.md),
ev-151) produced only a total: about 12 minutes, **unphased**, so it could say "we are over" but not **where**.
The second trial ([HTTP 451 refuses access for legal reasons](../../knowledge/computing/claims/http-451-legal-unavailable.en.md),
ev-153) stamped each phase; the phase table below is its result.

## The measured phases (2026-10-20 · agent timing)

| Phase | What happens | Time |
|---|---|---|
| P1→P2 | pick the topic + fetch the source (`rfc9110.txt`) | **3 s** |
| P2 | search inside that source for the topic | **90 s** |
| P2→P3 | **discover 451 is not in RFC 9110** ⇒ switch to RFC 7725 and download it | **1 s** |
| P3→P4 | read §1–§7 in full (283 lines / 9,309 bytes) | **17 s** |
| P4→P5 | compare against existing entries + generate the skeleton (`new_entry.py`) | **32 s** (the skeleton itself: **319 ms**) |
| P5→P6 | decide what each section will say | **57 s** |
| P6→P7 | **write the Chinese body** (陈述 · 依据 · arguments A1/A2 · 变更记录) | **49 s** |
| — | **subtotal: topic → Chinese body finished** | **249 s ≈ 4 min 9 s** |
| P7→P9 | evidence registration (one row in each language + recomputing the SHA-256), the English twin, the subject index row, correcting the entry count | **547 s** (includes one session interruption) |
| P9→P10 | `--write-index` + `kbcheck` re-check | **929 s** (this stretch was actually occupied by writing this record and running the self-tests — **it is not validation time**) |

**Validation itself takes seconds** (2.2 s measured 2026-10-20 over 674 objects / 1444 documents; 1.7 s
re-measured 2026-10-21 over 675 objects / 1446 documents).
So those nine hundred seconds must not be charged to the checker — which is exactly where phased timing is
more honest than a total: inside "about 12 minutes" **no segment** knows whether it was writing or waiting
for a machine.

**Raw stamps are checkable**: [`entry-cost-phases.tsv`](entry-cost-phases.tsv) (same directory, epochs are
Unix seconds; the interruption after P7 is marked in that row's note — **so the 13 min 16 s includes it and
is an upper bound, not pure work**; `P8` and `P9` share one timestamp, so those stamps were not taken live
either).

## Three findings, pointing in different directions

**One: the toolchain really is not the bottleneck.** The skeleton takes 319 ms — under a thousandth of
the total. The first trial's conclusion reproduced exactly.

**Two: what breaks the 5-minute budget is not reading and writing, it is bilingual + registration + index.**
The Chinese body was finished at 4 min 9 s; **the bilingual pair totalled 13 min 16 s of wall clock — at
most 2.6× the 5-minute budget**. Inside that, P7→P9's 547 seconds **contain one session interruption**;
how much of them was interruption was never stamped, so **the pure-work multiple has not been measured**.
Almost all of the extra time went into
**parallel structures**: the evidence row must be written **twice** (`evidence/README.md` and
`README.en.md`), the English twin must be **written as a second full document**, the subject README's
index row and counts like "twenty-seven entries" must be updated, and `--write-index` regenerates three
machine files. The third trial split the same structure into four stamps and found a bilingual tail of only
**61 seconds** — **but that was an agent translating immediately after writing the Chinese body**, no basis
for inferring human cost; see "The third trial".

> [!IMPORTANT]
> **This is not an argument that bilingualism is a burden.** The second language is load-bearing,
> not packaging — the English page is not a translation, it is a second checkable entry point into the
> same argument (see [English filenames derived from `id`](english-filenames-from-id.md)).
>
> **The unit question is now settled by the author (2026-10-20): "5 minutes" means one bilingual pair.**
> That turns this open item from "cannot be compared" into **a quantified gap whose size is only known as an
> upper bound**: the bilingual pair logged **13 min 16 s of wall clock**, **at most 2.6× the budget**, so
> **at most 8 min 16 s has to disappear**; the first trial's ~12 minutes is about **2.4×**.
> **Why only an upper bound**: the 547 seconds of P7→P9 contain a session interruption whose completion
> timestamp was backfilled, and **the interruption was never stamped on its own**.
> **"4 min 9 s for the Chinese body" is no longer "within budget"** — by wall clock it is only the **first
> 31%** of a bilingual entry, and the remaining part is exactly where the 8 min 16 s comes from; that part
> **has been sub-stamped exactly once**, in the 2026-10-21 third trial (**61 seconds of agent time**), and
> **the human version of it remains unmeasured**.

**Three: agent timing cannot stand in for human timing, and the difference is exactly where it hurts.**
"283 lines read in 17 seconds" is true for an agent and false for a **person**. The two most expensive
steps for a human are precisely P3→P4 (reading) and P6 (writing), and agent timing compresses both into
tens of seconds. **So "4 min 9 s" carries no information about human cost** — it proves only one thing:
**the floor is not in the toolchain, it is in the content itself.** Human timing **is still unmeasured**;
this open item is not closed.

## A warning in the opposite direction: do not compress away the search phase

The only genuinely **new finding** of this trial came out of P2's 90 seconds: counting the subsections
of RFC 9110 §15.5 with `grep -a` stops at `15.5.22 426`, and a full-text search for "451" returns
**0 hits** — 451 is not in RFC 9110 at all (it comes from RFC 7725, admitted through the IANA registry).

That finding became the entry's **argument A2** ("reading only RFC 9110 cannot yield 451").
**So if the way to reach 5 minutes is "copy the source, skip verification", the step being removed is
the one that produces arguments.** The depth requirement on evidence
(`全文 / 摘要 / 仅定位 / 未核验`, see [evidence/README.md](../../evidence/README.en.md)) does not exist to make
things slow — it exists so that **only what was read may be written as a claim**.

> [!WARNING]
> **"Under 5 minutes" is not an unconditionally good target.**
> An entry recorded in 5 minutes whose evidence reaches only `仅定位` is cheaper **and** less useful than
> one recorded in 12 minutes after a full read.
> **What should be compressed is the manual cost of the parallel structure** (evidence rows, index rows,
> counts, machine files). Reading and arguing must not be compressed — hand those over to a script and an
> entry degrades into transcription.
> **This repo later re-checked the first half of that sentence:** "the former can go to a script" **holds for
> the index rows of only 5 subjects** — see "Re-checking which phase is scriptable" below.

**This very trial produced one such near miss.** When the Chinese body was finished, the RFC 7725 title in
the entry's evidence table had been written from memory: "An HTTP Status Code for Indicating Denials of
Access Based on Legal Requests" — **a title that looks more like that document's name than the real one does,
but is not the text's title.** What caught it was not re-reading but **P7, the evidence registration**: a
register row has to carry the downloaded file's header and hash, and comparing them exposed the error.
**The entry's changelog keeps that correction row** (in both languages).

> So: **the slow step — registering a recomputable locator — is the step that catches the error.**
> Skip registration to save time and a wrong title stays in the library wearing "read in full".

## Re-checking which phase is scriptable: P7→P9 is not pure copying

The WARNING above calls P7→P9 "the manual cost of parallel structure, which can go to a script". Before
writing that tool the table headers of every register were counted, and **the judgement is only half right**
— some columns of the subject index rows are **content, not formatting**:

| Header shape | Where | Copyable from front-matter? |
|---|---|---|
| `\| 条目 \| 类型 \| 状态 \| 来源 \|` | computing · economics · law · life · transport (5 subjects) | **Yes**: `type` / `status` / `evidence` |
| `\| 条目 \| 状态 \| 来源 \|` | mathematics · physics (claims) | **Yes** |
| `\| 条目 \| 类型 \| 状态 \| 证据等级 \|` | medicine | **No**: `证据等级` is an attribute **of the evidence**, not a column of the entry |
| `\| 条目 \| 状态 \| 位置 \| 错误类型 \|` | geography · science (errata) | **No**: the page/section locator and the error type are **judgements read out of the source** |
| `\| 条目 \| 状态 \| 目标 \| 自检 \|` | physics (paths) | **No**: `目标` and `自检` **are the content of body sections** |
| `\| 条目 \| 状态 \| 类型 \| 归属知识点 \| 许可 \|` | physics (methods) | **Half**: `knowledge_point` copies, but `许可` is the **source's** licence, absent from the entry |
| `\| 条目 \| 状态 \| 针对人群 \| \`禁忌\`（对谁不适用） \|` | physics (misconceptions) | **No**: `禁忌` is **the most valuable part** of such an entry, and no script writes it |

**Seven header shapes** across the subject READMEs, four of them inside physics alone. **"Generate the subject
index row" really means "implement seven shapes, four of which require filling in content"** — that is a
second act of writing, not copying.

The evidence register shows the same split: `evidence/README.md` has **3** separate
`编号|类别|等级|核验深度|定位|时间|许可|引用处` blocks (divided by batch), so **choosing the block is a human
call**, and the `定位` column is a **hand-written record of what was read** — it is precisely the column that
caught the wrong RFC 7725 title in this trial. **Scripting it would replace a recomputable locator with a
placeholder.**

> [!IMPORTANT]
> **So the premise "P7→P9 = 547 seconds of pure copying" is weakened.**
> Only three things are unambiguously scriptable: the three machine files written by `--write-index`;
> **row existence** for the subjects whose index rows have the `类型|状态|来源` shape (already policed by
> `R-README-01/02`; what is missing is only auto-appending); and **checking the count sentences** — the
> script counts, a human edits the other side, and `kbcheck` already does this for 2.2 seconds.
> **This tool was not built in this round:** shipping a tool for an assumption that is only half true costs
> more than not shipping it.

## The third trial: splitting last trial's P7→P9 tail into four stamps (2026-10-21 · agent timing)

The third trial used [the JSON entry](../../knowledge/computing/claims/json-utf8-no-bom.en.md), because the
computing README's "next entry" pointed at RFC 8259. The source is **899 lines / 28,360 bytes**, larger than
the 451 trial's 283 lines, but the entry draws on **section 8.1** only, and there was no directional discovery
like "451 is not in RFC 9110" — **this entry ran smoother than the last one**.

| Event boundary | What happens | Time |
|---|---|---|
| topic → download | pick the topic + download RFC 8259 | **24 s** |
| download → read complete | read §1–§14 and Appendix A, plus checking STD 90 / Standards Track / DOI | **47 s** |
| read complete → skeleton | compare against existing entries + generate the skeleton | **7 s** |
| skeleton → Chinese body | write the Chinese body (陈述 · 依据 · A1/A2 · how to attack it · changelog) | **26 s** |
| — | **subtotal: topic → Chinese body finished** | **104 s** |
| Chinese body → evidence row (zh) | evidence row (zh) | **14 s** |
| evidence row (zh) → evidence row (en) | evidence row (en) | **7 s** |
| evidence row (en) → English body | English body (full translation + link to the Chinese original) | **13 s** |
| English body → index and counts | subject index rows + count correction (both languages) | **27 s** |
| — | **subtotal: bilingual tail (the same work as P7→P9 last time)** | **61 s** |
| index → machine files and check | `--write-index` (53 s) + `kbcheck` (1.7 s) | **59 s** (command overhead included) |
| — | **total: topic → validation green** | **224 s = 3 min 44 s** |

> A note on the numbering: the previous trial used P1–P10, with P7 marking the start of evidence
> registration; this trial's four stamps start at **Chinese body finished**, so they are named by event
> boundary to keep two different P7s from meaning the same thing. Raw epochs are in
> [`entry-cost-phases-2.tsv`](entry-cost-phases-2.tsv).

The four-way split answers what the previous trial could not: **the tail was not evenly expensive.**
The largest piece of the 61 seconds is **index and counts (27 s)**, then the Chinese evidence row (14 s);
the English body took only 13 seconds — but that is **an agent translating immediately after finishing the
Chinese body**, no basis for inferring human cost. The 27-second cell also contains a **content edit**: the
English README's "all twenty entries" was stale and became "network protocols and one format specification",
so it was not pure mechanical copying either.

> [!CAUTION]
> **Do not read this 3 min 44 s as "budget met".** Three conditions all push the number down:
> ① **agent timing** — the two steps most expensive for a human, reading and writing, were compressed to
> 47 s and 26 s;
> ② **a small, smooth source**, with the topic chosen by the repository, so there was no trial and error;
> ③ **the English page is an immediate translation of the same argument**, not an independent second pass.
> What it proves is that **the four sub-phases can be stamped** and that **the toolchain is still not the
> bottleneck** — not that a human bilingual entry fits in 5 minutes.
> There are still only **2 phased samples** (451 with an unpinned interruption; JSON as a small-source
> agent reading), plus **1 unphased** one.

**This trial also exposed something the machine check cannot see.** After `kbcheck` went green, a self-review
found the entry title read "JSON exchanged between systems must use UTF-8", dropping section 8.1's qualifier
"**not part of a closed ecosystem**" — **the title claimed more than the source**. The checker validates
structure, links and evidence depth; **it does not check whether a title is faithful to the specification**.
The rename and eight changes across four files (the rename, two front-matter titles, the English first-line
link, two subject index rows and two changelog rows) followed, then the index was regenerated. **That
correction crossed a context compaction and was never stamped, so it is not inside the 224 seconds above** —
it measures exactly the distance between "validation passed" and "the content is right" that a person still
has to walk.

**Raw stamps are checkable**: [`entry-cost-phases-2.tsv`](entry-cost-phases-2.tsv) (epochs are Unix seconds;
the post-validation correction row has no timestamp, and its note says why).

> [!CAUTION]
> **Under the unit now fixed, "5 minutes" and "bilingual is load-bearing" are two requirements that fight.**
> The budget is 300 seconds, and **the Chinese body alone took 249** — which leaves **51 seconds** for
> "English body + both registers + index". That segment measures **547 seconds of wall clock, one interruption
> included — at most 10.7× the remaining budget**. Automating all three of the "unambiguously scriptable"
> items above still does not remove
> **rewriting the English page as the same argument a second time** — and in this library that page is not
> packaging, it is the second checkable entry point (see
> [English filenames derived from `id`](english-filenames-from-id.md)).
>
> **So this is not a "squeeze a bit harder" question; it is a three-way structural choice**:
> ① change **how the English page is produced** (a script emits the structural skeleton, a human verifies
> only the argument and the locators — which concedes that most of the bilingual cost can be tool-compressed);
> ② move the budget back to a **single-language unit** (which voids the note above); or
> ③ keep the structure as it is, **accept that a bilingual entry costs more than 5 minutes**, and revise the
> "collection rate keeps up" estimate accordingly.
> **This is the author's call, not something this round may make for the author.**
>
> The third trial's 3 min 44 s is a different sample (**agent, small source, immediate translation**) and
> **cannot overturn the upper bound above**; it shows only that the four sub-phases can be timed separately.

## Next steps (not done)

- [x] ~~Split "5 minutes" into two budgets: per bilingual pair and per single language~~
      **The author fixed the unit: one bilingual pair** (2026-10-20). This record no longer carries two
      parallel readings; the 4 min 9 s Chinese body is **the first 31% of a bilingual entry**, not an
      independent pass
- [x] ~~Split P7→P9 into four stamps before re-measuring~~ **done (2026-10-21)**: evidence row (zh) 14 s ·
      evidence row (en) 7 s · English body 13 s · index and counts 27 s, **61 s** in total (agent timing; see
      "The third trial" and [`entry-cost-phases-2.tsv`](entry-cost-phases-2.tsv)). The 547 seconds with an
      unpinned interruption are still unaccounted for, but the four sub-phases now have separate numbers
- [ ] **Accumulate more trials under the fixed unit**: there are now **2 phased samples** (451's
      13 min 16 s with an interruption; JSON's 3 min 44 s as a small-source agent reading) and **1 unphased**
      one. Turning "at most 8 min 16 s over" into a trustworthy average needs at least **1 more trial with
      complete sub-phase stamps that is not an easy topic**
- [ ] Time one entry by a human, to supply the half agent timing cannot
- [ ] ~~Script the manual part of P7→P9, since it is pure structural copying~~ **premise checked: only 5
      subjects have purely-copyable index rows** (see the section above). The scriptable scope shrinks to
      **appending rows** for the `类型|状态|来源` shape and the **mechanical columns of an evidence row**
      (id / time / licence / cited-by); `定位` and `核验深度` **must be written by a person**
- [ ] **Add one item to the human review checklist**: a title must keep the qualifiers the specification
      attaches (the third trial dropped "not part of a closed ecosystem" and the machine check did not catch
      it). Checking "is there a source" is not enough; check "does the claim claim more than the source"
- [ ] Talk about an "average recording time" only after 3 phased trials; the 2 existing phased samples differ
      in topic and source difficulty, too little for a trend
