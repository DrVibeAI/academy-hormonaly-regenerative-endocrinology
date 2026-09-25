# Agent pre-review — Hormones and Peptides for Skin (v0.3.0-full-draft)

*Agent pre-review. Recommendation only — the GCLS board decides. Model gemini-3.8-flash, 2026-09-25. Package sha256 074ac5cc2473.*

**Recommendation: changes requested** (confidence high) · human time needed ≈ 45 min

This course is a comprehensive, advanced continuing education program designed for dermatologists, aesthetic clinicians, nurse practitioners, and allied healthcare providers evaluating hormone and peptide applications in dermatology. It systematically unpacks cutaneous neuro-immuno-endocrinology, steroidogenesis, adipose biology, incretin-driven facial volume changes, hair follicle immunology, melanocortin signaling, the somatotropic axis, and US FDA compounding/regulatory frameworks (503A/503B). Across seven structured modules, it trains clinicians to separate mechanistic biological plausibility from human clinical trial evidence, regulatory standing, and open empirical questions. The tone is rigorous, skeptical, and clinically objective, explicitly rejecting therapeutic overpromising and grounding practice decisions in GRADE methodology.

## Conditions
- Record the medical owner's approval of every module before accreditation; re-run the pre-review after.
- Have Fady Hannah-Shmouni, MD FRCPC confirm the listed changes.

## Look at these first
1. **package.jurisdictions / m3-p09, m4-p11, m5-p12, m5-p17, m6-p12, m7-p01** — The package lists GB (MHRA) alongside the US (FDA) as an active jurisdiction, but multiple module blocks explicitly state that UK/EU regulatory mapping is deferred or in progress. The package must either complete MHRA localization or restrict its scope to the US. (~10 min)
2. **approvals[0] / m4-p14, m4-p04, m4-p09, m4-p17** — Substantive evidence changes were introduced into Module 04 after Dr. Hannah-Shmouni's 2026-09-24 medical review (e.g., removing suspicious 'Hudson Biotech' trials, reclassifying Leuphasyl, and qualifying heavy metal claims), and the approval note explicitly states these await author confirmation. (~10 min)
3. **c-m02-19 / m2-p15** — Claim c-m02-19 states that androgen-secreting neoplasms account for about 0.2% of hyperandrogenic women and that over half are malignant. In claimSupport, this was marked not_found under searchedWholeDocument across both the Martin 2018 guideline and the course spine. (~8 min)
4. **c-m02-02, c-m02-11** — Claims c-m02-02 (lack of registered trials for 11β-HSD1 in skin ageing) and c-m02-11 (FDA MHT labeling changes excluding skin) are marked not_found with searchedWholeDocument in the cited sources. (~7 min)
5. **unreadableSources / fei-2026-hormone-cell-atlas, nieman-2008-cushings-diagnosis-guideline, nams-2022-hormone-therapy-position-statement** — Eleven sources were read only as abstracts or landing pages, preventing mechanical verification of key claims such as Cushing's discriminatory features (Nieman Table 1), NAMS 2022 Level II skin rating, and skin tissue inclusion in the Hormone Cell Atlas. (~10 min)

