**Part 2 — Bash script**

Write a bash script at `scripts/fb-fcc-dcc`. This is the command the user runs daily.

**Behaviour:**
1. Accept exactly one argument: the challenge filename (e.g. `challenge_293.py`) which may be preceded by a path. If missing, print usage to stderr and exit 1.
2. Resolve the challenge file path: look for it in `~/python-projects/fcc-coding-challenges/challenges/`. If not found there, try the argument as a literal path. If still not found, exit 1 with a clear error.
3. Resolve the Python script path relative to the bash script's own location using `$(dirname "$0")`.
4. Run: `uv run "$(dirname "$0")/assemble_prompt_for_feedback_on_fccdcc.py" "$challenge_path"` and capture stdout.
5. Pipe the output to `clip.exe` to copy to the Windows clipboard: `printf '%s' "$prompt" | clip.exe`
6. Extract the challenge name from the first line of the challenge file (between the date and ` - freeCodeCamp.org`) and print: `✓ Prompt for "<name>" copied to clipboard — paste into Claude`
7. Exit 0 on success.

**Requirements:**
- `#!/usr/bin/env bash` shebang
- `set -euo pipefail`
- The script must be made executable (`chmod 700`)
- No hardcoded absolute paths

---