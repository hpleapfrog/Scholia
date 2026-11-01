# Interface selftest: the half `kbcheck` cannot see

> 中文 → [interface-selftest.md](interface-selftest.md)

> Decided **2026-10-30**. The command is `python tools/selftest.py`; this records **why** it exists.

## What it looked like

CI ran two commands:

| Command | What it checks |
|---|---|
| `tools/kbcheck.py` | **content**: front-matter, links, evidence, graph relations, generated-file consistency |
| `tools/verify_rules.py` | **rules**: every mechanical rule has a failing injected sample |

Both are useful, and both **never run** three other interfaces:

| Interface | Who uses it | What breaks |
|---|---|---|
| `tools/scholia_mcp.py` | anyone mounting the library on an agent | handshake succeeds, the first tool call dies |
| `tools/make_tasks.py --json` | anyone wiring it into a script or opening issues | the JSON does not parse |
| `tools/new_entry.py` | a newcomer adding their first entry | the scaffold misses fields; the first `kbcheck` is a wall of red |

> **Added 2026-11-01**: `tools/review_packet.py` (review material on one page) came later — a fourth
> interface; `selftest` now has nine checks. The section above keeps its original three-interface scope.

## Why `kbcheck` cannot see it

Because it checks **content on disk**, not **behaviour when called**.

The sharpest spot: the MCP server's `tools/call` **swallows exceptions** —

```python
except Exception as e:
    text = f"error: {e}"
return {"content": [{"type": "text", "text": text}], "isError": False}
```

That is deliberate (one broken tool should not kill the session), but it means **a broken tool looks
like a successful call to a naive client**. `kbcheck` never reaches that code, so CI can be fully green
while an agent receives a single line of `error: ...`.

## What it became

`tools/selftest.py`: **nine checks that really spawn processes, instead of importing functions**.

| Check | What it proves |
|---|---|
| `generated_files` | the three generated files agree: paths exist, `title_en` and `path_en` come and go together, cited ids are not dangling |
| `gaps_determinism` | `compute()` returns the same thing twice; each group's count equals its item list; `review` + `review-blocked` is exactly all `待审` |
| `gaps_pages_in_sync` | every number in `docs/GAPS.md` / `.en.md` matches `compute()`, and every id on the page exists |
| `make_tasks_json` | `--json` parses, has the expected top-level keys, matches `compute()`; human mode lists every group |
| `new_entry_scaffold` | in a **temp directory**, the scaffold has all 11 fields and required sections; bad slug / missing subject / overwrite are refused |
| `mcp_handshake_and_readonly` | `initialize` / `ping` / `tools/list` work; all 9 tools are present; the three machine files **hash unchanged** afterwards |
| `mcp_tools_callable` | all 9 tools return usable payloads; `content` excludes `## 论证`; an unknown tool reports an error instead of silence |
| `mcp_print_config` | the JSON from `--print-config` parses and points at the server |
| `review_packet` | `tools/review_packet.py` builds material for a real pending entry: id, sources, evidence, the three questions and the `M-07` warning; `--out` writes exactly one file |

`mcp_tools_callable` is **deliberately rigid**: the tool-name set must be **exactly** those nine.
Adding or removing one fails the test — so whoever adds a tool must update the selftest and the docs,
instead of letting the test quietly adapt to a new reality.
The `review_packet` check is equally careful about **not answering** the three questions:
it can assert that the material is present, not that the review passed.

## One design choice: spawn, don't import

Importing a function only proves “the module loads”. What actually breaks is:

- the stdio handshake (newline-delimited JSON-RPC; one missing `flush` and it hangs);
- `--json` output polluted by a stray `print` (a human-readable hint on stdout makes the JSON unparseable);
- `new_entry` depending on the current directory (testing it inside the repo **writes into the repo**,
  so it must run in a temp directory).

So the selftest starts a real interpreter with `subprocess`, runs `new_entry` inside
`tempfile.mkdtemp()`, and talks to MCP over a pipe. The cost is speed — **about 3 s on this
machine** (machine-dependent; not a benchmark), still faster than a full `verify_rules` run.

## Costs (not glossed over)

1. **It knows the shape of the interfaces.** Tool names, top-level JSON keys, 11 required fields —
   each appears once in the test. That duplication is intentional: when the interface changes,
   the test should go red.
2. **It does not judge whether content is right.** Whether an argument holds or evidence is reliable
   stays with `kbcheck` and human review.
3. **It only covers the “call it once” path.** Concurrent calls, huge `limit` values and hostile input
   are out of scope.

## What was not done

- **No full MCP conformance suite.** Only `initialize` / `ping` / `tools/list` / `tools/call`;
  no notifications, cancellation or pagination.
- **CI runs on Ubuntu only.** Locally verified on Windows (path separators and console encoding both
  bit us), but there is no Windows runner.
- **It does not test whether tool descriptions are accurate.** Descriptions are for humans; a machine
  can only test that they exist.
