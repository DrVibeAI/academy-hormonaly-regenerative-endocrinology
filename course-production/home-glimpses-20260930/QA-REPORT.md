# Branded homepage course snippets — 2026-09-30

Owner requested replacing the old violet/green in homepage course snippets and making this repeatable for white-label academies. Five fresh captures show the actual blue learner runtime: opening film, trial evidence, clinic case, certificate-of-analysis audit and regulatory rules. They use new PNG paths so existing image caches cannot retain the old colors. The original clinical imagery, presenter, disclosure, course text and typography are preserved.

## Source and reusable checks

- Academy input: `495981abab6a6d351a6590ba12a14b678e602623`.
- Shared runtime: `5e9d98cddfc80fc8b47b68c93423406dd606e9d2` in `/Users/omar/DrVibe/releases/hormonaly-brand-guide-20260930/perceptor-runtime`.
- Foundry contract/template/check/ledger: `59dac3e733e373173e8e33d99a2e238d9db98c6a`.
- Capture manifest: `presentation-inputs/home-glimpses.json`; actual UI source commit `b937d9a1a58c9210843476996bbd5e1189583cc7`. The new runtime change only checks capture provenance during preparation; it does not change learner rendering.
- Course 1.1.0 SHA256 unchanged: `cb7b66528438d0081b05cc3d08e4b5f2625f3eac94898beb13ebafd5dd936334`.

The shared preparation check compares academy identity, visual branding fingerprint, course-package hash, complete image coverage and host image bytes. Tests cover two fictional palettes (blue/copper), cross-academy rejection, stale branding, package/image drift and legacy compatibility. Two runtime regression tests and four signature-audit tests pass; Hormonaly strict signature audit has zero errors/warnings. New signature-course templates declare the manifest. Legacy academies warn until migrated; this change does not deploy other customers or automatically recolor raster images.

## Actual browser verification

All five images were captured through the Codex in-app browser from the actual responsive runtime at 390×844. Browser resizing timed out, so an isolated local HTML wrapper supplied a 390×844 iframe viewport. No course-style changes were used. Local fixture unlocked modules 1–6 and selected the authored exercise choices through ordinary UI clicks; no live learner progress/grades were altered. The film was played/paused and sought to 6 seconds through its actual controls, retaining the existing presenter and disclosure.

Desktop strip at 1280×720: all five images resolve at native 390×844; `homepage-strip.png`, `preview-images.json`. Original localhost 5187 preview updated from the same input/guard files with pending certificate work preserved. Mobile homepage wrapper at 390×844: document width equals viewport (390), and the strip scrolls horizontally to the country-rules preview; `homepage-mobile.png`. This is local responsive-browser proof, not a physical-device claim.

Preparation, typecheck and production build passed. All six deployment suites passed in `../evals/report-2026-10-01T042912Z.md`. Deployment proof is recorded below after exact-candidate verification. No medical/assessment/content/media-production change, new certificate policy or international-edition sign-off.

## Deployed

https://hormonaly.perceptors.ai serves **100% on academy-hormonaly-00031-q7f**; immediate rollback predecessor `academy-hormonaly-00030-jkj`. Cloud Build `423b0268-34e2-448d-a854-dd9034bfac43`; image digest `us-central1-docker.pkg.dev/perceptors/cloud-run-source-deploy/academy-hormonaly@sha256:cc57d91cd3c541a1762b5058a99faa9993cd11b3f95bd310358e081ee8f8cb1e`.

Candidate app/database healthy, unauthenticated state/certificate 401. All five hosted new images return 200 and their SHA256 matches the local reviewed captures (`candidate-checks.json`). Existing enrolled owner continues into lesson 1/7, without answering or changing assessment outcomes. Exact candidate promoted through the normal deployment script. Production app/database and protected endpoints verified, 100% revision traffic recorded (`production-checks.json`); the live homepage resolves all five new images at 390×844 (`live-images.json`). Actual public strip screenshot: `live-homepage-strip.png`.

Capture wrappers removed, isolated 5188 server stopped and candidate/capture tabs closed. Existing preview and live homepage tabs remain. Viewport override/reset calls timed out; subsequent ordinary-page screenshots confirm the normal 1280×720 browser size. No temporary phone override was used in the successful captures. Pending original runtime authority/certificate work remains preserved. Source/evidence snapshots are committed locally; no main merge/push. Review hub receives the identical course context through the standard promotion step; no outbound reviewer notice or approval change.
