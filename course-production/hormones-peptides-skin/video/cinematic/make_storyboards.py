"""Module 2–7 opener storyboards (cinematic/1), written from each module's approved text only. Same look and rules as the Module 1
opener: HeyGen Avatar V presenter bookends (no on-screen label; disclosure under the player), text-free plates spotlit and labelled
as the narration names things, lists with a two-edge indicator, kinetic type over footage, ducked Lyria score."""
import json, re, sys
from pathlib import Path

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
AUTH = Path(sys.argv[2])

def blocks(m):
    d = json.loads((AUTH / f"m0{m}.json").read_text())
    return {b["id"]: b for b in d["blocks"]}

def en(x): return x.get("en", "") if isinstance(x, dict) else (x or "")
def sentences(t): return [s.strip() for s in re.split(r"(?<=[.?!])\s+(?=[A-Z])", t.strip()) if s.strip()]

def script(m, parts):
    """parts: [(block id, 'body'|'audio', [sentence numbers, 1-based])] → text + sources, verbatim approved sentences only."""
    B = blocks(m); text = []; src = []
    for bid, field, nums in parts:
        s = sentences(en(B[bid]["body"]) if field == "body" else en((B[bid].get("metadata") or {}).get("audioScript")))
        text += [s[n - 1] for n in nums]
        src.append(f"{bid} {'body' if field == 'body' else 'audioScript'}, sentences {', '.join(map(str, nums))}")
    return " ".join(text), src

VOICE = {"provider": "gemini-tts", "voice_id": "en-gb-tutor-1", "name": "Gemini 3.8 TTS · en-gb-tutor-1 (Omar's pick 2026-09-25)",
         "style": "Warm, clear and precise clinical educator speaking to physicians. Natural, unhurried pace. Pronounce every medical and chemical term carefully and confidently."}
PRESENTER = {"look": "2daeb4c1c74e491c89314a4e7dcd4879", "engine": "avatar_v", "resolution": "4k",
             "name": "HeyGen stock avatar \"Iris\" (licensed)", "disclosure": {"en": "Presented by a digital avatar (AI-generated presenter and voice)."}}
def score(seconds, mood): return {"src": "score.mp3", "kind": "music", "prompt": f"Instrumental underscore for a {seconds}-second medical education film opener about {mood}: calm, precise and modern; soft felt piano motif over warm analogue synth pads, a light pulse at 96 BPM entering after 10 seconds, gentle build to a lift two thirds of the way through, resolving softly at the end; documentary feel, same palette as the series, no vocals, no heavy drums, leave space for narration."}
def presenter_state(sid, on, frm, to, kinetic, at=None, zoom=(1.0, 1.07)):
    st = {"id": sid, "shape": {"kind": "frame", "fill": "ink"}, "content": {"video": {"presenter": {"from": frm, "to": to}, "focus": [0.5, 0.36], "zoom": list(zoom)}}, "kinetic": kinetic}
    st.update({"at": at} if at is not None else {"on": on}); return st
def lessons(on, kicker, rows, steps):
    out = [{"id": "lessons", "on": on, "shape": {"kind": "panel", "fill": "card"}, "list": {"kicker": kicker, "rows": [{"label": r, "marks": 0} for r in rows]}}]
    for i, (o, tag) in enumerate(steps): out.append({"id": f"l{i+1}", "on": o, "indicator": {"rows": [i, i], "tag": tag}})
    return out
def plate(sid, on, src, regions, focus, h=1280): return {"id": sid, "on": on, "shape": {"kind": "window", "fill": "paper", "h": h}, "kinetic": None, "content": {"image": {"src": src, "regions": regions, "focus": focus}}}
def broll(sid, on, src, kinetic, focus=(0.5, 0.55), zoom=(1.0, 1.12)): return {"id": sid, "on": on, "shape": {"kind": "frame", "fill": "ink"}, "content": {"video": {"src": src, "focus": list(focus), "zoom": list(zoom)}}, "kinetic": kinetic}

FILMS = {}

