import {spawn} from 'node:child_process';
import {createWriteStream} from 'node:fs';
import {resolve} from 'node:path';
const root=resolve(import.meta.dirname,'../..');const workspace=resolve(root,'..');let next=4;const results=[];
async function worker(){while(next<=7){const id=`m${String(next++).padStart(2,'0')}`;const log=createWriteStream(`${workspace}/media-${id}.log`);const code=await new Promise(ok=>{const p=spawn(process.execPath,[`${workspace}/foundry/tools/video/morph.mjs`,`${import.meta.dirname}/${id}-opener.ar.json`,'--work',`${workspace}/media/${id}`,'--steps','narrate'],{stdio:['ignore','pipe','pipe']});p.stdout.pipe(log);p.stderr.pipe(log);p.on('exit',ok)});results.push({id,code});console.log(id,code)}}
await Promise.all([worker(),worker()]);if(results.some(r=>r.code!==0))process.exitCode=1;
