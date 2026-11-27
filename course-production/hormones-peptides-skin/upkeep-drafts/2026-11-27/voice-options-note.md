# Voice options note: description only, no selection

**agent pre-review — no gate opened**

This note records which voice configuration is on file at base `4e63edc`. It does not select or change a voice, and it
does not write any narration config.

- **`academy.yaml → brand.voices`.** `en` is the stock ElevenLabs library voice "Alice — Clear, Engaging Educator"
  (`Xb7hH8MSUJpSbSDYk0k2`). The comment there calls it "narration on demand + tutor voice". `es-MX` is an empty
  placeholder. It is a library voice, not a clone, so `academy.yaml` needs no `cloned`/`release` record for it.
- **`course-production/hormones-peptides-skin/narration-voices.json` is absent on this base.** The pinned foundry
  (`69b4706`, `docs/narration.md` § The contract, item 3) puts the per-locale narration voices in that file. On the
  foundry's current main, `tools/narration/beats.mjs` returns "no voice for <locale> in narration-voices.json" when a
  locale has no registry entry, so on this base no beat could be voiced without a human first adding a registry.
- **Other branches have registries.** `origin/factory/readalong-pilot-m1` carries a course-level
  `narration-voices.json` with a `gemini-tts` `en` entry (`en-gb-tutor-1`, recorded as Omar's 2026-09-28 rule). Some
  release branches carry only locale-edition registries, for example `origin/release/hormonaly-spanish-selection-20261105`
  under `arabic-uae-20261007/` and `localization/ckb-IQ/`. The foundry main's `docs/narration.md` records that ElevenLabs
  v4 superseded that rule for read-along cards on 2026-10-16, and that existing `gemini-tts` registries keep working. Those
  branches are not this base, so they are not evidence for it. Which registry this course uses is the owner's decision.

Choosing a voice, a provider or a registry, and any synthesis, is out of scope for this draft. All of it stays behind the
owner's decision and the media preview gate.
