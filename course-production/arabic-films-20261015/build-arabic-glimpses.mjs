// Compose the original three UI demonstrations from actual Arabic runtime captures.
import {writeFileSync} from 'node:fs';
import {resolve,join} from 'node:path';
import {execFileSync} from 'node:child_process';
const dir=resolve(import.meta.dirname,'glimpses');
for(const [name,prefix,durations] of [['trial-or-brochure','trial',[0.5,1.3,1.3,4.416667]],['audit-certificate','audit',[0.5,1.2,1.3,4.416667]],['glow-case','glow',[1.2,4.883333]]]){
 const list=durations.map((d,i)=>`file '${prefix}-${i}.png'\nduration ${d}`).join('\n')+`\nfile '${prefix}-${durations.length-1}.png'\n`;
 const manifest=join(dir,name+'.concat');writeFileSync(manifest,list);
 execFileSync('ffmpeg',['-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',manifest,'-vf','scale=780:1688:flags=lanczos,format=yuv420p','-r','60','-t',String(durations.reduce((a,b)=>a+b,0)),'-c:v','libx264','-preset','fast','-crf','18','-movflags','+faststart',join(dir,name+'.mp4')],{stdio:'inherit'});
}
console.log('Three Arabic activity demonstrations composed from actual UI states.');
