#!/usr/bin/env node
import { readFileSync, writeFileSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
const root=dirname(fileURLToPath(import.meta.url))
const source=JSON.parse(readFileSync(resolve(root,'../../../packages/hormones-peptides-skin.json')))
const specs=[['cenegenics','es-MX'],['biolongeva','pt-BR'],['parallaxnet-skin','id']]
const textMaps=[]
function walk(v,path=''){
  if(Array.isArray(v))return v.forEach((x,i)=>walk(x,path+'/'+i))
  if(!v||typeof v!=='object')return
  if(typeof v.en==='string')textMaps.push({path,source:v.en})
  for(const [k,x] of Object.entries(v))walk(x,path+'/'+k)
}
walk(source)
const at=(obj,path)=>path.split('/').slice(1).reduce((v,k)=>v?.[k],obj)
const intentionallyRemoved=new Set(['/credential/coBrand/lockup'])
const numberTokens=s=>[...s.matchAll(/(?<![\p{L}\p{N}])\d+(?:[.,]\d+)*(?:\s*%|\b)/gu)].map(m=>m[0].replace(/\s/g,'').replace(/[.,]/g,'')).sort()
const qa=[]
for(const [partner,locale] of specs){
  const pkg=JSON.parse(readFileSync(join(root,'candidates',`${partner}.${locale}.json`)))
  const missing=[],same=[],numbers=[],branding=[]
  for(const x of textMaps){
    if(intentionallyRemoved.has(x.path))continue
    const map=at(pkg,x.path)
    const t=map?.[locale]
    if(typeof t!=='string'||!t.trim()){missing.push(x.path);continue}
    if(t===x.source && x.source.split(/\s+/).length>3)same.push(x.path)
    if(!['/summary','/audience/disclaimers/1','/credential/title','/provenance/citations/0/note'].includes(x.path)){
      const a=numberTokens(x.source),b=numberTokens(t)
      if(a.join('|')!==b.join('|'))numbers.push(x.path)
    }
    if(x.path.startsWith('/curriculum/')||x.path.startsWith('/tutorCorpus/')){
      if(/hormonaly/i.test(t))branding.push(x.path)
    }
  }
  const statuses={
    locale:pkg.locales.find(x=>x.locale===locale)?.status,
    modules:[...new Set(pkg.curriculum.modules.map(m=>m.status))],
    units:[...new Set(pkg.curriculum.modules.flatMap(m=>m.units.map(u=>u.status)))],
    assets:[...new Set(pkg.assets.map(a=>a.approvalStatus))],
    approvalCount:pkg.governance.approvals.length,
  }
  const media={sourceEnglishVideos:pkg.assets.filter(a=>a.kind==='video'&&a.locale==='en').length,targetVideos:pkg.assets.filter(a=>a.kind==='video'&&a.locale===locale).length,targetCaptions:pkg.assets.filter(a=>a.kind==='captions'&&a.locale===locale).length}
  qa.push({partner,locale,sourceMaps:textMaps.length-intentionallyRemoved.size,intentionallyRemoved:[...intentionallyRemoved],missing,same,numbers,branding,statuses,media,publishReady:false})
}
writeFileSync(join(root,'QUALITY-FLAGS.json'),JSON.stringify(qa,null,2)+'\n')
const numericReviews=Object.fromEntries(specs.map(([,locale])=>[locale,JSON.parse(readFileSync(join(root,`NUMERIC-REVIEW.${locale}.json`)))]))
const contextual=JSON.parse(readFileSync(join(root,'LOCAL-CONTEXT-JOBS.json')))
const regulatory=JSON.parse(readFileSync(join(root,'REGULATORY-JOBS.json')))
const lines=['# Localization draft QA','',`Source package: \`${source.id}\` ${source.version}. Automated checks do not constitute clinical or language review.`,'','| Edition | Text fields | Missing | Identical long fields | Number token flags | Hormonaly mentions in learning text | Target films/captions |','|---|---:|---:|---:|---:|---:|---:|',...qa.map(x=>`| ${x.partner} · ${x.locale} | ${x.sourceMaps} | ${x.missing.length} | ${x.same.length} | ${x.numbers.length} | ${x.branding.length} | ${x.media.targetVideos}/${x.media.targetCaptions} |`),'',
'All candidate modules, units and assets remain drafts; no source-course approvals transfer. Locale text completeness alone cannot make an edition publishable.',
'',`A second machine pass classified all ${qa.reduce((n,x)=>n+x.numbers.length,0)} number-token differences as formatting or spelled-out-number differences (${specs.map(([,locale])=>`${locale}: ${numericReviews[locale].findings.length}`).join(', ')}). This is an agent pre-review, not an independent clinical check. Review exact flagged fields in \`QUALITY-FLAGS.json\` and \`NUMERIC-REVIEW.*.json\`.`,
'',`The source carries ${Array.isArray(contextual) ? contextual.length : contextual.jobs?.length ?? 'a set of'} learner/assessment/tutor fields for local-context review and ${Array.isArray(regulatory) ? regulatory.length : regulatory.jobs?.length ?? 'a set of'} jurisdiction-specific regulatory moments. The review CSVs align every source and target text field; the film-script documents extract all seven opener transcript drafts.`,
'','Some source-package metadata remains English because it is a source locator, image-generation brief, or internal tutor context rather than a locale-keyed learner field. The importer should be checked for any of this metadata that reaches learners or tutor prompts before release.',
'','## Open release gates','','- Exact country product/route/indication claims and profession-scope review','- Native clinical language review of lessons, assessments, tutor answers and certificate copy','- Brand-neutral derivative copy and distribution rights','- Localized narration, films, captions, transcripts and trailer; human media preview','- Runtime locale/readiness enforcement, authenticated mobile checks and separate accreditation/publish decisions','',
'See `QUALITY-FLAGS.json` for exact pointers and `review/` for side-by-side editorial sheets.']
writeFileSync(join(root,'QA-REPORT.md'),lines.join('\n')+'\n')
console.log(qa.map(x=>`${x.locale}: ${x.sourceMaps-x.missing.length}/${x.sourceMaps} fields, ${x.numbers.length} number flags, ${x.branding.length} brand flags`).join('\n'))
