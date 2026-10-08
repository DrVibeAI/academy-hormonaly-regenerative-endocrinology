import {readFileSync,writeFileSync} from 'node:fs'
import {dirname,resolve,join} from 'node:path'
import {fileURLToPath} from 'node:url'
import {createRequire} from 'node:module'
import {execFileSync} from 'node:child_process'
const root=dirname(fileURLToPath(import.meta.url))
const out=resolve(process.argv[2])
const require=createRequire('/Users/omar/DrVibe/worktrees/runtime-hormonaly-arabic-20261007/package.json')
const {parse,stringify}=require('yaml')
const approval=JSON.parse(readFileSync(join(root,'OWNER-RELEASE-APPROVAL.json'),'utf8'))
execFileSync(process.execPath,[join(root,'prepare-cloud-review.mjs'),out],{stdio:'inherit'})
const config=join(out,'academy.yaml'),file=join(out,'packages/hormones-peptides-skin.ar-AE.json')
const y=parse(readFileSync(config,'utf8')),p=JSON.parse(readFileSync(file,'utf8'))
p.baseLocale='en'
p.version='1.2.0-ar-AE.1'
p.metadata.previewOnly=false
Object.assign(p.metadata.arabicEdition,{status:'approved',previewOnly:false,releaseAuthorized:true,releaseApproval:approval})
const ar=p.locales.find(l=>l.locale==='ar-AE')
ar.status='approved'
ar.notes += ' Public Arabic release authorized by the product owner in chat on 2026-10-08; this does not create a medical-reviewer attestation or resolve regulatory gaps.'
y.deployment.reviewOnly=false
delete y.deployment.reviewNotice
y.localization.defaultCountry='AE'
if(y.home?.certificate?.title && p.governance?.accreditation?.status!=='accredited') y.home.certificate.title.en='Certificate of completion'
if(y.home?.certificate?.body) y.home.certificate.body.ar='شهادة إتمام من Hormonaly Academy عند استيفاء متطلبات الدورة واجتياز التقييم النهائي.'
if(y.home?.trust?.title) y.home.trust.title.ar='محتوى يستند إلى الأدلة وحدودها'
writeFileSync(config,stringify(y))
writeFileSync(file,JSON.stringify(p,null,2))
execFileSync(process.execPath,[join(root,'../ui-polish-20261008/apply-ui-polish.mjs'),config],{stdio:'inherit'})
console.log('Prepared owner-authorized bilingual release; reference films and regulatory gaps remain labelled.')
