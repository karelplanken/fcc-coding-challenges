import ast
import os
import re
import sys
import tomllib
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from textwrap import TextWrapper
from typing import Final

SERIES_START: Final[date] = date(2025, 8, 11)
OUTPUT_DIR: Final[Path] = (
    Path.home() / 'python-projects/fcc-coding-challenges/challenges'
)
OUTPUT_NAME_TEMPLATE: Final[str] = '{number:03d}_{title}.py'
USAGE: Final[str] = 'Usage: uv run scripts/process_challenge_md.py challenge.md'
FRONTMATTER_PATTERN: Final[re.Pattern[str]] = re.compile(
    r'\A---\n(?P<frontmatter>.*?)\n---\n(?P<body>.*)\Z',
    re.DOTALL,
)
TITLE_PATTERN: Final[re.Pattern[str]] = re.compile(
    r'^Challenge (?P<number>\d+): (?P<title>.+)$'
)
SEED_BLOCK_PATTERN: Final[re.Pattern[str]] = re.compile(
    r'## --seed-contents--\n\n```py\n(?P<code>.*?)\n```',
    re.DOTALL,
)
ASSERT_METHOD_NAMES: Final[frozenset[str]] = frozenset({'assertEqual', 'assertIs'})
DESCRIPTION_MARKER: Final[str] = '# --description--'
HINTS_MARKER: Final[str] = '# --hints--'
SEED_MARKER: Final[str] = '# --seed--'
SOLUTIONS_MARKER: Final[str] = '# --solutions--'
COMMENT_PREFIX: Final[str] = '# '
RUFF_CONFIG_ENV_VAR: Final[str] = 'RUFFTOML'


@dataclass(frozen=True)
class ChallengeMetadata:
    number: int
    title: str
    challenge_date: date


@dataclass(frozen=True)
class ParsedTestCase:
    function_name: str
    function_call: str
    args_literal: str
    expected_literal: str


@dataclass(frozen=True)
class SeedFunction:
    name: str
    parameter_names: list[str]


def normalize_newlines(text: str) -> str:
    return text.replace('\r\n', '\n').replace('\r', '\n')


def challenge_date_from_number(number: int) -> date:
    return SERIES_START + timedelta(days=number - 1)


def load_comment_line_width() -> int:
    ruff_config_value = os.environ.get(RUFF_CONFIG_ENV_VAR)
    if ruff_config_value is None or ruff_config_value == '':
        raise ValueError(f'{RUFF_CONFIG_ENV_VAR} is not set')

    ruff_config_path = Path(ruff_config_value).expanduser()
    try:
        with ruff_config_path.open('rb') as config_file:
            config = tomllib.load(config_file)
    except FileNotFoundError as error:
        raise ValueError(f'ruff.toml not found: {ruff_config_path}') from error
    except OSError as error:
        raise ValueError(f'failed to read ruff.toml: {ruff_config_path}') from error
    except tomllib.TOMLDecodeError as error:
        raise ValueError(f'ruff.toml is invalid: {ruff_config_path}') from error

    line_length = config.get('line-length')
    if not isinstance(line_length, int) or line_length < len(COMMENT_PREFIX):
        raise ValueError('ruff.toml does not define a valid line-length')

    return line_length


def parse_frontmatter(contents: str) -> tuple[ChallengeMetadata, str]:
    match = FRONTMATTER_PATTERN.fullmatch(normalize_newlines(contents))
    if match is None:
        raise ValueError('input is missing valid frontmatter')

    frontmatter = match.group('frontmatter')
    title_value: str | None = None

    for line in frontmatter.splitlines():
        key, separator, value = line.partition(':')
        if separator == '':
            raise ValueError(f'malformed frontmatter line: {line}')
        if key.strip() == 'title':
            try:
                parsed_value = ast.literal_eval(value.strip())
            except (SyntaxError, ValueError) as error:
                raise ValueError(
                    'frontmatter title is not a valid quoted string'
                ) from error
            if not isinstance(parsed_value, str):
                raise ValueError('frontmatter title is not a string')
            title_value = parsed_value
            break

    if title_value is None:
        raise ValueError('frontmatter is missing title')

    title_match = TITLE_PATTERN.fullmatch(title_value)
    if title_match is None:
        raise ValueError('frontmatter title does not match "Challenge NNN: Title"')

    challenge_number = int(title_match.group('number'))
    challenge_title = title_match.group('title')

    return (
        ChallengeMetadata(
            number=challenge_number,
            title=challenge_title,
            challenge_date=challenge_date_from_number(challenge_number),
        ),
        match.group('body'),
    )


def output_path_for(metadata: ChallengeMetadata) -> Path:
    return OUTPUT_DIR / OUTPUT_NAME_TEMPLATE.format(
        number=metadata.number, title=metadata.title
    )


