#!/usr/bin/env node
// Generate partner-neutral wording for the translated presentation strings.
import { readFileSync, writeFileSync } from 'node:fs'
import { join, dirname } from 'node:path'
import { createHash } from 'node:crypto'
import { homedir } from 'node:os'
import { fileURLToPath } from 'node:url'
const root=dirname(fileURLToPath(import.meta.url))
const contract=JSON.parse(readFileSync(join(root,'GENERIC-NEUTRALIZATION.json')))
const key=readFileSync(join(homedir(),'.perceptors','gemini_api_key'),'utf8').trim()
const model=process.env.PERCEPTOR_TRANSLATION_MODEL||'gemini-3.7-flash'
const localeNames={'es-MX':'Mexican Spanish','pt-BR':'Brazilian Portuguese',id:'Bahasa Indonesia'}
for(const [locale,name] of Object.entries(localeNames)){
  const draft=JSON.parse(readFileSync(join(root,`${locale}.draft.json`)))
  if(draft.sourceSha256!==contract.sourceSha256)throw Error('Source/neutralization SHA mismatch')
  const entries=contract.entries.filter(e=>e.path.endsWith('/en')).map(e=>({
    path:e.path,sourceEnglish:e.from,neutralEnglish:e.to,
    currentTranslation:draft.translations[createHash('sha256').update(e.from).digest('hex')]
  }))
  if(entries.some(e=>typeof e.currentTranslation!=='string'))throw Error(`${locale}: missing original translation`)
  const prompt=`You are adapting a clinician course from its original Hormonaly-branded wording into a partner-neutral presentation. The original book titles and named authors remain in citations; generic learner text must say "the reference guide" or "both reference guides" where the revised English does. Target language: ${name}.
For every item, rewrite currentTranslation to match the meaning and attribution of neutralEnglish. Preserve all numbers, evidence grades, citations, safety caveats, clinical uncertainty, and other wording. Do not add or alter a medical or regulatory claim. Return JSON mapping each exact path to one complete revised string.\n${JSON.stringify(entries)}`
  const body={contents:[{parts:[{text:prompt}]}],generationConfig:{temperature:0.1,responseMimeType:'application/json'}}
  const res=await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`,{method:'POST',headers:{'content-type':'application/json','x-goog-api-key':key},body:JSON.stringify(body)})
  const data=await res.json()
  if(!res.ok||data.error)throw Error(`${locale}: HTTP ${res.status} ${JSON.stringify(data.error||data).slice(0,300)}`)
  const raw=data.candidates?.[0]?.content?.parts?.filter(p=>!p.thought).map(p=>p.text||'').join('')||''
  const result=JSON.parse(raw)
  const missing=entries.filter(e=>typeof result[e.path]!=='string'||!result[e.path].trim())
  if(missing.length)throw Error(`${locale}: ${missing.length} missing neutralization edits`)
  writeFileSync(join(root,`NEUTRALIZATION.${locale}.draft.json`),JSON.stringify({
    locale,sourceSha256:contract.sourceSha256,model,status:'machine-draft-unreviewed',
    edits:Object.fromEntries(entries.map(e=>[e.path,result[e.path]]))
  },null,2)+'\n')
  console.log(`${locale}: ${entries.length} neutralized translated strings`)
}
