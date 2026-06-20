**Part 1 — Python script**

Write a Python script at `scripts/assemble_prompt_for_feedback_on_fccdcc.py`.

It reads a freeCodeCamp coding challenge `.py` file whose path is passed as `sys.argv[1]` and prints the assembled review prompt to stdout. Nothing else — no clipboard, no file I/O, just stdout.

**Input file structure (always in this exact order):**

- Line 1: challenge header, always in the form `# Daily Coding challenge #299 (2026-06-05) - freeCodeCamp.org`
- Description block: lines from line 2 up to but not including the first line starting with `from` or `import`. May contain blank lines.
- Solution block: from the first `from`/`import` line up to but not including the line starting with `tests = [`
- Test block: from `tests = [` to end of file

**Parsing rules:**
- Extract the challenge name from line 1: the substring after the date and before ` - freeCodeCamp.org`. Example: `"Best Hand"`
- Strip leading `#` and one optional space from description lines. Preserve blank lines within the description.
- Preserve solution and test blocks as raw source, stripped of leading/trailing blank lines.

**Output: print this exact prompt to stdout:**

```
Hi Claude,

given this problem:

{description}

I came up with this solution:

```python
{solution}
```

Test cases used:

```python
{tests}
```

Please grade my solution given the requirements only, forget about docstrings, and keep in mind that I came up with this solution using only what I know by heart. Can we refactor this code to improve readability, efficiency, and speed?
```

**Requirements:**
- Type annotate everything, run clean under `mypy --strict`
- Standard library only (no third-party imports)
- If `sys.argv[1]` is missing or the file is not found, print a clear error to stderr and exit with code 1

---