#!/usr/bin/env python3
"""Review packet for the sitting-design pilot on Module 1 (Omar 2026-09-28: "yes to all 4").

    python3 review/make-sitting-pilot-review.py    → review/sitting-pilot-m01.html (self-contained but for the audio) + review/sitting-pilot-m01.docx

For Dr. Fady Hannah-Shmouni (every changed moment: before and after, the approved sentences it was built from, the reason, what moved
elsewhere and what is flagged) and Omar Saleem (the journey and dosage before and after, and the new narration to hear). Reads
authored/m01.json (postApprovalChanges and mediaChanges tagged pilot "sitting-design-2026-09-28"), the dosage audit reports in
course-production/dosage/, the narration manifest, the approved stills (focus regions drawn on them) and, when present,
review/sitting-pilot-m01.gates.json. Nothing here approves anything: every change stays open until the approvers confirm it
(confirmedBy / confirmedAt on the change, narrationPreview in signoffs.json).
"""
import base64, html, json, shutil, subprocess, tempfile
from pathlib import Path

D = Path(__file__).resolve().parent.parent            # course-production/hormones-peptides-skin
ROOT = D.parent.parent                                # academy root
PILOT = "sitting-design-2026-09-28"
OUT_HTML = D / "review" / "sitting-pilot-m01.html"
OUT_DOCX = D / "review" / "sitting-pilot-m01.docx"
a = json.loads((D / "authored" / "m01.json").read_text())
pkg = json.loads((ROOT / "packages" / "hormones-peptides-skin.json").read_text())
man = json.loads((D / "narration" / "readalong-manifest.json").read_text())["beats"] if (D / "narration" / "readalong-manifest.json").exists() else {}
voices = json.loads((D / "narration-voices.json").read_text()) if (D / "narration-voices.json").exists() else {}
DOSE = ROOT / "course-production" / "dosage"
dose = {v: json.loads((DOSE / f"{pkg['id']}-{v}.json").read_text()) for v in ("1.1.0", pkg["version"]) if (DOSE / f"{pkg['id']}-{v}.json").exists()}
GATES = D / "review" / "sitting-pilot-m01.gates.json"
gates = json.loads(GATES.read_text()) if GATES.exists() else None
changes = [c for c in a.get("postApprovalChanges", []) if c.get("pilot") == PILOT]
media = [c for c in a.get("mediaChanges", []) if c.get("pilot") == PILOT]
B = {b["id"]: b for b in a["blocks"]}
assets = {x["id"]: x for x in pkg.get("assets", [])}
e = lambda x: (x or {}).get("en", "") if isinstance(x, dict) else (x or "")
esc = html.escape
tmp = Path(tempfile.mkdtemp(prefix="sitting-pilot-review-"))
COLORS = [(90, 75, 196), (201, 97, 30), (32, 128, 96), (180, 40, 90)]


def focus_picture(bid):
    """The approved still with every beat's focus regions drawn in its beat's colour and numbered."""
    from PIL import Image, ImageDraw, ImageFont
    b = B[bid]
    uri = assets[b["teachingVisual"]["assetRef"]]["uri"]
    im = Image.open(ROOT / "public" / uri).convert("RGB")
    im.thumbnail((1100, 1100))
    d = ImageDraw.Draw(im); W, H = im.size
    try: font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except Exception: font = ImageFont.load_default()
    for i, beat in enumerate(b.get("audioBeats") or []):
        c = COLORS[i % len(COLORS)]
        for f in beat.get("focus") or []:
            x0, y0, x1, y1 = f["x"] / 100 * W, f["y"] / 100 * H, (f["x"] + f["w"]) / 100 * W, (f["y"] + f["h"]) / 100 * H
            d.rectangle([x0, y0, x1, y1], outline=c, width=3)
            label = f"{i + 1} {e(f.get('label'))}".strip()
            tw = d.textlength(label, font=font) if hasattr(d, "textlength") else 8 * len(label)
            d.rectangle([x0, y0, x0 + tw + 10, y0 + 24], fill=c)
            d.text((x0 + 5, y0 + 3), label, fill=(255, 255, 255), font=font)
    out = tmp / f"{bid}-focus.jpg"; im.save(out, quality=82)
    return out


