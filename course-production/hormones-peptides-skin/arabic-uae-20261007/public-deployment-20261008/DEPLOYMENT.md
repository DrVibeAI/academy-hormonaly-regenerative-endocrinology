# Public bilingual deployment — 8 October 2026 UTC

Published [Hormonaly Academy](https://hormonaly.perceptors.ai/) after Omar's direct instruction: “arabic approved now, lets finalize deploy”.

- Revision `academy-hormonaly-00054-4bq` serves 100% of traffic. Runtime `14cdacd80df1e18094599ac7b0b28eaad8a269e3`.
- The homepage has visible English / العربية buttons. English is the default for a new browser; a selected language persists through refresh and sign-in and is applied when entering the course. RTL/LTR follows the selection. Practice country is a separate preference, defaulting to UAE for this edition.
- The hosted English and Arabic homepage, Arabic sign-in, reference trailer and 390px phone layout were checked. Both language buttons remain visible; no horizontal overflow. Local course entry verified that a fresh Arabic selection overrides a previous saved UI language.
- All eight deployment suites and cloud production build passed. Main-domain app/database health is ok; unauthenticated certificate, progress and admin endpoints return 401.
- The previous review deployment restriction is removed for this owner-authorized public release; normal enrollment, terms acceptance, state sync and certificate eligibility rules apply. No live user progress, terms acceptance, purchase or certificate was created during verification.
- English reference films remain labelled while Arabic films/captions are in production. Regulatory notes keep their explicit evidence gaps. Owner release approval does not fabricate a medical-reviewer attestation or a GCLS accreditation decision; the unsupported English GCLS-accredited headline was replaced with “Certificate of completion”.
- The canonical English package is unchanged. Reproduce the prepared bilingual inputs with `prepare-release.mjs`; the approval record, input hashes, runtime evaluation report and traffic/HTTP evidence accompany this report. The deployment routine published its private operator review context; no reviewer notifications or emails were sent.

The earlier review-deployment report is historical. This report records the subsequent owner-authorized public promotion.
