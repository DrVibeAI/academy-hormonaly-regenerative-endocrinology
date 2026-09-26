# Opening films — vision QA notes

Whole-film vision QA (`perceptor-foundry tools/qa/visual-check.mjs --mode video`, gemini-3.8-flash; frames and narration
together, figure truth against the narration and the moment's cited sources): `visual-qa-m0N-opener.json`, one per film.

- 2026-09-25 — all seven films: 0 blocking, 0 warnings (m01 on its second run).
- m01, first run (`qa-run1-m01-opener.json`): flagged a narration false start at 59 s ("inside… Inside the skin") as
  blocking and a blank card during the 57 s transition as a warning. Checked: verbatim transcriptions (gemini-3.7-flash,
  "include every repeated word, false start, stutter") of the narration track (57.9–61.4 s) and of the film's final mix
  (58.2–62.2 s) both read "…made and used inside the skin [pause] is a local loop" — no repeat; the 0.6 s pause after
  "skin" is the voice's pacing. The second run of the same check found nothing. Recorded as a false positive.

## 2026-09-25 — label corrections (M4, M5)
- **m04-opener** ("Lysyl oxidase" only): whole-film check 0 blocking, 1 warn (a short lag on the final text graphic; cosmetic).
- **m05-opener** (CRH and ACTH · α-MSH · cortisol label the follicle as a whole): 0 blocking, 0 warn.
