"""Unit tests never use live model or telemetry credentials."""
import os

os.environ["BAKAYA_ENABLE_LLM"]="false"
for name in ("NEATLOGS_API_KEY","NEATLOGS_PROJECT_TOKEN"):
    os.environ.pop(name,None)
