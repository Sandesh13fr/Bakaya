# Release package — Bakaya, 11 October 2026

Prepared copy and recording plan, not a submitted entry. Repository public access and 94 backend tests were verified by the coordinating builder on 11 October. A silent workflow clip is available locally at `artifacts/qa/bakaya-workflow.mp4`; it is not yet the complete narrated sponsor demonstration.

## Three-minute demo script

Use the current app, readable crops and synthetic-only evidence. Reuse real captured model events rather than spending quota for cosmetic retakes. Do not splice separate experiments to imply a continuous live run.

| Time | Screen | Narration |
| --- | --- | --- |
| 0:00–0:20 | Synthetic case and invoice/payment/TDS evidence | “Bakaya helps Indian micro and small suppliers prepare delayed-payment evidence. A payment may include a valid TDS deduction, or a receipt may match several invoices. Treating either incorrectly can inflate a claim. This is a fictional case, not a real filing.” |
| 0:20–0:45 | Prepare case, saved agent steps and actual model decision | “The agent inventories evidence, analyzes the ledger, independently checks reconciliation and requests review. A bounded model selects the next allowed tool; Python handles the money. Each result guides the next step, and saved state survives a restart.” |
| 0:45–1:10 | Evidence quote, unresolved allocation, interest/reconciliation detail | “Every proposed fact points to evidence. Quotes and typed checks constrain extraction; unresolved buyer, allocation and rate questions block approval. The reviewer can inspect the calculation rather than accept a model's total.” |
| 1:10–1:30 | Recorded injected failure and same-run resume | “Here we deliberately inject a local reconciliation fault. Resume retains the failed step and retries without repeating inventory. This is a controlled recovery test, separate from the live model run; it does not simulate a verified RBI outage.” |
| 1:30–1:55 | Correct allocation, confirmations, approve, ZIP | “A source-backed correction changes the revision and invalidates prior approval. After resolving the blockers, a person approves this revision and downloads the evidence packet. Bakaya sends no letter and files no case.” |
| 1:55–2:15 | Neatlogs actual application trace | “Neatlogs makes the workflow, model and tool decision inspectable. This captured application trace verifies one planning and inventory step. We distinguish it from the separate diagnostic trace and do not claim complete historic trace coverage.” |
| 2:15–2:30 | Entire checkpoint/linked commit/attribution | “Entire stores the context behind our coding changes and links it to a commit. We verified a linked line and remote checkpoint. Git-assisted rollback passed in an isolated clone; native session resume restored conversation but did not restore code.” |
| 2:30–2:45 | Saved cfo model and explicit owner-input blanks | “Our business assumptions separate prices from delivery costs. At the higher delivery-cost assumption, included monthly packets and extras lose money before fixed costs. We will change pricing or delivery before a paid pilot.” **Saved model and formula readback are verified; show the real model. Cash and fixed costs are blank, so runway remains unknown. No cfo export is claimed.** |
| 2:45–3:00 | Synthetic comparison, repository and remaining gates | “On 20 labeled fixtures, our deliberate baseline matches 14 and the corrected matcher matches 20. This is not production accuracy. The code is public; real customer and professional validation, reliable OCR and secure production hosting remain pending.” |

Optional Crustdata buyer enrichment is implemented and browser-verified with consent and cached lookup; the cache consumed zero new credits. State the 500-credit working ceiling and that company data is not legal identity evidence. It must not crowd out the three mandatory sponsors.

## Mentor message — ready to copy

I'm building Bakaya, an evidence-first agent for Indian micro and small suppliers preparing delayed-payment documentation. It reconciles invoices, receipts and evidenced TDS, checks calculations deterministically, keeps saved tool state and stops for human review before export. We have a synthetic end-to-end workflow, a real Neatlogs application trace and Entire checkpoint evidence; our editable cfo business model and formula readback are verified, with assumptions and unknown cash disclosed. I'd value your feedback on whether the agent's planning/recovery evidence is substantial enough, which single user workflow we should validate first, and how to present the legal boundaries and pricing assumptions clearly. No real claim has been filed or professionally validated.

## Submission description — ready to copy after filling links

**Project:** Bakaya — evidence-first delayed-payment preparation.

