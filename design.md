# <Academy name> — design contract

> Stage 05 artifact (contract: perceptor-foundry `docs/design-contract.md`). Every customer-visible
> surface — landing, app, videos, certificates, emails — follows this document. Status: **proposed**
> until the approval block is signed by the `brand_approval` owner.

## 1 · Identity in one sentence

<Subject, audience, register — e.g. "Clinical-scientific editorial calm for health-curious adults in
pt-BR: evidence first, one blue, no noise.">

## 2 · Palette

Derived from: <customer kit | the logo (name the file) | proposed — no brand existed>.

| Token | Hex | Role |
|---|---|---|
| paper | `#` | page ground |
| panel | `#` | cards / raised surfaces |
| ink | `#` | primary text |
| muted | `#` | secondary text |
| line | `#` | hairlines, borders |
| primary | `#` | THE accent — actions, emphasis (from the logo) |
| primary-deep | `#` | hover / emphasis-strong |
| primary-soft | `#` | accent washes |

Usage ratio: ~70% paper/panel · ~20% ink/muted · ≤10% primary. Contrast: body text ≥ 4.5:1 on its ground;
primary on paper ≥ 4.5:1 for text uses.

## 3 · Typography

| Role | Face | Fallbacks | Rules |
|---|---|---|---|
| Display | <face> | <stack> | headings, weights, tracking |
| Body | <face> | <stack> | 16px base, 1.6 line-height |
| Utility | <face, usually a mono> | <stack> | uppercase microlabels +0.12em, data, citations |

## 4 · Shape & spacing

Radius: <one value, e.g. 2px> everywhere. Hairline rules (1px, `line`). Shadow recipe: <one soft recipe or
none>. Spacing scale: 8 / 16 / 24 / 40 / 64.

## 5 · Logo

Always the real asset: `assets/<slug>-logo.png` (+ variants). Minimum width <px>, clear space <rule>,
approved backgrounds <list>. **Never retype the wordmark, never recolor, never substitute a drawn glyph.**

## 6 · Imagery

<What images are here: information design (charts, diagrams in the palette), real product, released
faculty photography.> Not: stock people, fabricated clinical imagery, decorative filler. Faculty
photography only with `media.likenessRelease` on file.

## 7 · Slop kill-list (binding)

No gradient hero tiles · no CDN icon packs · no emoji as UI · no borrowed platform palettes · no
retyped/invented logos · no rounded-everything · no fake UI (simulated players, counterfeit tutors,
fabricated verification badges) · no unverifiable claims as design copy.

## 8 · Approval

`brand_approval`: **pending** — <name from governance.owners.brand> signs this document against a rendered
specimen (see `course-production/design/`). Date: —
