# Monthly source health — hormonaly / hormones-peptides-skin v1.1.0

**Date:** 2026-11-12 · **Runner:** Daedalus (cron, fleet job `course:hormonaly/hormones-peptides-skin` claims)
**Command:** `node ~/DrVibe/perceptor-foundry/bin/perceptor.mjs claims check packages/hormones-peptides-skin.json --sources-only --academy .` (from `~/DrVibe/academy-hormonaly-regenerative-endocrinology`, branch `factory/intake-hormonaly`)
**Scope:** sources-only provenance sweep — 774 cited units, 412 sources, edition en. No model pass (0 assertions, by design for `--sources-only`).

## Verdict: WARN — 1 source moved (lock-amendment request drafted); everything else unchanged or transient

## Result

- sources: 47 unavailable · 25 landing page · 42 pdf (full document) · 106 web page · 67 full text · 125 abstract only
- vs October: unavailable 50 → 47; landing 22 → 25 (three EDDE/register pages flipped to "landing" as their JS rendering varied — structural, not content changes).

## The one real change

**`gphc-pharmacist-prescribers-2025` — MOVED (HTTP 404 on the locked URL).**
Locked URL `https://assets.pharmacyregulation.org/files/2025-04/in-practice-guidance-for-pharmacist-prescribers-updated-april-2025.pdf?VersionId=gDMMsBlPEOdD2uTfSyjVzhutXbJ5RCCg` now returns 404. GPhC re-published the same document at
`https://assets.pharmacyregulation.org/files/2026-10/in-practice-guidance-for-pharmacist-prescribers-updated-april-2025a.pdf` (HTTP 200, 34-page PDF, cover confirms "In practice: Guidance for pharmacist prescribers, Updated April 2025" — same document, new path). The claim-support runner kept the cached copy, so cited units (m07: `c-m07-24`, `m7-p21`; plus the course source-lock list) still hold on cached bytes.
→ Drafted `research/lock-amendment-request-m07-2026-11-12.md` (request only, not applied).

## Not changes — verified transient/structural

- **`fda-drugsatfda-propecia-020788`** — refetch 404 resolved to `accessdata.fda.gov/apology_objects/abuse-detection-apology.html`: FDA bot-wall, not a dead application. Application 020788 (Propecia/finasteride) still exists; label PDFs (`drugsatfda_docs/label/2021/020788s028lbl.pdf`) are reachable. Pre-existing citation-hygiene note stands: the locked URL is the Drugs@FDA portal page — a candidate future amendment to cite the specific label PDF, not needed this month.
- **Refetch failures with cached copy kept (no content change shown):** 8 EMA pages (HTTP 429 rate-limit), `uk-hmr-2012-reg-46` (502), `lilly-v-kennedy-7th-cir` (405), 2 doh.gov.ae PDFs (TLS leaf-verification), 6 AES-encrypted regulator PDFs (AE/PT; pypdf `cryptography` dependency missing again — see environment note), `gphc` handled above.
- **October's four transient/unavailable sources** (tga-2026-melanotan-ii-safety-advisory, usc-21-333e-hgh, ae-ede-reg-centrum-shn, br-anvisa-register-opendata): all resolved or unchanged this month; none requires action.

## Environment finding (recurrence)

The October environment note recurred: this run again lacked `cryptography` for AES regulator PDFs (`pypdf.errors.DependencyError`), producing 6 refetch-failure rows that are artifacts, not source changes. The `/tmp/pdfpy` bundle from October was ephemeral. Recommendation stands: bake `pypdf` + `cryptography` into the VM's default python3 (or make `claim-support.mjs` fall back to a venv). Logged in `~/perceptor-runs/autopilot/FINDINGS.md`.

## Artifacts

- Refreshed provenance report committed on `factory/intake-hormonaly`:
  `course-production/claim-support/hormonaly.hormones-peptides-skin-1.1.0.md` (+ `.json`), package sha256 `6419297d6d01`.
- Lock-amendment request (draft): `research/lock-amendment-request-m07-2026-11-12.md`.
- Raw run log: `/tmp/claims-check-hps.log` (this host, ephemeral).
