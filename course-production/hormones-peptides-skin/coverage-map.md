# Coverage map — Hormones and Peptides for Skin (stage 20 · 2026-09-22 · module 04 authored 2026-09-24)

Generated view of `packages/hormones-peptides-skin.json` (built by `build-package.py` from the approved intake plan
`skin-outline-20260921-v2`). The skeleton is architecture only: 7 modules × 3 lesson units, each unit holding one
stub title pane. Teaching content, questions and media arrive at stages 30+.

## Pillars

| Pillar | What it certifies | Taught in | Assessed by |
|---|---|---|---|
| physiology | the skin–endocrine system: local axes, senescence, adipose and incretin biology, GH axis | m01, m02, m03, m06 | module checks · course quiz (25 %) |
| evidence-appraisal | reading a hormone or peptide claim against GRADE and the actual human evidence | m03, m04, m05, m06, m07 | module checks · course quiz (25 %) · capstone |
| regulatory-safety | regulatory status by jurisdiction, compounding reality, COA reading, safety signals and red flags | m04, m05, m06, m07 | module checks · course quiz (25 %) · capstone |
| patient-conversation | history-taking, counselling, referral and documentation when a patient asks about or is using a peptide | m02, m03, m05, m07 | module checks · course quiz (25 %) · capstone |

## Modules → sources → assessment

A&RE = Aesthetic & Regenerative Endocrinology (2026) · PPG-Aug = The Peptide Pocket Guide, August 2026 build. Pages are the
start pages of the intake reading sections the approved plan cites. Prerequisites: m01 before everything; m07 after m04–m06.

| Module | Title | Lessons | Pillars | Locked sources (sections) | Assessment |
|---|---|---:|---|---|---|
| m01 | Cutaneous Neuro-Immuno-Endocrinology and Dermal Aging | 3 | physiology | **A&RE** p.10, Chapter 5 · The skin as an, p.22, p.28 | m01-check + course-quiz |
| m02 | Steroid and Systemic Hormone Signaling in Dermatologic Practice | 3 | physiology, patient-conversation | **A&RE** p.34, p.41, p.89, p.102 | m02-check + course-quiz |
| m03 | Metabolic, Adipose, and Incretin Axis Dynamics in Facial Architecture | 3 | physiology, evidence-appraisal, patient-conversation | **A&RE** p.48, p.54 · **PPG-Aug** p.16, p.25, p.32 | m03-check + course-quiz |
| m04 | Matrix Remodeling, Wound Healing, and Topical Matrikine Peptides | 3 | evidence-appraisal, regulatory-safety | **A&RE** Chapter 5 · The skin as an · **PPG-Aug** p.44, p.51, p.58, p.101 | m04-check + course-quiz |
| m05 | Follicular Dynamics, Cutaneous Pigmentation, and Melanocortin Signaling | 3 | evidence-appraisal, regulatory-safety, patient-conversation | **A&RE** p.22, p.89 · **PPG-Aug** p.58, p.65 | m05-check + course-quiz |
| m06 | Somatotropic Axis Pharmacology and Cutaneous Tissue Manifestations | 3 | physiology, evidence-appraisal, regulatory-safety | **A&RE** p.1, p.54, p.81 · **PPG-Aug** p.32, p.39, p.116 | m06-check + course-quiz |
| m07 | Evidence Appraisal, Regulatory Frameworks, and Prescriber Compliance | 3 | evidence-appraisal, regulatory-safety, patient-conversation | **A&RE** p.10, p.61, p.74 · **PPG-Aug** p.1, p.9, p.16, p.108, p.124, p.131 | m07-check + course-quiz |

Capstone (all four pillars): one adversarial co-design conversation — a fictional patient asks for a named skin peptide; the
learner builds an evidence-graded answer while the agent presses on evidence, regulatory status and safety — with a dossier
output (COA + marketing-sheet appraisal, module 07 pattern). Agent pre-grade, then faculty gate.

## Orphan check

- Module objectives without a locked source: **0** 
- Pillars taught by no module: **0** 
- Pillars with no assessment plan: **0** 

**Module 04 is authored** (stage 30, `ai_draft`, 2026-09-24): one story unit, three lessons, 19 moments, 4 exercises (classify,
quickfire, scenario, chips), role router + three role versions on four moments, module check. Content source:
`authored/m04.json`; readable draft: `review/m04-draft.md`; literature: `citations/m04.md` (51 sources, 20 claims, all graded).

Every module objective traces to sections of the two locked guides. The guides are single-author secondary sources, so the
lock also requires a primary or guideline citation for each clinical statement before authoring; those citations are not yet
in `provenance.citations[]` (only the two guides are). Module 04 has three ungraded candidate sets under
`course-production/research/`; modules 03, 05, 06, 07 have none yet.

## Read but unused (available if scope grows)

- A&RE chapter 17 onward: supplements and senotherapeutics, lifestyle and circadian optimization, tissue replacement; and the closing reference pages.
- PPG-Aug: reproductive, mitochondrial, neuroactive, sleep and oncology peptide entries — excluded by the lock as non-cutaneous.

## Decisions this skeleton is waiting on

Decided 2026-09-22 (Omar): audience = all clinicians with the LMS adapting the application layer by level (prescriber · clinical staff ·
advisor; see `metadata.variants`); literature grader = Omar / Perceptors; final reviewer = Dr. Hannah-Shmouni.

1. Balance between endocrinopathies presenting with skin signs (m02) and elective aesthetic peptides (m04–m06).
2. GB/EU regulatory mapping for the SEASON London audience; until then US examples are labelled as such.
3. SEASON reviewer.
4. Unit rendering at authoring: the runtime renders one story per module today, so the three lesson units may be authored as
   one resumable story with three labelled lessons (the Cenegenics Corporate Longevity pattern) — an authoring choice, not a
   curriculum change.
5. ~~Two content gaps surfaced by the competitor comparison~~ — adopted 2026-09-24 and authored in module 04: (`competitive-landscape.md`): **oral collagen peptides** (A&RE ch.15 rates
   them GRADE C on a randomized trial, Kim 2018; every competitor "skin" module covers them; ours does not) and **SNAP-8 / acetyl
   octapeptide-3** (the Argireline successor named in A4M's syllabus; add to m04-l2 scope). Both are additions to scope, not new modules.
