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
