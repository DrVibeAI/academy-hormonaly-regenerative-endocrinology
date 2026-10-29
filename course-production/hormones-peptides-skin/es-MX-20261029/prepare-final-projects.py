from pathlib import Path
import json,shutil,re,hashlib,subprocess,os
O=Path('/tmp/hormonaly-bioform-demo-20261029');M=Path('/Users/omar/Documents/Codex/2026-10-27/task/media-es-MX-20261028');D=O/'approved-lipsync/with-source-speech';F=O/'final-films';F.mkdir(exist_ok=True)
ledger=json.loads((D/'ledger.json').read_text());jobs={e['key']:e for e in ledger['clips']};rows=json.loads((O/'lipsync-with-source-speech.json').read_text())['clips'];results=[]
for f in [f'm{i:02}' for i in range(1,8)]:
 selected=[r for r in rows if r['film']==f]
 if any(not jobs.get(f+'-'+r['content'],{}).get('output') for r in selected):continue
 source=Path('/tmp/hormonaly-module2-completion-20261029/m02') if f=='m02' else M/'narration-elevenlabs/visual-cue-drafts'/f
 target=F/f;project=target/'project';target.mkdir(exist_ok=True)
 if not project.exists():
  project.mkdir();(project/'media').mkdir();os.symlink(source/'project/assets',project/'assets');os.symlink(source/'project/narration.mp3',project/'narration.mp3')
  for p in (source/'project/media').iterdir():os.symlink(p,project/'media'/p.name)
 html=(source/'project/index.html').read_text();plan=json.loads((source/'plan.render-draft.json').read_text());changes=[]
 for r in selected:
  e=jobs[f+'-'+r['content']];c=next(c for c in plan['contents'] if c['id']==r['content']);old=c['video']['src'];name=f+'-'+r['content']+'-es-MX-lipsync.mp4';dest=project/'media'/name
  # Renderer expects the original full track span, although part of a closing track is off screen.
  # Pad only its invisible tail; never extend paid synthesis or alter any on-screen cue.
  need=c['video']['dur'];actual=float(subprocess.check_output(['/opt/homebrew/bin/ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',e['output']]).decode().strip());pad=max(0,need-actual)
  if not dest.exists():
   args=['/opt/homebrew/bin/ffmpeg','-v','error','-i',e['output'],'-an']
   if pad>.001:args+=['-vf',f'tpad=stop_mode=clone:stop_duration={pad+.05},fps=24','-t',str(need),'-c:v','libx264','-crf','18','-preset','fast']
   else:args+=['-c:v','copy']
   subprocess.run(args+['-movflags','+faststart',str(dest)],check=True,timeout=90)
  html=html.replace('media/'+old,'media/'+name);c['video']['src']=name;c['video'].pop('draftEnglishMouth',None)
  changes.append({'content':r['content'],'old':old,'new':name,'jobId':e['jobId'],'downloadSha256':e['sha256'],'sourceSeconds':actual,'invisibleTailPaddingSeconds':pad})
 warning='<div id="draft-warning">BORRADOR · Boca en inglés; narración en español. Sin sincronía labial.</div>'
 if html.count(warning)!=1:raise RuntimeError('Unexpected warning marker '+f)
 html=html.replace(warning,'');(project/'index.html').write_text(html)
 (project/'hyperframes.json').write_text(json.dumps({'name':f+'-es-MX-lipsync-local-candidate','hyperframes':'0.8.3','status':'local-lipsync-candidate-not-published'},indent=2)+'\n')
 (target/'plan.render-lipsync.json').write_text(json.dumps(plan,indent=2)+'\n')
 proof={'film':f,'changes':changes,'narrationUnchanged':hashlib.sha256((project/'narration.mp3').read_bytes()).hexdigest()==hashlib.sha256((source/'project/narration.mp3').read_bytes()).hexdigest(),'timingsUnchanged':True,'scientificImagesUnchanged':True,'warningRemovedAfterBothPresenterJobsComplete':True,'nativeFidelityApproval':False}
 (target/'integration.json').write_text(json.dumps(proof,indent=2)+'\n');results.append(proof);print(f,'ready',flush=True)
(F/'prepared-projects.json').write_text(json.dumps(results,indent=2)+'\n')
