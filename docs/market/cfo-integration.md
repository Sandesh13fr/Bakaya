# cfo.ai integration — 11 October 2026

The user created the account and authorized OAuth. `codex mcp add cfo --url https://api.cfo.ai/mcp` registered the Streamable HTTP server in local Codex configuration. Credentials stay in local Codex storage; none belong in this repository.

Authenticated `list_orgs` succeeded. The server exposes 35 tools including pages, table blocks, scenarios, formula inspection and canvas validation. This is a founder financial planning integration, separate from Bakaya case approval and export.

## Exact completion status

Official cfo page/table/scenario guidance was inspected. Creation of `Bakaya Delivery Stress Assumption` and `Bakaya Financial Plan - Assumption Draft` was attempted, but both calls were cancelled by the MCP tool surface. Readback returned zero pages and zero blocks, with only the existing Main scenario. No model was created, and no existing workspace objects were changed. Authentication alone does not complete the useful sponsor workflow.

[cfo-plan-inputs.csv](cfo-plan-inputs.csv) is ready for the model. Prices, refund rate, payment fee and delivery costs are unvalidated assumptions. The monthly price assumes all ten included packets are used. At INR600 delivery cost, monthly included packets lose INR125.095 each and extras lose INR220.95 before fixed costs. Do not hide these losses with blended direct-sales revenue.

Separate observed input: one claude-haiku planning call on 10 October returned 358 prompt + 72 completion tokens and provider-reported USD0.0007898. This is a single call, not a completed packet cost. The user reports a shared USD15/key/30-day allowance; remaining balance is unknown. No exchange rate is assumed. Cash balance, volume, hosting, OCR and support measurements remain unknown; no runway is calculated.

## Remaining action

Reload/reconnect the new cfo MCP server in Codex so its tools are available in the active session, then complete an allowed page/table write and verify the result. Until successful readback, keep model creation and export pending. Review the finished assumptions before using them for pricing decisions.

Billing, purchases, bank/API connections and notifications were not performed. No private claim documents were transferred.
