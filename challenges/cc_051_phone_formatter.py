"""Daily Coding Challenge #51 (2025-09-30) - freeCodeCamp.org."""

# Phone Number Formatter
# Given a string of eleven digits, return the string as a phone number in this format:
# "+D (DDD) DDD-DDDD".
import re

from pytest import mark

_PHONE_PATTERN = re.compile(
    r'(?P<country>\d)(?P<area>\d{3})(?P<prefix>\d{3})(?P<line>\d{4})',
    re.ASCII,
)


def format_number(number: str) -> str:
    """Format a string of eleven digits as a phone number.

    Args:
        number: A string of eleven ASCII digits.

    Returns:
        The number formatted as "+D (DDD) DDD-DDDD".

    Raises:
        ValueError: If number is not exactly eleven ASCII digits.
    """
    match = _PHONE_PATTERN.fullmatch(number)
    if match is None:
        msg = 'number must be a string of eleven digits'
        raise ValueError(msg)
    country, area, prefix, line = match.group('country', 'area', 'prefix', 'line')
    return f'+{country} ({area}) {prefix}-{line}'


tests = [
    ('05552340182', '+0 (555) 234-0182'),
    ('15554354792', '+1 (555) 435-4792'),
]


@mark.parametrize('number, expected', tests)
def test_format_number(number: str, expected: str) -> None:
    """Test format_number function."""
    assert format_number(number) == expected


if __name__ == '__main__':
    number, expected = tests[0]
    print(format_number(number))
