# Daily Coding challenge #252 (2026-04-19) - freeCodeCamp.org
# Unique Stair Climber
# Given a number of stairs, return how many distinct ways someone can climb them taking
# either 1 or 2 steps at a time.
from functools import cache

from pytest import mark


def get_unique_climbs(steps: int) -> int:
    # Ways to climb n steps = F(n+1): base cases are 1 way for 0 or 1 steps
    if steps <= 1:
        return 1

    curr, prev = 1, 0  # F(1), F(0) — true Fibonacci start
    for _ in range(steps):
        curr, prev = curr + prev, curr
    return curr


@cache
def get_unique_climbs_recursive(steps: int) -> int:
    if steps <= 1:
        return 1
    return get_unique_climbs_recursive(steps - 1) + get_unique_climbs_recursive(
        steps - 2
    )


tests = [
    (4, 5),
    (5, 8),
    (10, 89),
    (18, 4181),
    (29, 832040),
    (50, 20365011074),
]


@mark.parametrize('steps, expected', tests)
def test(steps: int, expected: int) -> None:
    assert get_unique_climbs(steps) == expected


@mark.parametrize('steps, expected', tests)
def test_cached_version(steps: int, expected: int) -> None:
    assert get_unique_climbs_recursive(steps) == expected


if __name__ == '__main__':
    steps, expected = tests[0]
    print(get_unique_climbs(steps))
