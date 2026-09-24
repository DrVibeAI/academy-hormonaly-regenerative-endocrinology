# Runtime and foundry gaps found while previewing module 04 (2026-09-24)

Previewed on a phone viewport from an isolated worktree of `perceptor-runtime` (HEAD `08792f9`, branch
`factory/tenant-from-academy-yaml`) with `COURSE=packages/hormones-peptides-skin.json`, feeding a copy of the package that
holds module 04 only. All four exercises, the stat bounds, the role router and the check render and behave correctly. These
are the things that did not, none of them content problems:

| # | Where | What | Impact | Workaround used |
|---|---|---|---|---|
| 1 | runtime `scripts/import-package.mts:118,120` | Reads `m.units[0]` and calls `fromQuiz(m.check)` on every module; crashes when a module has no `check` (any not-yet-authored module) | a partly authored course cannot be imported | preview package filtered to authored modules |
| 2 | runtime `src/App.tsx` (`lessons[id - 1]`, lines 338/784/1006) | Lessons are looked up by position from their numeric id | a course must ship modules numbered 1…N with no gaps | preview renumbered m04 → m01 |
| 3 | runtime | No renderer for block types `scenario`, `case-study`, `matrix`, `text`, `definition`, `highlight`, `poll`, `workshop`, `checkpoint`; the foundry schema and validator accept them | a dead, blank screen with no gate catching it | case moment authored as `audio` hosting the scenario interaction (the Metabolismo Real pattern) |
| 4 | runtime | `metadata.variants.audienceLevel` is not read; the learner's `role` exists in personalisation requests but no pane selects copy by it | the three role versions ship in the package but every learner sees the base copy | none yet — the base copy is role-neutral |
| 5 | runtime | Cenegenics-specific strings and keys: localStorage keys prefixed `cenegenics-`, "View full curriculum (8 modules)", "Module 01 of 08", "All 8 modules completed", Lucía's 14-day case, `index.html` title "Cenegenics Academy" | wrong copy for any other academy; shared storage keys across tenants on one origin | none |
| 6 | academy | `public/hormonaly-logo.png` referenced by `academy.yaml` is missing | broken logo in the header | none (brand kit pending) |
| 7 | academy | `academy.yaml` `catalog[0]` points at `packages/aesthetic-regenerative-endocrinology.json`, which was never authored | `perceptor check` fails on every run | none (pre-existing) |
| 8 | runtime | The app shell defaults to Spanish (`lang` default `es`); this course is English-only until localization | learners land in Spanish UI with English content | switched language in the preview |

Suggested owners: 1–5 and 8 → `perceptor-runtime`; 3 also → `perceptor-foundry` (the dead-screen audit should refuse block types the
runtime cannot draw); 6–7 → this academy repo.
