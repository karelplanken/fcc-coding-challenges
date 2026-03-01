# Daily Coding challenge #52 (2025-10-01) - freeCodeCamp.org
# Binary to Decimal
# Given a string representing a binary number, return its decimal equivalent as a
# number.

# A binary number uses only the digits 0 and 1 to represent any number. To convert
# binary to decimal, multiply each digit by a power of 2 and add them together. Start
# by multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so
# on. Once all digits have been multiplied by a power of 2, add the result together.

# For example, the binary number 101 equals 5 in decimal because:

# 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
from pytest import mark


def to_decimal(binary: str) -> int:
    # return int(binary, 2)
    return sum(int(bit) * 2**pow for pow, bit in enumerate(reversed(binary)))


tests = [
    ('101', 5),
    ('1010', 10),
    ('10010', 18),
    ('1010101', 85),
]


@mark.parametrize('binary, expected', tests)
def test_to_decimal(binary: str, expected: int) -> None:
    assert to_decimal(binary) == expected


if __name__ == '__main__':
    binary, expected = tests[3]
    print(to_decimal(binary))
