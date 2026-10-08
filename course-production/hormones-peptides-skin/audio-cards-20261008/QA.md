# Audio-following cards — 8 October 2026

The chapter-card click handler previously sought to the chapter start and called play before flipping. Automatic chapter highlighting did not reveal the supporting text. The revised card state follows the existing playback chapter segments and automatically reveals each idea on entry; previous reveals remain available. Manual flips change only the card face, without seeking, starting, pausing or reloading narration. Pause/resume within the same chapter respects a manual flip. Replay resets the automatic sequence. Hidden faces are marked for assistive technology and the active outline covers the revealed face too.

The explanatory hint and flip cues were updated in all five runtime UI languages. This change uses the course's existing proportional chapter segments; it does not add word-aligned timestamps or regenerate narration. Existing illustrations, clinical claims, course IDs and learner records are unchanged.

Four focused regression tests cover chapter boundaries, unknown duration, automatic reveals, persistent manual overrides, replay/reset and cards without supporting copy. Application and server type checks pass. Browser and deployment evidence follows below.

Real browser playback used the reported lesson (`m1-p11`, lesson 1 pane 13) and its existing Arabic audio, 101.36 seconds. A manual flip before playback left time 0 and paused true. Flipping during playback moved naturally from 10.072 to 10.327 seconds instead of jumping to the beginning. Later automatic playback revealed both subsequent cards while preserving the manually closed first card. A paused flip kept the exact timestamp 68.877616 seconds. Playback reached the end normally. Replay cleared the prior faces and revealed cards in order again. Flipping the current card and resuming at 43.097915 seconds kept it closed while playback continued. The phone layout remains within 390px with three cards. Full measurements: `local-playback-proof.json`.

English rendering and the manual-before-play state were checked locally; its on-demand narration requires an authenticated learner, so actual English playback was not exercised in local mode. The shared component was exercised with the Arabic narration. `automatic-card-preview.png` shows local playback with all three cards revealed and the third chapter active.

## Deployment and hosted checks

Runtime commit `28ceea8`; behavior contract and improvement ledger commit `4802cad`. Release directory: `/Users/omar/DrVibe/releases/hormonaly-audio-cards-20261008`. Canonical candidate deployment passed all eight eval suites, offline installation and type checking. Cloud Build `7845a4bc-a1b8-45d7-be71-69283aa6fe5d` produced revision `academy-hormonaly-00057-2dv`.

The exact candidate was promoted with `deploy/gcp.sh --promote-revision=academy-hormonaly-00057-2dv`. On 8 October 2026 at 18:26 UTC, the revision served 100% of production traffic at https://hormonaly.perceptors.ai/. Health returned app/db `ok`, unauthenticated certificates returned 401, and the learner JavaScript bundle matched between candidate and production (SHA-256 `271948e907900e8eac6a370ee6316dfb93bb55f0ecc5e40ad35affaeb84aaa89`) and included the updated card behavior. Proofs: `candidate-front-end-proof.json` and `production-front-end-proof.json`.

Authenticated read-only admin checks on both candidate and production found 54 enrolled learners, 54 started, one certificate; editing version 15, three drafts, seven messages and five releases. The workspace loaded and the model was available. No assistant message was sent and no learner state was written. Proofs: `candidate-admin-proof.json` and `production-admin-proof.json`. These checks verify hosted continuity and the deployed bundle; the actual learner playback walkthrough above was local.

The bilingual clinical package digest is unchanged: `9f3f3b47199c7aad43a2e23b30476784c44ed446abfcd64b65d5dd6b2a7b4491`. This UI repair makes no new claim of medical approval, film completion or regulatory review.
