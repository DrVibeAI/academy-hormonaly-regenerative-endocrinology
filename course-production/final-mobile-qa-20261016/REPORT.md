# Hormonaly Academy — final mobile QA

**Date:** 16 October 2026  
**Live site:** https://hormonaly.perceptors.ai  
**Deployed revision:** `academy-hormonaly-00080-fm4` — 100% production traffic  
**Runtime:** `b670943ceda5`  
**Academy source:** `a82c66b96355`

## Result

The identified functionality and presentation defects are fixed and published. The live service reports both application and database healthy. The certificate API still returns HTTP 401 without authentication.

## Coverage

| Area | Checked |
|---|---|
| Course pages | All 180 rendered pages in English and all 180 in Arabic across seven modules. The regional appendix makes module 7 contain 29 pages; the base package alone has 179 pages. |
| Activities | Quickfire, sequence, classification, branching, scenarios, document inspection, hotspots and closing checklists in all modules and both languages. Saved completion is preserved by practice replay. |
| Embedded quizzes | All 21 per language, including incorrect feedback, correct feedback, retry and explanations. |
| Final assessment | All 14 questions in each language, a failing attempt, review, retry and a passing attempt. QA left a 100% result on Omar’s account. No certificate issued. |
| Narration | All 48 English and 48 Arabic lesson tracks observed playing with finite duration and no HTML media error. Pause/resume and chapter cards checked. English cache persistence verified after reload. |
| Films | All seven English and seven Arabic opening films played; localized transcript controls checked. Additional seek/mute checks on selected films. |
| Responsive layout | Full walkthrough at 390×844, plus 320×740 spot checks of covers, audio/flip cards, course navigation and public pages. No horizontal document overflow in recorded observations. |
| Locale and navigation | Language switching, module drawer, Today, Course, Library/search/notes, Guide response with citations, profile language, completion and certificate readiness. |
| Homepage | English/Arabic compact course previews, certificate image/PDF link, faculty LinkedIn destinations, book-cover images/store links, offer through November 30, FAQ and footer. No broken rendered images in the checked landing page. |
| Release checks | Build/typecheck, eight mandatory evaluation suites and 31 automated regression tests pass. Missing-chunk recovery also verified in a local browser fixture using the actual recovery source. |

## Fixes

See [FINDINGS.md](FINDINGS.md) for nine finding groups and verification. Changes include activity/quiz replay, audio-cache permissions, Arabic labels and transcription prompt, localized cover artwork, numeric range direction and recovery from stale deployment files.

## Evidence

- `coverage-summary.json`: counts calculated from captured page/media observations.
- `visits.json` and `*.visit.json`: DOM snapshots and viewport/media observations. Data-URI audio payloads were omitted.
- `en-replay-*.json`: exercise completion and wrong-answer checks from the final English pass; earlier Arabic replay snapshots are also in `visits.json`.
- `live-final-cover-*`, `live-final-range-ar-320.jpg`, `live-final-flip-en-320.jpg`, `live-flip-ar-320.jpg`: final live narrow-screen checks.
- `en-cache-*.visit.json`: persistent English audio cache proof.
- `final-failure-*.jpg` and `final-pass-ar.jpg`: final-assessment states.
- `settled-*-module-*.jpg`: contact sheets of course review captures. Some figures were captured during their count-up animation; use final live range proof for numeric rendering.
- `release-proof.txt`, `regression-tests.txt` and the linked eval report record deployment/test evidence.

Early `en-m*`, `ar-m*` images and `montage-ar-*` files are scratch captures made during transitions and are not final visual evidence. The recorded DOM observations remain useful. Final screenshots are explicitly named above.

## Practical limits

The mobile checks used Chromium viewport emulation, not physical Safari or Android devices. Media testing establishes availability, decoding and control behavior; it is not a complete editorial listening review of every recording. Microphone recording/STT, fresh signup/terms acceptance and issuing a real certificate were not tested. The Arabic transcription prompt correction is source/build verified. Existing regional/legal review notices and scientific abbreviations remain as authored; governance and clinical approval gates were not changed.
