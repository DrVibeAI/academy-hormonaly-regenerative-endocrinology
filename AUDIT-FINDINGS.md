> Follow-up: repairs and current verification are recorded in [QA-FIXES.md](QA-FIXES.md). The findings below describe the pre-repair audit.

# Hormonaly Arabic edition — QA and audit

**Result: not ready for release.** The profile-menu overlap is corrected. The build and core Arabic text coverage pass, but there are **three high-priority defects**, four medium-priority defects and two lower-priority evidence issues.

Audited 7 October 2026 (Los Angeles). Scope: the local Arabic candidate at http://127.0.0.1:5197/, academy commit `0db635f`, runtime commit `3653fe2`. Exact hashes are in [scope.json](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/scope.json). The baseline is the previously verified serving Hormonaly snapshot `academy-hormonaly-00051-54r` / runtime `7209291`; this audit did not re-query deployment traffic or establish that no newer deployment exists.

Read-only audit under the [audit charter](/Users/omar/DrVibe/perceptor-foundry/docs/audit-charter.md). No implementation, course content, governance, catalog, deployment or production data was changed. Browser checks used guest preview and development preview routes; no assessment was submitted or certificate issued.

## Findings

### A01 · P1 · The Arabic homepage claims accreditation that the Arabic package does not hold

**Location:** [Arabic review configuration:289](course-production/hormones-peptides-skin/arabic-uae-20261007/academy.ar-AE.review.yaml:289), [catalog-summary.mts:49](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/scripts/catalog-summary.mts:49), [academy-home.tsx:70](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/academy-home.tsx:70). URL: http://127.0.0.1:5197/?home

**Evidence:** The review catalog retains `accreditation.status: accredited` from the English release. The Arabic package explicitly has `not_submitted` and no approvals. The summary importer passes through the catalog accreditation independently of package status; the homepage displays a GCLS badge, “GCLS-accredited certificate” and an accreditation statement beside Arabic copy saying the edition is under review. This is a visible contradiction, even though publication remains blocked.

**Suggested fix:** Bind accreditation presentation to the exact course edition and its recorded decision. Suppress the inherited badge and certificate claim for this derivative until the appropriate approval exists; retain the English source record unchanged. Add a regression check for a pending derivative using an accredited source catalog.

[Full homepage evidence](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/homepage-mixed-language.png).

### A02 · P1 · The regional summary omits all six substantive UAE/Saudi notes from the learner view

**Location:** [materialize.mjs:54](course-production/hormones-peptides-skin/arabic-uae-20261007/materialize.mjs:54), [App.tsx:2216](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/App.tsx:2216). Block: `m7-ar-uae-sa-context`.

**Evidence:** The materializer stores six product/regulatory rows in `points` on a block of type `action`. The action renderer never renders `points`; it displays the short scope statement twice and a “my next step” input. The SFDA unregistered-product explanation, semaglutide note, research-peptide uncertainty, Abu Dhabi restrictions, EDE check and outstanding product checks are therefore absent from this summary card. Reproduced through the local development route `?lesson=7&pane=28&tutor-preview=1`. This finding concerns the summary; the separate lesson country notes still exist.

The same block has no chips or suggestions, producing the strict interaction-audit failure. Action completion also checks for a typed note at [App.tsx:1305](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/App.tsx:1305).

**Suggested fix:** Use a supported informational rendering for all six notes and their sources, or an explicit structured interaction. Do not make a regulatory information card depend on arbitrary typed text for completion.

[Rendered regional card](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/regional-addendum-missing-details.png).

### A03 · P1 · The fallback tutor does not reliably answer for the selected practice country

**Location:** [tutor.ts:68](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/tutor.ts:68), [tutor.ts:196](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/tutor.ts:196), [App.tsx:2571](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/App.tsx:2571).

**Evidence:** With Arabic and UAE selected, “هل يسمح بحقن GHK-Cu في أبوظبي؟” returns a grounded answer describing US and UK rules, without the relevant Abu Dhabi rule. Those foreign jurisdictions are labelled, but they do not answer the local permission question. With Saudi Arabia selected, “هل جميع الببتيدات ممنوعة في السعودية؟” abstains despite the prepared Saudi corpus entry. Retrieval matches literal key substrings; it does not apply the local regulatory overlay before selecting the authored answer. This fallback is also used when the grounded service returns no answer.

Arabic platform help has the same retrieval weakness: “كيف أغير لغة التطبيق؟” abstains. The prepared help answers have Arabic prose but no Arabic matching keys.

**Suggested fix:** Apply explicit jurisdiction/topic routing and Arabic intent handling to the deterministic fallback too. Return the relevant reviewed local note or a local verification gap; retain foreign rules as labelled comparisons. Add course-specific Arabic fixtures with natural paraphrases and both AE and SA contexts. The configured course fixture file is currently absent.

[Exact prompts and replies](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/arabic-tutor-probes.json). This reproduces the local/fallback engine, not the live model-backed tutor.

### A04 · P2 · Saudi lesson notes are outside the package's formal jurisdiction map

