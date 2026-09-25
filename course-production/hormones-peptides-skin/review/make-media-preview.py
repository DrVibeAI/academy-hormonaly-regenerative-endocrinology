#!/usr/bin/env python3
"""Contact sheet for the human media preview of the teaching stills (stage 60).

    python3 review/make-media-preview.py            → review/media-preview.html (self-contained) + review/media-preview.docx

Reads authored/mNN.json (block.teachingVisual / imageBrief), media/images-manifest.json (the image tool's manifest) and
media/stills-review.json (one line of what each moment teaches, and what the medical owner should check first).
Thumbnails are embedded, so the HTML opens anywhere without the repo. Nothing here approves anything: the stills stay
drafts until Omar (design) and Dr. Hannah-Shmouni (scientific accuracy) sign off in the media preview.
"""
import base64, html, json, shutil, subprocess, sys, tempfile
from pathlib import Path

D = Path(__file__).resolve().parent.parent            # course-production/hormones-peptides-skin
ROOT = D.parent.parent                                # academy root
OUT_HTML = D / "review" / "media-preview.html"
OUT_DOCX = D / "review" / "media-preview.docx"
THUMB_W = 960

manifest = {e["asset_id"]: e for e in json.loads((D / "media" / "images-manifest.json").read_text())["images"] if not e.get("kind")}
notes = json.loads((D / "media" / "stills-review.json").read_text())
pkg = json.loads((ROOT / "packages" / "hormones-peptides-skin.json").read_text())
mod_title = {m["id"]: m["title"]["en"] for m in pkg["curriculum"]["modules"]}
e = lambda x: (x or {}).get("en", "")

tmp = Path(tempfile.mkdtemp(prefix="media-preview-"))
def thumb(src: Path) -> Path:
    out = tmp / (src.stem + ".jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", f"scale={THUMB_W}:-2", "-q:v", "4", str(out)], check=True)
    return out

rows = []
for n in range(1, 8):
    mid = f"m0{n}"
    a = json.loads((D / "authored" / f"{mid}.json").read_text())
    lesson_of = {bid: l for l in a["lessons"] for bid in l["blocks"]}
    for b in a["blocks"]:
        tv = b.get("teachingVisual")
        if not tv:
            continue
        m = manifest[tv["assetRef"]]
        f = ROOT / "public" / m["uri"].lstrip("/")
        nt = notes["stills"][b["id"]]
        rows.append({
            "mid": mid, "module": mod_title[mid], "lesson": f"Lesson {lesson_of[b['id']]['id']} · {e(lesson_of[b['id']]['title'])}",
            "id": b["id"], "time": b.get("time", ""), "lead": e(b.get("lead")), "title": e(b.get("title")),
            "alt": e(tv["alt"]), "teaches": nt["teaches"], "check": nt.get("medicalCheck"), "prio": nt.get("medicalCheckPriority", 99), "regenerated": nt.get("regenerated"),
            "file": m["uri"].lstrip("/"), "thumb": thumb(f), "model": m["model"], "generated": m["generated_at"][:10],
        })

flagged = sorted((r for r in rows if r["check"]), key=lambda r: r["prio"])
esc = html.escape
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()

cards, current = [], None
for r in rows:
    if r["mid"] != current:
        current = r["mid"]
        cards.append(f'<h2 id="{r["mid"]}"><span class="mono">Module {r["mid"][1:]}</span>{esc(r["module"])}</h2>')
    check = f'<p class="check"><span class="mono">Check first</span>{esc(r["check"])}</p>' if r["check"] else ""
    regen = f'<p class="meta">Regenerated {esc(r["regenerated"])}</p>' if r["regenerated"] else ""
    cards.append(f"""<article class="still" id="{r['id']}">
  <figure><div class="frame"><img src="data:image/jpeg;base64,{b64(r['thumb'])}" alt="{esc(r['alt'])}"><i class="bar" aria-hidden="true"></i></div></figure>
  <div class="text">
    <p class="mono">{esc(r['id'])} · {esc(r['time'])} · {esc(r['lead'])}</p>
    <h3>{esc(r['title'])}</h3>
    <p class="lesson">{esc(r['lesson'])}</p>
    <dl><dt>Teaches</dt><dd>{esc(r['teaches'])}</dd><dt>Alt text</dt><dd>{esc(r['alt'])}</dd></dl>
    {check}{regen}
    <p class="meta">{esc(r['file'])} · {esc(r['model'])} · draft · {esc(r['generated'])}</p>
  </div>
</article>""")

