# Build status — 11 October 2026

Bakaya is a working **trusted local receivables-preparation prototype**, not a deployed financial/legal service. Python/FastAPI, Pydantic, SQLite and Decimal power a React/TypeScript workspace.

## Implemented

- CSV/XLSX, searchable PDF/text ingestion with original files, hashes and page/line references. Hashes verify stored bytes, not authenticity.
- Source-quoted typed model proposals; live synthetic extraction validated through the OpenAI-compatible gateway using claude-haiku.
- Invoice/payment/TDS allocations, ambiguity blockers, control-total reconciliation and disclosed interest conventions with reviewer-supplied dated rates.
- Bounded planning, persistent steps/revisions, attempt limits, recoverable errors and reviewer waits. Deterministic mode is labeled.
- Source-backed corrections invalidate approval; current-revision human approval gates PDF/CSV/evidence ZIP export. Nothing is sent or filed.
- Ledger-first workspace, evidence review, collapsed secondary tools, accessible Radix dialogs and self-hosted fonts.

## Recorded verification

Latest pre-release snapshot: **79 backend tests freshly pass on 11 October**, frontend build passes; desktop/mobile allocation → confirmation → approval → ZIP download and tablet overflow checked, with no observed runtime errors. Export PDFs were visually inspected in earlier validation. Revalidate final changes; these are recorded snapshots.

Eight new Crustdata tests are included. Consent and cached buyer lookup passed browser checks at 1440/768/390 widths; the cached call consumed zero new credits. The local ledger shows 4 consumed / 4 reserved of the 500-credit ceiling. GitHub push/PR test-and-build validation has been added; remote CI is not yet claimed as passed.

A live four-tool model-planned run saved eight checkpoints and reached reviewer wait; state survived restart. A separate deterministic injected failure resumed with inventory executed once and one failed step retained. This was not a real provider outage or mid-call crash test.

Twenty synthetic fixtures: deliberate baseline 14/20 versus corrected matcher 20/20; false TDS short-payments 4 → 0 and planted ambiguities 0/2 → 2/2. This is fixture performance, not customer accuracy or legal certification.

Neatlogs application trace `45d523b11808755c75601c9114fc81b1`: successful workflow/model/inventory spans. One planning call reported 430 tokens / USD0.0007898; team total/remaining balance unknown. Entire saved remote checkpoint linkage, one-line attribution and isolated Git-assisted rollback passed; native Entire session resume restored conversation but **did not roll code back**.

## Remaining gates

| Area | Current truth / next action |
| --- | --- |
| cfo.ai | Authenticated; model/export pending verification. [Current integration status](market/cfo-integration.md). |
| Crustdata | Authenticated; optional buyer enrichment implemented and browser-verified under the 500-credit ceiling. [Current integration status](market/crustdata-integration.md). |
| Public evidence | Repository PUBLIC verified; final guest-link checks, progress post, narrated video and submission pending. |
| Docker / AWS | Docker supplied but daemon unavailable at previous check; AWS STS identity verified only. No deployment. |
| Real documents | OCR, messy-document validation and multi-invoice browser allocation editing remain incomplete. |
| Legal / rates / portal | Rate-history fetch/cache, actual portal schema/fees and qualified eligibility/interest review pending. |
| Production | Authentication/roles, tenant isolation, HTTPS, limits, retention/deletion, backups/restore, monitoring, malware controls and consent policy required. |
| Market | No CA/customer interviews or paid pilots; pricing and demand are hypotheses. |

See [judging evidence](JUDGING-EVIDENCE.md), [release package](RELEASE-PACKAGE.md) and [manual steps](MANUAL-STEPS.md). No completion percentage is a measured production-readiness score.
