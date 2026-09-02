# academy-<slug>

A Perceptor academy: one course family, one tenant, one repo. Created from
`DrVibeAI/perceptor-academy-template` (mirror of `perceptor-foundry/templates/academy-repo`).
The foundry, pinned in `foundry.lock`, compiles everything here; this repo holds only
content, production artifacts, and the gate record.

- `academy.yaml` — the catalog: every course, its status, series, and who gets access
- `INTAKE.md` — stage 00 intake (who, what, profile, source lock, locales, jurisdictions)
- `packages/` — canonical course packages (`course-package.schema.json`)
- `assets/` — registered media (drafts until the media-preview gate)
- `course-production/` — narration/video/b-roll manifests, render projects
- `CODEOWNERS` — the gates: a merge is an approval
- `.github/workflows/validate.yml` — factory gates as CI on every PR

Branches: `main` = published state; `factory/*` = operator work. No direct pushes to `main`.