b64 = lambda p: base64.b64encode(Path(p).read_bytes()).decode()
rel_public = lambda uri: "../../../public/" + uri   # from course-production/hormones-peptides-skin/review/

# ------------------------------------------------------------------ the journey, per lesson, before and after
def sequence(report, label):
    m = next((m for m in report["modules"] if m["id"] == "m01"), None)
    if not m: return ""
    rows = []
    for s in m["sittings"]:
        cards = " › ".join(f"<span class='{'dec' if p['decision'] else 'pas'}'>{esc(p['id'].replace('m1-', ''))}</span>" for p in s["panes"])
        fd = s["firstDecisionSeconds"]
        rows.append(f"<tr><td>{esc(s['label'])}</td><td class='seq'>{cards}</td><td>{'none' if fd is None else f'{fd // 60}:{fd % 60:02d}'}</td><td>{s['maxPassiveRun']}</td><td>{s['maxWords']} ({esc(s['maxWordsPane'])})</td><td>{'yes' if s['constructive'] else 'no'}</td></tr>")
    return (f"<h3>{esc(label)}</h3><table><tr><th>Lesson (sitting)</th><th>Moments in order (<span class='dec'>decision</span> · <span class='pas'>passive</span>)</th>"
            f"<th>First decision</th><th>Passive in a row</th><th>Most words before a tap</th><th>Constructive step</th></tr>{''.join(rows)}</table>")


def dose_summary(report):
    s, m = report["summary"], next(m for m in report["modules"] if m["id"] == "m01")
    fails = [f for f in report["findings"] if f["level"] == "fail" and f.get("module") == "m01"]
    return s, m, fails


# ------------------------------------------------------------------ one change
def text_block(v):
    if isinstance(v, str): return f"<p class='quote'>{esc(v)}</p>"
    return f"<pre>{esc(json.dumps(v, ensure_ascii=False, indent=1))}</pre>"


def beats_table(beats, with_keys=True):
    out = ["<ol class='beats'>"]
    for i, bt in enumerate(beats, 1):
        keys = " · ".join(esc(k) for k in bt.get("keyTerms", [])) if with_keys else ""
        out.append(f"<li><b>{esc(bt['title'])}</b> <span class='muted'>({len(bt['body'].split())} words)</span><br>{esc(bt['body'])}"
                   + (f"<br><span class='mono'>Key terms</span> {keys}" if keys else "") + "</li>")
    return "".join(out) + "</ol>"


def narration_rows(bid):
    rows = sorted(((e_["beat"], k, e_) for k, e_ in man.items() if e_["block"] == bid))
    out = []
    for n, k, x in rows:
        tim = ROOT / "public" / (x.get("timings_uri") or "")
        stats = json.loads(tim.read_text()).get("stats", {}) if x.get("timings_uri") and tim.exists() else {}
        out.append(f"<li><span class='mono'>beat {n}</span> {x['duration_seconds']:.1f} s · {esc(x['loudness'])} · word timings {stats.get('matched', '?')}/{stats.get('tokens', '?')}"
                   f"<br><audio controls preload='none' src='{esc(rel_public(x['audio_uri']))}'></audio><br><span class='path'>public/{esc(x['audio_uri'])}</span></li>")
    return "<ul class='narr'>" + "".join(out) + "</ul>" if out else ""


