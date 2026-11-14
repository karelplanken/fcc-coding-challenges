"""Daily Coding Challenge #95 (2025-11-13) - freeCodeCamp.org."""

# Array Shift
# Given an array and an integer representing how many positions to shift the array,
# return the shifted array.
#
# - A positive integer shifts the array to the left.
# - A negative integer shifts the array to the right.
# - The shift wraps around the array.
#
# For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3,
# 1].
from pytest import mark


def shift_array[T](arr: list[T], n: int) -> list[T]:
    """Shift a list by n positions, wrapping around.

    A positive n shifts left, a negative n shifts right. The input list is
    not modified.

    Args:
        arr: The list to shift.
        n: The number of positions to shift.

    Returns:
        A new, shifted list.

    Raises:
        ValueError: If the list is empty.
    """
    if not arr:
        msg = 'Array must not be empty'
        raise ValueError(msg)

    k = n % len(arr)
    return arr[k:] + arr[:k]


tests: list[tuple[list[int | str], int, list[int | str]]] = [
    ([1, 2, 3], 1, [2, 3, 1]),
    ([1, 2, 3], -1, [3, 1, 2]),
    (['alpha', 'bravo', 'charlie'], 5, ['charlie', 'alpha', 'bravo']),
    (['alpha', 'bravo', 'charlie'], -11, ['bravo', 'charlie', 'alpha']),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15, [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]),
]


@mark.parametrize('arr, n, expected', tests)
def test_shift_array(arr: list[int | str], n: int, expected: list[int | str]) -> None:
    """Test shift_array function."""
    assert shift_array(arr, n) == expected


if __name__ == '__main__':
    arr, n, expected = tests[0]
    print(shift_array(arr, n))
