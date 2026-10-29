// Translation-only derivative of the verified serving package. Reuse the English draft only
// after source matching; retain the existing UAE/Saudi labels and every source-language value.
import {readFileSync,writeFileSync} from 'node:fs'
import {createHash} from 'node:crypto'
import {createRequire} from 'node:module'
import {dirname,resolve} from 'node:path'
import {fileURLToPath} from 'node:url'
const here=dirname(fileURLToPath(import.meta.url)),root=resolve(process.env.ACADEMY_DIR||resolve(here,'../../..'))
const runtime=resolve(process.argv[2]??resolve(root,'../runtime'))
const {parseDocument}=createRequire(resolve(runtime,'package.json'))('yaml')
const hash=x=>createHash('sha256').update(x).digest('hex')
const parts=p=>p.slice(1).split('/').map(x=>x.replace(/~1/g,'/').replace(/~0/g,'~'))
const get=(x,p)=>parts(p).reduce((o,k)=>o?.[k],x)
const put=(x,p,v)=>{const ks=parts(p),k=ks.pop();ks.reduce((o,k)=>o[k],x)[k]=v}
const read=n=>JSON.parse(readFileSync(resolve(here,'inputs',n),'utf8'))
const bytes=readFileSync(resolve(root,'packages/hormones-peptides-skin.json'))
const overlay=read('course-es-MX-translation-overlay.json')
if(hash(bytes)!==overlay.sourcePackageSha256)throw Error('English source package changed; reconcile before materializing')
let course=JSON.parse(bytes)
for(const f of overlay.fields){
 if(get(course,f.sourcePath)!==f.en||hash(f.en)!==f.sourceTextSha256)throw Error('Translation source changed: '+f.sourcePath)
 put(course,f.targetPath,f['es-MX'])
}
const sidecars=read('tutor-es-MX-unintegrated-sidecars.json')
for(const f of sidecars.entries){
 if(get(course,f.sourcePath)!==f.en||hash(f.en)!==f.sourceHash)throw Error('Tutor source changed: '+f.sourcePath)
 if(f.kind==='tutorKey'){
  const ks=parts(f.sourcePath);ks.pop();const keys=ks.reduce((o,k)=>o[k],course)
  if(!keys.includes(f['es-MX']))keys.push(f['es-MX'])
 }else{
  const ks=parts(f.sourcePath);ks.pop();const unit=ks.reduce((o,k)=>o[k],course)
  unit.metadata??={};unit.metadata.localizedTutorContext={en:f.en,'es-MX':f['es-MX']}
 }
}
// The existing deterministic retriever matches authored keywords. Each translated suggestion must
// reach its own authored answer even when the source keyword set used only an English abbreviation.
for(const topic of course.tutorCorpus){
 const prompt=topic.suggestedPrompt?.['es-MX']
 if(prompt&&!topic.keys.includes(prompt))topic.keys.push(prompt)
 if(topic.id==='tutor-m02-hrt-skin')for(const key of ['terapia hormonal sustitutiva','terapia de reemplazo hormonal'])if(!topic.keys.includes(key))topic.keys.push(key)
}
// Align the reusable English draft's tutor presentation before rebasing onto the full serving source.
const servingBytes=readFileSync(resolve(root,'packages/hormones-peptides-skin.ar-AE.json'))
if(hash(servingBytes)!=='a31221d366bde348bb86658cb25bb03f7f0afbe6fa237d07d32d793c32d8dc8b')throw Error('Serving comparison package changed; reconcile presentation before materializing')
const serving=JSON.parse(servingBytes)
const sentences=(text,locale)=>[...new Intl.Segmenter(locale,{granularity:'sentence'}).segment(text)]
const headings={'Evidence and limits':'Evidencia y límites','Rules by country':'Normas por país','In practice':'En la práctica'}
for(const topic of course.tutorCorpus){
 const current=serving.tutorCorpus.find(t=>t.id===topic.id)
 const english=sentences(topic.answer.en,'en'),spanish=sentences(topic.answer['es-MX'],'es'),used=[]
 if(english.length!==spanish.length)throw Error('Tutor sentence alignment requires review: '+topic.id)
 topic.answer['es-MX']=current.answer.en.split('\n').map(line=>{
  if(!line.trim())return line
  if(line.startsWith('### ')){const title=headings[line.slice(4)];if(!title)throw Error('Unknown serving tutor heading');return '### '+title}
  const clean=line.replace(/^\*\*|\*\*$/g,'').replace(/^- /,'')
  const start=topic.answer.en.indexOf(clean)
  if(start<0)throw Error('Serving tutor contains a substantive change: '+topic.id)
  const indexes=english.flatMap((s,i)=>s.index>=start&&s.index<start+clean.length?[i]:[])
  if(indexes.map(i=>english[i].segment.trim()).join(' ')!==clean)throw Error('Serving tutor span is not sentence-aligned: '+topic.id)
  used.push(...indexes)
  const text=indexes.map(i=>spanish[i].segment.trim()).join(' ')
  return line.startsWith('**')?'**'+text+'**':line.startsWith('- ')?'- '+text:text
 }).join('\n')
 if(used.length!==english.length||new Set(used).size!==english.length)throw Error('Tutor sentence omitted or repeated: '+topic.id)
}
course.metadata.tutorVisuals=structuredClone(serving.metadata.tutorVisuals)
for(const [id,blockId] of Object.entries(course.metadata.tutorVisuals)){
 if(!course.tutorCorpus.some(t=>t.id===id)||!course.curriculum.modules.some(m=>m.units.some(u=>u.blocks.some(b=>b.id===blockId))))throw Error('Tutor visual is outside the original English course')
}
// The serving source is now verified and the owner explicitly requested parity with its
// additions. Rebase additively, without changing the English, Arabic or Sorani source values.
const englishDraft=course
const collect=(value,path='',out=new Map())=>{
 if(Array.isArray(value))value.forEach((v,i)=>collect(v,path+'/'+i,out))
 else if(value&&typeof value==='object'){
  if(typeof value.en==='string')out.set(path,value)
  for(const [key,v] of Object.entries(value))collect(v,path+'/'+key.replace(/~/g,'~0').replace(/\//g,'~1'),out)
 }
 return out
}
const draftMaps=collect(englishDraft),dictionary=new Map([...draftMaps.values()].filter(v=>v['es-MX']).map(v=>[v.en,v['es-MX']]))
const additional=read('serving-added-fields.es-MX.json')
if(additional.sourceSha256!==hash(servingBytes)||additional.fields.length!==88)throw Error('Serving additions must bind to the verified source')
const additionsByPath=new Map(additional.fields.map(f=>[f.sourcePath.slice(0,-3),f]))
course=structuredClone(serving)
let currentFieldCount=0
for(const [path,target] of collect(course)){
 const from=draftMaps.get(path),extra=additionsByPath.get(path)
 let translated
 if(extra){
  if(extra.en!==target.en||hash(extra.en)!==extra.sourceTextSha256)throw Error('Serving addition changed: '+path)
  translated=extra['es-MX']
 }else if(from?.['es-MX']&&(from.en===target.en||/^\/tutorCorpus\/\d+\/answer$/.test(path)))translated=from['es-MX']
 else translated=dictionary.get(target.en)
 if(!translated)throw Error('Missing current-source Spanish translation: '+path)
 target['es-MX']=translated;currentFieldCount++
}
if(currentFieldCount!==3885)throw Error('Unexpected serving text inventory')
for(const topic of course.tutorCorpus){
 const previous=englishDraft.tutorCorpus.find(t=>t.id===topic.id)
 for(const key of [...(previous?.keys??[]),topic.suggestedPrompt?.['es-MX']].filter(Boolean))if(!topic.keys.includes(key))topic.keys.push(key)
 if(topic.id===course.tutorCorpus.at(-1).id)for(const key of ['péptidos sauditas','péptidos en Arabia Saudita','aprobación de péptidos por la SFDA'])if(!topic.keys.includes(key))topic.keys.push(key)
}
const countryKeys={AE:['Emiratos Árabes Unidos','EAU','Abu Dabi','Dubái'],SA:['Arabia Saudita','saudí','saudita']}
for(const country of course.metadata.regionalTutor.countries)for(const key of countryKeys[country.code]??[])if(!country.aliases.includes(key))country.aliases.push(key)
const topicKeys={'peptide-category':['péptido','péptidos'],'research-peptides':['ipamorelina','péptidos de investigación'],'semaglutide':['semaglutida'],'other-products':['tirzepatida','colágeno oral','GHK-Cu tópico','cosmético']}
for(const topic of course.metadata.regionalTutor.topics)for(const key of topicKeys[topic.id]??[])if(!topic.keys.includes(key))topic.keys.push(key)
course.locales.push({locale:'es-MX',name:'Español (México)',direction:'ltr',status:'draft',unitsPolicy:'Preserve every source measurement, interval and jurisdiction; translation only, no country adaptation.',notes:'Spanish translation of the verified serving package, including its existing UAE/Saudi comparison material and Arabic-edition review labels. No Mexico applicability or Spanish approval is inferred. Independent Spanish fidelity reviewer not assigned. Media remain in their source languages.'})
// Spanish has no rendered film slot. Use the existing explicit English-reference mechanism;
// the source's English, Arabic and Sorani media bindings keep their normal precedence.
for(const module of course.curriculum.modules)for(const unit of module.units)for(const block of unit.blocks){
 const refs=(block.assetRefs??[]).map(id=>course.assets.find(a=>a.id===id))
 if(refs.some(a=>a?.kind==='video'&&(a.locale??course.baseLocale)==='en')){
  block.metadata??={};block.metadata.referenceVideoLocale='en'
 }
 const figures={'3 years':'3 años','~15 years':'~15 años','39 RCTs':'39 ECA','23 RCTs':'23 ECA'}
 if(figures[block.stat?.figure]){
  block.metadata??={};block.metadata.statFigureText={en:block.stat.figure,'es-MX':figures[block.stat.figure]}
 }
}
writeFileSync(resolve(root,'packages/hormones-peptides-skin.es-MX.json'),JSON.stringify(course,null,2)+'\n')
const yamlSource=readFileSync(resolve(root,'academy.yaml'),'utf8')
const doc=parseDocument(yamlSource),config=doc.toJS(),insertions=[]
const report={courseFields:currentFieldCount,originalDraftFields:overlay.fields.length,servingAdditionalFields:additional.fields.length,servingSourceSha256:hash(servingBytes),tutorKeywords:0,tutorContexts:0,configApplied:[],configChanged:[],configMissing:[]}
for(const f of sidecars.entries)report[f.kind==='tutorKey'?'tutorKeywords':'tutorContexts']++
for(const f of read('academy-es-MX-translation-overlay.json').fields){
 const translated=f.targetPath==='/deployment/reviewNotice/es-MX'
  ?'Vista previa de traducción al español (México) · revisión de fidelidad lingüística pendiente.'
  :f['es-MX']
 const source=get(config,f.sourcePath)
 if(source===undefined){report.configMissing.push(f.sourcePath);continue}
 if(source!==f.en){report.configChanged.push({path:f.sourcePath,current:source,previous:f.en});continue}
 if(hash(source)!==f.sourceTextSha256)throw Error('Invalid configuration source digest')
 const target=parts(f.targetPath)
 if(doc.hasIn(target)){
  if(doc.getIn(target)!==translated)throw Error('Existing Spanish copy differs: '+f.targetPath)
 }else{
  const node=doc.getIn(parts(f.sourcePath),true),mapping=doc.getIn(parts(f.sourcePath).slice(0,-1),true)
  const pair=mapping.items.find(p=>p.key.value==='en'),start=pair.key.range[0]
  const indent=' '.repeat(start-yamlSource.lastIndexOf('\n',start)-1)
  const offset=node.range[2]
  insertions.push({offset,text:(yamlSource[offset-1]==='\n'?'':'\n')+indent+'es-MX: '+JSON.stringify(translated)+'\n'})
 }
 report.configApplied.push(f.targetPath)
}
// Authorize a local draft preview through the existing owner-controlled locale review list.
const reviewLocales=doc.getIn(['deployment','reviewLocales'])?.toJSON()??[]
if(!reviewLocales.includes('es-MX')){
 const node=doc.getIn(['deployment','reviewLocales'],true)
 if(yamlSource[node.range[1]-1]!==']')throw Error('Reconcile the review locale list formatting')
 insertions.push({offset:node.range[1]-1,text:', es-MX'})
}
let yamlOutput=yamlSource
for(const {offset,text} of insertions.sort((a,b)=>b.offset-a.offset))yamlOutput=yamlOutput.slice(0,offset)+text+yamlOutput.slice(offset)
parseDocument(yamlOutput).toJS() // ensure inserted strings retain valid YAML
writeFileSync(resolve(root,'academy.yaml'),yamlOutput)
writeFileSync(resolve(here,'materialization-report.json'),JSON.stringify(report,null,2)+'\n')
console.log(JSON.stringify({courseFields:report.courseFields,tutorKeywords:report.tutorKeywords,tutorContexts:report.tutorContexts,configApplied:report.configApplied.length,configChanged:report.configChanged,configMissing:report.configMissing},null,2))
