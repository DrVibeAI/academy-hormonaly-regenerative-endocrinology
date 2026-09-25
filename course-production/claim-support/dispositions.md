# Claim-support dispositions — hormonaly.hormones-peptides-skin v1.0.0

The automated source check left 19 unit(s) with a major finding: a statement the fetched source text does not fully show — usually because only an abstract was readable, the statement records the absence of evidence, or it is standard clinical knowledge the cited source does not spell out. Each needs one decision from the medical owner: **keep** (the statement is right; say why), **edit** (say how), or **cite** (name the source that states it).

Disposition codes the agent may propose: `keep: absence` (a documented search found nothing — no source can state an absence) · `keep: full text` (the cited source states it beyond the abstract) · `keep: standard knowledge` · `edit: …` · `cite: …`.

Confirmed by: Fady Hannah-Shmouni, MD FRCPC, 2026-09-25 (rc.2 sign-off packet; relayed by Omar Saleem)

### `j-br-23`

- **Statement:** Thymus-derived immunomodulators containing other active ingredients (thymomodulin, Leucogen, thymostimulin) hold active registrations in ANVISA's register.
- **Source check (partial, br-anvisa-register-opendata):** The dataset confirms an active registration for Leucogen (thymomodulin) as an immunomodulator, but does not mention thymostimulin.
- **Cited:** br-anvisa-register-opendata, br-anvisa-register-dictionary

**Disposition:** CONFIRMED as proposed: keep: full text + keep: absence — ANVISA's open-data register (DADOS_ABERTOS_MEDICAMENTOS.csv, read 25 Sep 2026, all ~43,500 rows; the checker reads a 60,000-character excerpt of the 8.3-million-character file) lists thymostimulin as the active substance of EXTRATO DE CÉLULAS TÍMICAS, registration 117290005, status Ativo (row now quoted in jurisdictions/BR.json), and Leucogen (thymomodulin) as Ativo; no row names thymulin. The learner note names only thymomodulin.

### `c-m02-02`

- **Statement:** No registered trial tests an 11β-HSD1 inhibitor for skin ageing, and AZD4017 has no FDA approval.
- **Source check (not_found):** The provided sources do not confirm whether other registered trials exist for skin ageing or whether AZD4017 has FDA approval.
- **Cited:** ajjan-2022-azd4017-skin-pilot-rct, nct03313297-gc-sheald

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: absence — PubMed and ClinicalTrials.gov searches (September 2026) found no registered 11β-HSD1-inhibitor trial with a skin-ageing endpoint; AZD4017 has no Drugs@FDA record. No source can state an absence; the course dates it.

### `c-m02-04`

- **Statement:** The guideline recommends taking a detailed drug history to exclude exogenous glucocorticoid exposure (oral, inhaled, topical, injected, skin-bleaching creams, herbal tonics, joint/nerve injections) before biochemical testing.
- **Source check (partial, nieman-2008-cushings-diagnosis-guideline):** The abstract recommends excluding exogenous glucocorticoids prior to testing, but does not list the specific exposure routes or products.
- **Cited:** nieman-2008-cushings-diagnosis-guideline

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: full text — Nieman 2008 recommendation 3.1 (full text, PMC2386281, not open access) lists the exogenous glucocorticoid routes; the checker could read only the abstract. Medical owner to confirm against the guideline.

### `c-m02-05`

- **Statement:** The guideline recommends testing patients with multiple and progressive features (particularly discriminating ones) or features unusual for age.
- **Source check (partial, nieman-2008-cushings-diagnosis-guideline):** The abstract supports testing patients with multiple and progressive features with high discriminatory value, but does not mention features unusual for age.
- **Cited:** nieman-2008-cushings-diagnosis-guideline, hannah-shmouni-2026-are

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: full text — Nieman 2008 recommendations 1.x (testing for unusual features for age; multiple and progressive features; against widespread testing) are in the full guideline, not the abstract.

### `c-m02-11`

- **Statement:** The labeling changes did not add skin as an indication.
- **Source check (not_found):** The provided FDA sources do not mention skin or address whether it was added as an indication.
- **Cited:** fda-mht-labeling-request-2025-11-10, fda-mht-labeling-approval-2026-02-12

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: absence — the approved indications in the menopausal hormone therapy labels (hot flashes, vulvovaginal symptoms, bone) do not include skin; the 2026 labeling change revised warnings and added no indication.

