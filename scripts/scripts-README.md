# scripts/

Automation for the freeCodeCamp daily coding challenge review workflow.

## Purpose

This script pair assembles a structured review prompt from a finished solution, so you don't have to hand-copy the description, solution, and tests into Claude every time.

For the story of how it was built, see the [top-level README](../README.md#automation-scripts).

> A companion tool used to also fetch new challenge files automatically
> (`get-fcc-dcc`, `get_challenge_url.py`, `process_challenge_md.py`). It was
> removed once freeCodeCamp's daily series ended (2026-08-10, challenge
> #365) and its GitHub Code Search API dependency stopped returning usable
> results.

## Files

| File | Role |
|------|------|
| `fb-fcc-dcc` | Bash command that assembles a review prompt from a finished solution and copies it to the clipboard |
| `assemble_prompt_for_feedback_on_fccdcc.py` | Python script — parses the `.py` file and prints the prompt to stdout |

## Daily use

**Note**: make sure you have added the `scripts/` directory to your `PATH` (see Setup below).

### Assemble a review prompt from a finished solution

```bash
fb-fcc-dcc cc_293_best_hand.py
# ✓ Prompt for "Best Hand" copied to clipboard — paste into Claude
```

You can also target a challenge by its number:

```bash
fb-fcc-dcc 293
```

Run from anywhere. The script looks for the challenge file in `~/python-projects/fcc-coding-challenges/challenges/` by default, or accepts a path directly.

## Setup

### 1. Add `scripts/` to your PATH

Run this once from your terminal to add the export to `.bashrc`:

```bash
echo -e "\n# Custom script creating prompt for feedback on daily fCC coding challenges and put on clipboard" >> ~/.bashrc && \
    echo 'export PATH="$HOME/python-projects/fcc-coding-challenges/scripts:$PATH"' >> ~/.bashrc
```

### 2. Make the bash script executable

```bash
chmod 700 ~/python-projects/fcc-coding-challenges/scripts/fb-fcc-dcc
```

### 3. Verify

```bash
which fb-fcc-dcc
# Should print: /home/<you>/python-projects/fcc-coding-challenges/scripts/fb-fcc-dcc
```

## Dependencies

- `uv` — used to run the Python script (`uv run`).
- `clip.exe` — available by default in WSL2, no setup needed.
- Python standard library only — no third-party packages required.

## How `fb-fcc-dcc` works

The Python script parses your challenge `.py` file based on this fixed structure:

| Section | Boundary |
|---------|----------|
| Header | Line 1 — a module docstring: `"""Daily Coding Challenge #NNN (YYYY-MM-DD) - freeCodeCamp.org."""` |
| Description | Line 2 is blank; line 3 is `# <Challenge Name>`; the rest continues until the first `from`/`import` line |
| Solution | From first `from`/`import` until `tests = [` |
| Tests | From `tests = [` to end of file |

Before parsing, the bash wrapper validates that line 1 is a module docstring, line 2 is blank, and line 3 starts with `# ` — printing a clear error and exiting if the file doesn't match. The challenge name is always taken from line 3.

The assembled prompt is printed to stdout by the Python script; the bash script pipes it to `clip.exe`.