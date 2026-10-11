# Hackathon milestones — 11 October 2026

The [official event page](https://neatlogs.com/hackathon) was fetched live with Firecrawl on 11 October. Submission opens **12 October, 19:00 IST**; **23:55 IST is the planned close**, with the final cutoff announced on [Discord](https://neatlogs.com/discord). Aim for opening. Submit by quoting the official neatlogs X post with team/name, project, public repository and demo; recheck live instructions before publishing.

| Milestone | Current evidence / remaining action | Owner |
| --- | --- | --- |
| Core agent | Bounded model planning, deterministic calculations, persistent steps, reviewer wait, revision-bound approval and export implemented. Recorded 94-test snapshot; revalidate final changes. | Builder |
| Interface | A ledger workspace + B evidence review; secondary tools collapsed; dialog focus and desktop/mobile export/tablet overflow checks passed. | Builder |
| Neatlogs | Application trace readback succeeded. It covers one model/inventory step, not every historical run. Capture a final redacted run/comparison if claiming improvement. | Builder |
| Entire | Saved/pushed checkpoints, linked-file attribution and isolated Git rollback verified. Native session resume did not restore code. [Evidence](ENTIRE-EVIDENCE.md). | Complete for demonstrated scope |
| cfo.ai | [Saved cfo model](https://app.cfo.ai/s/p_AQGWpgYkOTYzMzUxMTgtNWY4OC00ZGEzLTlkMDEtYjExYjZiMDI4ZDRmDWRlZmF1bHRfbGF5ZXI) completed: editable unit economics and monthly revenue/burn/runway, separate hypothetical demand scenario; formula readback passed. Cash/fixed costs remain unknown; no export or guest access is claimed. [Status](market/cfo-integration.md). | Builder; user if account authorization blocks |
| Crustdata | Auth/free balance check verified; optional consented buyer enrichment implemented and browser-verified at desktop 1440/tablet 768/mobile 390. Cached lookup spent zero new credits. Local ledger 4 consumed / 4 reserved of 500. [Status](market/crustdata-integration.md). | Builder |
| Public repository | Repository PUBLIC, verified by coordinating builder on 11 October. All 248 Git objects/local refs scanned for configured keys and supplied key patterns with zero matches; final release/guest link checks still required. | User, then builder |
| Building in public | Private commits are not public progress. Publish an honest dated update tagged #neatHack and preserve its URL; do not backdate. | User |
| Demo | [Three-minute script](RELEASE-PACKAGE.md) ready; recording/upload URL pending. Synthetic evidence and injected failure must be labeled. | User / builder capture |
| Release verification | 94 tests pass including eight Crustdata checks; auth/tenant tests and local Docker build/run verified. Revalidate CI for the final pushed SHA. Final submitted SHA and safe guest-access links still required. | Builder |
| Submit | Fill release links, confirm official post/Discord cutoff, quote official post and retain permalink/confirmation. | User |

No visibility change, public post or submission is implied by this checklist. Authentication/tenant tests and Docker are verified. Hosting and off-host backups remain pending: AWS default-encrypted provisioning failed even without KmsKeyId; Vercel project/domain reserved, not deployed. OCR synthetic scans pass but CORD receipt amount extraction is 0/5. Professional signoff remains pending. See [manual steps](MANUAL-STEPS.md).


## Live synthetic deployment — 11 October 2026

Frontend: https://bakayaai-sandesh.vercel.app. AWS backend: https://3-93-34-52.sslip.io. Certificate validation, reviewer login, secure cookie, authenticated cases, logout and session revocation passed. The dedicated t3.small uses 16 GB unencrypted gp3 under explicit owner approval; synthetic data only. Daily encrypted backups are active; one downloaded off-host archive restored successfully. Automated off-host transfer, professional sign-off and sensitive-document production readiness remain pending. Stop the instance after the event; stop/start changes its public IP and requires updating the backend hostname and frontend rewrite.

Login details are in the ignored local artifacts/deploy/operator-access.txt; never publish that file. Live browser inspection was unavailable, so deployed UI visual QA remains pending.