**Location:** [materialize.mjs:56](course-production/hormones-peptides-skin/arabic-uae-20261007/materialize.mjs:56), candidate `jurisdictions` and `metadata.variants.jurisdiction.SA`.

**Evidence:** There are 30 Saudi lesson notes, but declared jurisdictions remain US, GB, EU, PT, BR and AE. The strict citation audit reports 30 unmapped Saudi notes and 21 Saudi notes with empty `citationRefs`: 51 findings. The coverage auditor passes because it checks note presence and ID resolution, not this contract.

Many empty-reference notes honestly state that product verification is outstanding. Their absence of evidence must not be “fixed” by attaching an unrelated citation or converting uncertainty into a legal assertion.

**Suggested fix:** Declare Saudi Arabia with accurate review owners and pending layer status. Represent unsupported product checks as explicit review gaps; attach product-specific evidence only where it supports the statement. Re-run the strict citation and jurisdiction gates.

[Package-check output](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/package-check.log).

### A05 · P2 · Arabic coverage stops short of an end-to-end learner experience

**Location:** [academy-home.tsx:53](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/academy-home.tsx:53), [App.tsx:3279](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/App.tsx:3279), [site-defaults.json:31](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/config/site-defaults.json:31), [review configuration:627](course-production/hormones-peptides-skin/arabic-uae-20261007/academy.ar-AE.review.yaml:627).

**Evidence:** Homepage navigation, sign-in, module/hour/source labels, FAQ heading and certificate details remain English. Its local helper only supplies Spanish, English and Portuguese. Library headings render “Module 1” and “35 sources”; the Arabic module-label value itself is English. Profile “Center” displays “United Arab Emirates” because the original bare-string center has no Arabic label. The legal pages remain English, with an honest Arabic notice explaining this. The final regional card also exposes an English “Finish module” accessibility label.

The 3,797-field translation pass covers original course maps, not all of these newly inherited runtime and legal surfaces. Original publication titles and real faculty names may appropriately remain as published.

**Suggested fix:** Audit rendered chrome independently of the package translation inventory. Complete Arabic labels, country/center labels, durations and accessibility names. Prepare reviewed Arabic terms/privacy documents with proper versioning before claiming an end-to-end Arabic release.

[Homepage](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/homepage-mixed-language.png) · [Library](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/library-mixed-labels.png) · [Terms](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/terms-english.png).

### A06 · P2 · Opening-film reference playback is broken in the Arabic preview

**Location:** [prepare-preview.mjs:1](course-production/hormones-peptides-skin/arabic-uae-20261007/prepare-preview.mjs:1), [App.tsx:1241](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/src/App.tsx:1241), [import-package.mts:138](/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/scripts/import-package.mts:138). URL: http://127.0.0.1:5197/#/lesson/1/2

**Evidence:** M1 displays its poster and controls, but the accessibility tree reports “Unable to play media.” The video element has no source and `readyState: 0`. The preview changes the base locale to Arabic and strips protected delivery, while the seven film assets remain English. All seven original files exist locally; this is a preview selection/transport issue, separate from the known absence of Arabic films.

**Suggested fix:** For local editorial review, provide an explicitly labelled English reference source through an intentional preview path, or show a clear pending-media state without nonfunctional player controls. Preserve production authentication. Produce and review the Arabic films/captions separately.

[Film evidence](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/opening-film.png).

### A07 · P2 · The standard caption scan cannot finish because the preview links back into itself

**Location:** [prepare-preview.mjs:4](course-production/hormones-peptides-skin/arabic-uae-20261007/prepare-preview.mjs:4), [caption-audit.mjs:35](/Users/omar/DrVibe/worktrees/perceptor-foundry-skin-locales-20260929/tools/qa/caption-audit.mjs:35).

**Evidence:** `preview-inputs/course-production` symlinks to its ancestor academy's `course-production`. The recursive audit uses `statSync`, follows the link repeatedly and terminates with `ENAMETOOLONG`. The full `perceptor check` exits 1. This is a real validation failure, not a bad caption finding.

**Suggested fix:** Put generated preview inputs outside the scanned source tree or avoid the recursive link. Make scanners cycle-safe and explicitly exclude generated inputs. A targeted scan of the seven recovered English tracks completed: 168 cues, no blocking timing/format findings, one 1.14-second cue warning. That does not approve their content or establish Arabic caption coverage.

### A08 · P3 · Preview-only film badges fail locale parity

**Location:** [prepare-preview.mjs:3](course-production/hormones-peptides-skin/arabic-uae-20261007/prepare-preview.mjs:3).

**Evidence:** All seven injected `videoBadge` maps have Arabic only, while the generated preview declares Arabic and English. Runtime parity checks 3,866 fields and reports seven missing English badge values; quiz structure has no reported issue.

**Suggested fix:** Supply both preview labels, or separate preview annotations from bilingual learner content without weakening the locale check.

[Parity result](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007/parity-eval.json).

### A09 · P3 · The downloadable review bundle predates the overlap correction evidence

**Location:** `Hormonaly-Skin-Arabic-Review.zip` and [ACCOUNT-NAVIGATION-QA.md](course-production/hormones-peptides-skin/arabic-uae-20261007/ACCOUNT-NAVIGATION-QA.md).

