# Arabic Hormonaly Academy — QA repairs, 7 October 2026

The reported runtime and preview defects are repaired and verified locally. Saudi product verification remains an explicit release blocker; this is not a medical, linguistic, legal or accreditation approval. Production was not deployed.

| Finding | Repair and result |
|---|---|
| A01 · accreditation | Homepage badges now require this package's matching accreditation decision, rather than inheriting the English catalog's badge. The Arabic package remains `not_submitted`. Tests cover missing, pending, matching and different-body decisions. |
| A02 · hidden regional notes | The final card now renders all six country/product notes in a readable stacked layout, labelled as a review draft. No text-input exercise hides the content. Browser inspection finds six rendered notes. |
| A03 · Arabic tutor | Shared Arabic intent recognition covers permission/prohibition paraphrases. Package-owned country notes supply deterministic regulatory answers for UAE/Saudi questions. Missing products/jurisdictions return an explicit gap; requested comparisons are labelled. Arabic platform-help matching works. The actual Abu Dhabi GHK-Cu browser question now returns the scoped DoH/EDE draft, not US/UK guidance. |
| A04 · Saudi mapping and gaps | Saudi Arabia now has a jurisdiction profile with all four layers in review and a named owner. All 21 unsupported product-note checks are registered as pending review tasks. Strict citations still report these 21 gaps; no unrelated citations, permissions or bans were invented. This finding remains open for product-level evidence and reviewer disposition. |
| A05 · Arabic surfaces | Homepage navigation/statistics/certificate labels, library module/source labels, country/center labels and the finish-button accessibility name are Arabic. Terms/privacy now have complete Arabic draft translations, source version/hash, RTL display and a visible legal-review-pending notice. English source wording remains intact. Real faculty names and publication titles retain their published form. Human legal review is still required. |
| A06 · reference playback | All seven English reference films play locally (`readyState:4`, no media errors), with explicit English-reference/Arabic-in-production labels. Transcript language follows the reference film. The fallback requires development plus local mode and an explicit preview marker; release media authorization was not weakened. This does not complete the Arabic films. |
| A07 · recursive preview | Replaced the ancestor directory link with narrow preparation-input links. Recursive caption scanning now completes: seven tracks, 168 cues, zero blocking findings; one existing 1.14-second cue warning. |
| A08 · locale parity | Both English and Arabic preview badges are present. 3,879 localized fields pass parity with zero issues. |
| A09 · stale review archive | Rebuilt the archive from current files, added current audit/repair evidence, overlap-fixed screenshots, legal drafts and regulatory gap records; refreshed SHA-256 and per-file manifest. Older navigation screenshots were removed from the archive. |

## Verification

- 18 focused tests pass; the authored tutor suite passes 64 assertions, including 17 Arabic course cases plus existing safety cases.
- Type checking, academy isolation, locale scan, production build and candidate schema pass. Existing bundle-size and future Vite configuration warnings remain non-blocking.
- All 110 declared local assets exist. All 48 Arabic narration checksums match; no audio was regenerated.
- Rechecked desktop and 458×934 phone account menus: opaque white surface, no local-mode banner bleeding through. Profile remains accessed from the name; the four learning destinations remain.
- Browser proofs cover homepage, legal pages, library, regional card, scoped tutor answer, menu and all seven reference films.
- Final release gate intentionally fails 11 of 28 checks. Besides genuine outstanding reviews, the Arabic assessment is now correctly draft instead of carrying its English approval status.
- The 21 citation gaps remain blocking. They are itemized in `course-production/hormones-peptides-skin/arabic-uae-20261007/REGULATORY-REVIEW-GAPS.json`, assigned to Fady@hormonaly.ai.

## Release boundary

Still required: product-specific Saudi evidence/disposition; Fady's Arabic medical/language review and source-lock amendment review; Arabic opening films with on-screen text and timed captions; legal review; media/native acceptance and applicable accreditation/publication decisions. English screenshot/reference imagery remains source material until target-language media QA. No paid generation, emails, terms acceptance, certificate issuance, cloud progress tests or deployment occurred in this repair pass. Model-backed tutor behavior was not re-tested; the corrected authored path was.

The local review package remains `in_review`, `mediaComplete:false`, `publishReady:false`. Runtime repair commit: `ddd70918f8f3036b09c9461209ac74db02e51e4a`.

Canonical English package unchanged: `6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa`.

Current evidence: [repair evidence](course-production/hormones-peptides-skin/arabic-uae-20261007/fixes-20261007). The earlier audit is retained as historical findings; this report records their current disposition.
