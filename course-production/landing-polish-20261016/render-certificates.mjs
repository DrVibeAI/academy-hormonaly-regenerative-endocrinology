import {mkdirSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const {certificatePdf}=await import(pathToFileURL(resolve('server/certificate-pdf.ts')));
const out=resolve('../academy/public/assets/certificate/previews/20261016');mkdirSync(out,{recursive:true});
for(const lang of ['en','ar']){
 const specimen={certId:'landing-preview',code:'SAMPLE-PREVIEW',learnerName:lang==='ar'?'اسمك هنا':'Your name',email:'preview@example.invalid',courseId:'hormonaly.hormones-peptides-skin',courseTitle:{en:'Hormones and Peptides for Skin',ar:'الهرمونات والببتيدات للجلد'},credentialType:'completion',issuer:{kind:'academy',name:'Hormonaly Academy'},issuedAt:'2026-10-16T12:00:00Z',validUntil:null,status:'design-proof',evidence:{modulesCompleted:7,moduleCount:7,quizScore:100}};
 const doc=await certificatePdf(specimen,lang,'https://verify.perceptors.ai/');const chunks=[];
 await new Promise((resolve,reject)=>{doc.on('data',chunk=>chunks.push(chunk));doc.on('end',resolve);doc.on('error',reject)});
 writeFileSync(`${out}/certificate-${lang}.pdf`,Buffer.concat(chunks));
 console.log(`${lang}: rendered certificate specimen without issuing a credential`);
}
