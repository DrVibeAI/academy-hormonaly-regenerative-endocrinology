# Evals — academy-inputs — 2026-10-08T040729Z

Result: **PASS** · runner tools/evals/run.sh · ab5067a Hide the skip link without creating RTL horizontal o

## Locale parity — PASS

```
✓ parity eval [ar, en]: 3879 localized fields checked · 0 issue(s)
```

## Guía consistency & clinical safety — PASS

```
✓ tutor evals: 64 pass · 0 fail (29 cases)
```

## Regional emergency routing and clinical terms — PASS

```
✔ emergency and crisis contacts follow the selected country, not the language (1.575417ms)
✔ an unknown country gets a local-services instruction without an invented number (0.161375ms)
✔ the Indonesian word reseptor does not trigger the prescription boundary (1.390708ms)
ℹ tests 3
ℹ suites 0
ℹ pass 3
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 197.613166
```

## Review deployment and reference media — PASS

```
✔ reference films require an explicit marker and prefer a supplied target edition (0.404792ms)
✔ review candidates protect live learner records and credentials while retaining authentication (0.595875ms)
ℹ tests 2
ℹ suites 0
ℹ pass 2
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 92.829208
```

## RAG groundedness (grounded coach) — PASS

```
rag index loaded: 1546 chunks (62890a46aab59d01)
✓ rag groundedness [ar]: 4 pass · 0 fail
```

## Paid enrolment boundaries — PASS

```
✔ October pricing follows Los Angeles midnight boundaries and invalid offers keep the regular price (0.455667ms)
✔ no-cost sessions carry enrollment metadata without requesting a PaymentIntent (0.277666ms)
✔ stripe signature: valid, tampered, stale, missing (0.282333ms)
✔ the session form charges the course price in cents, locks the email and carries the course (0.083416ms)
✔ on a shared Stripe account: the session and the payment say platform perceptors; promotion codes stay off (0.073042ms)
✔ checkout: a signed-in learner gets a Stripe session; anonymous is refused; an enrolled learner is not charged again (18.937375ms)
✔ password sign-in without email verification gives an actionable error and never creates checkout; a refreshed verified identity can continue (6.045916ms)
✔ checkout without keys answers 503; a free academy has no checkout (4.430666ms)
✔ return from Stripe: the paid session enrols its own email only (3.791083ms)
✔ webhook: signed and paid enrols; unsigned, unpaid or another course does not (3.816708ms)
✔ a complete session with nothing to pay enrols; an open no-charge session does not (1.569292ms)
✔ secrets pasted with a trailing newline still work (Authorization header and webhook signature) (1.3095ms)
✔ the server creates a zero session during October and refuses stale or manipulated browser prices after expiry (2.572916ms)
✔ an October enrollment can be fulfilled after expiry; open, nonzero, and other-course no-cost sessions are refused (2.610709ms)
ℹ tests 14
ℹ suites 0
ℹ pass 14
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 130.238291
```

## Verification email identity and delivery boundaries — PASS

```
✔ verification mail binds recipient and return URL to trusted identity/configuration; duplicate sends are throttled (69.934417ms)
✔ anonymous requests, caller-chosen recipients/URLs and unsupported methods cannot send verification emails (6.645ms)
✔ disabled and changed-email accounts cannot send; already verified accounts need no email (3.5835ms)
verification email request failed resend-delivery provider-error unspecified unspecified
✔ provider failure is explicit and retryable; missing secret prevents delivery (13.632875ms)
✔ email template escapes untrusted text, includes plain text and uses email-safe layout (4.097708ms)
✔ branded emails preserve logo scale, colors, and legal links beneath a mounted academy (4.156875ms)
ℹ tests 6
ℹ suites 0
ℹ pass 6
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 398.037583
```

## Today line (rotation, moments) — PASS

```
✔ one line per local day, the same all day, walking forward with "Another" (0.982375ms)
✔ a line opens the pane its moment sits on, or nothing when the moment is not in this build (0.347833ms)
✔ a line opens only where the learner has been; further on in the module reads "later", beyond it "ahead" (0.067958ms)
ℹ tests 3
ℹ suites 0
ℹ pass 3
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 72.59725
```

