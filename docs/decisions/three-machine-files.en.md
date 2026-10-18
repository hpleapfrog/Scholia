# Splitting the machine entry into three files: navigation / citations / evidence

> **中文 → [three-machine-files.md](three-machine-files.md)**

> Decided **2026-10-18**. The rule itself lives in `llms.txt` ("Machine entry point"); this page
> records **why**.

## What it was

One `index.json` held everything: `objects` (each with `来源`, `适用`, `条件`, `论证`),
the evidence registry (75 rows), statistics, `known_limits`. **179 KB ≈ 48k tokens.**

And `llms.txt` said: **"the only file you need to parse is index.json."**

So the default usage became: **to ask "do you have this?", you first swallow every locator and
every piece of evidence.**

## Three facts about the sizes

| Fact | Number |
|---|---|
| The resolved `来源` field alone, across all objects | **19.7%** |
| The evidence registry alone | **23%** |
| `scholia_search` used to return 20 hits, each with source/limits | ≈ **6k tokens per search** — **more than reading one entry** |

The last one is the giveaway: **when the search interface is heavier than the thing searched,
it is not a search interface.**

## What it is now

| File | Holds | When to read | Size |
|---|---|---|---|
| `index.json` | navigation + **may it be cited** | always first | ≈14k |
| `citations.json` | citation kit: `来源` / `证据` / limits / disclaimer position | **by id, one at a time** (≈160 tokens) | ≈18k |
| `evidence.json` | evidence registry (grade · verification depth · locator · licence · voided) | when verifying provenance | ≈9k |

Two MCP changes came with it: `scholia_search` returns navigation fields only and defaults to 5
hits (≈150 tokens), and a new `scholia_cite` fetches one citation kit by id.

## The cost (stated plainly)

1. **Total bytes grew**: 179 KB → 246 KB, because `citations.json` repeats a little metadata and
   each file carries its own `$comment`. **That is deliberate**: tokens are saved by *not reading*,
   not by a smaller sum.
2. **One more file to know**: citing takes two steps (index, then citations). For a call that
   never cites, this is pure gain; for a batch job that cites everything, it is one extra lookup.
3. **Compact JSON (no indentation)**: all three are generated and never hand-edited; indentation
   would add 25% to `index.json`. The price is unreadable diffs — nobody reads indexes by diff,
   that is what `START.md` is for.

## Not done

- **`evidence/README.md` and `evidence.json` are still the same facts in two places** (the former
  hand-written, the latter generated). Merging them means making `evidence/README.md` generated —
  a separate job.
- **`index.json` can still be read whole** (14k). For "enumerate the library" that cost is
  unavoidable; for "look up one entry" use `scholia_search` (≈150 tokens).
