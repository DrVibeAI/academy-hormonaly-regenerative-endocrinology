#!/usr/bin/env python3
"""Review packet for the 1.1 practice activities (Omar 2026-09-25: "go ahead with the 1.1 activities").

    python3 review/make-activities-review.py     → review/activities-1.1.html (self-contained) + review/activities-1.1.docx

Reads authored/mNN.json, takes every block whose metadata.activity.version is "1.1", and lays out for the medical owner what the
learner will see (title, prompt, every option and its explanation, the right answers) next to the approved sentences each
activity was built from, resolved from the module's own text ("m2-p02 body, sentence 2"). Hotspot pictures are drawn with their
spots. Nothing here approves anything: each activity stays a change after approval until Dr. Hannah-Shmouni confirms it.
"""
import base64, html, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

D = Path(__file__).resolve().parent.parent
ROOT = D.parent.parent
OUT_HTML = D / "review" / "activities-1.1.html"
OUT_DOCX = D / "review" / "activities-1.1.docx"
pkg = json.loads((ROOT / "packages" / "hormones-peptides-skin.json").read_text())
asset_uri = {a["id"]: a["uri"] for a in pkg.get("assets", [])}
e = lambda x: (x or {}).get("en", "") if isinstance(x, dict) else (x or "")
esc = html.escape
KIND = {"sequence": "Put in order", "branching": "Case in decisions", "hotspots": "Find on the picture", "inspect": "Spot the unsupported claim",
        "classify": "Sort or grade", "reveal": "Tap to reveal", "quickfire": "Quick judgement", "scenario": "Case, one decision", "chips": "Build the sentence"}

SENT = re.compile(r"(?<=[.!?])[\"'”’)]?\s+(?=[A-Z0-9\"'“‘(])")
def sentences(text): return [s.strip() for s in SENT.split(text or "") if s.strip()]

def nums(spec):
    idx = []
    for part in re.split(r"\s*(?:,|and|&)\s*", spec or ""):
        r = re.match(r"^(\d+)\s*[–-]\s*(\d+)$", part.strip())
        if r: idx += list(range(int(r.group(1)), int(r.group(2)) + 1))
        elif part.strip().isdigit(): idx.append(int(part.strip()))
    return idx

def pick_sentences(text, spec):
    if not spec: return text
    ss = sentences(text); picked = [ss[i - 1] for i in nums(spec) if 0 < i <= len(ss)]
    return " ".join(picked) if picked else None

UNITS = {}
def resolve(src, blocks, unit=None):
    """'m4-p05 tool row 3', 'm2-p02 body, sentence 2', 'm4-p14 means s1–2', 'm6-p07 beat 2', 'm4-p06 audienceLevel clinical-staff s2', 'unit tutorContext s7'…"""
    m = re.match(r"^\s*(m\d-[a-z0-9-]+)\b(.*)$", src)
    if not m:
        u = re.match(r"^\s*unit tutorContext\s*,?\s*(?:sentences?|s)\s*([\d–\-, and]+)", src)
        return pick_sentences(e((unit or {}).get("tutorContext")) if isinstance((unit or {}).get("tutorContext"), dict) else (unit or {}).get("tutorContext", ""), u.group(1)) if u and unit else None
    b = blocks.get(m.group(1)); rest = m.group(2)
    if not b: return None
    sent = re.search(r"(?:sentences?|\bs)\s*([\d][\d–\-, and]*)", rest)
    spec = sent.group(1).strip() if sent else None
    low = rest.lower()
    md = b.get("metadata") or {}
    if "tool row" in low:
        rows = nums(re.search(r"tool rows?\s*([\d–\-, and]+)", low).group(1)) if re.search(r"tool rows?\s*([\d–\-, and]+)", low) else []
        items = (b.get("tool") or {}).get("items", [])
        txt = " ".join(f"{e(items[i-1].get('label'))}: {e(items[i-1].get('value'))}{' (' + e(items[i-1].get('note')) + ')' if items[i-1].get('note') else ''}." for i in rows if 0 < i <= len(items))
        return txt or None
    if "callout" in low: return e((b.get("tool") or {}).get("callout")) or None
    for f in ("detail", "means", "doesnot", "label", "figure"):
        if re.search(rf"\bstat\b.*\b{f}\b|\b{f}\b", low) and b.get("stat"):
            key = {"doesnot": "doesNot"}.get(f, f); v = b["stat"].get(key)
            txt = e(v) if isinstance(v, dict) else (str(v) if v else "")
            if txt: return pick_sentences(txt, spec)
    if re.search(r"\baudiencelevel\b", low):
        lvl = re.search(r"audiencelevel\s+([a-z-]+)", low)
        v = ((md.get("variants") or {}).get("audienceLevel") or {}).get(lvl.group(1) if lvl else "", {})
        return pick_sentences(e(v), spec) if v else None
    if re.search(r"\b(audiobeats|beats?)\b", low):
        bn = re.search(r"(?:audiobeats|beats?)\s*(\d+)", low); beats = b.get("audioBeats") or []
        if bn and 0 < int(bn.group(1)) <= len(beats):
            bt = beats[int(bn.group(1)) - 1]; return pick_sentences(f"{e(bt.get('title'))}. {e(bt.get('body'))}", spec)
        return " ".join(f"{e(x.get('title'))}. {e(x.get('body'))}" for x in beats) or None
    if "points" in low:
        pts = b.get("points") or []; pn = re.search(r"points\s*([\d–\-, and]+)", low)
        sel = [pts[i-1] for i in nums(pn.group(1))] if pn else pts
        return " · ".join(e(x) for x in sel if x) or None
    if "audioscript" in low: return pick_sentences(e(md.get("audioScript")), spec)
    if "title" in low and "body" not in low: return e(b.get("title")) or None
    if "body" in low or spec: return pick_sentences(e(b.get("body")), spec)
    return e(b.get("body")) or None

