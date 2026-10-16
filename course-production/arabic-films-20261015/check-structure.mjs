import assert from 'node:assert/strict';
import {readFileSync,readdirSync,writeFileSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {createHash} from 'node:crypto';
const dir=import.meta.dirname, source=resolve(dir,'../hormones-peptides-skin/video/cinematic');
const normalize=(value,path='')=>{
 if(Array.isArray(value))return value.map((v,i)=>normalize(v,`${path}/${i}`));
 if(!value||typeof value!=='object')return value;
 return Object.fromEntries(Object.entries(value).filter(([k])=>!(path===''&&['script','voice','localization'].includes(k))&&!(path==='/presenter'&&k==='disclosure')).map(([k,v])=>{const p=path+'/'+k;return [k,typeof v==='string'&&(['title','kicker','label','text','display','sub','tag','on'].includes(k)||(['from','to'].includes(k)&&p.includes('/presenter/')))?'<localized>':normalize(v,p)]}));
};
const reports=[];
for(const file of readdirSync(dir).filter(f=>f.endsWith('.ar.json'))){
 const ar=JSON.parse(readFileSync(join(dir,file))),srcBytes=readFileSync(join(source,file.replace('.ar.json','.storyboard.json'))),en=JSON.parse(srcBytes);
 assert.equal(ar.localization.sourceSha256,createHash('sha256').update(srcBytes).digest('hex'));
 assert.deepEqual(normalize(ar),normalize(en),file+' structure changed');
 assert.equal(ar.script.locale,'ar-AE');assert.match(ar.script.text,/[\u0600-\u06ff]/);
 reports.push({film:ar.id,states:ar.states.length,structure:'identical',status:'draft'});
}
writeFileSync(join(dir,'structure-check.json'),JSON.stringify(reports,null,2)+'\n');console.log(reports);
