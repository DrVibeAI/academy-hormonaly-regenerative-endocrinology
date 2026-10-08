# Evals — academy-inputs — 2026-10-08T173855Z

Result: **PASS** · runner tools/evals/run.sh · cdf489f Recover unchanged editing workspaces after course up

## Locale parity — PASS

```
✓ parity eval [en, ar]: 3879 localized fields checked · 0 issue(s)
```

## Guía consistency & clinical safety — PASS

```
✓ tutor evals: 64 pass · 0 fail (29 cases)
```

## Regional emergency routing and clinical terms — PASS

```
✔ emergency and crisis contacts follow the selected country, not the language (0.758834ms)
✔ an unknown country gets a local-services instruction without an invented number (0.125583ms)
✔ the Indonesian word reseptor does not trigger the prescription boundary (1.37475ms)
ℹ tests 3
ℹ suites 0
ℹ pass 3
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 218.333292
```

## Review deployment and reference media — PASS

```
✔ reference films require an explicit marker and prefer a supplied target edition (0.310708ms)
✔ review candidates protect live learner records and credentials while retaining authentication (0.467083ms)
ℹ tests 2
ℹ suites 0
ℹ pass 2
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 95.878083
```

## RAG groundedness (grounded coach) — PASS

```
rag index loaded: 1546 chunks (62890a46aab59d01)
✓ rag groundedness [en]: 4 pass · 0 fail
```

## Paid enrolment boundaries — PASS

```
✔ October pricing follows Los Angeles midnight boundaries and invalid offers keep the regular price (0.50025ms)
✔ no-cost sessions carry enrollment metadata without requesting a PaymentIntent (0.301542ms)
✔ stripe signature: valid, tampered, stale, missing (0.353959ms)
✔ the session form charges the course price in cents, locks the email and carries the course (0.080209ms)
✔ on a shared Stripe account: the session and the payment say platform perceptors; promotion codes stay off (0.071542ms)
✔ checkout: a signed-in learner gets a Stripe session; anonymous is refused; an enrolled learner is not charged again (24.949084ms)
✔ password sign-in without email verification gives an actionable error and never creates checkout; a refreshed verified identity can continue (7.129042ms)
✔ checkout without keys answers 503; a free academy has no checkout (2.746125ms)
✔ return from Stripe: the paid session enrols its own email only (4.107083ms)
✔ webhook: signed and paid enrols; unsigned, unpaid or another course does not (3.780167ms)
✔ a complete session with nothing to pay enrols; an open no-charge session does not (1.897292ms)
✔ secrets pasted with a trailing newline still work (Authorization header and webhook signature) (2.848583ms)
✔ the server creates a zero session during October and refuses stale or manipulated browser prices after expiry (3.961416ms)
✔ an October enrollment can be fulfilled after expiry; open, nonzero, and other-course no-cost sessions are refused (3.55525ms)
ℹ tests 14
ℹ suites 0
ℹ pass 14
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 181.172625
```

## Verification email identity and delivery boundaries — PASS

```
✔ verification mail binds recipient and return URL to trusted identity/configuration; duplicate sends are throttled (83.308041ms)
✔ anonymous requests, caller-chosen recipients/URLs and unsupported methods cannot send verification emails (6.06125ms)
✔ disabled and changed-email accounts cannot send; already verified accounts need no email (3.590666ms)
verification email request failed resend-delivery provider-error unspecified unspecified
✔ provider failure is explicit and retryable; missing secret prevents delivery (15.371292ms)
✔ email template escapes untrusted text, includes plain text and uses email-safe layout (3.957583ms)
✔ branded emails preserve logo scale, colors, and legal links beneath a mounted academy (4.193ms)
ℹ tests 6
ℹ suites 0
ℹ pass 6
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 478.555292
```

## Today line (rotation, moments) — PASS

```
✔ one line per local day, the same all day, walking forward with "Another" (1.339167ms)
✔ a line opens the pane its moment sits on, or nothing when the moment is not in this build (0.381375ms)
✔ a line opens only where the learner has been; further on in the module reads "later", beyond it "ahead" (0.073208ms)
ℹ tests 3
ℹ suites 0
ℹ pass 3
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 103.199666
```