# Module opening films (cinematic lane): poster, length, where the narration comes from, and the hosted draft to watch.
FILMS = json.loads((D / "media" / "films-manifest.json").read_text()).get("films", []) if (D / "media" / "films-manifest.json").exists() else []
BUCKET = "https://storage.googleapis.com/perceptors-academy-hormonaly-media/"
film_cards = []
for f in FILMS:
    n = int(f["block"][1]); pth = thumb(ROOT / "public" / f["poster"])
    film_cards.append(f"""<article class="still film" id="{f['block']}">
  <figure><div class="frame tall"><img src="data:image/jpeg;base64,{b64(pth)}" alt="Opening film poster, module {n}"></div></figure>
  <div class="text">
    <p class="mono">{esc(f['block'])} · {round(f['durationSeconds'])} s · opening film</p>
    <h3>Module {n:02d} · {esc(mod_title[f'm0{n}'])}</h3>
    <p><a href="{BUCKET}{esc(f['uri'])}">Watch the draft film</a></p>
    <dl><dt>Narration</dt><dd>Approved text, verbatim: {esc('; '.join(f['scriptSources']))}</dd>
    <dt>Presenter</dt><dd>HeyGen digital avatar; under the player: \u201c{esc(f['disclosure']['en'])}\u201d</dd>
    <dt>Check</dt><dd>Each plate shows what the narration names at that moment; labels come from the film, the pictures carry no text.</dd></dl>
    <p class="meta">{esc(f['uri'])} · {esc(f['models'])} · draft</p>
  </div>
</article>""")
first = "".join(f'<li><a href="#{r["id"]}">{esc(r["id"])}</a> {esc(r["title"])} <span class="muted">— {esc(r["check"])}</span></li>' for r in flagged)
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Teaching stills · media preview</title>
<style>
:root {{ --paper:#F4F1E9; --panel:#FBF9F4; --ink:#1C1B2B; --muted:#66636B; --rule:#D7D2C8; --violet:#5A4BC4; --violet-soft:#E9E5F7; --sage:#E8EBE3; }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--paper); color:var(--ink); font:15px/1.6 "DM Sans", -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }}
main {{ max-width:1180px; margin:0 auto; padding:48px 32px 96px; }}
h1, h2, h3 {{ font-family:"Fraunces", "Source Serif 4", Georgia, serif; font-weight:500; letter-spacing:-0.01em; }}
h1 {{ font-size:44px; line-height:1.1; margin:8px 0 16px; }}
h2 {{ font-size:28px; margin:64px 0 8px; padding-top:24px; border-top:1px solid var(--rule); display:flex; gap:16px; align-items:baseline; }}
h3 {{ font-size:21px; line-height:1.25; margin:2px 0 4px; }}
.mono, h2 .mono {{ font-family:"DM Mono", ui-monospace, Menlo, monospace; font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }}
.lede {{ max-width:760px; font-size:16px; }}
.panel {{ background:var(--panel); border:1px solid var(--rule); border-radius:2px; padding:20px 24px; margin:24px 0; }}
.panel h4 {{ margin:0 0 8px; font:600 12px/1.4 "DM Mono", ui-monospace, Menlo, monospace; letter-spacing:.08em; text-transform:uppercase; }}
.panel ul {{ margin:0; padding-left:18px; }} .panel li {{ margin:4px 0; }}
.facts {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:1px; background:var(--rule); border:1px solid var(--rule); margin:24px 0; }}
.facts div {{ background:var(--panel); padding:14px 16px; }} .facts b {{ display:block; font-family:"Fraunces", Georgia, serif; font-size:22px; font-weight:500; }}
a {{ color:var(--violet); }}
.muted {{ color:var(--muted); }}
.still {{ display:grid; grid-template-columns:minmax(0, 1.25fr) minmax(0, 1fr); gap:28px; padding:24px 0; border-bottom:1px solid var(--rule); align-items:start; }}
figure {{ margin:0; }}
.frame {{ position:relative; background:var(--violet-soft); border:1px solid var(--rule); border-radius:2px; overflow:hidden; aspect-ratio:16/9; }}
.frame.tall {{ aspect-ratio:9/16; max-width:300px; }}
.frame img {{ display:block; width:100%; height:100%; object-fit:cover; object-position:top; }}
.bar {{ display:none; position:absolute; left:2.5%; right:2.5%; bottom:4%; height:27%; border-radius:6px; background:rgba(21,27,46,.82); }}
body.phone .bar {{ display:block; }}
dl {{ margin:10px 0 0; }} dt {{ font:600 11px/1.4 "DM Mono", ui-monospace, Menlo, monospace; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); margin-top:10px; }}
dd {{ margin:2px 0 0; }}
.lesson {{ margin:0; color:var(--muted); font-size:13px; }}
.check {{ background:var(--sage); border:1px solid var(--rule); border-radius:2px; padding:10px 12px; margin:14px 0 0; font-size:14px; }}
.check .mono {{ display:block; color:#506C5A; margin-bottom:2px; }}
.meta {{ font-family:"DM Mono", ui-monospace, Menlo, monospace; font-size:11px; color:var(--muted); margin:10px 0 0; word-break:break-all; }}
label.toggle {{ display:inline-flex; gap:8px; align-items:center; font-size:14px; cursor:pointer; }}
nav.toc {{ font-size:14px; }} nav.toc a {{ margin-right:14px; }}
@media (max-width:820px) {{ main {{ padding:28px 16px 64px; }} .still {{ grid-template-columns:1fr; gap:14px; }} h1 {{ font-size:34px; }} }}
</style></head>
<body><main>
<p class="mono">Hormonaly Academy · Hormones and Peptides for Skin · stage 60 media · human media preview</p>
<h1>Media preview — opening films and teaching stills</h1>
<p class="lede">One explanatory still for each narrated moment ({len(rows)} in all). Each one sits above the play control on the audio
card, so on a phone the learner sees it while the narration plays. Every still is a <b>draft</b>: nothing is approved until Omar Saleem
signs off the design and Dr. Fady Hannah-Shmouni signs off the scientific accuracy. All words stay in the app (titles, chapters, alt
text); the pictures carry no text, numbers, doses, products or faces.</p>
<div class="facts">
  <div><span class="mono">Stills</span><b>{len(rows)}</b>7 modules, one per narrated moment</div>
  <div><span class="mono">Generator</span><b>Nano Banana 2</b>gemini-3.1-flash-image · final tier · 16:9</div>
  <div><span class="mono">One hand</span><b>Style anchor</b>m1-p03 (four units of the skin), passed with every other still</div>
  <div><span class="mono">Look at first</span><b>{len(flagged)}</b>moments with a scientific point to confirm</div>
</div>
<div class="panel"><h4>How to review</h4><ul>
<li><b>Scientific accuracy (Dr. Hannah-Shmouni):</b> does the picture show what the moment says, at the level it is drawn? A wrong figure is worse than none — mark any still to redraw or drop.</li>
<li><b>Design (Omar):</b> one set, one hand; calm paper register; the violet marks the one thing the moment is about.</li>
<li><b>Phone view:</b> on a phone the play control covers roughly the bottom quarter of the picture. <label class="toggle"><input type="checkbox" id="phone"> Show where the play control sits</label></li>
<li>Reply with the moment id (for example <span class="mono">m5-p14</span>) and "keep", "redraw: …" or "drop".</li>
</ul></div>
<div class="panel"><h4>Look at these first</h4><ul>{first}</ul></div>
{('<h2 id="films"><span class="mono">Films</span>Module opening films</h2><p class="lede">One opening film per module, right after the module cover: the presenter introduces the module, then diagrams, plates and footage follow the narration word by word. Draft media: nothing is approved until the same two sign-offs as the stills.</p>' + ''.join(film_cards)) if film_cards else ''}
<nav class="toc">{''.join(f'<a href="#m0{n}">Module 0{n}</a>' for n in range(1, 8))}</nav>
{''.join(cards)}
<p class="meta">Generated by course-production/hormones-peptides-skin/review/make-media-preview.py from media/images-manifest.json · drafts pending the human media preview.</p>
</main>
<script>
(function () {{ var c = document.getElementById('phone'); if (!c) return;
  c.addEventListener('change', function () {{ document.body.classList.toggle('phone', c.checked); }}); }})();
</script>
</body></html>
"""
OUT_HTML.write_text(page)
print(OUT_HTML, f"{OUT_HTML.stat().st_size/1e6:.1f} MB", len(rows), "stills")

# .docx copy (pandoc embeds the thumbnails)
if shutil.which("pandoc"):
    md = [f"# Teaching stills — contact sheet\n",
          f"*Hormones and Peptides for Skin · stage 60 media · {len(rows)} draft stills · gemini-3.1-flash-image (Nano Banana 2), final tier, 16:9 · "
          "style anchor m1-p03. Drafts until Omar Saleem (design) and Dr. Fady Hannah-Shmouni (scientific accuracy) sign off. "
          "The pictures carry no text, numbers, doses, products or faces; all words stay in the app.*\n",
          "**How to reply:** give the moment id and \"keep\", \"redraw: …\" or \"drop\".\n",
          ] + ([f"## Module opening films ({len(FILMS)})\n"] + [x for f in FILMS for x in (
              f"### Module {int(f['block'][1]):02d} · {mod_title['m0' + f['block'][1]]}\n", f"![]({thumb(ROOT / 'public' / f['poster'])}){{width=2.4in}}\n",
              f"**Watch:** {BUCKET}{f['uri']} ({round(f['durationSeconds'])} s)  \n**Narration:** approved text, verbatim ({'; '.join(f['scriptSources'])})  \n**Presenter:** HeyGen digital avatar; under the player: \u201c{f['disclosure']['en']}\u201d\n")] if FILMS else []) + [
          "## Look at these first\n"] + [f"- **{r['id']}** {r['title']} — {r['check']}" for r in flagged] + [""]
    current = None
    for r in rows:
        if r["mid"] != current:
            current = r["mid"]; md.append(f"\n## Module {r['mid'][1:]} · {r['module']}\n")
        md.append(f"### {r['id']} · {r['title']}\n")
        md.append(f"*{r['time']} · {r['lead']} · {r['lesson']}*\n")
        md.append(f"![]({r['thumb']}){{width=6in}}\n")
        md.append(f"**Teaches:** {r['teaches']}  \n**Alt text:** {r['alt']}\n")
        if r["check"]: md.append(f"**Check first:** {r['check']}\n")
        md.append(f"`{r['file']}` · draft\n")
    src = tmp / "media-preview.md"
    src.write_text("\n".join(md))
    subprocess.run(["pandoc", str(src), "-o", str(OUT_DOCX), "--resource-path", str(tmp)], check=True)
    print(OUT_DOCX, f"{OUT_DOCX.stat().st_size/1e6:.1f} MB")
shutil.rmtree(tmp)
