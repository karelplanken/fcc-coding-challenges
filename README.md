# freeCodeCamp Daily Coding Challenges — Python Solutions

![GitHub last commit](https://img.shields.io/github/last-commit/karelplanken/fcc-coding-challenges?color=blue)
![GitHub repo size](https://img.shields.io/github/repo-size/karelplanken/fcc-coding-challenges?color=orange)
![License](https://img.shields.io/github/license/karelplanken/fcc-coding-challenges?color=success)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Challenges](https://img.shields.io/badge/Challenges-202-brightgreen)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-solutions-0a0a23?logo=freecodecamp&logoColor=white)

Personal repository of my Python solutions to the [freeCodeCamp Daily Coding Challenges](https://www.freecodecamp.org/learn/daily-coding-challenge/archive). A new puzzle drops every day at midnight US Central time. This repo tracks my ongoing progress, starting from the archive of past challenges.

---

## About the Challenges

freeCodeCamp's Daily Coding Challenges are short programming puzzles designed to keep your skills sharp through consistent practice. Each challenge is available in both Python and JavaScript — this repo contains Python solutions only.

- 📅 **New challenge:** every day at midnight US Central
- 🗂️ **Archive:** browse and solve past challenges at your own pace
- 📱 **Platforms:** [freeCodeCamp website](https://www.freecodecamp.org/learn/daily-coding-challenge/archive) and mobile app (iOS / Android)

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
uv run pytest challenges/<name>.py -v --cov --cov--report=term-missing
```

### Type checking

```bash
uv run mypy --strict challenges/<name>.py
```

---

## Repository Structure

```
fcc-coding-challenges/
├── challenges/
│   ├── <name>.py
│   ├── <name>.py
│   └── ...
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

---

## Workflow

This repo follows a branch-per-month workflow to keep `main` clean:

- A new branch `chore/challenges-<month>-<year>` is created at the start of each month
- Each day's solution gets its own commit
- At month-end, a PR is opened and squash-merged into `main`

---

## Links

- 🔗 [freeCodeCamp Daily Coding Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-01)
- 🗂️ [Challenge Archive](https://www.freecodecamp.org/learn/daily-coding-challenge/archive)
- 📰 [Announcement article](https://www.freecodecamp.org/news/introducing-freecodecamp-daily-python-and-javascript-challenges-solve-a-new-programming-puzzle-every-day/)

---

## License

This project is licensed under the [MIT License](LICENSE). Challenge descriptions are the intellectual property of freeCodeCamp — only my personal solution code is covered by this license.