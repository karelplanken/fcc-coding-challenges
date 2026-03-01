# Daily Coding challenge #7 (2025-08-17) - freeCodeCamp.org
# Targeted Sum
# Given an array of numbers and an integer target, find two unique numbers in the array
# that add up to the target value. Return an array with the indices of those two
# numbers, or "Target not found" if no two numbers sum up to the target.

# The returned array should have the indices in ascending order.
# def find_target(arr: list[int], target: int) -> list[int] | str:
#     for i, v in enumerate(arr):
#         for j in range(i + 1, len(arr)):
#             if v + arr[j] == target:
#                 return [i, j]
#     return 'Target not found'
from pytest import mark


def find_target(arr: list[int], target: int) -> list[int] | str:
    seen = {}  # Maps value -> index

    for i, num in enumerate(arr):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return 'Target not found'


tests = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4, 5], 6, [1, 2]),
    ([1, 3, 5, 6, 7, 8], 15, [4, 5]),
    ([1, 3, 5, 7], 14, 'Target not found'),
]


@mark.parametrize('arr, target, expected', tests)
def test_find_target(arr: list[int], target: int, expected: list[int] | str) -> None:
    assert find_target(arr, target) == expected


if __name__ == '__main__':
    arr, target, expected = tests[0]
    print(find_target(arr, target))