# ── Module 2 · Systemic hormones and the skin ──────────────────────────────────────────────────────────────────────────────
t, s = script(2, [("m2-p01", "body", [1, 2, 3]), ("m2-p02", "audio", [1, 2, 3, 4, 5, 6, 7])])
FILMS[2] = {"kicker": "MODULE 02 · SYSTEMIC HORMONES AND THE SKIN", "script": t, "sources": s, "mood": "the skin's own stress hormones", "seconds": 85,
  "assets": [
    {"src": "m2-axis.png", "kind": "image", "candidates": 2, "prompt": "Accurate scientific medical illustration plate with two vignettes stacked vertically, the same width, generous empty paper between and around them. Top vignette, the classic stress axis: a small side-view outline of the brain with the hypothalamus and the pituitary gland highlighted, a fine blood vessel running down to a kidney with its adrenal gland on top. Bottom vignette, the skin's own stress axis: a close-up cross-section of the epidermis over the upper dermis; a few skin cells release tiny violet signal molecules to their neighbours, and one cell in the middle is highlighted, turning pale inactive hormone particles into bright violet active ones inside it."},
    {"src": "m2-dermis.png", "kind": "image", "candidates": 2, "prompt": "Accurate scientific medical illustration plate: two vertical cross-section blocks of aged skin side by side, same width and height, generous empty paper between and around them. Each block shows the epidermis, the dermis with wavy collagen fibre bundles and a few spindle-shaped fibroblasts, and fat at the bottom. In the left block the dermis is visibly thinner, its collagen bundles sparse and fine. In the right block the dermis is visibly thicker, with dense, well-organised collagen bundles. The two blocks are otherwise identical."},
    {"src": "m2-broll-sun.mp4", "kind": "video", "prompt": "Extreme macro cinematography of sun-exposed, gently lined skin on the back of an older adult's hand: fine texture, light freckling and soft creases catching warm late-afternoon raking light, a very slow smooth push-in, shallow depth of field, calm and respectful, warm neutral grade, no face, no jewellery, no text, no logos."},
    score(85, "the skin's own stress hormones"),
  ],
  "states": [
    presenter_state("intro", None, "Most skin changes", "endocrine disease", [{"on": "ageing or lifestyle", "text": "Ageing or lifestyle"}, {"on": "endocrine disease", "text": "…or endocrine disease"}], at=0),
    *lessons("In three lessons", "Three lessons", ["What hormones do to skin", "What hormone therapy can do", "Signs for an endocrinologist"],
             [("local and systemic hormones", None), ("what hormone therapy can", None), ("which signs belong", None)]),
    {"id": "l4", "on": "with an endocrinologist", "indicator": {"rows": [2, 2], "tag": "Refer these"}},
    plate("axis", "Picture the skin", "m2-axis.png",
          {"adrenal": "the top vignette: the brain, pituitary, blood vessel and the kidney with its adrenal gland", "skin": "the bottom vignette: the strip of skin cells releasing violet signal molecules", "cell": "the single highlighted cell in the middle of the bottom vignette"},
          [{"on": "its own stress axis", "region": "skin", "label": "The skin's own stress axis"},
           {"on": "make CRH and ACTH", "region": "skin", "label": "CRH · ACTH"},
           {"on": "drive the adrenal glands", "region": "adrenal", "label": "The adrenal axis"},
           {"on": "respond to them", "region": "skin", "label": "…and their receptors"},
           {"on": "eleven beta HSD one", "region": "cell", "label": "11β-HSD1", "zoom": 1.4},
           {"on": "active cortisol", "region": "cell", "label": "Cortisone → cortisol", "zoom": 1.4}]),
    broll("sun", "In human skin samples", "m2-broll-sun.mp4", [{"on": "works harder with age", "text": "Higher with age"}, {"on": "sun-exposed skin", "text": "and in sun-exposed skin"}, {"on": "independently of the level", "text": "Independent of blood levels"}]),
    plate("dermis", "Cortisol slows collagen", "m2-dermis.png",
          {"thin": "the left skin block with the thinner dermis", "thick": "the right skin block with the thicker dermis"},
          [{"on": "slows collagen production", "region": "thin", "label": "Cortisol: less collagen"},
           {"on": "mice bred without", "region": "thick", "label": "No enzyme (mice): dermis kept"}]),
    presenter_state("close", "Hold all of this", "Hold all of this", "face will age", [{"on": "mechanism register", "text": "The mechanism register"}, {"on": "biopsies", "text": "Biopsies · cells · mice"}], zoom=(1.04, 1.1)),
  ]}

