# Read-along beat drafts for m4-p06 and m4-p11 (unapplied)

**agent pre-review — no gate opened**

This is a draft proposal, prepared offline on 2026-11-12 (operator run `20261112-104531-construct-goal-prepare-reversible-offline-read-alo`).
It is independent maintenance. It does not resume hub run `run-76e4274d-4ce7-40d0-9ee9-193e26e3a31d`, which is paused and pinned
to an older release. Nothing in `packages/`, `academy.yaml`, the source lock, approvals, accreditation, the catalog,
`foundry.lock` or any media was changed. To reverse this draft, delete this directory.

## The gap

In `packages/hormones-peptides-skin.json` (v1.1.0, sha256 `6419297d…a4fa`, base `4e63edc`), 46 of the 48 `audio` blocks
carry 3 `audioBeats` each (138 beats). Two blocks in module 04 have `metadata.audioScript` but no `audioBeats`:

| Block | Title | Proposed beats | Words per beat |
|---|---|---|---|
| `m4-p06` | Serum yes, syringe no. | 4 | 21 · 11 · 35 · 13 |
| `m4-p11` | Cosmetic, supplement, drug: three rulebooks. | 3 | 19 · 27 · 33 |

## Files

- `audio-beats-proposal.json`: the proposal. For each of the two blocks it has the block fingerprint, the hashes of `body.en`
  and `audioScript.en`, the block's `citationRefs` (copied unchanged), the qualifiers the beats must keep, the
  `proposedAudioBeats` (only `title` and `body`, the shape in the pinned schema) and `beatSources`, which gives the source
  field and exact sentence for every beat.
- `validate_proposal.py`: the offline check. It uses only the Python standard library and makes no network calls.
- `voice-options-note.md`: a note on which narration voices are on file. It does not select a voice.

## How the beats were drafted

- **Only existing approved text is used.** Every beat body is made of whole sentences copied verbatim from the same block's
  `body.en` or `metadata.audioScript.en` (module 04 has a `medical_review` approval on file, dated 2026-09-24). No
  word was added, removed or changed. Two body sentences are used in `m4-p11` (beat 1, and the first half of beat 3).
  Every other beat sentence comes from the audioScript.
- **Titles are verbatim phrases** from the same two fields. The only edit is a capitalised first letter ("the funding
  question" → "The funding question").
- **No new claims and no new citations.** The beats carry the block's own `citationRefs`, which all resolve in
  `provenance.citations`. That keeps them inside the source lock (`source-lock.md`, sha256 `e830148c…`, locked 2026-09-24),
  so no lock amendment is needed.
- **The honest bounds are kept.** In `m4-p06` the beats keep the topical/injected route split, "grade C", "no randomized
  trials of injection", the US status ("in the United States … outside the Category 1 listing that covers non-injectable
  use"), and "name the route every time". In `m4-p11` they keep "In the US", "not drugs … cosmetics framework", the
  limits on supplement claims, and the funding point.
- **Left out:** `m4-p06` drops "Here is what that means in the room.", which is a scene-setting opener with no claim. `m4-p11`
  uses the body's "In the US, …" sentence instead of the audioScript's "Now the regulatory register, stated for the United
  States. Cosmetic peptides are …" (the audioScript version also fits in 35 words, but it opens with meta-narration). It
  also uses the body's "Neither route has to prove efficacy before sale — …" instead of the audioScript's "That is the whole
  reason …", because that sentence only makes sense after the one before it. The check script lists every audioScript
  sentence a beat does not use.

## Reproducible check (offline)

Run this from the academy root:

```sh
python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-12/validate_proposal.py
```

It exits 0 only when all of these hold:

1. The banner is present, `draftStatus` is draft-only, and there are no approval fields.
2. The package bytes are unchanged. The script checks the recorded sha256 and size, and when git is available it also
   checks byte equality with `4e63edc:packages/hormones-peptides-skin.json` and the git blob `21085abf…`. The source lock's
   sha256 is unchanged too.
3. The proposal is keyed by exactly `m4-p06` and `m4-p11`, and those are still the only audio blocks without beats.
4. Each block's whole-object fingerprint and its `body.en` and `audioScript.en` hashes match.
5. `citationRefs` are identical to the block's, and each one resolves in `provenance.citations`.
6. Each block has 2–4 beats. Each beat has the schema shape and at most 35 words. Each beat body is its listed sentences
   joined, and each sentence is a whole, verbatim sentence of the named field. Each title is a verbatim phrase.
7. Every required qualifier (route, jurisdiction, evidence grade) appears in the beats.

The run on 2026-11-12 printed `OK: 0 failure(s)`, exit 0. These negative cases were run on mutated copies in `/tmp`, and
each one exited 1 on the intended check:

- one word changed in a beat
- a 43-word beat
- an extra citation
- a third block id
- a single beat
- the US beat dropped
- an `approvalStatus` field added
- a stale fingerprint
- a package byte changed
- `--emit-applied` aimed inside the repo

There is also an optional dry run, which never touches the repo package:

```sh
python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-12/validate_proposal.py --emit-applied /tmp/preview.json
```

It writes a patched **copy** of the package outside the repo. On 2026-11-12 that copy was put into a git-less copy of the
academy in `/tmp`, and `perceptor check` at the pinned foundry ref `69b4706` passed. The result was `✓ check: all gates
pass`, with schema valid, tic audit contrastive/meta/colon/dupOpen/dupClose all 0, and 145 beats across 48 audio blocks.
`perceptor check` on the real worktree also passed, before and after this draft.

## What this draft does not do

- **It does not complete the narration.** Even if a human applies these beats, the package on this base has **no narration
  audio assets at all**. Its 62 assets are 48 illustrations, 7 module openers and 7 posters. Text beats are not audio. No
  narration was synthesised, rendered or queued.
- **It applies nothing.** If a human applies it, the change is a reviewed edit to `packages/`, which goes through the
  CODEOWNERS medical and regulatory review. The beats would then go through any narration step and the media preview gate
  like other media.
- **It makes no scientific, copy or voice decision.** Two of the copied sentences use the "X, not Y" family of
  constructions ("Injected GHK-Cu is not the same product in a stronger form."; "… cosmetic ingredients, not drugs, …").
  `docs/narration.md` caps those at one per course. The pinned tic audit reports 0, but a copy reviewer may prefer to drop
  `m4-p06` beat 2. The draft still passes the check with 3 beats.
- **Beats after the first are framed by the first.** `m4-p11` beats 2–3 do not repeat "In the US". They depend on beat 1
  and on the block's base-locale (US) framing, as the approved body does. The block's GB/EU/PT/BR/AE jurisdiction variants
  are unchanged.
