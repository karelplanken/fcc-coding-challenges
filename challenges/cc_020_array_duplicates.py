"""Daily Coding Challenge #20 (2025-08-30) - freeCodeCamp.org."""

# Array Duplicates
# Given an array of integers, return an array of integers that appear more than once in
# the initial array, sorted in ascending order. If no values appear more than once,
# return an empty array.
#
# - Only include one instance of each value in the returned array.
from pytest import mark


def find_duplicates(arr: list[int]) -> list[int]:
    """Return an array of integers that appear more than once in the initial array.

    Args:
        arr: An array of integers.

    Returns:
        An array of integers that appear more than once in the initial array, sorted in
        ascending order.
    """
    seen: set[int] = set()
    duplicates: set[int] = set()

    for value in arr:
        target = duplicates if value in seen else seen
        target.add(value)

    return sorted(duplicates)


tests: list[tuple[list[int], list[int]]] = [
    ([1, 2, 3, 4, 5], []),
    ([1, 2, 3, 4, 1, 2], [1, 2]),
    (
        [2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4],
        [-6, 0, 2, 4, 5, 23],
    ),
]


@mark.parametrize('arr, expected', tests)
def test_find_duplicates(arr: list[int], expected: list[int]) -> None:
    """Test find_duplicates function."""
    assert find_duplicates(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(find_duplicates(arr))
