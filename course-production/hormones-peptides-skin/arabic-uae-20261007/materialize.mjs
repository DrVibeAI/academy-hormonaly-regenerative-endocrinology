import {readFileSync,writeFileSync,mkdirSync,readdirSync,existsSync} from 'node:fs'
import {createHash} from 'node:crypto'
import {createRequire} from 'node:module'
import {dirname,resolve,join} from 'node:path'
import {fileURLToPath} from 'node:url'
const root=dirname(fileURLToPath(import.meta.url)),academyRoot=resolve(root,'../../..'),locale='ar-AE'
const require=createRequire('/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/package.json')
const {parse,stringify}=require('yaml')
const sha=s=>createHash('sha256').update(s).digest('hex')
const bytes=readFileSync(join(academyRoot,'packages/hormones-peptides-skin.json'))
const original=JSON.parse(bytes),pkg=structuredClone(original)
const main=JSON.parse(readFileSync(join(root,locale+'.draft.json')))
const supplemental=JSON.parse(readFileSync(join(root,locale+'.supplemental-draft.json')))
if(main.sourceSha256!==sha(bytes)||main.missingHashes.length||supplemental.missingHashes.length)throw Error('Source mismatch or incomplete translation')
const translations={...main.translations,...supplemental.translations}
const fixes=existsSync(join(root,'corrections.json'))?JSON.parse(readFileSync(join(root,'corrections.json'))):{}
Object.assign(translations,fixes)
const translate=s=>translations[sha(s)]??s
let localized=0
function walk(v){
 if(Array.isArray(v))return v.forEach(walk)
 if(!v||typeof v!=='object')return
 if(typeof v.en==='string'){
  const ar=translations[sha(v.en)];if(typeof ar!=='string'||!ar.trim())throw Error('Missing translation: '+v.en.slice(0,70))
  v[locale]=ar;localized++
 }
 for(const [k,x]of Object.entries(v))if(k!==locale)walk(x)
}
walk(pkg)
const owner='Fady Hannah-Shmouni, MD FRCPC — Fady@hormonaly.ai'
pkg.version='1.2.0-ar-AE.draft.1'
pkg.locales.push({locale,name:'العربية — الإمارات العربية المتحدة',direction:'rtl',status:'in_review',reviewOwner:owner,unitsPolicy:'Preserve source-study units and reference intervals; no silent conversions; apply the local laboratory range in practice.',notes:'UAE-first Modern Standard Arabic; Saudi product-status supplement is a proposed source-lock amendment. English approvals do not approve this edition.'})
for(const entry of pkg.tutorCorpus){
 const arabic=entry.keys.map(translate)
 entry.keys=[...new Set([...entry.keys,...arabic,...arabic.map(s=>s.normalize('NFKD').replace(/[\u064B-\u065F\u0670]/g,'').replace(/[أإآ]/g,'ا'))])]
}
for(const m of pkg.curriculum.modules)for(const u of m.units){
 u.metadata={...u.metadata,localizedTutorContext:{en:u.tutorContext??'',[locale]:translate(u.tutorContext??'')}}
}
pkg.metadata={...pkg.metadata,sourcePackage:{id:original.id,version:original.version,sha256:sha(bytes)},arabicEdition:{locale,primaryJurisdiction:'AE',secondaryJurisdiction:'SA',reviewOwner:owner,status:'in_review',textComplete:true,mediaComplete:false,publishReady:false,sourceApprovalsApplyTo:'English source only',regulatoryAddendum:'course-production/hormones-peptides-skin/arabic-uae-20261007/regulatory-addendum.json'}}
// A separate package is a review candidate. Historical source approvals remain
// in the original package and are not carried across to approve this derivative.
pkg.governance.approvals=[]
pkg.governance.requiredGates=[...new Set([...pkg.governance.requiredGates,'regulatory_review'])]
pkg.governance.accreditation={body:'GCLS',status:'not_submitted',notes:'Arabic locale derivative awaiting review. Source English decisions are recorded only in the source package.'}
for(const m of pkg.curriculum.modules){m.status='ai_draft';for(const u of m.units)u.status='ai_draft'}
const addendum=JSON.parse(readFileSync(join(root,'regulatory-addendum.json')))
for(const s of addendum.sources){
 pkg.provenance.citations.push({id:s.id,title:s.title,url:s.url,sourceType:'regulator',year:2026,note:{en:'Proposed Arabic-edition source-lock amendment; reviewer confirmation pending. Checked 2026-10-07.','ar-AE':'إضافة مقترحة إلى مصادر النسخة العربية؛ بانتظار تأكيد المراجع. تاريخ التحقق 2026-10-07.'}})
 pkg.provenance.sourceLock.allowedSources.push(`DRAFT amendment, review pending: ${s.id} — ${s.url}`)
}
pkg.metadata.arabicEdition.regulatoryAmendmentStatus='pending-human-review'
const lastUnit=pkg.curriculum.modules.at(-1).units.at(-1)
lastUnit.blocks.push({id:'m7-ar-uae-sa-context',type:'action',title:addendum.title,body:addendum.scope,points:addendum.rows.map(r=>({en:`${r.jurisdiction} · ${r.product}: ${r.text.en}`,[locale]:`${r.jurisdictionLabel?.[locale]??r.jurisdiction} · ${r.productLabel?.[locale]??r.product}: ${r.text[locale]}`})),citationRefs:addendum.sources.map(s=>s.id),metadata:{status:'ai_draft',reviewOwner:owner,checkedAt:addendum.checkedAt,sourceLockAmendment:'pending-review'}})
const regionalOverlay=JSON.parse(readFileSync(join(root,'jurisdiction-overlay.json')))
for(const m of pkg.curriculum.modules)for(const u of m.units)for(const b of u.blocks??[]){
 const note=regionalOverlay.blocks[b.id]
 if(!note)continue
 b.metadata??={};b.metadata.variants??={};b.metadata.variants.jurisdiction??={}
 b.metadata.variants.jurisdiction.SA={text:note.text,citationRefs:note.citationRefs}
 b.metadata.regionalReview={country:'SA',topic:note.topic,checkedAt:note.checkedAt,status:note.status}
}
const allBlocks=pkg.curriculum.modules.flatMap(m=>m.units.flatMap(u=>u.blocks))
const incretinAE=allBlocks.find(b=>b.id==='m3-p09').metadata.variants.jurisdiction.AE
allBlocks.find(b=>b.id==='m3-p11').metadata.variants.jurisdiction.AE=structuredClone(incretinAE)
pkg.metadata.arabicEdition.localizationPolicy='course-production/hormones-peptides-skin/arabic-uae-20261007/localization-policy.json'
pkg.tutorCorpus.push({id:'tutor-ar-sa-peptide-status',keys:['الببتيدات السعودية','ببتيدات السعودية','هل الببتيدات ممنوعة','SFDA peptides','Saudi peptide approval'],answer:{en:addendum.rows[0].text.en+' '+addendum.rows[2].text.en,[locale]:addendum.rows[0].text[locale]+' '+addendum.rows[2].text[locale]},citationRefs:['sa-sfda-unregistered-peptides-20260929'],scope:'m07',suggestedPrompt:{en:'Are all peptides prohibited in Saudi Arabia?',[locale]:'هل جميع الببتيدات ممنوعة في السعودية؟'}})
// Narration variants use the existing source scripts and one licensed library voice.
const audio=[]
for(const m of pkg.curriculum.modules)for(const u of m.units)for(const b of u.blocks??[]){
 if(!b.metadata?.audioScript?.[locale])continue
 const id=`${b.id}-narration-ar-AE`
 const a={id,kind:'audio',role:'narration',locale,uri:`assets/hormones-peptides-skin/ar-AE/audio/${b.id}.mp3`,approvalStatus:'draft',generator:{tool:'perceptor-foundry/tools/narration/generate.mjs',model:'eleven_v3',promptRef:`course-production/hormones-peptides-skin/arabic-uae-20261007/narration-scripts.json#${b.id}`}}
 if(existsSync(join(root,'AUDIO-QA.json'))){const q=JSON.parse(readFileSync(join(root,'AUDIO-QA.json'))).segments.find(s=>s.id===b.id);if(q){a.durationSeconds=q.duration;a.checksum='sha256:'+q.sha256}}
 pkg.assets.push(a);b.assetRefs=[...(b.assetRefs??[]),id]
 audio.push({id:b.id,module:m.id,en:b.metadata.audioScript.en,ar:b.metadata.audioScript[locale],uri:a.uri})
}
writeFileSync(join(academyRoot,'packages/hormones-peptides-skin.ar-AE.json'),JSON.stringify(pkg,null,2)+'\n')
writeFileSync(join(root,'narration-scripts.json'),JSON.stringify(audio,null,2)+'\n')
writeFileSync(join(root,'narration-voices.json'),JSON.stringify({[locale]:{voice_id:'ZCXYdzd5Evtsll2EdoCi',name:'Yousef — Calm, Deep and Natural (licensed library; Modern Standard Arabic)',preset:'engaging'}},null,2)+'\n')
const supSource=JSON.parse(readFileSync(join(root,'supplemental-source.json')))
const films=supSource.films.map(f=>({id:f.id,title:translate(f.title.en),script:translate(f.script.en),locale,status:'draft',sourceScript:f.script.en}))
writeFileSync(join(root,'arabic-film-scripts.json'),JSON.stringify(films,null,2)+'\n')
const academy=parse(readFileSync(join(academyRoot,'academy.yaml'),'utf8'));walk(academy)
academy.brand.voices[locale]={voice_id:'ZCXYdzd5Evtsll2EdoCi',name:'Yousef — Modern Standard Arabic (ElevenLabs library)'}
const ae=academy.localization.countries.find(c=>c.code==='AE')
academy.localization.countries=[ae,...academy.localization.countries.filter(c=>c!==ae)]
ae.edition[locale]='العربية — نسخة إماراتية قيد المراجعة'
ae.approval[locale]='المراجعة العربية والطبية: فادي حنّا شمعوني — بانتظار الاعتماد'
academy.localization.countries.push({code:'SA',country:{en:'Saudi Arabia',[locale]:'المملكة العربية السعودية'},centers:[{name:'Saudi Arabia',labels:{en:'Saudi Arabia',[locale]:'المملكة العربية السعودية'}}],edition:{en:'Arabic UAE edition with Saudi supplement',[locale]:'نسخة عربية إماراتية مع ملحق سعودي'},units:{en:'Preserve source units; use local laboratory reference intervals',[locale]:'حفظ وحدات المصدر واستخدام المجالات المرجعية للمختبر المحلي'},approval:{en:'Saudi product checks awaiting Fady review',[locale]:'التحقق من المنتجات السعودية بانتظار مراجعة فادي'},contextLine:{en:'Product-specific SFDA status; no class-wide inference',[locale]:'وضع كل منتج لدى هيئة الغذاء والدواء؛ دون تعميم على الفئة'},status:'blueprint',learning:{locale,language:'العربية',shortLabel:'AR',direction:'rtl',review:{en:'Review pending',[locale]:'المراجعة قيد الانتظار'}}})
// Local review build inputs are separate from the release catalog.
academy.catalog[0].course='packages/hormones-peptides-skin.ar-AE.json'
academy.home.certificate.title[locale]='شهادة إتمام الدورة'
academy.home.certificate.body[locale]='تخضع النسخة العربية للمراجعة قبل إتاحتها للمتعلمين وإصدار شهاداتها.'
academy.home.trust.title[locale]='محتوى يستند إلى الأدلة — النسخة العربية قيد المراجعة'
academy.home.reviewers.forEach(r=>{r.role[locale]='مراجع النسخة العربية: فادي حنّا شمعوني — المراجعة قيد الانتظار'})
writeFileSync(join(root,'academy.ar-AE.review.yaml'),stringify(academy))
// Persist authored overlays; never rewrite approved English authoring files.
mkdirSync(join(root,'authored'),{recursive:true})
for(const m of pkg.curriculum.modules)writeFileSync(join(root,'authored',m.id+'.json'),JSON.stringify(m,null,2)+'\n')
const report={sourceSha256:sha(bytes),sourceVersion:original.version,locale,reviewOwner:owner,localizedFields:localized,sourceLocalizedFields:3797,modules:pkg.curriculum.modules.length,blocks:pkg.curriculum.modules.flatMap(m=>m.units).reduce((n,u)=>n+u.blocks.length,0),narrationScripts:audio.length,filmScripts:films.length,sourcePackageUnchanged:true,releaseReady:false,openGates:['Arabic linguistic and medical review','UAE/Saudi source-lock amendment review','Arabic films and captions','Media preview','Native learner acceptance and publication']}
writeFileSync(join(root,'BUILD-REPORT.json'),JSON.stringify(report,null,2)+'\n')
console.log(JSON.stringify(report))

// Carry forward the verified serving release, whose configuration is ahead of the canonical branch.
await import('./sync-live-baseline.mjs')
