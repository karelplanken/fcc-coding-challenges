**Part 3 — Patching Bash Script**

Write a bash script at `scripts/get-fcc-dcc`.

**Purpose:** Orchestrate fetching and assembling a new freeCodeCamp daily coding challenge `.py` file, ready to solve.

**Invocation:**
```bash
get-fcc-dcc                  # today's challenge
get-fcc-dcc 2026-06-20       # challenge for a specific date
get-fcc-dcc 301              # challenge by number
```

Accepts zero or one argument, passed through unchanged to `get_challenge_url.py`.

**Behavior:**

1. Resolve the script's own directory using `$(dirname "$0")` so paths are never hardcoded.
2. Run `uv run "$SCRIPT_DIR/get_challenge_url.py" "$@"` to get the raw download URL. Capture stdout. If the command exits non-zero, stop immediately — do not print additional error commentary, since the Python script already wrote a clear message to stderr.
3. Create a temporary file using `mktemp`. Set a `trap` to remove it on `EXIT` (success or failure), so cleanup always happens.
4. `curl` the URL into the temp file. Use `-fsSL` flags (fail on HTTP errors, silent, show errors, follow redirects). If `curl` fails, print a clear bash-level error to stderr (e.g. `"Error: failed to download challenge markdown"`) and exit 1.
5. Run `uv run "$SCRIPT_DIR/process_challenge_md.py" "$TEMP_FILE"`. Capture its stdout (which contains the success message and output path per the existing script behaviour). If it exits non-zero, stop immediately — same rule as step 2, no extra commentary.
6. Extract the path to the newly created `.py` file from `process_challenge_md.py`'s output, or determine it independently if more reliable (whichever is more robust given the actual script behaviour).
7. Run ruff against the new file using the `RUFFTOML` environment variable:
   ```bash
   uvx ruff check --fix "$NEW_FILE" --config "$RUFFTOML"
   uvx ruff format "$NEW_FILE" --config "$RUFFTOML"
   ```
   If `RUFFTOML` is not set, print a clear error to stderr and exit 1 before reaching this step.
8. On full success, print the message already produced by `process_challenge_md.py` (do not duplicate or rephrase it).

**Requirements:**
- `#!/usr/bin/env bash`
- `set -euo pipefail`
- No hardcoded absolute paths — everything relative to `$SCRIPT_DIR` or environment variables
- Script must be made executable (`chmod +x`)

---