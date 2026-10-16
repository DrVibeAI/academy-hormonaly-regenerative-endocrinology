# Hormonaly Academy design QA

**Date:** 2026-10-15  
**Surface:** signed-in learner course overview, lesson cards, activities and final-check entry  
**Account:** Omar S (`omar@hormonaly.ai`)  
**Viewport:** Codex in-app browser, desktop (1111 × 943 screenshot)

## Scope and coverage

The learner path was used to complete all seven modules. Activities, quizzes, hotspots, sorters, audio, transcript panels, regulatory disclosures and saved checklists were exercised through the normal course UI. Modules 1 and 2 initially resumed at steps 18 and 4; I later opened their earlier screens in review mode. Previously completed interaction state was retained, so those earlier activities were inspected but not replayed. Module 3 and modules 4–7 were traversed from their first lesson step. The final check was opened to its first question, left unanswered and unsubmitted. The certificate remains pending.

Language pass: modules 1–3, 5 and 7 were trialed in English; modules 4 and 6 were trialed in Arabic. The course overview and a previously active lesson were also checked in both languages. This gives functional coverage of the main activity types in both locales, but does not constitute a screen-by-screen translation review of every lesson in both languages. The course language is currently English.

## Findings

### P2 — Lesson footer is wider than the content card

On the active lesson screen, the lesson card is inset about 50 px from each side of the player column, while the sticky previous / step count / next footer spans the full player column. This makes the bottom bar feel oversized beside the card. The same relationship appears in English and Arabic. Align the footer to the card edges, or reduce its visual weight and width so it reads as a separate control rail.

### P2 — Large unused areas weaken lesson-card balance

The active practice card ends well above the bottom of the lesson stage, leaving roughly 120 px of blank stage space before the footer. In the course overview, the module rows also leave broad blank spans between their copy and the right-side action/lock control (English) or between the left-side lock and right-aligned copy (Arabic). Some whitespace is useful, but these gaps make the layout feel sparse and make row alignment harder to compare. Review card row grid columns and vertical stage sizing across card types.

### P3 — Arabic overview duration grammar

Arabic course metadata currently reads **“7 وحدات · 4 ساعة 55 دقيقة”** and the final-check row reads **“14 أسئلة · 5 دقيقة.”** The numbers and units are understandable, but the forms are grammatically mismatched. Suggested copy: **“7 وحدات · 4 ساعات و55 دقيقة”** and **“14 سؤالًا · 5 دقائق.”** Validate the preferred house style with the Arabic editor.

### P2 — Arabic opening films remain English

In the Arabic versions of modules 4 and 6, the opening film is explicitly labelled as the original English version with the Arabic version still in production. Opening the transcript in module 4 also displays English text. The surrounding lesson, controls, and later narration are Arabic, so the untranslated opening is conspicuous and interrupts the localized course flow.

### P2 — Evidence sorter gives weak per-item feedback

In module 3's six-item gut-toolkit sorter, two incorrect classifications were accepted without an immediate per-item signal. Only after all six selections did the page show 4/6 and the correct mappings. Learners can finish the activity without knowing which selections need review until the end. Add clear correct/incorrect feedback as each item is placed, or provide a retry affordance before advancing.

### P3 — Arabic lesson heading has broken word order

Module 6, step 7 renders the heading **“العوز تشخيص. والتراجع شيخوخة.”** The word order and punctuation read like an unedited literal translation. Have an Arabic editor rewrite this heading in natural Arabic.

### P3 — Course progress reads 100% while the final check is pending

After all seven modules are complete, the overview displays **“100% complete”** beside a **Start the final check** button, while the certificate status is **Pending**. The separate labels do distinguish lesson completion from credential completion, but the 100% label can imply the course itself is finished before the required assessment. Consider wording the progress as “All modules complete” or showing lesson and assessment progress separately.

## Passed in this pass

- The learner flow advanced sequentially through modules 1–7; the module drawer showed each module marked completed and the overview confirmed all seven modules complete.
- The activity types exercised in English and Arabic accepted their inputs: audio play/pause and transcript expansion, evidence and regulatory sorters, ordering activities, image hotspots, claim review, multi-decision fictional cases, quick checks, expandable rationales, country-status panels, and closing checklists.
- The quiz and activity feedback enabled progression after completion. Quick checks returned correct/incorrect rationale panels; completed sorters and cases showed final answer summaries.
- English course overview displays all seven module titles, duration, completion state, final-check entry, and pending certificate block. Arabic course overview showed the same content in RTL flow, with copy right-aligned and controls/thumbnails on the opposite edge.
- English and Arabic active lesson screens retain the same centered lesson stage and three-part bottom navigation; RTL reverses control order as expected.
- The final check opens at question 1 of 14. It was not answered or submitted; the certificate remains pending.

## Follow-up needed for full coverage

Review the English opening-film transcripts against the Arabic release plan, have the flagged Arabic copy professionally edited, and clarify the progress label. For a complete localization sign-off, replay all seven modules screen by screen in both languages and check responsive widths; this trial exercised each activity type across the two languages but did not replay every card in both locales. The assessment remains available at the final-check entry on the overview.
