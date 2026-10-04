# Skin optional practice — medical review packet

Status: confirmed by human report. On October 2, 2026, Omar replied “confirmed” when asked whether Fady had confirmed this exact bank. Reviewer of record: Fady Hannah-Shmouni, as reported by Omar. A separate signed/verbatim Fady record and original review date were not supplied; the timestamp below records receipt of Omar’s confirmation.

Bank: `skin-en`. SHA-256: `12121e756cca16c4e6afbc35f4eb9ef5186fb3ef2186a1df3f2819c1f6048153`.

The approved 1.1.0 course package is unchanged. Automated compatibility audit: 64/64 golden cases, zero failures/warnings, 52 new framing lines. Matching an existing sentence is a provenance check; it is not approval of its new use in a case.

Review the new wording below and the sourced teaching items in the companion bank. Record reviewer, date and dispositions for the exact bytes before confirmation. Production requires every library item confirmed, not just a bank-level flag. Fields were proposed during implementation; they are now confirmed from the subsequent human response.

## New wording — 52 lines

- [x] 1. `mirror-generalization` · `statement`: Claim to test: {{product}} as the first step for {{population}}.
- [x] 2. `mirror-question` · `statement`: Question about {{product}}.
- [x] 3. `mirror-compare` · `statement`: Question: are {{product}} and {{product2}} the same idea?
- [x] 4. `mirror-scope` · `statement`: Question about advice outside prescribing.
- [x] 5. `mirror-explain` · `statement`: Asked to explain this in one sentence.
- [x] 6. `mirror-post-needling` · `statement`: The course does not cover microneedling.
- [x] 7. `mirror-post-laser` · `statement`: Question: topical copper peptide after laser resurfacing.
- [x] 8. `case-default-ghk` · `title`: A patient asks about copper peptides
- [x] 9. `case-default-ghk` · `lead`: She has seen a GHK-Cu serum online and asks whether to start it.
- [x] 10. `case-default-ghk` · `facts[0]`: Your habit: {{product}} first, for {{population}}
- [x] 11. `case-default-ghk` · `facts[1]`: She asks: Should I start the serum?
- [x] 12. `case-default-ghk` · `facts[2]`: Route: Topical serum
- [x] 13. `case-default-ghk` · `facts[3]`: Your move: What do you tell her?
- [x] 14. `dec-default-ghk` · `prompt`: What do you tell her?
- [x] 15. `dec-default-ghk` · `options[0].label`: GHK-Cu serum is the standard first step.
- [x] 16. `dec-default-ghk` · `options[1].label`: It is a reasonable cosmetic conversation at GRADE C, and I name the route.
- [x] 17. `dec-default-ghk` · `options[2].label`: Offer the injection instead. It is the stronger form.
- [x] 18. `cmp-ghk-route` · `title`: Same molecule, two routes
- [x] 19. `qc-route-01` · `question`: Which route of GHK-Cu has an indexed randomized trial in human skin?
- [x] 20. `qc-route-01` · `options[0].text`: Topical GHK-Cu
- [x] 21. `qc-route-01` · `options[1].text`: Injected GHK-Cu
- [x] 22. `qc-route-01` · `options[2].text`: Both, since it is the same molecule
- [x] 23. `cmp-three` · `title`: Compare by what stands behind each
- [x] 24. `qc-compare-01` · `question`: Which one has no randomized efficacy trial in people published in full?
- [x] 25. `qc-compare-01` · `options[0].text`: BPC-157
- [x] 26. `qc-compare-01` · `options[1].text`: Topical GHK-Cu
- [x] 27. `qc-compare-01` · `options[2].text`: Matrixyl (pal-KTTKS)
- [x] 28. `prot-bpc157` · `title`: BPC-157
- [x] 29. `qc-bpc-01` · `question`: What do the missing trials show about BPC-157?
- [x] 30. `qc-bpc-01` · `options[0].text`: In people, it is an unknown, not a negative.
- [x] 31. `qc-bpc-01` · `options[1].text`: It does not work.
- [x] 32. `qc-bpc-01` · `options[2].text`: The rodent results are enough to go on.
- [x] 33. `tb-scope` · `prompt`: Say it to them in one sentence.
- [x] 34. `tb-scope` · `rubric.levels[0].description`: Gives advice, or says nothing about who decides.
- [x] 35. `tb-scope` · `rubric.levels[1].description`: Names the limit or the referral, not both.
- [x] 36. `tb-scope` · `rubric.levels[2].description`: Gives no advice on amounts, technique or sourcing, and routes injected products to a prescriber.
- [x] 37. `tb-bpc-explain` · `prompt`: Explain this to a nurse in one sentence.
- [x] 38. `tb-bpc-explain` · `rubric.levels[0].description`: Says it works or it does not.
- [x] 39. `tb-bpc-explain` · `rubric.levels[1].description`: Names what the evidence is, not what it means.
- [x] 40. `tb-bpc-explain` · `rubric.levels[2].description`: Names the evidence and says it is an unknown, not a negative.
- [x] 41. `prot-ghk-topical` · `title`: Topical GHK-Cu
- [x] 42. `dec-post-01` · `prompt`: What do you tell her?
- [x] 43. `dec-post-01` · `options[0].label`: It is proven to speed healing after procedures.
- [x] 44. `dec-post-01` · `options[1].label`: One small trial, after laser resurfacing. The rest is small or sponsor-run.
- [x] 45. `dec-post-01` · `options[2].label`: Inject it instead, for faster healing.
- [x] 46. `fb-gap-melasma` · `title`: Not covered in this course
- [x] 47. `fb-gap-melasma` · `text`: This course does not cover melasma or pigment changes on hormone creams. Its lesson on hormone creams is in Module 2.
- [x] 48. `fb-gap` · `title`: No match in this lesson
- [x] 49. `fb-gap` · `text`: I could not match that to what this lesson teaches, so I will not guess. Try a suggestion, or ask the Guide.
- [x] 50. `fb-blocked` · `title`: I did not read that
- [x] 51. `fb-blocked` · `text`: It looks like it holds a name, a date or an instruction, so I left it alone. Ask about the lesson without patient details.
- [x] 52. `fb-handoff` · `text`: The Guide can look across the whole course. It receives your question and this card.

