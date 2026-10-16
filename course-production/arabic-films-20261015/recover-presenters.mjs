// Read-only provider status recovery; never creates or retries a paid job.
import {readFileSync,writeFileSync,readdirSync,existsSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {homedir} from 'node:os';
import * as hg from '../../../foundry/tools/avatar/heygen.mjs';
const root=resolve(import.meta.dirname,'../../..');
const keyFile=[join(homedir(),'.perceptors/heygen_api_key'),join(homedir(),'.heygen/credentials')].find(existsSync);
const apiKey=process.env.HEYGEN_API_KEY?.trim()||readFileSync(keyFile,'utf8').trim();
const results=[];
for(const module of readdirSync(join(root,'media')).filter(n=>/^m\d\d$/.test(n))){
 const work=join(root,'media',module),dir=join(work,'media');
 const sb=JSON.parse(readFileSync(join(import.meta.dirname,`${module}-opener.ar.json`)));
 const plan=JSON.parse(readFileSync(join(work,'plan.json')));
 for(const f of readdirSync(dir).filter(n=>n.endsWith('.pending.json'))){
  const pending=JSON.parse(readFileSync(join(dir,f))),out=join(dir,f.replace('.pending.json','')),meta=out+'.json';
  if(existsSync(meta)){results.push({module,file:f,status:'downloaded'});continue}
  const s=(await hg.send(hg.videoStatusRequest({videoId:pending.videoId,apiKey}))).data;
  results.push({module,file:f,videoId:pending.videoId,status:s.status,failureCode:s.failure_code});
  writeFileSync(join(dir,f),JSON.stringify({...pending,status:s.status,failureCode:s.failure_code},null,2));
  if(s.status==='completed'){
   const response=await fetch(s.video_url);if(!response.ok)throw Error('Download failed');
   writeFileSync(out,Buffer.from(await response.arrayBuffer()));
   writeFileSync(meta,JSON.stringify({sha:pending.sha,videoId:pending.videoId,look:sb.presenter.look,engine:sb.presenter.engine,resolution:sb.presenter.resolution,slice:plan.presenters.find(p=>p.src===f.replace('.pending.json',''))?.slice,at:new Date().toISOString()},null,2));
  }
 }
}
writeFileSync(join(root,'media/presenter-status.json'),JSON.stringify(results,null,2));
console.log(results.map(({module,file,status,failureCode})=>({module,file,status,failureCode})))