# ── Module 3 · Fat, incretins and the ageing face ─────────────────────────────────────────────────────────────────────────
t, s = script(3, [("m3-p01", "body", [1, 2]), ("m3-p02", "audio", [1, 2, 3, 4, 5, 6, 7, 8, 9])])
FILMS[3] = {"kicker": "MODULE 03 · FAT, INCRETINS AND THE AGEING FACE", "script": t, "sources": s, "mood": "fat in and under the skin", "seconds": 80,
  "assets": [
    {"src": "m3-fat-layers.png", "kind": "image", "candidates": 2, "prompt": "Accurate scientific medical illustration: a vertical cross-section block of human skin seen slightly from the side like a textbook plate, centred with generous empty margins. From top to bottom: the epidermis, the papillary and reticular dermis with wavy collagen bundles, and a thick subcutaneous fat layer of rounded yellow fat lobules. Two hair follicles run down through the dermis, and around the lower part of each follicle sits a small cone of fat cells. Inside the lowest part of the reticular dermis runs a distinct thin band of fat cells, separate from the subcutaneous fat below it."},
    {"src": "m3-defence.png", "kind": "image", "candidates": 2, "prompt": "Accurate scientific medical illustration: a close-up round vignette of the lower dermis during a skin infection, centred with generous empty margins. On one side, grape-like clusters of small round bacteria (Staphylococcus aureus). Beside them, a group of newly formed small fat cells, each with a single pale lipid droplet, releases a haze of tiny violet antimicrobial peptide molecules toward the bacteria. Collagen fibres in the background."},
    score(80, "fat in and under the skin"),
  ],
  "states": [
    presenter_state("intro", None, "Facial shape depends", "on collagen", [{"on": "on fat", "text": "Fat"}, {"on": "as much as on collagen", "text": "as much as collagen"}], at=0),
    *lessons("In three lessons", "Three lessons", ["The skin's own fat", "Sugar damage to the dermis", "Weight-loss drugs and the gut"],
             [("the skin's own fat", None), ("sugar damage", None), ("weight-loss drugs", None)]),
    {"id": "l4", "on": "what is still mechanism", "indicator": {"rows": [0, 2], "tag": None}},
    plate("layers", "Most people picture", "m3-fat-layers.png",
          {"subcut": "the thick bottom layer of yellow fat lobules under the dermis", "dwat": "the thin band of fat cells inside the lowest part of the dermis, above the thick fat layer", "cone": "the small cone of fat cells around the lower part of one hair follicle"},
          [{"on": "one layer under the dermis", "region": "subcut", "label": "Subcutaneous fat"},
           {"on": "a second, thinner layer", "region": "dwat", "label": "A second, thinner layer", "zoom": 1.3},
           {"on": "dermal white adipose tissue", "region": "dwat", "label": "Dermal white adipose tissue", "zoom": 1.45}]),
    plate("defence", "In mice, this layer", "m3-defence.png",
          {"bacteria": "the grape-like clusters of small round bacteria", "fat": "the group of small fat cells releasing violet molecules"},
          [{"on": "Staphylococcus aureus", "region": "bacteria", "label": "S. aureus (mice)"},
           {"on": "release cathelicidin", "region": "fat", "label": "Cathelicidin"},
           {"on": "Older mice lose", "region": "fat", "label": "Lost with age · TGF-β"}], h=1100),
    plate("cones", "Human skin arranges", "m3-fat-layers.png",
          {"subcut": "the thick bottom layer of yellow fat lobules under the dermis", "dwat": "the thin band of fat cells inside the lowest part of the dermis, above the thick fat layer", "cone": "the small cone of fat cells around the lower part of one hair follicle"},
          [{"on": "small cones around hair follicles", "region": "cone", "label": "Cones around follicles (human)", "zoom": 1.4},
           {"on": "human acne lesions", "region": "cone", "label": "Acne: preadipocytes · cathelicidin", "zoom": 1.4},
           {"on": "What the layer contributes", "region": "dwat", "label": "Its part in human ageing?", "zoom": 1.2},
           {"on": "has not yet been measured", "zoom": 1}]),
    presenter_state("close", "So hold two things apart", "So hold two things apart", "still a proposal", [{"on": "defence story", "text": "Defence: strong in mice"}, {"on": "ageing story", "text": "Ageing: a proposal"}], zoom=(1.04, 1.1)),
  ]}

