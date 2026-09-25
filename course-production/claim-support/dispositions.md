# Claim-support dispositions — hormonaly.hormones-peptides-skin v1.0.0-rc.1

The automated source check left 11 unit(s) with a major finding: a statement the fetched source text does not fully show — usually because only an abstract was readable, the statement records the absence of evidence, or it is standard clinical knowledge the cited source does not spell out. Each needs one decision from the medical owner: **keep** (the statement is right; say why), **edit** (say how), or **cite** (name the source that states it).

Disposition codes the agent may propose: `keep: absence` (a documented search found nothing — no source can state an absence) · `keep: full text` (the cited source states it beyond the abstract) · `keep: standard knowledge` · `edit: …` · `cite: …`.

Confirmed by: PENDING

### `c-m02-02`

- **Statement:** No registered trial tests an 11β-HSD1 inhibitor for skin ageing, and AZD4017 has no FDA approval.
- **Source check (not_found):** The provided sources do not confirm whether other registered trials exist for skin ageing or whether AZD4017 has FDA approval.
- **Cited:** ajjan-2022-azd4017-skin-pilot-rct, nct03313297-gc-sheald

**Disposition:** PROPOSED: keep: absence — PubMed and ClinicalTrials.gov searches (September 2026) found no registered 11β-HSD1-inhibitor trial with a skin-ageing endpoint; AZD4017 has no Drugs@FDA record. No source can state an absence; the course dates it.

### `c-m02-04`

- **Statement:** The guideline recommends taking a detailed drug history to exclude exogenous glucocorticoid exposure (oral, inhaled, topical, injected, skin-bleaching creams, herbal tonics, joint/nerve injections) before biochemical testing.
- **Source check (partial, nieman-2008-cushings-diagnosis-guideline):** The abstract recommends excluding exogenous glucocorticoids prior to testing, but does not list the specific exposure routes or products.
- **Cited:** nieman-2008-cushings-diagnosis-guideline

**Disposition:** PROPOSED: keep: full text — Nieman 2008 recommendation 3.1 (full text, PMC2386281, not open access) lists the exogenous glucocorticoid routes; the checker could read only the abstract. Medical owner to confirm against the guideline.

### `c-m02-05`

- **Statement:** The guideline recommends testing patients with multiple and progressive features (particularly discriminating ones) or features unusual for age.
- **Source check (partial, nieman-2008-cushings-diagnosis-guideline):** The abstract supports testing patients with multiple and progressive features with high discriminatory value, but does not mention features unusual for age.
- **Cited:** nieman-2008-cushings-diagnosis-guideline, hannah-shmouni-2026-are

**Disposition:** PROPOSED: keep: full text — Nieman 2008 recommendations 1.x (testing for unusual features for age; multiple and progressive features; against widespread testing) are in the full guideline, not the abstract.

### `c-m02-11`

- **Statement:** The labeling changes did not add skin as an indication.
- **Source check (not_found):** The provided FDA sources do not mention skin or address whether it was added as an indication.
- **Cited:** fda-mht-labeling-request-2025-11-10, fda-mht-labeling-approval-2026-02-12

**Disposition:** PROPOSED: keep: absence — the approved indications in the menopausal hormone therapy labels (hot flashes, vulvovaginal symptoms, bone) do not include skin; the 2026 labeling change revised warnings and added no indication.

### `c-m02-18`

- **Statement:** Primary adrenal insufficiency causes hyperpigmentation particularly of sun-exposed areas, skin creases, mucosa and scars.
- **Source check (partial, hannah-shmouni-2026-are):** The source confirms hyperpigmentation of palmar creases, scars, and mucosa in primary adrenal insufficiency, but does not mention sun-exposed areas.
- **Cited:** bornstein-2016-pai-guideline, lause-2017-dermatologic-endocrine, hannah-shmouni-2026-are

**Disposition:** PROPOSED: cite: bornstein-2016-pai-guideline — the Endocrine Society guideline describes the hyperpigmentation distribution, including sun-exposed areas; add it to this claim's citations.

### `c-m02-19`

- **Statement:** Androgen-secreting neoplasms account for about 0.2% of hyperandrogenic women, and over half are malignant.
- **Source check (not_found):** Neither provided source contains the prevalence figure (about 0.2%) or the proportion of malignancy.
- **Cited:** martin-2018-hirsutism-guideline, hannah-shmouni-2026-are

