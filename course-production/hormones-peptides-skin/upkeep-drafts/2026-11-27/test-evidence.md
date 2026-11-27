# Offline verification evidence — 2026-11-27

**agent pre-review — no gate opened**

These are technical findings. The original draft stays unapplied; no human decision was created.

## Commands and results

Run from the academy worktree:

```sh
python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-27/validate_proposal.py
python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-27/test_validator.py
perceptor check packages/hormones-peptides-skin.json
git diff --check
```

- Offline validator: exit 0, `OK: 0 failure(s)`. [Full output](evidence/validator.txt).
- Mutation suite: exit 0, **17 tests passed**, including subcases for three block bindings, six source bindings and five approval field spellings. [Full output](evidence/validator-tests.txt).
- Worktree `perceptor check`: exit 0, schema valid; tic, anchor and citation audits clear; interaction audit 63 items, zero warnings. [Full output](evidence/perceptor-check.txt).
- `git diff --check`: exit 0. All added files were also checked with `git diff --no-index --check /dev/null FILE`: no whitespace findings (this Git returns 1 for some added-file differences even with no whitespace errors).
- `git diff --name-only`: empty; all changes are new files under this dated directory. No tracked package, authored content, source lock, academy config, Foundry lock, catalog, governance or gate file changed.

## Negative coverage

All mutation cases invoke the actual validator as a subprocess and require exit 1 plus the intended failure message. Temporary copies are removed afterwards:

- Changed beat body, changed title, or reordered valid whole-sentence beats with matching source maps.
- Citation replaced with an existing registry ID from the other target block.
- Stale whole-block fingerprint, body hash or audioScript hash.
- Stale original package SHA, size, blob or base commit; changed source-lock hash or Foundry ref.
- Added approval fields, governance/status fields or changed original provenance.
- Changed package teaching or watch metadata; changed source-lock bytes; unavailable local Git history.
- Emit target inside the repo, an already-existing target, or emission after failed validation.

Positive coverage includes the current package and a patched external copy. The copy is compared to the current package with only the seven proposed beats inserted; the source package remains byte-identical.

## Limits and unchanged state

The installed CLI was used for the requested worktree check:

- Resolved CLI: `/home/hermes/DrVibe/hub-releases/3101a4a7faeb4eab78ac2f9732285b49cbbc2fe5/bin/perceptor.mjs`.
- CLI SHA-256: `ccce511653580e3b2c492d5752916a82fc6c27bef637e1cd593522f0dbb2d7ca`.
- Environment: `Python 3.11.2`, `git version 2.39.5`.
- Academy Foundry pin remains `69b4706c26505bb6b03b08be6ab900b7493a0816`; the installed CLI release differs. This is not a claim of executing the pinned Foundry checkout. The operator retains responsibility for its foundry-tests and runtime-build checks.

The CLI reports dosage findings (70 fail, 146 warn, four notes) and one missing-logo finding in report-only mode. Its exit 0 does not clear these, resolve copy review or grant any human approval. Caption audit found no VTT tracks. No browser, runtime on-demand audio, provider, playback, paid QA or synthesis check was run.

Both complete target blocks, all proposal teaching and all provenance/citations/source-lock data match the original proposal baseline. The only package drift is the six added watch-source arrays. Their URLs were not fetched; they do not renew dated regulatory statements.

The package has 48 audio blocks, 138 existing beats across 46 blocks, and zero registered standalone audio assets. The two target blocks still have no beats. Its assets remain 48 illustrations, seven opener videos and seven posters. Runtime on-demand audio is a separate unverified path.

No controller call or hub-run update was made. The human pause on `run-76e4274d-4ce7-40d0-9ee9-193e26e3a31d` was not resumed or changed. No voice choice, media request, registration, cloud mutation, communication, staging, commit, push, merge or deployment occurred.

## Tested file hashes

| File | SHA-256 |
|---|---|
| `audio-beats-proposal.json` | `f3fda07716e83ddd17824db624281849250b996c66200d9e4acf11dd20330467` |
| `validate_proposal.py` | `9e9e41c513b8e9bac3c04aa3b8ce8dbfaf90cca12747663eee72f0152f42e40d` |
| `test_validator.py` | `57c9cc037d087b6cf3cc936cbebc1a5a1211734b0cc36e749c5d00de8f5968ae` |
| `voice-options-note.md` | `cc75600a0bf43a90fc0badfd4c28074067c1c466e38df95bdbe408920d94dff8` |
