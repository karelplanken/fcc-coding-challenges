# Daily Coding challenge #221 (2026-03-19) - freeCodeCamp.org
# Inverted Matrix
# Given a matrix (an array of arrays) filled with two distinct values, return a new
# matrix where all occurrences of one value are swapped with the other.

# For example, given:

# [
#   ["a", "b"],
#   ["a", "a"]
# ]
# Return:

# [
#   ["b", "a"],
#   ["b", "b"]
# ]
from pytest import mark

AnyMatrix = list[list[int | float | str]]


def invert_matrix(
    matrix: AnyMatrix,
) -> AnyMatrix:

    value_1, value_2 = set(value for row in matrix for value in row)

    return [
        [value_1 if value == value_2 else value_2 for value in row] for row in matrix
    ]


tests: list[tuple[AnyMatrix, AnyMatrix]] = [
    ([['a', 'b'], ['a', 'a']], [['b', 'a'], ['b', 'b']]),
    ([[1, 0, 1], [1, 1, 1], [0, 1, 0]], [[0, 1, 0], [0, 0, 0], [1, 0, 1]]),
    (
        [
            ['apple', 'banana', 'banana', 'apple'],
            ['banana', 'apple', 'apple', 'banana'],
            ['banana', 'banana', 'banana', 'apple'],
        ],
        [
            ['banana', 'apple', 'apple', 'banana'],
            ['apple', 'banana', 'banana', 'apple'],
            ['apple', 'apple', 'apple', 'banana'],
        ],
    ),
    (
        [
            [6, 7, 7, 7, 6],
            [7, 6, 7, 6, 7],
            [7, 7, 6, 7, 7],
            [7, 6, 7, 6, 7],
            [6, 7, 7, 7, 6],
        ],
        [
            [7, 6, 6, 6, 7],
            [6, 7, 6, 7, 6],
            [6, 6, 7, 6, 6],
            [6, 7, 6, 7, 6],
            [7, 6, 6, 6, 7],
        ],
    ),
    (
        [[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]],
        [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]],
    ),
]


@mark.parametrize('matrix, expected', tests)
def test_invert_matrix(matrix: AnyMatrix, expected: AnyMatrix) -> None:
    assert invert_matrix(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[0]
    print(invert_matrix(matrix))
