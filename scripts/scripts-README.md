# scripts/

Automation scripts for the freeCodeCamp daily coding challenge workflow.

## Purpose

These scripts cover both ends of the freeCodeCamp daily coding challenge workflow: creating a fresh `.py` challenge file from the upstream markdown and assembling a structured review prompt from your finished solution.

For the story of how these were built — including the freeCodeCamp/GitHub detective work behind `get-fcc-dcc` — see the [top-level README](../README.md#automation-scripts).

## Files

| File | Role |
|------|------|
| `get-fcc-dcc` | Bash command that fetches, assembles, and formats a new daily challenge file |
| `get_challenge_url.py` | Python script that resolves the download URL for a challenge's markdown |
| `process_challenge_md.py` | Python script that converts the downloaded markdown into a local `.py` challenge file |
| `fb-fcc-dcc` | Bash command that assembles a review prompt from a finished solution and copies it to the clipboard |
| `assemble_prompt_for_feedback_on_fccdcc.py` | Python script — parses the `.py` file and prints the prompt to stdout |

## Daily use

**Note**: make sure you have added the appropriate environment variables and added the `scripts/` directory to your `PATH` (see Setup below).

### Create today's challenge file

```bash
get-fcc-dcc
# ✓ Challenge #301 "Last Load" saved to challenges/301_last_load.py
```

You can also target a specific date or challenge number:

```bash
get-fcc-dcc 2026-06-20
get-fcc-dcc 301
```

### Assemble a review prompt from a finished solution

```bash
fb-fcc-dcc 293_best_hand.py
# ✓ Prompt for "Best Hand" copied to clipboard — paste into Claude
```

Run from anywhere. The script looks for the challenge file in `~/python-projects/fcc-coding-challenges/challenges/` by default, or accepts a path directly.

## Setup

### 1. Add `scripts/` to your PATH

Run this once from your terminal to add the export to `.bashrc`:

```bash
echo -e "\n# Custom script creating prompt for feedback on daily fCC coding challenges and put on clipboard" >> ~/.bashrc && \
    echo 'export PATH="$HOME/python-projects/fcc-coding-challenges/scripts:$PATH"' >> ~/.bashrc
```

### 2. Make the bash scripts executable

```bash
chmod 700 ~/python-projects/fcc-coding-challenges/scripts/get-fcc-dcc
chmod 700 ~/python-projects/fcc-coding-challenges/scripts/fb-fcc-dcc
```

### 3. Add your GitHub personal access token to your environment variables

```bash
echo -e "\n# Personal access token (classic) 'Token to get the daily coding challenge from fCC repo' with public_repo scope" >> ~/.bashrc && \
echo 'export GITHUB_TOKEN=your_token_here' >> ~/.bashrc && source ~/.bashrc
```

This will set `GITHUB_TOKEN` so `get_challenge_url.py` can query the GitHub API

### 4. Add your Ruff config file path to your environment variables

```bash
echo -e "\n# Ruff config file for formatting the generated challenge file" >> ~/.bashrc && \
echo 'export RUFFTOML=<path_to_your_ruff_config>' >> ~/.bashrc && source ~/.bashrc
```

This will set `RUFFTOML` so `get-fcc-dcc` can validate the Ruff config,
`process_challenge_md.py` can reuse Ruff's `line-length` for comment wrapping,
and `get-fcc-dcc` can format the generated file.

### 5. Verify

```bash
which get-fcc-dcc
# Should print: /home/<you>/python-projects/fcc-coding-challenges/scripts/get-fcc-dcc
which fb-fcc-dcc
# Should print: /home/<you>/python-projects/fcc-coding-challenges/scripts/fb-fcc-dcc
echo $GITHUB_TOKEN
# Should print your token
echo $RUFFTOML
# Should print the path to your Ruff config file
```

## Dependencies

- `uv` — used to run the Python scripts (`uv run`).
- `curl` — used by `get-fcc-dcc` to download the upstream challenge markdown.
- `GITHUB_TOKEN` — required by `get_challenge_url.py` for GitHub API access.
- `RUFFTOML` — path to the Ruff config file used by `get-fcc-dcc` and
  `process_challenge_md.py`.
- `ruff` — run via `uvx ruff format` after a new challenge file is created.
- `clip.exe` — available by default in WSL2, no setup needed.
- Python standard library only — no third-party packages required.

## How `get-fcc-dcc` works

```
get-fcc-dcc [DATE|NUMBER]
   ↓
get_challenge_url.py   resolves a challenge number (from today's date, a given
                        date, or a given number), searches the freeCodeCamp
                        GitHub repo for the matching markdown file, and prints
                        its download_url to stdout
   ↓
get-fcc-dcc             curl downloads that URL to a temp file
   ↓
process_challenge_md.py parses the markdown's frontmatter, description, seed
                        code, and hint-derived test cases, reads `line-length`
                        from `RUFFTOML`, and writes a ready-to-solve .py file
                        under challenges/
   ↓
get-fcc-dcc             runs `uvx ruff format` on the new file and prints the
                        success message produced by process_challenge_md.py
```

The challenge number is derived from the date using a fixed series start (`2025-08-11` = challenge #1). New challenges are published at midnight US Central time, so a requested number or date is rejected if it falls after the most recently published challenge.

## How `fb-fcc-dcc` works

The Python script parses your challenge `.py` file based on this fixed structure:

| Section | Boundary |
|---------|----------|
| Header | Line 1 — `# Daily Coding challenge #NNN (YYYY-MM-DD) - freeCodeCamp.org` or `# Daily Coding challenge #NNN (YYYY-MM-DD) <name> - freeCodeCamp.org` |
| Description | Lines 2+ until the first `from`/`import` line |
| Solution | From first `from`/`import` until `tests = [` |
| Tests | From `tests = [` to end of file |

The assembled prompt is printed to stdout by the Python script; the bash script pipes it to `clip.exe`. If the header does not include the challenge name, both scripts fall back to the first non-empty description line.