---
briefSchemaVersion: 0.1.0
channel: whiteglove
filledBy: "Daedalus (intake from customer-provided document, 2026-09-02)"
date: "2026-09-02"
academy:
  slug: "hormonaly"
  name: "Hormonaly Academy"
  shortName: "Hormonaly"
  profile: branded
customer:
  company: "Hormonaly.ai / Hormonaly Press"
  website: "https://hormonaly.ai"
  contact: { name: "Fady Hannah-Shmouni", email: "pending@intake.placeholder", role: "author & CEO" }
offering:
  summary: "Clinician-focused continuing education in aesthetic & regenerative endocrinology: physiology of endocrine aging, organs of aging (skin, adipose, gut), evidence-graded interventions (hormone optimization, peptides & bioregulators, senotherapeutics, lifestyle/circadian), and the regenerative frontier. Source: the Hormonaly Press 2026 pocket guide (109 pp., 20 chapters, GRADE A–D evidence ratings, 225 inline citations)."
  products:
    - { name: "Aesthetic & Regenerative Endocrinology — pocket guide (1st ed. 2026)", kind: content, what: "Evidence-graded clinician reference: 4 parts, 20 chapters, testing/interpretation reference, drug-safety tables, 3 clinical algorithms, consult + referral frameworks.", certifies: true }
audience:
  personas: ["practicing physicians optimizing skin/gut/endocrine axes for healthspan", "clinicians wanting point-of-care endocrine-dermatology guidance", "prescribers evaluating peptides/bioregulators/hormone optimization"]
  professionalScope: physicians
  regions: []              # INTAKE: jurisdiction(s) of practice not yet confirmed
outcomes:
  - statement: "After this course, a physician can evaluate endocrine-aging claims and interventions (hormones, peptides, senotherapeutics, lifestyle) against their evidence grade, and apply the testing, monitoring, and referral frameworks within their jurisdiction's regulatory boundary."
    objectives:
      - "Explain the skin–endocrine axis and the organs of aging"
      - "Interpret GRADE A–D strength-of-evidence ratings for specific indications"
      - "Apply testing & interpretation, drug-safety, and monitoring references"
      - "Run the hair-loss, adult-acne/androgen-excess, and menopausal-skin algorithms"
      - "Frame regenerative/frontier therapies honestly: what is established vs speculative"
boundaries:
  mustNever:
    - "Present off-label or unapproved hormone/peptide uses as established care; jurisdictional approval status must be stated where known"
    - "Upgrade or restate an evidence grade above what the source assigns to the specific indication"
    - "Prescribe individual doses or replace clinical judgment; the course educates on frameworks, not patient-specific treatment"
    - "Market compounded/unapproved products; the course teaches evaluation, not procurement"
locales: { base: en, editions: [] }    # INTAKE: additional editions (es-MX?) not confirmed
jurisdictions: []                        # INTAKE: ISO codes pending — drives the regulatory layer (Health Canada / FDA / COFEPRIS)
scope: { courses: 1, deliveryTemplate: certification-course, sessionMinutes: 5 }
productPacket:
  artifacts:
    - { type: guide, title: "Aesthetic & Regenerative Endocrinology — clinician pocket guide (Hormonaly Press, 1st ed. 2026)", uri: "corpus/hormonaly-pocket-guide-2026.pdf", rights: customer-owned, quotable: true }
    - { type: guide, title: "The Peptide Pocket Guide — Volume One, seventy therapeutics (Hormonaly Press, 2026 edition)", uri: "corpus/peptide-pocket-guide-2026.pdf", rights: customer-owned, quotable: true }
  claimsBoundary: { approved: [], prohibited: [] }   # INTAKE: customer's marketing/legal boundary not provided; draft mustNever above is the factory default
commercial:
  entitlement: open
  certificate: { access: included }
  gclsAccreditation: false        # INTAKE: licensed add-on decision pending
  leadGen: { landing: true, webinarFunnel: false }
governance:
  reviewerOfRecord: drvibe
  owners:
    medical: { name: "Fady Hannah-Shmouni, MD FRCPC", email: "pending@intake.placeholder" }
    brand: { name: "Hormonaly.ai", email: "pending@intake.placeholder" }
    publish: { name: "Omar Saleem", email: "omar@perceptors.ai" }
credential: {}                     # INTAKE: signatories/credit-hours TBD
media: { faculty: real-faculty, videoAmbition: narrated-slides }   # real-faculty → facultyReleaseOnFile required before any likeness/voice use
ops: { supportEmail: "pending@intake.placeholder" }
meta:
  intakeDeltas:
    - "Jurisdiction(s) of practice — drives the regulatory layer and which authorities map (Health Canada? FDA? COFEPRIS?)"
    - "Faculty consent & release — Dr. Fady Hannah-Shmouni likeness/voice needed for real-faculty media; consent email on file (per Omar) but scope confirmation for this academy pending"
    - "Customer contact emails — medical/brand/support owners currently placeholder addresses"
    - "Approved/prohibited claims boundary from customer marketing/legal (claimsBoundary empty)"
    - "Language editions — guide is English; es-MX or other editions not confirmed"
    - "GCLS accreditation decision (licensed add-on)"
    - "Entitlement/commercial model: open, invite-gated, or paid cohorts"
    - "Faculty headshot/B-roll assets for media stages (none provided yet)"
---

# Customer brief — Hormonaly Academy

New academy account (separate from Look4Gene). Intake built directly from the
customer-provided source: *Aesthetic & Regenerative Endocrinology*, Hormonaly
Press 2026, authored by **Fady Hannah-Shmouni, MD FRCPC** — endocrinologist &
biochemical geneticist (UBC), founder & CEO of Hormonaly.ai.

The pocket guide is an unusually factory-ready Tier-2 artifact: 20 chapters,
GRADE A–D strength-of-evidence ratings on every intervention claim, 225 inline
citations with per-chapter reference blocks, testing/interpretation and
drug-safety appendices, three clinical algorithms, and "three things to remember"
distillations per chapter. It maps nearly 1:1 onto a certification-course
structure with the book's own grades carried into the learner experience.

**Primary regulatory sensitivity:** the intervention chapters (hormone
optimization, peptides & bioregulators, senotherapeutics) live in heavily
regulated territory. Jurisdiction confirmation is the first blocking item —
it determines the authorities layer and what the course can say about
approval status. The factory default boundaries above are conservative until
the customer's claims boundary arrives.

## Second source artifact — The Peptide Pocket Guide (registered 2026-09-10)

Omar confirmed on 2026-09-10 that **The Peptide Pocket Guide** (Hormonaly Press 2026, Volume One: seventy peptide
therapeutics, biologics and mixtures, one page each with GRADE rating, mechanism, indications, dosing, evidence summary,
safety, clinical caveat and key references; 123 pp) is the source the **peptide course** is built from. It is registered
above as a second `productPacket.artifacts` entry (`corpus/peptide-pocket-guide-2026.pdf`, text extraction alongside).

Scope decision still open (kickoff): whether *Peptide Foundations* ships as a second course inside Hormonaly Academy
(`scope.courses: 2`) or as its own academy; either way it is the master for the Biolongeva (pt-BR / es-MX) and
SEASON skin editions — one evidence core, editions per academy. Boundaries above apply verbatim: the guide's dosing
pages inform the source lock but the course never prescribes doses.
