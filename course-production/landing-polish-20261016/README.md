# Landing-page polish — 16 October 2026

Owner request: add Omar Saleem and Fady Hannah-Shmouni LinkedIn profiles, show the real certificate with GCLS logo and existing signatures, fix footer alignment, and show actual book covers.

## Implementation

- Academy configuration now supplies all three faculty LinkedIn profiles, with localized labels.
- Certificate previews come from the production PDF renderer with a clearly marked sample learner and `SAMPLE-PREVIEW` code. The renderer now displays the already-configured partner logo and signatory institutions. Existing GCLS education-partner wording and issuance rules remain unchanged; no credential was issued.
- English and Arabic certificate image/PDF pairs are in `public/assets/certificate/previews/20261016/`. The preview links use exact locale overrides and the default English path, avoiding cross-language fallback for media URLs.
- Five authentic covers were downloaded from the bookstore's catalog. `books.json` records source URLs, titles, destination links and SHA-256 hashes. Three English books and two Arabic editions are shown in their corresponding language.
- The homepage footer uses the same content container as the page, with the wordmark, legal/support/store links, disclaimer, and platform credit. Mobile links form two columns with 44 px targets. Learner footer link padding is normalized too.

## Review

- Prepared academy and production build pass, including TypeScript.
- Desktop (830 and 1280 px) and mobile (390 px) review in English and Arabic; no horizontal overflow at 390 px. Real cover images and both certificate locales resolve. Screenshots are included here.
- Arabic book link opens the matching title's details dialog on books.perceptors.ai. The store currently labels that edition as being prepared for purchase; the landing page only invites visitors to explore it.
- Certificate PDFs are single-page A4 landscape, with GCLS logo, Fady's existing typeset signature mark and Dominik's existing signature image. Both PNG/PDF pairs were visually reviewed.
- Published as `academy-hormonaly-00072-8vk`; final production evidence is in `live/` and `../releases/academy-hormonaly-00072-8vk.md`. All eight required deployment eval suites passed.

## Reproduce certificate preview

From the sibling runtime checkout after `ACADEMY_DIR=../academy pnpm run prepare:academy`:

```sh
node --import tsx ../academy/course-production/landing-polish-20261016/render-certificates.mjs
```

Raster previews were rendered from the PDFs using PyMuPDF at 2× resolution (1684 × 1191).
