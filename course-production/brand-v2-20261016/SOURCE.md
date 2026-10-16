# Source and asset provenance

- Supplied by Omar: `Hormonaly-Academy-Brand-Book-v2.pdf`, 16 October 2026.
- SHA-256: `95a5d98ea07eb5c828503b4ee6a62eda71d505f6c82bdb66c19902e8417fd675`.
- Wordmark: original vector geometry and outlined lettering extracted from PDF page 12. Presentation panel and shadow removed for transparency.
- Orbit: existing academy vector geometry, recoloured to the v2 Ink value. Lilac watermark and app icon derive from the same vector.
- Google Sans Flex and Noto Sans Arabic: official `google/fonts` OFL directories; variable TTF source files and OFL licences accompany the WOFF2 and certificate TTF exports.
  - https://github.com/google/fonts/tree/main/ofl/googlesansflex
  - https://github.com/google/fonts/tree/main/ofl/notosansarabic
- `extract-identity.py <brand-book.pdf>` uses PyMuPDF and fontTools with Brotli; run after placing source TTF files in the versioned font directory.
- Six actual learner screenshots were captured in the Codex in-app browser at 390 × 844, using a local demonstration learner. Capture manifest records paths, locale, SHA-256, source package, and brand fingerprint. Progress/choices in these images are illustrative local state.
- `build-sharing.py` creates the two 1200 × 630 HTML compositions. Screenshots of those pages supply the PNG sharing assets. Their phone displays use the actual learner captures.
- Certificate PDFs are design proofs with `SAMPLE-DESIGN`, generated through the normal PDF renderer. No certificate was issued.
- Verification-email HTML files are local visual proofs, with a non-token sign-in URL. No email was sent.
