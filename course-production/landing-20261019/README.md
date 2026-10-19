# Hormonaly landing-page assets — 19 October 2026

Status: prepared and locally verified; not deployed.

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

Publication is pending Omar approval under /Users/omar/DrVibe/AGENTS.md.
For release, recheck current production lineage, then use the unchanged runtime deploy/gcp.sh with this academy directory; run its required release suites and verify anonymous /api/certificate is 401.
