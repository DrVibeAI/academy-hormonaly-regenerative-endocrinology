# Live release · academy-hormonaly-00072-8vk

Published 16 October 2026 to https://hormonaly.perceptors.ai with 100% traffic after candidate review.

## Source

- Runtime: `d81a55ba4fc2` — landing certificate preview, configurable bookshelf, footer layout, configured certificate partner logo and signatory institutions.
- Academy: `27fc8ff48c4d` — Omar/Fady LinkedIn profiles, authentic book covers, English/Arabic certificate specimens, localized links.
- Branch: `release/hormonaly-brand-v2-20261016` in both repositories.
- Image: `sha256:12ce11a224d5a18b75be320ec71f64d82b76d2f9e5bdf44c79d8b4b4a1ed5f4f`.
- Previous live revision: `academy-hormonaly-00071-mhv`.
- Build: `df39289e-2935-45ac-80c7-11d16931b80d`.

## Release proof

The standard `ACADEMY_DIR=../academy bash deploy/gcp.sh --candidate-only` workflow passed all eight eval suites, release lineage, offline frozen install, and prepared frontend/server TypeScript checks. The candidate was reviewed, then promoted through `--promote-revision=academy-hormonaly-00072-8vk`.

Production serves `/assets/index-BLj_OG_B.js`, matching the local production build. Health returns `{ "app": "ok", "db": "ok" }`; unauthenticated `/api/certificate` returns 401. GCP reports this exact revision at 100% traffic.

All nine new images/PDFs return HTTP 200 with the expected content type and identical SHA-256 hashes to local assets. Browser checks on the live domain confirm all three faculty LinkedIn links, English/Arabic certificate PDF URLs, three English book covers and two Arabic covers, and the footer's legal/support/store links. English desktop and Arabic mobile screenshots are saved in `../landing-polish-20261016/live/`. Mobile document and viewport width both measure 390 px, with no horizontal overflow.

No course content, accreditation decision, assessment record, or credential issuance was changed. Certificate preview data is an in-memory specimen marked `SAMPLE-PREVIEW`. GCLS remains the existing education partner, and the current no-CME/CE disclaimer is preserved. The existing November 30 free-enrollment offer remains displayed.

Required deployment eval report: `../evals/report-2026-10-16T182434Z.md`.
