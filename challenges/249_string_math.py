# Daily Coding challenge #249 (2026-04-16) - freeCodeCamp.org
# String Math
# Given a string with numbers and other characters, perform math on the numbers based
# on the count of non-digit characters between the numbers.

# If the count of characters separating two numbers is even, use addition.
# If it's odd, use subtraction.
# Consecutive digits form a single number.
# Operations are applied left to right.
# Ignore leading and trailing characters that aren't digits.
# For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an
# even number of characters between them. Then subtract 8 from 13 because there's an
# odd number of characters between the result and 8.
import re

from pytest import mark


def do_math(s: str) -> int:
    numbers = [int(n) for n in re.findall(r'\d+', s)]
    separators = re.split(r'\d+', s)[1:-1]  # trim edges

    # Return a signed sum
    return numbers[0] + sum(
        num if len(sep) % 2 == 0 else -num for sep, num in zip(separators, numbers[1:])
    )


tests = [
    ('3ab10c8', 5),
    ('6MINUS4', 2),
    ('9plus3', 12),
    ('5fkwo#10i#%.<>15P=@20!#B/25', 15),
    (
        "a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt",
        67,
    ),
]


@mark.parametrize('s, expected', tests)
def test_solution(s: str, expected: int) -> None:
    assert do_math(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(do_math(s))
