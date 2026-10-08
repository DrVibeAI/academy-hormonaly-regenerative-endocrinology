import{readFileSync,writeFileSync,readdirSync,existsSync}from'node:fs'
import{dirname,join,resolve}from'node:path'
import{fileURLToPath}from'node:url'
import{createHash}from'node:crypto'
const root=dirname(fileURLToPath(import.meta.url)),academy=resolve(root,'../../..'),locale='ar-AE'
const pkg=JSON.parse(readFileSync(join(academy,'packages/hormones-peptides-skin.json')))
const translations=Object.assign({},...readdirSync(join(root,'batches',locale)).filter(x=>x.endsWith('.json')).map(x=>JSON.parse(readFileSync(join(root,'batches',locale,x)))))
if(existsSync(join(root,'corrections.json')))Object.assign(translations,JSON.parse(readFileSync(join(root,'corrections.json'))))
const sha=s=>createHash('sha256').update(s).digest('hex')
const nums=s=>(s.match(/\d+(?:[.,]\d+)?/g)??[]).sort().join('|')
const equivalents=existsSync(join(root,'numeric-equivalences.json'))?JSON.parse(readFileSync(join(root,'numeric-equivalences.json'))):{}
const scripts=[];const blocked=[]
pkg.assets=[]
for(const m of pkg.curriculum.modules)for(const u of m.units)for(const b of u.blocks??[]){
 b.assetRefs=[]
 const en=b.metadata?.audioScript?.en;if(!en)continue
 const ar=translations[sha(en)];if(!ar)continue
 if(nums(en)!==nums(ar)&&!equivalents[b.id]){blocked.push(b.id);continue}
 b.metadata.audioScript[locale]=ar
 const id=b.id+'-narration-ar-AE',uri=`assets/hormones-peptides-skin/ar-AE/audio/${b.id}.mp3`
 pkg.assets.push({id,kind:'audio',role:'narration',locale,uri,approvalStatus:'draft'})
 b.assetRefs=[id];scripts.push({id:b.id,module:m.id,en,ar})
}
writeFileSync(join(root,'narration-ready.json'),JSON.stringify(pkg,null,2))
writeFileSync(join(root,'narration-voices.json'),JSON.stringify({[locale]:{voice_id:'ZCXYdzd5Evtsll2EdoCi',name:'Yousef — Calm, Deep and Natural (licensed library)',preset:'engaging'}},null,2))
writeFileSync(join(root,'narration-ready-scripts.json'),JSON.stringify(scripts,null,2))
console.log(JSON.stringify({ready:scripts.length,total:48,blockedNumeric:blocked}))
