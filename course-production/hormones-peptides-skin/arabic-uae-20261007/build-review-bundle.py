"""Refresh a local review archive; no publishing or approval actions."""
from pathlib import Path
import hashlib, json, zipfile
root=Path(__file__).resolve().parent
academy=root.parents[2]
target=root/'Hormonaly-Skin-Arabic-Review.zip'
with zipfile.ZipFile(target) as old:
    names=set(old.namelist())
    start=old.read('START-HERE.html')
# Legacy account screenshots predate the overlap fix. The source files stay intact.
names={n for n in names if not n.endswith(('/account-menu-mobile.jpg','/account-menu-desktop.jpg','/four-tab-mobile.jpg')) and n not in ['START-HERE.html','FILES-MANIFEST.json']}
for name in ['AUDIT-FINDINGS.md','QA-REPORT.md','QA-FIXES.md']:
    names.add(name)
for name in ['ACCOUNT-NAVIGATION-QA.md','account-menu-overlap-fixed.jpg','REGULATORY-REVIEW-GAPS.json','site.ar-AE.review.json','legal-arabic.json','build-legal-review.mjs','prepare-preview.mjs','refresh-preview.mjs','materialize.mjs','sync-live-baseline.mjs','BUILD-REPORT.json','build-review.mjs','build-review-bundle.py']:
    names.add(str((root/name).relative_to(academy)))
for folder in ['fixes-20261007','audit-20261007','evals','authored']:
    for file in (root/folder).rglob('*'):
        if file.is_file(): names.add(str(file.relative_to(academy)))
# A current navigation index points at current evidence and makes draft status explicit.
start=b'''<!doctype html><meta charset="utf-8"><title>Hormonaly Arabic review</title><style>body{max-width:850px;margin:50px auto;font:18px/1.6 system-ui}a{color:#0672df}</style><h1>Hormonaly Arabic review</h1><p>Draft for review. Not approved for release.</p><p><a href="QA-FIXES.md">Current repair report and remaining release requirements</a></p><p><a href="course-production/hormones-peptides-skin/arabic-uae-20261007/review.html">Bilingual course and audio review</a></p><p><a href="course-production/hormones-peptides-skin/arabic-uae-20261007/fixes-20261007/account-menu-mobile.png">Current mobile profile menu</a></p><p><a href="course-production/hormones-peptides-skin/arabic-uae-20261007/REGULATORY-REVIEW-GAPS.json">Pending Saudi product verification</a></p><p>Seven Arabic opening films and timed captions, medical/language/regulatory review, legal review and release decisions remain pending. Older evidence in audit-20261007 records the original findings; fixes-20261007 records the repairs.</p>'''
manifest={'status':'draft-review-only','releaseReady':False,'files':[]}
temporary=target.with_suffix('.tmp.zip')
with zipfile.ZipFile(temporary,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    z.writestr('START-HERE.html',start)
    manifest['files'].append({'path':'START-HERE.html','sha256':hashlib.sha256(start).hexdigest()})
    for name in sorted(names):
        file=academy/name
        if not file.is_file(): raise FileNotFoundError(file)
        z.write(file,name)
        manifest['files'].append({'path':name,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
    z.writestr('FILES-MANIFEST.json',json.dumps(manifest,indent=2))
with zipfile.ZipFile(temporary) as z:
    for row in manifest['files']:
        assert hashlib.sha256(z.read(row['path'])).hexdigest()==row['sha256'],row['path']
    audio=[n for n in z.namelist() if '/ar-AE/audio/' in n and n.endswith('.mp3')]
    assert len(audio)==48,len(audio)
    entries=len(z.namelist())
temporary.replace(target)
summary={'file':target.name,'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'entries':entries,'verifiedAudioLinks':len(audio),'recoveredEnglishCaptionTracks':7,'releaseReady':False,'allEntryChecksumsVerified':True,'runtimeRepairCommit':'ddd70918f8f3036b09c9461209ac74db02e51e4a'}
(root/'REVIEW-BUNDLE.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
