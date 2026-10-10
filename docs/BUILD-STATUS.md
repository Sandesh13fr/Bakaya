# Build status â€” 10 October 2026

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

71 Python checks pass (11 October 2026). The frontend production build passes. Headless browser checks exercised blocked approval, evidence allocation, confirmation, approval and ZIP download on desktop and mobile; no page-level horizontal overflow or runtime errors were observed. Exported PDFs were rendered and visually inspected. Sample CSV files successfully produce a reviewable new case.

On the 20 labelled synthetic cases, match correctness rises from 14/20 (70%) for a deliberately flawed baseline to 20/20 (100%) for the corrected matcher. False TDS short-payments fall from 4 to 0; both planted ambiguous cases are flagged. Corrected interest agrees to displayed paise with a separate daily reference calculation under the same disclosed convention. This is fixture performance, not an independently certified legal calculation or real-customer benchmark.

## Remaining work

| Area | Current limitation | Next action |
|---|---|---|
| Arbitrary messy-document extraction | Structured inputs work; optional quoted text proposals still require review | Validate provider output on consented real documents and improve reconciliation/extraction fixtures |
| Scanned images | OCR is not configured | Obtain readable originals or add and test an OCR provider |
| Rate recovery | Failure/retry/fallback is a labelled simulation; dated rates are reviewer inputs | Implement a real RBI rate-history fetch/cache, verification and recovery flow |
| ODR portal | Generic preparation worksheet; exact current schema unverified | Verify official portal fields, fees and accepted formats manually |
| Interest/eligibility | Convention and conservative review rules are explicit | Obtain professional validation before real filing |
| Complex allocations | API supports explicit split allocations; browser review currently targets one invoice per ambiguous receipt | Add a multi-invoice allocation editor; source-backed invoice correction is implemented |
| Sponsor evidence | Neatlogs application trace verified; Entire checkpoint and cfo.ai workflow pending | Approve pending hooks, capture checkpoint, complete user finance workflow |
| Crustdata | Buyer enrichment unconnected | Configure optional key, implement/test lookup and owner confirmation |
| Production | Single trusted local reviewer, no user accounts/tenant isolation | Add authentication, permissions, retention, deployment controls and real-data testing |
| Docker | Configuration supplied; local daemon unavailable | Start Docker and validate build/run if container deployment is needed |
| Market | Pricing and demand remain unvalidated | Interview CAs/suppliers and run paid pilots before advertising outcomes |

See [manual steps](MANUAL-STEPS.md), [input guide](INPUTS.md) and [market documents](market/README.md). No API key is required to use the local synthetic demo.

## Integrated verification — 11 October 2026

Ledger-first A and evidence-first B are implemented with self-hosted fonts, linked source facts, invoice corrections, bounded model planning and persistent agent checkpoints. The frontend production build and browser approval/export checks pass at desktop and 390px mobile width, with no page overflow or JavaScript errors. The contrast review identified secondary labels; their green text was darkened to #536747 and the same states recaptured.

Actual Neatlogs application trace `45d523b11808755c75601c9114fc81b1` finalized successfully with workflow, model and inventory tool spans. One gateway planning call reported 430 tokens and USD 0.0007898; remaining shared allowance is unknown. See the judging evidence ledger for exact scope. This remains a trusted local demo, not a production deployment.

## cfo connection update — 11 October 2026

Account OAuth and authenticated workspace discovery succeeded. Page/scenario creation calls were cancelled by the MCP tool surface; readback confirms no created page or blocks. Useful model/export remains pending. See [exact integration status](market/cfo-integration.md) and prepared model inputs.
