"""Daily Coding Challenge #31 (2025-09-10) - freeCodeCamp.org."""

# Array Diff
# Given two arrays with strings values, return a new array containing all the values
# that appear in only one of the arrays.
#
# - The returned array should be sorted in alphabetical order.
from pytest import mark


def array_diff(arr1: list[str], arr2: list[str]) -> list[str]:
    """Returns the values that appear in exactly one of the two arrays.

    Duplicate values within an array are treated as a single occurrence,
    since only membership (not count) determines the result.

    Args:
        arr1: The first array of strings.
        arr2: The second array of strings.

    Returns:
        A new array of the symmetric-difference values, sorted alphabetically.
    """
    return sorted(set(arr1) ^ set(arr2))


tests = [
    (['apple', 'banana'], ['apple', 'banana', 'cherry'], ['cherry']),
    (['apple', 'banana', 'cherry'], ['apple', 'banana'], ['cherry']),
    (
        ['one', 'two', 'three', 'four', 'six'],
        ['one', 'three', 'eight'],
        ['eight', 'four', 'six', 'two'],
    ),
    (
        ['two', 'four', 'five', 'eight'],
        ['one', 'two', 'three', 'four', 'seven', 'eight'],
        ['five', 'one', 'seven', 'three'],
    ),
    (['I', 'like', 'freeCodeCamp'], ['I', 'like', 'rocks'], ['freeCodeCamp', 'rocks']),
]


@mark.parametrize('arr1, arr2, expected', tests)
def test_array_diff(arr1: list[str], arr2: list[str], expected: list[str]) -> None:
    """Test array_diff function."""
    assert array_diff(arr1, arr2) == expected


if __name__ == '__main__':
    arr1, arr2, expected = tests[0]
    print(array_diff(arr1, arr2))
