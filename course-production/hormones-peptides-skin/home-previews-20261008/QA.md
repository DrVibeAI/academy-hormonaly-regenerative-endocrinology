# Homepage language previews — 8 October 2026

The four phone screenshots were English pixels with Arabic captions. This release makes the screenshot itself language-specific and removes the dense clinical-case preview, leaving three items in each language.

Six fresh captures come from the actual current learner runtime at 390 × 844 in isolated local mode. Arabic shows a short practice activity (module 1, pane 5), the skin illustration (module 1, pane 3), and evidence classification (module 4, pane 11). English retains its opening film, science illustration and evidence activity. The Arabic practice caption describes the activity; it does not claim an Arabic film is ready. Proper medicine names and scientific abbreviations retain their source spelling.

The manifest in `presentation-inputs/home-glimpses-bilingual.json` records every capture, locale, source pane, screenshot hash, course digest and brand fingerprint. Preparation now verifies every localized variant, including locale-qualified course filenames. The course package digest remains `9f3f3b47199c7aad43a2e23b30476784c44ed446abfcd64b65d5dd6b2a7b4491`; learner records and clinical course content were not changed.

Local checks: three capture-validation tests pass, including wrong-language and changed-image rejection; application and server type checks pass. Actual browser checks confirm exactly three screenshots, `/ar/` paths when Arabic is selected, `/en/` paths when English is selected, all images loaded, and no document horizontal overflow at 390px. Desktop RTL rendering was visually inspected at 1280px. All eight canonical deployment evaluation suites passed.

Runtime commits: `8b0e8e8`, `d25331f`. Foundry workflow correction: `9f3e8bc`. Academy capture/config commit: `353880d`.

Published via canonical candidate-only deployment and exact-revision promotion: `academy-hormonaly-00056-kgf`, 100% traffic. Cloud Build `fa8200d2-1315-4e2a-8ae2-67bc038b3df6` completed successfully. Candidate browser checks verified three loaded Arabic images, correct English switching, RTL, and no document overflow at 390px. Authenticated candidate checks retained 54 enrolled/started learners, one certificate, three editor proposals, seven messages and five releases. No assistant mutation was requested. Production verification confirms three loaded Arabic images and certificate API 401 without authentication. All six published screenshot bytes match their recorded SHA-256 hashes.

See `production-arabic-previews.png`, `production-traffic.json`, `candidate-arabic-proof.json`, `candidate-admin-proof.json` and `published-image-proof.json`. Prepared deployment: `/Users/omar/DrVibe/releases/hormonaly-home-previews-20261008`. Temporary local servers and the capture browser tab were closed after verification.