def change_card(c):
    bid = c["block"].split(",")[0].strip()
    parts = [f"<article class='chg' id='{esc(bid)}-{abs(hash(c['change'])) % 10000}'>",
             f"<p class='mono'>{esc(c['block'])} · {esc(c['date'])} · for {esc(c['forReview'])} · <b class='await'>awaiting confirmation</b></p>",
             f"<h3>{esc(c['change'])}</h3>", f"<p class='why'><b>Why.</b> {esc(c['reason'])}</p>"]
    ra = bid in B and (B[bid].get("metadata") or {}).get("presentation") == "readalong" and isinstance(c.get("after"), list)
    if ra:
        parts.append("<div class='two'><div><p class='mono'>Before · flip-card chapters</p>" + beats_table(c["before"], with_keys=False) + "</div>"
                     "<div><p class='mono'>After · read-along beats (what the learner reads and hears)</p>" + beats_table(c["after"]) + "</div></div>")
        pic = focus_picture(bid)
        parts.append(f"<figure><img class='pic' src='data:image/jpeg;base64,{b64(pic)}' alt='Focus regions on the approved still'><figcaption>Focus regions: each beat lights its numbered boxes (drawn here in the beat's colour).</figcaption></figure>")
        parts.append("<p class='mono'>Narration (Gemini 3.8 TTS, draft)</p>" + narration_rows(bid))
    elif c.get("before") is not None or c.get("after") is not None:
        parts.append(f"<div class='two'><div><p class='mono'>Before</p>{text_block(c.get('before'))}</div><div><p class='mono'>After</p>{text_block(c.get('after'))}</div></div>")
    if c.get("sources"): parts.append("<p class='mono'>Built from (approved sentences)</p><ul>" + "".join(f"<li>{esc(s)}</li>" for s in c["sources"]) + "</ul>")
    if c.get("carriedElsewhere"): parts.append("<p class='mono'>What left this card, and where the module still teaches it</p><ul>" + "".join(f"<li>{esc(s)}</li>" for s in c["carriedElsewhere"]) + "</ul>")
    if c.get("flags"): parts.append("<div class='flag'><p class='mono'>For your decision</p><ul>" + "".join(f"<li>{esc(s)}</li>" for s in c["flags"]) + "</ul></div>")
    parts.append("<p class='tick'>☐ Correct as written &nbsp; ☐ Change (note below)</p><p class='note'></p></article>")
    return "".join(parts)


# ------------------------------------------------------------------ page
quotes = [
    "yes to all 4 and i agree, the films are great, dont want to change them, rather its more what is around them and the journey that we are focused on here",
    "also for the audio, lets improve the quality of the narration, use gemini 3.8 tts across, even if it means redoing them",
]
before = dose.get("1.1.0"); after = dose.get(pkg["version"])
dose_html = ""
if before and after:
    (sb, mb, fb), (sa, ma, fa) = dose_summary(before), dose_summary(after)
    row = lambda k, x, y: f"<tr><td>{k}</td><td>{x}</td><td>{y}</td></tr>"
    def mm(s): return "—" if s is None else f"{s // 60}:{s % 60:02d}"
    fdb = [s["firstDecisionSeconds"] for s in mb["sittings"]]; fda = [s["firstDecisionSeconds"] for s in ma["sittings"]]
    dose_html = ("<h2>The dose, before and after</h2><p>perceptor-foundry <span class='mono'>tools/qa/dosage-audit.mjs</span> (report-only), Module 1. Estimates from content, not measured learner time."
                 " The films are unchanged.</p><table><tr><th>Module 1</th><th>1.1.0</th><th>" + esc(pkg["version"]) + "</th></tr>"
                 + row("First decision, per lesson", " · ".join(mm(x) for x in fdb), " · ".join(mm(x) for x in fda))
                 + row("Longest run of passive cards", max(s["maxPassiveRun"] for s in mb["sittings"]), max(s["maxPassiveRun"] for s in ma["sittings"]))
                 + row("Cards over 100 words before the first tap", sum(1 for s in mb["sittings"] for p in s["panes"] if p["words"] > 100), sum(1 for s in ma["sittings"] for p in s["panes"] if p["words"] > 100))
                 + row("Decisions (per 5 min, per lesson)", " · ".join(f"{s['decisions']} ({s['decisionsPer5Min']})" for s in mb["sittings"]), " · ".join(f"{s['decisions']} ({s['decisionsPer5Min']})" for s in ma["sittings"]))
                 + row("Lessons with a constructive step", sum(1 for s in mb["sittings"] if s["constructive"]), sum(1 for s in ma["sittings"] if s["constructive"]))
                 + row("Failures (rules broken)", len(fb), len(fa))
                 + row("Estimated minutes (stated 40)", mb["estimatedMinutes"], ma["estimatedMinutes"])
                 + "</table>" + sequence(before, "1.1.0, as authored") + sequence(after, f"{pkg['version']}, the re-cut")
                 + ("<p class='muted'>Remaining: " + "; ".join(esc(f"{f.get('pane', '')}: {f['msg']}") for f in fa) + ". The audit counts the action card's hidden prompt and the commitment's prefix, which the app draws only after a tap: on screen the card shows 96 words.</p>" if fa else ""))

