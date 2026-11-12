# Request only. Not applied, not approved.

**Request:** lock amendment — re-point `gphc-pharmacist-prescribers-2025` to the document's new URL.
**Modules:** m07

## What changed

The locked URL for `gphc-pharmacist-prescribers-2025` ("In practice: Guidance for pharmacist prescribers (updated April 2025)", General Pharmaceutical Council) returns HTTP 404:

- locked: `https://assets.pharmacyregulation.org/files/2025-04/in-practice-guidance-for-pharmacist-prescribers-updated-april-2025.pdf?VersionId=gDMMsBlPEOdD2uTfSyjVzhutXbJ5RCCg`

GPhC has re-published the same document at a new path (HTTP 200, verified 2026-11-12: 34-page PDF, cover page reads "In practice: Guidance for pharmacist prescribers / Updated April 2025" — same document, no content change observed on the cover/pagination):

- proposed: `https://assets.pharmacyregulation.org/files/2026-10/in-practice-guidance-for-pharmacist-prescribers-updated-april-2025a.pdf`

## What would change

Registry entry `sources[].url` for `gphc-pharmacist-prescribers-2025` in `packages/hormones-peptides-skin.json` (and the matching entry in the course source-lock list, wherever `allowedSources` mirrors it). No unit text changes — the citations and their roles stay as written.

## Units citing it

- `c-m07-24` (m07)
- `m7-p21` (m07, two citation slots)
- course source-lock list (`m07-story` provenance block)

## What I could not verify

Full page-by-page equality of the re-hosted PDF against the cached locked copy (byte hash differs by nature of re-publication; the automated source check currently holds on the cached copy). The dependent claims are held on the amendment's outcome until it is applied; the cached copy keeps the existing evidence intact in the meantime.

## Alternative if declined

Keep the locked 2025-04 VersionId URL as-is: the runner's cached copy is retained and re-verified monthly, and the claims hold on it. The cost is a permanent "refetch failed" row in source health until GPhC restores the old path or the URL is updated.
