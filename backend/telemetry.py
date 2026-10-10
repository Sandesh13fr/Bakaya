"""Content-free tracing for document extraction; no financial records exported."""
import os

import neatlogs


def redact_errors(item, *, context=None):
    # Route errors may contain uploaded filenames or validation excerpts.
    for event in item.get("events", []):
        attrs = event.get("attributes", {})
        for key in ("exception.message", "exception.stacktrace"):
            if key in attrs:
                attrs[key] = "[redacted]"
    return item


def initialize():
    neatlogs.init(
        api_key=os.getenv("NEATLOGS_API_KEY"),
        endpoint="https://ingest.neatlogs.com",
        workflow_name="invoice-document-extraction",
        register_shutdown_handlers=False,
        mask=redact_errors,
    )


def shutdown():
    neatlogs.shutdown()