def prompt_for_overwrite(output_path: Path) -> None:
    if not output_path.exists():
        return

    try:
        print(
            f'Overwrite {output_path.relative_to(OUTPUT_DIR.parent)}? [y/N]: ',
            end='',
            file=sys.stderr,
            flush=True,
        )
        answer = input()
    except EOFError as error:
        raise ValueError(
            f'output file already exists: {output_path.relative_to(OUTPUT_DIR.parent)}'
        ) from error

    if answer.strip().lower() not in {'y', 'yes'}:
        raise ValueError(
            f'output file already exists: {output_path.relative_to(OUTPUT_DIR.parent)}'
        )


def extract_section(text: str, start_marker: str, end_marker: str) -> str:
    start_index = text.find(start_marker)
    if start_index == -1:
        raise ValueError(f'missing section marker: {start_marker}')

    content_start = start_index + len(start_marker)
    end_index = text.find(end_marker, content_start)
    if end_index == -1:
        raise ValueError(f'missing section marker: {end_marker}')

    return text[content_start:end_index].strip()


def extract_description(body: str) -> str:
    return extract_section(body, DESCRIPTION_MARKER, HINTS_MARKER)


def extract_hints_block(body: str) -> str:
    return extract_section(body, HINTS_MARKER, SEED_MARKER)


def extract_seed_code(body: str) -> str:
    seed_section = extract_section(body, SEED_MARKER, SOLUTIONS_MARKER)
    match = SEED_BLOCK_PATTERN.search(seed_section)
    if match is None:
        raise ValueError('seed section is missing a Python code block')
    return match.group('code').strip()


def source_segment(source: str, node: ast.AST) -> str:
    segment = ast.get_source_segment(source, node)
    if segment is None:
        raise ValueError('could not extract source segment from hint')
    return segment


def extract_called_function_name(function_call: ast.Call) -> str:
    function = function_call.func
    if isinstance(function, ast.Name):
        return function.id
    raise ValueError('hint assertion does not call a plain function name')


def format_args_literal(argument_sources: list[str]) -> str:
    if not argument_sources:
        return '()'
    if len(argument_sources) == 1:
        return f'{argument_sources[0]}'
    return f'{", ".join(argument_sources)}'


def normalize_hint_assertion_line(line: str) -> str:
    if line.endswith('`)'):
        return line[:-2]
    if line.endswith('`'):
        return line[:-1]
    return line


def parse_hint_assertion(line: str) -> ParsedTestCase:
    try:
        parsed = ast.parse(line)
    except SyntaxError as error:
        raise ValueError(f'malformed hint assertion line: {line}') from error

    if len(parsed.body) != 1 or not isinstance(parsed.body[0], ast.Expr):
        raise ValueError(f'malformed hint assertion line: {line}')

    assertion = parsed.body[0].value
    if not isinstance(assertion, ast.Call):
        raise ValueError(f'malformed hint assertion line: {line}')
    if not isinstance(assertion.func, ast.Attribute):
        raise ValueError(f'malformed hint assertion line: {line}')
    if assertion.func.attr not in ASSERT_METHOD_NAMES:
        raise ValueError(f'unsupported unittest assertion in hint line: {line}')
    if len(assertion.args) != 2 or assertion.keywords:
        raise ValueError(f'malformed unittest assertion in hint line: {line}')

    function_call = assertion.args[0]
    if not isinstance(function_call, ast.Call):
        raise ValueError(f'hint assertion does not call the challenge function: {line}')
    if function_call.keywords:
        raise ValueError('hint assertions with keyword arguments are not supported')

    argument_sources = [
        source_segment(line, argument) for argument in function_call.args
    ]
    return ParsedTestCase(
        function_name=extract_called_function_name(function_call),
        function_call=source_segment(line, function_call),
        args_literal=format_args_literal(argument_sources),
        expected_literal=source_segment(line, assertion.args[1]),
    )


def extract_test_cases(body: str) -> list[ParsedTestCase]:
    hints_block = extract_hints_block(body)
    test_cases = [
        parse_hint_assertion(normalize_hint_assertion_line(stripped_line))
        for raw_line in hints_block.splitlines()
        if (stripped_line := raw_line.strip()).startswith('TestCase().assert')
    ]
    if not test_cases:
        raise ValueError('no hint assertions found')
    return test_cases


def parse_seed_function(seed_code: str) -> SeedFunction:
    try:
        module = ast.parse(seed_code)
    except SyntaxError as error:
        raise ValueError('seed code is not valid Python') from error

    for statement in module.body:
        if isinstance(statement, ast.FunctionDef):
            if statement.args.kwonlyargs:
                raise ValueError(
                    'seed function keyword-only parameters are not supported'
                )
            if statement.args.vararg is not None or statement.args.kwarg is not None:
                raise ValueError('seed function variadic parameters are not supported')
            positional_parameters = [
                *statement.args.posonlyargs,
                *statement.args.args,
            ]
            return SeedFunction(
                name=statement.name,
                parameter_names=[parameter.arg for parameter in positional_parameters],
            )
    raise ValueError('seed code does not define a function')


