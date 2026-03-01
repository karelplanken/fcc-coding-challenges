# Daily Coding challenge #53 (2025-10-02) - freeCodeCamp.org
# Decimal to Binary
# Given a non-negative integer, return its binary representation as a string.

# A binary number uses only the digits 0 and 1 to represent any number. To convert a
# decimal number to binary, repeatedly divide the number by 2 and record the remainder.
# Repeat until the number is zero. Read the remainders last recorded to first.
# For example, to convert 12 to binary:

# 12 ÷ 2 = 6 remainder 0
# 6 ÷ 2 = 3 remainder 0
# 3 ÷ 2 = 1 remainder 1
# 1 ÷ 2 = 0 remainder 1
# 12 in binary is 1100.
from pytest import mark


# Iterative approach:
def to_binary(decimal: int) -> str:
    if decimal == 0:
        return '0'

    bin_list = []
    while decimal > 0:
        decimal, remainder = divmod(decimal, 2)
        bin_list.append(remainder)

    return ''.join(map(str, reversed(bin_list)))


# Solution using recursion:
# def to_binary(decimal: int) -> str:
#     if decimal == 0:
#         return '0'

#     def get_binary_string(decimal: int, binary_string: str = '') -> str:
#         if decimal == 0:
#             return binary_string

#         quotient, remainder = divmod(decimal, 2)
#         return get_binary_string(quotient, str(remainder) + binary_string)

#     return get_binary_string(decimal)


# Solution using built-in function:
# def to_binary(decimal: int) -> str:
#     return bin(decimal)[2:]

# Solution using string formatting:
# def to_binary(decimal: int) -> str:
#     return f'{decimal:b}'

tests = [
    (5, '101'),
    (12, '1100'),
    (50, '110010'),
    (99, '1100011'),
]


@mark.parametrize('decimal, expected', tests)
def test_to_binary(decimal: int, expected: str) -> None:
    assert to_binary(decimal) == expected


if __name__ == '__main__':
    binary, expected = tests[3]
    print(to_binary(binary))
