# Gap dashboard: four mouths, one brain

> 中文 → [gap-dashboard.md](gap-dashboard.md)

> Decided **2026-10-30**. The page itself is [`docs/GAPS.en.md`](../GAPS.en.md); this records **why**.

## What it looked like

“What is this library still missing?” had four exits, each computing its own answer:

| Exit | How it used to compute |
|---|---|
| `tools/make_tasks.py` | scanned READMEs itself, counted `待审` itself, judged “missing method” itself |
| `docs/GAPS.md` | **did not exist** — the whole picture meant reading 500 lines of `make_tasks` output |
| MCP | **no such tool** — an agent had to read `index.json` whole and infer |
| `kbcheck` hints | `R-GRAPH-07` printed 17 “single-step coverage” lines to the terminal |

The last row is the clearest: **that fact lived only until the terminal closed.** Close the window,
and “an outcome is taught exactly once” in 17 paths became unknown again.

Worse were the first two: if `make_tasks` and (the later) page each kept their own filters,
“the page says 37, the task list says 35” was only a matter of time. **Both would be “right” —
just not about the same question** — and no check would notice, because no single place knew both answers.

## One criterion: what counts as a gap

**Only what a machine can count.** What it cannot — whether an argument holds, whether a prerequisite
is really required, whether a method works in a real classroom, whether two sources are independent —
stays out and gets its own table (“the half machines don't judge” in `docs/GAPS.md`).

The reason is not modesty; it is to **keep this table from looking more authoritative than it is**.
Mixing “human judgement” into “machine count” invites readers to treat every row as equally certain.

## What it became

| Layer | What it is |
|---|---|
| Computation | `compute()` in [`tools/gaps.py`](../../tools/gaps.py) — the **only** place gaps are counted |
| View 1 | `tools/make_tasks.py` (human text + `--json` + `--gh` to open issues) |
| View 2 | generated blocks in `docs/GAPS.md` / `docs/GAPS.en.md` (written by `--write-index`) |
| View 3 | MCP `scholia_gaps` (counts by default; add `group=` to list items) |
| View 4 | `kbcheck` hands the same `compute()` result to the page renderer |

Nine groups, each stating *why it counts as a gap* and *what to do next*:

| key | Count (2026-10-30) | Criterion |
|---|---|---|
| `review` | **570** | `待审` + argument written + all evidence read at `摘要`/`全文` |
| `review-blocked` | **3** | `待审` but evidence only at `仅定位`/`未核验`, or no argument / no evidence yet |
| `translate` | 0 | no `path_en` |
| `methods` | **37** | a concept with no `教法` attached |
| `external` | **2** | the same `标识` appears in ≥2 objects |
| `path-thin` | **17** | an outcome covered by exactly one step (`R-GRAPH-07`) |
| `path-shallow` | 0 | covering entries' evidence tops out at `仅定位`/`未核验` |
| `todo` | **110** | the author wrote `**待补**:` in the body |
| `coverage` | **2** | against the PEP catalogue, a whole chapter has no concept |

> **Do not add the counts up**: one object can sit in several rows (an unreviewed concept can both lack
> a method and carry a `待补` marker). That sentence is bold on the page because “add the nine rows”
> sounds like a number one could finish, and it is not.

## Two things that went into the index on the way

`index.json` `schema_version` went from 4 to 5 — additive only:

1. **`覆盖度`** (paths only): `已覆盖` / `声明` / `单环节成果` / `证据薄成果`.
   Before this, those three numbers existed only in `kbcheck`'s terminal output. `gaps.compute()` also
   aggregates them into `统计.路径成果` (17 paths · 73 outcomes · 67 taught once), so the "92%" sentence
   in the README now has a generated artefact to check against.
2. **`title_en`**: English pages and English search must be able to **name an entry in English**,
   instead of handing an English reader a Chinese title. The field is absent when there is no
   translation — **better absent than invented**.

## One error fixed along the way

`llms.txt` used to hand-write "`index.json` ≈14k / `citations.json` ≈18k / `evidence.json` ≈9k tokens".
After the library reached 746 objects, the real values were **96k / 158k / 38k** — **the section teaching
people to save tokens under-reported the cost by an order of magnitude**. Worse, it then advised
"read `index.json` whole at most once per session": a 96k "once" is not thrift, it is luxury.

That table is now a generated block (`render_machine_files_block`) recomputed from content, and the
advice became "do not read any of the three whole; fetch one entry with `scholia_search`".
This is the repo's own rule caught in the act: **never hard-code a number that can drift** — it will
drift while nobody is looking.

## Costs (not glossed over)

1. **`compute()` reads files, not just the index.** It scans `knowledge_point` lines in `methods/*.md`,
   `**待补**` markers in bodies, and 🔴 rows on the coverage page. So it is slower than pure JSON
   arithmetic (≈0.3 s) and more coupled to directory layout — rename a folder and counts can change
   silently. `selftest` can only prove **the page matches the computation**, not that **the criterion
   is still right**; that still needs a human.
2. **Each group shows only the first 10 items.** A 570-row page goes unread, but “only 10” invites the
   reader to think there are only 10. Every truncated group therefore says “and N more” and points at
   the full JSON.
3. **570 is not a “570 × 3 minutes” estimate.** The three minutes assume a reviewer who knows the
   subject; everyone else must read the evidence first. The number measures **queue length**, not
   **remaining work**.

## What was not done

- **A gap is not an error.** It does not affect `kbcheck`'s exit code. Making gaps fail the build
  would push people to write content just to turn CI green — exactly backwards.
- **No history.** Without snapshots there is no “how much did we close this month”. A trend needs
  daily statistics stored somewhere; that is a separate job.
- **Ordering is by downstream dependents only.** It answers “how many other entries does editing this
  affect”, not “which entry matters more”. Importance still needs a human.
