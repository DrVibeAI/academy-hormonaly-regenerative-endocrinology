---
name: perceptor-regional-localization
description: Adapt clinical microlearning courses to a language and practice jurisdiction, including fictional scenarios, terminology, product-specific regulatory notes, tutor context and editable motion-design media. Use for Perceptor/Hormonaly locale editions and regional audits; translation alone is not localization.
---

# Regional localization agent

Produce a reviewable locale edition with separate language and practice-country profiles. Reuse the academy's Foundry localization stage and existing materializer; do not create a second course engine. For the Hormonaly skin course, load [the current profile](references/hormonaly-skin.md). For implementation or runtime work, load [the CAIH adaptation pattern](references/caih-pattern.md).

## What changes, and what stays factual

- Language controls register, terminology, typography, RTL, narration and captions. Country/subnational authority controls regulatory and practice context. Never infer jurisdiction from Arabic, nationality, a name, or ethnicity. Respect a learner's declared country even when their language differs from its default.
- Keep the source package immutable. Derivatives retain IDs, answer keys, evidence grades, study populations, authors, outcomes and caveats. Record adaptations by field/block and source hash. A historical or foreign-regulatory example remains labelled as such; do not simply replace FDA with SFDA.
- Localize fictional patient/clinician names and settings consistently when it helps the scenario. If cases are unnamed, retain them unless a named continuity case serves a teaching purpose. Do not rename real faculty, researchers, institutions, medicines, or study locations. Use verified Arabic institutional names and useful Arabic generic terms alongside INNs/brand names; do not invent local brands or institutions.
- Preserve measurements and the cited study's units. Label any conversion and preserve its original value. Do not invent local reference intervals or transfer foreign professional titles/prescribing rights. Preserve UAE's diverse clinical workforce; avoid treating Arabic as a demographic stereotype.

## Construct the local layer

1. Read the source lock, audience/role definitions, existing country variants and target profile. Record source hash, locale, primary country, applicable subnational scope, optional comparison countries, named reviewer and media mode. Start from available evidence rather than re-asking known preferences.
2. Inventory every learner surface: lessons, cases, checks/final assessments, feedback, tutor retrieval keys/answers, source notes, onboarding, local-context choices, certificate wording, narration, film graphics and captions. Track media and UI coverage separately from prose.
3. Use an explicit block/topic-to-jurisdiction map. Do not select a clinical/regulatory rule by scanning the whole block for whichever drug name appears first. Keep country-specific notes next to the relevant lesson and provide a concise regional summary.
4. Browse current primary official sources for changed legal/product claims. Retain the authority, jurisdiction, exact product, active ingredient, formulation, route, indication, registration identifier when available, status, effective/source date, check date and supporting URL/section. Separate registration, indications, prescribing scope, facility licensing, compounding, import and advertising. A research-peptide notice is not a ban on all peptide medicines. No search result is not proof of a ban; unavailable records remain unverified.
5. Add new evidence through the academy's draft source-lock amendment. Identify the specific unverified products/pathways instead of writing a generic regulatory note that looks complete. When local evidence is missing, state the gap; never silently substitute another country's rules. Preserve country and route qualifiers in summaries, quizzes and tutor replies.
6. Reuse the source-constrained tutor. It should lead with the selected practice jurisdiction, label comparisons, detect regulatory questions in the learner's language, and abstain when local evidence is absent. Regulatory changes are editorial drafts, not live generated treatment permissions.
7. Materialize the derivative and run the existing package/schema, structural, numeric, coverage and RTL checks. Run `scripts/audit_locale.py SOURCE CANDIDATE --locale ar-AE --countries AE SA --output REPORT.json` for an additional regional inventory. Its passing result does not establish regulatory completeness or human approval.
8. Deliver concrete review artifacts and an honest coverage ledger (localized / source comparison retained / verification pending / media pending). Preserve `in_review` until the named reviewer acts. Production/local files may be created within the user's task; do not infer permission to email, publish, issue certificates or create recurring monitors.

## Slide-free microlearning media

Honor the declared `microlearning-motion` mode. Hormonaly uses microlearning cards and editable HyperFrames motion-design films, not a slide deck. Do not require, create, or translate slides for this mode. This is Omar's explicit October 7, 2026 course direction and takes precedence over generic slide-first guidelines.

Pin the original storyboard, composition, diagrams, assets, narration, word cues and hashes. Translate on-screen teaching labels separately from narration. Re-align to actual target speech; check Arabic shaping/RTL and mixed Latin abbreviations. Preserve source scientific diagrams rather than generate replacement scientific evidence. Reuse unchanged assets and cached paid media. Keep volatile regulations in editable cards/tutor context where possible so small legal updates do not force film rerenders. Use HyperFrames and the relevant media skills when rendering; course rules still govern the approved presenter/voice, source integrity, timing-shell QA and review gates.
