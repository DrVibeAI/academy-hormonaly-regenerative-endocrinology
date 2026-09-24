# Authoring brief — Hormones and Peptides for Skin (modules 01–03, 05–07)

Module 04 is the approved pilot (Dr. Fady Hannah-Shmouni approved it 2026-09-24). Every other module must match it in
rigour, shape and voice. Read these first, in this order:

1. `authored/m04.json` — the authored module (the exact file shape you produce).
2. `citations/m04.json` — the verified, graded literature registry (the exact file shape you produce), including `gradingRule`.
3. `review/m04-draft.md` — the same module as a reader sees it.
4. `source-lock.md` — what is in and out of the lock. `module-specs.md` — your module's objective, lessons and source sections.
5. `runtime-gaps.md` — what the learner app can and cannot render.
6. Corpus text: `../../corpus/hormonaly-pocket-guide-2026.md` (A&RE, the spine) and
   `../../corpus/peptide-pocket-guide-2026-08-clinical-reference.md` (PPG-Aug, skin-relevant entries only). Page markers
   `<!-- page N -->`. The approved plan's section map for your module is in `intake-handoff/source-map.json` (`sources[].sections[]`).

## What you produce (only these files — touch nothing else)

- `citations/mNN.json` — same shape as m04: `module`, `verifiedAt`, `verification`, `gradedAt`, `grader`, `gradingRule` (copy m04's
  verbatim), `finalReviewer`, `citations[]` (each with `grade` + `gradeNote`), `claims[]`, `authorFindings[]`.
- `citations/mNN.md` — generate it the same way m04.md is laid out (sources per lesson with grades; claims table; author findings).
- `authored/mNN.json` — same shape as m04: `module`, `authoredAt`, `status: "ai_draft"`, `unit`, `lessons` (3), `blocks`, `check`,
  `claimLocations`, `audienceLevelPanes`, plus two NEW keys: `courseQuiz` (exactly 2 questions for the final course quiz, schema
  `$defs.question`: `id`, `prompt`, `options[{text, why}]` ×3, `correct`, `rationale`, `pillar`, `citationRefs`) and `tutorEntries`
  (2 entries, schema `$defs.tutorEntry`: `id`, `keys[]` (6–12 lowercase phrases a learner would type), `answer` {en}, `citationRefs`,
  `scope` "mNN").
- Optional: research runs under `../research/` via `node /Users/omar/DrVibe/perceptor-foundry/bin/perceptor.mjs research --topic
  "<3–5 words>" --max 20`, run from the academy root (`/Users/omar/DrVibe/academy-hormonaly-regenerative-endocrinology`). Long
  topics return 0; OpenAlex rate-limits back-to-back runs (wait ~20 s).

Do NOT edit `build-package.py`, `packages/*.json`, `academy.yaml`, other modules' files, or anything in other repos. Do NOT git
commit or push — the lead commits. Do NOT start servers.

## Literature (stage 10 for your module)

- Every citation is verified live: PMIDs via NCBI E-utilities (`esummary`/`efetch`, compare title, first author, journal, year);
  trials via `https://clinicaltrials.gov/api/v2/studies/<NCT>`; regulators (FDA, Federal Register, MHRA, EMA) fetched live; open-access
  full text via Europe PMC when you need to confirm what a paper says. Keep to ~3 requests/second. Never cite from memory, never
  invent an identifier. If a guide reference does not resolve, record it in `authorFindings`.
- The two guides are single-author secondary sources: they locate a claim; a primary study, meta-analysis, guideline or regulatory
  record settles it. Cite the guide as well when the lesson reports the guide's own rating or recommendation.
- Grade every source with m04's `gradingRule` (A–D or `context`) and a one-line `gradeNote`. Where the two guides disagree, or
  newer independent evidence contradicts a guide's grade, teach the evidence and add an author finding (m04's oral-collagen pattern).
- 15–35 sources per module is typical. Every registry source must be cited by at least one block (the citation audit fails on
  unused sources); move considered-but-unused ones to `consideredNotUsed` with a reason.
- Claims: one per load-bearing teaching statement (10–20). `status: "verified"` when the cited sources support it as worded
  (grading was delegated to the agent by Omar on 2026-09-24); if nothing supports it, rewrite it as an absence/reported statement or
  drop it. `unit` = `mNN-l1|l2|l3`; ids `c-mNN-01…`.

## Content rules (non-negotiable)

- **No dosing, titration, reconstitution, stacking, sourcing or administration instructions — anywhere**, including tutor answers
  and quiz options. Hormone therapy is taught as evidence, indication boundaries and safety, never as a regimen.
