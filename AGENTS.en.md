# AGENTS.md — entry point for AI agents

> 中文 → [**AGENTS.md**](AGENTS.md)

> This file is for **AI agents working inside this repository** (coding agents, LLM agents).
> Human contributors → [CONTRIBUTING.en.md](CONTRIBUTING.en.md); readers → [START.en.md](START.en.md).

---

## 1. What this is

A **source-traceable** cross-disciplinary knowledge base. Every entry carries its **source**, its
**status** and the **rebuttals** against it; "what is true" is **computed by rules** from evidence
grade plus rebuttal structure — never by vote.

## 2. How to consume it

| How | Entry |
|---|---|
| Three machine-readable files | [index.json](index.json) (navigation) · [citations.json](citations.json) (citation kit by id) · [evidence.json](evidence.json) (evidence registry) — **all generated, never hand-edit** |
| Reading contract for AI (status, may-it-be-cited, how to save tokens) | [llms.txt](llms.txt) |
| **MCP server** (wire it into an agent) | [`tools/scholia_mcp.py`](tools/scholia_mcp.py) |

**Wire it as an MCP server:**

```json
{
  "mcpServers": {
    "scholia": { "command": "python", "args": ["tools/scholia_mcp.py"] }
  }
}
```

Read-only tools: `scholia_stats` · `scholia_search` · `scholia_list` · `scholia_get_object`
(`part="content"` returns only the reader half; `full` adds the argument) · `scholia_cite` ·
`scholia_get_evidence` · `scholia_rules`.

> **When citing anything**: give the `status` and the `来源` together; **never cite entries whose
> `可作事实引用` is false** (失据 / 已推翻 / 已失效); medical entries must be restated with their
> `适用` / `条件`. Details in [llms.txt](llms.txt).

## 3. If you edit here

**Run the checks after editing:**

```bash
python tools/kbcheck.py                 # must pass
python tools/kbcheck.py --write-index   # after content changes: regenerate the three machine files and doc blocks
python tools/verify_rules.py            # after rule changes: every rule needs a failing injected sample
```

Hard rules:

1. **`index.json` / `citations.json` / `evidence.json` and the `<!-- kbcheck:begin --> … <!-- kbcheck:end -->`
   blocks are generated** — hand-editing fails the check. Only `--write-index` may write them.
   **Each file does one job; never read them whole**: `index.json` for navigation, `citations.json` by id,
   `evidence.json` for provenance.
2. **One concept = one `.md`**; 11 required front-matter fields for **knowledge objects** (an `事件`
   lives top-level in `events/`, uses a different set of 9 fields, has **no argument and no edges** —
   see [FORMAT.en.md](FORMAT.en.md) §4). Body first line, status, level markers, medical disclaimer:
   see [FORMAT.en.md](FORMAT.en.md).
   **An English edition's filename is derived from the `id`** (`frame-of-reference.en.md`) — **not**
   "Chinese name + `.en.md`", which leaves English pages carrying Chinese filenames (`R-BILING-01`, §0).
3. **Changing a rule means changing the check**: the rule list lives in [`docs/RULES.en.md`](docs/RULES.en.md)
   (generated from the `RULES` entries) and in the check functions of [`tools/kbcheck.py`](tools/kbcheck.py).
   A new rule needs a **failing injected sample** in [`tools/verify_rules.py`](tools/verify_rules.py)
   (see CONTRIBUTING, "new-rule threshold").
4. **Never hard-code drifting numbers** (all statistics come from the script).
5. **Never upload textbook text or scanned pages** — locators, short quotations and original summaries only.
6. **AI may attack; AI may never be the reviewer for `已确证`** ([FORMAT.en.md](FORMAT.en.md) §6).
7. **Start new entries from the scaffold**: `python tools/new_entry.py --type <type> --subject <subject> --slug <slug> --title "<title>"`
   — skeletons come from [`templates/`](templates/README.en.md). **Structure to the script, content to you.**
   Run `kbcheck` immediately afterwards; its errors are your to-do list.

## 4. Language

**Documentation is bilingual**: `<name>.md` Chinese, `<name>.en.md` English (this file included).
Content is Chinese first, then English; quotations keep the original text with a Chinese gloss.
