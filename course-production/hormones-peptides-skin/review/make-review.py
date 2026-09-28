#!/usr/bin/env python3
"""Readable review draft of an authored module: python3 review/make-review.py m04"""
import json, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent
mid = sys.argv[1] if len(sys.argv) > 1 else "m04"
a = json.loads((D / "authored" / f"{mid}.json").read_text()); reg = json.loads((D / "citations" / f"{mid}.json").read_text())
short = {c["id"]: f"{c['authors'].split(',')[0].replace(' (sponsor)', '')} {c['year']}" for c in reg["citations"]}
short.update({"hannah-shmouni-2026-are": "Aesthetic & Regenerative Endocrinology 2026", "hannah-shmouni-2026-ppg-aug": "Peptide Pocket Guide (Aug 2026)"})
e = lambda x: (x or {}).get("en", "")
cites = lambda refs: " · ".join(short.get(r, r) for r in refs or [])
lessonOf = {bid: l for l in a["lessons"] for bid in l["blocks"]}
out = [f"""# Module {mid[1:]} — review draft

*Hormones and Peptides for Skin · stage 30 `{a['status']}` · authored {a['authoredAt']} · {len(a['blocks'])} moments, ~{a['unit']['estimatedMinutes']} min + module check*

For review by Omar Saleem, then Dr. Fady Hannah-Shmouni (final). Every factual sentence traces to the graded registry in
`citations/{mid}.md` ({len(reg['citations'])} sources, {len(reg['claims'])} claims). No dosing appears anywhere, by design. Audience: all
clinicians; moments marked **By role** carry three versions of the "what you do next" copy (prescriber · clinical staff · advisor) —
grades and regulatory facts never change by role. The last section lists what the author should check.
"""]
cur = None
for b in a["blocks"]:
    l = lessonOf[b["id"]]
    if l is not cur:
        cur = l; out.append(f"\n## Lesson {l['id']} · {e(l['title'])}\n")
    out.append(f"### {b['time']} · {e(b.get('title'))}  \n*{e(b.get('lead'))} · {b['type']}*\n")
    ra = (b.get("metadata") or {}).get("presentation") == "readalong"
    if ra and e(b.get("body")):  # a read-along card shows its beats; the body and points stay in the package for the Guide
        out.append(f"*Kept in the package for the Guide (a read-along card shows its beats instead):* {e(b['body'])}\n")
    elif e(b.get("body")): out.append(e(b["body"]) + "\n")
    for pt in ([] if ra else b.get("points", []) or []): out.append(f"- {e(pt)}")
    if b.get("points") and not ra: out.append("")
    s = b.get("stat")
    if s: out.append(f"**{s['figure']}** — {e(s.get('label'))} ({e(s.get('detail'))})  \n*Means:* {e(s.get('means'))}  \n*Does not mean:* {e(s.get('doesNot'))}\n")
    tl = b.get("tool")
    if tl:
        out.append("| | | |\n|---|---|---|")
        for it in tl["items"]: out.append(f"| {e(it['label'])} | {e(it['value'])} | {e(it.get('note'))} |")
        out.append(f"\n**Callout:** {e(tl.get('callout'))}\n" if tl.get("callout") else "")
    r = b.get("reflection")
    if r:
        out.append(f"*{e(r['prompt'])}*")
        for o in r["options"]: out.append(f"- **{e(o['label'])}** → {e(o['response'])}")
        out.append("")
    q = b.get("quiz")
    if q:
        out.append(f"**Q.** {e(q['prompt'])}")
        for i, o in enumerate(q["options"]): out.append(f"- {'✔' if i == q['correct'] else '✗'} {e(o['text'])} — *{e(o['why'])}*")
        out.append("")
    ix = b.get("interaction")
    if ix:
        out.append(f"**Exercise ({ix['kind']}) · {e(ix.get('title'))}** — {e(ix.get('prompt'))}")
        if ix["kind"] in ("classify", "quickfire"):
            lab = {x["value"]: e(x["label"]) for x in ix["labels"]}
            for it in ix["items"]: out.append(f"- {e(it['label'])} → **{lab[it['answer']]}** — *{e(it['why'])}*")
        if ix["kind"] == "scenario":
            out.append(f"\n{e(ix['setup'])}\n")
            for o in ix["options"]: out.append(f"- {'✔' if o.get('correct') else '✗'} {e(o['label'])} — *{e(o['why'])}*")
            out.append(f"\nFollow-up: {e(ix.get('followUp'))}")
        if ix["kind"] == "chips":
            out.append(f"*{e(ix['prefix'])} …* " + " · ".join(e(c['label']) for c in ix["chips"]))
        if ix["kind"] == "ladder":  # evidence ladder (sitting design, 2026-09-28): rungs low → high, each finding on its rung
            rung = {r["value"]: e(r["label"]) for r in ix["rungs"]}
            out.append("Rungs, low → high: " + " · ".join(rung.values()))
            for it in ix["items"]: out.append(f"- {e(it['label'])}{' — ' + e(it['detail']) if it.get('detail') else ''}: *{e(it['note'])}* → **{rung[it['answer']]}** — *{e(it['why'])}*")
            out.append(f"\nSummary: {e(ix.get('summary'))} · Closing: {e(ix.get('done'))}")
        if ix["kind"] == "twotier":  # move and reason (sitting design, 2026-09-28)
            out.append(f"\n{e(ix.get('setup'))}\n\n*{e(ix['prompt'])}*")
            for o in ix["options"]: out.append(f"- {'✔' if o.get('correct') else '✗'} {e(o['label'])} — *{e(o['why'])}*")
            out.append(f"\n*{e(ix['reasonPrompt'])}*")
            for o in ix["reasons"]: out.append(f"- {'✔' if o.get('correct') else '✗'} {e(o['label'])} — *{e(o['why'])}*")
            out.append(f"\n{'Optional reason in the learner’s own words (never graded). ' if ix.get('ownWords') else ''}Closing: {e(ix.get('done'))}")
        out.append("")
    if (b.get("metadata") or {}).get("presentation") == "readalong":  # read-along card: the beats are what the learner reads and hears
        out.append("**Read-along beats**")
        for i, bt in enumerate(b.get("audioBeats") or [], 1):
            keys = " · ".join(e(k) for k in bt.get("keyTerms") or [])
            regions = ", ".join(e(f.get("label")) or "region" for f in bt.get("focus") or [])
            out.append(f"{i}. **{e(bt['title'])}** — {e(bt['body'])}  \n   *Key terms:* {keys}{'  ·  *Picture:* ' + regions if regions else ''}")
        out.append("")
    v = (b.get("metadata") or {}).get("variants", {}).get("audienceLevel")
    if v:
        out.append("**By role**")
        for k, lab in [("prescriber", "Prescriber"), ("clinical-staff", "Clinical staff"), ("advisor", "Advisor")]: out.append(f"- *{lab}:* {e(v[k])}")
        out.append("")
    sc = e((b.get("metadata") or {}).get("audioScript"))
    if sc: out.append(f"<details><summary>{'Narration script of the audio story (kept for the Guide; this card speaks its beats)' if ra else 'Narration script'}</summary>\n\n{sc}\n\n</details>\n")
    if b.get("citationRefs"): out.append(f"<sub>Sources: {cites(b['citationRefs'])}</sub>\n")
c = a["check"]
out.append("\n## Module check\n")
out.append(f"**Q.** {e(c['prompt'])}")
for i, o in enumerate(c["options"]): out.append(f"- {'✔' if i == c['correct'] else '✗'} {e(o['text'])} — *{e(o['why'])}*")
out.append("\n## For the author\n")
out += [f"{i}. {f}" for i, f in enumerate(reg["authorFindings"], 1)]
(D / "review" / f"{mid}-draft.md").write_text("\n".join(out) + "\n")
print("wrote", D / "review" / f"{mid}-draft.md")
