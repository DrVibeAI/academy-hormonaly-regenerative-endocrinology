# Arabic film drafts — 15 October 2026

Seven module openers and the homepage trailer preserve the English storyboards' scene order, illustrations, presenter identity, diagram geometry and motion structure. Arabic narration, captions, labels and word-level cue timings are localized. Owner approval to publish all reviewed changes was received on 15 October 2026; see `../release-20261015/owner-approval.json`. Publication is tracked in that release folder.

## Production

- Original cinematic renderer: Foundry base `69b4706c26505bb6b03b08be6ab900b7493a0816`, with the Arabic cue, music duration and resumable HeyGen fixes in `3778b89`.
- Final renderer: HyperFrames 0.8.162; 1080 × 1920, 60 fps, delivery quality, one streaming worker per film. No motion blur.
- Presenter: original licensed HeyGen Iris stock look `2daeb4c1c74e491c89314a4e7dcd4879`. Voice: licensed ElevenLabs Yousef, v3, engaging preset. No voice clone.
- Narration: existing Arabic module transcripts; trailer translated from the original English script. Sources and medical claims were not added or broadened.
- All eight Arabic narration tracks and VTT files are retained alongside the editable local projects.
- Font: Noto Sans Arabic, embedded locally. RTL is scoped to text; the HyperFrames coordinate system remains LTR.
- Arabic cues retain Unicode letters and ignore vowel marks. Ten cue phrases were adjusted to match the exact spoken words, recorded in `cue-adjustments.json`.
- Five long onscreen labels were shortened without changing meaning, recorded in `typesetting-adjustments.json`.
- Music loops to the full narration duration and fades out. The same Module 6 mature-skin footage was retimed to fill its longer Arabic narration window; no new scene or footage was introduced.
- Web MP4s are remuxed with fast-start metadata, without re-encoding the reviewed picture or audio.

## Files and reproduction

Storyboards: `*.ar.json`; source translations: `*.translations.json`; scripts: `film-scripts.json`. `structure-check.json` compares each localized storyboard with its original after excluding only localized fields and provenance.

Local work is in `../../../media/{m01…m07,hype}` relative to this directory: audio, word alignment, plan, presenter caches, editable HyperFrames project, render and QA logs. Original illustration/footage assets are at `~/.perceptors/media/hormonaly-skin/cinematic/assets`.

`render-ready.mjs` resumes completed presenter caches and renders unfinished films. `qa-ready.mjs` runs whole-video QA once final renders exist. `wire-drafts.mjs` refuses to wire unfinished renders or missing presenter caches; it creates draft assets only. `build-review.mjs` builds the local review gallery.

To serve the gallery from the worktree root: `python3 -m http.server 8897 --bind 127.0.0.1 --directory media`.

## Review status

Automated QA reports are preserved verbatim in the QA packet. The generic b-roll rubric flags a frontal presenter face; that rule does not describe these presenter segments. Omar explicitly requested the original structure, which includes this licensed stock avatar. This is an applicability note, not a recorded human approval. Human Arabic media review remains required before publishing.

### Arabic UI demonstrations

The trailer's three original English course demonstrations are localized using actual 390×844 Arabic runtime captures of the same activities and choices: Module 4 trial sorter (pane 11), Module 7 certificate audit (pane 15), and Module 4 GLOW scenario (pane 22). `build-arabic-glimpses.mjs` assembles these captured states at the original 780×1688 / 60fps clip dimensions and durations. `finalize-project.mjs` substitutes the localized clips in the editable project while retaining the storyboard's filenames, scene order, zoom and framing. The original English files are unchanged.

## Owner publication approval · 15 October 2026

Omar: “looks good, publish all the changes to the live site”. This approves the reviewed release including the eight Arabic films and associated assets. Their package media statuses are now approved. The automated QA reports and their documented dispositions remain preserved; this is not a new medical or accreditation approval.