tmp = Path(tempfile.mkdtemp(prefix="activities-review-"))
def hotspot_picture(uri, spots, name):
    from PIL import Image, ImageDraw
    im = Image.open(ROOT / "public" / uri).convert("RGB")
    im.thumbnail((960, 960))
    d = ImageDraw.Draw(im); W, H = im.size
    for i, s in enumerate(spots, 1):
        x, y = s["at"][0] / 100 * W, s["at"][1] / 100 * H; r = (s.get("radius") or 11) / 100 * W
        d.ellipse([x - r, y - r, x + r, y + r], outline=(90, 75, 196), width=4)
        d.ellipse([x - 16, y - 16, x + 16, y + 16], fill=(90, 75, 196)); d.text((x - 5, y - 8), str(i), fill=(255, 255, 255))
    out = tmp / f"{name}.jpg"; im.save(out, quality=85); return out

def body_of(ix, bid):
    k = ix.get("kind"); parts = []
    if ix.get("setup"): parts.append(f'<p class="setup">{esc(e(ix["setup"]))}</p>')
    if ix.get("notice"): parts.append("<p class='mono'>What you notice</p><ul>" + "".join(f"<li>{esc(e(n))}</li>" for n in ix["notice"]) + "</ul>")
    if k == "sequence":
        parts.append("<ol class='steps'>" + "".join(f"<li><b>{esc(e(s['label']))}</b>{'<br><span class=why>' + esc(e(s.get('why'))) + '</span>' if s.get('why') else ''}</li>" for s in ix.get("steps", [])) + "</ol><p class='muted'>Shown shuffled; this is the right order.</p>")
    elif k == "branching":
        for n_i, n in enumerate(ix.get("nodes", []), 1):
            parts.append(f"<h4>Decision {n_i} · {esc(e(n['prompt']))}</h4><ul class='opts'>" + "".join(
                f"<li class='{'right' if o.get('correct') else ''}'><b>{'✓ ' if o.get('correct') else ''}{esc(e(o['label']))}</b><br><span class=why>{esc(e(o['why']))}</span>{' <span class=muted>→ next decision</span>' if o.get('next') else ''}</li>" for o in n["options"]) + "</ul>")
    elif k in ("classify", "quickfire"):
        labels = {l["value"]: e(l["label"]) for l in ix.get("labels", [])}
        parts.append("<p class='muted'>Buttons: " + " · ".join(esc(v) for v in labels.values()) + "</p><ul class='opts'>" + "".join(
            f"<li><b>{esc(e(i['label']))}</b>{' — ' + esc(e(i.get('detail'))) if i.get('detail') else ''}<br>Answer: <b>{esc(labels.get(i['answer'], i['answer']))}</b><br><span class=why>{esc(e(i['why']))}</span></li>" for i in ix.get("items", [])) + "</ul>")
    elif k == "inspect":
        parts.append("<ul class='opts'>" + "".join(f"<li class='{'flag' if s.get('suspect') else ''}'>{'⚑ ' if s.get('suspect') else ''}{esc(e(s['text']))}<br><span class=why>{esc(e(s['why']))}</span></li>" for s in ix.get("segments", [])) + "</ul>")
        if ix.get("hint"): parts.append(f"<p class='muted'>Hint: {esc(e(ix['hint']))}</p>")
    elif k == "reveal":
        parts.append("<ul class='opts'>" + "".join(f"<li><b>{esc(e(c['label']))}</b><br><span class=why>{esc(e(c['hidden']))}</span></li>" for c in ix.get("cards", [])) + "</ul>")
    elif k == "hotspots":
        uri = asset_uri.get(ix.get("imageAssetRef", ""))
        if uri and all(isinstance(s.get("at"), list) for s in ix.get("hotspots", [])):
            pic = hotspot_picture(uri, ix["hotspots"], bid)
            parts.append(f'<img class="pic" src="data:image/jpeg;base64,{base64.b64encode(pic.read_bytes()).decode()}" alt="">')
        parts.append("<ol class='opts'>" + "".join(f"<li><b>{esc(e(s['label']))}</b><br><span class=why>{esc(e(s['why']))}</span></li>" for s in ix.get("hotspots", [])) + "</ol>")
    elif k == "scenario":
        parts.append("<ul class='opts'>" + "".join(f"<li class='{'right' if o.get('correct') else ''}'><b>{'✓ ' if o.get('correct') else ''}{esc(e(o['label']))}</b><br><span class=why>{esc(e(o['why']))}</span></li>" for o in ix.get("options", [])) + "</ul>")
    if ix.get("followUp"): parts.append(f"<p><b>Then:</b> {esc(e(ix['followUp']))}</p>")
    if ix.get("done"): parts.append(f"<p class='done'>{esc(e(ix['done']))}</p>")
    return "".join(parts)

