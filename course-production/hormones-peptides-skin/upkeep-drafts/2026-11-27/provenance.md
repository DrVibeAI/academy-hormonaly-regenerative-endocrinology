# Refresh provenance

**agent pre-review — no gate opened**

Original proposal: `a09f3d4ea3c81744ce62d2cf770360f5334962f2:course-production/hormones-peptides-skin/upkeep-drafts/2026-11-12/` (read via `git show`).
Current fixed base: `124d4f7276ede2378d99570ccaddbacc13ec4806`. Original package base: `4e63edc9f8dab13fc493bbb5f98a8cdcc77a06f6`.
Original proposal creation date and operator attribution remain in the proposal. Its `refresh.originalSource` retains the full original source object.

## Package byte bindings

| Binding | Original | Current |
|---|---|---|
| `sha256` | `6419297d6d012d8c8e5b58909e9e9f1f950443aa548ca20618017dbb0ebfa4fa` | `51ecbf6b28b9964152532a43442f3b86a2a3034075a7bf0703235fa9a786bda1` |
| `bytes` | `2038738` | `2042100` |
| `gitBlob` | `21085abf15cb0b99ce90dcdf27c77fcb52a4a2f6` | `fdb2580030738a2cba080295c8ba3e986e1defc6` |
| `baseCommit` | `4e63edc9f8dab13fc493bbb5f98a8cdcc77a06f6` | `124d4f7276ede2378d99570ccaddbacc13ec4806` |

Unchanged Foundry pin: `69b4706c26505bb6b03b08be6ab900b7493a0816`.
Unchanged lock: `course-production/hormones-peptides-skin/source-lock.md`, SHA-256 `e830148c2de8ed85ce0e2c88ccae52c71473b19266ac833356e64205aaa836ff`.
The entire `provenance` object, including every citation record and the source lock, is equal at both commits.

## Exact changed JSON paths

Package comparison has only these additions (zero replacements/deletions). Array entries are in jurisdiction order:

| Path | Code | Added watch entries |
|---|---|---|
| `/jurisdictions/0/updateSources` | US | 2 |
| `/jurisdictions/1/updateSources` | GB | 2 |
| `/jurisdictions/2/updateSources` | EU | 1 |
| `/jurisdictions/3/updateSources` | PT | 1 |
| `/jurisdictions/4/updateSources` | BR | 1 |
| `/jurisdictions/5/updateSources` | AE | 3 |

Removing these six arrays yields whole-object equality with the original package, covering all modules, variants, assets and governance.
The watch URLs are operational metadata only: no live retrieval, teaching update, lock amendment, new citation or gate action is inferred.

## Unchanged target bindings

| Block | Whole block SHA-256 | body.en SHA-256 | audioScript.en SHA-256 |
|---|---|---|---|
| `m4-p06` | `9d873efb2bfb79359c843ea7acf200d67d225fba1ab25ef1bc4e929744bf763c` | `e470510fe12ba829b71468789f138c6c481a874409479225e060ccceeda17e19` | `3bcb6006c598a1fcf776c2094b1fffd735eb179095ae9d98f1f1758b09a3c912` |
| `m4-p11` | `e38000907c1513b0aec9e0ea3b9a2f9059d1716cd615ff870490528ca03da4dd` | `2ae86eeb67817c0583c3396b39a2eb6eb855474349ce09663bd16f2451f7ba6c` | `1fef9dd098f369517a61f57e0748f837f4b3edb3cf1b08dc8de25417d2516e29` |

Fingerprint method remains the inherited `fingerprintMethod` in the proposal.
Every proposed beat cites its unchanged parent block `citationRefs`; exact sentence and title attribution remains in `beatSources`.
No clinical claims or references have been added. This is an identity comparison, not renewed clinical validation.

## Original file SHA-256 values

| File (original dated directory) | SHA-256 |
|---|---|
| `README.md` | `8337bdfed7afaa339a9038db48d8e05c6c580a8698022dc049ac7ba845378f34` |
| `audio-beats-proposal.json` | `8cfbe726d0d800ef59875ed948d3d2c4d817b011f52d0c1dd5e554d7d4d2ac8f` |
| `validate_proposal.py` | `5d23b20c2c739420d311ff223ea689beb8f0074c3926d7a32fee1afd3753f0f9` |
| `voice-options-note.md` | `cc75600a0bf43a90fc0badfd4c28074067c1c466e38df95bdbe408920d94dff8` |

`voice-options-note.md` is copied verbatim. The other three files are refreshed as documented above.
Historical checks in the old README remain historical; current execution evidence is in [test-evidence.md](test-evidence.md).
The offline validator reads these exact original files from the fixed commit and verifies all proposal metadata as well as teaching.
