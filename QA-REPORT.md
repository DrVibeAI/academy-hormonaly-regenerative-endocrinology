> Follow-up: repairs and current verification are recorded in [QA-FIXES.md](QA-FIXES.md). The findings below describe the pre-repair audit.

# Arabic edition QA report — 7 October 2026

**Overall: FAIL / remains in review.** Read-only audit. Detailed findings, reproduction evidence and suggested repairs are in [AUDIT-FINDINGS.md](AUDIT-FINDINGS.md).

| Area | Outcome | Owner / remaining work |
|---|---|---|
| Package schema, protected structures and original Arabic field coverage | PASS mechanically | Fady still reviews medical meaning, terminology and Arabic language |
| Runtime build, type checks and isolation | PASS | Engineering |
| Account menu overlap and sampled RTL desktop/mobile behavior | PASS | Overlap corrected before this audit |
| Auth negative paths and focused local tests | PASS within tested scope | Authenticated production acceptance remains untested |
| Rendered Arabic coverage | FAIL, A05 | Localization / engineering; include homepage, library, labels and reviewed legal text |
| UAE/Saudi content delivery | FAIL, A02–A04 | Engineering plus Fady / regulatory review: visible summary, local tutor routing and formal Saudi mapping |
| Accreditation presentation | FAIL, A01 | Correct derivative presentation; no new approval inferred |
| Video preview, media completeness and caption scan | FAIL, A06–A07 | Motion/media production and engineering |
| Preview locale parity | FAIL, A08 | Seven English badge values absent |
| Review bundle currency | FAIL, A09 | Repackage after fixes |
| Claim support, Arabic medical review, media approval, final acceptance | OPEN | Exact-candidate reports and human decisions required |

Fady@hormonaly.ai is the named reviewer, not a recorded approval. No reviewer was contacted. Seven Arabic opening films and captions remain unproduced; 48 Arabic audio files pass checksum verification, with pronunciation review pending. No slides are required.

No implementation, package, governance, catalog or deployment was changed. The audit created this report, the findings report and local evidence only.

