import * as fs from 'node:fs/promises';
const root='/Users/omar/DrVibe/worktrees/hormonaly-qa-20261015/academy/course-production/final-mobile-qa-20261016';
export function bind(tab) {
 const snap=()=>tab.playwright.domSnapshot();
 const btn=(name)=>tab.playwright.getByRole('button',{name,exact:true});
 const loc=(s)=>tab.playwright.locator(s);
 const click=async b=>{await b.click();return snap();};
 async function capture(label,image=true){
  const state=await snap();
  if(image){await tab.playwright.waitForTimeout(650);await fs.writeFile(`${root}/${label}.jpg`,await tab.screenshot({fullPage:false}));}
  const metrics=await tab.playwright.evaluate(()=>({url:location.href,width:innerWidth,height:innerHeight,scrollWidth:document.documentElement.scrollWidth,media:[...document.querySelectorAll('audio,video')].map(e=>({tag:e.tagName,src:e.currentSrc.startsWith('data:')?'data:audio[omitted]':e.currentSrc.split('?')[0],time:e.currentTime,duration:Number.isFinite(e.duration)?e.duration:null,paused:e.paused,error:e.error?.code??null,ready:e.readyState}))}));
  const r={label,state,metrics};await fs.writeFile(`${root}/${label}.visit.json`,JSON.stringify(r,null,2));return r;
 }
 async function replay(lang){
  const ar=lang==='ar',practice=ar?'تدرّب مجددًا':'Practice again',back=ar?'العودة إلى النتيجة المحفوظة':'Back to saved result',label=lang+'-replay-'+(await tab.url()).split('/').slice(-2).join('-');
  await snap();
  const info=await tab.playwright.evaluate(()=>({kind:document.querySelector('.ix')?.className||(document.querySelector('.document-inspection')?'inspect':document.querySelector('.deck-quiz-options')?'quiz':'none'),quick:[...document.querySelectorAll('.ix-summary li')].map(e=>e.textContent.split('→').pop().trim()),sequence:[...document.querySelectorAll('.ix-seq strong')].map(e=>e.textContent),classify:[...document.querySelectorAll('.ix-item')].map(e=>[...e.querySelectorAll('button')].findIndex(b=>b.classList.contains('answer'))),decisions:[...document.querySelectorAll('.ix-decision')].map(e=>[...e.querySelectorAll('button')].findIndex(b=>b.classList.contains('right'))),scenario:[...document.querySelectorAll('.ix--scenario .ix-options button')].findIndex(b=>b.classList.contains('right')),quiz:[...document.querySelectorAll('.deck-quiz-options button')].findIndex(b=>b.classList.contains('correct')),inspect:[...document.querySelectorAll('.document-inspection [role="group"] button')].map((b,i)=>({i,flag:b.getAttribute('aria-pressed')==='true'}))}));
  if(info.kind.includes('chips')){const b=loc('.ix-chip').first(),before=await b.getAttribute('aria-pressed');await click(b);await click(b);return{kind:'chips',label,done:before===await b.getAttribute('aria-pressed')};}
  if(info.kind==='none'||!await btn(practice).count())return{kind:'none'};
  await click(btn(practice));let actions=0,wrongFeedback;
  if(info.kind==='quiz'){const bs=loc('.deck-quiz-options button');await click(bs.nth((info.quiz+1)%await bs.count()));const r=await capture(label+'-wrong',false);wrongFeedback=r.state.includes(ar?'غير صحيح حتى الآن.':'Not yet.');await click(bs.nth(info.quiz));await click(loc('.deck-quiz-details summary'));actions=3;}
  else if(info.kind==='inspect'){const bs=loc('.document-inspection [role="group"] button'),wrong=info.inspect.find(f=>!f.flag);if(wrong)await click(bs.nth(wrong.i));for(const f of info.inspect.filter(f=>f.flag))await click(bs.nth(f.i));actions=info.inspect.length;}
  else if(info.kind.includes('hotspots')){await loc('.ix-stage').press('Enter');await snap();for(const b of await loc('.ix-pin').all()){await click(b);actions++;}}
  else if(info.kind.includes('quickfire')){for(const a of info.quick){await click(loc('.ix--quickfire .ix-labels').getByRole('button',{name:a,exact:true}));actions++;}}
  else if(info.kind.includes('sequence')){for(const a of info.sequence){await click(btn(a));actions++;}}
  else if(info.kind.includes('classify')){for(let i=0;i<info.classify.length;i++){await click(loc('.ix-item').nth(i).getByRole('button').nth(info.classify[i]));actions++;}}
  else if(info.kind.includes('branching')){for(let i=0;i<info.decisions.length;i++){const bs=loc('.ix-decision').nth(i).getByRole('button');await click(bs.nth((info.decisions[i]+1)%await bs.count()));await click(bs.nth(info.decisions[i]));actions+=2;}}
  else if(info.kind.includes('scenario')){const bs=loc('.ix--scenario .ix-options').getByRole('button');await click(bs.nth((info.scenario+1)%await bs.count()));await click(bs.nth(info.scenario));actions=2;}
  else if(info.kind.includes('reveal')){for(const b of await loc('.ix-flip').all()){await click(b);actions++;}}
  else return{...info,done:false};
  await capture(label);const done=await btn(practice).count()>0;await click(btn(back));const result={kind:info.kind,label,actions,done,wrongFeedback};await fs.writeFile(`${root}/${label}.json`,JSON.stringify(result));return result;
 }
 async function walk(n,lang){const out=[];for(let i=0;i<n;i++){const s=await snap(),p=s.match(/progressbar "(?:الخطوة|Step) (\d+) (?:من|of) (\d+)/);if(!p)break;const r=await replay(lang);if(r.kind!=='none')out.push(r);if(r.kind!=='none'&&!r.done)break;for(const b of await loc('main main details > summary').all()){if(!await b.evaluate(e=>e.parentElement.open)){await click(b);await click(b);}}await capture(lang+'-review-'+(await tab.url()).split('/').slice(-2).join('-'));if(p[1]===p[2])break;await click(btn(lang==='ar'?'الفقرة التالية':'Next tap'));}return out;}
 return {capture,replay,walk};
}