NOTES = Path("/private/tmp/claude-501/-Users-omar-DrVibe/08a9c34b-8ea9-4677-8e10-0862fa9ea335/scratchpad/activities")
def drafting_notes(mid):
    # The drafting notes' open questions (headings that mention open points, checks, caveats or review), bullets only.
    f = NOTES / f"{mid}.md"
    if not f.exists(): return []
    out, on = [], False
    for line in f.read_text().splitlines():
        if re.match(r"^(#+ |\*\*[^*]+:\*\*\s*$)", line.strip()):
            on = bool(re.search(r"unsure|open|attention|review|check|caveat|question|note", line, re.I))
            continue
        if on and re.match(r"^\s*(-|\d+\.)\s+", line): out.append(re.sub(r"^\s*(-|\d+\.)\s+", "", line).strip())
    return out[:12]

sections, total, kinds = [], 0, {}
for n in range(1, 8):
    mid = f"m0{n}"
    a = json.loads((D / "authored" / f"{mid}.json").read_text())
    blocks = {b["id"]: b for b in a["blocks"]}
    lesson_of = {bid: l for l in a["lessons"] for bid in l["blocks"]}
    acts = [b for b in a["blocks"] if ((b.get("metadata") or {}).get("activity") or {}).get("version") == "1.1"]
    if not acts: continue
    title = next((m["title"]["en"] for m in pkg["curriculum"]["modules"] if m["id"] == mid), mid)
    cards = []
    for b in acts:
        ix = b["interaction"]; total += 1; kinds[ix["kind"]] = kinds.get(ix["kind"], 0) + 1
        l = lesson_of.get(b["id"]); order = l["blocks"].index(b["id"]) if l else -1
        after = l["blocks"][order - 1] if l and order > 0 else "—"
        srcs = (b.get("metadata") or {}).get("activity", {}).get("sources", [])
        src_html = "".join(f"<li><span class='mono'>{esc(s)}</span>{'<br>“' + esc(r) + '”' if (r := resolve(s, blocks, a.get('unit'))) else '<br><span class=muted>(check this reference by hand)</span>'}</li>" for s in srcs)
        hedge = f"<span class='hedge'>{esc(e(ix['hedge']))}</span>" if ix.get("hedge") else ""
        cards.append(f"""<article class="act"><div class="left"><p class="mono">{esc(b['id'])} · {esc(KIND.get(ix['kind'], ix['kind']))} · Lesson {esc(l['id'] if l else '?')}, after {esc(after)}</p>
<h3>{esc(e(b.get('title')))} {hedge}</h3><p class="prompt">{esc(e(ix.get('prompt')) or e(b.get('body')))}</p>{body_of(ix, b['id'])}</div>
<div class="right"><p class="mono">Built from</p><ul class="src">{src_html}</ul><p class="mono">Sources</p><p class="muted">{esc(b.get('sourceNote', ''))}</p>
<p class="mono">Review</p><p>☐ Correct as written &nbsp; ☐ Change (note below)</p><p class="note"></p></div></article>""")
    notes = drafting_notes(mid)
    notes_html = f'<div class="notes"><p class="mono">Points the drafting flagged for your attention</p><ul>{"".join(f"<li>{esc(x)}</li>" for x in notes)}</ul></div>' if notes else ""
    sections.append(f'<h2 id="{mid}"><span class="mono">Module {n}</span>{esc(title)}</h2>' + notes_html + "".join(cards))

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hormones and Peptides for Skin · 1.1 practice activities for review</title><style>
body{{margin:0;background:#F4F1E9;color:#1C1B2B;font:15px/1.55 "DM Sans",-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:44px 28px 96px}} h1,h2,h3{{font-family:"Fraunces",Georgia,serif;font-weight:500}}
h1{{font-size:40px;line-height:1.1;margin:6px 0 12px}} h2{{font-size:26px;margin:56px 0 6px;padding-top:20px;border-top:1px solid #D7D2C8;display:flex;gap:14px;align-items:baseline}}
h3{{font-size:21px;margin:4px 0}} h4{{margin:14px 0 6px;font-size:15px}} .mono{{font:600 11px/1.4 "DM Mono",ui-monospace,Menlo,monospace;letter-spacing:.06em;text-transform:uppercase;color:#66636B;margin:0 0 4px}}
.act{{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:28px;padding:22px 0;border-bottom:1px solid #D7D2C8}}
.prompt{{font-weight:600}} .setup{{background:#FBF9F4;border:1px solid #D7D2C8;border-radius:4px;padding:10px 12px}} .why{{color:#3f3d47}} .muted{{color:#66636B}}
.opts,.steps,.src{{padding-left:20px}} .opts li,.steps li,.src li{{margin:8px 0}} .opts li.right b{{color:#1f6b34}} .opts li.flag{{color:#8a3b00}}
.hedge{{font:600 12px "DM Sans";background:#fff;border:1px solid #D7D2C8;border-radius:999px;padding:3px 9px;vertical-align:middle;color:#5E5B64}}
.done{{background:#E8EBE3;border-radius:4px;padding:8px 10px}} .pic{{max-width:100%;border:1px solid #D7D2C8;border-radius:4px;margin:8px 0}}
.notes{{background:#fff;border:1px solid #D7D2C8;border-radius:4px;padding:10px 16px;margin:8px 0 4px;font-size:14px}}
.right{{background:#FBF9F4;border:1px solid #D7D2C8;border-radius:4px;padding:14px 16px;align-self:start}} .note{{min-height:60px;border-bottom:1px solid #D7D2C8}}
@media(max-width:820px){{.act{{grid-template-columns:1fr}}}}
</style></head><body><main><p class="mono">Hormones and Peptides for Skin · version 1.1 · for Dr. Fady Hannah-Shmouni</p>
<h1>New practice activities for review</h1>
<p>{total} activities across the seven modules ({', '.join(f'{v} {KIND.get(k, k).lower()}' for k, v in sorted(kinds.items()))}). Each is built only from sentences you have already approved; the right-hand column quotes them. Please mark each one correct as written, or note the change.</p>
{''.join(sections)}</main></body></html>"""
OUT_HTML.write_text(page)
print(f"✓ {OUT_HTML} ({total} activities)")
if shutil.which("pandoc"):
    subprocess.run(["pandoc", str(OUT_HTML), "-o", str(OUT_DOCX)], check=True)
    print(f"✓ {OUT_DOCX}")
