# Daily Coding challenge #28 (2025-09-07) - freeCodeCamp.org
# Roman Numeral Parser
# Given a string representing a Roman numeral, return its integer value.

# Roman numerals consist of the following symbols and values:

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Numerals are read left to right. If a smaller numeral appears before a larger one,
# the value is subtracted. Otherwise, values are added.
from pytest import mark


# My solution: O(n) time, O(n) space (for the values list)
def parse_roman_numeral(numeral: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Convert to values once
    values = [roman_values[char] for char in numeral]

    total = 0
    for i in range(len(values)):
        # Check if we should subtract (current < next)
        if i < len(values) - 1 and values[i] < values[i + 1]:
            total -= values[i]
        else:
            total += values[i]

    return total


# Refactored v1: O(n) time, O(1) space
# def parse_roman_numeral(numeral):
#     """Parse a Roman numeral string and return its integer value."""
#     roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

#     total = 0
#     prev_value = 0

#     # Process from right to left
#     for char in reversed(numeral):
#         current_value = roman_values[char]

#         if current_value < prev_value:
#             total -= current_value
#         else:
#             total += current_value

#         prev_value = current_value

#     return total

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
    assert parse_roman_numeral(numeral) == expected


if __name__ == '__main__':
    numeral, expected = tests[0]
    print(parse_roman_numeral(numeral))
