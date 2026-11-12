#!/usr/bin/env python3
"""Offline check of audio-beats-proposal.json against the package it was drafted from.

agent pre-review — no gate opened. Standard library only; no network. Reads the package, never writes it.

  python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-12/validate_proposal.py
  python3 .../validate_proposal.py --emit-applied /tmp/preview.json   # patched COPY for a dry-run check, outside the repo

Exit 0 when every check passes, 1 otherwise.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
EXPECTED_IDS = {"m4-p06", "m4-p11"}
BANNER = "agent pre-review — no gate opened"
MAX_WORDS, MIN_BEATS, MAX_BEATS = 35, 2, 4
FIELDS = {"body.en": lambda b: b["body"]["en"], "metadata.audioScript.en": lambda b: b["metadata"]["audioScript"]["en"]}

failures = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        failures.append(msg)
    return ok


def sha(data):
    return hashlib.sha256(data).hexdigest()


def fingerprint(block):
    return sha(json.dumps(block, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())


def words(text):
    return [t for t in text.split() if re.search(r"\w", t)]


def audio_blocks(node):
    if isinstance(node, dict):
        if node.get("type") == "audio" and "id" in node:
            yield node
        for v in node.values():
            yield from audio_blocks(v)
    elif isinstance(node, list):
        for v in node:
            yield from audio_blocks(v)


def is_whole_sentence(sentence, source):
    """sentence occurs in source, starting at the text start or after '. ', and ends on . ? or !"""
    if not sentence or sentence[-1] not in ".?!":
        return False
    start = source.find(sentence)
    while start != -1:
        if start == 0 or source[start - 2:start] in (". ", "? ", "! "):
            return True
        start = source.find(sentence, start + 1)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(REPO))
    ap.add_argument("--proposal", default=str(HERE / "audio-beats-proposal.json"))
    ap.add_argument("--emit-applied", metavar="PATH", help="write a patched copy of the package to PATH (must be outside the repo)")
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    prop = json.loads(Path(args.proposal).read_text(encoding="utf-8"))
    src = prop["source"]
    pkg_path = repo / src["package"]

    # 1. Draft markers: banner, draft status, nothing that reads as an approval.
    check(prop.get("banner") == BANNER, "banner is 'agent pre-review — no gate opened'")
    check(str(prop.get("draftStatus", "")).startswith("draft-only"), "draftStatus is draft-only")
    flat = json.dumps(prop, ensure_ascii=False).lower()
    check(not re.search(r'"(approvals|approvalstatus|approval_status|approvedby|approvedon)"', flat),
          "no approval fields in the proposal")

    # 2. Package bytes unchanged: recorded sha256 and size, and identical to the base commit's blob when git is available.
    raw = pkg_path.read_bytes()
    check(sha(raw) == src["sha256"], f"package sha256 matches recorded {src['sha256'][:16]}…")
    check(len(raw) == src["bytes"], f"package size matches recorded {src['bytes']} bytes")
    try:
        base = subprocess.run(["git", "-C", str(repo), "show", f"{src['baseCommit']}:{src['package']}"],
                              capture_output=True, check=True).stdout
        check(base == raw, f"package bytes identical to {src['baseCommit'][:7]}:{src['package']}")
        blob = subprocess.run(["git", "-C", str(repo), "hash-object", str(pkg_path)],
                              capture_output=True, check=True, text=True).stdout.strip()
        check(blob == src["gitBlob"], f"package git blob is {src['gitBlob'][:12]}")
    except (OSError, subprocess.CalledProcessError) as e:
        print(f"SKIP git byte comparison ({e.__class__.__name__}); sha256 check above still binds")
    lock = repo / src["sourceLock"]["path"]
    check(lock.exists() and sha(lock.read_bytes()) == src["sourceLock"]["sha256"], "source lock present and unchanged")

    pkg = json.loads(raw)
    citation_ids = {c["id"] for c in pkg["provenance"]["citations"]}
    by_id = {}
    for b in audio_blocks(pkg):
        by_id.setdefault(b["id"], []).append(b)

    # 3. Scope: exactly the two missing blocks.
    check(set(prop["blocks"]) == EXPECTED_IDS, f"proposal keys are exactly {sorted(EXPECTED_IDS)}")
    missing_now = sorted(i for i, bs in by_id.items() if not bs[0].get("audioBeats"))
    check(set(missing_now) == EXPECTED_IDS, f"blocks without audioBeats in the package: {missing_now}")

    for bid, entry in sorted(prop["blocks"].items()):
        found = by_id.get(bid, [])
        if not check(len(found) == 1, f"{bid}: exactly one audio block with this id"):
            continue
        block = found[0]
        # 4. Fingerprints.
        check(fingerprint(block) == entry["sourceFingerprint"], f"{bid}: block fingerprint matches")
        check(sha(FIELDS["body.en"](block).encode()) == entry["bodySha256"], f"{bid}: body.en sha256 matches")
        check(sha(FIELDS["metadata.audioScript.en"](block).encode()) == entry["audioScriptSha256"],
              f"{bid}: audioScript.en sha256 matches")
        check(not block.get("audioBeats"), f"{bid}: package still has no audioBeats (proposal unapplied)")
        # 5. Citations copied exactly and inside the lock's registry.
        check(entry["citationRefs"] == block.get("citationRefs"), f"{bid}: citationRefs identical to the block's")
        check(all(c in citation_ids for c in entry["citationRefs"]), f"{bid}: every citationRef resolves in provenance.citations")
        # 6. Beat shape, count, length, verbatim sources.
        beats, sources = entry["proposedAudioBeats"], entry["beatSources"]
        check(MIN_BEATS <= len(beats) <= MAX_BEATS, f"{bid}: {len(beats)} beats (allowed {MIN_BEATS}–{MAX_BEATS})")
        check(len(sources) == len(beats), f"{bid}: one source record per beat")
        for n, (beat, s) in enumerate(zip(beats, sources), 1):
            tag = f"{bid} beat {n}"
            check(set(beat) == {"title", "body"} and set(beat["title"]) == {"en"} and set(beat["body"]) == {"en"},
                  f"{tag}: schema shape {{title:{{en}}, body:{{en}}}}")
            body = beat["body"]["en"]
            nw = len(words(body))
            check(nw <= MAX_WORDS, f"{tag}: {nw} words (max {MAX_WORDS})")
            check(body == " ".join(x["sentence"] for x in s["sentences"]), f"{tag}: body is its source sentences joined")
            for x in s["sentences"]:
                field_text = FIELDS[x["field"]](block)
                check(is_whole_sentence(x["sentence"], field_text),
                      f"{tag}: whole verbatim sentence from {x['field']}: “{x['sentence'][:40]}…”")
            t, ts = beat["title"]["en"], s["title"]
            field_text = FIELDS[ts["field"]](block)
            check(ts["text"] in field_text and t == ts["text"][:1].upper() + ts["text"][1:],
                  f"{tag}: title “{t}” is a verbatim phrase from {ts['field']} (first letter capitalised only)")
        # 7. Honest bounds kept: the route, jurisdiction and evidence qualifiers survive in the beats.
        joined = " ".join(b["body"]["en"] for b in beats)
        for q in entry["requiredQualifiers"]:
            check(q in joined, f"{bid}: qualifier kept — “{q}”")
        # Informational: which source sentences the beats leave out.
        used = {x["sentence"] for s in sources for x in s["sentences"]}
        script = FIELDS["metadata.audioScript.en"](block)
        left = [x for x in re.split(r"(?<=[.?!])\s+", script) if x and x not in used]
        print(f"INFO {bid}: audioScript sentences not used in beats: {left}")

    # Optional dry-run copy: the proposal applied to a COPY of the package, written outside the repo.
    if args.emit_applied:
        out = Path(args.emit_applied).resolve()
        if repo in out.parents or out == pkg_path:
            check(False, f"--emit-applied target {out} is inside the repo; refusing")
        elif not failures:
            for b in audio_blocks(pkg):
                if b["id"] in prop["blocks"]:
                    b["audioBeats"] = prop["blocks"][b["id"]]["proposedAudioBeats"]
            out.write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"WROTE dry-run copy {out} (the repo package is untouched)")

    print(f"\n{'OK' if not failures else 'FAILED'}: {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
