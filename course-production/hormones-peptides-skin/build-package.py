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

# --- module literature registries (citations/<module>.json, verified) ------
CITATION_FIELDS = ("id", "title", "authors", "publication", "year", "url", "sourceType", "note")
LIT = {}
for f in sorted((HERE / "citations").glob("*.json")):
    reg = json.loads(f.read_text())
    LIT[reg["module"]] = reg
    for c in reg["citations"]:
        if any(x["id"] == c["id"] for x in CITATIONS):
            continue  # the same source registered by two modules: first registry wins
        entry = {k: c[k] for k in CITATION_FIELDS if k in c}
        entry["note"] = {"en": f"{c.get('design','')} · {c.get('independence','')} · role: {c.get('role','')}" + (f" · PMID {c['pmid']}" if c.get("pmid") else "") + (f" · {c['note']}" if c.get("note") else "")}
        CITATIONS.append(entry)
AUTHORED = {f.stem: json.loads(f.read_text()) for f in sorted((HERE / "authored").glob("*.json"))}
CLAIM_LOCATIONS = {k: v for a in AUTHORED.values() for k, v in a.get("claimLocations", {}).items()}
CLAIMS = [
    {"id": cl["id"], "text": cl["text"], "citationRefs": cl["citationRefs"], "status": cl["status"],
     "locations": CLAIM_LOCATIONS.get(cl["id"], [cl["unit"]]), "reviewNote": (cl.get("reviewNote") or "") + f" · grader: {reg['grader']}"}
    for reg in LIT.values() for cl in reg["claims"]
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
# Scope decisions after the intake plan (Omar 2026-09-24: add oral collagen peptides and SNAP-8 to module 04).
MODULE_OVERRIDES = {
    "module-04": {
        "scope": "Copper peptides (GHK/GHK-Cu); signal peptides and matrikines (pal-KTTKS / Matrixyl, Matrixyl 3000, Palmitoyl Tripeptide-1); oral collagen peptides; neurotransmitter modulators (Argireline, SNAP-8, Leuphasyl); investigational repair peptides (BPC-157, TB-500, KPV, LL-37); evidence hierarchies, sponsorship and funding bias; US regulatory status.",
    },
}
LESSON_OVERRIDES = {
    ("module-04", 2): {
        "title": "Cosmetic Signal Peptides, Oral Collagen, and Neurotransmitter Modulators",
        "objective": "Evaluate the human trial evidence, funding sources and delivery limits for topical signal peptides (pal-KTTKS), oral collagen peptides and SNAP-25 mimics (Argireline, SNAP-8, Leuphasyl), and explain why pooled benefit can disappear in independent trials.",
    },
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
    m = {**m, **MODULE_OVERRIDES.get(m["id"], {})}
    units = []
    for j, l in enumerate(m["lessons"], 1):
        l = {**l, **LESSON_OVERRIDES.get((m["id"], j), {})}
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
            "citationRefs": sorted(set(cites) | {c["id"] for c in LIT.get(mid, {}).get("citations", []) if c.get("lesson") == f"{mid}-l{j}"}),
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
    authored = AUTHORED.get(mid)
    if authored:
        # Stage 30: the runtime reads units[0] of each module, so an authored module ships as one story unit
        # carrying its three lessons (the Cenegenics Corporate Longevity pattern); lesson grouping lives in metadata.lessons.
        story = dict(authored["unit"])
        story["learningObjectives"] = [u["learningObjectives"][0] for u in units]
        story["citationRefs"] = sorted({r for b in authored["blocks"] for r in b.get("citationRefs", [])}
                                       | {r for b in authored["blocks"] for r in (b.get("interaction") or {}).get("citationRefs", [])}
                                       | {r for b in authored["blocks"] for r in (b.get("quiz") or {}).get("citationRefs", [])})
        story["blocks"] = authored["blocks"]
        story["status"] = authored.get("status", "ai_draft")
        story["metadata"] = {"lessons": authored["lessons"], "audienceLevelPanes": authored.get("audienceLevelPanes", []),
                             "authoredAt": authored["authoredAt"], "source": f"course-production/hormones-peptides-skin/authored/{mid}.json"}
        units = [story]
    modules.append({
        "id": mid,
        "slug": SLUGS[m["id"]],
        "title": {"en": m["title"]},
        "eyebrow": {"en": (f"Module {i:02d} · 3 lessons · {len(authored['blocks'])} moments · ~{authored['unit']['estimatedMinutes']} min"
                           if authored else f"Module {i:02d} · {len(units)} lessons · ~{LESSON_MIN*len(units)+CHECK_MIN} min")},
        "summary": {"en": m["scope"]},
        "objective": {"en": learner_objective(m["objective"])},
        "pillars": MODULE_PILLARS[m["id"]],
        "estimatedMinutes": (authored["unit"]["estimatedMinutes"] + CHECK_MIN) if authored else LESSON_MIN * len(units) + CHECK_MIN,
        "sortOrder": i,
        "prerequisites": PREREQS.get(m["id"], []),
        "isCapstone": False,
        "status": (authored or {}).get("status", "ai_draft"),
        "units": units,
        **({"check": authored["check"]} if authored else {}),
        "metadata": {
            "intakePlanModuleId": m["id"],
            "sourceSections": [
                {"id": r, "citation": sections[r]["citation"], "label": sections[r]["label"], "topics": sections[r]["topics"]}
                for r in m["sourceRefs"]
            ],
            "assessmentPlan": m["assessment"],
            **({"lessons": authored["lessons"]} if authored else {}),
            **({"literature": {
                "registry": f"course-production/hormones-peptides-skin/citations/{mid}.json",
                "worksheet": f"course-production/hormones-peptides-skin/citations/{mid}.md",
                "verifiedAt": LIT[mid]["verifiedAt"], "citations": len(LIT[mid]["citations"]), "claims": len(LIT[mid]["claims"]),
                "grader": LIT[mid]["grader"], "finalReviewer": LIT[mid]["finalReviewer"],
            }} if mid in LIT else {}),
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

COURSE_QUIZ = [q for mid in sorted(AUTHORED) for q in AUTHORED[mid].get("courseQuiz", [])]
TUTOR = [t for mid in sorted(AUTHORED) for t in AUTHORED[mid].get("tutorEntries", [])]
ASSESSMENTS = []
if COURSE_QUIZ:
    ASSESSMENTS.append({
        "id": "course-quiz", "kind": "course-quiz",
        "title": {"en": "Final check · Hormones and Peptides for Skin"},
        "questions": COURSE_QUIZ, "passingScorePct": 80,
        "weightDistribution": {p: round(sum(1 for q in COURSE_QUIZ if q.get("pillar") == p) / len(COURSE_QUIZ), 2) for p in PILLARS},
        "status": "ai_draft",
    })

pkg = {
    "packageSchemaVersion": "0.1.0",
    "id": "hormonaly.hormones-peptides-skin",
    "slug": "hormones-peptides-skin",
    "kind": "course",
    "version": "0.2.0-m04-draft",
    "title": {"en": "Hormones and Peptides for Skin"},
    "summary": {"en": outline["summary"]},
    "academy": {
        "id": "hormonaly",
        "name": "Hormonaly Academy",
        "deploymentProfile": "branded",
        "brand": {"displayName": "Hormonaly Academy", "accentColor": "#5A4BC4", "brandOwner": "Hormonaly.ai"},
        "client": {
            "organization": "Hormonaly.ai / Hormonaly Press",
            "productContext": "Skin edition of the Hormonaly peptide master course for clinicians, commissioned by SEASON Aesthetic Conferences and built on Perceptors.",
        },
    },
    "baseLocale": "en",
    "locales": [
        {"locale": "en", "name": "English", "direction": "ltr", "status": "base",
         "reviewOwner": "Omar Saleem (reviewer of record) · SEASON reviewer pending", "unitsPolicy": "US and UK conventions; regulatory examples labelled by jurisdiction"},
    ],
    "audience": {
        "personas": [
            "dermatologist, aesthetic physician or plastic surgeon evaluating hormone and peptide claims for skin",
            "nurse practitioner or physician associate who prescribes or counsels in aesthetic, dermatology or primary care",
            "registered nurse, aesthetic nurse or injector who delivers treatments and fields patient questions",
            "other licensed providers (pharmacists, naturopathic doctors, allied aesthetic professionals) who advise on skin products and referrals",
        ],
        "professionalScope": {"en": "Continuing professional education for licensed clinicians and allied providers. Every learner gets the same evidence, regulatory status and safety content; what each may do with it — prescribe, recommend, administer, or refer — follows their own licence and scope, and the course adapts its practice guidance to that role. It informs clinical reasoning; it is not a protocol, contains no dosing, and does not replace specialist input, formal guidelines or individual judgment."},
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
            "lockedBy": "Omar Saleem (confirmed 2026-09-24: August edition, exclusions as written, CME wording) · drafted by the agent from the approved intake handoff · module 04 literature graded 2026-09-24 under Omar's delegation · final review Dr. Fady Hannah-Shmouni — see course-production/hormones-peptides-skin/source-lock.md",
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
        "claims": CLAIMS,
    },
    "curriculum": {"pillars": PILLARS, "modules": modules},
    **({"assessments": ASSESSMENTS} if ASSESSMENTS else {}),
    **({"tutorCorpus": TUTOR} if TUTOR else {}),
    "credential": {
        "type": "certification",
        "title": {"en": "Certificate · Hormones and Peptides for Skin"},
        "issuer": {"name": "Geneva College of Longevity Science", "linkedinOrganizationName": "Geneva College of Longevity Science"},
        "coBrand": {"displayName": "Hormonaly Academy", "accentColor": "#5A4BC4", "lockup": {"en": "Issued by Geneva College of Longevity Science (GCLS) · Hormonaly Academy co-brand · verified by Perceptors"}},
        "requirements": {"assessmentRefs": ["course-quiz"], "capstoneRequired": False, "vivaRequired": False, "passingScorePct": 80},
        "sharing": {"linkedin": True, "nativeShare": True, "directoryOptIn": True},
    },
    "governance": {
        "requiredGates": ["medical_review", "brand_approval", "localization_review", "gcls_accreditation", "publish"],
        "approvals": [a["approval"] for a in AUTHORED.values() if a.get("approval")],
        "accreditation": {
            "body": "GCLS", "status": "not_submitted",
            "notes": "Designed toward future CME accreditation (Omar 2026-09-21; pathway confirmed 2026-09-24: CME to be sought through SEASON and its accredited joint-providership partner). CME-style measurable objectives, independence from commercial bias, disclosure of financial relationships. No CME/CE credit is claimed until that approval exists. GCLS accreditation add-on decision still pending from intake.",
        },
    },
    "distribution": {"targets": [{"platform": "academy-app", "notes": "Hormonaly Academy tenant until SEASON's brand kit arrives; a SEASON-branded edition shares this package (one evidence core, editions per academy)."}]},
    "metadata": {
        "generator": "course-production/hormones-peptides-skin/build-package.py",
        "generatedAt": TODAY,
        "factory": "perceptor-foundry (main) · stage 20 skeleton + stage 30 module 04 (pilot) ai_draft",
        "template": "blended-certification (phone-first delivery, certification-grade checks; unit rendering decided at authoring — the runtime renders one story per module today)",
        "variants": {
            "dimensions": ["audienceLevel"],
            "audienceLevel": {
                "decision": "Omar 2026-09-22: all clinicians included — physicians, NPs, PAs, nurses and other providers — and the agentic LMS adapts to each learner's application level.",
                "levels": [
                    {"id": "prescriber", "who": "physicians, NPs, PAs with prescriptive authority", "application": "prescribing decisions, compounding pathway, documentation and informed consent, referral"},
                    {"id": "clinical-staff", "who": "RNs, aesthetic nurses, injectors, clinical staff", "application": "administering and monitoring within protocol, recognising red flags, answering patient questions, escalation"},
                    {"id": "advisor", "who": "pharmacists, naturopathic doctors, allied aesthetic professionals", "application": "product-level counselling, sourcing and regulatory awareness, when to refer to a prescriber"},
                ],
                "invariant": "evidence grades, regulatory status and safety signals never change by level; only the 'what you do next' layer, the case framing and the practice questions do",
                "variantable": ["adjustment pane", "your-turn question", "case persona", "tutor persona"],
            },
        },
        "review": {
            "literatureGrader": "Graded by the agent under Omar Saleem's delegation (2026-09-24), grading rule recorded in citations/<module>.json; Omar reviews, Dr. Hannah-Shmouni gives final review",
            "finalReviewer": "Fady Hannah-Shmouni, MD FRCPC — receives the final draft for review (Omar 2026-09-22)",
            "seasonReviewer": "pending",
        },
        "assessmentPlan": assessments,
        "courseShape": "7 modules × 3 lessons = 21 lessons, ~3 h; module check per module, course quiz weighted across four pillars, capstone = one adversarial co-design conversation with a dossier output",
        "intake": {
            "portalProject": "nJO-DfnWUc2HvW99mYVZ7Q",
            "plan": outline["id"],
            "sample": "skin-lesson-20260921-v2 (module 04)",
            "directionApproved": "2026-09-21 via test client invitation — direction only, scientific review pending",
        },
        "openItems": [
            "author findings for Dr. Hannah-Shmouni (citations/m04.md, end) — send with the final draft",
            "capstone (adversarial co-design conversation) needs a package-driven runtime capstone; credential.capstoneRequired is false until then",
            "SEASON reviewer",
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
