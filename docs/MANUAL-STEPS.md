# What you need to do manually

## Use the local prototype

1. Run `scripts/start.ps1` from the project folder and open `http://127.0.0.1:8000`.
2. Load the synthetic demo first. Inspect evidence, blockers and the interest schedule before approval.
3. For real records, supply the seller's enterprise category, activity, registration evidence and date, buyer details, contract/PO and supply dates, written terms, acceptance/delivery evidence, objection resolution, payments and TDS evidence.
4. Confirm the RBI **Bank Rate**, its effective dates throughout the delayed period and the calculation convention. The synthetic rate table is not valid real-world rate evidence.
5. Resolve ambiguous payments and missing evidence; review and approve the document bundle yourself. File through the official portal yourself if appropriate. Bakaya does not file or send anything.

## Accounts and API keys

| Capability | Local build | Your action for a connected service |
|---|---|---|
| Local Python calculations and synthetic demo | No key | None |
| OpenAI text extraction | Adapter included; disabled; live call untested | Set `OPENAI_API_KEY` and `BAKAYA_ENABLE_LLM=true` in your local environment after approving uploaded-text processing; no model approval or money calculations |
| OCR for scanned documents | Unreadable scans flagged for review | Provide readable originals or choose an OCR service and configure its credentials; integration still required |
| neatlogs | Local audit is separate from sponsor tracing | Create account/project, obtain current SDK configuration and connect/test it; use redacted records |
| Entire | No sponsor checkpoint created | Create account, install/configure supported CLI, connect repository before claiming checkpoints |
| cfo.ai | OAuth and workspace discovery verified; model write cancelled | Reload/reconnect MCP tools, complete and verify the prepared financial model; see market/cfo-integration.md |
| Crustdata | Optional; not connected | Claim sponsor access if applicable, obtain key, configure and test buyer lookup; owner must confirm entity |
| AWS | No deployment | Claim/check access, confirm credits and eligible services, configure EC2 and security; use a single instance if rules require it |

Do not paste API keys into this chat or commit them. There is no reason to obtain paid API keys just to try the current local demo. No external account was created, billing cancelled or public service launched by this build.

## Before using customer financial data

The current service is intended for a single trusted local reviewer. Add authentication, permission checks and tenant isolation before exposing it publicly. Establish retention/deletion, backups, HTTPS, upload malware screening, redacted tracing and a privacy policy. Obtain the customer's permission to process their documents and review legal claims with a qualified professional.

## Market validation and hackathon submission

- Interview at least three CAs or suppliers. Ask about current claim preparation, missing evidence, time spent, and whether they will pay for a pilot. Prices in the supplied PRD remain hypotheses.
- Confirm the actual hackathon schedule and sponsor rules. The PRD lists **Monday, 12 October 2026, 7:00–11:55 PM IST**; this build has not independently verified the event deadline or access-link expiry.
- Create and publish the repository if wanted; establish sponsor tracing/checkpoints with real evidence.
- Record the demo and capture actual evaluation outputs. Show that the data is synthetic and distinguish the intentionally simplified baseline from the corrected matcher.
- Add sponsor trace/checkpoint links and actual measured costs; prepare the cfo.ai export.
- Review and publish any social posts and submit the entry yourself. No outreach or posts have been sent.

Detailed legal and market research is in `docs/market/`. The supplied documents are preserved in `docs/original-prd.md` and `docs/original-message.txt`.