# ── Module 4 · Matrix peptides and wound healing ──────────────────────────────────────────────────────────────────────────
t, s = script(4, [("m4-p01", "body", [1, 2]), ("m4-p03", "audio", [1, 2, 3, 4, 5, 6, 7, 8])])
FILMS[4] = {"kicker": "MODULE 04 · MATRIX PEPTIDES AND WOUND HEALING", "script": t, "sources": s, "mood": "matrix peptides and the evidence behind them", "seconds": 78,
  "assets": [
    {"src": "m4-ghk.png", "kind": "image", "candidates": 2, "prompt": "Schematic scientific illustration of a tripeptide, deliberately NOT a chemical structure: no atoms, no bonds, no rings, no ball-and-stick, no letters. Upper group, centred: three large smooth matte spheres of slightly different warm tones joined in a short gently curved row like beads on a fine thread, and a single smaller burnished copper-coloured sphere cradled between the second and the third bead, held there by two fine lines. Lower group, smaller, for comparison: the same three beads on their own with no copper sphere. Generous empty paper around both groups."},
    {"src": "m4-matrix.png", "kind": "image", "candidates": 2, "prompt": "Accurate scientific medical illustration: a close-up round vignette of the dermal extracellular matrix, centred with generous empty margins. A spindle-shaped fibroblast lies among wavy collagen fibre bundles and fine elastin fibres; tiny copper-coloured ions are delivered to small enzyme shapes that sit where neighbouring collagen fibres are being cross-linked, the cross-links drawn as short violet bridges between fibres."},
    score(78, "matrix peptides and the evidence behind them"),
  ],
  "states": [
    presenter_state("intro", None, "Most skin peptides", "any evidence does", [{"on": "reach your clinic", "text": "In your clinic"}, {"on": "before any evidence", "text": "before the evidence"}], at=0),
    *lessons("In three lessons", "Three lessons", ["What the human trials show", "Who paid for them", "Where the regulator stands"],
             [("what the human trials", None), ("who paid", None), ("where each one stands", None)]),
    plate("molecule", "Start with the molecule", "m4-ghk.png",
          {"peptide": "the lower three-residue chain without copper", "complex": "the upper three-residue chain holding the copper-coloured sphere", "copper": "the single copper-coloured sphere"},
          [{"on": "three-amino-acid peptide", "region": "peptide", "label": "GHK · Gly-His-Lys"},
           {"on": "first described in 1973", "region": "peptide", "label": "Human plasma · 1973"},
           {"on": "binds copper", "region": "copper", "label": "Copper", "zoom": 1.4},
           {"on": "copper complex", "region": "complex", "label": "GHK-Cu"},
           {"on": "skin-care labels", "region": "complex", "label": "“Copper peptide” on labels", "zoom": 1.2}]),
    plate("matrix", "The proposed mechanism", "m4-matrix.png",
          {"crosslinks": "the violet bridges between neighbouring collagen fibres and the small enzyme shapes at them", "fibroblast": "the spindle-shaped fibroblast"},
          [{"on": "delivers copper to enzymes", "region": "crosslinks", "label": "Copper to matrix enzymes", "zoom": 1.15},
           {"on": "lysyl oxidase", "region": "crosslinks", "label": "Lysyl oxidase · cross-links", "zoom": 1.3},
           {"on": "superoxide dismutase", "region": "fibroblast", "label": "Superoxide dismutase"},
           {"on": "toward wound healing", "zoom": 1, "label": None}], h=1100),
    presenter_state("close", "Two things to hold on to", "Two things to hold on to", "reach the trials", [{"on": "this is a mechanism", "text": "1 · A mechanism"}, {"on": "leaves open whether it does", "text": "Whether it works: open"}, {"on": "the group that discovered", "text": "2 · Written by its discoverers"}], zoom=(1.04, 1.1)),
  ]}

