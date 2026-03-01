# Daily Coding challenge #151 (2026-01-08) - freeCodeCamp.org
# Sorted Array?
# Given an array of numbers, determine if the numbers are sorted in ascending order,
# descending order, or neither.

# If the given array is:

# In ascending order (lowest to highest), return "Ascending".
# In descending order (highest to lowest), return "Descending".
# Not sorted in ascending or descending order, return "Not sorted".
from pytest import mark


def is_sorted(arr: list[int | float]) -> str:
    """Determine if array is sorted in ascending, descending, or neither."""
    if len(arr) <= 1:
        return 'Ascending'

    is_ascending = True
    is_descending = True

    for idx in range(len(arr) - 1):
        if arr[idx] >= arr[idx + 1]:
            is_ascending = False
        if arr[idx] <= arr[idx + 1]:
            is_descending = False

        # Early exit: if neither condition can be true, bail out
        if not is_ascending and not is_descending:
            return 'Not sorted'

    return 'Ascending' if is_ascending else 'Descending'


# def is_sorted(arr: list[int | float]) -> str:
#     """Determine if array is sorted in ascending, descending, or neither."""
#     if len(arr) <= 1:
#         return 'Ascending'  # Convention: empty or single-element arrays are sorted

#     # Check ascending
#     if all(arr[idx] < arr[idx + 1] for idx in range(len(arr) - 1)):
#         return 'Ascending'

#     # Check descending
#     if all(arr[idx] > arr[idx + 1] for idx in range(len(arr) - 1)):
#         return 'Descending'

#     return 'Not sorted'

tests = [
    ([1, 2, 3, 4, 5], 'Ascending'),
    ([10, 8, 6, 4, 2], 'Descending'),
    ([1, 3, 2, 4, 5], 'Not sorted'),
    ([3.14, 2.71, 1.61, 0.57], 'Descending'),
    ([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9], 'Ascending'),
    ([0.4, 0.5, 0.3], 'Not sorted'),
]


@mark.parametrize(('arr', 'expected'), tests)
def test_is_sorted(arr: list[int | float], expected: str) -> None:
    assert is_sorted(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    # print(is_sorted(arr))
    print(is_sorted([5, 5, 5, 5]))
