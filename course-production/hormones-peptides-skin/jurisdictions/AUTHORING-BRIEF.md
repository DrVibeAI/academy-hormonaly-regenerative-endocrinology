# Jurisdiction notes — module authoring brief (Hormones and Peptides for Skin)

Omar decided on 2026-09-25 that the course gives regulatory status for **US, UK, EU, Portugal, Brazil and the UAE**, in English.
The runtime now shows each learner the regulatory note for their own country on a moment, with the other jurisdictions one tap
away (`metadata.variants.jurisdiction`). You own ONE module file (`authored/<mNN>.json`) and edit nothing else.

## Inputs (read first)

- `authored/<mNN>.json`: your module. Every module is medically approved; every edit you make is logged for re-confirmation.
- `citations/jurisdictions.json`: the shared registry built from the research. `citations[]` are primary sources (ids `eu-…`,
  `pt-…`, `br-…`, `ae-…`); `claims[]` are the quote-backed statements (ids `j-eu-01`…), each with `jurisdiction`, `subject`,
  `substanceStatus`, `text` and the verbatim quote in `reviewNote`. `consideredNotUsed` lists what could NOT be verified.
- `jurisdictions/<CODE>.json`: the full research files, if you need context. Do not edit them or the registry.
- `citations/<mNN>.json`: your module's existing registry, for the US and UK source ids already used.
- `skills/perceptor-authoring/references/module-agent-brief.md` in the foundry (`~/DrVibe/worktrees/foundry-automation-20260924`),
  section "Multi-jurisdiction courses".

## Which moments

Only moments that state a **regulatory status or rule**: a substance's authorisation, prescription-only or controlled status,
compounding or unlicensed-medicine routes, research-use-only and import rules, cosmetic vs medicine borderline, food-supplement
claims, advertising to the public, enforcement. Moments that mention a regulator in passing (e.g. an FDA label as an evidence
source) are not regulatory moments. Notes render on `audio`, `stat`, `tool`, `action` and `reflection` blocks. `quiz` and `title`
blocks never show notes: leave them unchanged (if a quiz tests a US-only fact its stem must already name the US; flag it in your
report if it does not).

## What to change on each regulatory moment

1. **US stays in the base copy, unchanged.** It is the reviewed teaching, cited to FDA and US law.
2. **UK text moves into a `GB` note, verbatim.** The UK sentences added on 2026-09-25 ("In the UK, …") leave `body`/`points`/tool
   notes and become `metadata.variants.jurisdiction.GB = {"text": {"en": …}, "citationRefs": [the UK source ids they already cite]}`.
   Keep the wording exactly (Fady is confirming it); only join sentences if they were split. If a UK sentence is inseparable from
   the teaching (a UK column in a comparison table), leave it and say so in your report.
3. **Add `EU`, `BR` and `AE` notes** from `citations/jurisdictions.json`, and a **`PT` note only where Portuguese law adds to or
   differs from the EU note** (INFARMED specifics, magistral/officinal preparation rules, national advertising or supplement rules);
   a Portuguese learner otherwise reads the EU note. Each note: one or two sentences, plain English, starts with the jurisdiction
   ("In the EU, …", "In Brazil, …", "In the UAE, …"), dated where the source is dated, and states only what a registry claim states.
   Stay as close to the claim's `text` as the moment allows; never add facts. `citationRefs` = that claim's `citationRefs`.
   **UAE notes** start with the federal position (the Emirates Drug Establishment, EDE, has held medicines registration since
   Federal Decree-Law 28/2023; the medicines law is Federal Decree-Law 38 of 2024). Where Dubai (DHA) and Abu Dhabi (DoH) differ —
   peptides above all: DHA 29 July 2026 vs DoH 31 July 2026 — say so in the same `AE` note, naming each emirate (up to three
   sentences for AE only).
4. **Record placement**: for every registry claim a note uses, add `claimLocations["j-xx-NN"] = [block ids]` in your module.
5. **Nothing verified, no note.** If the registry has no statement for a substance in a jurisdiction (or lists it under
   `consideredNotUsed`), omit that jurisdiction's note on that moment. Absence statements keep the registry's strength exactly:
   "no registered medicine containing KPV was found in ANVISA's register (25 September 2026)" never becomes "KPV is not authorised"
   or "KPV is illegal". Only a regulator's own explicit statement (e.g. ANVISA's 2 July 2026 notice naming BPC-157) supports
   "not authorised" or "illegal", and the note then names who said it and when.
6. **m7-p21 and m7-p22** (module 07 only) were written as UK-only moments. Make them the "outside the US" moments: base copy states,
   in a sentence or two, what holds across the non-US jurisdictions in the registry (no 503A/503B-style bulk-substance lists; unlicensed
   or magistral routes under prescriber responsibility; no advertising of prescription-only medicines to the public), with UK
   specifics moved verbatim into the `GB` note and the other jurisdictions' specifics in their notes. Keep the moment ids.
7. **Tutor**: in `tutorEntries` and the unit `tutorContext`, remove statements that EU status is "not covered". Do not paste six
   jurisdictions into tutor answers; the Guide reads the notes directly.
8. **Role notes** (`metadata.variants.audienceLevel`) do not change, except to remove a UK-only instruction that now sits in a GB
   note (log it).
9. **Course disclaimers, blurb and the package's jurisdiction list** are NOT yours; the integrator updates them.

## Hard rules

- No dosing, titration, reconstitution, stacking, sourcing or administration instructions anywhere. Status and rules only.
- Four registers stay apart: mechanism, human evidence, regulatory status, open question. Notes are regulatory status only.
- No evidence grades, safety statements or clinical claims change.
- Learner-facing language: no internal words ("registry", "claim", "lock", "draft", source ids).
- Log every edited block in `postApprovalChanges`:
  `{"date": "2026-09-25", "block": "<id>", "change": "<one line: what moved or which notes were added>", "forReview": "Fady Hannah-Shmouni"}`.
  One entry per block. Moved UK text says "UK text moved verbatim into the UK note"; added notes list the jurisdictions.
- Keep the JSON valid; do not reformat untouched parts of the file (load, edit, write with the same indentation as the file).
- Do not commit, push, deploy or send anything.

## Report back

Blocks edited (by id, with jurisdictions added), UK text moved vs left in place (and why), registry claims used, claims you wanted
but the registry lacked, quizzes that test a US-only fact without naming the US, and anything a clinician would find surprising.
