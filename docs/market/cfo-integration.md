# cfo.ai integration — 11 October 2026

Latest browser check: after the owner signed in, the organization navigation appeared but the workspace remained on Loading. Opening its existing Welcome chat redirected to sign-in. No model could be created or read back. The local import-ready workbook is `artifacts/qa/bakaya-financial-plan.xlsx`: it contains source assumptions, contribution formulas, monthly revenue and owner-input runway formulas. Cash and fixed costs are blank rather than invented. It is not a cfo.ai export. Arithmetic and saved formula readback were checked; spreadsheet recalculation and cfo import remain unverified.

The user created the account and authorized OAuth. `codex mcp add cfo --url https://api.cfo.ai/mcp` registered the Streamable HTTP server in local Codex configuration. Credentials stay in local Codex storage; none belong in this repository.

Authenticated `list_orgs` succeeded. The server exposes 35 tools including pages, table blocks, scenarios, formula inspection and canvas validation. This is a founder financial planning integration, separate from Bakaya case approval and export.

## Exact completion status

Official cfo page/table/scenario guidance was inspected. Creation of `Bakaya Delivery Stress Assumption` and `Bakaya Financial Plan - Assumption Draft` was attempted, but both calls were cancelled by the MCP tool surface. Readback returned zero pages and zero blocks, with only the existing Main scenario. No model was created, and no existing workspace objects were changed. Authentication alone does not complete the useful sponsor workflow.

[cfo-plan-inputs.csv](cfo-plan-inputs.csv) is ready for the model. Prices, refund rate, payment fee and delivery costs are unvalidated assumptions. The monthly price assumes all ten included packets are used. At INR600 delivery cost, monthly included packets lose INR125.095 each and extras lose INR220.95 before fixed costs. Do not hide these losses with blended direct-sales revenue.

Separate observed input: one claude-haiku planning call on 10 October returned 358 prompt + 72 completion tokens and provider-reported USD0.0007898. This is a single call, not a completed packet cost. The user reports a shared USD15/key/30-day allowance; remaining balance is unknown. No exchange rate is assumed. Cash balance, volume, hosting, OCR and support measurements remain unknown; no runway is calculated.

## Remaining action

Completion was retried on 11 October in the active session and in two fresh noninteractive Codex sessions, including one without the shared daemon. `codex mcp get cfo` confirms the server is enabled at the official endpoint, but tool discovery returned no cfo tools in any of these sessions. No new writes were attempted. Earlier successful authentication is historical evidence; current account access could not be reverified.

Reload/reconnect the cfo MCP server in Codex so its tools are exposed, then complete a page/table write and verify it by readback. This is the exact remaining blocker: configured server without available tools. The prepared assumptions remain in the CSV; a local document is not a cfo-created model. Model creation and export remain pending. Review the finished assumptions before using them for pricing decisions.

Billing, purchases, bank/API connections and notifications were not performed. No private claim documents were transferred.
