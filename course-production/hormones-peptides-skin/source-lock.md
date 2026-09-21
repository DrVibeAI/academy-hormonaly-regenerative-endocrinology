# Source lock — Hormones and Peptides for Skin (DRAFT · confirmation pending)

**Status:** PROPOSED by the agent on 2026-09-21 from the approved Perceptors intake handoff. Nothing here is a lock until the medical
owner confirms it (Foundry stage 10 exit). Until then no authoring may treat these sources as settled.

**Course:** Hormones and Peptides for Skin · 7 modules · 21 lessons · pilot module = 04 (matrix remodeling, wound healing, topical
matrikine peptides). Audience, outcomes and boundaries are still open in the intake brief (7 of 8 tier-1 groups); the lock covers
evidence only.

**Provenance of this draft:** intake project `nJO-DfnWUc2HvW99mYVZ7Q` on onboarding.perceptors.ai — plan
`skin-outline-20260921-v2` and sample `skin-lesson-20260921-v2`, both direction-approved 2026-09-21 through a test client invitation
(direction only; scientific review pending). Exports are in [`intake-handoff/`](intake-handoff/): `source-map.json` (36 read sections
with verbatim quotes and offsets), `sample-lesson.json`, `design.md`, `frame.md`, `onboarding-handoff.json`.

## Decision needed first: which Peptide Pocket Guide edition

Two different files carry the same title. The lock must name one.

| | June build | August build |
|---|---|---|
| File | `corpus/peptide-pocket-guide-2026.pdf` | `corpus/peptide-pocket-guide-2026-08-clinical-reference.pdf` |
| sha256 | `d8ff1a37c8877cc7…` | `c533b43448507c9f…` |
| Built | 2026-06-28 · 123 pp | 2026-08-13 · 146 pp |
| Cover | "Volume One · Seventy Therapeutics" | "2026 Edition · Clinical Reference" — seventy-two entries |
| Differs by | trial names and NCT identifiers in the text | adds amino-acid sequences and **per-entry dosing**; GRADE tags appear 177× vs 81× |
| Standing | confirmed by Omar 2026-09-10 as "the handbook"; registered in corpus (f267a47) | the file Omar placed in the intake folder 2026-09-21; **the approved plan and sample quote this text** |

**Proposed:** lock the **August** build, because every source reference and verbatim quote in the approved plan resolves against it,
and keep the June build in the corpus as a superseded edition. If the June build is preferred, the intake reading has to be re-run on
it (about four minutes) so the quotes and offsets move with it. Owner: Dr. Fady Hannah-Shmouni (author) / Omar.

## In the lock (proposed)

1. **Aesthetic & Regenerative Endocrinology — A Clinician's Pocket Guide** (Hannah-Shmouni; Hormonaly Press, first edition 2026; 109 pp).
   `corpus/hormonaly-pocket-guide-2026.pdf`, sha256 `1478266b0809a3e3…` — byte-identical to the intake upload. Role: the course spine
   (skin as an endocrine organ, organs of aging, interventions, algorithms). `sourceType: client-documentation`.
2. **The Peptide Pocket Guide — 2026 Edition · Clinical Reference** (August build, above), **skin-relevant entries only**, used for
   mechanism, human-evidence summary, GRADE rating, regulatory and compounding status, and safety signals.
   `sourceType: client-documentation`.
3. **Primary literature behind each clinical claim** — to be added per module from the guides' own reference lists plus the
   `perceptor research` candidate sets. Both guides are secondary sources by one author: they locate a claim, they do not settle it.
   A clinical or scientific statement enters the course only with a primary or guideline citation in `provenance.citations[]`; the
   guide alone is enough only for statements about what the guide itself says or recommends.

## Out of the lock (explicit exclusions)

- **All dosing, titration, reconstitution, stacking and administration content** in either guide, in every lesson, tutor answer and
  asset. The course teaches evidence appraisal, regulatory status, safety signals and the patient conversation.
- Pocket Guide entries with no cutaneous relevance. The intake reading left these sections unmapped, and they stay out:
  - PPG-Aug Page 73 · section 11: Gray-market peptide use and PT-141, Vasopressin and oxytocin posterior pituitary peptides, GnRH agonists in oncology and reproductive care
  - PPG-Aug Page 81 · section 12: Kisspeptin reproductive pharmacology, SS-31 (Elamipretide) in mitochondrial disease, Longevity and anti-aging peptides (Epitalon, Klotho, MOTS-c)
  - PPG-Aug Page 87 · section 13: Gray-market metabolic and longevity compounds, Senolytic and anti-aging peptides, Mitochondrial-derived and organ-protective fragments
  - PPG-Aug Page 94 · section 14: Neuroactive and nootropic peptides (Selank, Semax, Dihexa), Sleep and mood-modulating peptides (DSIP, PE-22-28), Investigational oncology peptides (Met-5-Enkephalin)
