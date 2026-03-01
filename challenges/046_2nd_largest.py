# Daily Coding challenge #46 (2025-09-25) - freeCodeCamp.org
# 2nd Largest
# Given an array, return the second largest distinct number.
from pytest import mark


def second_largest(arr: list[int]) -> int | None:
    unique_sorted = sorted(set(arr), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None


tests = [
    ([1, 2, 3, 4], 3),
    ([20, 139, 94, 67, 31], 94),
    ([2, 3, 4, 6, 6], 4),
    ([10, -17, 55.5, 44, 91, 0], 55.5),
    ([1, 0, -1, 0, 1, 0, -1, 1, 0], 0),
]


@mark.parametrize('arr, expected', tests)
def test_second_largest(arr: list[int], expected: int | None) -> None:
    assert second_largest(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(second_largest(arr))
