# Hormonaly certificate redesign — 11 October 2026

Status: implemented and tested locally; design preview only. No deployment and no credential issuance.

## Design
Both institution logos, ivory paper, navy edge bands, fine gold double frame, a large faint Hormonaly orbit silhouette, centered award hierarchy, prominent learner name, and compact QR verification footer. Existing issuer/accreditation status stays authoritative. The GCLS mark retains the recorded GCLS AI Lab partner label and explanatory note.

## Implementation
- Runtime base `e3fb692`, containing the Hormonaly Arabic production baseline `2fa4d7d` and the boot-flash port.
- Academy base `a04a0f7`, the Arabic 1.2.0-ar-AE.1 release snapshot; both existing packages are unchanged.
- Academy opts into `brand.certificatePresentation.layout: institutional`; logo, partner logo and watermark are separate certificate assets so the academy UI wordmark remains unaffected.
- Runtime copies and validates declared certificate assets; missing required assets fail PDF generation rather than quietly producing an incomplete certificate.
- Other academies retain their existing layout. The stored name, course title, issuer, issue/expiry dates, evidence, code, and verification URL are preserved. Redundant certificate prefixes are removed only from the displayed course title.
- Hormonaly has no recorded signatories; none have been invented. This layout is designed for the current unsigned completion credential; future signed credentials need a signature layout extension.

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
