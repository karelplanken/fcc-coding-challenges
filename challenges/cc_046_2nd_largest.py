"""Daily Coding Challenge #46 (2025-09-25) - freeCodeCamp.org."""

# 2nd Largest
# Given an array, return the second largest distinct number.
from pytest import mark


def second_largest(arr: list[int | float]) -> int | float:
    """Finds the second largest distinct number.

    Args:
        arr: List of numbers.

    Returns:
        The second largest distinct number.

    Raises:
        ValueError: If `arr` does not contain two distinct numbers.
    """
    distinct = set(arr)
    if len(distinct) < 2:
        msg = 'at least two distinct numbers must be provided'
        raise ValueError(msg)

    distinct.remove(max(distinct))
    return max(distinct)


tests: list[tuple[list[int | float], int | float]] = [
    ([1, 2, 3, 4], 3),
    ([20, 139, 94, 67, 31], 94),
    ([2, 3, 4, 6, 6], 4),
    ([10, -17, 55.5, 44, 91, 0], 55.5),
    ([1, 0, -1, 0, 1, 0, -1, 1, 0], 0),
]


@mark.parametrize('arr, expected', tests)
def test_second_largest(arr: list[int | float], expected: int | float) -> None:
    """Test second_largest function."""
    assert second_largest(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[0]
    print(second_largest(arr))
