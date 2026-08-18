"""Assemble a prompt for feedback on a challenge solution.

This script reads a challenge file, extracts the description, solution, and tests,
and formats them into a prompt suitable for feedback.
Usage:
    python assemble_prompt_for_feedback_on_fccdcc.py <challenge-file>
The challenge file should have the following structure:
    - Header line with the format:
        \"\"\"Daily Coding challenge #<number> (<date>) - freeCodeCamp.org.\"\"\"
    - Description section starting with a line prefixed by '#'
    - Solution section starting with import statements
    - Tests section starting with the line 'tests = ['
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Final

HEADER_PATTERN: Final[re.Pattern[str]] = re.compile(
    r'^"""Daily Coding Challenge #\d+ \(\d{4}-\d{2}-\d{2}\) - freeCodeCamp\.org\."""$'
)
DESCRIPTION_PREFIX: Final[str] = '#'
TESTS_MARKER: Final[str] = 'tests'
IMPORT_PREFIXES: Final[tuple[str, str]] = ('from', 'import')


@dataclass(frozen=True)
class ChallengeParts:
    """Parts of a challenge file."""

    challenge_name: str
    description: str
    solution: str
    tests: str


def check_header_format(header_line: str) -> None:
    """Checks that the first line meets expected value.

    Regex HEADER_PATTERN is used to validate the header line.

    Args:
        header_line: The first line of the challenge file.

    Raises:
        ValueError: If the header line does not match the expected format.
    """
    header_match = HEADER_PATTERN.fullmatch(header_line)
    if header_match is None:
        msg = 'invalid challenge header'
        raise ValueError(msg)


def strip_description_prefix(line: str) -> str:
    """Strips the description prefix from line.

    Args:
        line: The line to strip.

    Returns:
        The line with the description prefix removed.
    """
    if not line.startswith(DESCRIPTION_PREFIX):
        return line

    return line.removeprefix(DESCRIPTION_PREFIX).strip()


def strip_blank_lines(lines: list[str]) -> str:
    """Strips leading and trailing blank lines from a list of lines.

    Args:
        lines: The list of lines to strip.

    Returns:
        Single string of lines, with leading and trailing blank
        lines removed.
    """
    start = 0
    end = len(lines)

    while start < end and lines[start] == '':
        start += 1
    while end > start and lines[end - 1] == '':
        end -= 1

    return '\n'.join(lines[start:end])


def extract_challenge_name(description_lines: list[str]) -> str:
    """Retrieve the challenge name.

    Args:
        description_lines: The lines containing the challenge description.

    Returns:
        The challenge name.

    Raises:
        ValueError: If the challenge name line does not start with the expected prefix.
    """
    if not description_lines[0].startswith(DESCRIPTION_PREFIX):
        msg = 'invalid challenge name line'
        raise ValueError(msg)
    challenge_name = description_lines[0].removeprefix(DESCRIPTION_PREFIX).strip()
    return challenge_name


def find_section_boundaries(lines: list[str]) -> tuple[int, int]:
    """Find the indices of the solution and tests sections.

    Args:
        lines: The lines of the challenge file.

    Returns:
        A tuple containing the indices of the solution and tests sections.

    Raises:
        ValueError: If the solution or tests sections are not found.
    """
    solution_start_index = next(
        (index for index, line in enumerate(lines) if line.startswith(IMPORT_PREFIXES)),
        -1,
    )
    tests_start_index = next(
        (index for index, line in enumerate(lines) if line.startswith(TESTS_MARKER)),
        -1,
    )

    if (
        solution_start_index == -1
        or tests_start_index == -1
        or tests_start_index <= solution_start_index
    ):
        msg = f'could not find solution/tests section boundaries in {len(lines)} lines'
        raise ValueError(msg)

    return solution_start_index, tests_start_index