- `Peptide Compendium — Pharmacokinetics and Stacking` and `mitopeptides.md` (protocol-heavy; not part of this course).
- Marketing language and blend names (for example GLOW, KLOW) as evidence. They may be named only as things a patient will ask about.
- Any statement that CME or CE credit is available. Per Omar 2026-09-21 the course is **designed toward future CME accreditation**
  (measurable objectives, independence from commercial bias, disclosure of financial relationships); it never states or implies
  current credit. The Learn-at-Pinnacle GCLS+ CME arrangement stays separate from peptide content.

## Module → source map (from the approved plan)

A&RE = Aesthetic & Regenerative Endocrinology · PPG-Aug = Peptide Pocket Guide, August build. Page numbers are the start pages of the
reading sections the plan cites (each section runs about 12,000 characters).

| # | Module | Lessons | Source sections cited by the approved plan |
|---|---|---:|---|
| 01 | Cutaneous Neuro-Immuno-Endocrinology and Dermal Aging | 3 | **A&RE** p.10, Chapter 5 · The skin as an, p.22, p.28 |
| 02 | Steroid and Systemic Hormone Signaling in Dermatologic Practice | 3 | **A&RE** p.34, p.41, p.89, p.102 |
| 03 | Metabolic, Adipose, and Incretin Axis Dynamics in Facial Architecture | 3 | **A&RE** p.48, p.54 · **PPG-Aug** p.16, p.25, p.32 |
| 04 | Matrix Remodeling, Wound Healing, and Topical Matrikine Peptides | 3 | **A&RE** Chapter 5 · The skin as an · **PPG-Aug** p.44, p.51, p.58, p.101 |
| 05 | Follicular Dynamics, Cutaneous Pigmentation, and Melanocortin Signaling | 3 | **A&RE** p.22, p.89 · **PPG-Aug** p.58, p.65 |
| 06 | Somatotropic Axis Pharmacology and Cutaneous Tissue Manifestations | 3 | **A&RE** p.1, p.54, p.81 · **PPG-Aug** p.32, p.39, p.116 |
| 07 | Evidence Appraisal, Regulatory Frameworks, and Prescriber Compliance | 3 | **A&RE** p.10, p.61, p.74 · **PPG-Aug** p.1, p.9, p.16, p.108, p.124, p.131 |

Read but not used by the plan, and available if scope grows: A&RE chapter 17 onward (supplements, lifestyle and circadian
optimization, tissue replacement) and the A&RE closing reference pages.

## Literature backing — pilot module 04 (candidates, not yet graded)

`perceptor research` runs of 2026-09-21 (OpenAlex rate-limited on two of three; PubMed and ClinicalTrials.gov answered):

| Topic | Candidates | Proposal |
|---|---:|---|
| GHK-Cu copper peptide skin | 34 | [`research/2026-09-21-ghk-cu-copper-peptide-skin/`](../research/2026-09-21-ghk-cu-copper-peptide-skin/LOCK-PROPOSAL.md) |
| Palmitoyl pentapeptide skin | 11 | [`research/2026-09-21-palmitoyl-pentapeptide-skin/`](../research/2026-09-21-palmitoyl-pentapeptide-skin/LOCK-PROPOSAL.md) |
| BPC-157 wound healing | 22 | [`research/2026-09-21-bpc-157-wound-healing/`](../research/2026-09-21-bpc-157-wound-healing/LOCK-PROPOSAL.md) |

First read of the GHK-Cu set supports the guide's GRADE C framing: the list is dominated by reviews and mechanistic or delivery
papers; the human trial signal is thin (one small randomized trial on laser-resurfaced skin, 2006; one phase 2 wound-healing gel
trial registered 2026 and still recruiting). That is the honest teaching point of the module and should be graded by a human
before it is written as such.

## Known gaps

1. **Reviewer of record is not named.** Medical owner for the start (Omar or Dr. Hannah-Shmouni) and the SEASON reviewer when one is named.
2. **Author and rights.** Both guides are Hormonaly Press titles; the intake records reuse rights as `unconfirmed`. A one-line
   written permission from the author/publisher closes this.
3. **Single-author secondary sources.** Modules 01–02 rest almost entirely on A&RE. Each needs its primary citations pulled from the
   chapter reference blocks before authoring.
4. **Modules 03, 05, 06, 07** have no literature runs yet. Suggested topics: GLP-1 receptor agonists facial volume skin; estrogen
   deficiency skin collagen; melanocortin afamelanotide / Melanotan safety; growth hormone secretagogues skin; FDA 503A bulk
   substances peptides (regulatory sources, not PubMed).
5. **Jurisdiction.** Regulatory content in both guides is US-centred (FDA 503A/503B, PCAC). A London audience (SEASON Skills Lab)
   needs MHRA/UK framing or an explicit "US regulatory example" label. Jurisdictions are still open in the intake brief.
6. **Figures.** The intake reads extracted text only. Every diagram in either guide needs separate visual and scientific review
   before reuse or redrawing.

## To confirm the lock

The medical owner answers three things: (1) August or June edition; (2) the exclusions above, as written; (3) who grades and signs
the module 04 literature set. On confirmation the agent writes `provenance.sourceLock` and seeds `provenance.citations[]` in
`packages/hormones-peptides-skin.json`, and stage 20 (curriculum) starts from the approved plan.
