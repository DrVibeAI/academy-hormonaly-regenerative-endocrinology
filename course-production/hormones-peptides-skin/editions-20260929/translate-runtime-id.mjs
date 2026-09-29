#!/usr/bin/env node
// Private machine draft of shared-runtime UI copy; never publishes an Indonesian edition.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs'
import { join, resolve } from 'node:path'
import { homedir } from 'node:os'
import { createHash } from 'node:crypto'

const runtimeDir = process.argv[2] || process.env.PERCEPTOR_RUNTIME_DIR
if (!runtimeDir) throw Error('Pass the runtime checkout path or set PERCEPTOR_RUNTIME_DIR')
const tableFile = join(resolve(runtimeDir), 'tools/i18n/ui-strings.id.json')
const rows = JSON.parse(readFileSync(tableFile))
const key = readFileSync(join(homedir(), '.perceptors', 'gemini_api_key'), 'utf8').trim()
const model = 'gemini-3.7-flash'
const batchDir = join(resolve(runtimeDir), 'tools/i18n/id-batches-retry')
mkdirSync(batchDir, { recursive: true })
const batches = []
let batch = [], size = 0
for (const row of rows.filter(row => !row.translation)) {
  if (batch.length && (batch.length >= 10 || size + row.en.length > 2500)) { batches.push(batch); batch = []; size = 0 }
  batch.push(row); size += row.en.length
}
if (batch.length) batches.push(batch)
const batchFile = i => join(batchDir, `${String(i + 1).padStart(3, '0')}-${createHash('sha256').update(JSON.stringify(batches[i].map(row => [row.id, row.en]))).digest('hex').slice(0, 12)}.json`)
const tokens = s => [...String(s).matchAll(/\$\{[^}]+\}/g)].map(x => x[0]).sort().join('|')
async function translate(batch, attempt = 0) {
  const input = Object.fromEntries(batch.map(row => [row.id, row.en]))
  const body = {
    system_instruction: { parts: [{ text: 'Translate every UI string accurately into natural Bahasa Indonesia for adult healthcare learners. This is generic academy interface copy. Preserve all identifiers, placeholders, numbers, URLs, HTML, punctuation needed for code, and every ${...} expression exactly. For a backtick template, keep both backticks and all JavaScript expressions unchanged; translate only human language. Do not add claims or advice. Return only a JSON object with exactly the supplied keys and translated string values.' }] },
    contents: [{ role: 'user', parts: [{ text: JSON.stringify(input) }] }],
    generationConfig: { temperature: 0.1, responseMimeType: 'application/json' },
  }
  const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, { method: 'POST', headers: { 'content-type': 'application/json', 'x-goog-api-key': key }, body: JSON.stringify(body) })
  const data = await response.json()
  if (!response.ok || data.error) throw Error(`HTTP ${response.status}: ${JSON.stringify(data.error ?? data).slice(0, 250)}`)
  const raw = data.candidates?.[0]?.content?.parts?.filter(p => !p.thought).map(p => p.text ?? '').join('') ?? ''
  const output = JSON.parse(raw)
  const missing = batch.filter(row => typeof output[row.id] !== 'string' || !output[row.id].trim() || tokens(output[row.id]) !== tokens(row.en) || (row.kind === 'template' && (!output[row.id].startsWith('`') || !output[row.id].endsWith('`'))))
  if (missing.length && attempt < 2) Object.assign(output, await translate(missing, attempt + 1))
  return output
}
let cursor = 0, failed = 0
async function worker() {
  while (cursor < batches.length && failed < 4) {
    const i = cursor++
    const file = batchFile(i)
    if (existsSync(file)) continue
    try {
      const result = await translate(batches[i])
      for (const row of batches[i]) {
        if (typeof result[row.id] !== 'string' || tokens(result[row.id]) !== tokens(row.en)) throw Error(`placeholder mismatch ${row.id}`)
      }
      writeFileSync(file, JSON.stringify(result, null, 2) + '\n')
    } catch (e) { failed++; console.error(`batch ${i + 1}: ${e.message}`) }
    console.log(`${cursor}/${batches.length} assigned`)
  }
}
await Promise.all([worker(), worker()])
const merged = Object.assign({}, ...Array.from({ length: batches.length }, (_, i) => batchFile(i)).filter(existsSync).map(file => JSON.parse(readFileSync(file))))
for (const row of rows) if (merged[row.id]) row.translation = merged[row.id]
const missing = rows.filter(row => !row.translation)
writeFileSync(tableFile, JSON.stringify(rows, null, 2) + '\n')
console.log(`${rows.length - missing.length}/${rows.length} translated; missing: ${missing.map(x => x.id).join(', ')}`)
