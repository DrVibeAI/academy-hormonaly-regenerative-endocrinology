#!/usr/bin/env node
import { readFileSync, writeFileSync } from 'node:fs'
import { join, resolve } from 'node:path'
const runtimeDir = process.argv[2] || process.env.PERCEPTOR_RUNTIME_DIR
if (!runtimeDir) throw Error('Pass the runtime checkout path or set PERCEPTOR_RUNTIME_DIR')
const file = join(resolve(runtimeDir), 'tools/i18n/ui-strings.id.json')
const rows = JSON.parse(readFileSync(file))
const values = {
  ea6f1c8: 'Panduan ini bersifat edukatif: saya tidak dapat membuat diagnosis, menetapkan dosis, atau mengubah obat Anda. Keputusan tersebut perlu dibuat bersama dokter yang mengetahui kondisi Anda. Saya dapat membantu Anda merumuskan pertanyaan untuk konsultasi berikutnya.',
  '2c89cb0': 'Batas klinis · kondisi pribadi',
  f1226d3: 'edisi tersedia',
  b9feff2: 'menunggu',
  f3adfd3: 'edisi dalam persiapan',
  fe3cb52: 'Tautan tersebut sudah digunakan atau kedaluwarsa. Minta tautan baru dan buka langsung dari email Anda.',
  '46caebc': 'Alamat email tidak cocok dengan tautan. Masukkan alamat tujuan pengiriman email.',
  ddcee94: 'Domain ini belum diizinkan untuk masuk. Hubungi tim Akademi.',
  ebade7b: 'Diterbitkan pada',
  a603b45: 'VERIFIKASI',
  b1eb5f2: 'Akreditasi GCLS',
  '95ebd3e': 'Penerbit · diverifikasi oleh Perceptors',
  '6ed322a': 'Pindai untuk verifikasi',
}
for (const row of rows) {
  if (values[row.id]) row.translation = values[row.id]
  if (row.id === '2bc47b9') row.translation = row.translation.replace("'my context'", "'konteks saya'").replace(' around ', ' terkait ')
  if (row.id === '3dcb2a3') row.translation = row.en.replace('Use “${learnerNote}” as this week’s example.', 'Gunakan “${learnerNote}” sebagai contoh minggu ini.').replace('Choose a real situation from your week and apply only this criterion.', 'Pilih situasi nyata dari minggu ini dan terapkan hanya kriteria ini.').replace(' Source: ', ' Sumber: ')
  if (row.id === '19901a0') row.translation = '`Proses masuk gagal (${code}). Minta tautan baru.`'
  if (row.id === '31b53d4') row.translation = row.en.replace('Completed ', 'Menyelesaikan ').replace(' of ', ' dari ').replace(' modules', ' modul').replace(' and passed the final check with ', ' dan lulus ujian akhir dengan nilai ')
  if (row.id === 'acab970') row.translation = '`Penerbit akreditasi · merek bersama ${academy.name} · diverifikasi oleh Perceptors`'
}
const missing = rows.filter(row => !row.translation)
if (missing.length) throw Error(`Still missing: ${missing.map(row => row.id).join(', ')}`)
writeFileSync(file, JSON.stringify(rows, null, 2) + '\n')
console.log(`${rows.length} Indonesian UI rows filled`)
