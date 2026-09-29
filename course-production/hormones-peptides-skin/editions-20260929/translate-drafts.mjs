#!/usr/bin/env node
// Draft localization only. Keeps the medically approved source package unchanged.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs'
import { resolve, dirname, join } from 'node:path'
import { createHash } from 'node:crypto'
import { homedir } from 'node:os'
import { fileURLToPath } from 'node:url'

const root = dirname(fileURLToPath(import.meta.url))
const sourcePath = resolve(root, '../../../packages/hormones-peptides-skin.json')
const sourceBytes = readFileSync(sourcePath)
const source = JSON.parse(sourceBytes)
const sourceSha256 = createHash('sha256').update(sourceBytes).digest('hex')
const locales = {
  'es-MX': 'Mexican Spanish for licensed clinicians in Mexico',
  'pt-BR': 'Brazilian Portuguese for licensed clinicians in Brazil',
  id: 'Bahasa Indonesia for licensed clinicians in Indonesia',
}
const selected = process.argv.slice(2).filter(x => x in locales)
const targets = selected.length ? selected : Object.keys(locales)
const key = readFileSync(join(homedir(), '.perceptors', 'gemini_api_key'), 'utf8').trim()
const model = process.env.PERCEPTOR_TRANSLATION_MODEL || 'gemini-3.7-flash'
const jobs = []
const seen = new Set()
function walk(v, path='') {
  if (Array.isArray(v)) return v.forEach((x,i) => walk(x, path+'/'+i))
  if (!v || typeof v !== 'object') return
  if (typeof v.en === 'string') {
    const hash = createHash('sha256').update(v.en).digest('hex')
    jobs.push({ path, hash, source: v.en })
    seen.add(hash)
  }
  for (const [k,x] of Object.entries(v)) walk(x, path+'/'+k)
}
walk(source)
const unique = [...new Map(jobs.map(j => [j.hash, {hash:j.hash, source:j.source}])).values()]
const batches = []
let batch=[], chars=0
for (const j of unique) {
  if (batch.length && (batch.length >= 42 || chars+j.source.length > 7000)) {
    batches.push(batch); batch=[]; chars=0
  }
  batch.push(j); chars += j.source.length
}
if (batch.length) batches.push(batch)
mkdirSync(root, { recursive:true })
writeFileSync(join(root,'source-map.json'), JSON.stringify({
  sourcePackage: sourcePath, sourceSha256, sourceVersion:source.version,
  generatedAt:'2026-09-29', maps:jobs.map(({path,hash}) => ({path,hash}))
}, null, 2)+'\n')
const system = `You are a clinical course localization editor. Return only a JSON object keyed by the supplied SHA256 IDs.
Translate every value accurately and naturally into the requested language for licensed clinicians.
Preserve all numbers, units, citations, evidence grades, safety cautions, uncertainty, limitations, drug names, product names, named authorities, URLs, markup, placeholders and structure.
Do not add or remove clinical claims. Do not turn a US, UK, EU, Brazil or UAE regulatory statement into local law. Keep the named source jurisdiction explicit.
Do not invent an approval, a product registration, a dosing instruction, a citation or a medical recommendation.
Keep register labels such as mechanism, human evidence, regulatory status and uncertainty distinct.
Preserve literal identifiers, angle-bracket placeholders and bracketed reference tokens.
Translate the full text, including quoted patient dialogue, and use locale-native punctuation and terminology.
If a phrase is ambiguous, translate conservatively without increasing certainty.`
async function call(locale, batch, attempt=0) {
  const input = Object.fromEntries(batch.map(j => [j.hash,j.source]))
  const body = {
    system_instruction:{parts:[{text:system}]},
    contents:[{role:'user',parts:[{text:`Target: ${locales[locale]}. Translate this JSON. Return exactly these keys and string values.\n${JSON.stringify(input)}`}]}],
    generationConfig:{temperature:0.1,responseMimeType:'application/json'},
  }
  const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`,{
    method:'POST', headers:{'content-type':'application/json','x-goog-api-key':key},body:JSON.stringify(body)
  })
  const data = await response.json()
  if (!response.ok || data.error) throw new Error(`HTTP ${response.status}: ${JSON.stringify(data.error || data).slice(0,350)}`)
  const raw = data.candidates?.[0]?.content?.parts?.filter(p=>!p.thought).map(p=>p.text||'').join('') || ''
  let parsed
  try { parsed=JSON.parse(raw) } catch { throw new Error(`Non-JSON response: ${raw.slice(0,120)}`) }
  const missing=batch.filter(j=>typeof parsed[j.hash]!=='string' || !parsed[j.hash].trim())
  if (missing.length && attempt<2) {
    const retry=await call(locale,missing,attempt+1)
    parsed={...parsed,...retry}
  }
  return parsed
}
async function run(locale) {
  const dir=join(root,'batches',locale);mkdirSync(dir,{recursive:true})
  let failed=0, cursor=0, completed=0
  async function worker() {
  while(cursor<batches.length && failed<8) {
    const i=cursor++
    const file=join(dir,`${String(i+1).padStart(3,'0')}.json`)
    if(existsSync(file)) continue
    try {
      const translated=await call(locale,batches[i])
      const wanted=batches[i].map(x=>x.hash)
      const present=Object.fromEntries(wanted.filter(h=>typeof translated[h]==='string' && translated[h].trim()).map(h=>[h,translated[h]]))
      if(Object.keys(present).length!==wanted.length) throw new Error(`Only ${Object.keys(present).length}/${wanted.length} strings returned`)
      writeFileSync(file,JSON.stringify(present,null,2)+'\n')
    } catch(e) {
      failed++
      console.error(`${locale} batch ${i+1}/${batches.length}: ${e.message}`)
      await new Promise(r=>setTimeout(r,1500*failed))
    }
    completed++
    if(completed%10===0) console.log(`${locale}: ${completed} new batches, ${cursor}/${batches.length} assigned`)
  }
  }
  await Promise.all([worker(),worker()])
}
console.log(`Source ${sourceSha256.slice(0,12)}: ${jobs.length} paths, ${unique.length} unique strings, ${batches.length} batches/locale`)
await Promise.all(targets.map(run))
for(const locale of targets) {
  const dir=join(root,'batches',locale)
  const fs=await import('node:fs')
  const files=fs.readdirSync(dir).filter(f=>f.endsWith('.json'))
  const merged=Object.assign({},...files.map(f=>JSON.parse(readFileSync(join(dir,f)))))
  const missing=unique.filter(j=>!merged[j.hash]).map(j=>j.hash)
  writeFileSync(join(root,`${locale}.draft.json`),JSON.stringify({
    locale,model,sourceSha256,sourceVersion:source.version,status:'machine-draft-unreviewed',
    totalStrings:unique.length,translatedStrings:Object.keys(merged).length,missingHashes:missing,translations:merged
  },null,2)+'\n')
  console.log(`${locale}: ${Object.keys(merged).length}/${unique.length} strings`)
}
