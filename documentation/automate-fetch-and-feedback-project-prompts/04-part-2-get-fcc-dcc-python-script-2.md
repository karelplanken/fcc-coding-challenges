**Part 2 — Python script to fetch challenge URL refactor**

Write a Python script at `scripts/process_challenge_md.py`.

**Purpose:** Read a freeCodeCamp daily coding challenge markdown file, parse it into its components, and write a ready-to-solve `.py` file to the challenges directory.

**Invocation:**
```bash
uv run scripts/process_challenge_md.py challenge.md
```

The single argument is the path to the downloaded markdown file.

**Input file structure** (always in this exact order):

```
---
id: <mongodb-id>
title: "Challenge NNN: <title>"
challengeType: 29
dashedName: challenge-NNN
---

# --description--

<problem description: one or more paragraphs>

# --hints--

`<function_call(args)>` should return `<expected>`.

```js
({test: () => { runPython(`
from unittest import TestCase
TestCase().assertEqual(<function_call(args)>, <expected>)`)
}})
```

... (repeated for each test case)

# --seed--

## --seed-contents--

```py
<seed function signature and body>
```

# --solutions--

```py
<solution - ignore this section entirely>
```
```

**Parsing rules:**

- **Challenge number and title:** extract from the `title` field in the frontmatter. Example: `"Challenge 301: Last Load"` → number `301`, title `Last Load`
- **Date:** derive from the challenge number using `date(2025, 8, 11) + timedelta(days=number-1)`, formatted as `YYYY-MM-DD`
- **Description:** everything between `# --description--` and `# --hints--`, stripped of leading/trailing whitespace
- **Seed function:** extract the code block under `## --seed-contents--`, stripped of leading/trailing whitespace
- **Test cases:** from each hint block, extract the `TestCase().assertEqual(...)` line. Parse it into `(args, expected)` where args are everything inside the outermost parentheses of the function call, and expected is the second argument to `assertEqual`. Preserve the original function call exactly as it appears in the hint line (e.g. `last_load_date(10, [2, 2, 2, 2, 2, 2, 2])`)
- **Solutions section:** ignore entirely

**Output file:**

Save to `~/python-projects/fcc-coding-challenges/challenges/` with filename `challenge_NNN.py` where NNN is zero-padded to 3 digits.

The file content must follow this exact template:

```python
# Daily Coding challenge #NNN (YYYY-MM-DD) - freeCodeCamp.org
# <title>
# <description, each line prefixed with '# '>
from pytest import mark


<seed function>


tests = [
    (<args>, <expected>),  # 0
    (<args>, <expected>),  # 1
    ...
]


@mark.parametrize('args, expected', tests)
def test_<function_name>(args, expected):
    assert <function_name>(*args) == expected


if __name__ == '__main__':
    args, expected = tests[0]
    print(<function_name>(*args))
```

**Requirements:**
- As soon as the filename is determined, the script should check if a file with that name already exists in the output directory. If it does, ask the user to overwrite the existing file.
- Extract the function name from the seed code (the `def` line)
- The `test_` function and `__main__` block must use the actual function name
- Type annotate everything, run clean under `mypy --strict`
- Strongly prefer standard library
- If the input file is missing or malformed, print a clear error to stderr and exit with code 1
- On success, print to stdout: `✓ Challenge #NNN "<title>" saved to challenges/challenge_NNN.py`

---