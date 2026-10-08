# Arabic review deployment — 7 October 2026

The Arabic review candidate is deployed at [Hormonaly Arabic review](https://candidate---academy-hormonaly-limjs7pr6a-uc.a.run.app/). This is a review deployment, not an approved public release.

- Candidate revision: `academy-hormonaly-00053-whj`, zero production traffic.
- Public English revision: `academy-hormonaly-00051-54r`, unchanged at 100% traffic.
- Runtime: `ab5067a978a37143018b845e1b0dd94c9c8a170c`.
- Based on the verified October 3 serving course and academy configuration. The canonical English course package is unchanged.
- Arabic review notices remain visible. Terms are readable without requiring reviewers to sign draft agreements. Existing enrollment authentication remains required for signed-in course access.
- Review progress stays in a separate local namespace. Production progress, new purchases, legal acceptance and certificate issuance are blocked in this candidate; the public English service is unaffected.
- English reference-film selection is explicit. Delivery records are preserved; the deployed source uses legacy reference MP4s. This does not mark Arabic films or captions complete.

## Verification

All eight deployment suites passed: locale parity; 64 authored tutor assertions; regional safety; review access/reference selection; four Arabic model-backed groundedness/safety assertions; checkout; email boundaries; and Today behavior. Type checking and the cloud production build passed. App/database health is 200/ok; unauthenticated certificate, progress and admin APIs return 401. No certificate, email, learner progress or legal acceptance was created during verification.

All 110 declared assets return HTTP 200. All 48 uploaded Arabic narration files match local checksums and use no-cache while in review. The hosted homepage and legal page render in Arabic/RTL. The reference trailer reaches readyState 4 with no media error. The final hidden keyboard skip link no longer creates horizontal overflow (verified document width equals the 1113px viewport); keyboard focus still reveals it. Earlier local mobile/account-menu proofs remain in the QA repairs folder; a fresh hosted phone-width proof is not claimed.

## Still required before public release

Arabic opening films, trailer, target-language screenshots/visuals and timed captions; the 21 Saudi citation/verification gaps; Fady's medical/language and source-lock amendment review; legal review; evidence refresh, design acceptance and final release decisions. No human approval was inferred or recorded.

The latest full release gate remains open on these items:

- medical review: every module medically approved (0/7).
- evidence: claim-support report is fresh for this content.
- quality: citations.
- quality: design contract (tier, logo, kill-list).
- structure: assessments approved.
- media: media preview approved (110 generated asset(s)).
- jurisdictions: SA regulatory layers mapped.
- locales: en edition reviewed (base edition, covered by the medical review).
- locales: ar-AE edition reviewed.
- framework: academy content merged to origin/factory/intake-hormonaly (reviewed build reproducible).
- sign-off: course signed off as final by the product owner (academy.yaml catalog → final: {by, date}).

The deployment gate passes runtime behavior checks; it does not replace the content release gate. The package remains in review, with `mediaComplete:false` and `publishReady:false`.
