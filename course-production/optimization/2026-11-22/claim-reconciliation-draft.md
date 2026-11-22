# November Hormonaly claim-support reconciliation — draft review packet

agent pre-review — no gate opened

Course: `hormones-peptides-skin`. Evidence-only preparation; no teaching correction, approval, final claim disposition or readiness decision is made here. Medical owner: **Dr. Fady Hannah-Shmouni**. Regulatory interpretation additionally requires the named jurisdiction owner. All actions below are proposals for those humans, not instructions already executed.

## Baseline, provenance and limits

- Branch: `operator/20261122-research-hps-claim-reconciliation-draft`; baseline and `origin/factory/intake-hormonaly`: `5497f64d1ad2af3148d0db232bee7f7028ecb89d`.
- Foundry contract pin: `69b4706c26505bb6b03b08be6ab900b7493a0816`. Read that revision's `CLAUDE.md`, `agent/PERSONA.md`, `agent/GATES.md`, research-lock skill and `docs/claim-support.md`; academy `AGENTS.md` read; no academy-root `CLAUDE.md` exists.
- Current package: `packages/hormones-peptides-skin.json` (abbreviated **P** below), SHA-256 `6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa`. JSON anchors use RFC 6901 pointers. **A** = `course-production/hormones-peptides-skin/authored/`; **C** = `course-production/hormones-peptides-skin/citations/`.
- Lock: `course-production/hormones-peptides-skin/source-lock.md:30–46,77–83`; P `/provenance/sourceLock`. The August Peptide Pocket Guide (PPG) is locked; June is superseded. The guides are secondary client documentation: their text proves what the guides say, **not** an independently established clinical result. The lock requires primary/guideline support for clinical claims. Registered primary references below are existing entries, not newly admitted sources; where their underlying text is absent, this packet does not treat the registry's summary as primary evidence.
- Local PPG: `corpus/peptide-pocket-guide-2026-08-clinical-reference.{md,pdf}`; A&RE: `corpus/hormonaly-pocket-guide-2026.{md,pdf}`. PDF hashes match the lock prefixes; full hashes are in the verification output below. No excluded dosing/administration passages are reproduced as evidence.
- No network retrieval, paid panel, model/tool spend, media generation, source import, hub inspection/mutation or second expert dispatch was performed. Paused hub run `run-76e4274d-4ce7-40d0-9ee9-193e26e3a31d` was left untouched; revision 26 is the task's stated context, not newly verified live state.

## Historical audit: recovered inventory, not current medical verdicts

The named ops wrapper `reports/course_hormonaly_hormones-peptides-skin/audit/20261117T162958Z.md` was not found at the academy root or corresponding checked ops/Foundry report locations. Its full prose was not obtained. However, the **full underlying claim-support JSON** was recovered read-only from the already-fetched `origin/factory/audit-2026-11-17` (`e8e97374de977a6338f89d0b55dda30a42285255`):

`course-production/claim-support/hormonaly.hormones-peptides-skin-1.1.0.json`, generated `2026-11-17T16:24:00.640Z` (**H** below; read with `git show <revision>:<path>`).

H reports exactly 2,601 assertions: 2,104 supported, 80 partial, 8 contradicted, 374 not_found, 35 unverified. H's recorded package SHA matches P's current bytes. That removes package-byte drift as an explanation, but does not independently validate the judge's source interpretation. H also reports 71 unavailable units and one error. The **current-tree** file at the same report path is instead a November 12 `sourcesOnly: true` report with zero assertions; it is not the November 17 panel and has not been overwritten.

The full eight-assertion inventory is:

- `c-m01-19` — H `/units/219/assertions/2`.
- `c-m04-12` — H `/units/279/assertions/2`.
- `c-m04-16` — H `/units/283/assertions/4`.
- `c-m07-12` — H `/units/349/assertions/2`.
- `m4-p09` — H `/units/517/assertions/1`.
- `m4-p13` — H `/units/527/assertions/4` (TB-500, not KPV).
- `m4-x04` — H `/units/532/assertions/5` (KPV).
- `m7-check` — H `/units/745/assertions/2`.

The grouped task list is not a ninth/eight-item one-to-one inventory. In particular, the BPC tutor allegation is H `/units/767/assertions/0`: judge `verdict: contradicted`, but effective **status: unverified**, quote match failed (`coverage: 0.78`). It is not one of the eight. Every H passage is historical judge evidence until checked against the underlying source here; `quoteCheck.ok` in H alone is not this packet's independent verification.

