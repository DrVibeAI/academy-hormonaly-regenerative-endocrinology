// Local-only refresh: reuse the existing media exports and index; no paid media or embedding generation.
import fs from 'node:fs'
import path from 'node:path'
import {execFileSync} from 'node:child_process'
import {fileURLToPath} from 'node:url'
const root=path.dirname(fileURLToPath(import.meta.url))
const runtime='/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007'
execFileSync(process.execPath,[path.join(root,'prepare-preview.mjs')],{stdio:'inherit'})
for(const file of ['academy.yaml','packages/hormones-peptides-skin.ar-AE.json'])fs.copyFileSync(path.join(root,'preview-inputs',file),path.join(runtime,file))
for(const script of ['academy-config','catalog-summary','editorial-skin','import-package','editing-context','review-context']) {
 const args=['--import','tsx',`scripts/${script}.mts`]
 if(script==='import-package')args.push('packages/hormones-peptides-skin.ar-AE.json')
 execFileSync(process.execPath,args,{cwd:runtime,stdio:'inherit',env:{...process.env,COURSE:'packages/hormones-peptides-skin.ar-AE.json',ACADEMY_DIR:path.join(root,'preview-inputs')}})
}
