// Run from the perceptor-runtime checkout with an output directory containing the
// exact archived source ref pinned by the partner store:
// node build-preview.mjs <store-dir> <candidate-json> <archived-source-dir> MX|ID
// This creates an invitation-only review input; it does not approve or publish a locale.
import { readFileSync, writeFileSync, cpSync, readdirSync, mkdirSync } from 'node:fs'
import { join, resolve } from 'node:path'
import { createRequire } from 'node:module'
import { createHash } from 'node:crypto'

const require = createRequire(process.cwd() + '/package.json')
const { parse, stringify } = require('yaml')
const [storeDir, candidatePath, outDir, market] = process.argv.slice(2)
if (!storeDir || !candidatePath || !outDir || !['MX', 'ID'].includes(market)) throw Error('Usage: store candidate output MX|ID')
const store = parse(readFileSync(join(storeDir, 'store.yaml'), 'utf8'))
const entry = store.courses.find((c) => c.id === 'hormones-peptides-skin')
const sourcePath = join(outDir, entry.package)
const sourceHash = createHash('sha256').update(readFileSync(sourcePath)).digest('hex')
if (sourceHash !== entry.sha256) throw Error('Store source package pin does not match archived source')

const isObject = (v) => v && typeof v === 'object' && !Array.isArray(v)
const merge = (a, b) => {
  if (b === null) return undefined
  if (Array.isArray(b)) return Array.isArray(a) && b.every(isObject) ? [...b.map((x, i) => merge(a[i], x)), ...a.slice(b.length)] : b
  if (isObject(b)) { const out = { ...(isObject(a) ? a : {}) }; for (const [k, v] of Object.entries(b)) { const m = merge(out[k], v); if (m === undefined) delete out[k]; else out[k] = m } return out }
  return b
}
const overlay = parse(readFileSync(resolve(storeDir, entry.overlay), 'utf8'))
const academy = merge(parse(readFileSync(join(outDir, 'academy.yaml'), 'utf8')), overlay)
for (const name of readdirSync(resolve(storeDir, entry.overlayFiles))) {
  const from = resolve(storeDir, entry.overlayFiles, name)
  const to = join(outDir, name)
  mkdirSync(to, { recursive: true })
  cpSync(from, to, { recursive: true, force: true })
}

const candidate = JSON.parse(readFileSync(candidatePath, 'utf8'))
const tag = market === 'MX' ? 'es-MX' : 'id'
const locale = candidate.locales.find((l) => l.locale === tag)
if (!locale || locale.status !== 'draft' || candidate.governance?.accreditation?.status !== 'not_submitted') throw Error('Expected unapproved candidate')
locale.status = 'in_review'
locale.notes = 'Invitation-only text preview authorized by Omar on 2026-09-29. Local clinical, regulatory, language and media reviews remain open.'
candidate.version = '1.1.0-localization-preview.1'
candidate.credential = null
candidate.distribution.targets[0].notes = 'Private invitation-only text preview. English films; no credential. Regional review and distribution paperwork remain open.'
writeFileSync(sourcePath, JSON.stringify(candidate, null, 2) + '\n')

