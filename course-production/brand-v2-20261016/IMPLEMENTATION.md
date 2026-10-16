# Hormonaly Academy · Brand Book v2 implementation

## Status
Implemented locally on `fix/hormonaly-brand-v2-20261016`. Production has not been changed by this update. The existing production release remains the November 30 offer extension. This is an implementation specimen for owner review, not a new accreditation or medical approval.

Runtime: `fe039e58dbf1425e2b90fa0cc00fd1f52f209a78`. Academy: this commit's inputs. Design source and extraction details: [SOURCE.md](SOURCE.md).

## Applied
- Supplied v2 wordmark, near-black orbit/favicon, neutral canvas, white surfaces, blue link/selection colour, lilac accent, and Ink primary buttons.
- Self-hosted Google Sans Flex and Noto Sans Arabic. Locale-aware typography and RTL navigation preserve the Latin wordmark's orientation.
- Shared UI theme covers public home, learner navigation, Today, course overview, lesson cards, activities, quizzes, Library, notes, Guide, profile, sign-in, enrollment, legal/footer surfaces, and admin controls.
- Course page containers are centered; English copy aligns left within them, Arabic copy aligns right. Header, content and footer use the same gutters. Lesson card and bottom navigation share one width.
- Six actual English/Arabic course previews replace the old homepage screenshots. Compact device sizing remains.
- English/Arabic social images and icons under `public/seo-v2-hormonaly`, with metadata updated to the versioned paths. Editable HTML sources accompany them.
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