## 1. COA sterility — current wording conflict verified; clinical correction unresolved

**Current content:** `m7-check`, P `/curriculum/modules/6/check/options/1/text/en`; identical at A `m07.json#/check/options/1/text/en` (correct answer index is 1):

> Topical GHK-Cu: small-trial evidence (C); in the US, non-injectable use sits in 503A Category 1, under evaluation; its certificate can show identity and purity, never sterility or legality.

**Available locked passage:** PPG `.md:794–798`, printed p.17 / PDF p.19, `hannah-shmouni-2026-ppg-aug` (P `/provenance/citations/1`):

> Compounding pharmacies should provide a COA documenting identity, purity, sterility, and endotoxin.

The guide does contain the alleged wording. This independently verifies a **wording tension** between documenting sterility tests and the answer's absolute “never sterility”; it does not prove that a COA guarantees the sterility of the vial in hand or legality. Those are separate questions. The guide passage concerns compounded products; the question begins with non-injectable topical use. Do not extend it to RUO injection or infer safety.

**Gap / proposed next action:** medical owner to compare the absolute answer with the more qualified COA treatment at C `m07.md:82` (`c-m07-13`) and the existing FDA briefing reference `fda-pcac-2026-bpc157-briefing` (C `m07.json:363–377`, P citation 387). That local entry is a summary, not the primary PDF. Obtain/recover its exact quality-testing passage before proposing clinical wording; a broader sterility-testing standard absent from the lock needs a human-applied lock amendment. Dr. Hannah-Shmouni and the jurisdiction owner must decide whether a scoped edit is needed. No automatic “COA proves sterility” replacement.

## 2. TB-500 fragment and KPV — resolve identity and evidence tier separately

**Current content:** `c-m04-12`, P `/provenance/claims/279/text`, also C `m04.json` claim `c-m04-12` / `m04.md:91`:

> TB-500 is the acetylated 17–23 fragment of thymosin β4 (Ac-LKKTETQ), not thymosin β4 itself; the fragment was characterized by analysing the product, and human trial data for the fragment do not exist.

`m4-p13`, P `/curriculum/modules/3/units/0/blocks/15/body/en`; A `m04.json#/blocks/15/body/en`:

> BPC-157 rests on a large rodent literature, mostly from one research group, and on uncontrolled human case series. TB-500 is not thymosin β4: it is a seven-residue fragment of it, identified by analysing the product itself, and no trial has tested the fragment. KPV, a tripeptide from the end of α-MSH, calms inflammation in mouse colitis and has no randomized human trial.

The same block's `/points/2/en` reads “KPV: mouse colitis only”. `m4-x04`, block 19, `/interaction/items/4/why/en` reads:

> A seven-residue fragment of thymosin β4 that has never been tested in a trial; what it has is a plausible mechanism.

Its KPV item 5 has `answer: preclinical`, whose label at `/interaction/labels/2/label/en` is “Mechanism or animal data only”; `/interaction/items/5/why/en` reads:

> Calms inflammation in mouse colitis models; no randomized human trial for any indication.

Both practice entries have identical A `m04.json#/blocks/19/...` counterparts. Tutor `tutor-m04-bpc157`, P `/tutorCorpus/7/answer/en`, A `m04.json#/tutorEntries/1/answer/en`, also says:

> TB-500 is a seven-residue fragment of thymosin beta-4 that has never been trialled; KPV has only mouse data.

**Available locked passages:** PPG TB-500 entry `.md:2532–2542`, printed p.49 / PDF p.51:

> Phase 2 trials for ophthalmic indications missed primary endpoints.

But its own caveat says “TB-500 and thymosin β4 are not interchangeable: the heptapeptide is a fragment”. Its reference is Crockford 2010, PMID 20536467; the current registry describes that source as the **parent molecule** review (P citation 275). Esposito 2012, PMID 22962027 (P citation 276), is registered as analytical fragment characterization, not a clinical trial. These are references, not freshly read primary texts.

PPG KPV entry `.md:2472–2483`, printed p.48 / PDF p.50:

> Preclinical data for inflammatory-bowel-disease models; small open-label studies for atopic dermatitis. No randomized human trials.

Its caveat separately describes “animal IBD models + small dermatology case reports + anecdotal use”. The entry's listed references at `.md:2490–2492` are Kannengiesser and Dalmasso; C `m04.json` / P citations 277–278 describe murine work, not the human reports.

