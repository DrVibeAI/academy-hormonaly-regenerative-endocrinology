import {readFileSync,writeFileSync} from 'node:fs'
import {createRequire} from 'node:module'
const require=createRequire('/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/package.json')
const {parse,stringify}=require('yaml')
const file=process.argv[2],y=parse(readFileSync(file,'utf8'))
const base='assets/hormones-peptides-skin/home'
y.home.glimpses.captureManifest='presentation-inputs/home-glimpses-bilingual.json'
y.home.glimpses.items=[
  {src:`${base}/en/inside-film.png`,srcByLocale:{ar:`${base}/ar/inside-practice.png`},caption:{en:'A short film opens every module',ar:'اختبر فهمك بخطوات قصيرة'}},
  {src:`${base}/en/inside-science.png`,srcByLocale:{ar:`${base}/ar/inside-science.png`},caption:{en:'Explore the science through illustrations',ar:'استكشف العلم من خلال الرسوم التوضيحية'}},
  {src:`${base}/en/inside-trial.png`,srcByLocale:{ar:`${base}/ar/inside-trial.png`},caption:{en:'Sort the evidence, one tap at a time',ar:'صنّف الأدلة بنقرة واحدة في كل خطوة'}},
]
writeFileSync(file,stringify(y))
