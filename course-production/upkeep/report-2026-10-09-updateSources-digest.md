# Jurisdiction updateSources digest — watchlist: hormonaly/hormones-peptides-skin

**Date:** 2026-10-09 · **Agent:** Daedalus (cron, perceptor-operator) · **Status:** WARN

## Scope

Package `packages/hormones-peptides-skin.json` v1.1.0 (generated 2026-09-24).
The package has no literal `updateSources` key — the jurisdiction block is
`jurisdictions[]`: 6 jurisdictions (US, GB, EU, PT, BR, AE) × 4 layers
(product/claims/practice/locale), all `status: mapped`. Review of record:
Fady Hannah-Shmouni, MD FRCPC (US 2026-09-24/25; other jurisdictions confirmed
2026-09-26). Underlying research: 2026-09-25 (US statements dated September 2026,
checked 2026-09-24).

The mapping is internally consistent and medically confirmed. It is ~2 weeks old.
Fresh check of the most volatile authorities (FDA compounding, MHRA enforcement/
safety) against the package text found **no statement that is now false**, and
two developments the package predates that a re-verify should pick up.

## Findings (candidates for clinical update / source-lock amendment)

### 1. FDA 503B bulks-list proposed rule — final determination still pending (WARN, US; modules 03/07)

- Proposed rule 91 FR 23431 (2026-05-01) to exclude semaglutide, tirzepatide,
  liraglutide from the 503B bulks list; comment period extended and closed
  2026-07-30; final rule not issued as of 2026-10-09.
- Source: https://www.fda.gov/news-events/press-announcements/fda-proposes-exclude-semaglutide-tirzepatide-and-liraglutide-503b-bulks-list · https://www.govinfo.gov/app/details/FR-2026-05-01/2026-08552
- Affected units: Module 3 (incretin/facial-architecture regulatory lines),
  Module 7 (m7 compounding-framework lesson). No statement in the package is
  falsified (the package correctly dates US status to September 2026), but the
  pending final rule is the single most likely near-term change to US
  compounding status in the course.

### 2. PCAC July 2026 vote outcomes not in the package (AMENDMENT CANDIDATE, US; modules 04/06/07)

- The package cites the advisory-committee meeting of 23–24 July 2026
  (m4-p16, m6 blocks, m7-p notices, claims[282]) and correctly states the votes
  are advisory and rulemaking is required. It does **not** record the vote
  outcomes: the committee recommended ~6 peptides for the 503A bulks list,
  including BPC-157 (8–6, over FDA staff advice to reject), while FDA's own
  review staff had weighed against BPC-157 (claims[347] covers staff
  conclusion only). No rule had been published as of 2026-10-02.
- Sources: https://www.ajmc.com/view/peptide-regulation-debate-intensifies-after-fda-advisory-panel-s-controversial-vote · https://www.fda.gov/media/94155/download (category lists, May 14, 2026)
- Affected units: Module 4 (m4-p16 "Where does it stand in the US?", the
  bulks-list ordering interaction), Module 6 (GH-secretagogue status lines),
  Module 7 (compliance lesson), tutor corpus entries on BPC-157, assessment
  q10/q13 rationales.
- Suggested amendment: add the recorded vote outcomes (with the advisory-only
  caveat the course already teaches) to m4-p16 and the tutor corpus so learners
  see that the committee has recommended listing while FDA staff disagreed —
  the exact "review is not approval" teaching moment the course builds.

### 3. MHRA enforcement line — already current (OK, GB; module 07)

- The package's MHRA enforcement statements (finasteride May 2026 warnings,
  retatrutide, the May 2026 seizure including peptide products) match the
  published record (2026-05-29 largest seizure; May 2026 Drug Safety Update).
- Source: https://www.gov.uk/government/news/two-arrested-during-the-mhras-largest-ever-seizure-of-unlicensed-weight-loss-medicines · https://www.gov.uk/drug-device-alerts/mhra-safety-roundup-september-2026 (September 2026 roundup contains nothing touching the course's molecules).

## Not checked / limits

- EU/PT/BR/AE authority feeds were not individually re-scanned this run; their
  mapped statements were confirmed by the reviewer of record on 2026-09-26.
- No live fetch of fda.gov/drugs/human-drug-compounding succeeded from this VM
  (HTTP error); FDA items rest on press/Federal Register/secondary corroboration.
- No files changed; nothing committed; no expert run used.

## Recommendation

File a lock-amendment request for item 2 (PCAC vote outcomes) whenever the
package is next touched; re-check item 1 on the next watchlist run (final
rule could drop any week).
