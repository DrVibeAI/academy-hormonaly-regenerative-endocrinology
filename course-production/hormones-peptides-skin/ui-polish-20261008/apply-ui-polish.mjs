import {readFileSync, writeFileSync} from 'node:fs'
import {createRequire} from 'node:module'
const require=createRequire('/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/package.json')
const {parse,stringify}=require('yaml')
const file=process.argv[2]
const y=parse(readFileSync(file,'utf8'))
const asset=name=>`/assets/hormones-peptides-skin/ui/${name}.jpg`
y.experience={...y.experience,density:'compact',moduleImages:{...y.experience?.moduleImages,'1':asset('skin-texture'),'4':asset('collagen-fibers'),'7':asset('evidence-desk')}}
y.home.practice.image={src:asset('skin-texture'),alt:{en:'Editorial close-up of natural skin texture',ar:'صورة توضيحية مقربة لملمس الجلد الطبيعي'}}
y.home.certificate.image={src:asset('evidence-desk'),alt:{en:'Notebook and magnifying glass on an evidence-review desk',ar:'دفتر وعدسة مكبرة على مكتب لمراجعة الأدلة'}}
for(const line of y.today?.lines?.items??[]){
  if(line.from==='m1-p01') line.image={src:asset('skin-texture'),alt:{en:'Editorial close-up of natural skin texture',ar:'صورة توضيحية مقربة لملمس الجلد الطبيعي'}}
  if(line.from==='m7-p13') line.image={src:asset('evidence-desk'),alt:{en:'A quiet workspace for reviewing evidence',ar:'مساحة عمل هادئة لمراجعة الأدلة'}}
}
writeFileSync(file,stringify(y))
