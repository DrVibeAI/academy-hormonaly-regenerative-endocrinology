# Evals — academy-inputs — 2026-10-08T042715Z

Result: **PASS** · runner tools/evals/run.sh · 14cdacd Add persistent homepage language controls and carry 

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
✔ emergency and crisis contacts follow the selected country, not the language (0.916333ms)
✔ an unknown country gets a local-services instruction without an invented number (0.141792ms)
✔ the Indonesian word reseptor does not trigger the prescription boundary (1.350667ms)
ℹ tests 3
ℹ suites 0
ℹ pass 3
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 159.100042
```

## Review deployment and reference media — PASS

```
✔ reference films require an explicit marker and prefer a supplied target edition (0.298417ms)
✔ review candidates protect live learner records and credentials while retaining authentication (0.439959ms)
ℹ tests 2
ℹ suites 0
ℹ pass 2
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 100.469708
```

## RAG groundedness (grounded coach) — PASS

```
rag index loaded: 1546 chunks (62890a46aab59d01)
✓ rag groundedness [en]: 4 pass · 0 fail
```

## Paid enrolment boundaries — PASS

```
✔ October pricing follows Los Angeles midnight boundaries and invalid offers keep the regular price (0.554875ms)
✔ no-cost sessions carry enrollment metadata without requesting a PaymentIntent (0.336708ms)
✔ stripe signature: valid, tampered, stale, missing (0.34075ms)
✔ the session form charges the course price in cents, locks the email and carries the course (0.084667ms)
✔ on a shared Stripe account: the session and the payment say platform perceptors; promotion codes stay off (0.083875ms)
✔ checkout: a signed-in learner gets a Stripe session; anonymous is refused; an enrolled learner is not charged again (19.897084ms)
✔ password sign-in without email verification gives an actionable error and never creates checkout; a refreshed verified identity can continue (6.808375ms)
✔ checkout without keys answers 503; a free academy has no checkout (2.875417ms)
✔ return from Stripe: the paid session enrols its own email only (2.583042ms)
✔ webhook: signed and paid enrols; unsigned, unpaid or another course does not (3.470375ms)
✔ a complete session with nothing to pay enrols; an open no-charge session does not (1.937541ms)
✔ secrets pasted with a trailing newline still work (Authorization header and webhook signature) (1.768375ms)
✔ the server creates a zero session during October and refuses stale or manipulated browser prices after expiry (3.523958ms)
✔ an October enrollment can be fulfilled after expiry; open, nonzero, and other-course no-cost sessions are refused (2.975041ms)
ℹ tests 14
ℹ suites 0
ℹ pass 14
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 156.711416
```

## Verification email identity and delivery boundaries — PASS

```
✔ verification mail binds recipient and return URL to trusted identity/configuration; duplicate sends are throttled (69.656208ms)
✔ anonymous requests, caller-chosen recipients/URLs and unsupported methods cannot send verification emails (6.361958ms)
✔ disabled and changed-email accounts cannot send; already verified accounts need no email (3.519042ms)
verification email request failed resend-delivery provider-error unspecified unspecified
✔ provider failure is explicit and retryable; missing secret prevents delivery (15.244917ms)
✔ email template escapes untrusted text, includes plain text and uses email-safe layout (4.372125ms)
✔ branded emails preserve logo scale, colors, and legal links beneath a mounted academy (3.8385ms)
ℹ tests 6
ℹ suites 0
ℹ pass 6
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 438.004375
```

## Today line (rotation, moments) — PASS

```
✔ one line per local day, the same all day, walking forward with "Another" (1.08725ms)
✔ a line opens the pane its moment sits on, or nothing when the moment is not in this build (0.3255ms)
✔ a line opens only where the learner has been; further on in the module reads "later", beyond it "ahead" (0.060958ms)
ℹ tests 3
ℹ suites 0
ℹ pass 3
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 99.849625
```

