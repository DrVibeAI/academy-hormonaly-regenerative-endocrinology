#!/usr/bin/env python3
"""Offline check of audio-beats-proposal.json against the package it was drafted from.

agent pre-review — no gate opened. Standard library only; no network. Reads the package, never writes it.

  python3 course-production/hormones-peptides-skin/upkeep-drafts/2026-11-27/validate_proposal.py
  python3 .../validate_proposal.py --emit-applied /tmp/preview.json   # patched COPY for a dry-run check, outside the repo

Exit 0 when every check passes, 1 otherwise.
"""
import argparse
import copy
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
ORIGINAL_COMMIT = "a09f3d4ea3c81744ce62d2cf770360f5334962f2"
BASE_COMMIT = "124d4f7276ede2378d99570ccaddbacc13ec4806"
ORIGINAL_DIR = "course-production/hormones-peptides-skin/upkeep-drafts/2026-11-12"
PACKAGE = "packages/hormones-peptides-skin.json"
LOCK = "course-production/hormones-peptides-skin/source-lock.md"
ORIGINAL_FILES = ("README.md", "audio-beats-proposal.json", "validate_proposal.py", "voice-options-note.md")

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


def git(repo, *args):
    # Offline objects only. Missing history fails closed; never fetch or silently skip.
    return subprocess.run(["git", "-c", "protocol.allow=never", "-C", str(repo), *args],
                          capture_output=True, check=True).stdout


def verify_refresh(repo, prop, raw):
    original_files = {f: git(repo, "show", f"{ORIGINAL_COMMIT}:{ORIGINAL_DIR}/{f}") for f in ORIGINAL_FILES}
    original = json.loads(original_files["audio-beats-proposal.json"])
    old_raw = git(repo, "show", f"{ORIGINAL_COMMIT}:{PACKAGE}")
    base_raw = git(repo, "show", f"{BASE_COMMIT}:{PACKAGE}")
    old_pkg, current = json.loads(old_raw), json.loads(raw)
    check(sha(old_raw) == original["source"]["sha256"], "original package matches original proposal binding")
    check(raw == base_raw, "current package bytes equal pinned base 124d4f7")

    # Reconstruct the only permitted refresh from immutable Git objects, independently
    # of the candidate's claimed hashes. This also pins titles, order and source maps.
    expected = copy.deepcopy(original)
    expected["source"].update(sha256=sha(base_raw), bytes=len(base_raw), baseCommit=BASE_COMMIT,
                             gitBlob=git(repo, "rev-parse", f"{BASE_COMMIT}:{PACKAGE}").decode().strip())
    expected["refresh"] = {
        "refreshedOn": "2026-11-27",
        "operatorRun": "20261127-104534-engineer-goal-refresh-existing-unapplied-hormonal",
        "originalProposalCommit": ORIGINAL_COMMIT,
        "originalDirectory": ORIGINAL_DIR,
        "originalSource": original["source"],
        "originalFileSha256": {f: sha(data) for f, data in original_files.items()},
        "drift": "Watch-only metadata: jurisdictions[].updateSources added; all other package data, both target blocks, citations, source lock and all proposal teaching text unchanged. No source-lock amendment or new teaching evidence inferred.",
    }
    check(prop == expected, "proposal is exact original plus four source bindings and refresh provenance only")
    check(prop["blocks"] == original["blocks"], "all seven beats, titles, citations, qualifiers and source maps equal original")

    stripped = copy.deepcopy(current)
    watches = {}
    for jurisdiction in stripped["jurisdictions"]:
        watches[jurisdiction["code"]] = jurisdiction.pop("updateSources", None)
    check(all("updateSources" not in j for j in old_pkg["jurisdictions"]), "original package has no watch metadata")
    check(stripped == old_pkg, "watch-only drift: removing updateSources restores entire original package")
    check({k: len(v) if isinstance(v, list) else None for k, v in watches.items()}
          == {"US": 2, "GB": 2, "EU": 1, "PT": 1, "BR": 1, "AE": 3}, "exact six watch-source additions (ten entries)")
    check(current["provenance"] == old_pkg["provenance"], "entire provenance, citation registry and sourceLock unchanged")
    old_blocks = {b["id"]: b for b in audio_blocks(old_pkg)}
    current_blocks = {b["id"]: b for b in audio_blocks(current)}
    check(all(current_blocks.get(bid) == old_blocks.get(bid) for bid in EXPECTED_IDS), "both complete target blocks unchanged")
    check((repo / LOCK).read_bytes() == git(repo, "show", f"{ORIGINAL_COMMIT}:{LOCK}"), "source lock bytes equal original proposal baseline")
    check((repo / "foundry.lock").read_bytes() == git(repo, "show", f"{BASE_COMMIT}:foundry.lock"), "foundry.lock unchanged from pinned base")


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
    pkg_path = repo / PACKAGE

    # 1. Draft markers: banner, draft status, nothing that reads as an approval.
    check(prop.get("banner") == BANNER, "banner is 'agent pre-review — no gate opened'")
    check(prop.get("draftStatus") == "draft-only — unapplied proposal; nothing in packages/ was changed", "draftStatus is draft-only")
    flat = json.dumps(prop, ensure_ascii=False).lower()
    check(not re.search(r'"(approvals|approvalstatus|approval_status|approvedby|approvedon)"', flat),
          "no approval fields in the proposal")

    # 2. Package bytes unchanged. Git history is required to prove exact reuse and watch-only drift.
    raw = pkg_path.read_bytes()
    verify_refresh(repo, prop, raw)
    check(sha(raw) == src["sha256"], f"package sha256 matches recorded {src['sha256'][:16]}…")
    check(len(raw) == src["bytes"], f"package size matches recorded {src['bytes']} bytes")
    blob = git(repo, "hash-object", str(pkg_path)).decode().strip()
    check(blob == src["gitBlob"], f"package git blob is {src['gitBlob'][:12]}")
    lock = repo / LOCK
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
        if repo in out.parents or REPO in out.parents or out == pkg_path:
            check(False, f"--emit-applied target {out} is inside the repo; refusing")
        elif out.exists():
            check(False, "--emit-applied target already exists; refusing to overwrite")
        elif not failures:
            for b in audio_blocks(pkg):
                if b["id"] in prop["blocks"]:
                    b["audioBeats"] = prop["blocks"][b["id"]]["proposedAudioBeats"]
            out.write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"WROTE dry-run copy {out} (the repo package is untouched)")

    print(f"\n{'OK' if not failures else 'FAILED'}: {len(failures)} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError, AttributeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL invalid input or unavailable offline Git history ({type(exc).__name__})")
        sys.exit(1)