# ── Module 5 · Follicle, pigment and melanocortins ────────────────────────────────────────────────────────────────────────
t, s = script(5, [("m5-p01", "body", [1, 2]), ("m5-p02", "audio", [1, 2, 3, 5, 8])])
FILMS[5] = {"kicker": "MODULE 05 · FOLLICLE, PIGMENT AND MELANOCORTINS", "script": t, "sources": s, "mood": "the hair follicle as a small gland", "seconds": 78,
  "assets": [
    {"src": "m5-follicle.png", "kind": "image", "candidates": 2, "prompt": "Accurate scientific medical illustration: a single growing human scalp hair follicle in longitudinal section, centred with generous empty margins, like a textbook plate: the hair shaft, the inner and outer root sheaths, the sebaceous gland, and at the base the onion-shaped hair bulb cupping the dermal papilla. Along the outer root sheath, tiny violet signal molecules are released, travel down to the bulb, and a fine dotted violet loop returns from the bulb back up to the outer root sheath."},
    {"src": "m5-miniaturisation.png", "kind": "image", "candidates": 2, "prompt": "Accurate scientific medical illustration: three human scalp hair follicles in longitudinal section standing side by side at the same scale, centred with generous empty margins, showing progressive miniaturisation from left to right: a large deep terminal follicle with a thick pigmented hair, a mid-sized follicle with a thinner hair, and a small shallow miniaturised follicle with a fine, short, pale vellus-like hair. Same dermis and scalp surface line across all three."},
    score(78, "the hair follicle as a small gland"),
  ],
  "states": [
    presenter_state("intro", None, "Two requests reach", "injection to tan", [{"on": "regrow hair", "text": "A peptide to regrow hair"}, {"on": "injection to tan", "text": "An injection to tan"}], at=0),
    *lessons("In three lessons", "Three lessons", ["Follicle and pigment hormones", "Approved vs gray-market", "Grading hair peptides"],
             [("the follicle and the pigment system", None), ("one melanocortin drug", None), ("how to grade", None)]),
    plate("follicle", "Each hair follicle behaves", "m5-follicle.png",
          {"sheath": "the outer root sheath along the side of the follicle where violet molecules are released", "bulb": "the onion-shaped hair bulb and dermal papilla at the base", "loop": "the dotted violet loop returning from the bulb"},
          [{"on": "a small gland", "region": "bulb", "label": "A small gland"},
           {"on": "alive in culture", "zoom": 1},
           {"on": "corticotropin-releasing hormone", "region": "sheath", "label": "CRH"},
           {"on": "ACTH and alpha-MSH", "region": "bulb", "label": "ACTH · α-MSH · cortisol", "zoom": 1.3},
           {"on": "feed back", "region": "loop", "label": "Feedback"}]),
    plate("dht", "On the scalp", "m5-miniaturisation.png",
          {"terminal": "the large deep follicle on the left with a thick hair", "small": "the small shallow follicle on the right with a fine short hair"},
          [{"on": "five-alpha-reductase", "region": "terminal", "label": "5α-reductase"},
           {"on": "into dihydrotestosterone", "region": "terminal", "label": "Testosterone → DHT"},
           {"on": "genetically susceptible", "region": "small", "label": "Susceptible follicles"},
           {"on": "gradual shrinking", "region": "small", "label": "Miniaturisation", "zoom": 1.3}], h=1000),
    presenter_state("close", "Most of this biology", "Most of this biology", "matter in patients", [{"on": "outside the body", "text": "Tissue outside the body"}, {"on": "hold it as mechanism", "text": "Hold it as mechanism"}], zoom=(1.04, 1.1)),
  ]}

