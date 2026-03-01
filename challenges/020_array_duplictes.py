# Daily Coding challenge #20 (2025-08-30) - freeCodeCamp.org
# Array Duplicates
# Given an array of integers, return an array of integers that appear more than once in
# the initial array, sorted in ascending order. If no values appear more than once,
# return an empty array.

# Only include one instance of each value in the returned array.
from pytest import mark


def find_duplicates(arr: list[int]) -> list[int]:
    seen = set()
    duplicates = set()
    for value in arr:
        if value in seen:
            duplicates.add(value)
        seen.add(value)

    return sorted(duplicates)


tests = [
    ([1, 2, 3, 4, 5], []),
    ([1, 2, 3, 4, 1, 2], [1, 2]),
    (
        [2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4],
        [-6, 0, 2, 4, 5, 23],
    ),
]


@mark.parametrize('arr, expected', tests)
def test_find_duplicates(arr: list[int], expected: list[int]) -> None:
    assert find_duplicates(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(find_duplicates(arr))