**Verified versus alleged:** the KPV guide/course **wording mismatch** is independently present. “No randomized human trial” does not mean “no human reports”; the explanatory sentence alone is not refuted by the guide. TB-500's Phase 2 line is independently present under that heading, but the guide's fragment/parent caveat prevents treating this as proof of fragment trials. H's TB-500 clinical contradiction remains **unverified at primary-study level**.

**Finite proposed disposition:** Dr. Hannah-Shmouni to request (a) the exact ophthalmic trial publication/registry record identifying molecule/sequence, formulation, route, indication and endpoints, and (b) the human KPV report citations/full text, including population, route, formulation and study design. Those primary passages are not present in the reviewed local corpus. Ophthalmic evidence of an unspecified formulation/route cannot be transferred to injected fragment use or skin outcomes; human case reports/open-label work cannot be promoted to randomized efficacy evidence. Keep both questions unresolved until source recovery; embed a draft lock-amendment request for any human KPV/trial source not already registered. Only then may the medical owner choose retain-with-rationale versus separately authorized scoped edits across claim/card/practice/tutor. No evidence-grade upgrade here.

## 3. Heavy metals, Matrixyl 3000 and BPC tutor — three different gaps

**Heavy metals: current** `c-m04-16`, P `/provenance/claims/283/text`, C `m04.md:95,106`, ends:

> Heavy-metal contamination is reported for this market, not documented; the lesson says exactly that.

Current `m4-p17` correct-option explanation, P `/curriculum/modules/3/units/0/blocks/22/interaction/options/1/why/en` and A `m04.json#/blocks/22/interaction/options/1/why/en`, already qualifies the attribution:

> Right. Stop the exposure, capture the evidence, and get the skin change assessed. The Hormonaly guide states that heavy-metal contamination is documented in these products; the published analysis behind that statement could not be found. The change needs assessment either way.

**Locked source:** A&RE `.md:2315–2318`, chapter 15 printed p.60:

> because research-use-only powder is made outside GMP, impurity, inaccurate dosing, and heavy-metal contamination (arsenic, lead) are documented.

The wording mismatch exists, but a guide saying “documented” is **not** the missing analytical documentation. C `m04.json` and P citations 282 (`vanhee-2020-seized-research-peptides`, PMID 31667971) and 216 (`ashraf-2024-online-semaglutide-quality`, PMID 39509151) are adjacent-product references; the Vanhee registry note explicitly says it does not document heavy-metal contamination. No direct skin-peptide metal-assay primary text was found in the reviewed materials.

**Proposal / owner:** Dr. Hannah-Shmouni to identify the guide's underlying analytical report (product identity/lot, metals tested, method, measured results), or confirm the attribution/qualification should remain. If the report is outside the lock, request a dated amendment, not an automatic reversal to “documented”. Do not generalize semaglutide/seized-product findings to a specific skin-peptide lot. Current qualified teaching must not be relabelled a verified medical defect from H alone.

**Matrixyl: current** `m4-p09`, P `/curriculum/modules/3/units/0/blocks/11/interaction/items/1/why/en`, A `m04.json#/blocks/11/interaction/items/1/why/en`:

> GRADE D. The evidence is the maker's technical dossier; no independent randomized trial was found.

**Locked source:** PPG `.md:2906–2908`, Matrixyl 3000 printed p.56 / PDF p.58:

> Manufacturer and small cosmetic studies report reduced wrinkle depth and volume over 1–2 months vs placebo; independent peer-reviewed RCTs are limited. No drug level efficacy data.

PPG `.md:2923` names only the non-indexed Sederma/Croda technical dossier for this blend. “Limited” does not identify an independent RCT and cannot establish its existence. This is a verified wording difference, **not an independently verified trial contradiction**. Do not substitute trials of pal-KTTKS (Matrixyl) for Matrixyl 3000 (pal-GHK + pal-GQPR; PPG `.md:2916`).

**Proposal / owner:** request the exact claimed independent Matrixyl 3000 trial, full methods, blend/formulation, route, funding and affiliation information. Missing primary/dossier text stays visible; Dr. Hannah-Shmouni decides retain-with-search-rationale or a later authorized evidence-specific edit. Any newly proposed source needs the lock-amendment path; no grade change now.

**BPC: current** `tutor-m04-bpc157`, P `/tutorCorpus/7/answer/en`, A `m04.json#/tutorEntries/1/answer/en`, begins:

