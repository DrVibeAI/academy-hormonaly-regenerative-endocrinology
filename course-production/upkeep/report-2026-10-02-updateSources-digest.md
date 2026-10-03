# UpdateSources digest — watchlist: hormonaly/hormones-peptides-skin
**Date:** 2026-10-02
**Agent:** daedalus (operator cron — perceptor-operator)
**Status:** FAIL — target package does not exist

## Task

Digest `packages/hormones-peptides-skin.json` jurisdiction updateSources and
flag clinical-update or source-lock-amendment candidates.

## Result

**File `packages/hormones-peptides-skin.json` does not exist.**

The academy is in **Stage 00 (Intake)** — no packages have been authored.
The `packages/` directory contains only `.gitkeep`. The sole package reference
in `academy.yaml` is `packages/aesthetic-regenerative-endocrinology.json`
(marked `status: draft`; "package not yet authored — Stage 20+").

## Discrepancy

| Field | Value |
|---|---|
| Task target | `packages/hormones-peptides-skin.json` |
| academy.yaml reference | `packages/aesthetic-regenerative-endocrinology.json` |
| Actual file | Does not exist (NEITHER path) |
| Academy stage | 00 (Intake) — pre-authoring |

The cron job's target package name (`hormones-peptides-skin`) does not match
the course name in `academy.yaml` (`aesthetic-regenerative-endocrinology`).
Neither file exists on disk.

## Source material on hand

- `corpus/hormonaly-pocket-guide-2026.pdf` (2.6 MB)
- `corpus/hormonaly-pocket-guide-2026.md` (3835 lines, 183 KB, extracted)
- 20 chapters with GRADE A–D evidence ratings, 225 inline citations
- No source-lock, claims-check, or jurisdiction data extracted yet

## Recommendation

1. Correct the cron job's package path to match the actual package name when
   it is authored.
2. The academy needs to advance through Stage 05 (design) → Stage 10 (source
   lock) → Stage 20+ (authoring) before any package exists to digest.

## Intelligence

- Repo is on `factory/intake-hormonaly` (clean), 2 ahead / 54 behind origin
- Prior sweeps (2026-10-01, 2026-10-02) also SKIPped with no-ops