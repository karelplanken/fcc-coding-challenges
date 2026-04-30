# Daily Coding challenge #248 (2026-04-15) - freeCodeCamp.org
# Sorted Array Swap
# Given an array of integers, return a new array using the following rules:

# Sort the integers in ascending order
# Then swap all values whose index is a multiple of 3 with the value before it.
from pytest import mark


def sort_and_swap(arr: list[int]) -> list[int]:
    result = sorted(arr)
    for i in range(3, len(result), 3):
        result[i], result[i - 1] = result[i - 1], result[i]
    return result


tests = [
    ([3, 1, 2, 4, 6, 5], [1, 2, 4, 3, 5, 6]),
    ([9, 7, 5, 3, 1, 2, 4, 6, 8], [1, 2, 4, 3, 5, 7, 6, 8, 9]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 4, 3, 5, 7, 6, 8, 9]),
    ([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11], [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 12]),
    ([100, -50, 0, 75, -25, 50, -75, 25], [-75, -50, 0, -25, 25, 75, 50, 100]),
    (
        [5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2],
        [-65, -10, 0, -4, 2, 8, 5, 9, 77, 13, 88, 101, 99, 313],
    ),
]


@mark.parametrize('arr, expected', tests)
def test_solution(arr: list[int], expected: list[int]) -> None:
    assert sort_and_swap(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(sort_and_swap(arr))
