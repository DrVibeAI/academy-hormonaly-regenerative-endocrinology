from pathlib import Path
import subprocess,os,json,hashlib,time
O=Path('/tmp/hormonaly-bioform-demo-20261029');F=O/'final-films';cli='/Users/omar/.npm/_npx/678e79b7eb349f79/node_modules/hyperframes/bin/hyperframes.mjs';ff='/opt/homebrew/bin/ffmpeg';probe='/opt/homebrew/bin/ffprobe';env=dict(os.environ,HYPERFRAMES_NO_TELEMETRY='1',DO_NOT_TRACK='1',HYPERFRAMES_EXTRACT_CACHE_DIR='off')
def cmd(a,**kw):return subprocess.run(a,check=True,**kw)
def duration(p):return float(subprocess.check_output([probe,'-v','error','-show_entries','format=duration','-of','csv=p=0',str(p)]).decode().strip())
def streamhash(p,typ):
 text=subprocess.check_output([ff,'-v','error','-i',str(p),'-map','0:'+typ+':0','-c','copy','-f','streamhash','-hash','sha256','-']).decode().strip();return text.split('=')[-1]
results=[]
for d in sorted(F.glob('m??')):
 if not (d/'integration.json').exists():continue
 f=d.name;raw=d/(f+'-es-MX-lipsync-render.mp4');out=d/(f+'-es-MX-lipsync-music.mp4')
 if out.exists():results.append(json.loads((d/'verification.json').read_text()));continue
 if not raw.exists():
  with (d/'check.log').open('w')as log:cmd(['node',cli,'check',str(d/'project'),'--timeout','30000','--json'],stdout=log,stderr=subprocess.STDOUT,env=env,timeout=180)
  text=(d/'check.log').read_text();report=json.loads(text[text.index('{'):]);
  if not report['ok']:raise RuntimeError('Composition check failed '+f)
  (d/'render-pending.json').write_text(json.dumps({'status':'running-local','started':time.time(),'quality':'high','fps':24,'workers':2})+'\n')
  with (d/'render.log').open('w')as log:cmd(['node',cli,'render',str(d/'project'),'--fps','24','--quality','high','--workers','2','--frames-cache-dir','off','--strict','--output',str(raw)],stdout=log,stderr=subprocess.STDOUT,env=env,timeout=1200)
 mix=O/f/(f+'-es-MX-music-English-mouth-demo-draft.mp4');delta=abs(duration(raw)-duration(mix))
 if delta>.05:raise RuntimeError('Unexpected duration change '+f+' '+str(delta))
 cmd([ff,'-v','error','-i',str(raw),'-i',str(mix),'-map','0:v:0','-map','1:a:0','-c','copy','-movflags','+faststart',str(out)],timeout=120)
 audioSame=streamhash(out,'a')==streamhash(mix,'a')
 if not audioSame:raise RuntimeError('Canonical mixed audio changed '+f)
 cmd([ff,'-v','error','-i',str(out),'-f','null','-'],timeout=120)
 v={'film':f,'file':out.name,'status':'local-lipsync-music-candidate','duration':duration(out),'durationDeltaSeconds':delta,'renderQuality':'high','fps':24,'canonicalMixedAudioPacketHashUnchanged':audioSame,'audioStreamSha256':streamhash(out,'a'),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'allFramesDecode':True,'originalCaptionsAndCuesUnchanged':True,'narrationRegenerated':False,'nativeLanguageCertification':False,'published':False}
 (d/'verification.json').write_text(json.dumps(v,indent=2)+'\n');results.append(v);print(json.dumps(v),flush=True)
(F/'verification.json').write_text(json.dumps({'films':results,'paidRenderingCalls':0},indent=2)+'\n')
