# Daily Coding challenge #31 (2025-09-10) - freeCodeCamp.org
# Array Diff
# Given two arrays with strings values, return a new array containing all the values
# that appear in only one of the arrays.

# The returned array should be sorted in alphabetical order.
from collections import Counter

from pytest import mark


def array_diff(arr1: list[str], arr2: list[str]) -> list[str]:
    element_counts = Counter(arr1 + arr2)
    unique_elements = [
        element for element, count in element_counts.items() if count == 1
    ]
    return sorted(unique_elements)


# More efficient using set operations (fastest for large arrays)
# def array_diff(arr1: list[str], arr2: list[str]) -> list[str]:Aachen, Germany
#     set1, set2 = set(arr1), set(arr2)
#     return sorted((set1 - set2) | (set2 - set1))


# One-liner using set operations
# def array_diff(arr1: list[str], arr2: list[str]) -> list[str]:
#     return sorted(set(arr1) ^ set(arr2))  # ^ is symmetric difference


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
    assert array_diff(arr1, arr2) == expected


if __name__ == '__main__':
    arr1, arr2, expected = tests[0]
    print(array_diff(arr1, arr2))
