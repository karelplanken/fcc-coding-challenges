"""Daily Coding Challenge #68 (2025-10-17) - freeCodeCamp.org."""

# Credit Card Masker
# Given a string of credit card numbers, return a masked version of it using the
# following constraints:
#
# - The string will contain four sets of four digits (0-9), with all sets being
#   separated by a single space, or a single hyphen (-).
# - Replace all numbers, except the last four, with an asterisk (*).
# - Leave the remaining characters unchanged.
#
# For example, given "4012-8888-8888-1881" return "****-****-****-1881".
import re

from pytest import mark

_PATTERN = re.compile(
    r'[0-9]{4}(?P<s1>[- ])[0-9]{4}(?P<s2>[- ])[0-9]{4}(?P<s3>[- ])(?P<last4>[0-9]{4})'
)


def mask(card: str) -> str:
    """Mask all but the last four digits of a credit card number.

    Args:
        card: Four groups of four ASCII digits. Each separator is a single
            hyphen or a single space; mixed separators are allowed.

    Returns:
        The card number with the first twelve digits replaced by asterisks,
        separators preserved.

    Raises:
        ValueError: If the input is not in the expected format.
    """
    match = _PATTERN.fullmatch(card)
    if match is None:
        msg = 'invalid credit card format'
        raise ValueError(msg)
    return match.expand(r'****\g<s1>****\g<s2>****\g<s3>\g<last4>')


tests = [
    ('4012-8888-8888-1881', '****-****-****-1881'),
    ('5105 1051 0510 5100', '**** **** **** 5100'),
    ('6011 1111 1111 1117', '**** **** **** 1117'),
    ('2223-0000-4845-0010', '****-****-****-0010'),
]


@mark.parametrize('card, expected', tests)
def test_mask(card: str, expected: str) -> None:
    """Test mask function."""
    assert mask(card) == expected


if __name__ == '__main__':
    card, expected = tests[0]
    print(mask(card))
