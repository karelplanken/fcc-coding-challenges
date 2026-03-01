# Daily Coding challenge #166 (2026-01-23) - freeCodeCamp.org
# Hex Validator
# Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color
# must:
# Start with a #, and
# be followed by either 3 or 6 hexadecimal characters.
# Hexadecimal characters are numbers 0 through 9 and letters a through f
# (case-insensitive).
import re

from pytest import mark

HEX_COLOR_PATTERN = re.compile(r'^#([0-9a-f]{3}){1,2}$', flags=re.IGNORECASE)


def is_valid_hex(s: str) -> bool:
    return bool(HEX_COLOR_PATTERN.match(s))


# Without regex (potentially faster for simple validation)
# def is_valid_hex(s: str) -> bool:
#     if not s.startswith('#') or len(s) not in (4, 7):
#         return False
#     return all(c in '0123456789abcdefABCDEF' for c in s[1:])


tests = [
    ('#123', True),
    ('#123abc', True),
    ('#ABCDEF', True),
    ('#0a1B2c', True),
    ('#12G', False),
    ('#1234567', False),
    ('#12 3', False),
    ('fff', False),
]


@mark.parametrize('s,expected', tests)
def test_is_valid_hex(s: str, expected: bool) -> None:
    assert is_valid_hex(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(is_valid_hex(s))
