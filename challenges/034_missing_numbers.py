# Daily Coding challenge #34 (2025-09-13) - freeCodeCamp.org
# Missing Numbers
# Given an array of integers from 1 to n, inclusive, return an array of all the missing
# integers between 1 and n (where n is the largest number in the given array).

# The given array may be unsorted and may contain duplicates.
# The returned array should be in ascending order.
# If no integers are missing, return an empty array.
from pytest import mark


def find_missing_numbers(arr: list[int]) -> list[int]:
    if not arr:
        return []
    arr_set = set(arr)
    return [i for i in range(1, max(arr)) if i not in arr_set]


tests = [
    ([1, 3, 5], [2, 4]),
    ([1, 2, 3, 4, 5], []),
    ([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]),
    ([10, 1, 10, 1, 10, 1], [2, 3, 4, 5, 6, 7, 8, 9]),
    ([3, 1, 4, 1, 5, 9], [2, 6, 7, 8]),
    ([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4], [11]),
]


@mark.parametrize('arr, expected', tests)
def test_find_missing_numbers(arr: list[int], expected: list[int]) -> None:
    assert find_missing_numbers(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[2]
    print(find_missing_numbers(arr))
