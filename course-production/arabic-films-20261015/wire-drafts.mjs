/** Register local Arabic film drafts. Does not approve, upload or deploy media. */
import {readFileSync,writeFileSync,mkdirSync,copyFileSync,existsSync} from 'node:fs';
import {resolve,join,dirname} from 'node:path';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import YAML from '../../../runtime/node_modules/yaml/dist/index.js';
const academy=resolve(import.meta.dirname,'../..'),root=resolve(academy,'..');
const names=['m01','m02','m03','m04','m05','m06','m07','hype'];
for(const name of names){const work=join(root,'media',name);if(!existsSync(join(work,'render.log'))||!readFileSync(join(work,'render.log'),'utf8').includes('100%  Render complete'))throw Error('Unfinished render '+name);const plan=JSON.parse(readFileSync(join(work,'plan.json')));if(!plan.presenters.every(p=>existsSync(join(work,'media',p.src+'.json'))))throw Error('Incomplete presenter '+name);}
const pkgPath=join(academy,'packages/hormones-peptides-skin.ar-AE.json');
const pkg=JSON.parse(readFileSync(pkgPath));
const blocks=pkg.curriculum.modules.flatMap(m=>m.units.flatMap(u=>u.blocks));
const manifest={createdAt:new Date().toISOString(),approvalStatus:'draft',published:false,films:[]};
const sha=f=>'sha256:'+createHash('sha256').update(readFileSync(f)).digest('hex');
for(const name of names){
 const id=name==='hype'?'hype':name+'-opener',work=join(root,'media',name),story=JSON.parse(readFileSync(join(import.meta.dirname,id+'.ar.json')));
 const uri=`assets/hormones-peptides-skin/ar-AE/video/${id}.mp4`,file=join(academy,'public',uri);mkdirSync(dirname(file),{recursive:true});
 execFileSync('ffmpeg',['-hide_banner','-loglevel','error','-y','-i',join(work,id+'.ar.mp4'),'-c','copy','-movflags','+faststart',file],{stdio:'inherit'});
 const posterUri=uri.replace('.mp4','-poster.jpg'),captionUri=uri.replace('.mp4','.vtt');
 execFileSync('ffmpeg',['-hide_banner','-loglevel','error','-y','-ss','2','-i',file,'-frames:v','1','-q:v','2',join(academy,'public',posterUri)]);
 copyFileSync(join(work,'captions.ar.vtt'),join(academy,'public',captionUri));
 const duration=Number(execFileSync('ffprobe',['-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',file],{encoding:'utf8'}).trim());
 const base=`asset-hps-${id}-ar`,block=name==='hype'?null:blocks.find(b=>b.id===`m${Number(name.slice(1))}-opener`);
 const common={locale:'ar-AE',approvalStatus:'draft',generator:{tool:'perceptor-foundry/tools/video/morph.mjs',model:'HeyGen Avatar V licensed Iris · ElevenLabs v3 Yousef · HyperFrames 0.8.162',promptRef:`course-production/arabic-films-20261015/${id}.ar.json`},metadata:{...(block?{block:block.id}:{}),mediaPreview:'Draft — awaiting human Arabic media review',structure:'Same states, source assets, presenter look and interactions as the original English film; Arabic text, narration and word timing.'}};
 const assets=[{...common,id:base,kind:'video',role:name==='hype'?'course-trailer':'module-opener',uri,durationSeconds:duration,checksum:sha(file),disclosure:story.presenter.disclosure},{...common,id:base+'-poster',kind:'image',role:'poster',uri:posterUri,checksum:sha(join(academy,'public',posterUri))},{...common,id:base+'-captions',kind:'captions',role:'caption-track',uri:captionUri,checksum:sha(join(academy,'public',captionUri))}];
 for(const a of assets){const i=pkg.assets.findIndex(x=>x.id===a.id);if(i<0)pkg.assets.push(a);else pkg.assets[i]=a;}
 if(block){block.assetRefs=[...new Set([...block.assetRefs,...assets.map(a=>a.id)])];block.title['ar-AE']=block.title['ar-AE'].replace(/^الفيلم الأصلي بالإنجليزية — النسخة العربية قيد الإنتاج: /,'');delete block.metadata.referenceVideoLocale;delete block.metadata.videoBadge;block.metadata.videoTranscript['ar-AE']=story.script.text;}
 manifest.films.push({id,uri,posterUri,captionUri,durationSeconds:duration,checksum:sha(file),sourceRender:join('media',name,id+'.ar.mp4'),assetIds:assets.map(a=>a.id)});
 console.log(id,'draft registered',duration.toFixed(2)+'s');
}
writeFileSync(pkgPath,JSON.stringify(pkg,null,2)+'\n');
const yamlPath=join(academy,'academy.yaml'),doc=YAML.parseDocument(readFileSync(yamlPath,'utf8'));
const trailer=manifest.films.find(f=>f.id==='hype');
doc.setIn(['home','heroVideo','srcByLocale'],{en:doc.getIn(['home','heroVideo','src']),'ar-AE':trailer.uri});
doc.setIn(['home','heroVideo','posterByLocale'],{en:doc.getIn(['home','heroVideo','poster']),'ar-AE':trailer.posterUri});
doc.setIn(['home','heroVideo','captionsByLocale'],{ar:{src:trailer.captionUri,language:'ar',label:'العربية'}});
doc.setIn(['home','heroVideo','disclosure','ar-AE'],'يُقدَّم عبر مجسّد رقمي (مقدّم وصوت مُنشآن بالذكاء الاصطناعي).');
writeFileSync(yamlPath,String(doc));
writeFileSync(join(import.meta.dirname,'draft-media-manifest.json'),JSON.stringify(manifest,null,2)+'\n');
const capturesPath=join(academy,'presentation-inputs/home-glimpses-bilingual.json');
const captures=JSON.parse(readFileSync(capturesPath));
captures.packageSha256=sha(pkgPath).replace('sha256:','');
captures.sourceRuntimeCommit=execFileSync('git',['rev-parse','HEAD'],{cwd:join(root,'runtime'),encoding:'utf8'}).trim();
delete captures.workingTreeChanges;
writeFileSync(capturesPath,JSON.stringify(captures,null,2)+'\n');
console.log('Capture provenance updated for the package media additions.');