## Sourced library items

- [x] `mirror-generalization` — "authored:2026-09-29 from chrome"
- [x] `mirror-question` — "authored:2026-09-29 from chrome"
- [x] `mirror-compare` — "authored:2026-09-29 from chrome"
- [x] `mirror-scope` — "authored:2026-09-29 from chrome"
- [x] `mirror-explain` — "authored:2026-09-29 from chrome"
- [x] `mirror-post-needling` — "authored:2026-09-29 from chrome"
- [x] `mirror-post-laser` — "authored:2026-09-29 from chrome"
- [x] `case-default-ghk` — "authored:2026-09-29 from framing only"
- [x] `dec-default-ghk` — "authored:2026-09-29 from m4-p04, m4-p06"
- [x] `flag-injectable` — "authored:2026-09-29 from m4-p06"
- [x] `cmp-ghk-route` — "authored:2026-09-29 from m4-p04, m4-p05, m4-p06, m4-p07, m4-x04"
- [x] `qc-route-01` — "authored:2026-09-29 from m4-p04, m4-p06, m4-p07"
- [x] `cmp-three` — "authored:2026-09-29 from m4-p04, m4-p05, m4-p09, m4-p11, m4-p13, m4-p16, m4-x04"
- [x] `qc-compare-01` — "authored:2026-09-29 from m4-p04, m4-p09, m4-p14"
- [x] `prot-bpc157` — "authored:2026-09-29 from m4-p14, m4-p16, m4-x04"
- [x] `qc-bpc-01` — "authored:2026-09-29 from m4-p14, m4-x03"
- [x] `flag-scope` — "authored:2026-09-29 from m4-x03, m7-p13"
- [x] `flag-dose` — "authored:2026-09-29 from m4-x03"
- [x] `tb-scope` — "authored:2026-09-29 from m4-x03"
- [x] `tb-bpc-explain` — "authored:2026-09-29 from m4-x03"
- [x] `prot-ghk-topical` — "authored:2026-09-29 from m4-p04, m4-p05, m4-p16"
- [x] `dec-post-01` — "authored:2026-09-29 from m4-p04, m4-p06"
- [x] `fb-gap-melasma` — "authored:2026-09-29 from coverage map"
- [x] `fb-gap` — "authored:2026-09-29 from chrome"
- [x] `fb-blocked` — "authored:2026-09-29 from chrome"
- [x] `fb-handoff` — "authored:2026-09-29 from chrome"

## Decision record

Confirmation source: Omar Saleem’s user message “confirmed”, responding to the named-bank question on October 2, 2026. Received at 2026-10-02T22:20:57Z. Disposition: bank confirmed as a whole, including the listed wording and sourced library items. No clinical text or answer key revisions made. Pre-confirmation reviewed digest: 12121e756cca16c4e6afbc35f4eb9ef5186fb3ef2186a1df3f2819c1f6048153. Confirmed metadata bank digest: 38e62e0c8a4499bc52b66eca0cc2e84e7e79cc50d9960146a9ed1ea7a6107364.

No revision can mark approval from the audit, a model response, or the implementation request alone.


## Deployment authorization

Omar explicitly requested “deploy and lets get them done” and then supplied the confirmation above. Enable this bank on the verified Skin candidate. This confirmation is limited to this bank; it does not confirm adaptations for other courses or languages.
