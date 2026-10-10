# Crustdata connection — 11 October 2026

The supplied API key is stored in ignored local `.env` and local Codex MCP configuration. Neither is committed. Official endpoint: https://mcp.crustdata.com/mcp (Bearer authentication), verified from https://mcp.crustdata.com/.

Authenticated initialization and tool discovery returned HTTP200. Free credit balance check succeeded and reported account balance5200 credits, spent_this_call0. The user explicitly sets the working ceiling at500 CREDITS; do not raise it without authorization. Account balance does not override this ceiling. No billable lookup, watcher or enrichment was performed in this verification.

The tool's price table reports company enrich v2 at2credits/company and identify v2 free, as of its published pricing snapshot. Recheck before usage. Limit fields and company count, record provider-reported usage, cache results and stop paid operations on unknown/error cost. No USD conversion is assumed. The provider-side500 limit is user-reported, not independently confirmed by balance data.

This connects the development MCP, not yet the Bakaya buyer-enrichment UI. Enrichment must remain optional and require owner confirmation; company data is not legal identity, Udyam eligibility, registration or tax evidence.

The user reports other manual tasks complete. cfo model creation/readback and Entire checkpoint evidence still need verification before the sponsor ledger can mark them verified. Repository visibility remains private under the last explicit instruction.
