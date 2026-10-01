# Skin course October checkout release

Live: https://hormonaly.perceptors.ai/ · revision `academy-hormonaly-00039-g8r` at 100% traffic (Fady admin access following Hormonaly-branded Resend verification email in `academy-hormonaly-00038-w2t`, password-email fix in `academy-hormonaly-00035-kbm`, top banner in `academy-hormonaly-00034-s7h`, and checkout release `academy-hormonaly-00033-7d9`).

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

This release was built on the exact serving SEO release, preserving homepage images and public metadata. Runtime source: `/Users/omar/DrVibe/releases/hormonaly-october-promo-20261001/perceptor-runtime`, deployed runtime commit `ebde079` on `codex/hormonaly-october-promo-20261001` (base `42cc868`; same application code as `bddd6ae`, plus permission documentation). Academy source: `codex/hormonaly-october-promo-20261001`, promotion commit `402bfa9`, banner commit `d2a288a`. Deploy only through `deploy/gcp.sh` with `ACADEMY_DIR`.

Future runtime releases must include `af09c83` or the equivalent promotion support; older runtime checkouts ignore the promotion config. The working runtime checkout with pending unrelated authority changes was preserved.

## Top-banner follow-up

User requested a top-of-page limited-time offer on October 1. The active promotion now supplies “Free for October,” “Limited-time offer · Ends October 31,” and an “Enroll free” button above the navigation. The header remains visible while scrolling; the main enrollment buttons also say “Enroll free” while the offer is active. The banner automatically disappears at the existing November 1 boundary.

Build/type checks and all six deployment evaluation suites passed again (`report-2026-10-01T144208Z.md`). The preview was reviewed at desktop and 390 × 844 phone size; there was no horizontal overflow, and the banner button opened the sign-in/enrollment flow. The exact preview revision was promoted. Public rendering and certificate authentication were verified after promotion. Screenshot: `outputs/skin-october-promotion-2026-10-01/live-top-october-banner.jpg`; phone proof: `banner-preview-mobile.jpg`. Future releases should preserve runtime commit `4621c2f` and the promotion banner fields.

## Password-email verification fix

The reported payment-opening error was a checkout authentication rejection: the password account had not verified its email. The original email-link QA did not cover this case. A read-only account check confirmed the cause; the real learner's account and enrollment were not changed.

Runtime commit `77a9f59` preserves verified-email checkout and adds an explicit `email-not-verified` 403 response. The paywall now explains the requirement, offers learner-triggered verification email and “I verified my email” controls, and refreshes the session before allowing enrollment. No verification email is sent automatically. Invalid or expired sign-in remains rejected.

Build/type checks and all six deployment evaluation suites passed (`report-2026-10-01T150907Z.md`), including all 14 checkout tests and the new unverified-password regression. A dedicated password QA account reproduced the 403 before verification. The browser showed the verification controls and kept enrollment blocked when verification was still pending. After consuming an operator-generated verification link for that QA account only (no email sent), the same browser session refreshed successfully, opened the real live Stripe $0 checkout without card fields, completed enrollment, and reached the course homepage with Module 1 available. No charge or certificate was issued.

The exact tested revision `academy-hormonaly-00035-kbm` was promoted through `deploy/gcp.sh`. Public health reports app/database OK, public pricing is $0 with a regular $199 price, and unauthenticated certificate access remains 401. Authenticated course access returned 200 on the public domain, and password sign-in opened the course there. A transient final-browser sign-in network error cleared after page refresh. Proof is in `/Users/omar/DrVibe/outputs/skin-checkout-verification-fix-2026-10-01/`: `verification-step.jpg`, `verified-password-zero-checkout.jpg`, and `live-password-course-access.jpg`.


## Hormonaly Resend verification email

User requested Hormonaly’s Resend account and existing Hormonaly email style. The verified `hormonaly.ai` domain and existing `resend-api-key` secret are configured for verification mail from `Hormonaly Academy <info@hormonaly.ai>`, with replies to `info@hormonaly.ai`. The React Email template follows the existing Hormonaly newsletter: logo, white 600px card, Helvetica and blue verification button. It includes plain text, a course return link and learner instructions. No marketing broadcast or recipient list was changed.

Runtime commits `6cfcdf5`, `b1189d0` and `bddd6ae` provide the template, authenticated mail endpoint, learner-triggered send and safe diagnostics. The endpoint reads the current tenant account, rejects disabled/changed-email users and caller-chosen recipients/return URLs, avoids mail to already verified accounts, and throttles repeat requests. Secrets, verification codes and links stay out of source and logs. Native password-reset and email-link sign-in mail retain their existing sender.

The dedicated runtime identity is `academy-hormonaly@perceptors.iam.gserviceaccount.com`, with runtime Cloud SQL/logging permissions, the seven mounted secret entries and academy media bucket read access. The custom project role `academyVerificationEmail` contains only `firebaseauth.users.sendEmail`; the custom role `academyTenantEmailAction` contains only `identitytoolkit.tenants.update` and is granted only on `hormonaly-academy-srbsc`. Identity Platform’s `GetOobCode` audit log identified the tenant permission requirement. Read/quota roles are Firebase Auth Viewer, Identity Platform Viewer and Service Usage Consumer. No Firebase Authentication Admin or user create/update/delete grant was added. The shared Compute identity has no new mail permission.

Build/type checks and all seven deployment eval suites passed (`report-2026-10-01T162735Z.md`), including 14 checkout tests and 5 verification-mail tests. A dedicated unverified password QA account received the actual Resend message, ID `01a0f854-72e2-71b3-ad64-8be36f592f4a`; Resend reported **delivered**. Sender and subject matched the intended Hormonaly envelope. Consuming that delivered message’s verification code verified only the QA account. In the same browser, “I verified my email” released the Enrol · $0 button, and enrollment opened real live Stripe Checkout at $0.00 with no card fields. This follow-up did not complete the order, issue a charge or grant course access. No email was sent to the real learner and their verification flag was not changed.

The exact tested revision `academy-hormonaly-00038-w2t` was promoted through `deploy/gcp.sh`. Public health reports app/database OK; pricing remains $0 during October with $199 regular price; anonymous certificate and verification-mail requests return 401. The verified QA account’s public mail request returns `{verified:true}` without sending another message, and course access remains 403 until enrollment. Desktop and 390 × 844 mobile email previews were reviewed with no horizontal overflow. Proof is in `/Users/omar/DrVibe/outputs/hormonaly-verification-email-2026-10-01/`: `verification-email-desktop.jpg`, `verification-email-mobile.jpg`, `verified-return-to-enrollment.jpg` and `verified-resend-zero-checkout.jpg`.


## Fady admin access

On October 1, Omar explicitly requested admin access for `fady@hormonaly.ai`. Academy commit `d7f61f8` adds that exact email to the existing Hormonaly `admins` list, preserving both Omar addresses. This grants the existing academy admin console and course access through the standard allowlist. A read-only tenant lookup confirmed Fady already has an enabled academy account; no credentials, account verification flag or payment record was changed, and no email was sent.

The prepared config matched exactly the three authorized admin emails. All seven deployment eval suites and type checks passed (`report-2026-10-01T171415Z.md`). Candidate `academy-hormonaly-00039-g8r` served the new admin list and passed app/database health and anonymous admin/certificate authentication checks. It was promoted through `deploy/gcp.sh` to 100% traffic. Public `/admin` serves the new configuration, anonymous `/api/admin/overview` and `/api/certificate` remain 401, and the October $0 / regular $199 pricing remains correct. Fady’s sign-in was not impersonated; he can use his own account at https://hormonaly.perceptors.ai/admin.
