# Daily Coding challenge #245 (2026-04-12) - freeCodeCamp.org
# Spiral Matrix
# Given a 2D matrix, return a flat array with all of its values in clockwise order.

# The returned array should have the top-left value first, move right along the top row,
# then down the right column, then left along the bottom row, then up the left column.
# Repeat inward for any remaining layers.

# For example, given:

# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Return [1, 2, 3, 6, 9, 8, 7, 4, 5].
from pytest import mark


def spiral_matrix[T](matrix: list[list[T]]) -> list[T]:
    # top row                   [const][var]
    # last column               [var][const]
    # last row reverse          [const][var]
    # first column reverse      [var][const]
    result: list[T] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # → first row
        result.extend(matrix[top][col] for col in range(left, right + 1))
        top += 1

        # ↓ last column
        result.extend(matrix[row][right] for row in range(top, bottom + 1))
        right -= 1

        # ← last row (only if there's still a row left)
        if top <= bottom:
            result.extend(matrix[bottom][col] for col in range(right, left - 1, -1))
            bottom -= 1

        # ↑ first column (only if there's still a column left)
        if left <= right:
            result.extend(matrix[row][left] for row in range(bottom, top - 1, -1))
            left += 1

    return result


tests: list[tuple[list[list[int | str | bool]], list[int | str | bool]]] = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (
        [
            ['a', 'b', 'c', 'd'],
            ['l', 'm', 'n', 'e'],
            ['k', 'p', 'o', 'f'],
            ['j', 'i', 'h', 'g'],
        ],
        [
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
        ],
    ),
    (
        [
            [True, False, False],
            [False, True, True],
            [False, True, False],
            [True, True, False],
        ],
        [True, False, False, True, False, False, True, True, False, False, True, True],
    ),
    (
        [
            [25, 24, 23, 22, 21],
            [10, 9, 8, 7, 20],
            [11, 2, 1, 6, 19],
            [12, 3, 4, 5, 18],
            [13, 14, 15, 16, 17],
        ],
        [
            25,
            24,
            23,
            22,
            21,
            20,
            19,
            18,
            17,
            16,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
        ],
    ),
]


@mark.parametrize('matrix, expected', tests)
def test_solution[T](matrix: list[list[T]], expected: list[T]) -> None:
    assert spiral_matrix(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[0]
    print(spiral_matrix(matrix))