> BPC-157's evidence is rodent studies from one group plus uncontrolled case series; no randomized efficacy trial in people has been published in full (September 2026); the one randomized trial FDA found, in ulcerative colitis, exists only as a 2005 meeting abstract and showed no significant difference from placebo.

Contrast `m4-p13`'s already-quoted “mostly from one research group”, not “one group” absolutely. H's FDA allegation quotes:

> Twenty four articles describe pharmacological effects of BPC-157 in different in-vivo and in-vitro nonclinical models,57 and one article describes the in-vitro cytoprotective effects of analogues of BPC-157 (Bodis et al. 1997).

That is **historical unverified text**, not a locally confirmed FDA excerpt. Even taken literally it counts articles/models, not independent groups. The underlying briefing PDF/reference bibliography is not present in the reviewed corpus; C `m07.json:363–377` contains only its registry summary. H source metadata reports a historical PDF basis, not a local source artifact this task opened.

**Proposal / owner:** recover that already-registered FDA document's exact nonclinical section and cited-study affiliations; distinguish BPC-157 from analogues and independent groups from multiple models. Dr. Hannah-Shmouni to reconcile the tutor's absolute “one group” against the card's “mostly”. Do not infer independent replication, human skin efficacy or new trial status. No corrected clinical sentence is drafted here.

## 4. Chung 2019 — historical numeric challenge, primary table missing

**Current:** `c-m01-19`, P `/provenance/claims/219/text` contains:

> clinical improvement in that trial was described only in 'multiple participants'

The same characterization is in P citation 150's note and C `m01.json:532–547` / `m01.md:57`. Claim locations are `m1-p15`, `m1-p17`, `m1-p18`; that location list does not mean each repeats the sentence. Actual `m1-p15`, P `/curriculum/modules/0/units/0/blocks/19/tool/items/3/note/en`, A `m01.json#/blocks/19/tool/items/3/note/en`:

> Small pilots measuring tissue markers. One exploratory randomized trial of topical rapamycin (36 enrolled, 19 dropped out) lowered skin p16, and clinical change was only described. No adequately sized trial with clinical skin-ageing outcomes was found (September 2026).

**Existing registered reference:** `chung-2019-topical-rapamycin`, PMID 31761958, Geroscience 2019;41:861–869. H reports fulltext via NCBI BioC, PMCID PMC6925069, and this passage:

> Clinical assessment of the 13 subjects completing the study is presented in Table 2. Of the 13 subjects, all except 2 showed improvement in clinical signs of cutaneous aging.

H calls this 11 of 13 improved. The quote is **a historical report excerpt only**: Table 2 and the surrounding primary article are not present in the reviewed local corpus. Current registry summaries repeat the challenged characterization; they cannot settle it. No replacement statistic is verified or proposed as teaching language.

**Proposal / owner:** recover the already-registered article's Table 2, legend, clinical-assessment paragraph and participant-flow/analysis-set description. Dr. Hannah-Shmouni must reconcile enrolled, discontinued, evaluated and endpoint-specific denominators, clinical ratings versus tissue markers, treatment comparison and attrition before deciding any correction. Do not turn a completing-subject count into a response rate for all enrolled participants or into adequately powered skin-ageing efficacy. Then authorize a separate synchronized registry/card/tutor review if needed; no extra source is admitted by this request.

## 5. Appeal date — freshness question, no new legal finding

**Current:** `c-m07-12`, P `/provenance/claims/349/text`, C `m07.json` claim `c-m07-12` / `m07.md:81`:

> the appeal was pending as of the latest filings found (June 2026).

`m7-p09`, P `/curriculum/modules/6/units/0/blocks/12/stat/doesNot/en`, A `m07.json#/blocks/12/stat/doesNot/en`:

> How residues are counted can be contested: a court upheld FDA's count of 39 for retatrutide in 2025, and the appeal was still open at the latest filings (June 2026).

The same dated topic occurs in A `m07.json#/unit/tutorContext` and its P unit counterpart. Existing legal references: P citation 391 / C `m07.json:430–445`, district-court amended order, Document 48, 3 October 2025; P citation 392 / C `m07.json:448` onward, Seventh Circuit No. 26-1301, CourtListener docket 73173235. The registry describes a September 24 search with June 5 reply brief as the latest entry seen; these are reference annotations, not current docket text.

**Historical allegation:** H quotes “The court directs the parties to file supplemental memoranda addressing appellate jurisdiction.” Its note alleges proceedings through October 2026. The quoted sentence itself contains **no date or merits outcome**. H's source metadata records a failed November 12 HTTP 405 refetch with a cached copy retained. No dated underlying docket entries are available in the reviewed corpus to independently verify that newer chronology. Later filings would not by themselves refute “pending as of June”.

