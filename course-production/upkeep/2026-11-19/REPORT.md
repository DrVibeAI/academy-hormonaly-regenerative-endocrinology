# Hormonaly Academy nightly upkeep — 2026-11-19

agent pre-review — no gate opened

## Result: warn — checks pass; existing media gaps unchanged

The monitor advance contains only the November 18 eval report and summary. No package or media changes were detected. Existing unapplied read-along drafts were revalidated rather than duplicated. Standalone narration remains incomplete; no paid production was initiated.

## Scope and ownership

- Academy: academy-hormonaly-regenerative-endocrinology; tracked branch factory/intake-hormonaly.
- Source commit: 5497f64d1ad2af3148d0db232bee7f7028ecb89d.
- Package SHA256: 6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa, identical to prior upkeep.
- Hub course: hormonaly-hormones-peptides-skin; run run-76e4274d-4ce7-40d0-9ee9-193e26e3a31d, revision 26, inspect mode, paused by a person, not busy; no open questions or pending requests.
- Hub run/stable/installed release: e3f0014bb224a6c275d7138c11b67ca19d5fc7ae; compatible; no release hold currently reported. Historical release-hold statements were not carried forward as current facts.
- Academy foundry.lock remains 69b4706c26505bb6b03b08be6ab900b7493a0816; no pin migration.
- Boot pull: foundry already up to date. Tracking check reports pre-existing dirty trees. Academy untracked course-production/claim-support/checkpoints/ and foundry modified .gitignore preserved. Unrelated repositories untouched. Evidence collected in an isolated worktree on operator/20261119-hormonaly-upkeep.

## Actual execution and evidence

See inventory.json, check.txt, dead-screen.txt and existing-proposal-check.txt beside this report.

- `perceptor check`: exit 0. Package, catalog, skills and config checks pass. Missing customer logo is report-only; no VTT tracks found. This is not publication readiness.
- Inventory traversed all 179 blocks: 48 audio blocks, zero registered audio assets; no narration-voices.json. Missing standalone audio remains a real gap; this does not say the films lack audio.
- Read-along: 138 beats across 46 audio blocks. m4-p06 and m4-p11 still lack beats in the selected package.
- No sourceInsights; guided-reading audio is not applicable, and none was invented.
- Zero videoBriefs; no missing-render brief calls for a new storyboard, generated still/footage, or desktop render request.
- `perceptor render status`: no render queue. Seven selected videos probed with ffprobe, all exit 0, with video/audio streams. All actual SHA256 values match registered checksums and prior upkeep evidence. No changed or newly landed film bytes.
- Dead-screen audit: exit 0, zero warnings, TOTAL 0.0 seconds because there are no videoBriefs. It does not inspect the seven rendered films. Stream probes and checksums do not establish playback, visual quality, motion or scientific correctness.
- No paid draft/primary vision gate repeated on unchanged media.

## Existing draft reused

Remote branch re-read and confirmed at a09f3d4ea3c81744ce62d2cf770360f5334962f2:

https://github.com/DrVibeAI/academy-hormonaly-regenerative-endocrinology/tree/operator/20261112-construct-goal-prepare-reversible-offline-read-alo

Its offline validator ran in a detached isolated checkout: exit 0, `OK: 0 failure(s)`. It verifies the same package digest as today's inventory, source/citation bindings and seven proposed beats for the two gaps. The proposals remain unapplied. No expert invocation used (maximum one allowed); identical inputs and an existing validated proposal do not justify duplicate authoring.

The voice-options note remains a proposal, not a voice selection. No provider/voice migration, governed voice registry or person's answer was invented. The initial proposal-validator invocation used an incorrect directory and exited 2; file discovery resolved the actual nested path and the real validator then completed successfully. An arbitrary-Python orchestration call was denied by cron security; normal read/terminal tools completed the inspection instead.

## Remaining work and boundaries

The course owner's voice decision and governed narration configuration are still needed before synthesis. Applying the existing reviewed beat proposal requires integration authority outside this job's no-merge boundary. Intentional production pause remains preserved; no resume, tick or replacement pipeline.

No new content/media draft was produced. No deploy, external message, approval, gate/catalog/accreditation edit, merge, source-lock application, selected-media replacement, paid media call, local render or queue mutation occurred. New artifacts are this report and deterministic evidence only, committed and pushed on the work branch.

Report URL after push:
https://github.com/DrVibeAI/academy-hormonaly-regenerative-endocrinology/blob/operator/20261119-hormonaly-upkeep/course-production/upkeep/2026-11-19/REPORT.md
