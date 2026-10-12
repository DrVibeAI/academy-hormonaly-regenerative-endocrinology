# Monthly source health — hormonaly / hormones-peptides-skin v1.1.0

**Date:** 2026-10-12 · **Runner:** Daedalus (cron, fleet job `course:hormonaly/hormones-peptides-skin` claims)
**Command:** `node ~/DrVibe/perceptor-foundry/bin/perceptor.mjs claims check packages/hormones-peptides-skin.json --sources-only --academy .` (from `~/DrVibe/academy-hormonaly-regenerative-endocrinology`, branch `factory/intake-hormonaly`)
**Scope:** sources-only provenance sweep — 774 cited units, 412 sources, edition en. No model pass (0 assertions, by design for `--sources-only`).

## Verdict: OK — no source died or moved; no lock amendment required

## Result

| Basis | Count |
|---|---|
| abstract | 128 |
| webpage | 106 |
| fulltext | 67 |
| pdf (full document) | 39 |
| landing | 22 |
| none (unavailable) | 50 |

0 sources disappeared, 0 new sources, 0 URLs redirected to different content. No claim depends on an unavailable source, so **no lock-amendment request is drafted**.

## The 4 sources that read "none" this month but were readable last month — all transient/structural, verified

1. **tga-2026-melanotan-ii-safety-advisory** — ETIMEDOUT during the run. Page manually re-fetched afterwards: live, safety advisory published 17 Aug 2026. Transient.
2. **usc-21-333e-hgh** — uscode.house.gov was "under maintenance" during the run. Statute text is not altered; same text also reachable via govinfo/Cornell. Transient; consider re-pointing the lock to the govinfo permalink if it recurs.
3. **ae-ede-reg-centrum-shn** — Dubai EDDE portal is a JavaScript app; the fetcher got no readable text this month (was `landing` last month). Portal-side rendering flake, not a content change.
4. **br-anvisa-register-opendata** — dados.anvisa.gov.br is a 44+ MB dataset; the tool refuses it by design ("cite the specific record or page"). Structural: a candidate lock amendment to cite a specific ANVISA record page, but no claim currently rests on this URL's bulk data.

The remaining 46 `none` sources were `none` at HEAD too (403-walled ANVISA bulario, UAE legislation portal, JS-only EDDE register pages, PubMed records with no abstract) — pre-existing, unchanged, and none carries a factual claim.

## Environment finding (not a source problem)

First run of the month reported ~35 sources as newly "unavailable" because `python3` on this VM has no `pypdf` (and no `cryptography` for AES-encrypted regulator PDFs). That produced a false "35 sources moved" signal. Fixed for this run by assembling a pypdf+cryptography+cffi bundle at `/tmp/pdfpy` from the uv cache and running with `PYTHONPATH=/tmp/pdfpy`. **Recommendation:** bake pypdf + cryptography into the operator VM's default python3 (or have `claim-support.mjs` fall back to a venv) — until then, monthly runs must set PYTHONPATH or they will under-read every regulator PDF. Logged in `~/perceptor-runs/autopilot/FINDINGS.md`.

## Artifacts

- Refreshed provenance report committed on `factory/intake-hormonaly`:
  `course-production/claim-support/hormonaly.hormones-peptides-skin-1.1.0.md` (+ `.json`), package sha256 `6419297d…a4fa`.
- Raw run log: `/tmp/claims-check-hps4.json` (this host, ephemeral).
