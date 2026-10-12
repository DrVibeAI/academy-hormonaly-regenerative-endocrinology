# Hormonaly certificate redesign — 11 October 2026

Status: PUBLISHED on October 11, 2026, revision `academy-hormonaly-00061-7lk` at 100% traffic. Latest design: `v5-october/`, Fady only. See publication evidence below.

## Design
Both institution logos, ivory paper, navy edge bands, fine gold double frame, a large faint Hormonaly orbit silhouette, centered award hierarchy, prominent learner name, and compact QR verification footer. Existing issuer/accreditation status stays authoritative. The GCLS mark retains the recorded GCLS AI Lab partner label and explanatory note.

## Implementation
- Runtime base `e3fb692`, containing the Hormonaly Arabic production baseline `2fa4d7d` and the boot-flash port.
- Academy base `a04a0f7`, the Arabic 1.2.0-ar-AE.1 release snapshot; both existing packages are unchanged.
- Academy opts into `brand.certificatePresentation.layout: institutional`; logo, partner logo and watermark are separate certificate assets so the academy UI wordmark remains unaffected.
- Runtime copies and validates declared certificate assets; missing required assets fail PDF generation rather than quietly producing an incomplete certificate.
- Other academies retain their existing layout. The stored name, course title, issuer, issue/expiry dates, evidence, code, and verification URL are preserved. Redundant certificate prefixes are removed only from the displayed course title.
- Signature blocks were added in revision 4; see the provenance and implementation notes below.

## Verification
- Production build, TypeScript, academy isolation, and locale scans pass.
- Six focused tests pass, including issuer/accreditation boundaries, mounted paths, second-brand fixtures, Arabic, expiry dates, and one-page output.
- All eight standard academy evaluation suites pass, including live RAG groundedness. The initial offline-key run failed RAG authentication; rerun with the existing configured key passed.
- English, Arabic, and long-name proofs are A4 landscape, one page each, visually inspected. Native Vision decoded the English QR as `https://verify.perceptors.ai`.
- Proofs use `SAMPLE-DESIGN`; their QR opens verification home and is not an issued credential. Production uses the actual stored certificate's verification URL.

## Assets
Hormonaly logo: existing approved authority asset from `academy-hormonaly-authority-20260930/public/assets/authority/hormonaly-logo.png`.
GCLS logo: existing runtime `public/gcls/gcls-logo.png`.
Orbit: rasterization of academy `public/assets/brand/hormonaly-mark-flat.svg` at 1400 px for PDFKit; no new or altered brand geometry.

## Review and release
Preview files are in this directory. Runtime source: `../runtime` relative to the academy root's parent. Branches: `feat/hormonaly-certificate-20261011` (runtime), `design/hormonaly-certificate-20261011` (academy).
Production publication awaits Omar's approval under `/Users/omar/DrVibe/AGENTS.md`. Use `deploy/gcp.sh` with these academy inputs, upload the new certificate assets, review a no-traffic candidate, verify `/api/certificate` returns 401 unauthenticated, and promote only the tested revision. Preserve the Arabic release lineage.

## Revision 2 — thicker dimensional frame

Owner requested a nicer thicker border and more 3D feel. The current implementation uses a broad navy frame with directional bevel highlights, a metallic gold inner band, subtle recessed-paper shadows and ivory shading. The PDF remains vector-based and printable. Current proofs are in `v2/`; the original proofs are retained for comparison. Build/typecheck and all six certificate tests pass; all three proofs remain one page, visually reviewed. No production deployment.

## Revision 3 — traditional border, dimensional certificate

Owner clarified that the border should be traditional and thicker, with depth in the certificate itself. Revision 2's beveled frame is superseded. The current version has flat navy/gold printed rules, engraved chain detail and ornamental corners, with softly shaded ivory paper, a shallow dimensional watermark and an embossed brand medallion. Current proofs: `v3/`. Build/typecheck and six certificate tests pass. No deployment.

## Revision 4 — signature blocks

Omar approved revision 3's direction and requested Fady for Hormonaly and Dominik for GCLS. No Fady signature was found; Omar explicitly replied, “Don’t think we do. You can create one for him.” His mark is therefore a new typeset signature-style name in Allura, not a supplied handwritten autograph or evidence of personal signing. This provenance is also in `academy.yaml`. Dominik uses the existing GCLS `dthor-signature.png` asset, copied unchanged. Roles: Fady Hannah-Shmouni, MD FRCPC — Founder & CEO, Hormonaly; Dr. Dominik Thor, MSc — President, Geneva College of Longevity Science.

The generic renderer supports configured signature images and designed name treatments, retains credential signature fallback, and fails on a missing declared signature image. Academy preparation copies and validates signature assets. The script font is Allura (Google Fonts), bundled with its SIL Open Font License. Signature presentation does not alter certificate issuer/accreditation records.

