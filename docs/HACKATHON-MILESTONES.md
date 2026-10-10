# Bakaya hackathon milestones

Working checklist for review, updated 11 October 2026. All times below are **IST (UTC+05:30)**. Targets remain proposed unless completion evidence is stated. Submission window: **Monday, 12 October 2026, 19:00–23:55 IST**, per the [official event page](https://neatlogs.com/hackathon). Aim to submit at opening and preserve time to correct upload issues.

The [judging ledger](JUDGING-EVIDENCE.md) maps evidence to the official weights: agent quality 30%, mandatory sponsor use 25%, demo 20%, building in public 15%, usefulness/originality 10%. Completing this checklist establishes evidence; it does not predict a score.

## Current position

| State | Evidence |
| --- | --- |
| Backend validation complete for current snapshot | Coordinating builder reports **71 backend tests passing**. Earlier MVP evidence also includes frontend build, desktop/mobile review/export and inspected PDFs; final release validation must match the submitted SHA. |
| Live agent and recovery verified | Actual HTTP model-planned run completed inventory, analysis, reconciliation and review request, saved eight checkpoints, and paused at `waiting_review`. Saved state survived server restart. Separate injected failure recovered to `waiting_review`, with inventory executed once and one failed audit step retained. |
| Live model connection verified | Initial `claude-haiku` structured JSON request: HTTP 200, 166 tokens. Synthetic buyer extraction passed validation separately from the four-tool planning run. The latter made no extraction call and did not approve or export a packet. |
| Neatlogs application trace verified | Trace `45d523b11808755c75601c9114fc81b1` finalized HTTP 200 / SUCCESS with three successful, correctly parented spans: `prepare-invoice-case`, `claude-haiku`, and `inventory_evidence`. The Doctor trace is separate diagnostic evidence. |
| Entire partly configured | Enabled locally with Git-ref checkpoints. Seven Codex hook approvals and a real captured checkpoint remain pending. |
| cfo.ai pending | No completed workflow evidence yet. User owns all financial-account actions. |
| Private repository pushes verified | `7c63b71` model planning/telemetry and `29f59c4` checkpointed agent/review corrections pushed on 10 October. User explicitly authorized batch pushes and chose to keep the repository private for now. Building-in-public evidence remains pending. |
| Optional services | AWS STS identity verified; no deployment claim. Crustdata key pending. Neither should delay mandatory sponsor evidence. |
| External review unavailable | No CA is available for this iteration. Use synthetic internal review, label it plainly, and leave legal/customer validation pending. |

## Dated delivery plan

| Target | Owner | Milestone / completion evidence | Dependencies and fallback |
| --- | --- | --- | --- |
| 10 Oct, 20:00 | Coordinating builder | **Backend check achieved: 71 tests pass.** Complete final UI integration/build checks and record commands/results, date and commit SHA. | A new change requires appropriate verification; the current count is a snapshot, not an evergreen final release claim. |
| 10 Oct, 21:00 | User + builder | Approve the seven pending Entire Codex hooks in the appropriate product interface; perform a small real development change; capture its checkpoint identifier and linked commit. | User approval is still required. If hooks remain blocked, keep this mandatory sponsor item incomplete and document the exact blocker. |
| 10 Oct, 22:00 | Builder | **Achieved in separate experiments:** live four-tool model-planned run; validated synthetic buyer extraction; finalized three-span application trace for one planner/inventory step. Assemble redacted evidence and final recording. | Do not present these as one continuous extraction-to-export trace. If quota fails, stop paid calls; existing captured evidence can be reused with its date disclosed. |
| 11 Oct, 11:00 | User | Complete a relevant cfo.ai workflow and provide a redacted result, date, and short explanation of its usefulness. | No agent card, purchase, cancellation or finance-account actions. Verify the actual available feature before defining the final demo claim. Missing cfo.ai evidence remains a mandatory integration gap. |
| 11 Oct, 13:00 | Builder | **Recovery achieved:** injected local failure → same-run resume → reviewer wait, inventory count one. **Persistence achieved:** separate model-planned run retained reviewer-wait state after restart. Finish final source correction → revision invalidation → approval → ZIP recording. | Distinguish local retry, restart persistence and mid-call crash recovery. Only the first two have been demonstrated. |
| 11 Oct, 15:00 | Builder | Refresh the 20-case synthetic evaluation and inspect exported PDF/ZIP contents. Record baseline and revised results, dataset version, evaluator version and final SHA. | Baseline is deliberately constructed. If results differ from the old 14/20 and 20/20 snapshot, publish the actual new results and explain differences. |
| 11 Oct, 17:00 | User + builder | Prepare repository description, baseline/change notes and potential public-update drafts while respecting the user's decision to keep the repository private. Batch code/document pushes are authorized. | Private pushes do not satisfy public progress evidence. Do not publish credentials, real invoices, financial dashboards or raw traces. |
| 11 Oct, 19:00 | User + builder | Public milestone remains pending under the user's current privacy choice. If that choice later changes, publish only authorized artifacts and verify their URLs anonymously. | Do not change repository visibility or publish posts based on this schedule. Preserve the public-criterion gap honestly. |
| 11 Oct, 21:00 | Builder | Rehearse the three-minute storyboard; capture a first complete recording with synthetic case, actual model decision, recovery, review/export and all three sponsors. | Use honest on-screen pending labels for unresolved items; never replace missing integration evidence with a logo. |
| 12 Oct, 11:00 | Builder | Final regression/build run after fixes; inspect desktop/mobile review flow and packet; update evidence ledger, trace/checkpoint identifiers and known limits. | Stop optional features. A failure reopens the relevant milestone. |
| 12 Oct, 14:00 | User + builder | Final demo recording and concise submission text reviewed against verified evidence. Ensure captions, public links and readable redaction. | Concept visuals must be labeled concepts. No CA/customer validation claims. |
| 12 Oct, 16:00 | User | Confirm event account access, submission requirements and accepted link formats; verify all mandatory sponsor artifacts and public URLs. | Check the live submission page for changes. Account access should not be discovered at the final deadline. |
| 12 Oct, 18:00 | Builder | Freeze release candidate; record final SHA, evidence index and known limitations. Prepare an upload-ready package and retain a local backup. | Any subsequent fix requires targeted verification and a revised final SHA. |
| 12 Oct, 19:00 | User / explicitly authorized submitter | Submit when the window opens; retain confirmation, submission ID, timestamp and submitted URLs. | This checklist does not itself authorize submission. If the page is unavailable, preserve the error and retry within the event window. |
| 12 Oct, 22:30 | User | Contingency check: submission accepted, links accessible, demo playable. Correct permitted issues with at least 85 minutes before the 23:55 close. | Do not wait until this target for the first submission. |

## Mandatory sponsor completion checks

### Neatlogs

- [x] Authenticated Doctor trace finalized and read back.
- [x] Application extraction instrumentation emitted separate spans, as recorded in tracing notes.
- [x] Actual application trace finalized HTTP 200 / SUCCESS, with one workflow root, one LLM child and one tool child, all successful and correctly parented. Scope: one planner/inventory step, not the complete four-tool run.
- [x] Returned usage for the associated planning call recorded: 358 prompt tokens, 72 completion tokens, provider-reported USD 0.0007898.
- [ ] Redacted capture links the trace to the demonstrated run and final commit.
- [ ] A useful diagnostic example shows what the trace revealed and how the fix or recovery was verified. An intentionally injected failure must be labeled.

Neatlogs' native fix dispatch currently targets Cursor Cloud Agents; do not claim native Codex dispatch unless independently verified. Keep synthetic datasets in the repository rather than implying use of a currently unavailable dedicated dataset feature. Sources: [triage documentation](https://docs.neatlogs.com/docs/features/triage) and [experiments documentation](https://docs.neatlogs.com/docs/features/experiments), researched 10 October 2026.

### Entire

- [x] Local settings enable Entire with Git-ref checkpoints.
- [ ] User resolves seven pending Codex hook approvals.
- [ ] A real development action produces an inspectable checkpoint.
- [ ] Checkpoint identifier, linked commit and dated redacted capture are recorded.
- [ ] Demonstration explains how the checkpoint helps understand or recover the change; enabled settings alone are insufficient.

### cfo.ai

- [ ] User confirms account access and the relevant feature available to them.
- [ ] User completes an authorized finance workflow and obtains a real useful result.
- [ ] User redacts sensitive account/card/transaction information from any demonstration.
- [ ] Evidence records the performed action and result without implying an unperformed transaction, cancellation or saving.
- [ ] Final demo includes the verified result. If unavailable, record the mandatory sponsor gap plainly.

## Usage budget and optional services

The gateway key has a **hard USD 15 allowance per 30 days shared across all teammates**, as specified by the user. It stops accepting requests when exhausted. One planning response reported **USD 0.0007898**, with **358 prompt and 72 completion tokens (430 total)**; actual usage is recorded in the local SQLite ledger. This is one provider-reported charge, not total team spend or an independently reconciled invoice. Remaining balance, other unreported call costs and exact model unit pricing remain unknown. Do not convert the initial 166-token response into an invented cost.

- Keep paid extraction opt-in; avoid repeated live calls for recording polish. Use a dated recorded successful run where appropriate.
- Current extraction output is bounded at 4,096 tokens and planning at 256 tokens per response. The agent has a planning-attempt limit. These limits constrain usage but do not guarantee a dollar ceiling or reserve balance for other teammates.
- Coordinate a small shared call budget before further demonstrations and log provider/model, time, returned input/output tokens, result, and any provider-reported charge. Leave unknown charges blank.
- Treat HTTP 402/429 quota responses as a stop condition for paid work. Do not rotate keys or automatically retry to bypass the limit.
- AWS is optional: STS success establishes identity only. Before deploying, confirm the event grant and restrictions, including supplied VPC, allowed services, region and storage. Do not assume S3/Bedrock or unused credit. See the [official AWS offer](https://neatlogs.com/hackathon/check-in/aws).
- Crustdata is optional and currently lacks a key. If it becomes available, use it for clearly labeled enrichment, never as authoritative proof of buyer identity or legal eligibility. Skip it if it threatens mandatory milestones.

## Provenance and publication gates

Record the baseline commit and final commit, then describe the actual changes between them. Existing reconciliation, review and export work remains preexisting MVP context even if first imported into Git during the event. Dated snapshots alone do not prove when every feature was originally created. The coordinating builder should inspect the final diff and identify event-period improvements precisely.

The public package should include synthetic fixtures, reproducible validation instructions, known limitations, dated sponsor evidence, and a short business rationale. Keep keys and actual sensitive financial data out of source, traces and recordings. No live filing, demand notice, customer outreach, public post or financial-account action is part of this document's execution.

## Ready-to-submit checklist

- [ ] Final build/test results reflect the submitted commit, with no invented passing count.
- [x] Model-planning evidence identifies the actual tool selections; separate extraction validation and deterministic decisions are distinguished in the [redacted evidence summary](evidence/synthetic-agent-validation.json).
- [x] Recovery evidence identifies the same run before and after the injected failure, with no repeated inventory. Final video capture remains pending.
- [ ] Synthetic case is clearly labeled; legal and CA review remain pending.
- [ ] Neatlogs application trace, Entire checkpoint and cfo.ai useful result are each inspectable.
- [ ] Public artifacts and development updates are actually published with authorization and anonymously accessible.
- [ ] Final demo uses live-build captures; concept boards are labeled separately.
- [ ] README/evidence ledger disclose unimplemented proposal items, optional-service gaps and local-only security limits.
- [ ] Submission confirmation and final accepted URLs are saved before 23:55 IST on 12 October.

## Workspace completion — 11 October 2026

Current integration verified: 71 backend tests pass; TypeScript/Vite production build passes; browser source review, human approval and ZIP download pass on desktop/mobile with no page-level overflow or runtime errors. A+B workspace is implemented. Secondary text contrast was corrected and recaptured; fresh finish reviewer disposition: ship for the scored contrast fix (6.18:1 on white, above 5.3:1 on selected/totals surfaces). Separate quality-bar card was unavailable. Final video, Entire checkpoint, cfo.ai workflow, public evidence and authorized submission remain outstanding. GitHub stays private by user instruction.

The 11 October workspace commit is `8cc81b4`, pushed privately. Its Entire prepare-commit hook stalled and was terminated; no new checkpoint is claimed. Documentation commits temporarily skip this stalled hook without changing its installed configuration.

## cfo connection update — 11 October 2026

Account OAuth and authenticated workspace discovery succeeded. Page/scenario creation calls were cancelled by the MCP tool surface; readback confirms no created page or blocks. Useful model/export remains pending. See [exact integration status](market/cfo-integration.md) and prepared model inputs.
