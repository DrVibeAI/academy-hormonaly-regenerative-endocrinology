# Iraqi Sorani and Arabic edition QA

Implementation and technical QA complete in local review copies. Status: **in_review**. Fady Hannah-Shmouni, MD FRCPC is assigned to Sorani, Arabic additions and clinical review for both academies. His sign-off and translated legal review remain pending; no new human approval is recorded.

- 7 modules, 180 lesson cards, 14 preserved final-check questions, 48 Sorani v4 narrations and 8 subtitle tracks (including trailer).
- Existing design and original films preserved; original Arabic media retained. Sorani films use subtitle sidecars. Localized artwork labels and homepage screenshots are additive.
- Across both academies: 10,421 unique source strings covered; 616 Sorani/Arabic lesson-card views checked, all RTL with no broken images or horizontal overflow. Full host dictionaries, account/recovery flows, tutor language, assessments, shared progress, exports, certificates and verifier contracts checked with synthetic fixtures.
- Both runtime typechecks, production builds, tenant isolation and Foundry evaluations pass. Foundations native host tests, host typechecks/builds and 9 no-send EN/AR/Sorani account-email renders pass.
- All 48 final Sorani narrations have hash-bound automated listening reviews; 96 narration files decode. Original video records remain unchanged. All 16 subtitle tracks are monotonic, non-overlapping and at most 25 characters/second. Independent English ASR timing checks cover all 15 module films.
- Translation QA corrections and dispositions are included. PTD-DBM correctly contains two Ds: the automated extra-D warning is a false positive. Fragment-only caption warnings were evaluated in whole timed Sorani sentences; complete-film bilingual checks pass. Automated reviews do not constitute native approval.
- Legacy Foundry schema compatibility is compared against the pinned source: no new normalized error signatures. Sources themselves have 76/157 legacy-schema errors; candidate counts 76/164. Seven additional alias records repeat existing unsupported metadata. Current runtime importer/reference/assessment contracts pass.

Source lock, coverage, narration receipts, caption timing and bilingual review evidence are included beside this report. Original approval records, learner records, completion policies and scoring are preserved. Foundations remains quiz-only completion; its Toolkit is optional.

No live deployment, real learner mutation, email send or valid certificate issuance occurred. Fady is the assigned Sorani, Arabic-addition and clinical reviewer. Before publication, record his completed review, review translated legal text, then approve the exact candidate and target deployment. Integration must compare current upstream work again.
