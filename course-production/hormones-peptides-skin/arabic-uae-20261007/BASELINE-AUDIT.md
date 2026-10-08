# Deployed Hormonaly baseline correction — 7 October 2026

The first Arabic preview used canonical academy commit cef13a4 and runtime 616130a. The canonical branch was current by date, but its academy configuration and tutor presentation lagged behind the serving release. Calling that preview the current live academy would have been incorrect.

Verified directly through Cloud Run: academy-hormonaly-00051-54r serves 100% of production traffic. Its runtime is 7209291fde69e6330b1d5ce0d3170f3111fde02e. Selected app, homepage, tutor, configuration and preparation files match the deployed source archive byte for byte. The Arabic runtime now uses that release plus the preserved Arabic changes; unrelated newer shared-runtime branches were not substituted.

The seven modules, final assessments and source citations match the original canonical package. Fourteen English tutor answers were reformatted in production, with one sentence-order change emphasizing the largest HRT trials; a tutor-to-illustration map was added. Those deployed English answers and mappings are carried forward. Arabic answers retain the same evidence and caveats in their existing prose form. No lesson narration changed.

The preview now carries the deployed blue brand palette, official mark, faculty section/photos, current homepage imagery, October promotion, text-only tutor setting, academy editing configuration and runtime site/agreement behavior. Arabic review status and jurisdiction notes remain intact. English homepage capture images are reference assets and still need Arabic recapture; their English approval manifest is not accepted as Arabic QA evidence. New or changed live interface/legal text still requires a final Arabic surface audit before release.

The complete deployed academy and source-course snapshots are in live-baseline/, with hashes and archive provenance. The materializer reapplies this baseline through sync-live-baseline.mjs, so regeneration does not revert to the stale canonical configuration. Original canonical package bytes remain unchanged.

Validation: 3,797 source text fields, 713 protected structures and 30 notes per country pass against the deployed course snapshot; all seven module objects and assessments match the pre-localization source. Runtime type checks, jurisdiction tests, tenant isolation, locale checks and production build passed. Browser check confirms the refreshed Arabic learner home with blue branding. Production login, tutor services, payments and certificate issuance were not exercised. No deployment was changed.
