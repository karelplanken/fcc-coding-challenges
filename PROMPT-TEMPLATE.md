# Claude Review Prompt Template

Use this after you have completed your own first solution without AI assistance.

```text
Hi Claude,
given this problem:

<problem/challenge description>

with these requirements:

<requirements>

I came up with this solution initially:

<complete solution>

Please grade my solution against the requirements only (ignore docstrings), and keep in mind that I came up with the algorithm and core solution logic myself, using only non-generative editor assistance such as IntelliSense, linting, and formatting. Can we refactor this code to improve readability, efficiency, and speed?
```
