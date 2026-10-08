# Homepage language previews — 8 October 2026

The four phone screenshots were English pixels with Arabic captions. This release makes the screenshot itself language-specific and removes the dense clinical-case preview, leaving three items in each language.

Six fresh captures come from the actual current learner runtime at 390 × 844 in isolated local mode. Arabic shows a short practice activity (module 1, pane 5), the skin illustration (module 1, pane 3), and evidence classification (module 4, pane 11). English retains its opening film, science illustration and evidence activity. The Arabic practice caption describes the activity; it does not claim an Arabic film is ready. Proper medicine names and scientific abbreviations retain their source spelling.

The manifest in `presentation-inputs/home-glimpses-bilingual.json` records every capture, locale, source pane, screenshot hash, course digest and brand fingerprint. Preparation now verifies every localized variant, including locale-qualified course filenames. The course package digest remains `9f3f3b47199c7aad43a2e23b30476784c44ed446abfcd64b65d5dd6b2a7b4491`; learner records and clinical course content were not changed.

Local checks: three capture-validation tests pass, including wrong-language and changed-image rejection; application and server type checks pass. Actual browser checks confirm exactly three screenshots, `/ar/` paths when Arabic is selected, `/en/` paths when English is selected, all images loaded, and no document horizontal overflow at 390px. Desktop RTL rendering was visually inspected at 1280px. All eight canonical deployment evaluation suites passed.

Runtime commits: `8b0e8e8`, `d25331f`. Foundry workflow correction: `9f3e8bc`. Hosted proof follows after candidate verification and promotion.
