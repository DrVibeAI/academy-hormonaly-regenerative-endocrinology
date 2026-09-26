# Agent pre-review — Hormones and Peptides for Skin (v1.0.0)

*Agent pre-review. Recommendation only — the GCLS board decides. Model gemini-3.8-flash, 2026-09-26. Package sha256 efe7c2d2f301.*

**Recommendation: accredit with conditions** (confidence high) · human time needed ≈ 20 min

This course provides continuing professional education for licensed medical clinicians and aesthetic providers on cutaneous endocrinology, peptide therapeutics, and regulatory governance across six jurisdictions. It systematically bridges basic cutaneous biology with clinical evidence for hormones, incretin-driven facial volume changes, cosmeceutical peptides, and growth-hormone secretagogues. The instructional approach contrasts biological plausibility with rigorous human outcome trials while emphasizing statutory compounding limitations and prescribing compliance. The tone is objective, clinically disciplined, and meticulous about jurisdictional boundaries.

## Conditions
- Verify and supply primary literature citations for the epidemiological claims in claim c-m02-19 regarding the 0.2% prevalence and >50% malignancy rate of androgen-secreting neoplasms, or temper the numerical assertion in block m2-p15.
- Formulate the negative literature search finding in claim c-m02-02 (regarding lack of registered trials for 11beta-HSD1 inhibitors in skin aging) as an explicit methodological search note rather than citing Ajjan 2022 directly for a document-wide absence.
- Ensure that post-PCAC July 2026 notes in Module 04 and Module 07 explicitly reiterate that advisory committee recommendations do not permit 503A compounding prior to formal final rulemaking in 21 CFR 216.23.

## Look at these first
1. **c-m02-19** — Claim support search marked searchedWholeDocument for Martin 2018 and found neither the 0.2% prevalence of androgen-secreting neoplasms nor the >50% malignancy rate in the cited text. (~6 min)
2. **c-m02-02** — Claim support search confirmed searchedWholeDocument on Ajjan 2022 and NCT03313297: the statement that no registered trial tests an 11beta-HSD1 inhibitor for skin aging is not substantiated within the locked source. (~5 min)
3. **m7-p08** — Verify the exact current status of withdrawn 503A bulk substances (BPC-157, TB-500, KPV) against live FDA category listings and rulemaking dockets. (~5 min)
4. **j-br-23** — ANVISA register source support was partial: Leucogen (thymomodulin) is confirmed, but thymostimulin registration remains unverified in the provided records. (~4 min)

## Risks (3)
- ⚠️ **major · evidence** @ c-m02-19: The specific statistical claim that androgen-secreting neoplasms occur in ~0.2% of hyperandrogenic women and that over half are malignant could not be located in Martin 2018 (marked not_found with searchedWholeDocument). → *Cite the primary epidemiological paper from which the Endocrine Society guideline derived the 0.2% and >50% malignancy figures, or qualify the statement as an estimate from specialist reviews.*
- · **minor · evidence** @ c-m02-02: The claim that no registered trial tests an 11beta-HSD1 inhibitor for skin aging is an external negative search finding not contained in the cited trial report (Ajjan 2022) or registry entry (NCT03313297). → *Formulate as an independent registry search note with exact date and parameters: 'A search of ClinicalTrials.gov on 24 September 2026 identified no registered trial testing 11beta-HSD1 inhibitors for skin aging.'*
- · **minor · regulatory** @ m7-p08: Discussion of the July 2026 PCAC advisory committee meeting for BPC-157, KPV, and TB-500 reports non-binding advisory votes that must not be misconstrued by learners as completed rulemaking. → *Maintain prominent callouts in lesson 7.2 that advisory committee recommendations do not alter the codified 21 CFR 216.23 bulks list until a final rule is promulgated.*

