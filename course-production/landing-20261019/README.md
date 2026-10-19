# Hormonaly landing-page assets — 19 October 2026

Status: published 19 October 2026. Live revision academy-hormonaly-00091-gdn serves 100% of traffic at https://hormonaly.perceptors.ai/?home&lang=en.

Visual direction: preserve the current Hormonaly page; display the real certificate as a legible document and authentic books as a compact shelf.
Content: certificate section, faculty links, bookstore section.
Interaction: retain existing certificate-to-PDF link, individual book links, hover feedback and reduced-motion behavior.

Restores the presentation configuration removed from the current multilingual source:
- English/Arabic certificate specimens and PDF links from the existing production renderer.
- Fady: https://www.linkedin.com/in/fady-hannah-shmouni/
- Omar: https://www.linkedin.com/in/omarfsaleem/
- Three English covers and two Arabic covers, linked to their bookstore detail dialogs.
- Sorani uses the English certificate preview with a localized English-preview label.

Reuses existing assets without regenerating certificate signatures, book artwork or credentials. Book provenance remains in ../landing-polish-20261016/books.json.
The user attachment informed the compact book grouping; individual original covers suit the narrower responsive section.

Base: live revision academy-hormonaly-00090-7d5, runtime e865f01208c9, academy 34c0424f67a8.
Working runtime: ../runtime at the same unchanged deployed commit.
Only academy.yaml presentation fields changed. Package files, access settings, credential rules, locale and other configuration match the base.

Verification:
- prepare:academy passed (PREPARE_SKIP_RAG=1 for local presentation review).
- pnpm run build passed, including isolation, locale checks and both TypeScript projects. Existing bundle-size warning remains.
- All nine certificate/cover asset URLs return correct types locally.
- In-app browser review at 1280px and 390px; English/Arabic shelves and certificate routing checked; Sorani English-preview label and fallback checked.
- English, Arabic and Sorani have no horizontal document overflow at 390px.
- Screenshots alongside this file.
- Public preview: http://127.0.0.1:4193/?home&lang=en

Publication approved explicitly by Omar, including operator enrollment setup. Published using the unchanged deploy/gcp.sh candidate and exact-revision promotion commands. All eight release evaluation suites and type checks passed. Live /_health reports app/db ok; anonymous /api/certificate returns 401. Deployment environment and service account are unchanged. Course package files and RAG index match the prior live deployment. All nine assets return the expected image/PDF content types. Candidate and live browser checks confirm certificate, faculty links and book covers; mobile shelf fits at 390px.

Foundry enrollment: hormonaly-hormones-peptides-skin
Canonical run: run-76e4274d-4ce7-40d0-9ee9-193e26e3a31d
Release pin: 664764a67b5e779fe026d2cd0bfca2fe8f441723 (candidate channel)
Execution: inspect; outcome inspected, revision 8. Approved landing change change-1c6378c4-4977-4368-8e42-7b730ae4b8df is reconciled. This is an existing-course presentation release through the operator deployment path. Legacy whole-course QA gaps remain reported; enrollment does not assert new whole-course completion or accreditation approval.

Deployed source: 5915f9dea4f9; runtime: e865f01208c9. Source branch: release/hormonaly-landing-20261019. Live screenshots: live-bookstore-en.png and live-certificate-en.png. Release evaluations: ../evals/report-2026-10-19T165234Z.md.