## Risks (7)
- ⛔ **blocking · medical_safety** @ governance.approvals: Medical review is not recorded for modules 1, 2, 3, 5, 6, 7 (Fady Hannah-Shmouni, MD FRCPC). Their content is a verified AI draft, not a medically approved course. → *Record the medical owner's approval of every module before accreditation; re-run the pre-review after.*
- ⚠️ **major · medical_safety** @ governance.approvals: Module 4 has 6 changes made after Fady Hannah-Shmouni, MD FRCPC's approval that Fady Hannah-Shmouni, MD FRCPC has not yet confirmed. → *Have Fady Hannah-Shmouni, MD FRCPC confirm the listed changes.*
- ⚠️ **major · regulatory** @ package.jurisdictions / m3-p09, m4-p11, m5-p12, m5-p17, m6-p12, m7-p01: The course package registers the United Kingdom (MHRA) as an approved jurisdiction alongside the United States (FDA). However, multiple blocks in modules 03, 04, 05, 06, and 07 explicitly contain placeholder statements indicating that UK and EU regulatory mapping is deferred or incomplete (e.g., 'UK and EU status is being mapped for this course', 'UK and EU mapping for the rest of this course is still in progress'). → *Author and integrate complete MHRA regulatory statuses (e.g., Human Medicines Regulations 2012, unlicensed specials framework, MHRA borderlines policy) for all discussed peptides before claiming GB jurisdiction, or restrict package.jurisdictions strictly to 'US' for this release.*
- ⚠️ **major · evidence** @ approvals[0] / m4-p04, m4-p08, m4-p09, m4-p14, m4-p17: Substantial textual and evidence edits were introduced to Module 04 after medical review sign-off by Dr. Fady Hannah-Shmouni on 2026-09-24, explicitly recorded in the approval notes as 'Changed after this approval, awaiting the approver's confirmation'. Changes include removing two ClinicalTrials.gov records with questionable sponsor legitimacy ('Hudson Biotech'), altering Leuphasyl classifications, and modifying heavy-metal contamination claims. → *Obtain signed re-approval from Dr. Fady Hannah-Shmouni confirming the post-review edits in Module 04 prior to final accreditation.*
- ⚠️ **major · evidence** @ c-m02-19 / m2-p15: Claim c-m02-19 asserts that androgen-secreting neoplasms account for about 0.2% of hyperandrogenic women and that over half are malignant. In mechanical claimSupport checking, this assertion returned not_found with searchedWholeDocument: true across the cited Martin 2018 Endocrine Society guideline and Hannah-Shmouni 2026. → *Replace the quantitative statistic with exact phrasing from the Endocrine Society guideline, or cite the primary epidemiological study (e.g., secondary endocrine neoplasia series) where the 0.2% and >50% malignancy figures originate.*
- · **minor · evidence** @ claimSupport.unreadableSources: Eleven locked sources were flagged as unreadable or checked only as abstracts/landing pages (e.g., fei-2026-hormone-cell-atlas, nieman-2008-cushings-diagnosis-guideline, nams-2022-hormone-therapy-position-statement), leading to multiple 'not_found' assertion statuses for clinical guideline details like Nieman Table 1 Cushing's discriminating features and NAMS Level II evidence ratings. → *Ingest readable open-access PMC full texts or institutional PDFs for Nieman 2008 (PMC2386281) and NAMS 2022 to verify these assertions mechanically.*
- · **minor · scope_creep** @ credential / audience.disclaimers: The course package configures a formal completion certificate co-branded by GCLS and Hormonaly Academy, while the package disclaimers and closing lesson (m7-p20) state: 'Designed toward future CME accreditation. No CME or CE credit is currently offered.' → *Ensure onboarding materials and certificate text make crystal clear that the certificate is an institutional completion credential and carries no CME, CEU, or CPD credit hours.*

