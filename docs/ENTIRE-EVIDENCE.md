# Entire evidence verification — 11 October 2026

Read-only checks performed against the local Bakaya repository and origin:

- `entire status`: enabled on main, Codex integration present, checkpoint sync target origin.
- `entire doctor`: Git hooks OK; Codex hooks installed; hook approval records PRESENT; no stuck sessions found.
- `entire checkpoint list`: zero saved checkpoints on main.
- `entire checkpoint list --pending --json`: two task-completion records, both with empty checkpoint ID and metadata directory. These are pending activity, not persistent commit-linked evidence.
- `git for-each-ref` for local/remote Entire refs: none returned.
- `git ls-remote origin` for Entire checkpoint refs/branches: none returned.
- Status reports session attribution/tracking divergence after Git history movement; do not present attribution totals as reliable.

Verdict: hook installation and user approval are verified. Persistent checkpoint creation, linkage to a Bakaya commit and remote synchronization remain unverified. No checkpoint ID or URL can truthfully be supplied yet.

Next evidence required: a real development change captured through the approved hooks, a saved checkpoint ID, its linked commit, and successful remote readback. Before capturing session transcripts, verify secret redaction because credentials appeared in the conversation; do not publish raw session data. This verification did not modify sessions, condense/discard history, change Git refs or create checkpoints.

## Completed checkpoint verification — 11 October 2026

- Saved checkpoint: `01M4KRBT9GY4SCGC3WR3NXRGTR`.
- Linked main commit: `0958d0e` (`Link agent commits automatically for checkpoint evidence`), with an Entire-Checkpoint trailer.
- Local checkpoint ref: `refs/entire/checkpoints/TR/01M4KRBT9GY4SCGC3WR3NXRGTR`.
- Local and origin ref object IDs both: `da34ac5436932b9cd457da37beac6be3da33615e`.
- Normal Git push reported one checkpoint ref pushed successfully. Exact remote readback matched the local object.
- Entire metadata readback reports one root Codex session and two stored subagent transcripts. This checkpoint is marked logs-only: it proves stored development context linked to a commit, not independently measured file attribution or a rollback experiment.
- Ten stored files (12,259,101 bytes) were scanned for locally configured KEY/TOKEN values and supplied gateway/Crustdata key patterns before push; zero matches. This is a bounded text check, not a guarantee against all sensitive data formats.

Cause of previous stalls: the prepare-commit-msg hook awaited confirmation in a hidden Windows controlling terminal. `commit_linking: always` resolves that prompt for the authorized agent commits. Custom redaction rules protect the two supplied key formats; default scanner remains enabled. Redaction behavior follows https://github.com/entireio/cli/blob/main/docs/security-and-privacy.md.

Verdict: installed/trusted hooks, permanent saved context, commit linkage and remote synchronization are now verified. Repository remains private. No public checkpoint page or recovery/rollback experiment was verified.