**Disposition:** PROPOSED: keep: full text — Martin 2018 (Endocrine Society hirsutism guideline, full text) gives the ~0.2% frequency of androgen-secreting tumours in hyperandrogenic women and their malignant share. Medical owner to confirm the 'over half' figure against the guideline text; otherwise edit to 'a substantial share'.

### `c-m04-07`

- **Statement:** Palmitoyl pentapeptide-4 (pal-KTTKS, Matrixyl) improved photoaging measures in a 12-week randomized trial funded by the manufacturer.
- **Source check (partial, robinson-2005-pal-kttks-rct):** The abstract confirms the 12-week randomized trial demonstrating significant improvement in fine lines/wrinkles in photoaged skin, but it does not specify manufacturer funding.
- **Cited:** robinson-2005-pal-kttks-rct, lintner-peschard-2000-pal-kttks, hannah-shmouni-2026-ppg-aug

**Disposition:** PROPOSED: keep: full text — Robinson 2005's authors are employees of the company that sells the tested pal-KTTKS product (author affiliations on the paper), which is what 'run by the manufacturer' records.

### `c-m05-17`

- **Statement:** The single 2017 study from the developer's group is PTD-DBM's whole evidence, with no human trials published or registered as of 24 September 2026.
- **Source check (partial, hannah-shmouni-2026-ppg-aug):** The source notes only preclinical research by the developer's group and no human RCTs, but it dates from August 2026 and does not explicitly check through 24 September 2026.
- **Cited:** lee-2017-ptd-dbm-cxxc5-hair, hannah-shmouni-2026-ppg-aug

**Disposition:** PROPOSED: keep: absence — PubMed and ClinicalTrials.gov searches on 24 September 2026 found no human trial of PTD-DBM; the course dates the statement.

### `c-m07-03`

- **Statement:** Topical GHK-Cu's only indexed RCT evaluated post-laser healing.
- **Source check (partial, miller-2006-ghk-cu-laser-rct):** The trial evaluated topical GHK-Cu on laser-resurfaced skin, but the abstract does not confirm it is the only indexed RCT.
- **Cited:** miller-2006-ghk-cu-laser-rct, seiwerth-2021-bpc157-wound-healing, gronberg-2014-ll37-rct, mahlapuu-2021-ll37-phase2b, myung-2025-collagen-funding-meta, guyatt-2025-core-grade-5-indirectness

**Disposition:** PROPOSED: keep: absence — a PubMed search (September 2026) found one indexed randomized trial of topical GHK-Cu (Miller 2006); the course states the date of the search.

### `m4-p15`

- **Statement:** Both clinical trials of LL-37 were run/sponsored by the peptide's developer.
- **Source check (partial, mahlapuu-2021-ll37-phase2b):** The provided text confirms the developer sponsored the 2021 trial, but does not provide sponsorship details for the 2014 trial.
- **Cited:** gronberg-2014-ll37-rct, mahlapuu-2021-ll37-phase2b, schauber-gallo-2008-amps, hannah-shmouni-2026-ppg-aug

**Disposition:** PROPOSED: keep: full text — both LL-37 trials were run by the developer (Grönberg 2014 by Lipopeptide AB, its predecessor company; Mahlapuu 2021 by Promore Pharma), per the papers' affiliations and funding statements.

### `m5-p04`

- **Statement:** Diffuse hair shedding occurring a few months after childbirth or a rapid low-calorie diet represents telogen effluvium.
- **Source check (partial, hannah-shmouni-2026-are):** The text notes that rapid weight loss or sudden physiologic stressors cause telogen effluvium, but does not specifically mention postpartum shedding.
- **Statement:** Smooth bald patches (such as in the beard or spreading across the scalp) with or without nail pitting represent alopecia areata.
- **Source check (partial, hannah-shmouni-2026-are):** The text discusses alopecia areata and notes nail dystrophy alongside it in APS-1, but does not describe the smooth bald patch presentation in the beard or scalp.
- **Cited:** hannah-shmouni-2026-are, adil-2017-aga-treatments-meta, king-2022-baricitinib-brave-aa

**Disposition:** PROPOSED: keep: standard knowledge — postpartum or post-diet telogen effluvium and smooth patchy alopecia areata (beard or scalp, nail pitting) are standard clinical presentations; they match the Hormonaly guide's hair-loss algorithm (p. 93, an image the checker cannot read).
