# Hormonaly interface repair retro — 8 October 2026

Audio cards: separating the reveal state from playback controls fixed manual flips restarting narration. A small pure state reducer made manual overrides, automatic chapter entry and replay independently testable. Real playback was necessary to check that a card flip preserved the timestamp and paused state; static screenshots could not prove this behavior.

Four focused regression tests, all eight deployment eval suites, prepared application/server type checks and candidate/production health checks passed. Existing Arabic audio provided the local playback proof. English on-demand narration was not exercised without learner authentication. No content research or medical review was part of this interface repair, so corpus hit rate and review cycles are not scored here.

The existing proportional chapter timing remains a limitation: a future word-aligned sequence requires authored or derived timestamps. The reusable interaction contract and regression lesson are recorded in the Foundry learner-experience guide and improvement ledger (`4802cad`). Hosted deployment used runtime commit `28ceea8`, exact candidate promotion and matching bundle hashes. Detailed evidence: [audio-card QA](hormones-peptides-skin/audio-cards-20261008/QA.md).


## Brand v2 and product UI release · 16 October 2026

Release `academy-hormonaly-00071-mhv` uses the owner-approved brand and interface, with the current live sharing release merged before publication. Fresh sharing/icon paths avoided changing cached artwork under existing URLs. Self-hosted browser and certificate fonts were checked against published bytes; existing bucket CORS was sufficient.

A live signed-in lesson check exposed a broad heading rule overriding white text over photographic covers. The follow-up keeps the cover heading inverse while preserving neutral headings elsewhere. The final candidate and production styles, plus English/Arabic browser screenshots, confirm the correction. Future brand reviews should include both plain and photographic title cards alongside ordinary lesson cards.

The standard candidate/promotion workflow preserved production while builds ran. All eight required release suites and TypeScript checks passed; the public domain serves the promoted bundle, healthy app/database, gated certificate endpoint and November 30 offer. This release added no clinical claims, accreditation changes, assessment submissions or credential issuance.

## Landing-page certificate, books and footer · 16 October 2026

Rendering the certificate specimen through the production renderer exposed a configured partner logo that the material layout had loaded but omitted. Using the actual template now keeps the preview and learner certificate consistent. Media locale selection must use an exact locale lookup with a default path: the general text fallback can otherwise select an unrelated available language. Browser review caught and corrected that English-to-Arabic PDF fallback before publication.

Real bookstore cover files and catalog deep links provide an image-led section without introducing simulated product artwork. The footer now shares the page container and uses a compact two-column mobile link layout. Build and responsive EN/AR review passed; deployment gate results and the promoted revision are recorded in the release evidence. Clinical content and credential issuance were outside this UI change.
