import{readFileSync,writeFileSync,mkdirSync}from'node:fs'
import{dirname,join,resolve}from'node:path'
import{fileURLToPath}from'node:url'
import{createHash}from'node:crypto'
const root=dirname(fileURLToPath(import.meta.url)),academy=resolve(root,'../../..'),locale='ar-AE'
const source=JSON.parse(readFileSync(join(root,'live-baseline/hormones-peptides-skin.json')))
const pkg=JSON.parse(readFileSync(join(academy,'packages/hormones-peptides-skin.ar-AE.json')))
const sourceMap=JSON.parse(readFileSync(join(root,'source-map.json')))
const at=(v,p)=>p.split('/').slice(1).reduce((o,k)=>o[k],v)
const digits=s=>(s.match(/\d+(?:[.,]\d+)?/g)??[]).sort()
const flags=[],missing=[],unchanged=[];let checks=0
for(const row of sourceMap.maps){
 const before=at(source,row.path).en,after=at(pkg,row.path)
 if(before!==after.en)throw Error('English source drift at '+row.path)
 if(!after[locale]?.trim())missing.push(row.path)
 if(after[locale]===before&&before.split(/\s+/).length>3)unchanged.push(row.path)
 if(JSON.stringify(digits(before))!==JSON.stringify(digits(after[locale]??'')))flags.push({path:row.path,en:before,ar:after[locale],sourceNumbers:digits(before),targetNumbers:digits(after[locale]??'')})
 checks++
}
let answerChecks=0
function compareAnswers(a,b,path=''){
 if(Array.isArray(a)){a.forEach((v,i)=>compareAnswers(v,b[i],path+'/'+i));return}
 if(!a||typeof a!=='object')return
 for(const[k,v]of Object.entries(a)){
  if(['correct','correctIndex','correctAnswer','correctOrder','answerKey','grade','citationRefs'].includes(k)){
   if(JSON.stringify(v)!==JSON.stringify(b[k]))throw Error('Structural answer/citation drift '+path+'/'+k)
   answerChecks++
  }else if(k!=='metadata')compareAnswers(v,b[k],path+'/'+k)
 }
}
compareAnswers(source.curriculum,pkg.curriculum,'curriculum');compareAnswers(source.assessments,pkg.assessments,'assessments')
const report={banner:'Agent pre-review — no gate opened',checks,missing,unchangedLong:unchanged,numericRepresentationFlags:flags.length,answerAndCitationChecks:answerChecks,sourceUnchanged:true,reviewOwner:'Fady@hormonaly.ai',releaseReady:false}
writeFileSync(join(root,'QA.json'),JSON.stringify(report,null,2)+'\n');writeFileSync(join(root,'NUMERIC-REVIEW.json'),JSON.stringify(flags,null,2)+'\n')
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))
function texts(v,out=[],path=''){
 if(Array.isArray(v)){v.forEach((x,i)=>texts(x,out,path+'/'+i));return out}
 if(v&&typeof v==='object'){
  if(typeof v.en==='string'&&typeof v[locale]==='string')out.push({en:v.en,ar:v[locale],path})
  else for(const[k,x]of Object.entries(v))texts(x,out,path+'/'+k)
 }
 return out
}
const labels={title:'العنوان',body:'المحتوى',lead:'مقدمة',answer:'إجابة المدرّس',prompt:'السؤال',feedback:'التغذية الراجعة',rationale:'التفسير',text:'النص',why:'سبب الإجابة',audioScript:'نص التعليق الصوتي'}
const row=t=>`<div class="textrow"><span class="kind">${esc(labels[t.path.split('/').at(-1)]??'محتوى تعليمي')}</span><p>${esc(t.ar)}</p><details><summary>النص الإنجليزي للمقارنة</summary><p dir="ltr" lang="en">${esc(t.en)}</p></details></div>`
const reg=JSON.parse(readFileSync(join(root,'regulatory-addendum.json')))
const cards=pkg.curriculum.modules.map(m=>`<section id="${m.id}"><div class="chapter"><small>${esc(m.id)}</small><h2>${esc(m.title[locale])}</h2><p>${esc(m.objective?.[locale])}</p></div>${m.units.flatMap(u=>u.blocks).map(b=>{const seen=new Set();const ts=texts(b).filter(x=>!seen.has(x.ar)&&seen.add(x.ar));const audio=pkg.assets.find(a=>a.id===b.id+'-narration-ar-AE');return `<article data-search="${esc(ts.map(x=>x.ar+' '+x.en).join(' '))}"><div class="meta">${esc(b.id)}</div><h3>${esc(b.title?.[locale]??b.lead?.[locale]??'')}</h3>${audio?`<audio controls preload="none" src="../../../public/${esc(audio.uri)}"></audio>`:''}${ts.map(row).join('')}</article>`}).join('')}${m.check?`<article><h3>تقييم الوحدة</h3>${texts(m.check).map(row).join('')}</article>`:''}</section>`).join('')
const assessments=`<section id="assessments"><h2>التقييم النهائي</h2>${pkg.assessments.map(a=>`<article>${texts(a).map(row).join('')}</article>`).join('')}</section>`
const tutor=`<section id="tutor"><h2>المدرّس والمصطلحات</h2>${pkg.tutorCorpus.map(t=>`<article><small>${esc(t.id)}</small>${texts(t).map(row).join('')}<details><summary>مرادفات البحث</summary><p>${esc(t.keys.join(' · '))}</p></details></article>`).join('')}</section>`
const sources=`<section id="sources"><h2>المصادر</h2><article>${pkg.provenance.citations.map(c=>`<p dir="auto">${c.url?`<a href="${esc(c.url)}" target="_blank" rel="noopener noreferrer">${esc(c.title)}</a>`:esc(c.title)} <small>${esc(c.id)}</small></p>${c.note?.[locale]?`<details><summary>ملاحظة المصدر</summary><p>${esc(c.note[locale])}</p><p dir="ltr" lang="en">${esc(c.note.en)}</p></details>`:''}`).join('')}</article></section>`
const html=`<!doctype html><html lang="ar-AE" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>الهرمونات والببتيدات للجلد — مراجعة النسخة العربية</title><style>*{box-sizing:border-box}body{margin:0;background:#f5f3ef;color:#252238;font:17px/1.9 'Geeza Pro','Arial',sans-serif}header{background:#262137;color:white;padding:44px max(6vw,24px)}header p{max-width:850px}h1{font-size:clamp(30px,4vw,48px);line-height:1.5;margin:8px 0}h2{font-size:28px}h3{font-size:23px}main{max-width:1060px;margin:auto;padding:30px 20px}.notice{background:#fff3cc;border-right:4px solid #ac7415;padding:18px 24px;border-radius:8px;margin:24px 0}nav{display:flex;gap:9px;flex-wrap:wrap;margin:25px 0}nav a{border:1px solid #aaa0bb;border-radius:20px;padding:5px 14px;color:inherit;text-decoration:none}article{background:white;border:1px solid #ddd7e4;border-radius:16px;padding:24px;margin:18px 0}section{scroll-margin-top:20px}.chapter{padding-top:30px}.meta,.kind,small{font-size:12px;color:#726980;overflow-wrap:anywhere}.meta{direction:ltr;text-align:left}p{margin:8px 0 16px;white-space:pre-wrap;overflow-wrap:anywhere}summary{cursor:pointer;color:#6e55a5;font-size:14px}details[open]{background:#f7f5fa;padding:14px;border-radius:8px}.textrow{border-top:1px solid #eee9f2;padding:14px 0}input{width:100%;padding:16px;font:inherit;border:1px solid #b9adc9;border-radius:12px;background:white}a{color:#66439c}audio{width:100%;margin:12px 0}footer{padding:40px;text-align:center;font-size:14px;color:#6c6276}.hidden{display:none}@media(max-width:600px){article{padding:17px}header{padding:26px 20px}body{font-size:16px}}</style><header><small style="color:#cec4df">HORMONALY ACADEMY · نسخة المراجع</small><h1>${esc(pkg.title[locale])}</h1><p>نسخة عربية موجهة للممارسين السريريين في الإمارات، مع توضيح وضع المنتجات في السعودية.</p><p>المراجع: فادي حنّا شمعوني · <bdi>Fady@hormonaly.ai</bdi></p></header><main><div class="notice">مسودة للمراجعة الطبية واللغوية. لم تُعتمد للنشر. الصوت العربي مسودة؛ الأفلام والترجمة الزمنية لا تزال قيد الإنتاج. قرارات الاعتماد السابقة للمحتوى الإنجليزي لا تمثل اعتماداً لهذه النسخة.</div><nav>${pkg.curriculum.modules.map((m,i)=>`<a href="#${m.id}">الوحدة ${i+1}</a>`).join('')}<a href="#assessments">التقييم</a><a href="#tutor">المدرّس</a><a href="#sources">المصادر</a></nav><input id="search" aria-label="ابحث في محتوى الدورة" placeholder="ابحث في المحتوى العربي أو الإنجليزي"><div class="notice">تفاصيل الأرقام، والاستطبابات، ودرجات الأدلة، والوضع التنظيمي تحتاج مراجعة فادي. حُفظت وحدات الدراسات كما وردت دون تحويل صامت.</div>${cards}${assessments}${tutor}${sources}</main><footer>Hormonaly Academy · 7 أكتوبر 2026 · Agent pre-review — no gate opened</footer><script>document.getElementById('search').addEventListener('input',e=>{const q=e.target.value.trim().toLowerCase();document.querySelectorAll('article[data-search]').forEach(a=>a.classList.toggle('hidden',!a.dataset.search.toLowerCase().includes(q)))})</script></html>`
writeFileSync(join(root,'review.html'),html)
writeFileSync(join(root,'QA-REPORT.md'),`# Arabic UAE edition — QA\n\nAgent pre-review — no gate opened.\n\n- ${checks} source text paths checked; ${missing.length} missing Arabic fields.\n- ${unchanged.length} unchanged English passages longer than three words.\n- ${answerChecks} original answer/grade/citation structures retained.\n- ${flags.length} numeric representation differences saved in NUMERIC-REVIEW.json; agent semantic comparison is documented in NUMERIC-SEMANTIC-REVIEW.json. Human medical review remains pending.\n- Original English source unchanged.\n- Reviewer: Fady@hormonaly.ai.\n- Arabic video/caption production and human review remain open; not publication-ready.\n`)
console.log(JSON.stringify(report))
