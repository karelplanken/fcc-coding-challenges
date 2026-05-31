# Daily Coding challenge #276 (2026-05-13) - freeCodeCamp.org
# Offending Element
# Given an array of integers that is sorted in ascending order except for one
# out-of-place element, return the index of that element.
# If more than one element could be considered out of place, return the index of the
# first one.
from pytest import mark


def find_offender(arr: list[int]) -> int:
    return next(
        (
            (i if i == 0 or arr[i - 1] <= arr[i + 1] else i + 1)
            for i in range(len(arr) - 1)
            if arr[i] > arr[i + 1]
        ),
        -1,
    )


tests = [
    ([1, 6, 2, 3, 4, 5], 1),
    ([1, 2, 3, 5, 4, 5], 3),
    ([2, 1], 0),
    ([2, 4, 1, 6, 8], 2),
    ([5, 18, 24, 33, 40, 55, 15, 68, 84, 91], 6),
]


@mark.parametrize('arr, expected', tests)
def test(arr: list[int], expected: int) -> None:
    assert find_offender(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[4]
    print(find_offender(arr))
