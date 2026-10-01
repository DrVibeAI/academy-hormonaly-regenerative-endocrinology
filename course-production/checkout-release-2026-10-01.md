# Skin course October checkout release

Live: https://hormonaly.perceptors.ai/ · revision `academy-hormonaly-00034-s7h` at 100% traffic (top-banner follow-up to the verified checkout release `academy-hormonaly-00033-7d9`).

The course is $0 for new Stripe Checkout sessions created from October 1, 2026 at 00:00 through November 1, 2026 at 00:00, America/Los_Angeles. The normal one-time price remains $199 USD and resumes automatically for new sessions on November 1. No promotion code or card is required for the free offer. The full course and included completion certificate retain their existing completion requirements. Enrolled learners retain course access after the promotion expires. A session created during October keeps its offer for Stripe's normal session lifetime.

Promotion configuration: `catalog[0].entitlement.promotion` in `academy.yaml`. The runtime selects the price at checkout creation; browser-supplied amounts cannot override it. A stale browser must review the updated price before checkout opens. Fulfillment uses the existing signed Stripe webhook, accepting a completed zero-total session with `no_payment_required`.

## Verification

- Build and type checks passed; all six deployment evaluation suites passed, including 13 checkout tests.
- Tests cover Los Angeles start/end boundaries, invalid promotions, stale or manipulated prices, and enrollment after the offer expires.
- Actual live Stripe $0 checkout completed for QA alias `omars1123+skin-oct-qa-1790864615@gmail.com`. No card was entered and no charge occurred.
- Before checkout, that learner's course state endpoint returned 403. After Stripe completion, it returned 200 **before** calling the return-confirmation endpoint, proving webhook fulfillment. Learner progress remained empty; no certificate was issued.
- The same restricted Stripe key successfully created an unpaid $199 USD session (`amount_total: 19900`). It was immediately expired. A $199 charge was not performed.
- Public `/api/checkout/config` reports enabled, effective price $0, regular price $199, and the configured October boundaries. Unauthenticated `/api/certificate` returns 401.
- The public course page shows the struck-through $199, $0 October offer, certificate included, and no card/code required. Screenshots are in `outputs/skin-october-promotion-2026-10-01/` under DrVibe.
- Course package remains version 1.1.0, SHA-256 `cb7b66528438d0081b05cc3d08e4b5f2625f3eac94898beb13ebafd5dd936334`.

## Source for subsequent deployments

This release was built on the exact serving SEO release, preserving homepage images and public metadata. Runtime source: `/Users/omar/DrVibe/releases/hormonaly-october-promo-20261001/perceptor-runtime`, commit `4621c2f` on `codex/hormonaly-october-promo-20261001` (base `42cc868`). Academy source: `codex/hormonaly-october-promo-20261001`, promotion commit `402bfa9`, banner commit `d2a288a`. Deploy only through `deploy/gcp.sh` with `ACADEMY_DIR`.

Future runtime releases must include `af09c83` or the equivalent promotion support; older runtime checkouts ignore the promotion config. The working runtime checkout with pending unrelated authority changes was preserved.

## Top-banner follow-up

User requested a top-of-page limited-time offer on October 1. The active promotion now supplies “Free for October,” “Limited-time offer · Ends October 31,” and an “Enroll free” button above the navigation. The header remains visible while scrolling; the main enrollment buttons also say “Enroll free” while the offer is active. The banner automatically disappears at the existing November 1 boundary.

Build/type checks and all six deployment evaluation suites passed again (`report-2026-10-01T144208Z.md`). The preview was reviewed at desktop and 390 × 844 phone size; there was no horizontal overflow, and the banner button opened the sign-in/enrollment flow. The exact preview revision was promoted. Public rendering and certificate authentication were verified after promotion. Screenshot: `outputs/skin-october-promotion-2026-10-01/live-top-october-banner.jpg`; phone proof: `banner-preview-mobile.jpg`. Future releases should preserve runtime commit `4621c2f` and the promotion banner fields.
