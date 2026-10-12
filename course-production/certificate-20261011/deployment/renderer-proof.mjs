// Run inside the exact deployed image via Cloud Build. No database reads or writes.
import assert from 'node:assert/strict'
import PDFDocument from 'pdfkit'
import { certificatePdf } from './server/certificate-pdf.ts'
import { academy } from './src/generated/academyConfig.ts'
import { certificateReleaseMissing } from './src/certificate-release.ts'
assert.equal(academy.slug, 'hormonaly')
assert.equal(academy.accreditation.gcls, false)
assert.equal(academy.site.certificatePartner, null)
assert.equal(academy.certificatePresentation.partnerLogo, undefined)
assert.equal(academy.certificatePresentation.signatures.length, 1)
assert.deepEqual(certificateReleaseMissing({release:academy.certificate.release}), [])
let texts = [], pages = 0
const originalText = PDFDocument.prototype.text, originalPage = PDFDocument.prototype.addPage
PDFDocument.prototype.text = function(...args) { texts.push(String(args[0])); return originalText.apply(this,args) }
PDFDocument.prototype.addPage = function(...args) { pages++; return originalPage.apply(this,args) }
for (const [lang, kind] of [['en','academy'], ['ar','academy'], ['en','gcls']]) {
 texts=[]; pages=0
 const cert={certId:'image-proof',code:'SAMPLE-DESIGN',learnerName:lang==='ar'?'أحمد العوضي':'Ahmed Elawadi',email:'design@example.invalid',courseId:'image-proof',courseTitle:{en:'Certificate · Hormones and Peptides for Skin',ar:'شهادة · الهرمونات والببتيدات للجلد'},credentialType:'completion',issuer:{kind,name:'Hormonaly Academy'},issuedAt:'2026-10-10T12:00:00Z',validUntil:null,status:'design-proof',evidence:{modulesCompleted:7,moduleCount:7,quizScore:100}}
 const doc=await certificatePdf(cert,lang,'https://verify.perceptors.ai')
 const chunks=[]
 await new Promise((resolve,reject)=>{doc.on('data',chunk=>chunks.push(chunk));doc.on('end',resolve);doc.on('error',reject)})
 const pdf=Buffer.concat(chunks)
 assert.equal(pdf.subarray(0,5).toString(),'%PDF-')
 assert.ok(pdf.length>20000)
 assert.equal(pages,1)
 assert.ok(texts.some(text=>text.includes('Fady Hannah-Shmouni')))
 assert.ok(!texts.some(text=>/GCLS|Dominik|Geneva College/i.test(text)))
 console.log(JSON.stringify({lang,storedIssuerKind:kind,pdfBytes:pdf.length,pages,fadyPresent:true,gclsElements:false,issuedCredential:false}))
}
console.log('DEPLOYED_IMAGE_CERTIFICATE_PROOF_PASS')
