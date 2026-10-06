# Hormonaly Academy — Weekly Maintenance Audit 2026-10-06

**agent pre-review — no gate opened**

## Course: hormones-peptides-skin · v1.1.0
**Academy:** hormonaly (`factory/intake-hormonaly`)
**Foundry pin:** 69b4706c (PR stack #9/#11/#14/#17)
**Audit date:** 2026-10-06, 07:30 PT

## Summary

| Check | Result |
|---|---|
| Schema validation (pinned ref 69b4706c) | ✓ passes |
| Tic audit (narration rewrite surface) | 48 scripts, 0 contrastive, 0 meta, 0 colon, 0 dup |
| Anchor audit | 0 recycled anchors |
| Citation audit | 412 citations, 0 findings |
| Dead-screen audit | 0.0% dead, 0 warnings |
| Interaction audit | 63 across 7 modules, 0 warnings |
| Caption audit | No VTT tracks (none expected) |
| academy.yaml | 1 catalog entry, 0 failing |
| Design audit | 1 cosmetic: logo not shipped (report-only) |
| Skills layout | 15 checked, 0 failing |
| Agent config | Parses; hyperframes pin 0.8.3 |

**Overall: ✓ all gates pass** (report-only; --strict not applied)

---

## 1. Package Validation

Validator against the pinned foundry ref (69b4706c, which carries the interaction-kind schema from PR #11/#14/#17):

- `packageSchemaVersion`: 0.1.0
- 7 modules (m01–m07), 179 blocks, 63 interactions
- 0 cross-field errors (citation refs resolve, asset refs resolve, locale coverage intact)
- Interaction kinds in use: quickfire (7), sequence (7), branching (7), classify (14), inspect (7), hotspots (7), scenario (7), chips (7) — all recognised

## 2. Citation & Link Coverage

- **412 citations** in the provenance registry
- **410 have URLs** (web or document links)
- **2 without URLs**: `hannah-shmouni-2026-are` (Hormonaly Aesthetic Reference Encyclopedia) and `hannah-shmouni-2026-ppg-aug` (Peptide Pocket Guide) — internal clinical references, expected
- **Claim support** files exist for versions 0.2.0-m04, 0.3.0, 1.0.0, 1.0.1, 1.1.0 (plus rc variants)
- All 412 citations verified by `perceptor check` citation audit — 0 findings

**Note:** Citation URL liveness was not checked (network-dependent; use `perceptor claims check --sources-only` after the intake stage).

## 3. Locale Completeness

- Single locale: **en** (English, base, ltr)
- 1 locale edition registered — expected for this stage
- No additional locales required yet

## 4. Asset Existence (Manifests)

### Teaching Visuals (stills)
- **48 stills** in `images-manifest.json` (gemini-3.1-flash-image, 1K, 16:9, house frame)
- All at `approval_status: "draft — pending human media preview"`
- Generator cost: $5.09 (76 calls)
- Agent QA performed on all (no human approval yet)

### Opening Films
- **7 module openers** in `films-manifest.json`
- Models: HeyGen Avatar V, Gemini 3.8 TTS, GPT Image 2.5, Veo 3.1, Lyria 3.5, HyperFrames
- All draft media — human media preview not yet completed
- Disclosure label: "Presented by a digital avatar (AI-generated presenter and voice)."
- Trailers: 1 (trailer.mp4) — visual QA completed (0 blocking, 0 warn)

### Binaries in repo
- No MP4/JPG/PNG/VTT files in git (expected — served from GCS bucket after `publish-media.sh`)
- `public/assets/hormones-peptides-skin/` directory exists but contains no files locally
- Outstanding: m04-opener-r3.mp4 and m05-opener-r3.mp4 have QA reports but no MP4s in repo

## 5. Catalog & Accreditation Consistency

### Governance
- **Status:** all modules at `draft` (no published content)
- **Required gates:** medical_review, brand_approval, localization_review, gcls_accreditation, publish
- **Accreditation status:** `not_submitted` (body: GCLS)
- **Accreditation note:** "Designed toward future CME accreditation... No CME/CE credit is claimed until that approval exists"

### Approvals
| Gate | Approver | Date | Scope |
|---|---|---|---|
| medical_review | Fady Hannah-Shmouni, MD FRCPC | 2026-09-24 | All 7 modules |
| medical_review (post-approval) | Fady Hannah-Shmouni (Omar relay) | 2026-09-25/26 | Practice additions, UK/EU/AE/PT/BR jurisdiction notes |
| Editorial changes | Omar Saleem (product owner) | 2026-09-25/26 | Module titles, summaries, field edits |

### Accreditation Dossiers Exist
- 0.3.0-full-draft, 1.0.0, 1.0.1, 1.1.0 — each with checklist, dossier.json, review-brief.md and review-brief.json
- Dossier 1.1.0 matches the current package version

### Academy catalog
- 1 entry in academy.yaml catalog (hormones-peptides-skin)
- No catalog status inconsistencies

## 6. Library & Tutor Corpus

- **Library section:** empty (no sourceInsights, no guidedReading, no curated resources)
- **Tutor corpus:** present but not audited for completeness (full tutor blueprint not yet triggered)
- Expected at intake stage; curated resources will be populated post-launch

## 7. Outstanding Items (carried from prior sweeps)

1. **Logo file** — `hormonaly-logo.png` declared but not shipped (runtime falls back to typographic wordmark). Customer logo pending.
2. **m04-opener-r3.mp4** and **m05-opener-r3.mp4** — QA reports exist but MP4s not pushed to repo. If these are intended release versions, push the renders.
3. **Foundry staleness** — The local foundry checkout (main, 5efb7e1) is behind the pinned ref (69b4706c) by ~70 commits from the #9/#11/#14/#17 PR stack. The sweep works around this by using the pinned worktree; the foundry should merge the PR stack to main.
4. **Interaction schema gap** — The schema on main (5efb7e1) has no interaction kind definitions, causing false validation failures. The PR stack (#9/#11/#14/#17) at 69b4706c resolves this.

---

*Report generated by Daedalus — weekly maintenance audit, 2026-10-06.*
*agent pre-review — no gate opened*