#!/usr/bin/env node
// Reviewer handoff from the pinned source and private localization candidates.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const root = dirname(fileURLToPath(import.meta.url))
const source = JSON.parse(readFileSync(resolve(root, '../../../packages/hormones-peptides-skin.json')))
const reviews = join(root, 'review')
mkdirSync(reviews, { recursive: true })
const editions = [
  { key: 'cenegenics', locale: 'es-MX', label: 'Cenegenics · Mexico' },
  { key: 'biolongeva', locale: 'pt-BR', label: 'Biolongeva · Brazil' },
  { key: 'parallaxnet-skin', locale: 'id', label: 'Parallaxnet Healthcare · Indonesia' },
]
const at = (obj, path) => path.split('/').slice(1).reduce((value, segment) => value?.[segment], obj)
const q = value => `"${String(value ?? '').replaceAll('"', '""')}"`
const cells = []
const contextPaths = new Set(JSON.parse(readFileSync(join(root, 'LOCAL-CONTEXT-JOBS.json'))).jobs.map(job => job.path))
const regulatoryBlocks = JSON.parse(readFileSync(join(root, 'REGULATORY-JOBS.json'))).jobs.map(job => job.sourcePath)
function visit(value, path = '') {
  if (Array.isArray(value)) return value.forEach((item, index) => visit(item, `${path}/${index}`))
  if (!value || typeof value !== 'object') return
  if (typeof value.en === 'string') cells.push({ path, en: value.en })
  for (const [key, item] of Object.entries(value)) visit(item, `${path}/${key}`)
}
visit(source)

for (const edition of editions) {
  const candidate = JSON.parse(readFileSync(join(root, 'candidates', `${edition.key}.${edition.locale}.json`)))
  const rows = ['path,review_area,source_english,target_draft,review_status,reviewer_note']
  for (const cell of cells) {
    if (cell.path === '/credential/coBrand/lockup') continue // source-only Hormonaly lockup
    const target = at(candidate, cell.path)?.[edition.locale] ?? ''
    const area = cell.path.startsWith('/tutorCorpus') ? 'tutor' : cell.path.startsWith('/assessments') ? 'assessment' : cell.path.includes('/videoTranscript') ? 'film transcript' : cell.path.startsWith('/curriculum') ? 'lesson' : cell.path.startsWith('/provenance') ? 'citation' : 'course/presentation'
    const note = [contextPaths.has(cell.path) ? 'Check local context' : '', regulatoryBlocks.some(block => cell.path.startsWith(`${block}/`)) ? 'Check country product, route, indication and profession rules' : ''].filter(Boolean).join('; ')
    rows.push([cell.path, area, cell.en, target, 'unreviewed', note].map(q).join(','))
  }
  writeFileSync(join(reviews, `${edition.key}.${edition.locale}.review.csv`), rows.join('\n') + '\n')

  const lines = [`# ${edition.label} · module film transcript drafts`, '', `Locale: ${edition.locale}. Source film audio and burned-in captions remain English. The text below is a narration draft for each new localized render; it has not been recorded or timed.`, '']
  for (let i = 0; i < candidate.curriculum.modules.length; i++) {
    const module = candidate.curriculum.modules[i]
    const block = module.units.flatMap(unit => unit.blocks ?? []).find(item => item.metadata?.videoTranscript?.[edition.locale])
    if (!block) throw Error(`Missing ${edition.locale} transcript for ${module.id}`)
    lines.push(`## ${module.id} · ${module.title[edition.locale]}`, '', `**English reference (${block.id})**`, '', block.metadata.videoTranscript.en, '', `**${edition.locale} draft**`, '', block.metadata.videoTranscript[edition.locale], '', 'Review: clinical meaning, terminology, narration timing, on-screen words, captions, partner branding and media rights.', '')
  }
  writeFileSync(join(reviews, `${edition.key}.${edition.locale}.film-scripts.md`), lines.join('\n'))
  console.log(`${edition.locale}: ${rows.length - 1} aligned text rows; ${candidate.curriculum.modules.length} film scripts`)
}
