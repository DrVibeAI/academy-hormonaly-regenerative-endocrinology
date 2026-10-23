# Localization draft QA

Source package: `hormonaly.hormones-peptides-skin` 1.1.0. Automated checks do not constitute clinical or language review.

| Edition | Text fields | Missing | Identical long fields | Number token flags | Hormonaly mentions in learning text | Target films/captions |
|---|---:|---:|---:|---:|---:|---:|
| cenegenics · es-MX | 3796 | 0 | 0 | 26 | 0 | 0/0 |
| biolongeva · pt-BR | 3796 | 0 | 0 | 29 | 0 | 0/0 |
| parallaxnet-skin · id | 3796 | 0 | 0 | 22 | 0 | 0/0 |

All candidate modules, units and assets remain drafts; no source-course approvals transfer. Locale text completeness alone cannot make an edition publishable.

A second machine pass classified all 77 number-token differences as formatting or spelled-out-number differences (es-MX: 26, pt-BR: 29, id: 22). This is an agent pre-review, not an independent clinical check. Review exact flagged fields in `QUALITY-FLAGS.json` and `NUMERIC-REVIEW.*.json`.

The source carries 289 learner/assessment/tutor fields for local-context review and 30 jurisdiction-specific regulatory moments. The review CSVs align every source and target text field; the film-script documents extract all seven opener transcript drafts.

Some source-package metadata remains English because it is a source locator, image-generation brief, or internal tutor context rather than a locale-keyed learner field. The importer should be checked for any of this metadata that reaches learners or tutor prompts before release.

## Open release gates

- Exact country product/route/indication claims and profession-scope review
- Native clinical language review of lessons, assessments, tutor answers and certificate copy
- Brand-neutral derivative copy and distribution rights
- Localized narration, films, captions, transcripts and trailer; human media preview
- Runtime locale/readiness enforcement, authenticated mobile checks and separate accreditation/publish decisions

See `QUALITY-FLAGS.json` for exact pointers and `review/` for side-by-side editorial sheets.