total_s = sum(x["duration_seconds"] for x in man.values())
narr_list = "".join(f"<tr><td>{esc(x['block'])}</td><td>{x['beat']}</td><td>{x['duration_seconds']:.1f} s</td><td><audio controls preload='none' src='{esc(rel_public(x['audio_uri']))}'></audio></td><td class='path'>{esc(x['audio_uri'].split('/')[-1])}</td></tr>"
                    for x in sorted(man.values(), key=lambda x: (x["block"], x["beat"])))
v = voices.get("en", {})
flags = [(c["block"], f) for c in changes for f in c.get("flags", [])]
gates_html = ""
if gates:
    gates_html = "<h2>Gates</h2><table><tr><th>Gate</th><th>Result</th></tr>" + "".join(f"<tr><td>{esc(g['gate'])}</td><td>{esc(g['result'])}</td></tr>" for g in gates["gates"]) + "</table>"

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sitting design pilot · Module 1 review</title><style>
:root{{--paper:#F4F1E9;--panel:#FBF9F4;--ink:#1C1B2B;--muted:#66636B;--rule:#D7D2C8;--violet:#5A4BC4;--sage:#E8EBE3;--amber:#8a3b00}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font:15px/1.55 "DM Sans",-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:44px 24px 96px}} h1,h2,h3{{font-family:"Fraunces",Georgia,serif;font-weight:500}}
h1{{font-size:38px;line-height:1.1;margin:6px 0 12px}} h2{{font-size:26px;margin:52px 0 8px;padding-top:18px;border-top:1px solid var(--rule)}} h3{{font-size:19px;margin:4px 0 8px;line-height:1.3}}
.mono{{font:600 11px/1.4 "DM Mono",ui-monospace,Menlo,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:10px 0 4px}}
.lede{{max-width:820px;font-size:16px}} .muted{{color:var(--muted)}} .quote{{background:var(--panel);border:1px solid var(--rule);border-radius:2px;padding:8px 12px;margin:4px 0}}
table{{border-collapse:collapse;width:100%;margin:10px 0;font-size:14px}} th,td{{border:1px solid var(--rule);padding:6px 8px;text-align:left;vertical-align:top}} th{{background:var(--panel);font-weight:600}}
td.seq{{font:12px/1.7 "DM Mono",ui-monospace,Menlo,monospace}} .dec{{background:var(--violet);color:#fff;border-radius:2px;padding:1px 4px}} .pas{{background:#E4E0D6;border-radius:2px;padding:1px 4px}}
.chg{{padding:18px 0 22px;border-bottom:1px solid var(--rule)}} .await{{color:var(--amber)}} .why{{margin:4px 0 8px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:18px}} .beats{{padding-left:20px}} .beats li{{margin:6px 0}} pre{{white-space:pre-wrap;font-size:12px;background:var(--panel);border:1px solid var(--rule);padding:8px;border-radius:2px;max-height:360px;overflow:auto}}
.pic{{max-width:100%;border:1px solid var(--rule);border-radius:2px}} figure{{margin:12px 0}} figcaption{{color:var(--muted);font-size:13px}}
.flag{{background:#FFF6EC;border:1px solid #E7C9A6;border-radius:2px;padding:4px 14px;margin:10px 0}} .tick{{margin:10px 0 0}} .note{{min-height:40px;border-bottom:1px solid var(--rule)}}
.narr{{list-style:none;padding:0}} .narr li{{margin:8px 0}} audio{{width:100%;max-width:420px}} .path{{font:11px "DM Mono",ui-monospace,Menlo,monospace;color:var(--muted);word-break:break-all}}
.panel{{background:var(--panel);border:1px solid var(--rule);border-radius:2px;padding:14px 18px;margin:16px 0}}
@media(max-width:820px){{.two{{grid-template-columns:1fr}} main{{padding:28px 16px 64px}} h1{{font-size:30px}}}}
</style></head><body><main>
<p class="mono">Hormones and Peptides for Skin · package {esc(pkg['version'])} · DRAFT · awaiting Dr. Fady Hannah-Shmouni and Omar Saleem</p>
<h1>Module 1, re-cut in the sitting design</h1>
<p class="lede">The live course is 1.1.0 and stays live. This draft changes Module 1 only: where the decisions fall, how the explanations read
and sound, and three exercises. The films are unchanged. Every change below is built from sentences you have already approved, and
stays open until you confirm it. Nothing reaches learners before both sign-offs.</p>
<div class="panel"><p class="mono">Omar, 2026-09-28</p>{''.join(f'<p>“{esc(q)}”</p>' for q in quotes)}
<p class="muted">Approved: the dosage rules as audited defaults; the read-along explain card in place of the flip-card audio story, piloted here;
films unchanged; move and reason (twotier) and the evidence ladder built first; Gemini 3.8 TTS for every narrated card (films keep their audio).</p></div>
<div class="panel"><p class="mono">How to review</p><ul>
<li><b>Dr. Hannah-Shmouni:</b> each change: is every sentence right, and at the level it is stated? Read the “For your decision” boxes first ({len(flags)} items). Tick “correct as written” or note the change.</li>
<li><b>Omar:</b> the journey and dose tables, the focus regions on each picture, and the narration (players below; open this file from the branch so the players find the audio).</li>
<li>Reply with the moment id (for example <span class="mono">m1-p15</span>) and “confirm” or “change: …”.</li></ul></div>
{dose_html}
<h2>For your decision ({len(flags)})</h2><ol>{''.join(f'<li><b>{esc(b)}</b>: {esc(f)}</li>' for b, f in flags)}</ol>
<h2>Every change ({len(changes)})</h2>
{''.join(change_card(c) for c in changes)}
<h2>Media preview: the new narration ({len(man)} beats, {total_s:.0f} s)</h2>
<p>Gemini 3.8 Flash TTS (<span class="mono">{esc(v.get('model', ''))}</span>), voice <span class="mono">{esc(v.get('voice_id', ''))}</span>, the voice and delivery of the module opening films:
“{esc(v.get('style', ''))}” Loudness −16 LUFS as heard; word timings aligned to each beat's own text (ElevenLabs Scribe). Drafts until the media preview.
The films keep their approved audio. Before this, these cards were narrated on demand by ElevenLabs “Alice” from their audio-story scripts.</p>
<table><tr><th>Moment</th><th>Beat</th><th>Length</th><th>Listen</th><th>File</th></tr>{narr_list}</table>
<p class="muted">Files: public/assets/hormones-peptides-skin/narration/readalong/&lt;moment&gt;/b&lt;n&gt;.en.&lt;sha8&gt;.mp3 (and .json word timings); cache: course-production/hormones-peptides-skin/narration/readalong-manifest.json.</p>
<h2>Focus regions ({len(media) - sum(1 for m in media if 'narration' in m['change'])} pictures)</h2>
<ul>{''.join(f"<li><b>{esc(m['block'])}</b>: {esc(m['change'])}</li>" for m in media if 'narration' not in m['change'])}</ul>
{gates_html}
<p class="path">Generated by course-production/hormones-peptides-skin/review/make-sitting-pilot-review.py from authored/m01.json, course-production/dosage/ and the narration manifest.</p>
</main></body></html>"""
OUT_HTML.write_text(page)
print(f"✓ {OUT_HTML.relative_to(ROOT)} ({OUT_HTML.stat().st_size / 1e6:.1f} MB, {len(changes)} changes, {len(man)} narration files)")

# ------------------------------------------------------------------ .docx (pandoc; audio listed, pictures embedded)
if shutil.which("pandoc"):
    md = [f"# Module 1, re-cut in the sitting design\n",
          f"*Hormones and Peptides for Skin · package {pkg['version']} · DRAFT · awaiting Dr. Fady Hannah-Shmouni and Omar Saleem. The live course (1.1.0) is unchanged; nothing reaches learners before both sign-offs. The films are unchanged.*\n",
          "**Omar, 2026-09-28:** " + " / ".join(f"“{q}”" for q in quotes) + "\n",
          "**How to reply:** the moment id and “confirm” or “change: …”.\n"]
    if before and after:
        md.append("## The dose, before and after (Module 1)\n")
        md.append("| | 1.1.0 | " + pkg["version"] + " |\n|---|---|---|")
        md.append(f"| First decision per lesson | {' · '.join(mm(x) for x in fdb)} | {' · '.join(mm(x) for x in fda)} |")
        md.append(f"| Longest passive run | {max(s['maxPassiveRun'] for s in mb['sittings'])} | {max(s['maxPassiveRun'] for s in ma['sittings'])} |")
        md.append(f"| Cards over 100 words | {sum(1 for s in mb['sittings'] for p in s['panes'] if p['words'] > 100)} | {sum(1 for s in ma['sittings'] for p in s['panes'] if p['words'] > 100)} |")
        md.append(f"| Failures | {len(fb)} | {len(fa)} |\n")
        for rep, lab in ((before, "1.1.0"), (after, pkg["version"])):
            m = next(m for m in rep["modules"] if m["id"] == "m01")
            md.append(f"**{lab}:** " + " / ".join(f"{s['id']}: " + " › ".join(("**" + p['id'].replace('m1-', '') + "**") if p["decision"] else p["id"].replace("m1-", "") for p in s["panes"]) for s in m["sittings"]) + "  (bold = decision)\n")
    md.append(f"## For your decision ({len(flags)})\n")
    md += [f"{i}. **{b}**: {f}" for i, (b, f) in enumerate(flags, 1)] + [""]
    md.append(f"## Every change ({len(changes)})\n")
    for c in changes:
        bid = c["block"].split(",")[0].strip()
        md.append(f"### {c['block']} · {c['change']}\n")
        md.append(f"*For {c['forReview']} · awaiting confirmation · {c['date']}*  \n**Why.** {c['reason']}\n")
        if bid in B and (B[bid].get("metadata") or {}).get("presentation") == "readalong" and isinstance(c.get("after"), list):
            md.append("**Before (flip-card chapters):**\n")
            md += [f"{i}. **{x['title']}** — {x['body']}" for i, x in enumerate(c["before"], 1)] + [""]
            md.append("**After (read-along beats):**\n")
            md += [f"{i}. **{x['title']}** — {x['body']}  \n   *Key terms:* {' · '.join(x.get('keyTerms', []))}" for i, x in enumerate(c["after"], 1)] + [""]
            md.append(f"![]({focus_picture(bid)}){{width=6in}}\n")
            md.append("**Narration:** " + "; ".join(f"beat {x['beat']} {x['duration_seconds']:.1f} s (public/{x['audio_uri']})" for x in sorted((x for x in man.values() if x['block'] == bid), key=lambda x: x['beat'])) + "\n")
        else:
            for k in ("before", "after"):
                if c.get(k) is not None:
                    val = c[k] if isinstance(c[k], str) else json.dumps(c[k], ensure_ascii=False, indent=1)
                    md.append(f"**{k.title()}:**\n\n" + (f"> {val}\n" if isinstance(c[k], str) else f"```\n{val}\n```\n"))
        for k, lab in (("sources", "Built from"), ("carriedElsewhere", "What left this card, and where the module still teaches it"), ("flags", "For your decision")):
            if c.get(k): md.append(f"**{lab}:**\n\n" + "\n".join(f"- {s}" for s in c[k]) + "\n")
        md.append("☐ Correct as written  ☐ Change: ______________________\n")
    md.append(f"## Media preview: the new narration ({len(man)} beats, {total_s:.0f} s)\n")
    md.append(f"Gemini 3.8 Flash TTS, voice {v.get('voice_id', '')} (the films' voice and delivery), −16 LUFS as heard, word timings per beat. Drafts until the media preview; the films keep their audio.\n")
    md += [f"- {x['block']} beat {x['beat']} · {x['duration_seconds']:.1f} s · public/{x['audio_uri']}" for x in sorted(man.values(), key=lambda x: (x['block'], x['beat']))] + [""]
    if gates:
        md.append("## Gates\n")
        md += [f"- **{g['gate']}:** {g['result']}" for g in gates["gates"]] + [""]
    src = tmp / "sitting-pilot-m01.md"; src.write_text("\n".join(md))
    subprocess.run(["pandoc", str(src), "-o", str(OUT_DOCX), "--resource-path", str(tmp)], check=True)
    print(f"✓ {OUT_DOCX.relative_to(ROOT)} ({OUT_DOCX.stat().st_size / 1e6:.1f} MB)")
shutil.rmtree(tmp)