## Claims (139)
- `c-m01-01` **supported as cited** — Supported by Slominski 2025 and Hannah-Shmouni 2026; establishes the skin as a peripheral neuro-immuno-endocrine organ with four regulatory units.
- `c-m01-02` **supported as cited** — Supported by Slominski 2013, Zouboulis 2004, and Hannah-Shmouni 2026; enzymatic machinery (CYP11A1, 11β-HSD1, 5α-reductase, aromatase) verified.
- `c-m01-03` **supported as cited** — Supported by Ito 2005; human hair follicles operate an autonomous HPA-like feedback loop ex vivo.
- `c-m01-04` **supported as cited** — Supported by Phan 2021; murine Cyp11b1 knockout demonstrates keratinocyte-derived glucocorticoid control of skin immune tone.
- `c-m01-05` **supported as cited** — Supported by Mancino 2021 and Hannah-Shmouni 2026; cutaneous thyroid and somatotropic loop data verified.
- `c-m01-06` **supported as cited** — Supported by Holick 1980 and Bikle 2014; skin synthesis of previtamin D3 and systemic activation verified.
- `c-m01-07` **supported as cited** — Supported by Slominski 2013 and Zouboulis 2004; skin contribution to systemic circulating androgens/estrogens verified.
- `c-m01-08` **supported as cited** — Supported by Hannah-Shmouni 2026 and Safer 2011; systemic manifestations of cortisol and thyroid disease on skin verified.
- `c-m01-09` **plausible needs source check** — Fei 2026 was checked as an abstract only; while 379 genes and 14 million cells are verified, skin inclusion is not explicitly stated in the abstract text.
- `c-m01-10` **supported as cited** — Supported by the Hormone Cell Atlas portal statement and Liu 2016; atlas predictions are putative/hypothesis-generating and transcript levels do not guarantee protein secretion.
- `c-m01-11` **supported as cited** — Supported by Hannah-Shmouni 2026; inference that skin is one of the largest distributed endocrine networks is presented accurately as a hypothesis-generating deduction.
- `c-m01-12` **supported as cited** — Supported by Hannah-Shmouni 2026; native receptor activation and enzymatic modification of local potency verified.
- `c-m01-13` **supported as cited** — Supported by Neale 2019; artificial UV blocks vitamin D synthesis while field trials of moderate-SPF sunscreen showed no 25(OH)D drop.
- `c-m01-14` **supported as cited** — Supported by Coppé 2008 and Wang & Dreesen 2018; permanent growth arrest and SASP secretome characterization verified.
- `c-m01-15` **supported as cited** — Supported by Ressler 2006 and Wang & Dreesen 2018; p16 accumulation in epidermis/dermis and lack of universal marker verified.
- `c-m01-16` **supported as cited** — Supported by Waaijer 2016; 178-subject Leiden Longevity Study association between p16 counts, wrinkles, and 3-year perceived age verified.
- `c-m01-17` **plausible needs source check** — Abstract-only check for Varani 2006 and Fisher 2009; mechanistic collagen fragmentation and MMP-1 feedback verified, but the qualifying clause on living skin senescent cell causality was not in the abstracts.
- `c-m01-18` **supported as cited** — Supported by Baker 2016 and Xu 2018; p16 clearance extending murine lifespan and slowing wound closure verified.
- `c-m01-19` **plausible needs source check** — Supported in substance by Hickson 2019 and Chung 2019, but the negative literature search date (24 September 2026) cannot be verified from the cited documents.
- `c-m01-20` **supported as cited** — Supported by Hughes 2013, Sitohang 2022, Kafi 2007, and Varani 2000; trial outcomes for sunscreen, tretinoin, and retinol verified.
- `c-m02-01` **supported as cited** — Supported by Slominski & Wortsman 2000 and Tiganescu 2011, 2013; cutaneous 11β-HSD1 expression and knockout protection from atrophy verified.
- `c-m02-02` **unsupported** — Ajjan 2022 verifies trial outcomes, but the assertion that no registered trial tests an 11β-HSD1 inhibitor for skin ageing and that AZD4017 has no FDA approval was marked not_found under searchedWholeDocument in the cited sources.
- `c-m02-03` **plausible needs source check** — Nieman 2008 was evaluated by abstract only; Table 1 discriminating features (bruising, plethora, proximal myopathy, striae >1 cm) require full-text verification.
- `c-m02-04` **plausible needs source check** — Nieman 2008 abstract only; 2-3 per million incidence and iatrogenic predominance require full-text verification.
- `c-m02-05` **plausible needs source check** — Nieman 2008 abstract only; recommendations against widespread testing and random serum cortisol require full-text check.
- `c-m02-06` **supported as cited** — Supported by Rittié 2008 and Thornton 2013; topical estradiol increasing procollagen in sun-protected but not photoaged skin verified.
- `c-m02-07` **supported as cited** — Supported by Brincat 1985, 1987 and Thornton 2013; 1-2% annual postmenopausal collagen decline and review citation of 30% figure verified.
- `c-m02-08` **supported as cited** — Supported by Maheux 1994, Sauerbronn 2000, and Pivazyan 2023; systemic HT skin thickness/collagen effects and meta-analysis conclusions verified.
- `c-m02-09` **plausible needs source check** — Supported for Phillips 2008 and Owen 2016 wrinkle trials, but NAMS 2022 was read as abstract only and lacks the Level II rating text.
- `c-m02-10` **supported as cited** — Supported by Creidi 1994, Ashcroft 1999, and 21 CFR 310.530; topical estrogen trial data and US OTC unapproved drug status verified.
- `c-m02-11` **unsupported** — The claimSupport check marked searchedWholeDocument for the assertion that FDA labeling changes did not add skin as an indication; the cited FDA web documents do not mention skin.
- `c-m02-12` **plausible needs source check** — Supported for WHI and VMS timing, but NAMS 2022 abstract lacks the specific bioidentical compounding statements.
- `c-m02-13` **supported as cited** — Supported by NAMS 2020 GSM statement and Hannah-Shmouni 2026; vaginal estrogen efficacy without progestogen verified.
- `c-m02-14` **supported as cited** — Supported by Hughes 2013, Renova prescribing information, and Hannah-Shmouni 2026; sunscreen RCT and tretinoin label disclaimer verified.
- `c-m02-15` **supported as cited** — Supported by Darling 1997; 88% angiofibromas and 72% collagenomas in 32 MEN1 patients verified.
- `c-m02-16` **supported as cited** — Supported by Correa 2015 and Kirschner 2000; Carney complex PRKAR1A genetics, canthal lentigines, and cardiac myxoma mortality verified.
- `c-m02-17` **supported as cited** — Supported by Stanescu 2024; MEN2A cutaneous lichen amyloidosis, RET codon-634 variants, and interscapular presentation verified.
- `c-m02-18` **plausible needs source check** — Bornstein 2016 was read as abstract only; treating crisis before test results return is not explicit in the abstract.
- `c-m02-19` **unsupported** — The 0.2% prevalence of androgen-secreting neoplasms and >50% malignancy rate were marked not_found with searchedWholeDocument across the cited sources.
- `c-m02-20` **plausible needs source check** — Acanthosis nigricans and hypothyroidism dry skin verified, but thyrotropin-receptor mechanism for pretibial myxedema not explicitly verified in Lause 2017 text.
- `c-m03-01` **plausible needs source check** — Preclinical dWAT cathelicidin production and human acne preadipocyte data verified; unmeasured contribution to skin ageing not explicit in sources.
- `c-m03-02` **supported as cited** — Supported by Rohrich & Pessa 2007; anatomical facial fat compartments and changes with ageing verified.
- `c-m03-03` **supported as cited** — Supported by Guyuron 2009; 186 twin pairs showing 4-point BMI impact on perceived age before/after 40 verified.
- `c-m03-04` **supported as cited** — Supported by Gkogkolou & Böhm 2012, Dyer 1993, and Hannah-Shmouni 2026; glycation chemistry, RAGE activation, and associative human evidence verified.
- `c-m03-05` **supported as cited** — Supported by Dyer 1993 and Verzijl 2000; 15-year skin collagen half-life and 5-fold AGE increase verified.
- `c-m03-06` **supported as cited** — Supported by Meerwaldt 2004; skin autofluorescence correlation (r = 0.47-0.62) and validation in non-pigmented skin verified.
- `c-m03-07` **supported as cited** — Supported by Hannah-Shmouni 2026 and Draelos 2025; GRADE C rating for anti-glycation cosmetics based on surrogate endpoints verified.
- `c-m03-08` **supported as cited** — Supported by Drucker 2018 and Hannah-Shmouni 2026; incretin physiology and receptor pharmacology verified.
- `c-m03-09` **supported as cited** — Supported by FDA labels for Ozempic, Wegovy, Mounjaro, and Zepbound; approval dates, non-cutaneous indications, and absence of facial claims verified.
- `c-m03-10` **supported as cited** — Supported by Wilding 2021 (STEP-1 -14.9%) and Jastreboff 2022 (SURMOUNT-1 -15.0% to -20.9%); GRADE A ratings verified.
- `c-m03-11` **supported as cited** — Supported by Batsis 2026; systematic review of 35 RCTs showing median 28% muscle-related weight loss verified.
- `c-m03-12` **supported as cited** — Supported by Sharma 2025 (9% midface loss in 20 patients), Rao 2026 (1,226 patient survey), and Daneshgaran 2025; lack of RCTs measuring face verified.
- `c-m03-13` **supported as cited** — Supported by Wegovy and Zepbound labels and Burke 2025; labeled hair loss percentages, dysesthesia, and absence of facial volume loss verified.
- `c-m03-14` **supported as cited** — Supported by Paschou 2025 and Hannah-Shmouni 2026; lack of human trials on direct incretin effects on facial fat verified.
- `c-m03-15` **supported as cited** — Supported by FDA 2026 warnings and Ashraf 2024; compounded/counterfeit GLP-1 warnings and failed independent testing verified.
- `c-m03-16` **supported as cited** — Supported by Nikolis 2025 Delphi consensus, Humphrey 2023, and registered trials NCT07419854/NCT07685834; expert opinion status verified.
- `c-m03-17` **supported as cited** — Supported by Franceschi 2000 and Ferrucci & Fabbri 2018; inflammaging concept and predictive value of IL-6/CRP verified.
- `c-m03-18` **supported as cited** — Supported by Cani 2007, Erridge 2007, Camilleri 2019, and Scheffler 2018; metabolic endotoxemia data and ELISA zonulin flaws verified.
- `c-m03-19` **supported as cited** — Supported by Makrgeorgou 2018 (Cochrane 39 RCTs), Vassilopoulou 2024, and Suez 2019; eczema probiotic data verified.
- `c-m03-20` **plausible needs source check** — Parodi 2008, Faurschou 2015, Lebwohl 2026, and Reynolds 2019 verified; September 2026 post-PCAC bulks list status requires registry check.
- `c-m04-01` **supported as cited** — Supported by Pickart & Thaler 1973 and Hannah-Shmouni 2026; endogenous discovery and copper chelation verified.
- `c-m04-02` **supported as cited** — Supported by Pickart 2015 and Pickart & Margolina 2018; copper delivery to SOD/lysyl oxidase and gene profiling verified.
- `c-m04-03` **supported as cited** — Supported by Miller 2006 and Hannah-Shmouni 2026; one indexed post-laser RCT and GRADE C cosmetic rating verified.
- `c-m04-04` **supported as cited** — Supported by Hannah-Shmouni 2026 and Li 2016; absence of injectable RCTs and copper tissue irritation verified.
- `c-m04-05` **supported as cited** — Supported by Ogórek 2025 and Hostynek 2010; unsettled dermal penetration and in vitro Franz-cell dependence verified.
- `c-m04-06` **supported as cited** — Supported by FDA 503A categories (May 14, 2026); non-injectable Category 1 standing and planned February 2027 PCAC review verified.
- `c-m04-07` **plausible needs source check** — Robinson 2005 abstract only; 12-week pal-KTTKS RCT efficacy verified, but manufacturer funding disclosure requires full text.
- `c-m04-08` **supported as cited** — Supported by Blanes-Mira 2002, Wang 2013, and Aruan 2023; SNAP-25 mimicry, modest wrinkle trial efficacy, and neuromuscular implausibility verified.
- `c-m04-09` **supported as cited** — Supported by Dragomirescu 2014, Errante 2020, and Hannah-Shmouni 2026; pentapeptide-18 enkephalin mimicry, lack of RCTs, and GRADE D rating verified.
- `c-m04-10` **supported as cited** — Supported by Bjerke 2026 and Lupo & Cole 2007; cosmetic peptide regulatory safety framework verified.
- `c-m04-11` **supported as cited** — Supported by FDA PCAC briefing (July 2026), McGuire 2025, and ClinicalTrials.gov records; absence of published human RCTs verified.
- `c-m04-12` **plausible needs source check** — Supported by Esposito 2012 for the Ac-LKKTETQ fragment identity; assertion that no human trials exist for the fragment requires literature confirmation.
- `c-m04-13` **supported as cited** — Supported by Dalmasso 2008, Kannengiesser 2008, and Hannah-Shmouni 2026; KPV α-MSH identity, murine colitis data, and lack of human RCTs verified.
- `c-m04-14` **supported as cited** — Supported by Grönberg 2014 (n=34 positive pilot) and Mahlapuu 2021 (n=148 negative phase IIb); trial discordance verified.
- `c-m04-15` **supported as cited** — Supported by Federal Register 91 FR 20465, PCAC July 2026 calendar, and Tailor Made 2020 warning letter; advisory status and enforcement verified.
- `c-m04-16` **supported as cited** — Supported by Hannah-Shmouni 2026, Vanhee 2020, and Ashraf 2024; non-GMP status of RUO peptides and lack of published skin-peptide quality analyses verified.
- `c-m04-17` **supported as cited** — Supported by Hannah-Shmouni 2026; GLOW and KLOW identified as marketing blends of RUO peptides without controlled trials.
- `c-m04-18` **supported as cited** — Supported by Myung & Park 2025 (23 RCTs, 1,474 participants); disappearance of oral collagen benefit in unfunded and high-quality trials verified.
- `c-m04-19` **supported as cited** — Supported by Hannah-Shmouni 2026; US dietary supplement status and prohibition of disease claims verified.
- `c-m04-20` **supported as cited** — Supported by Errante 2020 and Shin 2024; SNAP-8 manufacturer figures and evaluation in multi-active microneedle patches verified.
- `c-m05-01` **supported as cited** — Supported by Ito 2005 and Hannah-Shmouni 2026; ex vivo human follicle HPA and somatotropic loop activity verified.
- `c-m05-02` **supported as cited** — Supported by Adil 2017 and Hannah-Shmouni 2026; 5α-reductase conversion of testosterone to DHT driving follicle miniaturization verified.
- `c-m05-03` **supported as cited** — Supported by Bertolini 2020; anagen follicle immune privilege and NKG2D+ CD8 T-cell collapse in alopecia areata verified.
- `c-m05-04` **supported as cited** — Supported by King 2022 (BRAVE-AA1/2) and FDA approval letter (June 13, 2022); baricitinib efficacy and US approval verified.
- `c-m05-05` **plausible needs source check** — The algorithm excerpt in the check payload lacked the detailed flowchart text for first-pass hair-loss workup, though referral triggers are verified.
- `c-m05-06` **supported as cited** — Supported by Adil 2017 meta-analysis; superiority of topical minoxidil (men/women) and finasteride (men) verified.
- `c-m05-07` **supported as cited** — Supported by Drugs@FDA records; Rogaine OTC approval (1988) and Propecia prescription approval (1997) verified.
- `c-m05-08` **supported as cited** — Supported by Slominski & Wortsman 2000 and Laiho & Murray 2022; POMC cleavage and melanocortin receptor functional distribution verified.
- `c-m05-09` **plausible needs source check** — Langendonk 2015 and Scenesse labels verify EPP trial data; GRADE A letter header in the guide excerpt was omitted in check payload.
- `c-m05-10` **supported as cited** — Supported by EMA EPAR (2014) and FDA label (2019/2024); EPP indication and twice-yearly skin exam warning verified.
- `c-m05-11` **supported as cited** — Supported by Dorr 1996, Wessells 1998, Böhm 2025, and Hannah-Shmouni 2026; limited 1990s human data and GRADE D rating verified.
- `c-m05-12` **supported as cited** — Supported by Cardones 2009, Böhm 2025, Mallory 2021, Nelson 2012, and FDA Category 2 risks page; reported adverse events verified.
- `c-m05-13` **supported as cited** — Supported by Breindahl 2015 (43-88% content, 5.9% impurities) and TGA advisory (22-54 mg in 30 mg sprays); substandard dosing verified.
- `c-m05-14` **supported as cited** — Supported by FDA Category 2 page, MHRA FOI 24/274, and TGA August 2026 alert; regulatory stances across US, UK, and Australia verified.
- `c-m05-15` **supported as cited** — Supported by Cardones 2009, Böhm 2025, and Hannah-Shmouni 2026; melanoma contraindication and lack of preventive effect verified.
- `c-m05-16` **supported as cited** — Supported by Mang 2012 and Scenesse prescribing information; dermoscopic naevus alterations mimicking melanoma verified.
- `c-m05-17` **plausible needs source check** — Lee 2017 verifies mechanism and animal data; September 2026 search date and PPG-Aug Grade D header require source-text check.
- `c-m05-18` **supported as cited** — Supported by Mehta 2025; discrepancy between review abstract 'clinical efficacy' and body table noting unapproved mouse data and oncologic risk verified.
- `c-m05-19` **plausible needs source check** — Dardenne 1982 verifies zinc dependency; PPG-Aug unindexed case series and Grade D assignment require text check.
- `c-m05-20` **plausible needs source check** — Absence of PTD-DBM and 21 CFR 216.23 bulks exclusion verified; thymulin acetate in Category 3 requires verification against the May 2026 PDF.
- `c-m06-01` **supported as cited** — Supported by Tavakkol 1992 and Edmondson 2003; differential dermal/epidermal receptor expression and cell proliferation verified.
- `c-m06-02` **supported as cited** — Supported by Hannah-Shmouni 2026 citing Horesh 2023; ex vivo human follicle somatotropic axis verified.
- `c-m06-03` **supported as cited** — Supported by Veldhuis 2008 and Hannah-Shmouni 2026; somatopause and necessity of age-adjusted IGF-1 reference ranges verified.
- `c-m06-04` **supported as cited** — Supported by Lange 2001 and Ben-Shlomo & Melmed 2006; epidermal thinning in GHD and glycosaminoglycan skin puffiness in acromegaly verified.
- `c-m06-05` **supported as cited** — Supported by Breederveld 2014 Cochrane review (13 RCTs, 701 patients); faster burn healing, hyperglycemia risk, and bias risk verified.
- `c-m06-06` **supported as cited** — Supported by Rudman 1990 (skin thickness P = 0.07, non-significant) and Papadakis 1996 (15% hydroxyproline increase); trial metrics verified.
- `c-m06-07` **supported as cited** — Supported by Liu 2007 meta-analysis, Blackman 2002, and Hannah-Shmouni 2026; modest body composition shifts, adverse events, and advice against anti-ageing use verified.
- `c-m06-08` **supported as cited** — Supported by 21 U.S.C. § 333(e); federal criminal offense to knowingly distribute HGH for unapproved anti-ageing use verified.
- `c-m06-09` **supported as cited** — Supported by Falutz 2010 pooled phase 3 trials (n=806, -15% visceral fat) and Egrifta WR labeling (approved 2010; excludes weight loss); GRADE A rating verified.
- `c-m06-10` **supported as cited** — Supported by Egrifta WR label; 47% with IGF-1 >2 SDS, 5% vs 1% diabetes-range HbA1c, and active malignancy contraindication verified.
- `c-m06-11` **plausible needs source check** — Khorram 1997 trial data verified; negative PubMed search assertion for September 2026 requires verification.
- `c-m06-12` **supported as cited** — Supported by Teichman 2006, Dominikowski 2026, and Hannah-Shmouni 2026; CJC-1295 PK data, absence of human trials for CJC without DAC, and GRADE D course rating verified.
- `c-m06-13` **supported as cited** — Supported by Beck 2014, Nass 2008, and Adunsky 2011; ipamorelin ileus failure and MK-677 hip fracture early termination for heart failure verified.
- `c-m06-14` **supported as cited** — Supported by 78 FR 14095 and Drugs@FDA; Geref approval/discontinuation history and non-marketing status verified.
- `c-m06-15` **supported as cited** — Supported by FDA Category 2 listings, PCAC October 2024 minutes, and Tailor Made 2020 warning letter; compounding restrictions on GH secretagogues verified.
- `c-m06-16` **plausible needs source check** — Ben-Shlomo 2006 and Giustina 2024 verify acromegaly signs; Katznelson 2014 abstract lacks specific comorbidity screening recommendations.
- `c-m06-17` **supported as cited** — Supported by Genotropin and Egrifta WR labels; fluid retention symptoms, glucose intolerance, and nevus monitoring warning verified.
- `c-m06-18` **supported as cited** — Supported by Knuppel 2020, Dal 2018, and Renehan 2004; IGF-1 cancer risk associations and acromegaly SIR figures (1.1 vs 1.5) verified.
- `c-m06-19` **supported as cited** — Supported by Swerdlow 2017 (SAGhE cohort, n=23,984), Boguszewski 2022, Guevara-Aguirre 2011, and Dominikowski 2026; absence of long-term secretagogue safety data verified.
- `c-m07-01` **supported as cited** — Supported by Balshem 2011 and Guyatt 2008; GRADE 4-level framework applying to bodies of evidence rather than single studies verified.
- `c-m07-02` **supported as cited** — Supported by Balshem 2011 and Guyatt 2025 Core GRADE series; five downgrading domains and upgrade criteria verified.
- `c-m07-03` **plausible needs source check** — Course examples map correctly to GRADE domains, but Miller 2006 abstract does not confirm being the 'only' indexed RCT.
- `c-m07-04` **supported as cited** — Supported by Lundh 2017 Cochrane review (75 papers); RR 1.27 for favorable efficacy and RR 1.34 for favorable conclusions in industry-funded studies verified.
- `c-m07-05` **supported as cited** — Supported by Hannah-Shmouni 2026; adaptation of GRADE A-D rating evidence rather than legality, and separation of mechanism from grade, verified.
- `c-m07-06` **supported as cited** — Supported by 21 U.S.C. § 353a and FDA guidance; 503A hierarchical qualification, registered facility, and CoA requirements verified.
- `c-m07-07` **supported as cited** — Supported by 21 U.S.C. § 353b and FDA 503B guidance; cGMP compliance, risk-based inspection, and unapproved status of outsourcing products verified.
- `c-m07-08` **supported as cited** — Supported by 21 CFR 216.23; codified list containing only six non-peptide substances unchanged since 2019 verified.
- `c-m07-09` **supported as cited** — Supported by FDA category lists (May 14, 2026) and safety risks page; Category 1 GHK-Cu non-injectable status and withdrawn table verified.
- `c-m07-10` **supported as cited** — Supported by FDA PCAC briefing (July 2026) and 21 CFR 216.23; advisory nature of committee, negative staff recommendation for BPC-157, and need for rulemaking verified.
- `c-m07-11` **supported as cited** — Supported by 85 FR 10057 and FDA deemed-BLA lists; 40-amino-acid cutoff, transition of tesamorelin/hyaluronidase to BLAs, and loss of 503A/503B eligibility verified.
- `c-m07-12` **supported as cited** — Supported by Lilly v. Kennedy (S.D. Ind. 2025; 7th Cir. 2026); retatrutide 39-amino-acid backbone ruling and pending appeal verified.
- `c-m07-13` **supported as cited** — Supported by Hannah-Shmouni 2026 and FDA briefing documents; CoA components, analytical limits, and inability to prove sterility/storage verified.
- `c-m07-14` **supported as cited** — Supported by FDA 2026 endotoxin guidance; dosage-regimen/route dependent calculation of endotoxin limits verified.
- `c-m07-15` **supported as cited** — Supported by FDA PCAC BPC-157 briefing (July 2026); nominator CoA salt discrepancy, missing impurity limits, and absent endotoxin testing verified.
- `c-m07-16` **supported as cited** — Supported by Ashraf 2024 (7.7-14.4% purity, 29-39% overfill, universal endotoxin) and Popławska 2019 (unidentified GHRP-2 analogue); analytical failures verified.
- `c-m07-17` **supported as cited** — Supported by 21 CFR 312.160, 21 CFR 201.128, and Hannah-Shmouni 2026; research-only shipping limits, objective intended use, and lack of clinical route verified.
- `c-m07-18` **supported as cited** — Supported by FDA cosmetics and supplement guidance; appearance vs structure/function claims, absence of legal meaning for 'cosmeceutical', and DSHEA rules verified.
- `c-m07-19` **supported as cited** — Supported by FDA off-label guidance, 21 U.S.C. § 331, and Tailor Made 2020 warning letter; requirement of prior approval for off-label use verified.
- `c-m07-20` **supported as cited** — Supported by Hannah-Shmouni 2026 and 21 CFR 50.25; informed consent and chart documentation elements for unapproved/compounded peptides verified.