Bakaya turns invoice, receipt and TDS evidence into a reviewable ledger and draft claim packet. A bounded agent chooses eligible tools, preserves progress, checks reconciliation with deterministic Python arithmetic and asks a person to resolve missing or ambiguous evidence. Corrections invalidate previous approval; export requires approval of the current revision. It does not send notices or file claims.

We demonstrate synthetic evidence, a saved model-planned run, a separate injected-failure recovery and human-approved export. Neatlogs provides application-trace evidence; Entire links coding context to commits. [Our saved cfo business plan](https://app.cfo.ai/s/p_AQGWpgYkOTYzMzUxMTgtNWY4OC00ZGEzLTlkMDEtYjExYjZiMDI4ZDRmDWRlZmF1bHRfbGF5ZXI) covers pricing, costs, monthly revenue and conditional runway; cash and fixed costs remain unknown. A 20-fixture comparison is labeled as a deliberate baseline against the corrected matcher, not production accuracy. Authentication/tenant authorization tests and local Docker build/run pass. Synthetic OCR passes, but CORD public receipt amounts extracted 0/5. Real-document/professional signoff, deployed hosting and off-host backups remain pending; Vercel is reserved, not deployed, and AWS default encryption provisioning failed even without KmsKeyId.

- Team / name: **[FILL]**
- Public repository: https://github.com/Sandesh13fr/Bakaya
- Submitted commit: **[FILL FINAL SHA]**
- Narrated demo: **[FILL ACCESSIBLE VIDEO URL]**
- Sponsor / judging evidence: [JUDGING-EVIDENCE.md](JUDGING-EVIDENCE.md)
- cfo saved business plan: [Open model](https://app.cfo.ai/s/p_AQGWpgYkOTYzMzUxMTgtNWY4OC00ZGEzLTlkMDEtYjExYjZiMDI4ZDRmDWRlZmF1bHRfbGF5ZXI); guest access/export unverified.
- Neatlogs redacted trace screenshot/link: **[FILL VERIFIED GUEST-ACCESSIBLE LINK]**
- Entire evidence: [ENTIRE-EVIDENCE.md](ENTIRE-EVIDENCE.md)
- Public progress update: **[FILL POST URL]**

## Short X quote-post draft

Built Bakaya: an evidence-first agent that reconciles invoices, receipts and TDS, verifies money in Python and pauses for human approval before exporting a claim packet. Synthetic demo; no automatic filing. Team/name: [FILL]. Repo: https://github.com/Sandesh13fr/Bakaya Demo: [FILL] #neatHack

Quote the official neatlogs submission post, rather than publishing this as if it were already accepted. Add verified cfo/evidence links if the live instructions require them.

## Final checklist

- [ ] Revalidate final code, UI and ZIP; record the final SHA and actual test count.
- [x] Saved cfo plan/readback including pricing, costs, revenue and conditional runway assumptions; cash/fixed costs remain blank.
- [ ] Verify cfo guest access or provide a redacted export/screenshot.
- [ ] Verify public repo, video, sponsor proof and business-plan links as a guest.
- [ ] Narrate/assemble the clip into the final demo; hide credentials, private records and local account metadata.
- [ ] Replace every [FILL] placeholder.
- [ ] Confirm official X post and final Discord cutoff. Official page says 12 October 19:00–23:55 IST **planned close**.
- [ ] User publishes/submits and saves the confirmation/permalink.

No public post or submission has been made by preparing this file.


## Live synthetic deployment — 11 October 2026

Frontend: https://bakayaai-sandesh.vercel.app. AWS backend: https://3-93-34-52.sslip.io. Certificate validation, reviewer login, secure cookie, authenticated cases, logout and session revocation passed. The dedicated t3.small uses 16 GB unencrypted gp3 under explicit owner approval; synthetic data only. Daily encrypted backups are active; one downloaded off-host archive restored successfully. Automated off-host transfer, professional sign-off and sensitive-document production readiness remain pending. Stop the instance after the event; stop/start changes its public IP and requires updating the backend hostname and frontend rewrite.

Login details are in the ignored local artifacts/deploy/operator-access.txt; never publish that file. Live browser inspection was unavailable, so deployed UI visual QA remains pending.
