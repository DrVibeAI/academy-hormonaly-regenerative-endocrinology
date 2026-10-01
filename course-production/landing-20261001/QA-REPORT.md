# Skin course landing page — 1 October 2026

Owner request: four mobile screenshots total (one video plus three platform screens), include a scientific illustration, correct Geneva College of Longevity Science, and add portraits with Fady as faculty and Dominik Thor/Omar Saleem as advisory.

Four actual learner-runtime captures: opening film, Module 1 skin anatomy illustration, trial-evidence exercise and clinic case. Existing film/trial/case bytes retained. New science screen captured in the Codex in-app browser at 390 × 844; hash and pane recorded in presentation-inputs/home-glimpses.json. No learner data was changed.

Faculty portraits are the existing 512 × 512 WebP images from the Perceptors website's attached_assets/*-deck.webp, copied byte-for-byte. Fady's medical-review role and source authorship are retained; Dominik and Omar are explicitly Advisory. The shared runtime reads every name, role and image from academy-owned inputs. Desktop uses three columns; mobile uses compact portrait/text rows.

College name corrected in the catalog display name and FAQ, which also corrects the hero accreditation line, certificate section and logo alternative text. Course package is byte-identical to the deployed baseline: cb7b66528438d0081b05cc3d08e4b5f2625f3eac94898beb13ebafd5dd936334. No accreditation verdict, certificate policy or course-content changes.

Validation: production build, client/server typecheck, isolation and locale checks passed; both existing screenshot-provenance tests passed. Package and academy validation passed using Foundry 59dac3e, the schema version used for the previous homepage release. The historical foundry.lock a02bc40 predates the deployed interactive course/paid-entitlement schema and rejects those unchanged inputs; it was preserved. Desktop and 390px actual-browser checks show all four preview images and all three portraits loading, with no document overflow. Faculty mobile screenshot records the compact rows. Existing Vite import/chunk-size notices remain non-blocking.

Screenshots: gallery-desktop.jpg, faculty-desktop.jpg, faculty-mobile.jpg. Release evidence follows after deployment.
