# Daily Coding challenge #328 (2026-07-04) - freeCodeCamp.org
# Kaprekar's Routine
# Given a 4-digit number, return the number of times you need to apply Kaprekar's
# routine until reaching 6174.
#
# Kaprekar's routine works as follows:
#
# - Arrange the digits in descending order to form the largest number
# - Arrange the digits in ascending order to form the smallest number (pad with leading
#   zeros if necessary)
# - Subtract the smaller from the larger
# - Repeat with the new number
from pytest import mark

KAPREKAR = 6174


def do_kaprekar(n: int) -> int:
    digits = sorted(f'{n:04d}')
    return int(''.join(digits[::-1])) - int(''.join(digits))


def kaprekar(n: int) -> int:
    if not 1000 <= n <= 9999:
        raise ValueError(f'{n} is not a 4-digit number')
    if len(set(f'{n:04d}')) == 1:
        raise ValueError(f'{n} is a repdigit and never reaches {KAPREKAR}')

    steps = 0
    while n != KAPREKAR:
        n = do_kaprekar(n)
        steps += 1
    return steps


tests = [
    (1234, 3),
    (2025, 6),
    (7173, 4),
    (3164, 7),
    (8082, 2),
]


@mark.parametrize('n, expected', tests)
def test_kaprekar(n: int, expected: int) -> None:
    assert kaprekar(n) == expected


if __name__ == '__main__':
    n, expected = tests[4]
    print(kaprekar(n))
