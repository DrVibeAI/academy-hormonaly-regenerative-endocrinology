# Skin text tutor integration — October 2, 2026

**agent pre-review — no gate opened**

The shared runtime candidate adds current authored activity, explicit editable preferences, optional prepared practice and aggregate formative metrics to the existing text Guide. The bank is a separate companion; the approved hormones-peptides-skin 1.1.0 package is byte-identical to the existing release. Current Hormonaly admin-assistant code/configuration is preserved.

## Candidate and content

- Runtime pin: `1ee774a2b2779831a5281fe92192c50f203cd39b`, based on the live admin-assistant runtime `30ac81e6f2af198377586e92252800d3c3c98020`.
- Academy baseline: `fec72a7c02f8148fb20231c99dd7f9a22167531b`. Companion bank: `../tutor/hormonaly.hormones-peptides-skin.bank.json`; proposed, no reviewer confirmation recorded.
- [Medical packet](MEDICAL-REVIEW.md): 52 new framing lines and 26 sourced library items, with exact bank digest. Existing source approval does not approve a new clinical case.
- Bank audit: 64/64 golden cases, zero failures/warnings, 100-word maximum before the first tap. [Audit](bank-audit.json).

## Findings

| Check | Finding / evidence |
|---|---|
| Authored activity and grounded fallback | Module/moment/locale resolved by server; safety and existing retrieval retained. Final seven release suites pass at the runtime pin. [Final course report](../evals/report-2026-10-02T220200Z.md). |
| Scope, server grading, review/locale gates | Authenticated org/course/user; forged choices/scores, replay and stale versions rejected. Proposed and unsupported-locale banks disabled in production. [Tutor suite](tutor-tests.txt). |
| Preference durability and event privacy | Closed learner-selected fields; course/account isolation, transactional rollback and server aggregates exercised with real PostgreSQL semantics via pinned PGlite. Typed questions/mirror quotes/teach-back prose excluded from new records. Existing Guide gap/chat logging remains separate. |
| Wrong-answer feedback and repeated exposure | Every option's rationale and correct marker shown immediately; options remain tappable. Repeated correct taps and revisits do not inflate first independent correct indicators. [Browser preview](skin-quick-check-feedback-final.png). |
| UI and production build | Current Guide styling, preferences and source controls checked locally. [Build](skin-build.txt). [Admin regression](editing-regression.txt) preserves current assistant/editing behavior. |
| Small screen | Real course rendered in a synthetic 390 × 844 CSS viewport; scrolling, feedback, input and memory controls inspected. [Phone preview](skin-phone-feedback-390.png). This is not physical-device evidence. |
| Formal checks and approved assets | Approved package unchanged; prepared practice is formative and cannot award course/check/certificate outcomes. Narration, video, captions and accreditation records unchanged. |

## Open release conditions

1. Fady Hannah-Shmouni confirms or revises the exact bank and each item. The response-layer specification says: “The medical owner confirms” and “A learner-facing build refuses any item that is not confirmed.” Proposed content appears only in the visibly marked local preview. No field was pre-confirmed.
2. Stage a candidate based on the current release lineage, then check an actual enrolled session, preference save/reload/clear across sessions, practice review gating, source navigation and existing paid enrollment/media/admin boundaries on that exact revision.
3. Inspect declared locale/jurisdiction/device behavior. Skin remains English text-only. Future course banks and translations need their own review; this bank must not be copied into unrelated courses.
4. Promote only the tested revision through the existing release process. Current observed live service remains `academy-hormonaly-00044-2h8`; this change has not been published.

No live learners, formal assessments, provider purchases or clinical approvals were changed. No conversational video integration or active pilot. Vendor latency/cost, delayed recall, transfer benefit and international network performance are not measured by these local checks.