## Claims (13)
- `c-m01-01` **supported as cited** — Verified against Slominski 2025 and Hannah-Shmouni 2026: describes the skin as a neuro-immuno-endocrine organ structured into four regulatory units.
- `c-m01-09` **plausible needs source check** — Fei 2026 abstract confirms 379 hormone/receptor genes across 14 million cells and 47 tissues, but inclusion of skin was verified via portal landing page rather than full-text inspection.
- `c-m02-02` **unsupported** — Assertion that no registered trial tests 11beta-HSD1 inhibition for skin aging is not found in Ajjan 2022 or NCT03313297, which were searched in full (searchedWholeDocument).
- `c-m02-19` **unsupported** — Prevalence figure (0.2% of hyperandrogenic women) and malignancy rate (>50%) for androgen-secreting neoplasms were not found in Martin 2018 despite full-document search.
- `c-m03-09` **supported as cited** — FDA package inserts (Wegovy, Ozempic, Mounjaro, Zepbound) and Drugs@FDA histories mechanically verify approved indications and absence of cutaneous/facial indications.
- `c-m04-06` **supported as cited** — FDA 503A category list (14 May 2026) verifies Category 1 non-injectable status and exclusion of injectable routes for GHK-Cu.
- `c-m05-04` **supported as cited** — King 2022 and FDA supplemental approval letter verify baricitinib phase 3 BRAVE-AA trial endpoints, sample sizes, and approval date for severe alopecia areata.
- `c-m06-08` **supported as cited** — 21 U.S.C. 333(e) statutory text verifies criminal prohibition against distributing human growth hormone for unauthorized indications.
- `c-m07-06` **supported as cited** — 21 U.S.C. 353a statutory text and FDA 503A guidance verify the three-tiered hierarchical qualification for bulk compounding substances and CoA mandate.
- `j-ae-02` **supported as cited** — EDE news announcement of 1 June 2026 verifies approval of oral Wegovy for long-term weight management as the second country globally.
- `j-ae-04` **supported as cited** — MOHAP Circular 9217/2024 passage verifies genuine Mounjaro registration status and dual diabetes/weight-management indication.
- `j-ae-01` **plausible needs source check** — Registration numbers are plausible, but register verification was limited by an unreadable product detail page and an excerpted directory landing page.
- `j-br-23` **plausible needs source check** — DATAVISA open data extract confirmed active registration for Leucogen (thymomodulin), but thymostimulin was not located in the provided extract.

## Modules
- **m01** [skim] Establishes cutaneous neuro-immuno-endocrinology, steroidogenic capacity, single-cell atlas transcriptomic limits, and cellular senescence biology.
- **m02** [verify] Contrasts cutaneous 11beta-HSD1 cortisol generation with Cushing's syndrome, appraises postmenopausal HRT trials, and details syndromic dermatologic flags.
- **m03** [skim] Details dermal white adipose physiology, glycation biochemistry, incretin weight-loss trials, 'Ozempic face' fat deflation, and gut-skin barrier evidence.
- **m04** [verify] Critiques topical vs injectable GHK-Cu, matrikines, oral collagen meta-analyses by funding source, and tissue-repair peptides (BPC-157, TB-500, LL-37).
- **m05** [verify] Covers hair follicle immunology, approved alopecia therapies vs unproven peptides (PTD-DBM), and approved afamelanotide vs illicit Melanotan II risks.
- **m06** [skim] Evaluates GH/IGF-1 dermal-epidermal signaling, somatopause myths, tesamorelin trials, secretagogue compounding status, and oncologic associations.
- **m07** [verify] Instructs on GRADE evidence appraisal, 503A/503B compounding statutes, international unlicensed medicines mechanisms, and CoA auditing.

## Assessment
The 14-question final course quiz directly assesses all four curriculum pillars: cutaneous physiology (36%), evidence appraisal (29%), regulatory safety (29%), and patient communication (7%). Every item has exactly one defensible, evidence-grounded correct option with clear distractors that address common industry misconceptions. Module-level checks and quickfire quizzes consistently reinforce objectives without ambiguity.

## Educational quality
Educational design is exemplary. Learning objectives across all 7 modules are specific, behavioral, and clinically measurable. The curriculum employs an innovative instructional framework that rigorously disentangles four distinct epistemic registers: biological mechanism, human trial evidence, jurisdictional regulatory status, and unresolved empirical questions. Content is dense, rigorous, and free from administrative filler.

## Learning time
≈ 215 min (Calculated independently: 7 module video openers (8.5 minutes total); reading of core lesson prose and comparative tables across 48 interactive moments (~22,000 words at 130 words per minute = 169 minutes); completion of 14 complex scenario-based final quiz items (21 minutes); 7 module check exercises and interactive audits (16.5 minutes).) — credit hours proportionate: yes · Estimated learning time of ~3.6 hours aligns cleanly with the 213-minute planning sum. The package issues an institutional Certificate of Completion without asserting unaccredited CME/CE credit hours, fully complying with accreditation standards.

## Localization
Only the English ('en') locale was requested and delivered. No translated editions are claimed. Jurisdictional variations for the US, UK, EU, Portugal, Brazil, and the UAE are implemented via dedicated, locale-specific regulatory variant blocks referencing primary statutory and regulatory sources from September 2026.
