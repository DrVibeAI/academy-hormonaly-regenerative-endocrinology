# Hormonaly blue feedback follow-up — deployed

Owner requested replacing remaining green course accents with Hormonaly blue during the authorized deployment. Live https://hormonaly.perceptors.ai now serves **100% on academy-hormonaly-00030-jkj**. Rollback predecessor: academy-hormonaly-00029-nj2.

- Runtime input: `b937d9a1a58c9210843476996bbd5e1189583cc7`, isolated release checkout `/Users/omar/DrVibe/releases/hormonaly-brand-guide-20260930/perceptor-runtime`.
- Academy input: `890b53a63efcd4bc0e8e6773bf206bd5cfd006a0`.
- Foundry contract/ledger: `06d135b8a3e6a599e182a3e92bef7dff077e14d1`.
- Immutable image: `us-central1-docker.pkg.dev/perceptors/cloud-run-source-deploy/academy-hormonaly@sha256:70bd9eed6230c7ee90ea179adfcfb77696980ce54a8dc135c5c219b7b674da9c`.
- Course 1.1.0 package unchanged: SHA256 `cb7b66528438d0081b05cc3d08e4b5f2625f3eac94898beb13ebafd5dd936334`.

## Changes

Success background/ink now use `#EBF4FF` / `#0064CA`; primary remains `#0071E3`. Editorial palette mapping now includes remaining green hues and the separate interaction stylesheet. Interaction overrides change colors only, preserving geometry, typography and shadows. High-energy battery markers use academy palette variables. Other themes retain their fallbacks. Warning/error roles remain distinguishable. No lecture imagery, clinical content, tutor behavior, scoring or certificate policy changed.

## Verification

- Academy preparation, frozen offline dependency install, typecheck and production build passed. All six deployment suites passed in `../evals/report-2026-10-01T020319Z.md`.
- Actual local exercise sequence: placed CRH correctly; marker `rgb(0, 113, 227)` and background `rgb(235, 244, 255)`. Computed foreground/background/border/fill/stroke/shadow audit found no green UI colors on that exercise screen. Proof: `sequence-blue.png`, `computed-colors.json`. Local QA used isolated local mode; no live learner answers or grades changed.
- Exact hosted candidate: existing enrolled owner opens lesson 1/7; palette values match the input tokens. App/database healthy, unauthenticated state/certificate 401, logo 200. `candidate-checks.json` records revision/image.
- Production promotion: 100% traffic on revision 00030; app/database healthy (`production-checks.json`). Browser reload of the live domain confirms blue primary and success tokens.
- Original localhost 5187 preview updated from the same scoped files. Pending certificate/authority work remains preserved. Temporary 5188 QA server stopped and candidate/QA tabs closed.

This is focused visual/build/deployment verification, not exhaustive testing of every course state or a new clinical assessment. The preceding release's media and tutor verification applies because those inputs are unchanged. Source snapshots are committed locally; no main merge/push or new outbound messages.
