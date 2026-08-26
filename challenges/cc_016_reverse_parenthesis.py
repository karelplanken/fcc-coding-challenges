"""Daily Coding Challenge #16 (2025-08-26) - freeCodeCamp.org."""

# Reverse Parenthesis
# Given a string that contains properly nested parentheses, return the decoded version
# of the string using the following rules:
#
# - All characters inside each pair of parentheses should be reversed.
# - Parentheses should be removed from the final result.
# - If parentheses are nested, the innermost pair should be reversed first, and then its
#   result should be included in the reversal of the outer pair.
# - Assume all parentheses are evenly balanced and correctly nested.
import re

from pytest import mark

_PATTERN = re.compile(r'\([^\(\)]*\)')


def decode(s: str) -> str:
    """Decode a string with nested parentheses.

    Reverses all characters inside each pair of parentheses. If parentheses are nested,
    the innermost pair is reversed first, and then its result is included in the
    reversal of the outer pair. Parentheses are removed from the final result.

    Expects that all parentheses in the input string are evenly balanced and correctly
    nested.

    Args:
        s: A string containing properly nested parentheses.

    Returns:
        A string with all characters inside each pair of parentheses reversed and
        parentheses removed.
    """
    while _PATTERN.search(s):
        # The lambda function is called for every non-overlapping occurrence of pattern
        s = _PATTERN.sub(lambda m: m.group()[1:-1][::-1], s)
    return s


# Stack-based approach (no regex)
# def decode(s: str) -> str:
#     stack = []
#     current = []

#     for char in s:
#         if char == '(':
#             stack.append(current)
#             current = []
#         elif char == ')':
#             current.reverse()
#             if stack:
#                 current = stack.pop() + current
#         else:
#             current.append(char)

#     return ''.join(current)


tests = [
    ('(f(b(dc)e)a)', 'abcdef'),
    ('((is?)(a(t d)h)e(n y( uo)r)aC)', 'Can you read this?'),
    ('f(Ce(re))o((e(aC)m)d)p', 'freeCodeCamp'),
]


@mark.parametrize('s, expected', tests)
def test_decode(s: str, expected: str) -> None:
    """Test decode function."""
    assert decode(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(decode(s))
