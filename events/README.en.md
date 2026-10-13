# Events

> **中文: [README.md](README.md)**

> [!IMPORTANT]
> **This directory holds "events" — a second kind of record, **parallel to** the knowledge
> objects in [`knowledge/`](../knowledge/).**
>
> A proposition answers "**what is true**" (it has a truth value, is attacked and defended,
> and converges to `已确证`/`已推翻`/`失据`); an event answers "**what happened**"
> (officially published facts recorded in time order, **with evidence only, no attackable claim**).
>
> So events live **top-level**, **do not enter `index.json`'s `objects`**, are not counted in the
> object total, and have **no `## 论证` section and no `先修`/`支持`/`攻击` edges**.
> Rules: [FORMAT.md §4 "事件"](../FORMAT.md).

## Index

| Event | Status | Evidence | Last updated |
|---|---|---|---|
| [伊尔库茨克反瘟疫研究所员工死亡事件（2026 年 9–10 月）](伊尔库茨克反瘟疫研究所事件.en.md) | 持续更新 | `ev-064` `ev-065` `ev-066` `ev-067` `ev-068` | 2026-10-13 |

**1 event.**

## Status

An event's status answers one question only: **is this record still being updated?**

| Status | Meaning |
|---|---|
| **持续更新** (ongoing) | the event is still developing; this entry **adds evidence rows** as it evolves |
| **已封存** (archived) | the event has stopped developing; no more additions |

> [!NOTE]
> Events have **no** `已确证` / `已推翻` / `失据` / `已失效` — those are proposition statuses.
> An event is not established by argument and does not "expire". **If it happened, it happened.**

## Maintenance protocol (on each new development)

1. **Add a row** to the timeline in `陈述`
2. If it is a new source, add a row to the `依据` table and to [`evidence/README.md`](../evidence/README.md)
3. Add a `变更记录` row
4. Set `updated:` to today; keep `status` at `持续更新`
5. Run `python tools/kbcheck.py --write-index` (updates `index.json`)
6. Open a PR
