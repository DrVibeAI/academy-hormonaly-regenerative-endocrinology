import {spawn} from 'node:child_process';
import {readFileSync,existsSync,createWriteStream,writeFileSync} from 'node:fs';
import {resolve,join} from 'node:path';
const root=resolve(import.meta.dirname,'../../..');
const run=(args,cwd,log)=>new Promise((resolve,reject)=>{const f=createWriteStream(log);const p=spawn(args[0],args.slice(1),{cwd,stdio:['ignore','pipe','pipe']});p.stdout.pipe(f);p.stderr.pipe(f);p.on('error',reject);p.on('close',code=>{f.end();resolve(code)})});
const queue=['m01','m02','m03','m04','m05','m06','m07','hype'];
async function worker(){for(let name;name=queue.shift();){
 const work=join(root,'media',name),id=name==='hype'?'hype':name+'-opener',story=join(import.meta.dirname,id+'.ar.json');
 if(existsSync(join(work,'render.log')) && readFileSync(join(work,'render.log'),'utf8').includes('100%  Render complete') && existsSync(join(work,id+'.ar.mp4'))){console.log(name,'render reused');continue}
 const plan=JSON.parse(readFileSync(join(work,'plan.json')));
 const deadline=Date.now()+20*60*1000;
 while(!plan.presenters.every(p=>existsSync(join(work,'media',p.src+'.json')))){
  if(Date.now()>deadline){console.log(name,'waiting for presenter clips');break}
  await new Promise(r=>setTimeout(r,5000));
 }
 if(!plan.presenters.every(p=>existsSync(join(work,'media',p.src+'.json'))))continue;
 for(const [args,log] of [
  [['node','foundry/tools/video/morph.mjs',story,'--work',work,'--media','/Users/omar/.perceptors/media/hormonaly-skin/cinematic/assets','--steps','build','--no-blur'],'rebuild.log'],
  [['node',join(import.meta.dirname,'finalize-project.mjs'),work],'typesetting.log'],
  [['npx','hyperframes','render',join(work,'project'),'--fps','60','--workers','1','--quality','delivery','--output',join(work,id+'.ar.mp4')],'render.log']]){
  const code=await run(args,args[0]==='npx'?join(root,'foundry'):root,join(work,log));
  if(code!==0)throw Error(name+' '+log+' failed with '+code);
 }
 console.log(name,'render complete');
}}
await Promise.all([worker(),worker()]);