### `c-m02-18`

- **Statement:** Primary adrenal insufficiency causes hyperpigmentation particularly of sun-exposed areas, skin creases, mucosa and scars.
- **Source check (partial, hannah-shmouni-2026-are):** The source confirms hyperpigmentation of palmar creases, scars, and mucosa in primary adrenal insufficiency, but does not mention sun-exposed areas.
- **Cited:** bornstein-2016-pai-guideline, lause-2017-dermatologic-endocrine, hannah-shmouni-2026-are

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: full text — the claim already cites the Endocrine Society guideline (Bornstein 2016), whose full text describes the hyperpigmentation distribution, including sun-exposed areas; the checker could read only its abstract.

### `c-m02-19`

- **Statement:** Androgen-secreting neoplasms account for about 0.2% of hyperandrogenic women, and over half are malignant.
- **Source check (not_found):** Neither provided source contains the prevalence figure (about 0.2%) or the proportion of malignancy.
- **Cited:** martin-2018-hirsutism-guideline, hannah-shmouni-2026-are

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: full text — Martin 2018 (Endocrine Society hirsutism guideline, full text) gives the ~0.2% frequency of androgen-secreting tumours in hyperandrogenic women and their malignant share. Medical owner to confirm the 'over half' figure against the guideline text; otherwise edit to 'a substantial share'.

### `c-m04-07`

- **Statement:** Palmitoyl pentapeptide-4 (pal-KTTKS, Matrixyl) improved photoaging measures in a 12-week randomized trial funded by the manufacturer.
- **Source check (partial, robinson-2005-pal-kttks-rct):** The abstract confirms the 12-week randomized trial demonstrating significant improvement in fine lines/wrinkles in photoaged skin, but it does not specify manufacturer funding.
- **Cited:** robinson-2005-pal-kttks-rct, lintner-peschard-2000-pal-kttks, hannah-shmouni-2026-ppg-aug

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: full text — Robinson 2005's authors are employees of the company that sells the tested pal-KTTKS product (author affiliations on the paper), which is what 'run by the manufacturer' records.

### `c-m05-17`

- **Statement:** The single 2017 study from the developer's group is PTD-DBM's whole evidence, with no human trials published or registered as of 24 September 2026.
- **Source check (partial, hannah-shmouni-2026-ppg-aug):** The source notes only preclinical research by the developer's group and no human RCTs, but it dates from August 2026 and does not explicitly check through 24 September 2026.
- **Cited:** lee-2017-ptd-dbm-cxxc5-hair, hannah-shmouni-2026-ppg-aug

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: absence — PubMed and ClinicalTrials.gov searches on 24 September 2026 found no human trial of PTD-DBM; the course dates the statement.

### `c-m07-03`

- **Statement:** Topical GHK-Cu's only indexed RCT evaluated post-laser healing.
- **Source check (partial, miller-2006-ghk-cu-laser-rct):** The trial evaluated topical GHK-Cu on laser-resurfaced skin, but the abstract does not confirm it is the only indexed RCT.
- **Cited:** miller-2006-ghk-cu-laser-rct, seiwerth-2021-bpc157-wound-healing, gronberg-2014-ll37-rct, mahlapuu-2021-ll37-phase2b, myung-2025-collagen-funding-meta, guyatt-2025-core-grade-5-indirectness

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: absence — a PubMed search (September 2026) found one indexed randomized trial of topical GHK-Cu (Miller 2006); the course states the date of the search.

### `m3-p08›metadata.variants.jurisdiction.BR`

- **Statement:** Since 23 June 2025, GLP-1 receptor agonist medicines may only be sold with retention of the prescription under RDC 973/2025 and IN 360/2025.
- **Source check (partial, br-anvisa-semaglutide-synthetic-2026):** The requirement for retention of prescription for GLP-1 receptor agonists is supported, but the specific effective date (23 June 2025) and regulation numbers (RDC 973/2025, IN 360/2025) are not contained in the readable sources.
- **Cited:** br-label-ozempic, br-anvisa-register-opendata, br-label-wegovy, br-anvisa-semaglutide-synthetic-2026, br-anvisa-semaglutide-five-2026, br-anvisa-consultas-medicamentos, br-label-mounjaro, br-anvisa-glp1-qa-2025, br-anvisa-glp1-retention-2025

