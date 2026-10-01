# Tutor answer formatting · 2026-09-30

Local preview: http://127.0.0.1:5187/#/home. Sign-in is disabled in this preview. No production deployment or runtime pin promotion.

## Result

The Guide renders a lead takeaway, short headed sections, lists, limited bold emphasis and expandable readable source titles. Legacy plain text splits at sentence boundaries without deleting content. Spoken replies remove formatting markers. The latest reply opens at its beginning, including after closing and reopening the tutor; scrolling up preserves reading position when another reply arrives.

All 14 authored skin-course answers are reformatted. Original clinical words, numbers, country/date qualifiers and caveats are retained; the HRT negative-trial finding is moved into the takeaway. Authored clinical sections remain complete even with the concise preference.

Each answer can reuse one explicitly mapped existing teaching illustration, with its module, authored title and accessible description. `metadata.tutorVisuals` maps tutor entry IDs to existing block IDs. The importer validates image role, local asset path and alt text. Live answers select imagery only from exact cited corpus/block IDs in the active locale. Model-supplied HTML, URLs and image Markdown cannot create executable content or images. Unmapped, clinical-safety, platform-help and abstention replies receive no illustration. Failed images disappear cleanly.

No Nano-Banana integration or new generated clinical images. Existing lecture imagery provides a reviewed course reference without generation delay. House typography and blue branding remain.

## Verification

- Production build, type checking, academy isolation and locale checks passed.
- Current pinned Foundry package validator passed.
- 10 formatter, visual-reference, second-academy and regional-safety tests passed.
- Generic tutor safety evaluation: 20 checks passed across 12 cases. This academy has no separate course-specific evaluation fixture file.
- Original-versus-formatted word multiset comparison passed for all 14 entries; every entry has an explicit visual mapping.
- Desktop and 390px / 320px browser checks: illustration loads, no horizontal overflow, source disclosure works by mouse and keyboard, reopening starts at the latest takeaway without a false unread indicator.
- Two real grounded-model formatting smoke checks returned sections, bullets and citations: HRT and GHK-Cu. Saved in `live-rag-smoke.json`. These are formatting/retrieval smoke checks, not a full clinical-quality certification; the UI preview uses the deterministic course answers.
- Runtime and academy whitespace checks passed. Existing certificate/authority changes were preserved.

Screenshots: `hrt-desktop.png` (course visual and evidence bullets), `hrt-mobile.png` (regulatory bullets on mobile).

## Shared implementation

Runtime: `/Users/omar/DrVibe/worktrees/runtime-authority-marks-20260930`.
Package: `packages/hormones-peptides-skin.json` in this academy.
Shared renderer/parser: `src/guide-answer.tsx`, `src/guide-answer-format.ts`, `src/guide-answer.css`.
Importer contract: `scripts/tutor-visuals.mts` and `scripts/import-package.mts`.
Live format instruction: `server/guide-rag.ts`; oversized generated replies fall back rather than truncating a safety caveat.

For this local preview, `public/assets/hormones-peptides-skin` is linked to the academy's existing assets. Recreate this link if a subsequent prepare removes it; normal release packaging must include these assets.


Deployment update (2026-09-30): the reviewed work is now live at https://hormonaly.perceptors.ai on academy-hormonaly-00029-nj2. See ../release-20260930/QA-REPORT.md for exact scope, pins, live proof and remaining verification limits.