def validate_test_function_names(
    test_cases: list[ParsedTestCase], seed_function_name: str
) -> None:
    for test_case in test_cases:
        if test_case.function_name != seed_function_name:
            raise ValueError(
                'hint assertion function name does not match seed function: '
                f'{test_case.function_call}'
            )


def extract_argument_count(args_literal: str) -> int:
    try:
        parsed = ast.parse(f'f({args_literal})')
    except SyntaxError as error:
        raise ValueError(f'malformed test case arguments: {args_literal}') from error

    call = parsed.body[0]
    if not isinstance(call, ast.Expr) or not isinstance(call.value, ast.Call):
        raise ValueError(f'malformed test case arguments: {args_literal}')
    return len(call.value.args)


def validate_test_case_arity(
    test_cases: list[ParsedTestCase], parameter_names: list[str]
) -> None:
    for test_case in test_cases:
        argument_count = extract_argument_count(test_case.args_literal)
        if argument_count != len(parameter_names):
            raise ValueError(
                'hint argument count does not match seed function signature: '
                f'{test_case.function_call}'
            )


def render_description(description: str, comment_line_width: int) -> str:
    rendered_lines: list[str] = []

    for line in description.splitlines():
        if line == '':
            rendered_lines.append('#')
            continue

        initial_prefix = COMMENT_PREFIX
        subsequent_prefix = COMMENT_PREFIX
        if line.startswith('- '):
            initial_prefix = '# - '
            subsequent_prefix = '#   '
            line = line[2:]

        wrapper = TextWrapper(
            width=comment_line_width,
            initial_indent=initial_prefix,
            subsequent_indent=subsequent_prefix,
            break_long_words=False,
            break_on_hyphens=False,
        )
        rendered_lines.extend(wrapper.wrap(line))

    return '\n'.join(rendered_lines)


def render_tests_block(test_cases: list[ParsedTestCase]) -> str:
    return '\n'.join(
        f'    ({test_case.args_literal}, {test_case.expected_literal}),'
        for test_case in test_cases
    )


def render_test_parameter_names(parameter_names: list[str]) -> str:
    return ', '.join([*parameter_names, 'expected'])


def render_output_file(
    metadata: ChallengeMetadata,
    description: str,
    seed_code: str,
    seed_function: SeedFunction,
    test_cases: list[ParsedTestCase],
    comment_line_width: int,
) -> str:
    test_parameter_names = render_test_parameter_names(seed_function.parameter_names)
    function_arguments = ', '.join(seed_function.parameter_names)
    return (
        f'# Daily Coding challenge #{metadata.number:03d} '
        f'({metadata.challenge_date.isoformat()}) - freeCodeCamp.org\n'
        f'# {metadata.title}\n'
        f'{render_description(description, comment_line_width)}\n'
        'from pytest import mark\n'
        '\n\n'
        f'{seed_code}\n'
        '\n\n'
        'tests = [\n'
        f'{render_tests_block(test_cases)}\n'
        ']\n'
        '\n\n'
        f"@mark.parametrize('{test_parameter_names}', tests)\n"
        f'def test_{seed_function.name}({test_parameter_names}):\n'
        f'    assert {seed_function.name}({function_arguments}) == expected\n'
        '\n\n'
        "if __name__ == '__main__':\n"
        f'    {test_parameter_names} = tests[0]\n'
        f'    print({seed_function.name}({function_arguments}))\n'
    )


def write_output(output_path: Path, contents: str) -> None:
    if not OUTPUT_DIR.is_dir():
        raise ValueError(f'output directory does not exist: {OUTPUT_DIR}')
    output_path.write_text(contents, encoding='utf-8')


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(USAGE, file=sys.stderr)
        return 1

    input_path = Path(argv[1])

    try:
        comment_line_width = load_comment_line_width()
        raw_contents = input_path.read_text(encoding='utf-8')
        metadata, body = parse_frontmatter(raw_contents)
        output_path = output_path_for(metadata)
        prompt_for_overwrite(output_path)
        description = extract_description(body)
        seed_code = extract_seed_code(body)
        seed_function = parse_seed_function(seed_code)
        test_cases = extract_test_cases(body)
        validate_test_function_names(test_cases, seed_function.name)
        validate_test_case_arity(test_cases, seed_function.parameter_names)
        rendered_output = render_output_file(
            metadata=metadata,
            description=description,
            seed_code=seed_code,
            seed_function=seed_function,
            test_cases=test_cases,
            comment_line_width=comment_line_width,
        )
        write_output(output_path, rendered_output)
    except FileNotFoundError:
        print(f'Error: file not found: {input_path}', file=sys.stderr)
        return 1
    except (OSError, ValueError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1

    print(
        f'✓ Challenge #{metadata.number:03d} "{metadata.title}" saved to '
        f'{output_path.relative_to(OUTPUT_DIR.parent)}'
    )
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
