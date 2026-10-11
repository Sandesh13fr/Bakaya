# Bakaya

An evidence-first workspace for Indian micro and small suppliers preparing delayed-payment documentation. Python performs the calculations; people review the evidence and approve the export.

## Run locally

Windows PowerShell, Python 3.12+, Node.js 22+:

```powershell
.\scripts\start.ps1
```

Open http://127.0.0.1:8000. The startup script installs dependencies, builds the interface, and serves it with FastAPI. No API key is needed for the local synthetic demo. Keep this service on your own computer until authentication and deployment controls are added.

Use **Explore a demo** for the guided case, or start a new claim and upload the five fictional CSVs in `samples/`. The [input guide](docs/INPUTS.md) explains the accepted fields and current extraction limits. The [manual checklist](docs/MANUAL-STEPS.md) and [market drafts](docs/market/README.md) cover your setup and commercial decisions.

For development, run the backend and frontend separately:

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

```powershell
cd frontend
npm.cmd ci
npm.cmd run dev
```

## Technology

- Python 3.12, FastAPI, Pydantic and SQLite for typed records, local persistence and review gates.
- Decimal arithmetic for interest and payment allocations.
- React, TypeScript and Vite for the review workspace.
- Pinned Python dependency snapshot and an npm lockfile for reproducible installs.
- PDF/text extraction and spreadsheet ingestion, with unsupported or unreadable evidence surfaced for review.
- A human approval gate for the document bundle. The app does not send demand letters or file claims.

## Before real use

The supplied PRD is a product brief, not an authoritative legal source. The prototype prepares drafts, and the synthetic demo is not a real claim. Confirm legal eligibility, contract/supply/acceptance dates, objections, rate history and the portal's current requirements with a qualified reviewer. Review the dated research and setup checklist in `docs/market/`.

You must supply and verify real documents, resolve ambiguous allocations, substantiate TDS deductions, confirm the relevant RBI Bank Rate periods, review the output and approve it. Invoice dates alone do not establish acceptance or registration eligibility. Current published rates must not be applied retroactively to earlier periods.

## Sponsor integrations and credentials

The local synthetic demo requires no keys. Live synthetic extraction and bounded planning using claude-haiku through the OpenAI-compatible gateway are verified. Model proposals need source quotes and typed validation; Python calculates money and people approve export. Enable processing only with permission for the records. Configuration is local; see `.env.example` and [tracing](docs/TRACING.md).

Neatlogs application tracing and Entire saved/pushed checkpoints are verified. Crustdata buyer enrichment is implemented and browser-verified with consent and cached lookup; follow [current enrichment status](docs/market/crustdata-integration.md) for the app workflow. cfo.ai authentication was verified previously, but useful financial-model creation remains pending workspace/tool access and successful readback; [status](docs/market/cfo-integration.md). OCR remains unconnected. AWS STS identity is verified, not deployment. Do not commit secrets or private records.

The repository is now public, verified on 11 October. Final public progress posts, narrated demo and hackathon submission remain manual. No billing action, outreach, portal filing or production deployment is implied. See the [release package](docs/RELEASE-PACKAGE.md) and [current evidence ledger](docs/JUDGING-EVIDENCE.md).

## Validation

```powershell
.\.venv\Scripts\python.exe -m pytest tests -q
cd frontend
npm.cmd run build
```

Refer to the evaluation outputs for measured synthetic performance. Fixture performance is not production accuracy, and a deliberately simplified baseline is not evidence of a historical deployed failure.

Recorded verification: 79 Python tests; frontend build; desktop/mobile evidence review, human approval and ZIP download; tablet overflow check; sample CSV ingestion and earlier visual PDF inspection. Live synthetic model extraction/planning and separate injected local recovery passed. The 20-case synthetic benchmark scored 70% for a deliberate baseline and 100% for the evidence-aware matcher under disclosed conventions. This is not production accuracy. OCR and live RBI rate-fetch recovery remain unverified. Revalidate new changes before release.

## Deployment

The multi-stage Dockerfile builds the interface and runs the Python service as a non-root user. For local use:

```powershell
docker build -t bakaya .
docker run --rm -p 127.0.0.1:8000:8000 -v bakaya-data:/app/data bakaya
```

Public use additionally requires authentication, tenant isolation, HTTPS, rate limits, retention controls, backups and a privacy policy. This is a local prototype, not a production financial or legal service.

The Docker configuration is supplied but was not run: the local Docker daemon was unavailable. Set `BAKAYA_ALLOWED_HOSTS` to an explicit comma-separated list of deployment hostnames when using a trusted reverse proxy; local host validation is enabled by default.

Original supplied documents are preserved in `docs/original-prd.md` and `docs/original-message.txt`.
