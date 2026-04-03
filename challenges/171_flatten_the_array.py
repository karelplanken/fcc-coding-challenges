# Daily Coding challenge #171 (2026-01-28) - freeCodeCamp.org
# Given an array that contains nested arrays, return a new array with all values
# flattened into a single, one-dimensional array. Retain the original order of the
# items in the arrays.
from pytest import mark


def flatten(arr: list) -> list:
    flat_list = []
    for el in arr:
        # Base case:
        if not isinstance(el, list):
            flat_list.append(el)
        # Recursive case:
        else:
            flat_list.extend(flatten(el))
    return flat_list


# Generator version:
# from collections.abc import Iterator
# from typing import Any
# def flatten(arr: list) -> list:
#     def _flatten_gen(items: list) -> Iterator[Any]:
#         for el in items:
#             if isinstance(el, list):
#                 yield from _flatten_gen(el)
#             else:
#                 yield el

#     return list(_flatten_gen(arr))

# Iterative version:
# def flatten(arr: list) -> list:
#     result = []
#     stack = list(reversed(arr))

#     while stack:
#         el = stack.pop()
#         if isinstance(el, list):
#             stack.extend(reversed(el))
#         else:
#             result.append(el)

#     return result

tests = [
    ([1, [2, 3], 4], [1, 2, 3, 4]),
    ([5, [4, [3, 2]], 1], [5, 4, 3, 2, 1]),
    (['A', [[[['B']]]], 'C'], ['A', 'B', 'C']),
    (
        [
            ['L', 'M', 'N'],
            ['O', ['P', 'Q', ['R', ['S', ['T', 'U']]]]],
            'V',
            ['W', ['X', ['Y', ['Z']]]],
        ],
        ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ),
    (
        [
            ['red', ['blue', ['green', ['yellow', ['purple']]]]],
            'orange',
            ['pink', ['brown']],
        ],
        ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown'],
    ),
]


@mark.parametrize('arr,expected', tests)
def test_flatten(arr: list, expected: list) -> None:
    assert flatten(arr) == expected


if __name__ == '__main__':
    arr, expected = tests[4]
    print(flatten(arr))
