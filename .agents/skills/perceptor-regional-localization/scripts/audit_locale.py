#!/usr/bin/env python3
"""Read-only locale/structure and country-note audit; does not validate medical claims."""
import argparse, hashlib, json
from pathlib import Path

def audit(source, candidate, locale, countries):
    errors=[]; localized=0; preserved=0
    keys={'correct','correctIndex','correctAnswer','correctOrder','answerKey','grade','citationRefs'}
    def walk(a,b,path=''):
        nonlocal localized,preserved
        if path == '/governance/approvals': return  # source approvals must not approve a new locale
        if isinstance(a,dict):
            if not isinstance(b,dict): errors.append({'path':path,'error':'source shape missing'}); return
            if isinstance(a.get('en'),str):
                localized+=1
                if b.get('en')!=a['en']: errors.append({'path':path,'error':'English source changed'})
                if not isinstance(b.get(locale),str) or not b[locale].strip(): errors.append({'path':path,'error':'missing translation'})
            for k,v in a.items():
                if k in keys and '/metadata/' not in path:
                    preserved+=1
                    if b.get(k)!=v: errors.append({'path':path+'/'+k,'error':'answer/evidence/citation changed'})
                if isinstance(v,(dict,list)): walk(v,b.get(k),path+'/'+k)
        elif isinstance(a,list):
            if not isinstance(b,list) or len(b)<len(a): errors.append({'path':path,'error':'source items missing'});return
            for i,v in enumerate(a):walk(v,b[i],path+'/'+str(i))
    walk(source,candidate)
    citation_ids={c['id'] for c in candidate.get('provenance',{}).get('citations',[])}
    notes={c:[] for c in countries}; gaps=[]
    for m in candidate['curriculum']['modules']:
        for u in m['units']:
            for block in u['blocks']:
                variants=block.get('metadata',{}).get('variants',{}).get('jurisdiction',{})
                if not variants:continue
                for country in countries:
                    note=variants.get(country)
                    if not note:gaps.append({'block':block['id'],'country':country});continue
                    notes[country].append(block['id'])
                    if not note.get('text',{}).get(locale):errors.append({'block':block['id'],'country':country,'error':'country note not localized'})
                    for ref in note.get('citationRefs',[]):
                        if ref not in citation_ids:errors.append({'block':block['id'],'error':'unknown citation','ref':ref})
    return {'locale':locale,'sourceFieldsChecked':localized,'protectedStructuresChecked':preserved,'countryNotes':{k:len(v) for k,v in notes.items()},'countryNoteBlocks':notes,'countryCoverageGaps':gaps,'errors':errors,'interpretation':'Mechanical coverage only. Does not establish product legality, freshness, clinical completeness or reviewer approval.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('candidate',type=Path);p.add_argument('--locale',required=True);p.add_argument('--countries',nargs='+',required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    data=a.source.read_bytes();report=audit(json.loads(data),json.loads(a.candidate.read_text()),a.locale,a.countries)
    report['sourceSha256']=hashlib.sha256(data).hexdigest();a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='countryNoteBlocks'},ensure_ascii=False));raise SystemExit(bool(report['errors']))
