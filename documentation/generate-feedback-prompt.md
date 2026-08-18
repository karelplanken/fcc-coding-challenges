# Feedback Prompt Generation for freeCodeCamp Daily Coding Challenges

Instead of manually copying and pasting the challenge description, solution, and test
cases into Claude for feedback, we can automate this process with a Python script and a
bash wrapper.

## Part 1 — Python script

Write a Python script at `scripts/assemble_prompt_for_feedback_on_fccdcc.py`.

It reads a freeCodeCamp coding challenge `.py` file whose path is passed as `sys.argv[1]`
and prints the assembled review prompt to stdout. Nothing else — no clipboard, no file
I/O, just stdout.

Please note that the line number is 1-based, with the first line of the file being line
1.

1. Input file structure (always in this exact order):

- Line 1: challenge header, always in the form `"""Daily Coding challenge #299
  (2026-06-05) - freeCodeCamp.org."""`
- Line 2: blank line
- Line 3: challenge name, always in the form `# Best Hand`
- Description block: lines from line 4 up to but not including the first line starting
  with `from` or `import`. May contain blank lines.
- Solution block: from the first `from`/`import` line up to but not including the line
  starting with `tests = [`
- Test block: from `tests = [` to end of file

2.  Parsing rules:
- Extract the challenge name from line 3 by stripping the leading `# `
- Strip leading `#` and one optional space from description lines (lines after line 3
  until the start of the solution block, i.e. `from` or `import`). Preserve blank lines
  within the description.
- Preserve solution and test blocks as raw source, stripped of leading/trailing blank
  lines.

3. Output: print this exact prompt to stdout:

    ```
        """Daily Coding challenge {challenge number} ({date}) - freeCodeCamp.org."""
        Hi Claude,
        given this problem:
        
        {description}
        
        ```python
        from pytest import mark

        {solution}
        ```

        Test cases used:

        ```python
        {tests}
        ```

        Context: this comes from a personal coding-challenge repo with a fixed harness. The test
        cases are provided by the challenge itself, not authored by me — treat them as
        requirements/spec, not as a demonstration of my own test-design judgment, and don't
        evaluate their coverage as a hiring signal. The only thing I write is the solution
        function. The `@mark.parametrize` decorator, the test function signature, `tests`, and
        the `if __name__ == '__main__'` block are fixed and kept identical in structure across
        all challenge files; `__main__` is debugging scaffolding used while developing, not part
        of the evaluation. The seed function's parameter count, order, and return contract are
        also fixed by the harness — only parameter *names* are mine to choose (the tests never
        call it via keyword arguments). Do not read the fixed shape of that signature as a design
        decision or count it against the assessment. Evaluate the solution the way a senior
        engineer doing code review would assess the code on its own merits — do not default to a
        junior-level assessment or treat that as the baseline to be argued up from. Consider:
        correctness against the problem description; the quality of the algorithm and data
        structures chosen, including efficiency; code clarity and idiomatic style; and whether
        edge-case or ambiguous behavior implied by the description itself (e.g. tie-breaks,
        invalid input) — not by the provided tests — was handled deliberately. The provided tests
        are a correctness check, not a checklist of edge cases the solution is expected to
        anticipate beyond what the problem description actually implies. Give a hiring-relevant
        assessment as the first line, choosing freely across the full range from "junior-ready"
        through "senior-level" — state it plainly rather than reaching for a hedge — with a short
        justification grounded in specific evidence from the code. Note any strengths that would
        stand out for a career-transitioner without inflating the assessment, and any genuine
        weaknesses without inflating them either. Calibrate against realistic professional
        practice, not idealized exhaustive coverage. Then: (1) refactor for readability,
        efficiency, and speed; (2) propose one alternative approach with a brief implementation
        sketch. Verify your output for errors and contradictions before responding.
    ```

4. Requirements:
- Type annotate everything, run clean under `mypy --strict`
- Standard library only (no third-party imports)
- If `sys.argv[1]` is missing or the file is not found, print a clear error to stderr and
  exit with code 1

---

## Part 2 — Bash script

Write a bash script at `scripts/fb-fcc-dcc`. This is the command the user runs daily.

**Behaviour:**
1. Accept exactly one argument: the challenge filename (e.g. `cc_293_<name>.py` or
   `<number>`) which may be preceded by a path. If missing, print usage to stderr and
   exit 1.
2. Resolve the challenge file path: look for it in
   `~/python-projects/fcc-coding-challenges/challenges/`. If not found there, try the
   argument as a literal path. If still not found, exit 1 with a clear error.
3. Resolve the Python script path relative to the bash script's own location using
   `$(dirname "$0")`.
4. Run: `uv run "$(dirname "$0")/assemble_prompt_for_feedback_on_fccdcc.py"
   "$challenge_path"` and capture stdout.
5. Pipe the output to `clip.exe` to copy to the Windows clipboard: `printf '%s' "$prompt"
   | clip.exe`
6. Extract the challenge name from the first line of the challenge file (between the date
   and ` - freeCodeCamp.org`) and print: `✓ Prompt for "<name>" copied to clipboard —
   paste into Claude`
7. Exit 0 on success.

**Requirements:**
- `#!/usr/bin/env bash` shebang
- `set -euo pipefail`
- The script must be made executable (`chmod 700`)
- No hardcoded absolute paths

---