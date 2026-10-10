# Neatlogs tracing

Project: `24eef2dd-58aa-4b22-b549-9fc33c68b740` (selected by the supplied project key).

The key is in the ignored root `.env`, loaded by the existing backend configuration.
No key is included in source or frontend configuration. Restart the backend manually
to load this integration; setup deliberately did not run or restart the app.

Only the Python backend calls a model. The upload HTTP entry point has an independent
`invoice-document-extraction` workflow root per request. Its custom OpenAI HTTP call
has one manual LLM span recording model, timing, actual returned token counts and
errors, followed by quoted-record validation. No OpenAI SDK/framework is used, so
provider wrapping or framework auto-instrumentation would not capture this call.
The transport, timeout, extraction rules and returned data are unchanged.

Initialization runs once in FastAPI lifespan; shutdown drains the SDK on server exit.
Health, CRUD and the frontend are not instrumented. Traces omit source documents,
prompts, model output and financial records. Error messages and stack traces are
redacted before export. No detections, alerts or evaluations were configured.

Installed Neatlogs 1.4.26 from the current PyPI release; dependencies are locked.
The network-free SDK Doctor v2 check passed. Dashboard delivery and actual model
tracing have not been verified by running the application.

For a model trace, configure `OPENAI_API_KEY` and `BAKAYA_ENABLE_LLM=true` locally,
restart the backend, then upload a text document or readable PDF through the normal
UI. Model-disabled or CSV-only uploads have no model call or token usage to record.
Check the supplied project in Neatlogs for the extraction workflow.

Reference: https://docs.neatlogs.com/sdk/python

## Configured gateway and budget
The local configuration now selects `https://litellm.vision.aivar.app/v1` with
`claude-haiku`, using the ignored `LITELLM_API_KEY`. The authorized total model
budget is USD 15. This is not a hard enforced application cap: the gateway owner
must set a USD 15 maximum budget on this key. Exact alias pricing and structured
JSON-schema compatibility remain unverified. No paid call or app restart was made.

## Live verification after implementation approval
On 10 October 2026, a minimal structured-output gateway request returned HTTP 200
using `claude-haiku` (166 total tokens), and a synthetic buyer extraction passed
quoted-field validation through the application provider. These were real model
calls. No private records were used. Exact dollar spend was not returned.

The authenticated Neatlogs Doctor probe passed, including finalized trace readback,
valid parents and numeric usage. Probe trace: `9f12d6ec853a4d4ec8b43b8da7c4fb57`.
This verifies the diagnostic trace; the synthetic application extraction emitted
its own spans but was not separately read back from the dashboard.

The user confirmed the provider enforces USD 15 per key over 30 days, shared by
all teammates, and stops requests when exhausted. Application extraction limits
output to 4096 tokens; planning limits output to 256 and never retries a paid call
automatically. HTTP 402/429 returns a quota/budget message requiring manual action.
