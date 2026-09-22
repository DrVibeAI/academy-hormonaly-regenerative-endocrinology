#!/usr/bin/env python3
"""Stage 20 · curriculum skeleton for Hormones and Peptides for Skin.

Reads the approved intake plan (intake-handoff/source-map.json, plan
skin-outline-20260921-v2) and emits packages/hormones-peptides-skin.json:
modules, units, objectives, pillar tags and assessment skeletons — no blocks.
Re-run after any change to the handoff or to the mappings below.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TODAY = "2026-09-22"
handoff = json.loads((HERE / "intake-handoff" / "source-map.json").read_text())
outline = handoff["outline"]

# --- sources -------------------------------------------------------------
GUIDES = {
    "Aesthetic-and-Regenerative-Endocrinology-Pocket-Guide-2026.pdf": "hannah-shmouni-2026-are",
    "The-Peptide-Pocket-Guide.pdf": "hannah-shmouni-2026-ppg-aug",
}
sections = {}
for s in handoff["sources"]:
    cid = GUIDES[s["name"]]
    for c in s["sections"]:
        sections[c["id"]] = {
            "citation": cid,
            "label": c["label"],
            "topics": c.get("finding", {}).get("topics", []),
        }

CITATIONS = [
    {
        "id": "hannah-shmouni-2026-are",
        "title": "Aesthetic & Regenerative Endocrinology — A Clinician's Pocket Guide",
        "authors": "Hannah-Shmouni F",
        "publication": "Hormonaly Press · first edition 2026 · 109 pp",
        "year": 2026,
        "sourceType": "client-documentation",
        "note": {"en": "Course spine. Secondary source by one author; GRADE ratings and chapter reference blocks are carried, clinical statements still need their primary citation before authoring. corpus/hormonaly-pocket-guide-2026.pdf · sha256 1478266b0809a3e3…"},
    },
    {
        "id": "hannah-shmouni-2026-ppg-aug",
        "title": "The Peptide Pocket Guide — 2026 Edition · Clinical Reference (seventy-two entries)",
        "authors": "Hannah-Shmouni F",
        "publication": "Hormonaly Press · August 2026 build · 146 pp",
        "year": 2026,
        "sourceType": "client-documentation",
        "note": {"en": "Skin-relevant entries only: mechanism, human-evidence summary, GRADE rating, regulatory and compounding status, safety signals. Dosing pages are outside the lock. Edition chosen by Omar 2026-09-22. corpus/peptide-pocket-guide-2026-08-clinical-reference.pdf · sha256 c533b43448507c9f…"},
    },
]

# --- pillars -------------------------------------------------------------
PILLARS = ["physiology", "evidence-appraisal", "regulatory-safety", "patient-conversation"]
MODULE_PILLARS = {
    "module-01": ["physiology"],
    "module-02": ["physiology", "patient-conversation"],
    "module-03": ["physiology", "evidence-appraisal", "patient-conversation"],
    "module-04": ["evidence-appraisal", "regulatory-safety"],
    "module-05": ["evidence-appraisal", "regulatory-safety", "patient-conversation"],
    "module-06": ["physiology", "evidence-appraisal", "regulatory-safety"],
    "module-07": ["evidence-appraisal", "regulatory-safety", "patient-conversation"],
}
SLUGS = {
    "module-01": "skin-as-endocrine-organ", "module-02": "systemic-hormones-and-skin",
    "module-03": "adipose-incretins-facial-architecture", "module-04": "matrix-peptides-and-wound-healing",
    "module-05": "follicle-pigment-melanocortins", "module-06": "gh-axis-and-skin",
    "module-07": "evidence-regulation-compliance",
}
PREREQS = {
    "module-02": ["m01"], "module-03": ["m01"], "module-04": ["m01"],
    "module-05": ["m01"], "module-06": ["m01"], "module-07": ["m04", "m05", "m06"],
}
LESSON_MIN, CHECK_MIN = 8, 4


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower())[:60].strip("-")


def learner_objective(text):
    return "By the end, you can " + text[0].lower() + text[1:]


modules, assessments = [], []
for i, m in enumerate(outline["modules"], 1):
    mid = f"m{i:02d}"
    refs = [sections[r] for r in m["sourceRefs"]]
    cites = sorted({r["citation"] for r in refs})
    units = []
    for j, l in enumerate(m["lessons"], 1):
        units.append({
            "id": f"{mid}-l{j}",
            "slug": f"{mid}-l{j}-{slug(l['title'])}",
            "title": {"en": l["title"]},
            "description": {"en": l["objective"]},
            "type": "lesson",
            "learningObjectives": [{"en": l["objective"]}],
            "estimatedMinutes": LESSON_MIN,
            "sortOrder": j,
            "isRequired": True,
            "status": "ai_draft",
            "citationRefs": cites,
            # Stage 20 stub: the lesson's opening pane only. Authoring (stage 30)
            # replaces it with the full block rhythm noted in metadata.blockRhythm.
            "blocks": [{
                "id": f"{mid}-l{j}-title",
                "type": "title",
                "lead": {"en": f"Module {i:02d} · Lesson {j}"},
                "title": {"en": l["title"]},
                "body": {"en": l["objective"]},
                "citationRefs": cites,
                "sourceNote": "stage-20 skeleton — objective as opening pane; no teaching content yet",
            }],
            "metadata": {
                "intakeLesson": f"{m['id']}/lesson-{j}",
                "blockRhythm": "hook → concept → evidence (GRADE + primary citation) → nuance (regulatory status by jurisdiction, safety signals) → adjustment (what this changes in practice) → your-turn (check)",
            },
        })
    modules.append({
        "id": mid,
        "slug": SLUGS[m["id"]],
        "title": {"en": m["title"]},
        "eyebrow": {"en": f"Module {i:02d} · {len(units)} lessons · ~{LESSON_MIN*len(units)+CHECK_MIN} min"},
        "summary": {"en": m["scope"]},
        "objective": {"en": learner_objective(m["objective"])},
        "pillars": MODULE_PILLARS[m["id"]],
        "estimatedMinutes": LESSON_MIN * len(units) + CHECK_MIN,
        "sortOrder": i,
        "prerequisites": PREREQS.get(m["id"], []),
        "isCapstone": False,
        "status": "ai_draft",
        "units": units,
        "metadata": {
            "intakePlanModuleId": m["id"],
            "sourceSections": [
                {"id": r, "citation": sections[r]["citation"], "label": sections[r]["label"], "topics": sections[r]["topics"]}
                for r in m["sourceRefs"]
            ],
            "assessmentPlan": m["assessment"],
        },
    })
    assessments.append({
        "id": f"{mid}-check",
        "kind": "module-check",
        "moduleRef": mid,
        "pillars": MODULE_PILLARS[m["id"]],
        "plan": m["assessment"],
    })

assessments += [
    {
        "id": "course-quiz",
        "kind": "course-quiz",
        "passingScorePct": 80,
        "weightDistribution": {p: 0.25 for p in PILLARS},
        "plan": "Pillar-tagged questions across all seven modules; rationale on every option; no question answerable from marketing language alone.",
    },
    {
        "id": "capstone",
        "kind": "capstone",
        "pillars": PILLARS,
        "components": [
            "One adversarial co-design conversation: the learner builds an evidence-graded answer to a fictional patient's request for a named skin peptide, while the agent presses on evidence, regulatory status and safety.",
            "Dossier output: appraisal of a simulated Certificate of Analysis and marketing sheet (module 07 pattern), with the patient conversation the learner would have.",
            "Evaluation: agent pre-grade, then faculty gate (reviewer of record).",
        ],
    },
]

pkg = {
    "packageSchemaVersion": "0.1.0",
    "id": "hormonaly.hormones-peptides-skin",
    "slug": "hormones-peptides-skin",
    "kind": "course",
    "version": "0.1.0-curriculum",
    "title": {"en": "Hormones and Peptides for Skin"},
    "summary": {"en": outline["summary"]},
    "academy": {
        "id": "hormonaly",
        "name": "Hormonaly Academy",
        "deploymentProfile": "branded",
        "brand": {"displayName": "Hormonaly Academy", "accentColor": "#0a7a72", "brandOwner": "Hormonaly.ai"},
        "client": {
            "organization": "Hormonaly.ai / Hormonaly Press",
            "productContext": "Skin edition of the Hormonaly peptide master course; commissioned by SEASON Aesthetic Conferences (Perceptors.ai partnership) and built without waiting for their reviewer.",
        },
    },
    "baseLocale": "en",
    "locales": [
        {"locale": "en", "name": "English", "direction": "ltr", "status": "base",
         "reviewOwner": "Omar Saleem (reviewer of record) · SEASON reviewer pending", "unitsPolicy": "US and UK conventions; regulatory examples labelled by jurisdiction"},
    ],
    "audience": {
        "personas": [
            "aesthetic physician or dermatologist evaluating hormone and peptide claims for skin",
            "plastic surgeon or aesthetic clinician whose patients ask about peptides",
            "aesthetic nurse practitioner or physician associate (inclusion pending the accreditation-audience decision)",
        ],
        "professionalScope": {"en": "Continuing professional education for licensed clinicians. It informs clinical reasoning; it is not a protocol, contains no dosing, and does not replace specialist input, formal guidelines or individual judgment."},
        "disclaimers": [
            {"en": "Educational content for clinicians. It does not prescribe, and it never restates an evidence grade above what the source assigns to the specific indication."},
            {"en": "Regulatory statements name their jurisdiction. US compounding examples (FDA 503A/503B) do not describe UK or EU status."},
            {"en": "Designed toward future CME accreditation. No CME or CE credit is currently offered."},
        ],
    },
    "jurisdictions": [
        {
            "code": "US", "name": "United States",
            "authorities": [{"name": "FDA", "scope": "Compounding (503A/503B), bulk-substance categories, cosmetic vs drug", "url": "https://www.fda.gov/drugs/human-drug-compounding"}],
            "layers": [{"id": k, "status": "review", "detail": "Mapped from the guides' US regulatory content; a named owner confirms."} for k in ["product", "claims", "practice", "locale"]],
            "reviewOwner": "pending (medical owner)",
        },
        {
            "code": "GB", "name": "United Kingdom",
            "authorities": [{"name": "MHRA", "scope": "Medicines and unlicensed products; SEASON London Skills Lab audience", "url": "https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency"}],
            "layers": [{"id": k, "status": "review", "detail": "No UK-specific regulatory content in the corpus yet; US examples must be labelled until mapped."} for k in ["product", "claims", "practice", "locale"]],
            "reviewOwner": "pending (SEASON reviewer)",
        },
    ],
    "provenance": {
        "sourceLock": {
            "lockedAt": TODAY,
            "lockedBy": "PROPOSED by the agent 2026-09-21/22 from the approved intake handoff · edition decided by Omar 2026-09-22 (August build) · exclusions + literature grader confirmation PENDING (medical owner) — see course-production/hormones-peptides-skin/source-lock.md",
            "corpusDescription": "Two Hormonaly Press clinician guides by Fady Hannah-Shmouni (A&RE first edition 2026; The Peptide Pocket Guide August 2026 build, skin-relevant entries only) plus, per module, the primary literature behind each clinical claim (guide reference blocks + perceptor research candidate sets). Excluded: all dosing/titration/stacking content, non-cutaneous peptide entries, blend names as evidence, any current CME/CE claim.",
            "allowedSources": [
                "hannah-shmouni-2026-are · corpus/hormonaly-pocket-guide-2026.pdf · sha256 1478266b0809a3e3…",
                "hannah-shmouni-2026-ppg-aug · corpus/peptide-pocket-guide-2026-08-clinical-reference.pdf · sha256 c533b43448507c9f… (skin-relevant entries only; dosing excluded)",
                "course-production/research/2026-09-21-ghk-cu-copper-peptide-skin/ (34 candidates, ungraded)",
                "course-production/research/2026-09-21-palmitoyl-pentapeptide-skin/ (11 candidates, ungraded)",
                "course-production/research/2026-09-21-bpc-157-wound-healing/ (22 candidates, ungraded)",
                "course-production/hormones-peptides-skin/intake-handoff/source-map.json (36 read sections with verbatim quotes and offsets)",
            ],
        },
        "citations": CITATIONS,
    },
    "curriculum": {"pillars": PILLARS, "modules": modules},
    "credential": {
        "type": "certification",
        "title": {"en": "Certificate · Hormones and Peptides for Skin"},
        "issuer": {"name": "Geneva College of Longevity Science", "linkedinOrganizationName": "Geneva College of Longevity Science"},
        "coBrand": {"displayName": "Hormonaly Academy", "accentColor": "#0a7a72", "lockup": {"en": "Issued by Geneva College of Longevity Science (GCLS) · Hormonaly Academy co-brand · verified by Perceptors"}},
        "requirements": {"assessmentRefs": ["course-quiz", "capstone"], "capstoneRequired": True, "vivaRequired": False, "passingScorePct": 80},
        "sharing": {"linkedin": True, "nativeShare": True, "directoryOptIn": True},
    },
    "governance": {
        "requiredGates": ["medical_review", "brand_approval", "localization_review", "gcls_accreditation", "publish"],
        "approvals": [],
        "accreditation": {
            "body": "GCLS", "status": "not_submitted",
            "notes": "Designed toward future CME accreditation (Omar 2026-09-21): CME-style measurable objectives, independence from commercial bias, disclosure of financial relationships. No CME/CE credit is claimed until an accredited provider pathway exists (SEASON's DC host university is the candidate). GCLS accreditation add-on decision still pending from intake.",
        },
    },
    "distribution": {"targets": [{"platform": "academy-app", "notes": "Hormonaly Academy tenant until SEASON's brand kit arrives; a SEASON-branded edition shares this package (one evidence core, editions per academy)."}]},
    "metadata": {
        "generator": "course-production/hormones-peptides-skin/build-package.py",
        "generatedAt": TODAY,
        "factory": "perceptor-foundry (main) · stage 20 curriculum skeleton",
        "template": "blended-certification (phone-first delivery, certification-grade checks; unit rendering decided at authoring — the runtime renders one story per module today)",
        "assessmentPlan": assessments,
        "courseShape": "7 modules × 3 lessons = 21 lessons, ~3 h; module check per module, course quiz weighted across four pillars, capstone = one adversarial co-design conversation with a dossier output",
        "intake": {
            "portalProject": "nJO-DfnWUc2HvW99mYVZ7Q",
            "plan": outline["id"],
            "sample": "skin-lesson-20260921-v2 (module 04)",
            "directionApproved": "2026-09-21 via test client invitation — direction only, scientific review pending",
        },
        "openItems": [
            "source lock confirmation: exclusions as written + who grades the module 04 literature (medical owner)",
            "reviewer of record + SEASON reviewer",
            "accreditation audience: physicians only vs multidisciplinary (plan question 1)",
            "balance between endocrinopathy-with-skin-signs and elective aesthetic peptide content (plan question 2)",
            "GB/EU regulatory mapping for the SEASON London audience",
            "primary citations per module before authoring (guides are single-author secondary sources)",
            "tier-1 brief still 7/8 open on the intake portal (audience, outcomes, boundaries, locales, delivery)",
        ],
    },
}
out = ROOT / "packages" / "hormones-peptides-skin.json"
out.write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n")
print(out, len(modules), "modules,", sum(len(m["units"]) for m in modules), "units,", len(assessments), "planned assessments")
