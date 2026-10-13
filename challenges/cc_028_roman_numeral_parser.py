"""Daily Coding Challenge #28 (2025-09-07) - freeCodeCamp.org."""

# Roman Numeral Parser
# Given a string representing a Roman numeral, return its integer value.
#
# Roman numerals consist of the following symbols and values:
#
# | Symbol | Value |
# |--------|-------|
# | I      | 1     |
# | V      | 5     |
# | X      | 10    |
# | L      | 50    |
# | C      | 100   |
# | D      | 500   |
# | M      | 1000  |
#
# - Numerals are read left to right. If a smaller numeral appears before a larger one,
#   the value is subtracted. Otherwise, values are added.
from types import MappingProxyType

from pytest import mark

_ROMAN_VALUES = MappingProxyType({
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
})


def parse_roman_numeral(numeral: str) -> int:
    """Parse a Roman numeral string and return its integer value.

    Does not validate numeral well-formedness (e.g. repeated symbols
    beyond the conventional limit, or invalid subtractive pairs) —
    only individual symbol validity and the subtraction rule.

    Args:
        numeral: A string representing a Roman numeral.

    Returns:
        The integer value of the Roman numeral.

    Raises:
        ValueError: If the input contains a character that is not a
            valid Roman numeral symbol.
    """
    total = 0
    prev_value = 0

    for char in reversed(numeral):
        if (value := _ROMAN_VALUES.get(char)) is None:
            msg = f'invalid Roman numeral character: {char!r}'
            raise ValueError(msg)

        total += value if value >= prev_value else -value
        prev_value = value

    return total


tests = [
    ('III', 3),
    ('IV', 4),
    ('XXVI', 26),
    ('XCIX', 99),
    ('CDLX', 460),
    ('DIV', 504),
    ('MMXXV', 2025),
]


@mark.parametrize('numeral, expected', tests)
def test_parse_roman_numeral(numeral: str, expected: int) -> None:
    """Test parse_roman_numeral function."""
    assert parse_roman_numeral(numeral) == expected


if __name__ == '__main__':
    numeral, expected = tests[0]
    print(parse_roman_numeral(numeral))