## Modules
- **m01** [skim] Establishes cutaneous neuro-immuno-endocrinology, local steroidogenesis, single-cell RNA atlas interpretation, and cellular senescence vs. proven matrix therapies. Scientifically rigorous and properly caveats transcriptomic data.
- **m02** [verify] Differentiates local cutaneous steroid loops from systemic endocrine disease (Cushing syndrome, inherited endocrine neoplasias) and appraises the lack of facial wrinkle efficacy in large MHT trials. Clinical referral guidance is excellent.
- **m03** [skim] Examines dermal white adipose tissue, glycation/AGE cross-linking, and incretin (GLP-1/GIP) facial fat deflation ('Ozempic face'). Excellent separation of pivotal trial weight endpoints from small observational facial data.
- **m04** [verify] Critiques topical matrikines, GHK-Cu, oral collagen trials, and unregulated tissue-repair peptides (BPC-157, TB-500). Contains unconfirmed post-approval edits that require verification.
- **m05** [skim] Covers hair follicle neuroendocrinology, pattern hair loss treatments, melanocortin receptor biology, and the severe clinical hazards of Melanotan II. Strongly contrasts approved EPP therapy (afamelanotide) with illicit tanning compounds.
- **m06** [skim] Details somatotropic axis pharmacology (somatropin, tesamorelin, secretagogues, IGF-1 LR3) and acromegaloid soft-tissue manifestations. Properly highlights federal legal restrictions and mitogenic concerns.
- **m07** [verify] Provides an operational framework for GRADE evidence appraisal, 503A/503B statutory compounding criteria, Certificate of Analysis auditing, and medicolegal charting. Exceptional instructional utility.

