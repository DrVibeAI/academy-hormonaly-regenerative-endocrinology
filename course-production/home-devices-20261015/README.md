# Compact homepage course previews

Local draft requested by Omar on 2026-10-15. Reference: the supplied three-phone shopping-app composition. Hormonaly uses its own actual course screenshots and localized feature descriptions.

- Desktop: three evenly spaced 200px devices, with floating callouts.
- Mobile: 156px devices in one horizontally scrollable row. At 390px the entire section is about 554px high, replacing the initial tall stack.
- English and Arabic; native RTL scrolling and callout text in Arabic.
- Original screenshot files and capture manifest remain unchanged. All styling is live HTML/CSS; screenshot text is not generated or retouched.
- Keyboard focus and arrow scrolling work; hover effects are disabled for reduced motion.
- Verified 320px, 390px, 768px and 1280px layouts without page overflow. All source images loaded. English keyboard scroll advanced to the next preview. Arabic desktop/mobile were visually inspected.
- Runtime isolation, locale scan, both TypeScript configurations and Vite build passed. Existing bundle-size warning remains. The pnpm wrapper attempted an unnecessary dependency refresh against the shared node_modules symlink and stopped; the same build stages were run directly without changing dependencies.

Proofs: `home-devices-en.png`, `home-devices-mobile-en.png`, `home-devices-mobile-ar.png`. Measurements: `home-device-checks.json`. Build: `build-device-showcase.txt`.

Preview: http://127.0.0.1:5199/?home#inside. Publication remains pending owner approval.