**Proposal / owners:** retain this as an unresolved freshness/temporal-scope review, not a verified reversal or termination. Request the dated, already-locked docket snapshot/entries supporting any newer statement, or a human-applied lock amendment for a later snapshot. Dr. Hannah-Shmouni and the named jurisdiction reviewer decide whether to retain an explicitly historical anchor or authorize a separately sourced update. **All newer legal claims remain unverified.** No web-based legal update or current appeal-status assertion was made.

## Verification and handoff

`claim-reconciliation-evidence.json` is the small deterministic companion: exact current-field substrings, authored mirrors, guide line ranges and historical assertion pointers. It is not a claims verdict file. The current excerpts above were checked as exact substrings of decoded JSON string fields; guide excerpts as exact substrings of the local Markdown and normalized passages of the locked PDFs.

Executed read-only verifier: `python3 /home/hermes/.hermes/cache/scratch/verify-hps-reconciliation.py` (exit 0):

```text
current-quotes: PASS 16; authored-mirrors: PASS 12
guide-quotes: PASS 7; matching PDF passages: PASS 7
historical-inventory: PASS 8 contradicted; BPC allegation: unverified
locked-PDF: PASS corpus/peptide-pocket-guide-2026-08-clinical-reference.pdf sha256=c533b43448507c9f6da16c4f6889639059dc198c0c0d9f244f9bfe45fbc61233
locked-PDF: PASS corpus/hormonaly-pocket-guide-2026.pdf sha256=1478266b0809a3e3b7bc08c0af00d3e654468486d2753a25b0d8f9b0dfcdb475
package-sha256: PASS 6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa
```

PDF verification initially stopped on `β4` extracted as `β 4`, then on a NUL extracted between `drug` and `level`; normalization was explicitly limited to Unicode NFKC, whitespace/case, that beta-digit spacing and NUL-to-space. Exact Markdown/JSON checks were not loosened. These are source-text matching checks, not a new clinical evidence panel.

A portable, simple read-only recheck of every companion current-content quote and authored mirror (run from academy root; uses only the standard library):

```sh
python3 -c 'import json,pathlib
r=pathlib.Path("."); e=json.loads((r/"course-production/optimization/2026-11-22/claim-reconciliation-evidence.json").read_text()); p=json.loads((r/"packages/hormones-peptides-skin.json").read_text())
def get(o,s):
 for k in s.strip("/").split("/"): o=o[int(k)] if isinstance(o,list) else o[k]
 return o
for q in e["currentQuotes"]:
 assert q["quote"] in get(p,q["pointer"]),q["id"]
 if "mirror" in q:
  f,s=q["mirror"].split("#"); a=json.loads((r/"course-production/hormones-peptides-skin/authored"/f).read_text()); assert q["quote"] in get(a,s),q["id"]
print("PASS: current excerpts and authored mirrors")'
```

The portable command above was also executed from this document: `PASS: current excerpts and authored mirrors` (exit 0). A separate read-only Python substring check compared all 21 block quotes in this packet against decoded current package strings, local guide text or the explicitly historical H strings: `packet-block-quotes: PASS 21` (exit 0). This checks transcription, not historical allegations' truth. Both `git diff --check` and `git diff --cached --check` returned no diagnostics (exit 0). Normal wrapper built-ins were invoked against `git diff --cached --no-ext-diff --unified=3` using `BUILTIN_CHECKS` from `/home/hermes/DrVibe/perceptor-foundry/tools/operator/guards.mjs` (local Foundry checkout `da10a0b3db1217824092188dc1d9c42009f60c82`):

```text
gate-scan: PASS — no gate touched
secret-scan: PASS — no secrets in added lines
```

No preprint is used as clinical support. No network-based source-resolution check, fresh claims panel, package build, playback verification or publication-readiness check was run. Primary-source gaps above remain unresolved despite the deterministic quote/guard passes. Only this packet and its evidence JSON are staged for the requested work-branch commit; the operator independently reruns its checks and cross-lab review.

Human queue: medical-owner review of each proposed disposition and exact missing evidence; jurisdiction-owner review for COA/legal scope; human-applied lock amendments only if recovered evidence is not already admitted. Cross-lab review and wrapper draft-PR handling remain with the operator. No human gate was opened, no existing report or teaching artifact changed, and no push, merge, deployment or message was performed.
