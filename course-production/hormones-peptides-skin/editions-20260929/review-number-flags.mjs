#!/usr/bin/env node
// Second-pass clinical number audit. Findings are review tasks; never auto-edits packages.
import { readFileSync, writeFileSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import { homedir } from 'node:os'
const root=dirname(fileURLToPath(import.meta.url))
const source=JSON.parse(readFileSync(resolve(root,'../../../packages/hormones-peptides-skin.json')))
const flags=JSON.parse(readFileSync(join(root,'QUALITY-FLAGS.json')))
const key=readFileSync(join(homedir(),'.perceptors','gemini_api_key'),'utf8').trim()
const model=process.env.PERCEPTOR_TRANSLATION_MODEL||'gemini-3.7-flash'
const at=(o,p)=>p.split('/').slice(1).reduce((v,k)=>v?.[k],o)
for(const row of flags){
  const file=join(root,'candidates',`${row.partner}.${row.locale}.json`)
  const pkg=JSON.parse(readFileSync(file))
  const items=row.numbers.map(path=>({path,english:at(source,path).en,translation:at(pkg,path)[row.locale]}))
  const chunks=[];let chunk=[],chars=0
  for(const item of items){
    const n=JSON.stringify(item).length
    if(chunk.length&&chars+n>22000){chunks.push(chunk);chunk=[];chars=0}
    chunk.push(item);chars+=n
  }
  if(chunk.length)chunks.push(chunk)
  const findings=[]
  for(const group of chunks){
    const prompt=`You are a clinical localization number auditor. Compare English and target-language (${row.locale}) text in each item. A mechanical checker flagged digit differences. Many are harmless: spelled-out English numbers written as digits, date reordering, decimal comma, thousands separators, and neutralized internal provenance notes. Identify true changes in a clinical statistic, sample size, date, dose, percentage, cited identifier, or quantity. Return JSON object with key "findings": array of objects {path,category,reason,correction}. category must be "harmless", "needs_review", or "real_mismatch". If harmless, correction must be empty. If real_mismatch, provide a complete corrected target-language text preserving all other meaning. Do not invent data or sources.\n${JSON.stringify(group)}`
    const body={contents:[{parts:[{text:prompt}]}],generationConfig:{temperature:0.1,responseMimeType:'application/json'}}
    const res=await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`,{method:'POST',headers:{'content-type':'application/json','x-goog-api-key':key},body:JSON.stringify(body)})
    const data=await res.json()
    if(!res.ok||data.error)throw Error(`${row.locale}: HTTP ${res.status} ${JSON.stringify(data.error||data).slice(0,300)}`)
    const raw=data.candidates?.[0]?.content?.parts?.filter(p=>!p.thought).map(p=>p.text||'').join('')||''
    const parsed=JSON.parse(raw)
    if(!Array.isArray(parsed.findings))throw Error(`${row.locale}: no findings array`)
    findings.push(...parsed.findings)
  }
  const seen=new Set(findings.map(f=>f.path))
  if(row.numbers.some(p=>!seen.has(p)))throw Error(`${row.locale}: incomplete numeric review`)
  writeFileSync(join(root,`NUMERIC-REVIEW.${row.locale}.json`),JSON.stringify({
    locale:row.locale,model,status:'agent-pre-review',sourceFlags:row.numbers.length,findings
  },null,2)+'\n')
  const counts=Object.groupBy(findings,f=>f.category)
  console.log(`${row.locale}: ${findings.length} reviewed; ${counts.real_mismatch?.length||0} mismatches; ${counts.needs_review?.length||0} needs human review`)
}
