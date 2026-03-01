# Daily Coding challenge #62 (2025-10-11) - freeCodeCamp.org
# Hex to Decimal
# Given a string representing a hexadecimal number (base 16), return its decimal
# (base 10) value as an integer.

# Hexadecimal is a number system that uses 16 digits:

# 0-9 represent values 0 through 9.
# A-F represent values 10 through 15.
# Here's a partial conversion table:

# Hexadecimal	Decimal
# 0	0
# 1	1
# ...	...
# 9	9
# A	10
# ...	...
# F	15
# 10	16
# ...	...
# 9F	159
# A0	160
# ...	...
# FF	255
# 100	256
# The string will only contain characters 0–9 and A–F.
from pytest import mark

HEX_TO_DEC = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}


def hex_to_decimal(hex_str: str) -> int:
    return sum(16**i * HEX_TO_DEC[char] for i, char in enumerate(reversed(hex_str)))


# Using Horner's method:
# def hex_to_decimal(hex_str: str) -> int:
#     result = 0
#     for char in hex_str:
#         result = result * 16 + HEX_TO_DEC[char]
#     return result

tests = [
    ('A', 10),
    ('15', 21),
    ('2E', 46),
    ('FF', 255),
    ('A3F', 2623),
]


@mark.parametrize('hex_str, expected', tests)
def test_hex_to_decimal(hex_str: str, expected: int) -> None:
    assert hex_to_decimal(hex_str) == expected


if __name__ == '__main__':
    hex_str, expected = tests[4]
    print(hex_to_decimal(hex_str))