Production build/typecheck and eight focused certificate tests pass. English, Arabic, and long-name proofs are one-page A4 landscape and visually reviewed; QR still decodes to verification home for the sample. Current proofs are in `v4/`. Not deployed or issued.

## Release conditions — November 1, 2026

Omar specified that this certificate becomes available only after November 1 once the course is GCLS certified and paid. The local implementation gates status, claiming, PDF download, and direct issuance from `2026-11-01T00:00:00-07:00` (Los Angeles midnight). All conditions must pass: the configured release date, enabled GCLS issuance with course status `accredited` and a nonempty accreditation ID, and a positive current course price. An extended free promotion keeps the certificate blocked. The date never changes accreditation automatically; current package approval records remain unchanged. Normal module and assessment requirements still apply. Existing award records and public verification remain intact.

The academy homepage and FAQ now state the conditional November release in English and Arabic. The signed-in certificate card explains pending conditions. This is a course-level paid-launch gate. Whether October's free enrollees must individually pay before receiving a certificate remains an open owner decision; no individual payment requirement or upgrade flow has been added.

Validation: production build/typecheck passes; 13 focused certificate tests pass, including date boundary, missing accreditation, free/extended promotion, invalid configuration, and direct issuance blocked before database access. All eight standard academy suites pass: `../evals/report-2026-10-12T020251Z.md` (report records pre-commit HEAD; executed with the release-gate working tree). Latest visual proofs remain `v4/`. No deployment or credential issuance.

## Revision 5 — October completion certificate (current owner decision)

This supersedes the November-only release policy above. Omar requested that everyone taking the free October course can receive the improved Hormonaly certificate after the normal completion and assessment requirements. Keep the traditional thick border, dimensional ivory paper, orbit silhouette, medallion, Hormonaly logo, Fady signature treatment, learner details and verification QR. Remove the GCLS logo, Dominik signature, and associated GCLS partner text. Fady's single signature is centered. His typeset-mark provenance remains unchanged.

The active academy configuration has no certificate release-date or paid-course gate. `accreditation.gcls` is false for academy-only issuance, and `site.certificatePartner: null` explicitly suppresses the shared platform's inherited GCLS partner name/note. Course package governance, catalog records, checkout pricing and October promotion are untouched. No learner must pay specifically to receive this October completion certificate. Historical issued records remain intact.

Latest proofs: `v5-october/` (English, Arabic, long name). All three PDFs are one page, visually inspected, retain Fady, and contain no GCLS, Geneva College or Dominik text. The compiled October policy is open. Production build/typecheck and 13 certificate tests pass. No live deployment or credential issuance.

November: the approved two-signature design and original assets remain in `v4/` and prior Git history (`52cc977` academy, `7b8acc5` runtime). The GCLS additions can be restored from November 1, 2026 after confirmed certification and the paid-course launch. There is no automatic calendar switch in this October configuration; do not retrospectively rewrite old academy-issued records as GCLS credentials.

Final revision 5 academy evaluation: all eight suites PASS in `../evals/report-2026-10-12T031845Z.md`, executed with the revision 5 working tree.

## Published — October 11, 2026 (Los Angeles)

Omar explicitly approved: “Yes, publish the October version with Fady’s signature and no GCLS branding or Dominik signature.” Published at https://hormonaly.perceptors.ai, revision `academy-hormonaly-00061-7lk`, 100% traffic. Previous revision: `academy-hormonaly-00060-g8s`. Runtime `b94c04bde457`; academy input `9a32cea64125`; both pushed to `release/hormonaly-october-certificate-20261011`. Existing Arabic release lineage retained.

Image digest: `sha256:65f3a1f7b402b467eaf46a29aba7a76771e2120a883c54ccaa545a1ad4ae9c07`. Build `d316679c-9e22-431e-8099-90eb7b57f917`. Staged with `deploy/gcp.sh --candidate-only --skip-media`, then promoted the exact candidate with `--promote-revision=academy-hormonaly-00061-7lk`. Only the two required Hormonaly certificate images were uploaded; public bytes match the approved assets.

Verification: deploy preflight/typecheck and all eight eval suites pass (`../evals/report-2026-10-12T032344Z.md`). Exact deployed-image renderer proof, build `a5296742-73cb-43e8-887a-2e768a4a6b41`, passes for English, Arabic, and a legacy completion record with GCLS issuer kind but no accreditation ID: one page, Fady present, no GCLS/Dominik text, required images/font available. These were in-memory sample proofs, with no learner records or certificates created. Both candidate and live health checks report app/db OK; certificate status and PDF endpoints return 401 without authentication. Candidate and live browser checks confirm English/Arabic October-included completion wording. Evidence is in `deployment/`.

The October certificate is now live and included for free enrollees after normal completion and pass requirements. GCLS logo and Dominik signature remain reserved for a later November certified release; no automatic November switch was enabled.
