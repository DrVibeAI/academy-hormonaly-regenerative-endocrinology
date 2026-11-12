# Hormonaly Academy nightly upkeep — 2026-11-12

agent pre-review — no gate opened

## Result: warn — reviewed offline drafts, missing narration remains

Package checks pass. One expert run produced unapplied, source-bound read-along proposals for the two missing beat sets, with seven proposed beats total. Cross-lab technical review accepted the draft; no human gate was opened. No audio, image or video was generated; the selected package and media remain unchanged.

## Source and ownership

- Academy repo: academy-hormonaly-regenerative-endocrinology; tracked branch factory/intake-hormonaly.
- Source commit: 4e63edc9f8dab13fc493bbb5f98a8cdcc77a06f6.
- Package sha256: 6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa.
- Monitor advance from 76fcf8175295 contains only two evaluation report files, not package/media/storyboard changes.
- Original checkout has a pre-existing untracked course-production/hormones-peptides-skin/watchlist/; preserved. Foundry .gitignore and unrelated dirty repos were likewise not discarded, stashed or reset.
- Live hub capabilities: installed/stable 7b1c169c4dc41951ccdea5bcc5995a0e00bf9d06, compatible.
- Existing course hormonaly-hormones-peptides-skin; run run-76e4274d-4ce7-40d0-9ee9-193e26e3a31d, revision 21, paused by a person, inspect execution, not busy. No open questions or pending requests.
- Its release remains 3101a4a7faeb4eab78ac2f9732285b49cbbc2fe5 with explicit migration hold. No resume, migration or production dispatch performed. Offline maintenance does not bypass that hold.
- Academy foundry.lock remains 69b4706c26505bb6b03b08be6ab900b7493a0816.

## Verified inventory and checks

See inventory.json, check.txt and dead-screen.txt beside this report.

- `perceptor check` in the academy and evidence worktree: exit 0; package/catalog/skill/config checks pass. Customer logo absent, report-only warning. No .vtt tracks were found.
- 48 audio blocks have authored scripts; no package audio assets, narration manifests or course narration-voices.json. Standalone narration remains missing for all 48 blocks. This does not imply the seven existing films lack sound.
- 46 blocks contain 138 existing audioBeats. m4-p06 and m4-p11 lack them in the selected package.
- No library.sourceInsights: guided-reading audio not applicable; no invented readings.
- Zero package videoBriefs: no missing-render brief requiring storyboard, stills, footage or desktop queue request.
- Seven selected package film files: ffprobe exit 0 for all seven, with audio/video streams; all seven file SHA256 values match registered checksums.
- No newly landed renders in monitored changes; queue monitor reports zero. Draft and primary paid whole-video QA were not rerun on unchanged media.
- Dead-screen audit exits 0 but reports TOTAL 0.0s because there are no videoBriefs. This is not whole-film dead-screen, playback, scientific or visual clearance. Stream probes are not playback verification.

## Sole expert run and draft

Run: 20261112-104531-construct-goal-prepare-reversible-offline-read-alo.

Command: `perceptor expert run --class construct --engine claude-code --model opus --repo /home/hermes/DrVibe/academy-hormonaly-regenerative-endocrinology --base origin/factory/intake-hormonaly --task-file /home/hermes/perceptor-runs/hormonaly-upkeep-20261112-brief.md`.

Used the configured `opus` alias (the prior upkeep had incorrectly passed a full model ID). Author: Claude Opus 5.5, high; reviewer: Codex GPT-6.1 Sol. Wrapper outcome ready, exit 0, zero fix rounds; gate-scan, secret-scan, diff-check and academy-check pass. Exactly one expert invocation, no replacement run. Wrapper pushed true and remote exact ref verified separately.

Draft commit: a09f3d4ea3c81744ce62d2cf770360f5334962f2.

Draft branch: https://github.com/DrVibeAI/academy-hormonaly-regenerative-endocrinology/tree/operator/20261112-construct-goal-prepare-reversible-offline-read-alo

Files under course-production/hormones-peptides-skin/upkeep-drafts/2026-11-12/:
- audio-beats-proposal.json: m4-p06 four beats, m4-p11 three beats, exact existing sentences and copied citations, package/block/source-lock fingerprints, explicit unapplied draft status.
- validate_proposal.py: offline source/shape/word-count/qualification/fingerprint checks.
- README.md: reproducible verification and limitations.
- voice-options-note.md: existing stock Alice versus historical Gemini registry context; no voice selected or registered.

Parent reran `python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-12/validate_proposal.py` in the expert worktree: exit 0, `OK: 0 failure(s)`. Beat word counts verified by tool: m4-p06 21/11/35/13; m4-p11 19/27/33. Package SHA and original source bytes unchanged; expert worktree clean. Technical review returned no findings. The reviewer decision is a code/draft check only, not creator/scientific approval.

## Remaining work / human boundaries

- Drafts are unapplied. Existing selected package still lacks the two beat sets and all standalone narration. No claim of production or media readiness.
- Course-owner review/voice decision and the governed narration registry are needed before audio synthesis; no voice/provider migration or unbounded generation was invented. Existing records name stock Alice while film provenance names historical Gemini; the draft documents this distinction.
- These proposals preserve approved source wording, including potentially repetitive contrastive phrasing; source-faithful extraction is not a copy-quality rewrite or fresh regulatory review.
- Intentional-pause recovery and run migration need applicable Omar authorization if production is to resume; this job did neither.
- No merge, deploy, send, approval, gate edits, catalog/accreditation changes, selected-media replacement, paid media calls, queue mutation or local render.

Evidence branch: https://github.com/DrVibeAI/academy-hormonaly-regenerative-endocrinology/tree/operator/20261112-hormonaly-upkeep

Fleet upkeep is warn, not fail: the bounded offline draft task executed and passed technical checks, while actual narration remains incomplete and the proposed package change is deliberately unapplied.