## Assessment
The assessment strategy is robust and psychometrically sound. It incorporates 21 lesson-level formative checks, 7 module-level scenario checks, and a 14-question summative course quiz requiring an 80% passing score. The items test thestated learning objectives across four defined pillars: physiology (36%), evidence appraisal (29%), regulatory safety (29%), and patient conversation (7%). Every question features three plausible options, a single defensible correct key, and detailed pedagogical rationales. Weaknesses are minor: question cq-m02-1 relies on an assertion regarding skin HPA-axis expression that was marked not_found in the Nieman abstract check, and question cq-m06-2 has partial missing evidence in the abstract-only check of Veldhuis 2008, though both keys are clinically defensible.

## Educational quality
Educational quality is exceptional. Learning objectives are stated with measurable Bloom's taxonomy verbs and align directly with module instruction and assessment items. The pedagogical framework systematically enforces four distinct epistemic registers in every clinical discussion: biological mechanism, human clinical trial evidence, statutory regulatory status, and the open scientific question. Content is concise, dense with clinical pearls, and completely free of padding or editorial voice tics (the automated voice audit passed with zero contrastive or duplicated tags). The role-routing reflection in m1-p02 establishes professional scope boundaries effectively.

## Learning time
≈ 235 min (Calculated independently based on: 47 audio/narrative text blocks (~12,000 words at 140 wpm = 86 min), 16 interactive clinical classification and sorting tools (at 4 min each = 64 min), 10 statistical analysis blocks (at 2 min each = 20 min), and 42 total assessment items across formative checks and summative quiz (at 1.5 min each = 65 min). Total runtime is approximately 235 minutes (~3.9 hours).) — credit hours proportionate: yes · Package estimatedMinutes is 211 (~3.5 hours), which represents a fast baseline. The independent estimate of 235 minutes (~3.9 hours) reflects realistic interactive tool engagement and assessment time. No credit hours are currently assigned or claimed, which aligns with disclaimers.

## Localization
Only the English edition ('en') is requested in requestedLocales; no translated editions are claimed. Terminology, biochemical units, and clinical phrasing are fully appropriate for international Anglophone clinical practice. However, there is a substantial localization divergence at the regulatory level: package.jurisdictions lists both US and GB, but the course content repeatedly states that UK/MHRA rules are omitted or in progress.
