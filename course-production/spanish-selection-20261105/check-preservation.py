"""Verify that selecting the existing Spanish edition preserves all original package data."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
original=root/'packages/hormones-peptides-skin.ar-AE.json'
selected=root/'packages/hormones-peptides-skin.es-MX.json'
a=json.loads(original.read_text());b=json.loads(selected.read_text());changes=[];leaves=0

def walk(old,new,path=''):
    global leaves
    if isinstance(old,dict) and isinstance(new,dict):
        for key,value in old.items():
            if key not in new:changes.append(path+'/'+key)
            else:walk(value,new[key],path+'/'+key)
    elif isinstance(old,list) and isinstance(new,list):
        for index,value in enumerate(old):
            if index>=len(new):changes.append(path+'/'+str(index))
            else:walk(value,new[index],path+'/'+str(index))
    else:
        leaves+=1
        if old!=new:changes.append(path)
walk(a,b)
assert not changes,changes
manifest=json.loads((root/'presentation-inputs/home-glimpses-bilingual.json').read_text())
assert manifest['packageSha256']==hashlib.sha256(selected.read_bytes()).hexdigest()
for item in manifest['captures']:
    assert hashlib.sha256((root/'public'/item['src']).read_bytes()).hexdigest()==item['sha256']
report={'originalSha256':hashlib.sha256(original.read_bytes()).hexdigest(),'selectedSha256':hashlib.sha256(selected.read_bytes()).hexdigest(),'originalLeavesCompared':leaves,'changedOrMissingOriginalPaths':changes,'unchangedScreenshotFiles':len(manifest['captures']),'packagesEdited':False,'scope':'Existing original leaves preserved recursively; screenshots remain their recorded languages. Does not certify Spanish translation or clinical content.'}
Path(__file__).with_name('package-preservation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
