#!/usr/bin/env node
// Materialize private partner review candidates. Never changes the owner package or any live academy.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { dirname, resolve, join } from 'node:path'
import { createHash } from 'node:crypto'
import { fileURLToPath } from 'node:url'
const root=dirname(fileURLToPath(import.meta.url))
const sourceFile=resolve(root,'../../../packages/hormones-peptides-skin.json')
const sourceBytes=readFileSync(sourceFile)
const sourceSha256=createHash('sha256').update(sourceBytes).digest('hex')
const source=JSON.parse(sourceBytes)
const outDir=join(root,'candidates');mkdirSync(outDir,{recursive:true})
const neutralContract=JSON.parse(readFileSync(join(root,'GENERIC-NEUTRALIZATION.json')))
const specs=[
  {key:'cenegenics',locale:'es-MX',name:'Cenegenics',country:'MX',countryName:'Mexico',authority:'COFEPRIS',authorityUrl:'https://www.gob.mx/cofepris/articulos/cofepris-presenta-visor-de-registros-sanitarios-de-medicamentos',accent:'#116E72',units:'SI units and Mexican laboratory reference intervals; report source-study units without silent conversion'},
  {key:'biolongeva',locale:'pt-BR',name:'Biolongeva',country:'BR',countryName:'Brazil',authority:'ANVISA',authorityUrl:'https://www.gov.br/anvisa/pt-br/sistemas/consulta-a-registro',accent:'#414141',units:'SI units and Brazilian laboratory reference intervals; report source-study units without silent conversion'},
  {key:'parallaxnet-skin',locale:'id',name:'Parallaxnet Healthcare',country:'ID',countryName:'Indonesia',authority:'BPOM',authorityUrl:'https://cekbpom.pom.go.id/',accent:'#414141',units:'SI units and Indonesian laboratory reference intervals; report source-study units without silent conversion'},
]
const clone=x=>structuredClone(x)
const pointer=(obj,path)=>path.split('/').slice(1).reduce((v,k)=>v?.[k],obj)
const setPointer=(obj,path,value)=>{
  const parts=path.split('/').slice(1),last=parts.pop()
  const parent=parts.reduce((v,k)=>v[k],obj)
  parent[last]=value
}
function eachMap(v,fn,path=''){
  if(Array.isArray(v))return v.forEach((x,i)=>eachMap(x,fn,path+'/'+i))
  if(!v||typeof v!=='object')return
  if(typeof v.en==='string')fn(v,path)
  for(const [k,x] of Object.entries(v))eachMap(x,fn,path+'/'+k)
}
const reports=[]
for(const s of specs){
  const translation=JSON.parse(readFileSync(join(root,`${s.locale}.draft.json`)))
  if(translation.sourceSha256!==sourceSha256)throw Error(`${s.locale}: source hash changed`)
  if(translation.missingHashes.length)throw Error(`${s.locale}: ${translation.missingHashes.length} missing translations`)
  const pkg=clone(source)
  let count=0;const identical=[]
  eachMap(pkg,(map,path)=>{
    const hash=createHash('sha256').update(map.en).digest('hex')
    const value=translation.translations[hash]
    if(typeof value!=='string'||!value.trim())throw Error(`${s.locale}: missing ${path}`)
    map[s.locale]=value
    count++
    if(value===map.en && map.en.split(/\s+/).length>3)identical.push(path)
  })
  const neutral=JSON.parse(readFileSync(join(root,`NEUTRALIZATION.${s.locale}.draft.json`)))
  if(neutral.sourceSha256!==sourceSha256||neutralContract.sourceSha256!==sourceSha256)throw Error('Neutralization source mismatch')
  for(const edit of neutralContract.entries){
    if(pointer(pkg,edit.path)!==edit.from)throw Error(`Neutralization drift at ${edit.path}`)
    setPointer(pkg,edit.path,edit.to)
    if(edit.path.endsWith('/en')){
      const target=neutral.edits[edit.path]
      if(typeof target!=='string'||!target.trim())throw Error(`Missing neutralized ${s.locale} ${edit.path}`)
      setPointer(pkg,edit.path.slice(0,-2)+s.locale,target)
    }
  }
  pkg.id=`${s.key}.hormones-peptides-skin`
  pkg.version='1.1.0-localization-draft.1'
  pkg.academy.id=s.key
  pkg.academy.name=s.name
  pkg.academy.brand={displayName:s.name,accentColor:s.accent,brandOwner:s.name}
  pkg.academy.client={organization:s.name,productContext:`Private ${s.countryName} localization candidate of the Hormonaly source course; distribution rights pending`}
  const summaries={
    'es-MX':'Curso clínico sobre la fisiología endocrina de la piel, la evidencia sobre péptidos y tratamientos relacionados, la seguridad y la evaluación crítica de afirmaciones. La revisión regulatoria específica para México sigue pendiente.',
    'pt-BR':'Curso clínico sobre a fisiologia endócrina da pele, as evidências sobre peptídeos e tratamentos relacionados, a segurança e a avaliação crítica de alegações. A revisão regulatória específica para o Brasil segue pendente.',
    id:'Kursus klinis tentang fisiologi endokrin kulit, bukti mengenai peptida dan terapi terkait, keselamatan, serta penilaian kritis atas klaim. Telaah regulasi khusus Indonesia masih berlangsung.'
  }
  pkg.summary={en:`Clinical course on skin endocrine physiology, evidence for peptides and related therapies, safety and critical appraisal of claims. ${s.countryName}-specific regulatory review is pending.`,[s.locale]:summaries[s.locale]}
  const localNotices={
    'es-MX':'El contenido original explica normas de Estados Unidos y de otros países como ejemplos comparativos. El registro, la indicación, la vía de administración y las reglas profesionales aplicables en México deben verificarse con COFEPRIS y revisarse localmente antes de tomar decisiones clínicas.',
    'pt-BR':'O conteúdo original explica regras dos Estados Unidos e de outros países como exemplos comparativos. O registro, a indicação, a via de administração e as regras profissionais aplicáveis no Brasil devem ser conferidos na Anvisa e revisados localmente antes de decisões clínicas.',
    id:'Materi sumber menjelaskan aturan Amerika Serikat dan negara lain sebagai perbandingan. Status izin edar, indikasi, rute pemberian, dan aturan profesi di Indonesia harus diperiksa melalui BPOM serta ditinjau secara lokal sebelum keputusan klinis dibuat.'
  }
  pkg.audience.disclaimers[1]={en:`The source explains US and other countries' rules as comparisons. ${s.countryName} product registration, indication, route and professional-practice status require current checks with ${s.authority} and local review before clinical use.`,[s.locale]:localNotices[s.locale]}
  pkg.locales=[
    {...source.locales[0],reviewOwner:'Source course reviewer of record'},
    {locale:s.locale,name:s.locale==='es-MX'?'Español (México)':s.locale==='pt-BR'?'Português (Brasil)':'Bahasa Indonesia',direction:'ltr',status:'draft',reviewOwner:'Pending named local clinical and language reviewers',unitsPolicy:s.units,notes:'Complete machine draft; clinical, regulatory, language, media and partner reviews pending.'}
  ]
  pkg.jurisdictions=[{
    code:s.country,name:s.countryName,
    authorities:[{name:s.authority,scope:'Medicine/cosmetic product status, authorized indication, route and claims; exact-product checks pending',url:s.authorityUrl}],
    layers:['product','claims','practice','locale'].map(id=>({id,status:'review',detail:`${s.countryName} adaptation pending exact-product/source checks and named local reviewer; source-country status does not transfer.`})) ,
    reviewOwner:'Pending named local clinical and regulatory reviewer'
  }]
  for(const module of pkg.curriculum.modules){
    module.status='ai_draft'
    for(const unit of module.units)unit.status='ai_draft'
  }
  for(const asset of pkg.assets)asset.approvalStatus='draft'
  pkg.governance.requiredGates=['medical_review','regulatory_review','brand_approval','localization_review','gcls_accreditation','publish']
  pkg.governance.approvals=[]
  pkg.governance.accreditation={body:'GCLS',status:'not_submitted',notes:'Source-course decisions do not transfer to this partner derivative. Partner credential terms and review are pending.'}
  pkg.credential.type='completion'
  pkg.credential.title={en:'Course completion · Hormones and Peptides for Skin',[s.locale]:s.locale==='es-MX'?'Constancia de finalización · Hormonas y péptidos para la piel':s.locale==='pt-BR'?'Comprovante de conclusão · Hormônios e peptídeos para a pele':'Bukti penyelesaian · Hormon dan peptida untuk kulit'}
  delete pkg.credential.issuer
  pkg.credential.coBrand={displayName:s.name,accentColor:s.accent}
  pkg.credential.sharing={linkedin:false,nativeShare:false,directoryOptIn:false}
  pkg.distribution={targets:[{platform:'academy-app',notes:`Draft partner adaptation for ${s.name}; do not deploy or expose before rights, regional review and publication gates.`}]}
  pkg.metadata={...pkg.metadata,sourcePackage:{id:source.id,version:source.version,sha256:sourceSha256,owner:'Hormonaly.ai / Hormonaly Press'},localizationStatus:'machine-draft-unreviewed',pendingReview:[
    'Partner distribution rights and brand/claims agreement',
    'Country-specific medicine/cosmetic/compounding claims and profession scope',
    'Native clinician and language review of all translated content, assessments and tutor answers',
    'Localized media, captions, transcripts and runtime UI',
    'Separate accreditation and publication decisions'
  ]}
  const file=join(outDir,`${s.key}.${s.locale}.json`)
  writeFileSync(file,JSON.stringify(pkg,null,2)+'\n')
  reports.push({partner:s.name,locale:s.locale,sourceSha256,translatedPaths:count,neutralizedEdits:neutralContract.entries.length,identicalLongStrings:identical,package:file,status:'draft',publishReady:false})
}
writeFileSync(join(root,'QUALITY-SUMMARY.json'),JSON.stringify(reports,null,2)+'\n')
console.log(JSON.stringify(reports.map(r=>({partner:r.partner,locale:r.locale,translatedPaths:r.translatedPaths,identicalLongStrings:r.identicalLongStrings.length,publishReady:false}))))
