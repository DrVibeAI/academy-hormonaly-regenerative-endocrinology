#!/usr/bin/env python3
"""Stage 20 · curriculum skeleton for Hormones and Peptides for Skin.

Reads the approved intake plan (intake-handoff/source-map.json, plan
skin-outline-20260921-v2) and emits packages/hormones-peptides-skin.json:
modules, units, objectives, pillar tags and assessment skeletons — no blocks.
Re-run after any change to the handoff or to the mappings below.
"""
import hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TODAY = "2026-09-24"
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

# --- jurisdictions researched after the US/UK build (citations/jurisdictions.json, from jurisdictions/<CODE>.json via the foundry's
# tools/course/jurisdiction-registry.mjs). A jurisdiction's layers read "mapped" only once its notes sit on moments
# (claimLocations of its j-<code>-NN claims); until then "review". Confirmation by the medical reviewer is tracked per module in
# postApprovalChanges, like every other change after approval.
JREG = LIT.get("jurisdictions", {})
PLACED = {}
for a in AUTHORED.values():
    for cid, locs in (a.get("claimLocations") or {}).items():
        if cid.startswith("j-"):
            PLACED.setdefault(cid.split("-")[1].upper(), set()).update(locs)
# Medical confirmation of the post-approval changes (every country note is one), from the authored change logs: the jurisdiction
# records read "confirmed by <reviewer> on <date>" once none is open, never a stale "confirmation pending".
_CHANGES = [c for a in AUTHORED.values() for c in (a.get("postApprovalChanges") or [])]
_OPEN = [c for c in _CHANGES if not c.get("confirmedBy")]
_MED = sorted((c for c in _CHANGES if str(c.get("confirmedBy", "")).startswith("Fady Hannah-Shmouni")), key=lambda c: c.get("confirmedAt", ""))
CONFIRMATION = ("confirmation pending with the post-approval changes" if _OPEN or not _MED
                else f"confirmed by Fady Hannah-Shmouni, MD FRCPC on {_MED[-1]['confirmedAt']}")
REVIEW_OWNER = "Fady Hannah-Shmouni, MD FRCPC" + (" (confirmation pending)" if _OPEN or not _MED else f" (confirmed {_MED[-1]['confirmedAt']})")
JURISDICTION_LAYER_TOPICS = {
    "product": ("substances", None),
    "claims": ("frameworks", {"advertising", "cosmetics", "supplements"}),
    "practice": ("frameworks", {"compounding", "unlicensed", "professional", "import", "controlled", "research-use-only", "enforcement"}),
}
def _jprofile(code, info):
    claims = [c for c in JREG.get("claims", []) if c.get("jurisdiction") == code]
    placed = sorted(PLACED.get(code, set()))
    status = "mapped" if placed else "review"
    def detail(layer):
        kind, topics = JURISDICTION_LAYER_TOPICS[layer]
        n = sum(1 for c in claims if (c.get("kind") == "substance") == (kind == "substances") and (topics is None or c.get("subject") in topics))
        return (f"{n} primary-source statement(s) researched {info.get('researchedAt')}; " +
                (f"notes on {len(placed)} moment(s); {CONFIRMATION}." if placed else "not yet placed on moments."))
    layers = [{"id": k, "status": status, "detail": detail(k)} for k in ("product", "claims", "practice")]
    layers.append({"id": "locale", "status": status, "detail": "Base English edition; each note names its jurisdiction and date and is shown first to learners who choose that country."})
    return {"code": code, "name": info.get("name", code),
            "authorities": [{k: a[k] for k in ("name", "scope", "url") if a.get(k)} for a in info.get("authorities", [])],
            "layers": layers, "reviewOwner": REVIEW_OWNER}
# Same order everywhere the learner sees the list (homepage, folded notes, course blurb): US, UK, then EU, Portugal, Brazil, UAE.
JURISDICTION_ORDER = ["EU", "PT", "BR", "AE"]
JURISDICTION_PROFILES = [_jprofile(code, info) for code, info in sorted(JREG.get("jurisdictions", {}).items(),
                         key=lambda kv: (JURISDICTION_ORDER.index(kv[0]) if kv[0] in JURISDICTION_ORDER else len(JURISDICTION_ORDER), kv[0]))]
