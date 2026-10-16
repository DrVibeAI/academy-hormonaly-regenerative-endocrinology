# Hormonaly Academy · Brand Book v2 implementation

## Status
Approved for publication by Omar on 16 October 2026: “looks good, publish all the changes to the live site”. Release branch: `release/hormonaly-brand-v2-20261016`. Candidate publication and production verification are being recorded separately below. This is a brand and interface release; accreditation and medical approval are unchanged.

Runtime: `573706e112d83526a142fa5c5f105543012327f8` (includes the follow-up product UI refinement below). Academy: this commit's inputs. Design source and extraction details: [SOURCE.md](SOURCE.md).

## Applied
- Supplied v2 wordmark, near-black orbit/favicon, neutral canvas, white surfaces, blue link/selection colour, lilac accent, and Ink primary buttons.
- Self-hosted Google Sans Flex and Noto Sans Arabic. Locale-aware typography and RTL navigation preserve the Latin wordmark's orientation.
- Shared UI theme covers public home, learner navigation, Today, course overview, lesson cards, activities, quizzes, Library, notes, Guide, profile, sign-in, enrollment, legal/footer surfaces, and admin controls.
- Course page containers are centered; English copy aligns left within them, Arabic copy aligns right. Header, content and footer use the same gutters. Lesson card and bottom navigation share one width.
- Six actual English/Arabic course previews replace the old homepage screenshots. Compact device sizing remains.
- English/Arabic social images and icons under `public/seo-v3-hormonaly`, with metadata updated to the versioned paths. Editable HTML sources accompany them.
- Verification email branding and certificate renderer updated. Certificate proofs use the new fonts, original logo, lilac watermark and blue course title. Footer overflow is corrected; all three proof PDFs are one page.
- Homepage section links explicitly scroll to their target, including links opened before React mounts.

## Evidence
- `pnpm run prepare:academy`: passed with all six capture hashes, current package digest and brand fingerprint.
- `pnpm run build`: passed, including TypeScript, isolation and locale checks. Existing bundle-size warning remains. No new test suites were added or run.
- Visual review: English and Arabic home/course/science/activity screens at 390 × 844; desktop course and lesson at 1280 × 720; Arabic Today, Library, notes and profile; English and Arabic sign-in.
- Desktop course: heading, hero and syllabus all start at x=124 with a 1124px content width.
- Desktop lesson: card and footer both start at x=244 with a 792px width, inside the centered 820px lesson frame.
- Mobile home: viewport and document both 390px wide, with a compact horizontally scrollable device gallery.
- Local proofs: screenshots under `screens/`; EN/AR and long-name certificate PDFs; EN/AR verification-email HTML. These do not issue certificates or send mail.

## Scope and release notes
- The new styles are opt-in via `brand.theme: material`. The shared runtime remains academy-configured. Existing editorial skin output is preserved.
- The public sign-in screen was inspected; no new authenticated admin walkthrough was performed. Admin styles were applied through the common theme and checked in source/build.
- This is a brand/layout review, not a repeat of the earlier end-to-end course QA. Existing course videos, narration, scientific illustrations and assessment content have not been re-rendered or rewritten. Typography baked into those videos retains its existing design.
- The free offer remains through November 30, 2026 (expires December 1, 00:00 Pacific). Bookstore links and supplied faculty credentials are preserved.
- No cloud deployment, live enrollment mutation, production progress update, certificate issuance or outbound email occurred in this update.
- Publish via `ACADEMY_DIR=../academy deploy/gcp.sh` after owner approval and the repository's normal provenance/release gates. No direct deployment or gate bypass.

## Preview
- Home: http://127.0.0.1:5199/?home#inside
- Course: http://127.0.0.1:5199/?capture#/course
- Production-built sign-in: http://127.0.0.1:5200/login

## Follow-up: modern Apple-like product UI
Owner direction: “make sure to Apply a modern apple product like UI across all elements”. The supplied brand typography, palette, logos and clinical content remain authoritative.

- Shared navigation uses subtle translucency with an opaque fallback and reduced-transparency support. Selected destinations have a restrained inset treatment; controls retain keyboard focus and reduced-motion support.
- Modules are a continuous grouped list with inset separators, neutral metadata and 44px actions. Individual nested card shadows and lifting rows are removed.
- Resource/locale segments, account sheets, grouped settings, forms, admin tables, Guide bubbles and homepage framing share the same surface hierarchy and touch sizes.
- The lesson footer keeps its card width, restores its progress counter on mobile, and gives Next a compact pill instead of a full-width bar.
- Restored the final-check and certificate rows hidden by the legacy mobile stylesheet. Their existing enrollment/completion gates remain intact.
- Mobile homepage header places the language selector beside the logo and all section links plus Sign in on the row below. Both reading directions fit within 390px.
- Six actual course captures and both 1200 × 630 sharing images are refreshed. All configured PNG files contain PNG bytes; browser screenshots saved as JPEG are identified by `.jpg`.

Visual review in the Codex in-app browser: English/Arabic 390 × 844 course, lesson, practice and home; Arabic Library, account sheet, profile/settings and Guide; English desktop course/lesson at 1280 × 720. Course/hero/syllabus start at x=124 with width 1124; lesson card/footer start at x=244 with width 792. Mobile document width equals the 390px viewport. Proofs are in `product-ui/`, with the six homepage specimens under `public/assets/hormones-peptides-skin/home/brand-v2/`.

Preparation validates the six image hashes. The production build, TypeScript, locale and tenant-isolation checks pass. Existing Vite configuration/chunk warnings remain. No additional automated test suites or authenticated admin walkthrough were run for this visual refinement. No deployment, email, certificate or production learner mutation occurred.

## Publication preparation · 16 October 2026

- Current production baseline: `academy-hormonaly-00069-7bp`, runtime `26b29048dfdc`, academy `33933137af65`.
- The current live sharing release is merged into this release history. Its v2 JPEG artwork and original icons remain available; the approved new brand images and icons use fresh `seo-v3-hormonaly` URLs.
- Runtime target: `573706e112d83526a142fa5c5f105543012327f8`. Publication uses the standard Cloud Run candidate and exact-revision promotion flow.
- Public media bucket already permits cross-origin GET/HEAD, including font delivery. No CORS change is needed.
