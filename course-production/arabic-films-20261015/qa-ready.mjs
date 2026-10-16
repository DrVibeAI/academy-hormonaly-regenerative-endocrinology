import {spawn} from 'node:child_process';
import {readFileSync,existsSync,createWriteStream,writeFileSync} from 'node:fs';
import {resolve,join} from 'node:path';
const root=resolve(import.meta.dirname,'../../..');
const queue=['m01','m02','m03','m04','m05','m06','m07','hype'];
const ready=w=>existsSync(join(w,'render.log')) && /Render complete|Rendered|Successfully rendered|Output:/.test(readFileSync(join(w,'render.log'),'utf8'));
async function worker(){for(let name;name=queue.shift();){
 const work=join(root,'media',name),id=name==='hype'?'hype':name+'-opener';
 if(existsSync(join(work,'video-qa.json'))){console.log(name,'QA report reused');continue}
 const deadline=Date.now()+60*60*1000;
 while(!ready(work)){if(Date.now()>deadline)throw Error('Render timeout '+name);await new Promise(r=>setTimeout(r,10000));}
 const story=JSON.parse(readFileSync(join(import.meta.dirname,id+'.ar.json')));
 writeFileSync(join(work,'narration.txt'),story.script.text);
 const log=createWriteStream(join(work,'video-qa.log'));
 const code=await new Promise((done,reject)=>{const p=spawn('node',['bin/perceptor.mjs','qa','--files',join(work,id+'.ar.mp4'),'--video','--locale-hint','ar-AE','--model','gemini-3.8-flash','--narration',join(work,'narration.txt'),'--vtt',join(work,'captions.ar.vtt'),'--report',join(work,'video-qa.json')],{cwd:join(root,'foundry'),stdio:['ignore','pipe','pipe']});p.stdout.pipe(log);p.stderr.pipe(log);p.on('error',reject);p.on('close',done)});
 log.end();console.log(name,'QA complete',code);
}}
await Promise.all([worker(),worker()]);
