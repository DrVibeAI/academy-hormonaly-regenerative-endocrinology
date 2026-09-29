# Regional skin editions: QA and release status

Checked 2026-09-29 against Hormonaly package 1.1.0, SHA256 `6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa`. The three files in `candidates/` remain private drafts. This report replaces the earlier pass claims, which counted drafted notes as completed regulatory review and misstated media readiness.

## What was verified

- All three draft packages preserve the source course's module and lesson structure. The text inventory reports 3,796 retained translatable fields per edition. `QA-REPORT.md`, `QUALITY-FLAGS.json`, and `NUMERIC-REVIEW.*.json` hold the detailed machine checks. Those checks are pre-review, not clinical or native-language sign-off.
- The shared runtime now routes urgent and crisis contact information by the learner's selected country, in both the local tutor and grounded Guide. An unknown country receives generic local-services guidance. Indonesian `reseptor` no longer triggers the `resep` prescription boundary. Focused tests pass, and all 14 authored tutor prompt chips per target language retrieved their intended answer in local imports.
- Official primary sources were used to narrow three Mexico and three Indonesia regulatory notes (`m3-p09`, `m7-p13`, `m7-p16`). The Brazil draft now points to the live [ANVISA warning about home mixing of tirzepatide](https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/manipulacao-caseira-de-tirzepatida-nao-e-segura); its prior URL returned 404. These are editorial corrections, not country approval.
- Draft locale gating keeps the new languages hidden from learners. The source package and live store pins remain English. The seven video assets in each candidate are English and contain burned-in English captions; no localized film or caption is approved. Each candidate passed the runtime parity check and TypeScript typecheck when imported separately.

## Regulatory work still open

`REGULATORY-JOBS.json` lists 30 source moments needing jurisdiction review. Mexico and Indonesia each have three candidate notes and 27 moments still awaiting exact-product, route, indication, claims and profession-scope checks. A drafted note also needs in-country clinical and regulatory review. The Brazil candidate contains 29 jurisdiction variants; `m3-p11` has no Brazil note in the source inventory. Its existing variants and the new warning require a dated ANVISA recheck at release. A variant count is not a regulatory pass rate.

The local reviewers should record the exact product or substance, formulation, route, indication, authorization holder or registration number where applicable, current source URL and check date. The review CSVs currently mark target fields `unreviewed`. See `REGULATORY-REVIEW.md` and `REGULATORY-JOBS.json` for the work list.

## Owner direction and GCLS record

Omar's 2026-09-29 instruction, “use my approval for now while we optimize the GCLS review format,” is recorded as interim product-owner direction to continue remediation and staged deployment. It does not identify an in-country clinical reviewer, grant partner distribution rights, or provide written GCLS accreditation for these derivatives. Their package records therefore remain `governance.accreditation.status: not_submitted`; no derivative GCLS certificate should be issued from this instruction. The existing English store's public accreditation wording follows Omar's earlier verbal-approval direction documented in `academy.yaml`, while written confirmation and an accreditation ID remain outstanding.

`agreement: null` in a partner store means no agreement is recorded there; it is not proof that distribution is unauthorized. The agreement or other rights basis should be filed before wider commercial rollout.

## Release verdict

| Edition | Candidate text | Regional review | Local media | Launch decision |
| --- | --- | --- | --- | --- |
| Cenegenics `es-MX` | Draft complete | 3 notes drafted; 27 moments and named Mexico reviewer pending | 0/7 films | Private review only |
| Biolongeva `pt-BR` | Draft complete | 29 variants need dated ANVISA and named Brazil review | 0/7 films | Held until Biolongeva is ready |
| Parallaxnet `id` | Draft complete | 3 notes drafted; 27 moments and named Indonesia reviewer pending | 0/7 films | Private review only |

Before learner release: finish the regional work list, obtain native clinical/language and partner decisions, establish distribution rights, render and review localized films/captions and related UI, run signed-in/mobile completion checks, then pin and stage the exact approved packages. Runtime safety fixes can be deployed independently of language release.

## Runtime deployment, 2026-09-29

The safety and tutor runtime fix was staged and promoted on the existing English skin services. Cloud Run reports 100% traffic on `academy-cenegenics-skin-00004-skr`, `academy-parallaxnet-skin-00009-bxj`, and `academy-hormonaly-00026-5mn`. Each live `/_health` returned `app: ok, db: ok`; each unauthenticated `/api/certificate` request returned 401. The partner services used the exact Hormonaly 1.1.0 store pin and unchanged package SHA above. The final Hormonaly candidate was built from that same checked commit and SHA, and its review-hub record identifies version 1.1.0 at `6419297d6d01`.

An earlier Hormonaly runtime promotion, `academy-hormonaly-00025-j6x`, briefly used an older local 1.0.1 course checkout. It was replaced with the checked 1.1.0 revision above. The mistaken revision has no production traffic. At that point, no new-language candidate had been staged or added to a store edition list.

## Invitation-only translation previews, 2026-09-29

Omar approved deployment. The Mexico and Indonesia drafts were staged as **review candidates** on their existing partner services, with 0% production traffic and no change to the English store pins. The reproducible assembly is in `build-preview.mjs`: it checks the store's exact source SHA, applies the partner overlay, marks the regional language `in_review`, keeps the catalog `draft` and invitation based, removes credential and accreditation promotion from the preview landing page, and adds an explicit English-film and pending-review notice. The package governance record stays `not_submitted`. The semantic Guide index is disabled for these previews; the deterministic Guide remains available. The seven source videos remain English.

| Partner preview | Package SHA256 | Cloud Run candidate | Review URL | Live traffic |
| --- | --- | --- | --- | --- |
| Cenegenics Spanish for Mexico | `a30b4086dcd272c1ea11915ec175434ff7551f2be4b5f4df821e55b6b0a75eb0` | `academy-cenegenics-skin-00006-6b8` | [Mexico review course](https://candidate---academy-cenegenics-skin-limjs7pr6a-uc.a.run.app/hormones-peptides-skin/) | English `academy-cenegenics-skin-00004-skr` at 100% |
| Parallaxnet Bahasa Indonesia | `ec8a2c76798347d49357a1c6c441401760d44cc075882e3c7505833a8c705641` | `academy-parallaxnet-skin-00011-8bq` | [Indonesia review course](https://candidate---academy-parallaxnet-skin-limjs7pr6a-uc.a.run.app/hormones-peptides-skin/) | English `academy-parallaxnet-skin-00009-bxj` at 100% |

For both final candidates, the deployment gate passed all six runtime suites and TypeScript checks; Cloud Run reported `app: ok, db: ok`; the course route returned HTTP 200; and unauthenticated `/api/certificate` returned 401. A browser check confirmed that the public landing screen identifies the translation preview, pending regional review, English videos, and no certificate before sign-in. The preview package has `credential: null`, and the runtime blocks certificate issuance for such packages. Signed-in learner completion, native language review, and named local clinical/regulatory review remain open. Biolongeva was not staged because its launch is on hold.
