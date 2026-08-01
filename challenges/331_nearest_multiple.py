# Daily Coding challenge #331 (2026-07-07) - freeCodeCamp.org
# Nearest Multiple
# Given two integers, round the first to the nearest multiple of the second.
from pytest import mark


def round_to_nearest_multiple(num: int, multiple: int) -> int:
    quotient, remainder = divmod(num, multiple)
    if 2 * remainder > multiple:  # ties round down, matching original behavior
        quotient += 1
    return quotient * multiple


tests = [
    (5, 3, 6),
    (17, 4, 16),
    (43, 5, 45),
    (38, 11, 33),
    (93, 12, 96),
]


@mark.parametrize('num, multiple, expected', tests)
def test_round_to_nearest_multiple(num: int, multiple: int, expected: int) -> None:
    assert round_to_nearest_multiple(num, multiple) == expected


if __name__ == '__main__':
    num, multiple, expected = tests[4]
    print(round_to_nearest_multiple(num, multiple))
