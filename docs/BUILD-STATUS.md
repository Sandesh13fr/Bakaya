# Build status — 10 October 2026

This is a working **local MVP**, based on the supplied brief and PRD. The original documents are preserved, and legal/market claims were researched separately. No external signup, public deployment, buyer message or filing occurred.

## Implemented and checked

- Python/FastAPI service, Pydantic records, SQLite storage and a React/TypeScript interface.
- Structured CSV/XLSX ingestion; text-searchable PDF and text evidence with page/line references; source hashes and original-file downloads.
- Optional OpenAI quoted-field extraction adapter, disabled by default. Local validation tests pass; a live paid request has not been made.
- Invoice references, explicit allocations, partial receipts, evidenced TDS, ambiguous-match questions and control-total reconciliation.
- Due dates, written-term cap, timely objections, conservative eligibility review and blocking of invoices not yet overdue.
- Decimal interest with monthly anniversary rests, dated rate periods, payment splits, source references and disclosed conventions.
- Human review, revision-bound approval, approval invalidation on changes and gated ZIP download.
- Draft letter, generic ODR field worksheet, complete PDF/CSV interest schedule, invoice/payment summaries, evidence and audit bundle.
- Synthetic demo, 20-case measured evaluation, labelled failure/recovery simulation and editable CSV samples.
- Marketing, competitor, pricing and legal-research drafts produced using the requested skills.

## Validation evidence

52 Python checks pass. The frontend production build passes. Headless browser checks exercised blocked approval, evidence allocation, confirmation, approval and ZIP download on desktop and mobile; no page-level horizontal overflow or runtime errors were observed. Exported PDFs were rendered and visually inspected. Sample CSV files successfully produce a reviewable new case.

On the 20 labelled synthetic cases, match correctness rises from 14/20 (70%) for a deliberately flawed baseline to 20/20 (100%) for the corrected matcher. False TDS short-payments fall from 4 to 0; both planted ambiguous cases are flagged. Corrected interest agrees to displayed paise with a separate daily reference calculation under the same disclosed convention. This is fixture performance, not an independently certified legal calculation or real-customer benchmark.

## Remaining work

| Area | Current limitation | Next action |
|---|---|---|
| Arbitrary messy-document extraction | Structured inputs work; optional quoted text proposals still require review | Validate provider output on consented real documents and improve reconciliation/extraction fixtures |
| Scanned images | OCR is not configured | Obtain readable originals or add and test an OCR provider |
| Rate recovery | Failure/retry/fallback is a labelled simulation; dated rates are reviewer inputs | Implement a real RBI rate-history fetch/cache, verification and recovery flow |
| ODR portal | Generic preparation worksheet; exact current schema unverified | Verify official portal fields, fees and accepted formats manually |
| Interest/eligibility | Convention and conservative review rules are explicit | Obtain professional validation before real filing |
| Complex allocations | API supports explicit split allocations; browser review currently targets one invoice per ambiguous receipt | Add a multi-invoice allocation editor and edit/replacement workflow for typed records |
| Sponsor evidence | No neatlogs traces, Entire checkpoints or cfo.ai export | Configure accounts, integrations and real trace/cost evidence |
| Crustdata | Buyer enrichment unconnected | Configure optional key, implement/test lookup and owner confirmation |
| Production | Single trusted local reviewer, no user accounts/tenant isolation | Add authentication, permissions, retention, deployment controls and real-data testing |
| Docker | Configuration supplied; local daemon unavailable | Start Docker and validate build/run if container deployment is needed |
| Market | Pricing and demand remain unvalidated | Interview CAs/suppliers and run paid pilots before advertising outcomes |

See [manual steps](MANUAL-STEPS.md), [input guide](INPUTS.md) and [market documents](market/README.md). No API key is required to use the local synthetic demo.
