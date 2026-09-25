# Jurisdiction research brief — Hormones and Peptides for Skin

Omar decided on 2026-09-25 that the course gives regulatory status for **US, UK, EU, Portugal, Brazil and the UAE** (course stays in
English). US and UK are already authored. Each research agent covers ONE new jurisdiction and writes ONE file:
`course-production/hormones-peptides-skin/jurisdictions/<CODE>.json` (EU, PT, BR, AE). Research only: do NOT edit authored/,
citations/, packages/, build-package.py or anything else. An authoring pass will turn these files into jurisdiction notes that each
learner sees for their own country.

## What to establish (current status, dated)

**Substances the course discusses** — for each, the regulatory position in your jurisdiction: authorised medicine (name the product,
the authorising body, the authorised indications relevant here, date), not authorised, withdrawn, refused, controlled, or unknown:
semaglutide (Ozempic/Wegovy), tirzepatide (Mounjaro/Zepbound), retatrutide, afamelanotide (Scenesse), Melanotan II / "melanotan",
baricitinib (Olumiant), minoxidil, finasteride, somatropin (growth hormone), tesamorelin, sermorelin, ipamorelin, CJC-1295,
ibutamoren (MK-677), BPC-157, TB-500 (thymosin beta-4 fragment), KPV, GHK-Cu, LL-37, thymulin, PTD-DBM, topical tretinoin (licensed
uses), menopausal hormone therapy / estradiol (licensed uses; is skin an indication?), oral collagen (food/supplement status).

**Frameworks** — the rules a clinician in your jurisdiction must know, with the legal instrument:
- compounding / pharmacy-made or magistral preparations, and prescribing unlicensed or off-label medicines (who may, on what basis);
- products sold "for research use only" and online sale / import of unauthorised medicines (including personal import rules);
- cosmetics law for topical peptide products (when a "peptide serum" is a cosmetic vs a medicine; borderline guidance);
- food-supplement and health-claims law (oral collagen);
- advertising of prescription-only medicines and health claims to the public (and social-media enforcement if any);
- controlled-substance status where relevant (e.g. growth hormone, anabolic agents);
- professional-regulator rules on aesthetic prescribing or hormone use for aesthetic purposes, where they exist;
- regulator warnings or enforcement actions about peptides, melanotan, falsified/compounded GLP-1s (with dates).

## Rules

- **Primary sources only**, read live: the regulator's own site, official journals/gazettes, legislation databases, the official
  product register / product information. Secondary sources (news, reviews, law-firm blogs) may point you to a primary source but are
  never cited for a fact. Record the date you read each page (`readAt`).
- **Every statement carries a verbatim quote** from its source (in the source's language) plus an English translation when not English.
  If you cannot quote it, do not state it.
- **Absence is hard to prove.** State "no authorised product for X was found" only when the official register is searchable and the
  search is conclusive; record the query and date. Otherwise put it under `notVerified`.
- **No dosing, no product sourcing advice.** Statements are about status and rules, not use.
- Statements are short (one or two sentences), plain English, jurisdiction-named and dated, e.g. "In the EU, afamelanotide
  (Scenesse) is authorised only for erythropoietic protoporphyria (EMA, 2014)."
- Never print secrets. Do not commit, push or deploy.

## Output file shape (`jurisdictions/<CODE>.json`)

```json
{
  "jurisdiction": { "code": "EU", "name": "European Union", "authorities": [{ "name": "", "scope": "", "url": "" }] },
  "researchedAt": "2026-09-25",
  "sources": [{ "id": "eu-…", "title": "", "authors": "issuing body", "publication": "", "year": 2026, "url": "",
                "sourceType": "regulator|legislation|label|register", "language": "en|pt|ar", "readAt": "2026-09-25", "note": "" }],
  "substances": [{ "name": "semaglutide", "status": "authorised|not-authorised|withdrawn|refused|controlled|unknown",
                   "statement": "", "sourceIds": [""], "quote": "", "quoteEn": "" }],
  "frameworks": [{ "topic": "compounding|unlicensed|research-use-only|import|cosmetics|supplements|advertising|controlled|professional|enforcement",
                   "statement": "", "sourceIds": [""], "quote": "", "quoteEn": "" }],
  "notVerified": [{ "subject": "", "reason": "" }],
  "authorFindings": [""]
}
```

Source ids are prefixed with the lower-case code (`eu-`, `pt-`, `br-`, `ae-`) and must be unique. Report back: counts (sources,
substances by status, frameworks), what could not be verified, and anything surprising a clinician in that jurisdiction must know.
