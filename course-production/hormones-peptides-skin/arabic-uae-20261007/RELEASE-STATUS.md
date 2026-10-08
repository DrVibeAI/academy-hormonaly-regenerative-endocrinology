# Arabic UAE course edition — review handoff

Agent pre-review — no gate opened. Prepared 7 October 2026.

Primary audience: clinicians in the UAE. Language: Modern Standard Arabic, ar-AE, RTL. Secondary regulatory context: Saudi Arabia, with product-specific status and explicit uncertainty. Named medical/language reviewer: Fady Hannah-Shmouni, Fady@hormonaly.ai. No message has been sent to the reviewer.

## Delivered for review
- Seven modules, all 3,797 original localized text fields translated; zero blank Arabic fields or unchanged long English passages. Seven module checks and 14 final questions retained.
- Arabic tutor answers, search synonyms, source notes, and localized academy copy.
- 48 Arabic narration recordings (Yousef, licensed ElevenLabs library voice), transcripts, duration and checksum manifest. Technical playback tested; pronunciation review is pending.
- Seven opening-film scripts translated. Original editable English projects, narration, visuals, presenter media and caption timings recovered; source hashes and extracted English VTTs recorded.
- UAE/Saudi regulatory addendum, 30 lesson notes per country, Arabic authority/product labels, and explicit product-verification gaps; source-lock amendment pending.
- Reusable regional-localization agent based on the CAIH country-profile pattern; declared practice country is independent of learner language. Hormonaly remains slide-free microlearning plus editable motion films.
- Native platform Arabic interface and regional-locale fixes; RTL desktop/mobile checks, role selection, exercise feedback and audio playback verified.
- Arabic certificate PDF layout proof. SAMPLE-NOT-VALID is a layout specimen, not an issued credential. Mixed-direction text and numbers checked visually.

## Validation
- Source English SHA-256: 6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa. Original source file unchanged.
- 332 original answer/grade/citation structures checked without changes.
- 59 numeric-format differences compared semantically: spelled-out numbers, Arabic dual forms, expanded year ranges/decades, Roman II, and duplicated bilingual terms. No numeric-value change found. This is agent QA, not medical sign-off.
- Corrections include a reversed Portugal advertising restriction, erythropoietic protoporphyria terminology, ND professional title, and several grammar/terminology issues.
- Package schema validation passed against the foundry version matching this source course. The older canonical foundry checkout's schema does not support existing source-course interactions; no source fields were removed to fit it.
- Locale auditor: 3,797 original fields and 713 protected structures pass; 30 notes per country, no citation-ID or translation gaps. This is coverage, not legal approval.
- Runtime type checks, jurisdiction-context tests, tenant-isolation check, locale check and production build passed. Regional-locale and certificate-direction tests passed.
- Live tutor API, sign-in, payment, certificate issuance, and full learner end-to-end acceptance were not exercised against production.

## Still required before release
1. Fady’s Arabic language/medical review, including pronunciation, study claims, evidence grades, professional scope and diagram-arrow direction.
2. Review of the regulatory source-lock amendment. Saudi registration is not inferred for research peptides or for Mounjaro from an inaccessible product record. Unregistered-product enforcement is not described as a ban on every peptide medicine. Abu Dhabi rules remain explicitly scoped to DoH facilities.
3. The seven original editable films and source assets have now been recovered from the laptop’s hidden Perceptors media folder; see FILM-SOURCES-RECOVERED.json. English timed captions were recovered verbatim from the compositions. Confirm their approved release correspondence, pin the Arabic render contracts, and produce/QA the Arabic films and captions.
4. Media review, native acceptance on the approved edition, accreditation decision where applicable, and explicit publication authorization.

The ar-AE edition stays `in_review`, with `mediaComplete:false` and `publishReady:false`. No approvals were copied from the English edition. No live course or deployment was changed.

## Review entry points
- `review.html`: complete bilingual editorial review, assessments, tutor corpus, source notes, and Arabic narration.
- `regulatory-addendum.json`: UAE/Saudi change proposal and official sources.
- `LOCALIZATION-COVERAGE.md`: implemented regional adaptation and remaining verification.
- `localization-policy.json` and `jurisdiction-overlay.json`: reusable production/country policy and explicit lesson mappings.
- `certificate-layout-sample.pdf`: specimen only.
- Native local preview: http://127.0.0.1:5197/ (requires the local preview server).

The local preview input copy uses ar-AE as its base language solely to inspect the draft. It is excluded from version control and must not be deployed. The actual review package retains English as its base and Arabic as `in_review`.
