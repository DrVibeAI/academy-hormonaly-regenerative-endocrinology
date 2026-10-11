# Source of Cloud Run revision academy-hormonaly-00059-7md

Recorded 2026-10-11 from the revision's own build archive (nothing here is inferred from names or dates).

| | |
|---|---|
| Service / project | `academy-hormonaly` · project `perceptors` · us-central1 |
| Created | 2026-10-09 03:37:41Z, by omar@hormonaly.ai (serving 100 % as of 2026-10-11) |
| Image | `us-central1-docker.pkg.dev/perceptors/cloud-run-source-deploy/academy-hormonaly@sha256:5126f26483edf933174f516fd92d049198277462f98e1d42e17d4db878d094fd` |
| Source archive | `gs://run-sources-perceptors-us-central1/services/academy-hormonaly/1791516899.294321-a5d6e93bad3f4b8f8933637fbbf68f2d.zip` (uploaded 03:34:59Z) |
| Course served | `hormonaly.hormones-peptides-skin` **1.2.0-ar-AE.1** (Arabic, UAE edition) |

## Runtime source

- Every tracked file of the archive is byte-identical to **perceptor-runtime `2fa4d7d`** ("Audit P2/P3 fixes: enroll defaults to
  create-account, hours basis, print rules, terms banner, admin placeholders, Arabic copy", 2026-10-08 20:33:58 PDT).
- GitHub backup branch: **`release/hormonaly-00059-20261009`** in DrVibeAI/perceptor-runtime (21 commits beyond `origin/main`, which stops at
  74c818c, 2026-10-02; they existed on this Mac only until 2026-10-11).
- Not in 00059 although on disk next to it: the staged boot-flash changes in `releases/academy-boot-flash-20261011/runtime-hormonaly`, and the
  diverged "premium pass" line (`73cf9b5`, 132 commits not in `2fa4d7d`, which lacks 21 commits that 2fa4d7d has). Deploying that line to
  Hormonaly would drop the Arabic and audit work.

## Academy content

- `academy.yaml` (sha256 86cfd2b97ca4951bedb003c4a72645d25cb6620639b78e8d0a573f66901d9ea1) and
  `packages/hormones-peptides-skin.ar-AE.json` (sha256 9f3f3b47199c7aad43a2e23b30476784c44ed446abfcd64b65d5dd6b2a7b4491) are
  the files of this branch, verified identical to the archive's.
- Origin on disk: `/Users/omar/DrVibe/releases/hormonaly-audio-cards-20261008/academy-inputs/` (not a git checkout). They were never committed:
  this branch is `factory/arabic-skin-20261007` (3ef575e, package `1.2.0-ar-AE.draft.1`) plus those files.
- The English 1.1.0 course package in this branch is unchanged from that branch; 00059 itself ships only the ar-AE package.
- Searched 2026-10-11 for anything newer: no `academy.yaml` or ar-AE package newer than 2026-10-08 20:34 exists on disk; the only newer
  GitHub pushes (Hermes, `operator/20261008-build-hormonaly-upkeep-…`) add an upkeep report, no content.
