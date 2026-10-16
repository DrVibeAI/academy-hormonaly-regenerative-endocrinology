# Hormonaly release · 15 October 2026

Owner approval: `owner-approval.json` records the explicit instruction to publish all reviewed changes. No new medical, translation-professional, or accreditation approval is inferred.

## Source

- Runtime: `26b2904` on `release/hormonaly-qa-arabic-20261015`.
- Academy: `9f976ec` on the same release branch name.
- Media renderer fixes: Foundry `3778b89`, pushed on `fix/hormonaly-arabic-film-tools-20261015`; original Foundry package pin retained.
- Previous live revision: `academy-hormonaly-00065-wnw` (runtime `5aa8b16ec515`, academy `58a29dec693a`). Those metadata changes were merged into this release.

## Scope

Eight Arabic films with matching posters/captions, localized playback and transcripts, course layout and activity-feedback fixes, shared navigation/footer, bookstore links, compact bilingual homepage phone previews, and supplied faculty credentials/biography/LinkedIn link. Original English films are retained. New screenshot URLs are versioned to avoid stale browser caches.

## Pre-publication evidence

- 720 bilingual responsive card visits and 28 bilingual film playback checks: `../qa-fixes-20261015/QA-REPORT.md`.
- Compact homepage responsive checks: `../home-devices-20261015/README.md`.
- Package checks pass; historical report-only design findings are unchanged.
- All eight deployment eval suites pass, including locale parity, clinical-safety routing, grounded tutor, payment boundaries and verification-email boundaries.
- Seven metadata regression tests pass after merging the latest live metadata changes.
- Exact frozen/offline dependency install and both TypeScript configurations pass.
- Eight reviewed film SHA-256 checks pass (`media-integrity.json`).
- 30 uploaded objects match local MD5 and size (`cloud-media-integrity.json`).

## Deployment

Standard `deploy/gcp.sh --candidate-only`, then exact-revision promotion after candidate health, certificate authentication and browser checks. Cloud build: `6572980e-72d6-4fc4-a647-2426429fc4d8`. Final revision and live proofs will be appended after publication.

### Candidate playback correction

Candidate `academy-hormonaly-00066-f5c` passed health/auth and homepage checks but was not promoted: the Arabic homepage trailer failed to load with CORS mode on a bucket-redirected video. The bucket had no CORS configuration. Applied the standard public GET/HEAD media CORS policy (`media-cors.json`). Runtime `26b2904` additionally uses the existing same-origin VTT proxy without forcing CORS mode on local caption paths; external caption URLs retain CORS mode. Verified the production build through the real server and published Cloud Storage media: 78.15-second Arabic trailer, readyState 4, active playback, no media error (`cloud-media-player-fix.json`). Candidate caption endpoint serves the Arabic WEBVTT successfully. Rebuilding via the same deployment script with `--skip-media`; media checksums remain unchanged.

## Published

Published on 15 October 2026, revision `academy-hormonaly-00067-9vk`, 100% traffic. Final cloud build `ec9994e1-c55a-4e13-a562-52d59676de1e`. Exact-revision promotion used the standard deployment script; provenance checks passed without an override. `deployment.json` records the full release identity.

Live checks on https://hormonaly.perceptors.ai:

- Health: app and database OK. Unauthenticated certificate endpoint returns 401.
- Both homepage trailer editions load and play; Arabic is 78.15 seconds with its Arabic caption URL.
- Authenticated Module 1 films play in English and Arabic; Arabic is 113.033333 seconds, readyState 4, active playback, no media error.
- Faculty credentials, supplied Dominik biography and LinkedIn link are present.
- Homepage and footer bookstore links point to books.perceptors.ai.
- Compact previews use versioned screenshot URLs and display the new feature callouts.
- The learner account still has seven completed modules and a pending final assessment/certificate. No assessment was submitted; the account language was restored to English after the check.

The review-hub publication step correctly skipped accreditation publication because this academy does not license that flow. No accreditation status or certificate was issued by this release.

Proof: `live-browser.json`, `live-revision.json`, `live-homepage.png`, `live-arabic-module.png`; full checks are in the associated QA packets.