# ── Module 6 · The growth-hormone axis and the skin ───────────────────────────────────────────────────────────────────────
t, s = script(6, [("m6-p01", "body", [1, 2, 3]), ("m6-p02", "audio", [1, 2, 3, 4, 5, 7, 8, 9, 10])])
FILMS[6] = {"kicker": "MODULE 06 · THE GROWTH-HORMONE AXIS AND THE SKIN", "script": t, "sources": s, "mood": "growth hormone, IGF-1 and two layers of skin", "seconds": 85,
  "assets": [
    {"src": "m6-two-layers.png", "kind": "image", "candidates": 2, "prompt": "Accurate scientific medical illustration: a vertical cross-section of human skin centred with generous empty margins, like a textbook plate: the stratified epidermis of keratinocytes on top, some of them dividing, and below it the dermis with wavy collagen bundles, several spindle-shaped fibroblasts and a small blood capillary. Pale grey-blue hormone particles leave the capillary and reach the fibroblasts; the fibroblasts release tiny violet particles that rise to the keratinocytes at the base of the epidermis."},
    {"src": "m6-broll-mature.mp4", "kind": "video", "prompt": "Extreme macro cinematography of mature skin texture on the outer upper arm of an older adult: fine crepey lines and soft folds catching warm window light, a very slow smooth push-in, shallow depth of field, calm and clinical. Only skin fills the frame: no face, no mouth, no lips, no eyes, no hands, no fingernails, no jewellery, no clothing, no text, no logos."},
    score(85, "skin biology, second in a calm series"),
  ],
  "states": [
    presenter_state("intro", None, "Growth hormone and IGF-1", "much less behind it", [{"on": "approval-grade trials", "text": "One peptide: approval-grade trials"}, {"on": "much less behind it", "text": "Most: much less"}], at=0),
    *lessons("In three lessons", "Three lessons", ["Physiology vs promise", "Approved vs anecdotal", "Visible effects vs unmeasured risks"],
             [("the physiology from the promise", None), ("the approved from the anecdotal", None), ("the side-effects you can see", None)]),
    {"id": "l4", "on": "the risks nobody has measured", "indicator": {"rows": [2, 2], "tag": None}},
    plate("layers", "Two layers of skin", "m6-two-layers.png",
          {"dermis": "the dermis with the spindle-shaped fibroblasts and collagen", "epidermis": "the epidermis of keratinocytes on top", "capillary": "the small blood capillary in the dermis"},
          [{"on": "two different parts", "region": "capillary", "label": "One axis, two hormones"},
           {"on": "speaks mainly to the dermis", "region": "dermis", "label": "Growth hormone → dermis"},
           {"on": "expressed more on fibroblasts", "region": "dermis", "label": "GH receptor: mainly fibroblasts"},
           {"on": "fibroblast numbers", "region": "dermis", "label": "More fibroblasts", "zoom": 1.25},
           {"on": "supports collagen synthesis", "region": "dermis", "label": "Collagen synthesis", "zoom": 1.25},
           {"on": "sometimes through IGF-1", "region": "dermis", "label": "Directly, or through IGF-1", "zoom": 1.1},
           {"on": "The epidermis listens", "region": "epidermis", "label": "IGF-1 → epidermis"},
           {"on": "carry the IGF-1 receptor", "region": "epidermis", "label": "IGF-1 receptor"},
           {"on": "neighbours in the dermis supply", "region": "dermis", "label": "Supplied by the dermis"},
           {"on": "keratinocytes divide", "region": "epidermis", "label": "Keratinocytes divide", "zoom": 1.3}]),
    broll("age", "With age", "m6-broll-mature.mp4", [{"on": "fall steadily", "text": "GH and IGF-1 fall with age"}, {"on": "the somatopause", "text": "The somatopause"}]),
    presenter_state("close", "Hold all of this as mechanism", "Hold all of this as mechanism", "trials answer it", [{"on": "could matter for skin", "text": "Why it could matter"}, {"on": "the trials answer it", "text": "Whether it helps: the trials"}], zoom=(1.04, 1.1)),
  ]}