**Evidence:** Comparing archive entries with current source files finds a stale `ACCOUNT-NAVIGATION-QA.md`. The corrected `account-menu-overlap-fixed.jpg` is absent. The existing mobile-menu evidence was captured before the overlap fix.

**Suggested fix:** Rebuild the review archive after triage, include current screenshots/audit findings, and update its checksum manifest. Keep old evidence clearly dated if retained.

## Verified passes and limits

| Check | Result |
|---|---|
| TypeScript, isolation, locale-source scan, Vite production build | Pass. Vite warns about future native-config compatibility and large chunks; no build failure. |
| Arabic candidate schema | Pass against the matching Foundry checkout. |
| Original localized fields / protected structures | 3,797 / 713 checked; no missing/blank Arabic fields, protected-structure drift or unresolved citation IDs in that coverage audit. This is not semantic medical approval. |
| Local package assets | All 110 asset paths exist, including 48 Arabic narration files. |
| Arabic audio integrity | 48 checksums match the manifest; 74.364 minutes total. M1 narration plays in-browser at 93.28 seconds, readyState 4. Pronunciation not approved. |
| Account menu | Phone 458×934 and desktop 1280×720 checked; opaque surface, menu z-index 1100, no horizontal overflow in sampled views. Escape closes and restores focus; desktop Tab/Shift+Tab wrap; certificate destination opens. |
| Main navigation and library | Four learning destinations; profile accessed through the name. Library module expansion works. |
| Focused automated tests | 30 checks pass. One attempted card-course locale test is inapplicable: this legacy course does not generate `server/generated/learning-course.json`. It was not counted as a pass. |
| Generic authored tutor suite | 20 assertions pass, but no academy-specific fixture file exists and the generic cases do not establish Arabic regional behavior. |
| Additional Arabic probes | Personal-dose request refuses; UAE and Saudi emergency prompts route to immediate care without inventing phone numbers. Regulatory/help failures are A03. |
| Public auth probes | Unauthenticated GETs to [certificate API](https://hormonaly.perceptors.ai/api/certificate) and [admin overview](https://hormonaly.perceptors.ai/api/admin/overview) return 401. Non-admin authenticated access was not tested. |
| Full package / final release gates | Fail. Details in the saved package-check and final-gate logs. |

The original canonical English package remains at SHA-256 `6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa`.

## Regulatory source spot-check

The current [SFDA notice](https://sfda.gov.sa/ar/news/19668) concerns unregistered peptide products and unauthorized marketing. The draft's refusal to infer a class-wide ban is consistent with that notice. The [DoH standard](https://www.doh.gov.ae/-/media/61BBC1A0A8EA45FCB3BBB9F30B034C83.ashx), section 3.34 and Appendix 2, supports an Abu Dhabi-specific restriction framework with route qualifiers; it should not be presented as a Saudi list.

The [EDE directory](https://www.ede.gov.ae/en/drug-directory) is reachable, but its landing page does not verify every individual product. The SFDA semaglutide PDF could not be re-fetched in this audit. No new product permission, prohibition or registration status was established from those unsuccessful checks. These spot-checks do not replace the complete source-lock and product review.

## Release requirements still open

- Fady's Arabic medical/language decision, including narration pronunciation and scientific figure review; 0/7 Arabic modules have recorded medical approval.
- Fresh claim-support verification tied to this exact derivative, regulatory source-lock amendment review, and completion/disposition of UAE/Saudi product and pathway gaps.
- Seven Arabic opening films, Arabic on-screen text and timed captions, with exact-render media QA and human approval. English source timing recovery is not target-language media approval.
- Reviewed Arabic legal surfaces, product-owner acceptance, applicable accreditation decision and publication authorization.

The final gate reports 10 failed items out of 27. Its “assessments approved” pass is a structural/status-field result and must not be interpreted as Arabic reviewer approval. The dead-screen audit inspects base English and reports zero analyzed seconds here; its green exit does not verify the future Arabic films.

Two other automated outputs need triage rather than blind content edits: the design scanner flags a cached SFDA source HTML page for its external icon framework, and the narration checker flags nine Arabic colon constructions. Neither alone proves a learner-facing design violation or invalid Arabic narration.

## Coverage boundaries and follow-up order

All five audit layers were sampled: package/claims, schema/gates, runtime, visible product and deployment tooling. Security review was focused on auth boundaries, bounded inputs, parameterized database call sites and existing negative-path fixtures; it was not an exhaustive penetration test. Deployment scripts were read only. No live sign-in, terms acceptance, payment, model-backed tutor, cloud progress synchronization or certificate issuance was exercised. The 416-source corpus was not freshly adjudicated claim by claim.

Triage A01–A03 first, then A04–A07, then regenerate parity/evidence for A08–A09. Re-run the affected checks after repairs and perform native acceptance on the exact release candidate. Keep the Arabic edition `in_review`, `mediaComplete:false`, `publishReady:false`.

Raw logs, exact prompts and screenshots: [audit evidence folder](course-production/hormones-peptides-skin/arabic-uae-20261007/audit-20261007).
