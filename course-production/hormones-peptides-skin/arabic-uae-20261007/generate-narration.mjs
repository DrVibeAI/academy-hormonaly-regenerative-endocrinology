import{readFileSync,writeFileSync,existsSync}from'node:fs'
import{dirname,join,resolve}from'node:path'
import{fileURLToPath}from'node:url'
import{spawn,execFileSync}from'node:child_process'
const root=dirname(fileURLToPath(import.meta.url)),academy=resolve(root,'../../..')
execFileSync(process.execPath,[join(root,'prepare-narration.mjs')],{stdio:'inherit'})
const pkg=JSON.parse(readFileSync(join(root,'narration-ready.json')))
const prior=existsSync(join(root,'narration-manifest.json'))?JSON.parse(readFileSync(join(root,'narration-manifest.json'))):{segments:[]}
const jobs=[]
for(const m of pkg.curriculum.modules){
 if(!m.units.some(u=>u.blocks.some(b=>b.assetRefs.length)))continue
 const p={...pkg,curriculum:{...pkg.curriculum,modules:[m]}}
 const input=join(root,`narration-${m.id}.input.json`),manifest=join(root,`narration-${m.id}.manifest.json`)
 writeFileSync(input,JSON.stringify(p));
 if(!existsSync(manifest))writeFileSync(manifest,JSON.stringify({...prior,segments:prior.segments.filter(s=>s.block_id.startsWith(`m${Number(m.id.slice(1))}-`))}))
 jobs.push({id:m.id,input,manifest})
}
let cursor=0;const errors=[]
async function worker(){while(cursor<jobs.length){const j=jobs[cursor++];try{await new Promise((ok,bad)=>{const p=spawn(process.execPath,['/Users/omar/DrVibe/perceptor-foundry/tools/narration/generate.mjs',j.input,'--out',join(academy,'public'),'--voices',join(root,'narration-voices.json'),'--manifest',j.manifest,'--locales','ar-AE'],{stdio:'inherit'});p.on('exit',c=>c===0?ok():bad(Error(j.id+' exit '+c)));p.on('error',bad)})}catch(e){errors.push(e.message)}}}
await Promise.all([worker(),worker(),worker()])
const segments=new Map(prior.segments.map(s=>[s.asset_id,s]))
for(const j of jobs)if(existsSync(j.manifest))for(const s of JSON.parse(readFileSync(j.manifest)).segments)segments.set(s.asset_id,s)
writeFileSync(join(root,'narration-manifest.json'),JSON.stringify({provider:'elevenlabs',model_id:'eleven_v3',package:pkg.id,approval_status:'draft — pending Fady media preview',segments:[...segments.values()]},null,2))
console.log(JSON.stringify({audioSegments:segments.size,errors}));if(errors.length)process.exitCode=1