# ── Module 7 · Evidence, regulation and compliance ────────────────────────────────────────────────────────────────────────
t, s = script(7, [("m7-p01", "body", [1, 2]), ("m7-p02", "audio", [1, 2, 3, 4, 5, 6, 8, 9, 10])])
FILMS[7] = {"kicker": "MODULE 07 · EVIDENCE, REGULATION AND COMPLIANCE", "script": t, "sources": s, "mood": "grading evidence and the rules around it", "seconds": 85,
  "assets": [score(85, "careful clinical reasoning, the series finale")],
  "states": [
    presenter_state("intro", None, "This last module", "three habits", [{"on": "three habits", "text": "Three habits"}], at=0),
    *lessons("You will rate", "Three habits", ["Grade the certainty", "Read the status and the certificate", "Write the consent and chart note"],
             [("rate the certainty", None), ("read a compounding status", None)]),
    {"id": "coa", "on": "certificate of analysis", "indicator": {"rows": [1, 1], "tag": None}},
    {"id": "l3", "on": "write the consent", "indicator": {"rows": [2, 2], "tag": None}},
    {"id": "unapproved", "on": "an unapproved product needs", "indicator": {"rows": [2, 2], "tag": None}},
    {"id": "hidden", "on": "Every claim you hear", "shape": {"kind": "card", "fill": "card"}, "content": {"kicker": "Every claim about a skin peptide", "display": "carries a hidden question"}},
    {"id": "sure", "on": "How sure", "shape": {"kind": "card", "fill": "card"}, "content": {"kicker": "The hidden question", "display": "How sure can we be?"}},
    {"id": "levels", "on": "four levels", "shape": {"kind": "panel", "fill": "card"}, "list": {"kicker": "GRADE · certainty of evidence", "rows": [{"label": "High", "marks": 4}, {"label": "Moderate", "marks": 3}, {"label": "Low", "marks": 2}, {"label": "Very low", "marks": 1}]}},
    {"id": "high", "on": "from high", "indicator": {"rows": [0, 0], "tag": None}},
    {"id": "low", "on": "to very low", "indicator": {"rows": [3, 3]}},
    {"id": "outcome", "on": "The rating belongs", "indicator": False, "chips": [{"id": "outcome", "place": "above", "text": "One outcome · wrinkle depth at 12 weeks", "on": "wrinkle depth"}]},
    {"id": "not", "on": "never to a single study", "chips": [{"id": "study", "place": "below", "text": "a single study", "strike": True}, {"id": "molecule", "place": "below", "text": "the molecule itself", "strike": True, "on": "the molecule"}]},
    {"id": "rct", "on": "Randomized trials", "indicator": {"rows": [0, 0], "tag": "Randomized trials"}, "drop": ["outcome", "study", "molecule"]},
    {"id": "obs", "on": "observational studies", "indicator": {"rows": [2, 2], "tag": "Observational studies"}},
    {"id": "startlow", "on": "start low", "indicator": {"rows": [2, 2], "tag": "…start low"}},
    {"id": "drops", "on": "certainty drops", "indicator": {"rows": [3, 3], "tag": "Rated down"}, "chips": [
        {"id": "r1", "place": "below", "icon": "down", "text": "Risk of bias", "on": "risk of bias"},
        {"id": "r2", "place": "below", "icon": "down", "text": "Inconsistency", "on": "inconsistency between"},
        {"id": "r3", "place": "below", "icon": "down", "text": "Indirectness", "on": "indirectness"},
        {"id": "r4", "place": "below", "icon": "down", "text": "Imprecision", "on": "imprecision"},
        {"id": "r5", "place": "below", "icon": "down", "text": "Publication bias", "on": "publication bias"}]},
    {"id": "letters", "on": "A to D", "letters": ["A", "B", "C", "D"], "indicator": False, "drop": ["r1", "r2", "r3", "r4", "r5"]},
    {"id": "same", "on": "same four levels", "chips": [{"id": "same", "place": "above", "text": "The same four levels, adapted"}]},
    presenter_state("close", "They rate the evidence", "They rate the evidence", "a product is legal", [{"on": "for that use", "text": "Evidence for that use"}, {"on": "whether a product is legal", "text": "…not whether it is legal"}], zoom=(1.04, 1.1)),
  ]}

for m, f in FILMS.items():
    sb = {"format": "cinematic/1", "id": f"m0{m}-opener", "title": f"Module {m:02d} opener — Hormones and Peptides for Skin",
          "note": "Module opener in the cinematic lane (docs/motion-contract.md § 10b), same look and rules as the Module 1 opener. Script assembled only from approved text (sources below); presenter lines pass the course script review; draft media until the media preview.",
          "script": {"text": f["script"], "sources": f["sources"], "locale": "en"}, "voice": VOICE, "presenter": PRESENTER,
          "music": {"src": "score.mp3", "lufs": -22}, "chrome": {"kicker": f["kicker"]}, "lead": 0.12,
          "assets": [{**a, "src": a["src"]} for a in f["assets"]], "states": f["states"]}
    # the score is per film: name it after the film so films can share one media folder
    for a in sb["assets"]:
        if a["kind"] == "music": a["src"] = f"m0{m}-score.mp3"
    sb["music"]["src"] = f"m0{m}-score.mp3"
    for st in sb["states"]:
        for fo in (st.get("content", {}).get("image", {}) or {}).get("focus", []) or []:
            if fo.get("label", 1) is None: fo.pop("label")
    if m == 7:
        for st in sb["states"]:
            if st["id"] == "close": st["drop"] = ["same"]
    (OUT / f"m0{m}-opener.storyboard.json").write_text(json.dumps(sb, indent=2, ensure_ascii=False) + "\n")
    print(f"m0{m}: {len(f['script'].split())} words, {len(sb['states'])} states, {len(sb['assets'])} assets")
