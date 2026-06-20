**Part 1 — Python script to fetch challenge URL**

Write a Python script at `scripts/get_challenge_url.py`.

**Purpose:** Given a freeCodeCamp daily coding challenge identifier (number, date, or nothing), return the direct download URL for the corresponding Python challenge markdown file. Print the URL to stdout and nothing else.

**Invocation:**
```bash
uv run scripts/get_challenge_url.py           # no argument: uses today's date
uv run scripts/get_challenge_url.py 2026-06-06  # date argument: YYYY-MM-DD
uv run scripts/get_challenge_url.py 300         # number argument: integer
```

**Logic:**

The challenge number is derived from the date using:
```python
from datetime import date
SERIES_START = date(2025, 8, 11)  # Challenge #1
number = (target_date - SERIES_START).days + 1
```

Once the challenge number is known, the URL is obtained in two steps:

**Step 1 — Search:** Query the GitHub Search API to locate the markdown file:
```
GET https://api.github.com/search/code?q=dashedName:+challenge-{number}+repo:freeCodeCamp/freeCodeCamp
```
The search returns two results (JavaScript and Python versions). Filter for the result whose path contains `daily-coding-challenges-python` and extract its file path.

**Step 2 — Resolve:** Call the GitHub Contents API using that path:
```
GET https://api.github.com/repos/freeCodeCamp/freeCodeCamp/contents/{path}
```
Parse the JSON response and extract the `download_url` field. Print that value to stdout and exit.

**Authentication:**

Read the GitHub token from the environment variable `GITHUB_TOKEN`. If not set, print a clear error to stderr and exit with code 1.

Set these headers on all requests:
```python
{
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.raw",
}
```

**Argument parsing:**

- No argument → use today's date
- Argument matches `YYYY-MM-DD` → parse as date
- Argument is a plain integer → use directly as challenge number (but the maximum number is determined by today's date and new challenges are released at midnight US Central time, so validate against that accounting for time zones)
- Anything else → print usage to stderr and exit with code 1

**Requirements:**
- Type annotate everything, run clean under `mypy --strict`
- Standard library only (`urllib.request`, `json`, `sys`, `os`, `datetime`, `re`)
- If the search returns no Python result, print a clear error to stderr and exit with code 1

---
