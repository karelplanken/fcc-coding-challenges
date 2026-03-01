# Daily Coding challenge #142 (2025-12-30) - freeCodeCamp.org
# Sum the String
# Given a string containing digits and other characters, return the sum of all numbers
# in the string.

# Treat consecutive digits as a single number. For example, "13" counts as 13,
# not 1 + 3.
# Ignore any non-digit characters.
import re

from pytest import mark


# Concise:
def string_sum(s: str) -> int:
    return sum(map(int, re.findall(r'\d+', s)))
    # return sum(int(match) for match in re.findall(r'\d+', s))


# Append a non-digit sentinel (like a space) to force the final flush:
# def string_sum(s: str) -> int:
#     total = 0
#     number = ''
#     for char in s + ' ':  # Add sentinel to trigger final flush
#         if char.isdigit():
#             number += char
#         elif number:  # Non-digit and we have accumulated digits
#             total += int(number)
#             number = ''
#     return total


# Use a helper to "flush" the accumulated number:
# def string_sum(s: str) -> int:
#     total = 0
#     number = ''

#     def flush():
#         nonlocal total, number
#         if number:
#             total += int(number)
#             number = ''

#     for char in s:
#         if char.isdigit():
#             number += char
#         else:
#             flush()
#     flush()  # Final flush
#     return total


tests = [
    ('3apples2bananas', 5),
    ('10cats5dogs2birds', 17),
    ('125344', 125344),
    ('a1b20c300', 321),
    ('a12b34c56d78e90f123g456h789i0j1k2l3m4n5', 1653),
]


@mark.parametrize('s, expected', tests)
def test_string_sum(s: str, expected: int) -> None:
    assert string_sum(s) == expected


if __name__ == '__main__':
    s, expected = tests[2]
    print(string_sum(s))
