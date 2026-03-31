# Daily Coding challenge #229 (2026-03-27) - freeCodeCamp.org
# Truncate the Text 2
# Given a string, return a new string that is truncated so that the total width of the
# characters does not exceed 50 units.

# Each character has a specific width:

# Letters	Width
# "ilI"	1
# "fjrt"	2
# "abcdeghkmnopqrstuvwxyzJL"	3
# "ABCDEFGHKMNOPQRSTUVWXYZ"	4
# The table above includes all upper and lower case letters. Additionally:

# Spaces (" ") have a width of 2

# Periods (".") have a width of 1

# If the given string is 50 units or less, return the string as-is, otherwise
# Truncate the string and add three periods at the end ("...") so it's total width,
# including the three periods, is as close as possible to 60 units without going over.
from pytest import mark

CHAR_WIDTHS = {
    **{c: 1 for c in 'ilI.'},
    **{c: 2 for c in 'fjrt '},
    # Note that 't' and 'r' are removed from the following group:
    **{c: 3 for c in 'abcdeghkmnopqsuvwxyzJL'},
    **{c: 4 for c in 'ABCDEFGHKMNOPQRSTUVWXYZ'},
}

ELLIPSIS = '...'
ELLIPSIS_WIDTH = 3
MAX_WIDTH = 50
TRUNCATION_BUDGET = MAX_WIDTH - ELLIPSIS_WIDTH  # 47


def char_width(char: str) -> int:
    try:
        return CHAR_WIDTHS[char]
    except KeyError:
        raise ValueError(f'Width for character {char!r} is unknown')


def text_width(s: str) -> int:
    return sum(char_width(c) for c in s)


def truncate_text(s: str) -> str:
    if text_width(s) <= MAX_WIDTH:
        return s

    width = 0
    for i, char in enumerate(s):
        width += char_width(char)
        if width > TRUNCATION_BUDGET:
            return s[:i] + ELLIPSIS

    return s  # unreachable, but safe fallback


tests = [
    ('The quick brown fox', 'The quick brown f...'),
    ('The silky smooth sloth', 'The silky smooth s...'),
    ('THE LOUD BRIGHT BIRD', 'THE LOUD BRIG...'),
    ('The fast striped zebra', 'The fast striped z...'),
    ('The big black bear', 'The big black bear'),
]


@mark.parametrize('s, expected', tests)
def test_truncate_text(s: str, expected: str) -> None:
    assert truncate_text(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(truncate_text(s))
