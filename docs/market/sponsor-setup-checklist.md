# Manual sponsor setup and submission evidence

**Prepared 2026-10-10 from the supplied PRD. Unverified sponsor terms are checklist items, not facts certified by this document.** No account was created, billing changed, access claimed, message sent or deployment performed for market research.

Use the original organizer emails/official event portal to verify deadlines, credits, restrictions and URLs. Do not put invite tokens, API keys or private email contents in a public repository. The PRD's 12 October 19:00–23:55 IST submission window and 11 October 08:54 IST AWS-link expiry need original-source confirmation.

| Sponsor | Manual action | Evidence needed | Boundary / unresolved item |
|---|---|---|---|
| neatlogs | Verify official onboarding; owner creates project and supplies secret locally; configure sanitized traces; run synthetic baseline/fix/recovery | Project/run URLs, dated cost/latency, before/after metrics, error and recovery | Confirm pricing, retention, sensitive-field filtering; do not trace real bank details or secrets |
| Entire | Confirm event link `hack.entire.io/neathacks-2026` against organizer source; install/authenticate per official instructions; enable on intended repository | First connected checkpoint, fix checkpoint ID+URL, coding-session linkage, graph output | Do not claim “from commit one” if connection started later; record actual start |
| cfo.ai | Verify event offer and billing terms; owner chooses signup/trial and any renewal settings; enter clearly labeled assumptions followed by observed costs | Exported dated model with source inputs and sponsor-cost vs list-price view | PRD says cancel billing immediately; this document is **not** authority to cancel or change a paid account. Verify effect on trial access first |
| Crustdata (optional) | Verify official offer/code ordering before signup; keep code private; owner supplies API access if desired | One timestamped synthetic/demo lookup with source and owner confirmation | Lookup is enrichment, not legal identity proof; confirm credit use and caching permissions |
| AWS (optional) | Check invite expiry in original email; owner claims access; verify approved region/services/instance limits; create a budget alert | Resource/region list, live URL if deployed, credit balance and estimated post-credit monthly bill | PRD says one EC2 in us-east-1 and excludes S3/Bedrock; treat as event-specific until verified. No infrastructure purchase was made |

## Current integration state

At drafting: neatlogs, Entire, cfo.ai and Crustdata are not connected. The optional OpenAI extraction adapter is implemented but disabled by default (`BAKAYA_ENABLE_LLM` plus `OPENAI_API_KEY` enables it); live inference is untested. OCR is not configured. Local functionality and local logs are not proof of sponsor integration. See [manual setup steps](../MANUAL-STEPS.md) and the repository README for current implementation details.

## Sequence and proof register

- [ ] Founder verifies sponsor/event terms and whether an India-focused project is accepted.
- [ ] Confirm who owns each account, spend cap, expiry and shutdown responsibility.
- [ ] Add only local environment variables for secrets; review ignore rules before any public push.
- [ ] Capture synthetic-only connection proof for each required sponsor.
- [ ] Record actual integration state: planned / configured / successful test / used in measured demo.
- [ ] Reconcile evaluated code version, sample-data version, baseline/fix results and exact trace/checkpoint IDs.
- [ ] Replace economics assumptions with observed costs where available, leaving unknown support/list-price inputs explicit.
- [ ] Verify repository visibility, redaction, README links, demo length and current submission fields.
- [ ] Founder reviews final public post/submission and explicitly authorizes sending/publishing.
- [ ] After event, owner reviews renewals, resource shutdown and retention settings; no automatic cancellation implied.

Proof log template: sponsor | owner | setup date | plan/offer | expiry | approved spend | integration mode | successful run ID | public-safe URL | unresolved issue. Empty cells mean unknown, not completed.
