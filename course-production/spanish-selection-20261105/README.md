# Spanish package selection correction — 2026-11-05

The catalog now selects the existing `packages/hormones-peptides-skin.es-MX.json` package. The former Arabic-named package omitted the Spanish edition even though `deployment.reviewLocales` enabled es-MX. All package files remain unedited. No governance, status, entitlement, approval or release-date changes are included.

`check-preservation.py` compares every original leaf against the selected package and verifies the nine recorded home-glimpse capture hashes. `package-preservation.json` records 27,600 preserved leaves and zero changed/missing paths. The capture manifest points to the selected package and includes an amendment explaining that the existing screenshots remain evidence only for their recorded languages; no Spanish screenshot or clinical signoff is implied.

Use with the runtime locale-selection guard and public-language changes on `fix/hormonaly-spanish-selection-20261105`. The shared runtime remains academy-independent. See the task workspace `FIX-RESULT.md` and evidence logs for validation and limitations. This is a local correction, not a deployment or completed Bioform curriculum.
