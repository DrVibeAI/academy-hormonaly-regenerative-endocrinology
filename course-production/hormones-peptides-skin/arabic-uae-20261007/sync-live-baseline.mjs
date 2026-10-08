import fs from 'node:fs';import path from 'node:path';import{fileURLToPath}from'node:url';import{createRequire}from'node:module';
const root=path.dirname(fileURLToPath(import.meta.url)),academy=path.resolve(root,'../../..'),req=createRequire('/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/package.json'),yaml=req('yaml'),locale='ar-AE';
const read=n=>fs.readFileSync(path.join(root,n),'utf8'),old=yaml.parse(read('academy.ar-AE.review.yaml')),live=yaml.parse(read('live-baseline/academy.yaml')),known=new Map();
function walk(x,fn){if(x&&typeof x==='object'){if(typeof x.en==='string')fn(x);Object.values(x).forEach(v=>walk(v,fn))}}
walk(old,x=>{if(x[locale])known.set(x.en,x[locale])});
const additions={
'Enroll now':'سجّل الآن','Explore the science through illustrations':'استكشف العلم من خلال الرسوم التوضيحية','Faculty & advisory':'هيئة التدريس والمجلس الاستشاري','Faculty · Medical review':'هيئة التدريس · المراجعة الطبية','Endocrinologist and biochemical geneticist. Author of the Hormonaly pocket guides.':'اختصاصي الغدد الصماء والوراثة الكيميائية الحيوية، ومؤلف أدلة هورمونالي المرجعية المختصرة.','Advisory':'المجلس الاستشاري','The course is accredited by GCLS, the Geneva College of Longevity Science. CME or CE credit is not offered at this time.':'النسخة العربية قيد المراجعة، ولم يُعتمد لها رصيد تعليم طبي أو مهني مستمر.','October offer · free through October 31':'عرض أكتوبر · مجانًا حتى 31 أكتوبر','Free for October':'مجانًا خلال أكتوبر','Limited-time offer · Ends October 31':'عرض لفترة محدودة · ينتهي في 31 أكتوبر','Enroll free':'سجّل مجانًا'};
walk(live,x=>{const ar=additions[x.en]??known.get(x.en);if(!ar)throw Error('Untranslated live copy: '+x.en);x[locale]=ar});
live.localization=old.localization;live.brand.voices[locale]=old.brand.voices[locale];live.catalog[0].course=old.catalog[0].course;live.home.certificate=old.home.certificate;live.home.trust.title[locale]=old.home.trust.title[locale];live.home.reviewers=old.home.reviewers;
fs.writeFileSync(path.join(root,'academy.ar-AE.review.yaml'),yaml.stringify(live));
const packagePath=path.join(academy,'packages/hormones-peptides-skin.ar-AE.json'),p=JSON.parse(fs.readFileSync(packagePath)),source=JSON.parse(read('live-baseline/hormones-peptides-skin.json'));
for(const item of source.tutorCorpus){const target=p.tutorCorpus.find(t=>t.id===item.id);if(!target)throw Error('Tutor missing: '+item.id);target.answer.en=item.answer.en}
p.metadata.tutorVisuals=source.metadata.tutorVisuals;p.metadata.arabicEdition.deployedBaseline=JSON.parse(read('live-baseline/provenance.json'));
fs.writeFileSync(packagePath,JSON.stringify(p,null,2)+'\n');console.log('Applied verified deployed academy configuration and tutor presentation; Arabic content preserved.');

const reportPath=path.join(root,'BUILD-REPORT.json');if(fs.existsSync(reportPath)){const report=JSON.parse(fs.readFileSync(reportPath));report.deployedBaseline=JSON.parse(read('live-baseline/provenance.json'));fs.writeFileSync(reportPath,JSON.stringify(report,null,2)+'\n')}
