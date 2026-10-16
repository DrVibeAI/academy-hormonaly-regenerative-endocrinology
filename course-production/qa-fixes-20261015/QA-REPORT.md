# Hormonaly Academy — design and functionality fixes

Local draft, 15–16 October 2026. No production deployment or media upload performed.

## Baseline

Production Cloud Run revision `academy-hormonaly-00063-fb7`; runtime base `1725ef8d8f30`, academy base `58477599046c`. The baseline source archive was compared with these worktrees before editing. Runtime candidate: `da92f75`. Foundry media-tool candidate: `3778b89`.

## Changes

- All main learner pages share the same left edge and content width in English and Arabic. Arabic text and controls retain RTL flow.
- Lesson cards use their content height. Tall content scrolls within the stage; the previous/next footer matches the card edges and remains visible.
- Shared footer includes Terms, Privacy, Contact and the book store. Bilingual bookstore features appear on the public homepage and learner Today page.
- Arabic duration/question grammar corrected, including 4 ساعات و55 دقيقة and 14 سؤالًا · 5 دقائق.
- Sorters show immediate correct/incorrect feedback, chosen answer, correct classification and rationale.
- Closing checklist requires a saved choice. When earlier required work remains, its action reads “Review remaining activities” and opens the first unfinished activity.
- Module completion is labelled separately from the final assessment. Failed scores no longer mark the final check passed or offer certificate issuance in the overview.
- Arabic audio elapsed/total times retain LTR numeric order.
- Module 6 heading rewritten as “نقص الهرمون تشخيص مرضي. وانخفاضه مع العمر تغير طبيعي.”
- Module films, poster images, captions, transcripts and homepage trailer select the learner's language. English originals remain unchanged. Arabic media remains draft.

## Verification

- 720 rendered card visits: all 180 cards × English/Arabic × 390×844 and 1280×900. No horizontal document overflow; every card/footer shares its left edge and width; each footer stays within the viewport. Raw geometry is in `responsive-layout.json`.
- Today, Course and Library checked in both languages: identical desktop content edge and width, identical footer destinations. Profile additionally checked in both languages at mobile and desktop widths.
- Public homepage checked in EN/AR at phone and desktop widths. Bookstore link clicked through to `books.perceptors.ai`; destination displayed the Hormonaly book collection.
- Arabic audio played/paused and sought to 20 seconds. English sorter exercised with an incorrect selection and then completed: immediate feedback, score 6/7, Next enabled, next card opened.
- Arabic closing activity checked empty and after selection; its saved choice enabled review of remaining activities. Production final assessment and certificate were not submitted.
- Original live QA traversed all seven modules and exercised audio, transcripts, hotspots, orderers, sorters, claim review, cases, quick checks, jurisdiction panels and closing checklists. Modules 1–3, 5 and 7 used English; 4 and 6 used Arabic. Earlier saved activities in Modules 1–2 were inspected rather than reset. This follow-up adds the full bilingual responsive card sweep; it is not an independent medical or professional translation sign-off.
- Final media playback sweep: all seven module films in both locales at 390×844 and 1280×720 (28 checks), with correct source/poster language, loaded duration, active playback, no media errors, matching card/footer widths and no horizontal overflow. Arabic transcript and sound controls also checked. Homepage trailer switches between the English original and Arabic draft.
- Final media files: eight H.264/AAC films at 1080×1920, 60fps; checksums verified. Whole-video review confirms Arabic narration in all eight, 14/14 figures on time, no frozen footage and no generation artifacts. The first trailer pass’s English UI leakage was fixed and its final review has no locale finding.
- Package check passes, including 63 interactions with no warnings and 15 caption tracks with no findings. One existing short English caption warning remains. The report-only design audit retains baseline findings about the academy palette, an institutional-affiliation string and a downloaded third-party source HTML page; these were not introduced by this change.
- Runtime TypeScript application and node projects pass; academy isolation and locale checks pass. Targeted test run: 17 test entries pass, including 13 time/question assertions. Foundry motion and renderer tests: 25 pass.
- An unrelated faculty-remediation suite was attempted but could not start because this academy does not generate its separate `server/generated/learning-course.json` fixture. No claim is made that this suite passed.

## Media evidence and human gate

See `../arabic-films-20261015/README.md`, `structure-check.json`, the draft asset manifest and the whole-video reports in this folder. All scene structures match the originals. Audio/caption duration checks pass for all eight films. Automated presenter-face findings are preserved with an applicability note: the user requested the original licensed presenter structure. No automated finding is recorded as human approval.

Human review of the Arabic films and approval of the live release are the remaining gates. `/Users/omar/DrVibe/AGENTS.md` requires Omar's approval before a cloud/live deployment.

## Review links (local)

- Film gallery: http://127.0.0.1:8897/
- Homepage: http://127.0.0.1:5199/?home
- Learner course: http://127.0.0.1:5199/#/course
- Arabic UI demo correction: `trailer-arabic-demos-final.jpg`.
- Final bilingual book-store proof: `arabic-public-bookstore-final.png` and `english-public-bookstore-final.png`.

Local preview uses a guest fixture. It does not change Omar's production progress, assessment or certificate. Local preview servers must be running for these links.
