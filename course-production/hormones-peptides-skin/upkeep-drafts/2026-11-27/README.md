# Offline read-along proposal refresh — unapplied

**agent pre-review — no gate opened**

Refreshed on 2026-11-27 by run `20261127-104534-engineer-goal-refresh-existing-unapplied-hormonal`.
This reuses the seven beats for `m4-p06` (four) and `m4-p11` (three) from proposal commit
`a09f3d4ea3c81744ce62d2cf770360f5334962f2`, read with `git show` from its `2026-11-12` directory.
Original `createdOn`, `operatorRun`, context, rules and teaching are retained. The original branch was neither
merged nor cherry-picked. Delete this directory to reverse this draft.

## Why the byte bindings changed

The base is `origin/factory/intake-hormonaly` at `124d4f7276ede2378d99570ccaddbacc13ec4806`.
Relative to the original proposal's package, the entire parsed package is identical after removing only the
six newly added `jurisdictions[].updateSources` arrays: US 2, GB 2, EU 1, PT 1, BR 1, AE 3 watch entries.
These are report-only watch metadata, not admitted teaching evidence or a regulatory re-review
(`agent/GATES.md`, operational gates; canonical path below).
The exact watch entries are bound by the pinned package bytes; this refresh makes no claim about the live sites.

Only `source.sha256`, `source.bytes`, `source.baseCommit` and `source.gitBlob` changed in the inherited proposal.
The new `refresh` record retains the complete original source binding and hashes of all four original files.
Both complete target blocks (including jurisdiction variants), the entire citation registry and
`provenance.sourceLock` are unchanged. All seven beat bodies, titles, order, source sentences, citationRefs
and qualifiers are identical to the original proposal. No teaching text was authored for this refresh.
See [provenance.md](provenance.md) for exact hashes and comparison paths.

## Files and checks

- `audio-beats-proposal.json`: reused teaching, current byte bindings, original provenance and dated refresh record.
- `validate_proposal.py`: standard-library, offline validator. Requires local Git objects for both fixed commits;
  missing history fails closed, and Git transport protocols are disabled. It reconstructs the permitted refresh
  from the original proposal and pinned base, so altered source-valid text, titles or ordering still fail.
  It also retains sentence, citation, qualifier, beat-length and draft-only checks from the old validator.
- `test_validator.py`: mutation tests using temporary copies of only the package, source lock and Foundry lock.
- `voice-options-note.md`: byte-for-byte historical note from 2026-11-12, not a current branch/provider survey.
  No voice was selected, auditioned or configured. The academy config remains identical to that proposal's baseline.
- `test-evidence.md` and `evidence/`: commands, outputs and limits of this run's checks.

Run from the academy root:

```sh
python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-27/validate_proposal.py
python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-27/test_validator.py
perceptor check packages/hormones-peptides-skin.json
```

The optional `--emit-applied /tmp/NEW-preview.json` writes a validated patched COPY outside both the chosen repo
and this worktree; existing output files are refused. It does not apply the proposal. Mutation tests verify
that the copy differs only by the seven proposed beats and that validation failures emit nothing.

## Remaining holds and limits

The package still has 48 audio blocks: 46 carry three beats each (138), and these two still have none.
There are **no standalone audio assets registered for any of the 48 blocks**: the package's 62 assets are
48 illustrations, seven module-opener videos and seven posters. Proposed text does not complete narration.
Runtime on-demand audio is a distinct path, referenced in the academy voice configuration; it was not
exercised or verified by this task. No audio was synthesized, inspected, queued, registered or rendered.

Original copy-review concerns remain: the inherited proposal flags two contrastive constructions against
`docs/narration.md`'s course-wide cap. The tic audit's zero finding does not resolve that human copy review.
The US framing in `m4-p11` beat 1 still governs its later beats. Nothing here updates dated clinical or
regulatory statements; watch sources do not establish fresh evidence. Any future teaching change requires
separate source-locked review (a lock-amendment request if the corpus cannot support it).

Applying beats to authored content/package requires the named CODEOWNERS medical/regulatory review. Any
later voice/provider choice, synthesis and human media preview are separate work. Scientific, localization,
likeness/script, accreditation and publication gates remain as they stood; this draft opens none.
Hub run `run-76e4274d-4ce7-40d0-9ee9-193e26e3a31d` stays paused and untouched. No controller call was made.
The operator owns deterministic checks and cross-lab review before any integration; this run does not
commit, push, merge, deploy or contact anyone.

Canonical contracts read: `/home/hermes/DrVibe/perceptor-foundry/agent/GATES.md`,
`skills/perceptor-media/SKILL.md`, `docs/narration.md`, `docs/default-media-policy.md`.
The academy's `foundry.lock` remains `69b4706c26505bb6b03b08be6ab900b7493a0816`.
