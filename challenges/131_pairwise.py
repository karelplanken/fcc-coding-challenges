# Daily Coding challenge #131 (2025-12-19) - freeCodeCamp.org
# Pairwise
# Given an array of integers and a target number, find all pairs of elements in the
# array whose values add up to the target and return the sum of their indices.

# For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

# 2 and 8 (2 + 8 = 10), whose indices are 0 and 4
# 4 and 6 (4 + 6 = 10), whose indices are 2 and 3
# Add all the indices together to get a return value of 9.
from pytest import mark

# Verbose and very readable, O(n²)
# def pairwise(arr: list[int], target: int) -> int:
#     n = len(arr)
#     sum_idxs = 0

#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == target:
#                 print(i, j)
#                 sum_idxs += i + j

#     return sum_idxs


# Concise and advanced, O(n²)
def pairwise(arr: list[int], target: int) -> int:
    n = len(arr)

    # Generate all unique pairs (i,j) where i < j
    return sum(
        i + j
        for i in range(n - 1)
        for j in range(i + 1, n)
        if arr[i] + arr[j] == target
    )


# Below is an attempted optimization that doesn't fully work due to an implied
# constaint of unique indices only but the description asks for ALL PAIRS
# Efficient, O(n)
# def pairwise(arr: list[int], target: int) -> int:
#     """Find pairs that sum to target and return sum of their indices."""
#     seen = {}  # Maps value -> index
#     sum_idxs = 0
#     used_indices = set()

#     for i, value in enumerate(arr):
#         complement = target - value
#         print(f'{i=}, {value=}: {complement=}, {seen=}')

#         # Check if complement exists and hasn't been used
#         if complement in seen and seen[complement] not in used_indices:
#             j = seen[complement]
#             sum_idxs += i + j
#             used_indices.add(i)
#             used_indices.add(j)

#         # Only add to seen if not yet used (prevents reuse)
#         if i not in used_indices:
#             seen[value] = i

#     return sum_idxs


tests = [
    ([2, 3, 4, 6, 8], 10, 9),
    ([4, 1, 5, 2, 6, 3], 7, 15),
    ([-30, -15, 5, 10, 15, -5, 20, -40], -20, 22),
    ([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24, 10),
    ([3, 5, 2, 5, 5], 10, 16),
]


@mark.parametrize('arr, target, expected', tests)
def test_pairwise(arr: list[int], target: int, expected: int) -> None:
    assert pairwise(arr, target) == expected


if __name__ == '__main__':
    arr, target, expected = tests[4]
    print(pairwise(arr, target))
