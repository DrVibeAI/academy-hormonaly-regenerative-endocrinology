# Hormonaly Brand Book v2 · published 16 October 2026

Owner authorization: “looks good, publish all the changes to the live site”.

## Release
- Production: https://hormonaly.perceptors.ai
- Final revision: `academy-hormonaly-00071-mhv`, 100% traffic.
- Runtime: `977de5eca5a21a64076854007c425c272d9d2ead`.
- Academy source: `50f033219ae6dd09e9d8da7b8acce3a7081632f8`.
- Branch in both repositories: `release/hormonaly-brand-v2-20261016`.
- Image: `sha256:7df9e402f478e8b521792ff4114d774082924774db21c36e2e9449f2f3c40fc4`.
- Previous baseline: `academy-hormonaly-00069-7bp`. Its sharing-image source commit is merged into this release history. New approved sharing assets use `/seo-v3-hormonaly/` to avoid stale caches.

## Published
Brand v2 identity and self-hosted typography; shared product UI; centered course containers and matching lesson/card navigation widths; compact bilingual homepage screenshots; English/Arabic social images and icons; email and certificate branding. The November 30 free offer, bookstore links and faculty credentials are preserved.

## Release evidence
- Standard `deploy/gcp.sh` flow: pushed clean sources → candidate with no traffic → health/auth checks → exact candidate promotion. No provenance override.
- Eight mandatory release suites passed for both builds, with application/server TypeScript checks. Latest report: `../evals/report-2026-10-16T180115Z.md`.
- Production health: app and database both `ok`; certificate endpoint returns 401 without authentication.
- Checkout config: active price $0, regular price $199, offer ends December 1, 2026 at 00:00 Pacific (free through November 30).
- English and Arabic sharing metadata references new PNG images; both images match local bytes. Twenty-three brand/font/home assets match local SHA-256 values; fonts have correct CORS headers.
- English and Arabic public home and signed-in course/lesson views inspected in the Codex in-app browser. New homepage images load in both languages; bookstore links appear in the home section and footer.
- Desktop lesson card and bottom navigation both x=244, width=792 at a 1280px viewport. Local Arabic mobile layout: both x=12, width=366 at 390px, document width=390.
- Live follow-up caught an inherited dark heading on photographic lesson covers. Runtime `977de5e` restores the inverse foreground; final production computed heading colour is white in English and Arabic. Final candidate stylesheet and live browser proof confirm the correction.
- Initial brand revision `00070-wk9` was followed by final contrast revision `00071-mhv`. Homepage screenshots were captured on 00070; lesson proofs and final HTTP/traffic evidence are from 00071. Homepage appearance and academy inputs are identical between these revisions.

## Scope
This publication check is not a repeat of every course activity. No final assessment was submitted, certificate issued, or email sent during publication. An existing signed-in learner session was used to inspect completed content. No authenticated admin walkthrough was performed in this release. The previously noted limitation on typography baked into existing videos remains.

Evidence: `../brand-v2-20261016/live/` (HTTP, revision, traffic, media digests, and live screenshots). The post-deployment documentation commit records the release and is not represented as its deployed source SHA.