const notice = market === 'MX' ? {
  en: 'Translation preview. Mexico clinical and regulatory review is still in progress. Videos are in English. No certificate is issued.',
  es: 'Vista previa de la traducción. La revisión clínica y regulatoria para México sigue en curso. Los videos están en inglés. No se emite constancia.',
} : {
  en: 'Translation preview. Indonesia clinical and regulatory review is still in progress. Videos are in English. No certificate is issued.',
  id: 'Pratinjau terjemahan. Tinjauan klinis dan regulasi untuk Indonesia masih berlangsung. Video berbahasa Inggris. Sertifikat belum diterbitkan.',
}
academy.localePreview = { visibleLocales: [tag], notice }
delete academy.brand?.certificatePresentation
delete academy.home?.certificate
delete academy.catalog?.[0]?.accreditation
delete academy.catalog?.[0]?.certificate
delete academy.catalog?.[0]?.final
academy.home.faq = (academy.home.faq ?? []).filter((item) => !/CME|CE credit|What do I get at the end/i.test(item.q?.en ?? ''))
academy.home.faq.push({
  q: { en: 'Is a certificate issued during this preview?', [market === 'MX' ? 'es' : 'id']: market === 'MX' ? '¿Se emite una constancia durante esta vista previa?' : 'Apakah sertifikat diterbitkan selama pratinjau ini?' },
  a: { en: 'No. This is a translation preview while regional clinical, regulatory and media reviews are in progress.', [market === 'MX' ? 'es' : 'id']: market === 'MX' ? 'No. Esta es una vista previa de la traducción mientras continúan las revisiones clínicas, regulatorias y de medios para México.' : 'Tidak. Ini adalah pratinjau terjemahan selama tinjauan klinis, regulasi, dan media untuk Indonesia masih berlangsung.' },
})
const marketName = market === 'MX' ? 'Mexico' : 'Indonesia'
academy.home.kicker.en = `${marketName} translation preview · ${academy.brand.name}`
academy.home.lede.en = `Invitation-only translation preview for clinical review. ${notice.en}`
academy.home.practice.body.en = 'Review the source evidence and draft regional notes. Verify local authorization, clinical scope, and claims before applying any teaching in practice.'
academy.home.practice.points[2].en = 'Identify local authorization and scope questions for review'
academy.home.glimpses.items[0].caption.en = 'An English film opens every module'
academy.home.trust.title.en = 'Source evidence. Regional review in progress.'
academy.home.trust.items[1].title.en = `${marketName} notes in review`
academy.home.trust.items[1].body.en = `Regional status statements for ${marketName} are draft and require named local clinical and regulatory review.`
academy.home.disclaimer.en = `${notice.en} ${academy.home.disclaimer.en}`
const regionalFaq = academy.home.faq.find((item) => /Which countries|Which markets/i.test(item.q?.en ?? ''))
if (regionalFaq) regionalFaq.a.en = `This preview is for ${marketName}. The source course also describes other jurisdictions, but ${marketName} notes are under review and must not be treated as final local advice.`
academy.catalog[0].blurb.en = `${academy.catalog[0].blurb.en} ${marketName} translation preview; local review pending.`
if (academy.brand.landing?.og) academy.brand.landing.og.description = `${marketName} translation preview for invited clinical reviewers. Local clinical and regulatory review is pending.`
academy.localization ??= { countries: [] }
academy.localization.defaultCountry = market
if (market === 'MX') {
  academy.localization.countries = [{
    code: 'MX', country: { en: 'Mexico', es: 'México' }, centers: ['México'],
    edition: { en: 'Spanish translation preview', es: 'Vista previa en español' },
    units: { en: 'Source-study units retained; local intervals require review', es: 'Se conservan las unidades de los estudios; los intervalos locales requieren revisión' },
    approval: { en: 'Mexico clinical and regulatory review pending', es: 'Revisión clínica y regulatoria de México pendiente' },
    contextLine: { en: 'Mexico notes are under review', es: 'Las notas de México están en revisión' },
    status: 'blueprint',
    learning: { locale: tag, language: 'Español (México)', shortLabel: 'ES', direction: 'ltr', review: { en: 'Local review pending', es: 'Revisión local pendiente' } },
  }, ...(academy.localization.countries ?? []).filter((c) => c.code !== 'MX')]
  academy.home.disclaimer.es = 'Vista previa educativa para profesionales de la salud. La revisión clínica y regulatoria para México sigue en curso; los videos están en inglés. Consulte las normas locales y su criterio profesional.'
} else {
  const indonesia = academy.localization.countries.find((c) => c.code === 'ID')
  if (!indonesia) throw Error('Parallaxnet overlay has no Indonesia profile')
  indonesia.country.id = 'Indonesia'
  indonesia.edition = { en: 'Indonesian translation preview', id: 'Pratinjau Bahasa Indonesia' }
  indonesia.approval = { en: 'Indonesia clinical and regulatory review pending', id: 'Tinjauan klinis dan regulasi Indonesia belum selesai' }
  indonesia.contextLine = { en: 'Indonesia notes are under review', id: 'Catatan Indonesia masih dalam peninjauan' }
  indonesia.status = 'blueprint'
  indonesia.learning = { locale: tag, language: 'Bahasa Indonesia', shortLabel: 'ID', direction: 'ltr', review: { en: 'Local review pending', id: 'Tinjauan setempat belum selesai' } }
  academy.home.disclaimer.id = 'Pratinjau edukasi untuk tenaga kesehatan. Tinjauan klinis dan regulasi Indonesia masih berlangsung; video berbahasa Inggris. Gunakan penilaian profesional dan periksa peraturan setempat.'
}
writeFileSync(join(outDir, 'academy.yaml'), stringify(academy))
const previewHash = createHash('sha256').update(readFileSync(sourcePath)).digest('hex')
if (academy.presentation?.manifest) {
  const manifestPath = resolve(outDir, academy.presentation.manifest)
  const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'))
  if (manifest.sourceSha256 !== sourceHash) throw Error('Presentation source pin mismatch')
  manifest.sourceSha256 = previewHash
  manifest.packageId = candidate.id
  manifest.text = manifest.text.filter((edit) => {
    if (edit.path.startsWith('/credential/')) return false
    const current = edit.path.slice(1).split('/').reduce((value, key) => value?.[key], candidate)
    if (current === edit.to) return false
    if (current === edit.from) return true
    throw Error(`Presentation text drift at ${edit.path}`)
  })
  writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n')
}
console.log(JSON.stringify({ academy: academy.academy, package: sourcePath, sourceRef: entry.ref, sourceHash, previewHash, tag, status: locale.status, credential: candidate.credential, catalogStatus: academy.catalog[0].status, entitlement: academy.catalog[0].entitlement.type }))