def parse_challenge_file(contents: str) -> ChallengeParts:
    """Parse the challenge file contents into its components.

    Args:
        contents: The contents of the challenge file.

    Returns:
        A ChallengeParts object containing:
            - challenge name
            - description
            - solution
            - tests

    Raises:
        ValueError: If the challenge file is empty or does not have the expected format.
    """
    lines = contents.splitlines()
    if not lines:
        msg = 'empty challenge file'
        raise ValueError(msg)

    check_header_format(lines[0])

    solution_start_index, tests_start_index = find_section_boundaries(lines)
    description_lines = lines[2:solution_start_index]

    return ChallengeParts(
        challenge_name=extract_challenge_name(description_lines),
        description='\n'.join(
            strip_description_prefix(line) for line in description_lines[1:]
        ),
        solution=strip_blank_lines(lines[solution_start_index:tests_start_index]),
        tests=strip_blank_lines(lines[tests_start_index:]),
    )


def assemble_prompt(parts: ChallengeParts) -> str:
    """Assemble the prompt for feedback on the challenge solution.

    Args:
        parts: The ChallengeParts object containing:
            - challenge name
            - description
            - solution
            - tests

    Returns:
        A string containing the assembled prompt for feedback.
    """
    return (
        'Hi Claude,\n'
        'given this problem:\n\n'
        f'{parts.challenge_name}\n\n'
        f'{parts.description}\n\n'
        'I came up with this solution:\n\n'
        '```python\n'
        f'{parts.solution}\n'
        '```\n\n'
        'Test cases used:\n\n'
        '```python\n'
        f'{parts.tests}\n'
        '```\n\n'
        'Context: this comes from a personal coding-challenge repo with a fixed '
        'harness. The test cases are provided by the challenge itself, not authored '
        'by me — treat them as requirements/spec, not as a demonstration of my own '
        "test-design judgment, and don't evaluate their coverage as a hiring signal. "
        'The only thing I write is the solution function. The `@mark.parametrize` '
        'decorator, the test function signature, `tests`, and the `if __name__ == '
        "'__main__'` block are fixed and kept identical in structure across all "
        'challenge files; `__main__` is debugging scaffolding used while developing, '
        "not part of the evaluation. The seed function's parameter count, order, and "
        'return contract are also fixed by the harness — only parameter *names* are '
        'mine to choose (the tests never call it via keyword arguments). Do not read '
        'the fixed shape of that signature as a design decision or count it against '
        'the assessment.\n'
        'Evaluate the solution the way a senior engineer doing code review would '
        'assess the code on its own merits — do not default to a junior-level '
        'assessment or treat that as the baseline to be argued up from. Consider: '
        'correctness against the problem description; the quality of the algorithm '
        'and data structures chosen, including efficiency; code clarity and '
        'idiomatic style; and whether edge-case or ambiguous behavior implied by the '
        'description itself (e.g. tie-breaks, invalid input) — not by the provided '
        'tests — was handled deliberately. The provided tests are a correctness '
        'check, not a checklist of edge cases the solution is expected to anticipate '
        'beyond what the problem description actually implies. Give a hiring-relevant '
        'assessment as the first line, choosing freely across the full range from '
        '"junior-ready" through "senior-level" — state it plainly rather than '
        'reaching for a hedge — with a short justification grounded in specific '
        'evidence from the code. Note any strengths that would stand out for a '
        'career-transitioner without inflating the assessment, and any genuine '
        'weaknesses without inflating them either. Calibrate against realistic '
        'professional practice, not idealized exhaustive coverage.\n'
        'Then: (1) refactor for readability, efficiency, and speed; (2) propose one '
        'alternative approach with a brief implementation sketch. Verify your output '
        'for errors and contradictions before responding.\n'
    )


def main(argv: list[str]) -> int:
    """Main function to assemble the prompt for feedback on a challenge solution.

    Args:
        argv: The command-line arguments passed to the script.

    Returns:
        An integer exit code (0 for success, 1 for error).
    """
    if len(argv) < 2:
        print('Error: missing challenge file path.', file=sys.stderr)
        return 1

    input_path = Path(argv[1])

    try:
        contents = input_path.read_text(encoding='utf-8')
        prompt = assemble_prompt(parse_challenge_file(contents))
    except FileNotFoundError:
        print(f'Error: file not found: {input_path}', file=sys.stderr)
        return 1
    except ValueError as error:
        print(f'Error: {error}.', file=sys.stderr)
        return 1

    print(prompt)
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
