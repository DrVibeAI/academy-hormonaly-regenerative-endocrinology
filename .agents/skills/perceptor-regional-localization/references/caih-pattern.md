# Reusing the CAIH pattern

Inspected on October 7, 2026:
- `/Users/omar/DrVibe/GCLS-Certification-Course-drvibe-main/artifacts/api-server/src/geo-adaptive-packs.ts`: primary/secondary country packs and topic-focused regulatory, workflow and validation context.
- Same repository, `artifacts/api-server/src/ai.ts`, `runGeoAdaptiveAgent`: grounded regional brief; primary jurisdiction first, labelled cross-border notes, source IDs and structured actions.
- GCLS operating memory records that language and jurisdiction are independent and that named native/clinical/regulatory review differs from owner/media publication approval.

Adapt those principles, not the medical-AI content or the entire application. Peptide courses need exact products, routes and indications, unlike CAIH's AI/privacy/device examples. The inspected CAIH agent falls back to a US/HIPAA baseline when no local pack exists; **do not copy that behavior** for medication legality. Use an explicit evidence gap instead.

Perceptor already has academy-owned country profiles, block `metadata.variants.jurisdiction`, a build-time regulatory retrieval index, and a source-constrained guide. Extend these layers; do not hardcode a tenant into the shared runtime. Preserve localized factual text and answer keys in the package. Countries select notes; languages select text. A reused source citation is not proof that every local product has been checked.
