// Operator QA. Signs into an existing verified admin account without sending email.
// Credentials remain in memory; output contains counts and outcomes only.
import {execFileSync} from 'node:child_process'
import {writeFileSync} from 'node:fs'
const base=process.argv[2], out=process.argv[3], ask=process.argv.includes('--ask')
if(!/^https:\/\/(?:hormonaly\.perceptors\.ai|candidate---academy-hormonaly-[a-z0-9-]+\.a\.run\.app)$/.test(base)) throw Error('Unexpected QA host')
const tenant='hormonaly-academy-srbsc',email='omar@hormonaly.ai'
const access=execFileSync('gcloud',['auth','print-access-token','--configuration=perceptors'],{encoding:'utf8'}).trim()
const operatorHeaders={Authorization:`Bearer ${access}`,'X-Goog-User-Project':'perceptors','Content-Type':'application/json'}
async function json(url,options){const r=await fetch(url,options);const data=await r.json();if(!r.ok)throw Error(`QA request failed (${r.status})`);return data}
const users=await json(`https://identitytoolkit.googleapis.com/v1/projects/perceptors/tenants/${tenant}/accounts:batchGet?maxResults=1000`,{headers:operatorHeaders})
if(!users.users?.some(u=>u.email===email&&u.emailVerified&&!u.disabled)) throw Error('Existing verified admin required')
const link=await json('https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode',{method:'POST',headers:operatorHeaders,body:JSON.stringify({requestType:'EMAIL_SIGNIN',email,returnOobLink:true,tenantId:tenant,continueUrl:'https://hormonaly.perceptors.ai/'})})
const code=new URL(link.oobLink).searchParams.get('oobCode')
const signed=await json('https://identitytoolkit.googleapis.com/v1/accounts:signInWithEmailLink?key=AIzaSyDCZFExF1aRxwlxq3ifHsQCjJD-bUgAwZ0',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email,oobCode:code,tenantId:tenant})})
const headers={Authorization:`Bearer ${signed.idToken}`,'Content-Type':'application/json'}
const overview=await json(base+'/api/admin/overview',{headers})
const workspace=await json(base+'/api/editing/workspace',{headers})
const proof={host:base,verifiedAt:new Date().toISOString(),learners:overview.learners,started:overview.started,certificates:overview.certificates,editor:{loads:true,version:workspace.version,drafts:workspace.drafts.length,messages:workspace.messages.length,releases:workspace.releases.length,modelAvailable:workspace.modelAvailable},ask:null}
if(ask){
 const result=await json(base+'/api/editing/ask',{method:'POST',headers,body:JSON.stringify({version:workspace.version,group:'brand',instruction:'Explain briefly which branding fields I can edit here. This is a functional check: propose no changes and return an empty changes list.'})})
 if(result.drafts.length!==workspace.drafts.length||result.liveRevision!==workspace.liveRevision||result.messages.length!==workspace.messages.length+1)throw Error('Unexpected assistant mutation')
 proof.ask={responded:!!result.messages.at(-1)?.answer,draftsUnchanged:true,liveDesignUnchanged:true,newVersion:result.version}
}
writeFileSync(out,JSON.stringify(proof,null,2)+'\n');console.log(JSON.stringify(proof))
