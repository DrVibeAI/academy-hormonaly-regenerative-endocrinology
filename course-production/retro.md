# Hormonaly interface repair retro — 8 October 2026

Audio cards: separating the reveal state from playback controls fixed manual flips restarting narration. A small pure state reducer made manual overrides, automatic chapter entry and replay independently testable. Real playback was necessary to check that a card flip preserved the timestamp and paused state; static screenshots could not prove this behavior.

Four focused regression tests, all eight deployment eval suites, prepared application/server type checks and candidate/production health checks passed. Existing Arabic audio provided the local playback proof. English on-demand narration was not exercised without learner authentication. No content research or medical review was part of this interface repair, so corpus hit rate and review cycles are not scored here.

The existing proportional chapter timing remains a limitation: a future word-aligned sequence requires authored or derived timestamps. The reusable interaction contract and regression lesson are recorded in the Foundry learner-experience guide and improvement ledger (`4802cad`). Hosted deployment used runtime commit `28ceea8`, exact candidate promotion and matching bundle hashes. Detailed evidence: [audio-card QA](hormones-peptides-skin/audio-cards-20261008/QA.md).
