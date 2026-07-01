# freeCodeCamp Daily Coding Challenges — Python Solutions

![GitHub last commit](https://img.shields.io/github/last-commit/karelplanken/fcc-coding-challenges?color=blue)
![GitHub repo size](https://img.shields.io/github/repo-size/karelplanken/fcc-coding-challenges?color=orange)
![License](https://img.shields.io/github/license/karelplanken/fcc-coding-challenges?color=success)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Challenges](https://img.shields.io/badge/Challenges-294-brightgreen)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-solutions-0a0a23?logo=freecodecamp&logoColor=white&color=purple)

Personal repository of my Python solutions to the
[freeCodeCamp Daily Coding Challenges](https://www.freecodecamp.org/learn/daily-coding-challenge/archive).
A new puzzle drops every day at midnight US Central time. This repo tracks my
ongoing progress, starting from the archive of past challenges.

---

## About the Challenges

freeCodeCamp's Daily Coding Challenges are short programming puzzles designed to
keep your skills sharp through consistent practice. Each challenge is available
in both Python and JavaScript — this repo contains Python solutions only.

- 📅 **New challenge:** every day at midnight US Central
- 🗂️ **Archive:** browse and solve past challenges at your own pace
- 📱 **Platforms:** [freeCodeCamp website](https://www.freecodecamp.org/learn/daily-coding-challenge/archive) and mobile app (iOS / Android)

---

## How I Solve These Challenges

I treat these challenges as deliberate practice for my own problem-solving
skills, so I intentionally avoid AI assistance during the solving phase.

- I start by turning off GitHub Copilot (and similar guardrails)
- I copy the challenge description from freeCodeCamp and solve it on my own
  first
- For harder problems, I sketch pseudocode and think explicitly about:
	- input and output shape
	- data structures involved
	- the transformation steps from input to output
- While implementing, I run the script repeatedly and use `print` statements to
  inspect intermediate values

Only after I have a working first solution do I use AI as a review tool, not as a solver.

- I run `fb-fcc-dcc` to assemble my solution into a reusable feedback prompt
  (the template lives in [`scripts/assemble_prompt_for_feedback_on_fccdcc.py`](scripts/assemble_prompt_for_feedback_on_fccdcc.py))
- I paste that prompt into Claude for feedback, grading, and refactoring ideas
- In most cases, only minor issues come up
- Most of the time I keep my own solution or use a hybrid of my approach and
  Claude's suggestions; only rarely do I adopt Claude's full solution

This workflow keeps the focus on becoming a better programmer, rather than
optimizing for how well an AI can solve the challenge. In practice,
AI-generated alternatives can sometimes be overengineered or miss edge cases,
and AI-based grading of hand-crafted solutions can be unreliable. This is not a
rejection of GenAI's strengths for coding, but a reminder to stay cautious with
LLM-derived solutions for real problems.

---

## Code Standards

Every solution in this repo follows the same conventions:

- **Type annotations** throughout — all function signatures are fully typed
- **pytest** — each solution includes tests and can be run with `pytest`
- **mypy --strict** — all solutions pass strict static type checking

---

## Running the Solutions

### Prerequisites

```bash
# Install uv (if not already installed)
curl -Ls https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

### Run a solution

```bash
uv run python challenges/<name>.py
```

### Run tests

```bash
uv run pytest challenges/<name>.py -v --cov --cov-report=term-missing
```

### Type checking

```bash
uv run mypy --strict challenges/<name>.py
```

---

## Automation Scripts

Two small tools remove the repetitive parts of the daily routine — fetching a fresh challenge file and assembling a review prompt. Full usage details live in [`scripts/scripts-README.md`](scripts/scripts-README.md).

```bash
get-fcc-dcc                       # fetch & assemble today's challenge file
fb-fcc-dcc <challenge-file.py>    # assemble a review prompt, copy to clipboard
```

### How they were built

Both scripts were built through a deliberate division of labor:

- **Claude (Sonnet 4.6)** — planning, architecture decisions, and writing the exact prompts handed to Copilot
- **GitHub Copilot (GPT-5.4)** — generating the actual code from those prompts, inside VS Code
- **Me** — the detective work, the decisions, the testing, the corrections, and the final say on every design choice

Neither tool wrote code unsupervised. Every prompt was reviewed before being run, and every generated script was tested and corrected by hand before being accepted.

**`fb-fcc-dcc`** replaced a manual habit — copying the challenge description and a finished solution into Notepad, wrapping them in a fixed template, pasting into Claude. The fix split the work into a pure Python parser (reads the `.py` file, prints the assembled prompt to stdout) and a thin bash wrapper (resolves the file, calls Python, pipes the result to `clip.exe`). Prompts: [`01-part-1-fb-fcc-dcc-python-script.md`](documentation/automate-fetch-and-feedback-project-prompts/01-part-1-fb-fcc-dcc-python-script.md), [`02-part-2-fb-fcc-dcc-bash-script.md`](documentation/automate-fetch-and-feedback-project-prompts/02-part-2-fb-fcc-dcc-bash-script.md).

**`get-fcc-dcc`** took real detective work before any code got written. The starting question was simple — *can a new challenge file be generated automatically instead of copy-pasting from the browser?* — but freeCodeCamp's daily-challenge page is fully client-side rendered, so a plain `curl` of the page returns nothing but an empty shell and JavaScript bundles. The content had to be found elsewhere:

- The challenge content lives in freeCodeCamp's **public GitHub repo**, but each file is named after a MongoDB ObjectId (e.g. `6a0dcc730cb92a616f86f0c5.md`) — not derivable from a date or challenge number.
- ObjectIds encode a creation timestamp in their first 4 bytes, which looked promising — until decoding it showed the *seeding* date, not the challenge's scheduled date. Dead end.
- The actual link turned out to be in each file's frontmatter: a `dashedName: challenge-NNN` field, directly tied to the challenge number.
- Challenge numbers are just an offset from a known start date (`2025-08-11` = challenge #1), so any date trivially maps to a number.
- The **GitHub Search API** can look up a file by searching for `dashedName: challenge-NNN`, returning two results (JS and Python versions) to filter between.
- The Search API result only gives a file *path* — the download link comes from a second call to the **GitHub Contents API**, whose JSON response includes a ready-to-use `download_url` field.

That chain — date → number → search → path → contents → download URL — was proven manually with `curl` and `jq` before any script was written. With the data flow confirmed, the build followed the same bash-orchestrates-Python pattern, split into three focused, independently testable pieces: `get_challenge_url.py` resolves a challenge identifier to a download URL, `process_challenge_md.py` parses the markdown and writes the `.py` template, and `get-fcc-dcc` ties them together — `curl`s the download, runs `ruff format` on the result, reports success.

Prompts: [`03-part-1-get-fcc-dcc-python-script-1.md`](documentation/automate-fetch-and-feedback-project-prompts/03-part-1-get-fcc-dcc-python-script-1.md), [`04-part-2-get-fcc-dcc-python-script-2.md`](documentation/automate-fetch-and-feedback-project-prompts/04-part-2-get-fcc-dcc-python-script-2.md), [`05-part-3-get-fcc-dcc-patching-bash-script.md`](documentation/automate-fetch-and-feedback-project-prompts/05-part-3-get-fcc-dcc-patching-bash-script.md).

### Design principles followed throughout

- **Bash orchestrates, Python processes.** Each script does one job; bash never parses data, Python never touches the network or the shell.
- **Errors are owned by whoever detects them.** Python scripts print clear errors to stderr and exit non-zero; bash stops on failure without adding redundant commentary.
- **No hardcoded paths.** Scripts resolve their own location via `$(dirname "$0")` and rely on environment variables (`GITHUB_TOKEN`, `RUFFTOML`) for configuration.
- **Standard library first.** Both Python scripts avoid third-party dependencies, so they run anywhere `uv` and Python are available.

---

## Repository Structure

```
fcc-coding-challenges/
├── LICENSE
├── README.md
├── challenges
│   ├── 001_vowel_balance.py
│   ├── 002_base_check.py
│   └── ...
├── documentation
│   ├── automate-fetch-and-feedback-project-prompts
│   │   ├── 01-part-1-fb-fcc-dcc-python-script.md
│   │   ├── 02-part-2-fb-fcc-dcc-bash-script.md
│   │   ├── 03-part-1-get-fcc-dcc-python-script-1.md
│   │   ├── 04-part-2-get-fcc-dcc-python-script-2.md
│   │   ├── 05-part-3-get-fcc-dcc-patching-bash-script.md
│   │   └── 06-part-4-get-fcc-dcc-update-readme.md
│   ├── git-workflow.md
│   └── hard-challenges.md
├── pyproject.toml
├── scripts
│   ├── assemble_prompt_for_feedback_on_fccdcc.py
│   ├── fb-fcc-dcc
│   ├── get-fcc-dcc
│   ├── get_challenge_url.py
│   ├── process_challenge_md.py
│   └── scripts-README.md
└── uv.lock
```

---

## Workflow

This repo follows a branch-per-month workflow to keep `main` clean:

- A new branch `chore/cc-<month>-<year>` is created at the start of
  each month
- Each day's solution gets its own commit
- At month-end, a PR is opened and squash-merged into `main`

Full details, including the `gh` CLI commands used for branching and merging, are in [`documentation/git-workflow.md`](documentation/git-workflow.md). A running list of challenges I found particularly hard — worth revisiting later — is kept in [`documentation/hard-challenges.md`](documentation/hard-challenges.md).

---

## Links

- 🔗 [freeCodeCamp Daily Coding Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-01)
- 🗂️ [Challenge Archive](https://www.freecodecamp.org/learn/daily-coding-challenge/archive)
- 📰 [Announcement article](https://www.freecodecamp.org/news/introducing-freecodecamp-daily-python-and-javascript-challenges-solve-a-new-programming-puzzle-every-day/)

---

## License

This project is licensed under the [MIT License](LICENSE). Challenge
descriptions are the intellectual property of freeCodeCamp — only my personal
solution code is covered by this license.