**Disposition:** CONFIRMED as proposed: keep: full text + keep: absence — ANVISA's GLP-1 questions-and-answers page (br-anvisa-glp1-qa-2025), which the checker could not fetch, reads: 'A Instrução Normativa-IN nº 360 e a Resolução da Diretoria Colegiada - RDC nº 973 foram publicadas em 24 de abril de 2025, e entrarão em vigor 60 (sessenta) dias após essa data. Assim, as novas medidas relativas aos agonistas do receptor GLP-1 passarão a valer a partir de 23 de junho de 2025.' (verbatim, jurisdictions/BR.json). No row of ANVISA's register file names Zepbound (search 25 Sep 2026); Mounjaro and Mounjaro Multidose are listed.

### `m4-p05›metadata.variants.jurisdiction.GB`

- **Statement:** In the UK, a GHK-Cu serum sold for appearance is classified as a cosmetic product.
- **Source check (partial, uk-cosmetics-reg-1223-2009-art2):** The regulation defines cosmetic products as any substance or mixture applied externally to change appearance, but does not specifically mention GHK-Cu.
- **Cited:** uk-cosmetics-reg-1223-2009-art2, mhra-gn8-medicinal-product-2025

**Disposition:** CONFIRMED as proposed: keep: definition applied — the cited definition (Regulation 1223/2009 art. 2(1)(a), as it applies in Great Britain) makes a product a cosmetic by where it is applied (the external parts of the body) and what it is for (including changing appearance); the note applies it only to a topical GHK-Cu serum sold for appearance, and MHRA Guidance Note 8 (cited) marks where a product becomes a medicine. No source names GHK-Cu, and none needs to.

### `m4-p15`

- **Statement:** Both clinical trials of LL-37 were run/sponsored by the peptide's developer.
- **Source check (partial, mahlapuu-2021-ll37-phase2b):** The provided text confirms the developer sponsored the 2021 trial, but does not provide sponsorship details for the 2014 trial.
- **Cited:** gronberg-2014-ll37-rct, mahlapuu-2021-ll37-phase2b, schauber-gallo-2008-amps, hannah-shmouni-2026-ppg-aug

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: full text — both LL-37 trials were run by the developer (Grönberg 2014 by Lipopeptide AB, its predecessor company; Mahlapuu 2021 by Promore Pharma), per the papers' affiliations and funding statements.

### `m5-p04`

- **Statement:** Diffuse hair shedding occurring a few months after childbirth or a rapid low-calorie diet represents telogen effluvium.
- **Source check (partial, hannah-shmouni-2026-are):** The text notes that rapid weight loss or sudden physiologic stressors cause telogen effluvium, but does not specifically mention postpartum shedding.
- **Statement:** Smooth bald patches (such as in the beard or spreading across the scalp) with or without nail pitting represent alopecia areata.
- **Source check (partial, hannah-shmouni-2026-are):** The text discusses alopecia areata and notes nail dystrophy alongside it in APS-1, but does not describe the smooth bald patch presentation in the beard or scalp.
- **Cited:** hannah-shmouni-2026-are, adil-2017-aga-treatments-meta, king-2022-baricitinib-brave-aa

**Disposition:** CONFIRMED for rc.1 (Fady Hannah-Shmouni, 2026-09-25), unit unchanged in rc.2 — keep: standard knowledge — postpartum or post-diet telogen effluvium and smooth patchy alopecia areata (beard or scalp, nail pitting) are standard clinical presentations; they match the Hormonaly guide's hair-loss algorithm (p. 93, an image the checker cannot read).

### `m5-p08`

- **Statement:** The Peptide Pocket Guide rates Melanotan II C and the Aesthetic & Regenerative Endocrinology guide rates it D.
- **Source check (partial, hannah-shmouni-2026-are):** The Aesthetic & Regenerative Endocrinology guide rates Melanotan II D, but the Peptide Pocket Guide excerpt does not contain a Grade C rating for it.
- **Cited:** langendonk-2015-afamelanotide-epp, ema-scenesse-epar, fda-scenesse-label-2024, dorr-1996-melanotan-ii-pilot, wessells-1998-melanotan-ii-ed, bohm-2025-mc1r-activation-review, nct06109649-scenesse-vitiligo, hannah-shmouni-2026-ppg-aug, hannah-shmouni-2026-are

