# Hormonaly Academy — design contract

> Stage 05 artifact (contract: perceptor-foundry `docs/design-contract.md`).
> **Tier: 0 · House.** Every customer-visible surface (app, review room, emails, certificates, videos) renders the
> Perceptors house theme verbatim. Status: **approved**. See the approval block.

## Identity in one sentence

Evidence-graded clinical education in hormone and peptide medicine, course by course, for every clinician who meets these questions, in the Perceptors
premium-editorial register: calm, exact, and no marketing noise.

## Inherited from the house

Everything visual comes from perceptor-foundry `docs/brand.md` (Perceptors AI brand kit, 2026-08-24) and
`templates/house-theme.yaml`. Nothing is copied here. When the house kit improves, this academy improves on its next build.

- **Palette, type, shape, spacing, components, imagery rules and the kill-list** are the house values.
- **academy.yaml** sets `theme: perceptors-house`, `designTier: 0` and the house violet accent only. It sets no palette and no fonts.

## Logo and wordmark

- The customer has not supplied a logo asset yet.
- Until one ships in `public/`, the runtime sets a typographic wordmark: "Hormonaly" in the house display serif, with the
  suffix "ACADEMY" in house mono (`brand.wordmarkSuffix`).
- A supplied logo appears on paper with clear space equal to its cap height. It never brings its own typography.
  If the customer wants its own palette or type, that is a tier-2 amendment chosen at intake.

## Voice and likeness

- Narration and the tutor voice use a stock library voice (ElevenLabs "Alice"), declared in `academy.yaml`.
- No faculty likeness or cloned voice is used without a filed release.

## Approval

| Gate | Owner | Decision | Date |
|---|---|---|---|
| brand_approval | Omar Saleem (Perceptors) | Align the academy with perceptors.ai; drop the inherited Cenegenics look | 2026-09-24 |

## Hormonaly identity update · 2026-09-30

Owner direction: retain Perceptor's existing design language; use the Hormonaly logo and adopt design-guide details only where they improve the experience. Reference: https://claude.ai/artifact/WTWPHoaUnFU1Dyx3MbQLmv.

Use the supplied clinical-blue app icon unchanged in the tutor header, answer avatars, pending answer state, academy wordmark and favicon. Keep the house paper, violet actions, Fraunces/DM Sans type, spacing and lesson interactions. The icon sits beside the house wordmark, rather than recreating Hormonaly's outlined logo typography. No palette overhaul or unsupported evidence-grade claims. Certificate branding is outside this update.

## Hormonaly palette amendment · 2026-09-30

Omar's latest direction: improve the logo treatment and adopt Hormonaly design-book colors throughout; keep the current typography and layout. This supersedes the earlier instruction to retain the violet/paper palette.

- Clinical blue `#0071E3` for primary actions and the tutor header; soft blue `#EBF4FF` for selection and answer surfaces. A deeper `#0064CA` is used for small links on gray.
- Gray page `#F5F5F7`, white raised surfaces, ink `#1D1D1F`, hairlines `#E8E8EB`, muted `#6E6E73`, charcoal `#1E232B`. Functional success/error colors retain their meaning; no decorative purple gradients.
- The academy name keeps its existing house display/mono typography. Its standalone orbit uses the exact supplied app-icon vector geometry, in guide-approved clinical blue, without the square tile. The official app icon remains unchanged for answer avatars and favicon. Its tutor-header wrapper is transparent, removing the awkward pale corners. No lockup typography is recreated.
- Fraunces, DM Sans, DM Mono, type scale, weights, radii, spacing, imagery and course interactions are unchanged. Brand palette overrides are declared in academy.yaml; shared neutral tokens retain Perceptor fallbacks.
- Scope is the public homepage and learner interface. Existing certificate work is preserved; no deployment is implied.

## Guide answer formatting · 2026-09-30

Owner asked for scannable tutor answers and useful illustrations. Keep the house fonts and Hormonaly colors. Use a clear takeaway, short section labels, bullets and expandable source titles; preserve complete clinical limits. Course teaching illustrations are explicitly mapped by tutor entry ID in `metadata.tutorVisuals`, resolved by the shared importer, and captioned with their module/title. Live answers may reuse only imagery associated with exact cited course blocks or corpus entries. No model-authored image URLs or generated medical diagrams in this version. Local QA: `course-production/tutor-formatting-20260930/QA-REPORT.md`.
