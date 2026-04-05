# Daily Coding challenge #238 (2026-04-05) - freeCodeCamp.org
# Digit Rotation Escape
# Given a positive integer, determine if it, or any of its rotations, is evenly
# divisible by its digit count.

# A rotation means to move the first digit to the end. For example, after 1 rotation,
# 123 becomes 231.

# Check rotation 0 (the given number) first.
# Given numbers won't contain any zeros.
# Return the first rotation number if one is found, or "none" if not.
from pytest import mark


def get_rotation(n: int) -> int | str:
    s = str(n)
    num_digits = len(s)

    for i, num in enumerate(int(s[j:] + s[:j]) for j in range(num_digits)):
        if num % num_digits == 0:
            return i

    return 'none'


tests = [
    (123, 0),
    (13579, 3),
    (24681, 'none'),
    (84138789345, 6),
]


@mark.parametrize('n, expected', tests)
def test_get_rotation(n: int, expected: int | str) -> None:
    assert get_rotation(n) == expected


if __name__ == '__main__':
    n, expected = tests[3]
    print(get_rotation(n))


# Numeric rotation implementation — equivalent to the string-slicing approach above,
# but avoids string conversion entirely. This pattern is idiomatic in lower-level
# languages (C/C++) where string conversion carries real overhead. The math works by
# splitting n at a power-of-10 boundary: left_part holds the leading k digits,
# right_part the remainder; swapping and recombining them performs the rotation.
# def get_number_of_digits(n: int) -> int:
#     digit = 0

#     while n > 0:
#         digit += 1
#         n //= 10

#     return digit


# def rotate_number(n: int, k: int, num_digits: int) -> int:
#     k %= num_digits
#     if k == 0:
#         return n

#     divisor = int(10 ** (num_digits - k))
#     left_part = n // divisor
#     right_part = n % divisor

#     return right_part * int(10**k) + left_part


# def get_rotation(n: int) -> int | str:
#     num_digits = get_number_of_digits(n)

#     for i in range(num_digits):
#         rotated = rotate_number(n, i, num_digits)
#         if rotated % num_digits == 0:
#             return i

#     return 'none'
