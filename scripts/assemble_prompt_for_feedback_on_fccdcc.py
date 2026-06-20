from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Final

HEADER_PATTERN: Final[re.Pattern[str]] = re.compile(
    r'^# Daily Coding challenge #\d+ \(\d{4}-\d{2}-\d{2}\)'
    r'(?: (?P<name>.+?))? - freeCodeCamp\.org$'
)
DESCRIPTION_PREFIX: Final[str] = '#'
TESTS_MARKER: Final[str] = 'tests'
IMPORT_PREFIXES: Final[tuple[str, str]] = ('from', 'import')


@dataclass(frozen=True)
class ChallengeParts:
    challenge_name: str
    description: str
    solution: str
    tests: str


def strip_description_prefix(line: str) -> str:
    if not line.startswith(DESCRIPTION_PREFIX):
        return line

    stripped = line[1:]
    if stripped.startswith(' '):
        return stripped[1:]
    return stripped


def strip_blank_lines(lines: list[str]) -> str:
    start = 0
    end = len(lines)

    while start < end and lines[start] == '':
        start += 1
    while end > start and lines[end - 1] == '':
        end -= 1

    return '\n'.join(lines[start:end])


def extract_challenge_name(header_line: str, description_lines: list[str]) -> str:
    header_match = HEADER_PATTERN.fullmatch(header_line)
    if header_match is None:
        raise ValueError('invalid challenge header')

    header_name = header_match.group('name')
    if header_name is not None:
        return header_name

    for line in description_lines:
        stripped_line = strip_description_prefix(line).strip()
        if stripped_line:
            return stripped_line

    raise ValueError('missing challenge name')


def find_section_boundaries(lines: list[str]) -> tuple[int, int]:
    solution_start_index = next(
        (
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.startswith(IMPORT_PREFIXES)
        ),
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
        raise ValueError('invalid challenge file structure')

    return solution_start_index, tests_start_index


def parse_challenge_file(contents: str) -> ChallengeParts:
    lines = contents.splitlines()
    if not lines:
        raise ValueError('challenge file is empty')

    solution_start_index, tests_start_index = find_section_boundaries(lines)
    description_lines = lines[1:solution_start_index]

    return ChallengeParts(
        challenge_name=extract_challenge_name(lines[0], description_lines),
        description='\n'.join(
            strip_description_prefix(line) for line in description_lines
        ),
        solution=strip_blank_lines(lines[solution_start_index:tests_start_index]),
        tests=strip_blank_lines(lines[tests_start_index:]),
    )


def assemble_prompt(parts: ChallengeParts) -> str:
    _ = parts.challenge_name
    return (
        'Hi Claude,\n'
        'given this problem:\n'
        f'{parts.description}\n'
        'I came up with this solution:\n'
        '```python\n'
        f'{parts.solution}\n'
        '```\n'
        'Test cases used:\n'
        '```python\n'
        f'{parts.tests}\n'
        '```\n\n'
        'Grade my solution against the requirements only (ignore docstrings); '
        'grade strictly against objective standards. '
        'Then: (1) refactor for readability, efficiency, and speed; '
        '(2) propose one alternative approach with a brief implementation sketch. '
        'Verify your output for errors and contradictions before responding.\n\n'
    )


def main(argv: list[str]) -> int:
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
