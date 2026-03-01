# Daily Coding challenge #68 (2025-10-17) - freeCodeCamp.org
# Credit Card Masker
# Given a string of credit card numbers, return a masked version of it using the
# following constraints:

# The string will contain four sets of four digits (0-9), with all sets being separated
# by a single space, or a single hyphen (-).
# Replace all numbers, except the last four, with an asterisk (*).
# Leave the remaining characters unchanged.
# For example, given "4012-8888-8888-1881" return "****-****-****-1881".
from pytest import mark


def mask(card: str) -> str:
    # Most performant way:
    return f'****{card[4]}****{card[9]}****{card[14:]}'
    # Alternative using join and enumerate:
    # return ''.join(
    #     '*' if char.isdigit() and i < 14 else char for i, char in enumerate(card)
    # )


tests = [
    ('4012-8888-8888-1881', '****-****-****-1881'),
    ('5105 1051 0510 5100', '**** **** **** 5100'),
    ('6011 1111 1111 1117', '**** **** **** 1117'),
    ('2223-0000-4845-0010', '****-****-****-0010'),
]


@mark.parametrize('card, expected', tests)
def test_mask(card: str, expected: str) -> None:
    assert mask(card) == expected


if __name__ == '__main__':
    card, expected = tests[0]
    print(mask(card))