**Disposition:** CONFIRMED as proposed: keep: full text — the Peptide Pocket Guide (August 2026) grades Melanotan II C: its contents list ('Melanotan II · GRADE C') and the monograph header on p. 73 ('GRADE C · NON-SELECTIVE MELANOCORTIN AGONIST'); the checker's 60,000-character excerpt of the 256,000-character guide missed that page. The Aesthetic & Regenerative Endocrinology guide's D is the quote the checker found.

### `m5-p12›metadata.variants.jurisdiction.BR`

- **Statement:** Under Law 6.360/1976, no product covered by the law, including an imported one, may be manufactured, offered for sale or supplied for consumption before being registered with the Ministry of Health.
- **Source check (not_found):** The cited text of Law 6.360/1976 is unavailable in the provided sources.
- **Cited:** br-anvisa-register-opendata, br-anvisa-register-dictionary, br-anvisa-consultas-medicamentos, br-lei-6360-1976

**Disposition:** CONFIRMED as proposed: keep: full text + keep: absence — Law 6.360/1976 art. 12 (planalto.gov.br, which the checker could not fetch) reads: 'Art. 12 - Nenhum dos produtos de que trata esta Lei, inclusive os importados, poderá ser industrializado, exposto à venda ou entregue ao consumo antes de registrado no Ministério da Saúde.' (verbatim, jurisdictions/BR.json). No row of ANVISA's register file names melanotan (search 25 Sep 2026).

### `m5-p17`

- **Statement:** Both thymulin and PTD-DBM carry Grade D evidence.
- **Source check (partial, hannah-shmouni-2026-ppg-aug):** The pocket guide rates Zinc Thymulin as Grade D, but PTD-DBM is not mentioned in the provided excerpts.
- **Cited:** fda-503a-categories-2026-05-14, fda-503a-bulks-page, ecfr-21-cfr-216-23-bulks-list, hannah-shmouni-2026-ppg-aug, adil-2017-aga-treatments-meta

**Disposition:** CONFIRMED as proposed: keep: full text — the Peptide Pocket Guide grades PTD-DBM D (monograph p. 59, 'GRADE D · CELL-PENETRATING WNT-PATHWAY ACTIVATOR') and zinc thymulin D (p. 61); the checker's excerpt held only the thymulin page (its re-check of c-m05-17 finds PTD-DBM's D).

### `m7-p21›metadata.variants.jurisdiction.PT`

- **Statement:** INFARMED may authorise exceptional use (AUE) of a medicine without a marketing authorisation when clinically justified as indispensable and no authorised alternative exists.
- **Source check (partial, pt-infarmed-aue):** The source confirms INFARMED can authorise exceptional use (AUE) under DL 176/2006, but the consolidated statute text defining clinical indispensability is unavailable.
- **Cited:** pt-infarmed-circ148-2011, pt-dl176-2006, pt-infarmed-aue, pt-dl95-2004, pt-infarmed-manipulados

**Disposition:** CONFIRMED as proposed: keep: full text — Decreto-Lei 176/2006 (Estatuto do Medicamento) art. 92(1)(a), whose consolidated text on diariodarepublica.pt the checker could not fetch, reads: 'O INFARMED, I.P., pode autorizar a utilização em Portugal de medicamento não possuidor de qualquer das restantes autorizações previstas no presente decreto-lei … a) Mediante justificação clínica, sejam considerados imprescindíveis à prevenção, diagnóstico ou tratamento de determinadas patologias, desde que seja demonstrada a inexistência de alternativa no conjunto de medicamentos com autorização de introdução no mercado' (verbatim, jurisdictions/PT.json); INFARMED's AUE page (cited, read by the checker) confirms the AUE under article 92.

### `m7-p15›metadata.variants.jurisdiction.PT`

- **Statement:** INFARMED may authorise exceptional use (AUE) of a medicine without a marketing authorisation, for example when it is clinically justified as indispensable and no authorised alternative exists.
- **Source check (partial, pt-infarmed-aue):** The source confirms that INFARMED grants exceptional use authorisations (AUE) and mentions situations without therapeutic alternatives, but the specific criterion of being clinically indispensable is not detailed in the text.
- **Cited:** pt-dl176-2006, pt-infarmed-aue

**Disposition:** CONFIRMED as proposed: keep: full text — the same Decreto-Lei 176/2006 art. 92(1)(a) text as m7-p21 (PT) above.
