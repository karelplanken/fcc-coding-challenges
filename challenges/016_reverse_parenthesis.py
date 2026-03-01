# Daily Coding challenge #16 (2025-08-26) - freeCodeCamp.org
# Reverse Parenthesis
# Given a string that contains properly nested parentheses, return the decoded version
# of the string using the following rules:

# All characters inside each pair of parentheses should be reversed.
# Parentheses should be removed from the final result.
# If parentheses are nested, the innermost pair should be reversed first, and then its
# result should be included in the reversal of the outer pair.
# Assume all parentheses are evenly balanced and correctly nested.
import re

from pytest import mark


def reverse_and_remove(substring: str, to_remove: list[str]) -> str:
    reversed_substring = substring[::-1]

    for pattern in to_remove:
        reversed_substring = reversed_substring.replace(pattern, '')

    return reversed_substring


def decode(s: str) -> str:
    pattern = r'\([^\(\)]*\)'
    parentheses_list = ['(', ')']

    while True:
        to_reverse = re.findall(pattern, s)
        if len(to_reverse) == 0:
            return s
        for substring in to_reverse:
            replacement = reverse_and_remove(substring, parentheses_list)
            s = s.replace(substring, replacement)


# More efficient with single pass per level
# import re

# def decode(s: str) -> str:
#     pattern = r'\([^\(\)]*\)'

#     while '(' in s:
#         # Use sub() to replace all matches in one pass
#         s = re.sub(pattern, lambda m: m.group()[1:-1][::-1], s)

#     return s

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
    assert decode(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(decode(s))
