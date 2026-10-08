import fs from 'node:fs'
import {createHash} from 'node:crypto'
const runtime = '/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007'
const raw = fs.readFileSync(runtime+'/config/site-defaults.json'), site = JSON.parse(raw)
const arabic = JSON.parse(fs.readFileSync(new URL('./legal-arabic.json', import.meta.url)))
if (arabic.sourceSha256 !== createHash('sha256').update(raw).digest('hex')) throw Error('Legal source changed: re-review the Arabic translation before rebuilding')
for (const key of ['terms','privacy']) {
  const doc=site[key], t=arabic[key]
  if (doc.sections.length!==t.sections.length) throw Error('Legal section count changed')
  doc.sourceVersion=doc.version
  doc.sourceSha256=createHash('sha256').update(raw).digest('hex')
  doc.version+='-ar-review-20261007'
  doc.reviewNotice={en:'Arabic translation draft — legal review pending.',ar:'مسودة ترجمة عربية — بانتظار المراجعة القانونية.'}
  doc.title.ar=t.title
  doc.sections.forEach((section,i)=>{
    const [title,...paragraphs]=t.sections[i]
    if (section.paragraphs.length!==paragraphs.length) throw Error('Legal paragraph count changed')
    section.title.ar=title
    section.paragraphs.forEach((p,j)=>p.ar=paragraphs[j])
  })
}
site.certificatePartner.note.ar='شريك تقنيات التعلم. لا تمنح هذه العلامة اعتماد GCLS.'
fs.writeFileSync(new URL('./site.ar-AE.review.json',import.meta.url),JSON.stringify(site,null,2)+'\n')