# A claim may be placed by several modules (jurisdiction statements are shared): its locations are the UNION, never the last
# module's list (2026-09-25 — a dict comprehension had kept only the last module's placements).
CLAIM_LOCATIONS = {}
for _a in AUTHORED.values():
    for _k, _v in (_a.get("claimLocations") or {}).items():
        _locs = CLAIM_LOCATIONS.setdefault(_k, [])
        _locs.extend(x for x in _v if x not in _locs)
CLAIMS = [
    {"id": cl["id"], "text": cl["text"], "citationRefs": cl["citationRefs"], "status": cl["status"],
     "locations": CLAIM_LOCATIONS.get(cl["id"], [cl["unit"]]), "reviewNote": (cl.get("reviewNote") or "") + f" · grader: {reg['grader']}"}
    for reg in LIT.values() for cl in reg["claims"]
    if reg["module"] != "jurisdictions" or cl["id"] in CLAIM_LOCATIONS  # research statements enter the package once a moment uses them
]
# Jurisdiction sources likewise: only those a placed statement or an authored note cites (the registry keeps the full research).
def _refs(node, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "citationRefs" and isinstance(v, list): out.update(v)
            else: _refs(v, out)
    elif isinstance(node, list):
        for v in node: _refs(v, out)
    return out
_JIDS = {c["id"] for c in JREG.get("citations", [])}
_JUSED = _refs(list(AUTHORED.values()), set()) | {r for cl in CLAIMS for r in cl["citationRefs"]}
CITATIONS[:] = [c for c in CITATIONS if c["id"] not in _JIDS or c["id"] in _JUSED]

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
        "scope": "Copper peptides (GHK/GHK-Cu); signal peptides and matrikines (pal-KTTKS / Matrixyl, Matrixyl 3000, Palmitoyl Tripeptide-1); oral collagen peptides; neurotransmitter modulators (Argireline, SNAP-8, Leuphasyl); investigational repair peptides (BPC-157, TB-500, KPV, LL-37); evidence hierarchies, sponsorship and funding bias; US and UK regulatory status.",
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
    # Plain titles everywhere (Omar 2026-09-25: "plain module titles might be nicer, esp on mobile"): the authored unit's title
    # without its lesson count, in the app, the homepage and the certificate alike; the intake plan's working title stays in the plan.
    plain = re.sub(r"\s*·\s*(one|two|three|four|five|six|\d+) lessons?$", "", (authored or {}).get("unit", {}).get("title", {}).get("en", "")).strip() or m["title"]
    if authored:
        units[0]["title"] = {"en": plain}
    modules.append({
        "id": mid,
        "slug": SLUGS[m["id"]],
        "title": {"en": plain},
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

def approval_notes(a):
    """Changes made after an approval: unconfirmed ones are listed as awaiting the approver (the pre-review treats them as a
    major risk); confirmed ones are recorded as confirmed, with who and when."""
    ch = a.get("postApprovalChanges") or []
    open_ = [c for c in ch if not c.get("confirmedBy")]
    done = [c for c in ch if c.get("confirmedBy")]
    if open_:
        return {"notes": "Changed after this approval, awaiting the approver's confirmation: " + " | ".join(f"{c['block']}: {c['change']}" for c in open_)}
    if done:
        groups = {}
        for c in done:
            groups.setdefault((c["confirmedBy"], c["confirmedAt"]), []).append(c)
        return {"notes": "; ".join(f"{len(g)} change{'s' if len(g) != 1 else ''} made after this approval, confirmed by {by} on {at}: " + " | ".join(f"{c['block']}: {c['change']}" for c in g)
                                  for (by, at), g in groups.items())}
    return {}

# Course-level sign-offs (final quiz, tutor answers) recorded from the medical owner's final packet (signoffs.json).
SIGNOFFS = json.loads((HERE / "signoffs.json").read_text()) if (HERE / "signoffs.json").exists() else {}

COURSE_QUIZ = [q for mid in sorted(AUTHORED) for q in AUTHORED[mid].get("courseQuiz", [])]
TUTOR = [t for mid in sorted(AUTHORED) for t in AUTHORED[mid].get("tutorEntries", [])]
ASSESSMENTS = []
if COURSE_QUIZ:
    ASSESSMENTS.append({
        "id": "course-quiz", "kind": "course-quiz",
        "title": {"en": "Final check · Hormones and Peptides for Skin"},
        "questions": COURSE_QUIZ, "passingScorePct": 80,
        "weightDistribution": {p: round(sum(1 for q in COURSE_QUIZ if q.get("pillar") == p) / len(COURSE_QUIZ), 2) for p in PILLARS},
        "status": "approved" if SIGNOFFS.get("courseQuiz") else "ai_draft",
    })

# Stage 60 media: the teaching stills that authored blocks reference (block.teachingVisual.assetRef), taken from the image tool's
# manifest (perceptor-foundry tools/images/generate.mjs). Files live under public/assets/ (published to the media bucket by
# tools/deploy/publish-media.sh). Every still is a draft until the human media preview is recorded in signoffs.json.
MEDIA_MANIFEST = HERE / "media" / "images-manifest.json"
# Media status follows the recorded human media preview (signoffs.json mediaPreview), never the build's own judgement.
_MP = SIGNOFFS.get("mediaPreview")
MEDIA_APPROVAL = "approved" if _MP else "draft"
MEDIA_NOTE = (f"approved — {_MP['approver']}, {_MP['date']} (media preview of {_MP['date']}; see governance approvals)" if _MP
              else "pending — course-production/hormones-peptides-skin/review/media-preview.html")
IMAGES = {e["asset_id"]: e for e in json.loads(MEDIA_MANIFEST.read_text()).get("images", []) if not e.get("kind")} if MEDIA_MANIFEST.exists() else {}
ASSETS = []
for mid in sorted(AUTHORED):
    for b in AUTHORED[mid]["blocks"]:
        ref = (b.get("teachingVisual") or {}).get("assetRef")
        if not ref:
            continue
        e = IMAGES.get(ref)
        if not e:
            sys.exit(f"{b['id']}: teachingVisual.assetRef {ref} is not in {MEDIA_MANIFEST.relative_to(ROOT)}")
        f = ROOT / "public" / e["uri"].lstrip("/")
        if not f.exists():
            sys.exit(f"{b['id']}: {ref} file missing: {f.relative_to(ROOT)}")
        ASSETS.append({
            "id": ref, "kind": "image", "role": "illustration", "uri": e["uri"].lstrip("/"),
            "checksum": "sha256:" + hashlib.sha256(f.read_bytes()).hexdigest(),
            "generator": {"tool": "perceptor-foundry/tools/images", "model": e["model"],
                          "promptRef": f"course-production/hormones-peptides-skin/media/images-manifest.json#{e['id']}"},
            "approvalStatus": MEDIA_APPROVAL,
            "metadata": {"block": b["id"], "use": "teachingVisual", "route": e["route"], "tier": e["tier"], "aspectRatio": e["aspect_ratio"],
                         "promptSha256": e["prompt_sha256"], "generatedAt": e["generated_at"],
                         "mediaPreview": MEDIA_NOTE},
        })

# Module opening films (cinematic lane, docs/motion-contract.md § 10b): rendered from course-production/hormones-peptides-skin/video/
# cinematic/<id>.storyboard.json and listed in media/films-manifest.json; each film is a draft asset with its poster until the media
# preview, and carries the disclosure line the runtime shows under the player (a synthetic presenter is never unlabelled).
FILMS_MANIFEST = HERE / "media" / "films-manifest.json"
FILMS = json.loads(FILMS_MANIFEST.read_text()).get("films", []) if FILMS_MANIFEST.exists() else []
for fm in FILMS:
    for key in ("uri", "poster"):
        f = ROOT / "public" / fm[key]
        if not f.exists():
            sys.exit(f"{fm['block']}: film {key} missing: {f.relative_to(ROOT)}")
    video = ROOT / "public" / fm["uri"]; poster = ROOT / "public" / fm["poster"]
    ASSETS.append({
        "id": fm["id"], "kind": "video", "role": "module-opener", "locale": "en", "uri": fm["uri"], "durationSeconds": fm["durationSeconds"],
        "checksum": "sha256:" + hashlib.sha256(video.read_bytes()).hexdigest(),
        "generator": {"tool": "perceptor-foundry/tools/video/morph.mjs", "model": fm["models"], "promptRef": fm["storyboard"]},
        "approvalStatus": MEDIA_APPROVAL, "disclosure": fm["disclosure"],
        "metadata": {"block": fm["block"], "use": "module opening film", "scriptSources": fm["scriptSources"],
                     "mediaPreview": MEDIA_NOTE},
    })
    ASSETS.append({
        "id": fm["id"] + "-poster", "kind": "image", "role": "poster", "uri": fm["poster"],
        "checksum": "sha256:" + hashlib.sha256(poster.read_bytes()).hexdigest(),
        "generator": {"tool": "perceptor-foundry/tools/video/morph.mjs", "model": "frame of the film", "promptRef": fm["storyboard"]},
        "approvalStatus": MEDIA_APPROVAL, "metadata": {"block": fm["block"], "use": "film poster", "mediaPreview": MEDIA_NOTE},
    })

pkg = {
    "packageSchemaVersion": "0.1.0",
    "id": "hormonaly.hormones-peptides-skin",
    "slug": "hormones-peptides-skin",
    "kind": "course",
    "version": "1.0.1",
    "title": {"en": "Hormones and Peptides for Skin"},
    "summary": {"en": outline["summary"]},
    "academy": {
        "id": "hormonaly",
        "name": "Hormonaly Academy",
        "deploymentProfile": "branded",
        "brand": {"displayName": "Hormonaly Academy", "accentColor": "#5A4BC4", "brandOwner": "Hormonaly.ai"},
        "client": {
            "organization": "Hormonaly.ai / Hormonaly Press",
            "productContext": "A peptides-for-skin course for clinicians from Hormonaly Academy, built on Perceptors.",
        },
    },
    "baseLocale": "en",
    "locales": [
        {"locale": "en", "name": "English", "direction": "ltr", "status": "base",
         "reviewOwner": "Omar Saleem (reviewer of record)", "unitsPolicy": "US and UK conventions; regulatory examples labelled by jurisdiction"},
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
            {"en": "Regulatory statements name their jurisdiction and date. US status (FDA, 503A/503B compounding) is given in the lesson text; status in the United Kingdom, the European Union, Portugal, Brazil and the United Arab Emirates (federal, with Dubai and Abu Dhabi where they differ) is given in each moment's regulatory note, read from each regulator's own primary sources in September 2026, and the learner's own country is shown first. The US compounding categories have no equivalent in the other jurisdictions. Check the live status with the national regulator before acting."},
            {"en": "Designed toward future CME accreditation. No CME or CE credit is currently offered."},
        ],
    },
    "jurisdictions": [
        {
            "code": "US", "name": "United States",
            "authorities": [{"name": "FDA", "scope": "Compounding (503A/503B), bulk-substance categories, cosmetic vs drug", "url": "https://www.fda.gov/drugs/human-drug-compounding"}],
            "layers": [{"id": k, "status": "mapped", "detail": "US regulatory statements (FDA approvals, 503A/503B categories, warnings; dated September 2026) reviewed within the medical review of every module (Fady Hannah-Shmouni, 2026-09-24/25)."} for k in ["product", "claims", "practice", "locale"]],
            "reviewOwner": "Fady Hannah-Shmouni, MD FRCPC (medical review of every module, 2026-09-24/25)",
        },
        {
            "code": "GB", "name": "United Kingdom",
            "authorities": [
                {"name": "MHRA", "scope": "Medicines licensing, unlicensed ('special') products, borderline classification, medicines advertising and enforcement", "url": "https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency"},
                {"name": "OPSS", "scope": "Cosmetic products (assimilated Regulation (EC) No 1223/2009) in Great Britain", "url": "https://www.gov.uk/guidance/making-cosmetic-products-available-to-consumers-in-great-britain"},
                {"name": "ASA / CAP", "scope": "Advertising claims, including the ban on advertising prescription-only medicines to the public (CAP Code 12.12)", "url": "https://www.asa.org.uk/type/non_broadcast/code_section/12.html"},
                {"name": "GMC · GPhC · NMC", "scope": "Professional standards for prescribing unlicensed medicines and for cosmetic interventions", "url": "https://www.gmc-uk.org/professional-standards/the-professional-standards/good-practice-in-prescribing-and-managing-medicines-and-devices/prescribing-unlicensed-medicines"},
            ],
            "layers": [{"id": k, "status": "mapped", "detail": d + f" UK statements added 2026-09-25; {CONFIRMATION}."} for k, d in [
                ("product", "Product status mapped for the UK: MHRA-licensed products checked in UK product information (semaglutide as Ozempic and Wegovy, tirzepatide as Mounjaro, baricitinib, minoxidil, finasteride, somatropin, estradiol HRT, topical tretinoin), afamelanotide's UK licence (via NICE HST27), no UK product information for tesamorelin, sermorelin or ipamorelin (MHRA products database), somatropin as a Class C controlled drug, and the cosmetic (assimilated Regulation 1223/2009) and food-supplement (Food Supplements (England) Regulations 2003) categories. Modules 02–06."),
                ("claims", "Claims and advertising mapped for the UK: no sale, supply or advertising of a medicine without a UK marketing authorisation (Human Medicines Regulations 2012, regs 46 and 279), no advertising of prescription-only medicines to the public (reg. 284; CAP Code 12.12; MHRA Blue Guide; ASA ruling of 11 Feb 2026), cosmetic claims (Regulation 1223/2009 art. 20; ASA ruling of 13 May 2026 on a peptide serum), and food disease and health claims (Regulation 1169/2011 art. 7(3); Regulation 1924/2006 art. 10). Modules 04 and 07."),
                ("practice", "Practice mapped for the UK: the 'specials' route (reg. 167) and pharmacy preparation (Medicines Act 1968 s. 10) in place of 503A/503B, MHRA Guidance Note 14's order of preference (licensed, off-label, imported, special), prescriber responsibility (GMC paras 102–108, MHRA Drug Safety Update 2009, GPhC 2025, NMC Code 18), GMC's physical examination before injectable cosmetic medicines, MHRA's finasteride warnings (May 2026) and enforcement (retatrutide; the May 2026 seizure including peptide products; melanotan). Two new moments in module 07 (m7-p21, m7-p22); role versions changed only where the practice line differs by jurisdiction."),
                ("locale", "Locale mapped for UK learners on the base English edition: UK regulatory wording ('licensed', 'unlicensed medicine', 'special', 'prescription-only medicine', 'marketing authorisation') is used in the UK notes, each labelled 'In the UK' and dated, and shown first to learners who choose the United Kingdom."),
            ]],
            "reviewOwner": REVIEW_OWNER,
        },
    ] + JURISDICTION_PROFILES,
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
    **({"assets": ASSETS} if ASSETS else {}),
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
        # Changes made after an approval ride on that approval's notes (governance is outside the claim-support content digest),
        # so the GCLS reviewer and the review agent see what the approver has not yet re-confirmed.
        "approvals": [{**a["approval"], **approval_notes(a)} for a in AUTHORED.values() if a.get("approval")] + [SIGNOFFS[k] for k in ("courseQuiz", "tutorCorpus", "mediaPreview") if SIGNOFFS.get(k)],
        "accreditation": {
            "body": "GCLS", "status": "not_submitted",
            "notes": "Designed toward future CME accreditation (Omar 2026-09-21; pathway confirmed 2026-09-24: CME to be sought through an accredited provider (pathway to be confirmed)). CME-style measurable objectives, independence from commercial bias, disclosure of financial relationships. No CME/CE credit is claimed until that approval exists. GCLS accreditation: add-on licensed (Omar, 2026-09-24); medical review of every module complete (2026-09-24); next is the GCLS review room. The certificate is GCLS-issued only once GCLS accredits.",
        },
    },
    "distribution": {"targets": [{"platform": "academy-app", "notes": "Hormonaly Academy (hormonaly.perceptors.ai), the home for Hormonaly's peptide courses. Partner editions may share this package later (one evidence core, editions per academy)."}]},
    "metadata": {
        "generator": "course-production/hormones-peptides-skin/build-package.py",
        "pendingReview": [{"gate": "medical_review", "module": mid, "status": AUTHORED[mid].get("status", "ai_draft"), "owner": "Fady Hannah-Shmouni, MD FRCPC"} for mid in sorted(AUTHORED) if not AUTHORED[mid].get("approval")],
        "generatedAt": TODAY,
        "factory": "perceptor-foundry · stage 30 authored and medically approved, all seven modules (Fady Hannah-Shmouni, 2026-09-24)",
        "template": "blended-certification (phone-first delivery, certification-grade checks; unit rendering decided at authoring — the runtime renders one story per module today)",
        "variants": {
            "dimensions": ["audienceLevel", "jurisdiction"],
            "jurisdiction": {
                "decision": "Omar 2026-09-25: regulatory status for the US, UK, EU, Portugal, Brazil and the UAE, course in English. US in the lesson text; each other jurisdiction in metadata.variants.jurisdiction on the moments that state a status or rule, cited to that jurisdiction's primary sources (citations/jurisdictions.json, research in jurisdictions/<CODE>.json); the runtime shows the learner's own country first (EU note for other member states).",
                "invariant": "evidence grades, safety signals and the teaching never change by jurisdiction; only the regulatory status and rules do"
            },
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
            "capstone (adversarial co-design conversation) needs a package-driven runtime capstone; credential.capstoneRequired is false until then",
            "balance between endocrinopathy-with-skin-signs and elective aesthetic peptide content (plan question 2)",
            "tier-1 brief still 7/8 open on the intake portal (audience, outcomes, boundaries, locales, delivery)",
        ],
    },
}
out = ROOT / "packages" / "hormones-peptides-skin.json"
# Jurisdiction sources that are the same document as a course citation (same URL; e.g. the EMA Scenesse EPAR registered by
# module 05 and by the EU research) collapse onto the course id: every citationRef is rewritten and the duplicate dropped.
import re as _re
def _norm_url(u):
    u = str(u or "").lower()
    u = _re.sub(r"^https?://(www\.)?", "", u)
    u = _re.sub(r"#(?!!?/).*$", "", u)
    return u.rstrip("/")
_course_by_url = {_norm_url(c.get("url")): c["id"] for c in pkg["provenance"]["citations"] if c["id"] not in _JIDS and c.get("url")}
_alias = {c["id"]: _course_by_url[_norm_url(c.get("url"))] for c in pkg["provenance"]["citations"] if c["id"] in _JIDS and _norm_url(c.get("url")) in _course_by_url}
def _realias(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "citationRefs" and isinstance(v, list):
                node[k] = list(dict.fromkeys(_alias.get(x, x) for x in v))
            else:
                _realias(v)
    elif isinstance(node, list):
        for v in node: _realias(v)
if _alias:
    _realias(pkg)
    pkg["provenance"]["citations"] = [c for c in pkg["provenance"]["citations"] if c["id"] not in _alias]
    print("aliased jurisdiction sources onto course citations:", _alias)
out.write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n")
print(out, len(modules), "modules,", sum(len(m["units"]) for m in modules), "units,", len(assessments), "planned assessments")
