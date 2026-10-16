import {readFileSync,writeFileSync,readdirSync,copyFileSync,existsSync} from 'node:fs';
import {resolve,join} from 'node:path';
const work=resolve(process.argv[2]),fonts=resolve(work,'../fonts'),project=join(work,'project');
const glimpses=resolve(import.meta.dirname,'glimpses');
if(work.endsWith('/hype')) for(const name of ['trial-or-brochure','audit-certificate','glow-case']) {
  const src=join(glimpses,name+'.mp4');
  if(!existsSync(src)) throw Error('Missing Arabic UI demonstration: '+name);
  copyFileSync(src,join(project,'media',name+'.mp4'));
}
for(const f of readdirSync(fonts).filter(f=>f.endsWith('.ttf')))copyFileSync(join(fonts,f),join(project,'assets/fonts',f));
let html=readFileSync(join(project,'index.html'),'utf8');
html=html.replace(/<style id="arabic-typesetting">[\s\S]*?<\/style>/g,'');
html=html.replace('<html lang="en">','<html lang="ar">');
const css=readFileSync(join(fonts,'arabic.css'),'utf8')+`
#root { width:100%;height:100%; }
#root :is(.pilltext,.kicker,.display,.list-kicker,.label,.letter,.tag,.rlabel,.chiptext,.roundtext,.kin,#ailabel,#kicker,.dg-n b,.dg-n small,.dg-l,.cap) { font-family:'Noto Sans Arabic',sans-serif; direction:rtl; unicode-bidi:plaintext; letter-spacing:0; }
#root .cap { line-height:1.6; font-size:36px; }
#root .kin { font-size:80px; line-height:1.4; }
#root .display { line-height:1.45; }
#root .row .label { font-size:40px; }
#root #kicker { padding-inline:60px; line-height:1.5; }
#root .list-kicker { font-size:26px; line-height:1.5; }
#root .dg-n b { line-height:1.5; }
`;
html=html.replace('</head>',`<style id="arabic-typesetting">${css}</style></head>`);
writeFileSync(join(project,'index.html'),html);
const wj=JSON.parse(readFileSync(join(work,'words.json')));const stamp=t=>{const ms=Math.round(t*1000);return `${String(Math.floor(ms/3600000)).padStart(2,'0')}:${String(Math.floor(ms/60000)%60).padStart(2,'0')}:${String(Math.floor(ms/1000)%60).padStart(2,'0')}.${String(ms%1000).padStart(3,'0')}`};
writeFileSync(join(work,'captions.ar.vtt'),'WEBVTT\n\n'+wj.cues.map((c,i)=>`${i+1}\n${stamp((c.at??c.start)+0.5)} --> ${stamp((c.until??c.end)+0.5)}\n${c.text}\n`).join('\n'));
console.log('Arabic project and captions ready:',work);