- **Four registers kept apart**: mechanism · human evidence · regulatory status · open question. Never blend them in one sentence.
- **Regulatory statements name their jurisdiction and date** ("In the US, as of …"). UK/EU mapping is pending: do not assert
  UK/EU status unless you verify it from MHRA/EMA and cite it.
- **Audience = all clinicians.** Base copy is role-neutral. On 2–4 "what changes in practice" moments add
  `metadata.variants.audienceLevel` = {`prescriber`, `clinical-staff`, `advisor`} (each `{"en": …}`), as m04 does. Grades and facts
  never vary by role. Only **module 01** carries the role router: its `m1-p02` is a `reflection` identical in function to `m4-p02`
  (values `prescriber`, `clinical-staff`, `advisor`), worded for the course start ("How will you use this course?").
- **CME**: the course is "designed toward future CME accreditation"; never state or imply that credit is available.
- **Learner-facing language**: no internal words ("lock", "registry", "claim", "draft", "A&RE", "PPG"). Name the guides as
  "the Aesthetic & Regenerative Endocrinology guide" / "the Peptide Pocket Guide" or "the Hormonaly guides". Voice = Module 04's:
  clear, precise, calm, second person, no hype, no "revolutionary/seamless", no exclamation marks.
- **Fictional cases are labelled fictional.** No invented trial results, statistics or regulatory facts.

## Runtime constraints (the learner app — see runtime-gaps.md)

- Block `type` ∈ {`title`, `audio`, `stat`, `tool`, `quiz`, `reflection`, `action`} only. Anything else renders a blank screen.
- A `scenario` interaction goes on an `audio` block (m4-p17). `hotspots` need images — do not use.
- 2–4 interactions per module, of at least two kinds (`classify`, `quickfire`, `scenario`, `reveal`, `chips`), on no more than half
  the moments; the last moment is an `action` with a `chips` interaction and `action.suggestions` (m4-p19).
- **Never leak answers**: a `tool` block's items render ABOVE its classify/quickfire exercise, so tool items must not state the
  answers; put grades/verdicts in the item `why`s (m4-p09, m4-p16).
- Every `stat` has `means` and `doesNot`. Every quiz has exactly 3 options, one correct, a `why` on each, plus `feedback`, `pillar`
  and `citationRefs`. Each lesson ends on a quiz (`Your turn`); the module has a `check` (m04 pattern).
- Every `audio` block has `audioBeats` (3) and `metadata.audioScript` (~110–170 words). Narration rules (the tic audit fails them):
  no label-colons ("X: y") in scripts, no "not X but Y" / "is not X — it's Y" pivots, no sentence starting with "No"/"Not",
  no trailing ", not Y." fragments, no "In this lesson/module…" meta openers.
- Ids: blocks `mN-pNN` (N without leading zero, e.g. `m1-p01`), 16–20 moments, `time` "01 / N". Lessons: 3, ids "N.1"–"N.3", using the
  lesson titles in `module-specs.md` (you may tighten wording). `unit.id` = `mNN-story`, `type` "story", `estimatedMinutes` 22–28.
  `tutorContext` = a dense factual summary with the key grades and boundaries (m04 pattern); `tutorKeywords` 15–25.
- Every non-title/reflection/action block has `citationRefs`, each id present in your registry or one of the two guide ids
  (`hannah-shmouni-2026-are`, `hannah-shmouni-2026-ppg-aug`).

## Checks you must pass before you finish

From the academy root:
```
python3 course-production/hormones-peptides-skin/build-package.py
node /Users/omar/DrVibe/perceptor-foundry/bin/perceptor.mjs check packages/hormones-peptides-skin.json
node /Users/omar/DrVibe/perceptor-foundry/tools/qa/narration-tic-audit.mjs packages/hormones-peptides-skin.json
node /Users/omar/DrVibe/perceptor-foundry/tools/qa/interaction-audit.mjs packages/hormones-peptides-skin.json
```
Your module must show: package valid; 0 citation-audit findings attributable to your module; tic audit 0 for your `mN-` ids;
interaction audit 2–4 interactions for your module with no warnings. (Other agents are writing other modules at the same time — ignore
their findings; the `academy.yaml catalog[0]` failure is pre-existing.) Then also run
`python3 course-production/hormones-peptides-skin/review/make-review.py mNN` and read the result as a clinician would.

Report back: moments, interactions, sources (by grade), claims (verified/flagged), author findings, and anything you were unsure of.

- **Shared sources:** before adding a source, check the other `citations/*.json` registries; if the same paper is already registered, reuse its exact `id` (the build keeps the first registration).
