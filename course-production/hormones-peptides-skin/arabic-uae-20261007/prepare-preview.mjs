import {readFileSync, writeFileSync, mkdirSync, existsSync, symlinkSync, lstatSync, unlinkSync} from 'node:fs'
import {dirname, resolve, join} from 'node:path'
import {fileURLToPath} from 'node:url'
import {createRequire} from 'node:module'
const root = dirname(fileURLToPath(import.meta.url)), academy = resolve(root, '../../..')
const require = createRequire('/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/package.json')
const {parse, stringify} = require('yaml')
const out = join(root, 'preview-inputs')
mkdirSync(join(out, 'packages'), {recursive:true})
const y = parse(readFileSync(join(root, 'academy.ar-AE.review.yaml'), 'utf8'))
const p = JSON.parse(readFileSync(join(academy, 'packages/hormones-peptides-skin.ar-AE.json')))
p.metadata.previewOnly = true
p.baseLocale = 'ar-AE'
// This private local preview uses exported reference films. The release candidate retains protected delivery.
for (const a of p.assets) if (a.kind === 'video') delete a.delivery
p.metadata.arabicEdition.previewOnly = true
p.metadata.arabicEdition.originalBaseLocale = 'en'
const ae = y.localization.countries.find(c => c.code === 'AE')
ae.learning = {...ae.learning, locale:'ar-AE', language:'العربية', shortLabel:'AR', direction:'rtl'}
if (y.home?.glimpses) delete y.home.glimpses.captureManifest
// The preview's course and legal documents are review copies, not approved public offers.
y.catalog = y.catalog.slice(0, 1)
y.catalog[0].course = 'packages/hormones-peptides-skin.ar-AE.json'
for (const m of p.curriculum.modules) for (const u of m.units) for (const b of u.blocks) {
  if (!b.metadata?.videoTranscript) continue
  b.title['ar-AE'] = 'الفيلم الأصلي بالإنجليزية — النسخة العربية قيد الإنتاج: ' + b.title['ar-AE']
  b.metadata.previewReferenceLocale = 'en'
  b.metadata.videoBadge = {en:'English reference film — Arabic edition in production', 'ar-AE':'الفيلم الإنجليزي الأصلي — النسخة العربية قيد الإنتاج'}
}
writeFileSync(join(out, 'academy.yaml'), stringify(y))
writeFileSync(join(out, 'packages/hormones-peptides-skin.ar-AE.json'), JSON.stringify(p, null, 2))
for (const name of ['public', 'presentation-inputs']) if (existsSync(join(academy,name)) && !existsSync(join(out,name))) symlinkSync(join(academy,name), join(out,name), 'dir')
// Never link an ancestor into its own descendant. Only the three preparation inputs are needed.
const production = join(out, 'course-production')
if (existsSync(production) && lstatSync(production).isSymbolicLink()) unlinkSync(production)
mkdirSync(production, {recursive:true})
for (const name of ['accreditation', 'claim-support', 'tutor']) {
  const source = join(academy, 'course-production', name), target = join(production, name)
  if (existsSync(source) && !existsSync(target)) symlinkSync(source, target, 'dir')
}
console.log(out)
