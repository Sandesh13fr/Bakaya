# Judging evidence — current snapshot, 11 October 2026

The [official event page](https://neatlogs.com/hackathon), fetched live with Firecrawl on 11 October, weights five categories. These are **weights, not a predicted score**. Mandatory sponsors are Neatlogs, Entire and cfo.ai. The cfo business plan must cover pricing, costs, revenue and runway. Submission requires a public repository with event-period commits and an accessible demo; public updates should be tagged #neatHack.

| Criterion | Weight | Verified evidence | Remaining evidence |
| --- | ---: | --- | --- |
| The agent | 30% | Bounded planning; deterministic Decimal verification; saved checkpoints/reviewer wait; restart persistence; separately injected recovery without repeated inventory; revision-bound approval/export. | Final integrated recording and release checks at submitted SHA. |
| Sponsor use | 25% | Real model request; finalized Neatlogs application trace; Entire permanent checkpoints, attribution and remote readback. | cfo useful model/readback/export; final run trace and meaningful before/after evidence if claiming improvement. |
| Demo | 20% | Desktop/mobile approval/export checks; synthetic inputs; [script](RELEASE-PACKAGE.md). | Actual final video and accessible URL. |
| Building in public | 15% | Dated event-period commits; repository PUBLIC, verified on 11 October. | Verify public source/commits; honest public progress update and URL. Private pushes alone are insufficient. |
| Usefulness/originality | 10% | Specific evidence-preparation/reconciliation workflow and attributed legal/competitor research. | Real user/professional validation remains unavailable; synthetic case only. |

## Evidence register

| Evidence | Exact scope / limitation |
| --- | --- |
| Tests / UI | Fresh 79 backend tests pass on 11 October; frontend build and desktop/mobile review/export plus tablet overflow passed. Revalidate final changes; do not advertise an evergreen test count. |
| Live agent | Run `2557a200a4cb48abaa05f4c74ee9e214`: four tools/eight saved checkpoints/reviewer wait, retained after restart. No extraction or export within that run. |
| Extraction | Separate real claude-haiku synthetic buyer proposal passed source-quote/type validation. Initial structured-output call: HTTP200, 166 tokens. Not legal correctness. |
| Recovery | Run `12f1bf9b0cb84c8093b8e59f540afffe`: injected reconciliation failure, same-run resume, inventory once, failed step retained. Deterministic/local, not provider outage. |
| Neatlogs | Application trace `45d523b11808755c75601c9114fc81b1`, successful root prepare-invoice-case with claude-haiku and inventory_evidence children. One step, not complete lifecycle. Doctor `9f12d6ec853a4d4ec8b43b8da7c4fb57` is separate diagnostics. |
| Cost | One call: 358 prompt + 72 completion tokens, reported USD0.0007898. Not total spend or packet cost. User cap USD15/shared key/30 days; remaining unknown. |
| Entire | Checkpoint `01M4KRBT9GY4SCGC3WR3NXRGTR` linked `0958d0e`, remote object matches; latest UI checkpoint `01M4KYXAQ24EBCG4NE32TZQA0H` linked `ad4a7ab`. [Detailed evidence](ENTIRE-EVIDENCE.md). |
| Attribution / rollback | Tested .entire/settings.json line15 attributes to Codex/checkpoint/commit. Native resume restored logs but did not restore code; explicit Git rollback passed in isolated clone only. |
| cfo.ai | OAuth/discovery verified; actual useful model remains pending until successful readback. [Current status](market/cfo-integration.md). Prepared assumptions are not a sponsor-created model. |
| Crustdata | Authentication/free balance verified; optional app enrichment implemented and browser-verified with consent at 1440/768/390; cached lookup spent zero new credits; local ledger 4 consumed / 4 reserved of 500. [Current status](market/crustdata-integration.md). Not identity/eligibility proof. |
| AWS | STS identity only; no deployed service, verified credit balance or production availability. |
| Synthetic comparison | 20 fixtures: deliberately flawed baseline 14/20 vs corrected 20/20; false TDS 4→0, ambiguity 0/2→2/2. Not production accuracy or a trace-based historical improvement. |
| Research | [Market documents](market/README.md): source-backed research and pricing hypotheses; no CA interviews, paid demand or recovery outcome claimed. |

The first MVP is the baseline; describe event-period changes using actual diffs. Sponsor logos/configuration do not substitute for useful workflows. No raw private evidence, public post, filing or billing action is part of this ledger.

## Final release evidence

Record the final SHA and tests/build; attach redacted before/after traces when available, actual recovery evidence, Entire checkpoint, cfo plan/export and video/repository/public-update URLs. Verify guest access. Missing artifacts stay pending. See [milestones](HACKATHON-MILESTONES.md) and [submission package](RELEASE-PACKAGE.md).
