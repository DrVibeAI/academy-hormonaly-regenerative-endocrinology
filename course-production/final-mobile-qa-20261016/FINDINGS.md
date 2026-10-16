# Final mobile QA findings — 16 October 2026

All fixes below are deployed in `academy-hormonaly-00080-fm4`.

| Finding | Fix | Verification |
|---|---|---|
| Completed activities could not be retried | Added localized Practice again and Back to saved result. Practice state stays local and preserves saved completion. | Replayed every activity in English and Arabic; reload restored saved results. |
| Completed embedded quizzes could not be retried | Added local practice attempts with wrong/correct feedback and evidence explanations. | All 21 checks per language exercised. |
| Static audio topic markers invited an impossible flip | Instructions now distinguish topic markers from cards with a reverse side. | Playback and flip controls checked. |
| English narration could play only through an uncached fallback | With explicit owner approval, granted the existing service object creation only under `guide-audio/`. | Newly generated GCS audio played; reload reused the same URL. |
| Arabic voice-note prompt requested English transcription | Corrected the Arabic transcription instruction. | Source/build verified; microphone recording remains untested. |
| Arabic retry guidance and profile language label leaked English | Localized retry guidance; profile uses the selected learner language. | Profile shows العربية; final assessment pass/fail/retry exercised in both languages before final label-only patch. |
| Arabic covers inherited the English film poster as a background | Importer now keeps explicit hero artwork separate; existing cover component selects the language-specific poster and places it above the title. | All seven covers in both languages loaded at 320 px on the final live revision. |
| Numeric ranges reversed visually in Arabic | Isolated authored numeric figures with left-to-right direction. | Live Arabic 7.7–14.4% card visually verified at 320 px. |
| Older open pages could go blank after a deployment changed a dynamic JS filename | Added a bounded automatic reload and an accessible manual retry fallback. | Real browser fixture recovered from a missing chunk; regression tests cover loop prevention and unrelated errors. |

## Scope limits

This is functional and responsive UI QA, not clinical reapproval. Published governance and clinical claims were not changed. Testing used the Codex in-app Chromium browser with mobile viewport overrides, not physical iOS/Android devices. Audio/video playback, decoding, controls and transcript availability were checked; every full recording was not listened to end-to-end. Microphone input, new-account enrollment/terms acceptance and certificate issuance were not exercised. No certificate was issued. QA attempts saved 100% on Omar’s account.
