# Events

> **中文: [README.md](README.md)**

> [!IMPORTANT]
> **This directory holds "events" — a second kind of record, **parallel to** the knowledge
> objects in [`knowledge/`](../knowledge).**
>
> A proposition answers "**what is true**" (it has a truth value, is attacked and defended,
> and converges to `已确证`/`已推翻`/`失据`); an event answers "**what happened**"
> (officially published facts recorded in time order, **with evidence only, no attackable claim**).
>
> So events live **top-level**, **do not enter `index.json`'s `objects`**, are not counted in the
> object total, and have **no `## 论证` section and no `先修`/`支持`/`攻击` edges**.
> Rules: [FORMAT.md §4 "事件"](../FORMAT.en.md).

## Index

| Event | Status | Evidence | Last updated |
|---|---|---|---|
| [伊尔库茨克反瘟疫研究所员工死亡事件（2026 年 9–10 月）](irkutsk-anti-plague-institute-2026.en.md) | 持续更新 | `ev-064` `ev-065` `ev-066` `ev-067` `ev-068` | 2026-10-18 |
| [Timeline and origins of the COVID-19 pandemic (2019–2025)](covid19-timeline-and-origins.en.md) | 持续更新 | `ev-090` `ev-091` `ev-092` `ev-093` `ev-094` `ev-095` `ev-096` `ev-097` `ev-098` `ev-099` `ev-100` `ev-101` `ev-102` `ev-103` `ev-104` `ev-105` `ev-106` `ev-107` `ev-108` `ev-109` `ev-110` `ev-111` `ev-112` `ev-113` `ev-114` `ev-115` `ev-116` `ev-117` `ev-118` `ev-119` `ev-120` `ev-121` `ev-122` `ev-123` `ev-124` `ev-125` `ev-126` `ev-127` `ev-128` `ev-129` `ev-130` `ev-131` `ev-132` `ev-133` `ev-134` | 2026-10-19 |

**2 events.**

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
2. If it is a new source, add a row to the `依据` table and to [`evidence/README.md`](../evidence/README.en.md)
3. Add a `变更记录` row
4. Set `updated:` to today; keep `status` at `持续更新`
5. Run `python tools/kbcheck.py --write-index` (updates `index.json`)
6. Open a PR
