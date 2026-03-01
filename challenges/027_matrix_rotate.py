# Daily Coding challenge #27 (2025-09-06) - freeCodeCamp.org
# Matrix Rotate
# Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and
# return it. For instance, given [[1, 2], [3, 4]], which looks like this:

# 1	2
# 3	4
# You should return [[3, 1], [4, 2]], which looks like this:

# 3	1
# 4	2
from pytest import mark

# def rotate(matrix: list[list[int]]) -> list[list[int]]:
#     rows = len(matrix)
#     cols = len(matrix[0])

#     rotated_matrix = []

#     for col in range(cols):
#         rotated_matrix.append([matrix[row][col] for row in reversed(range(rows))])

#     return rotated_matrix


# Ultimate one-liner using zip and unpacking:
def rotate(matrix: list[list[int]]) -> list[list[int]]:
    """Mental Model:
    zip(*matrix) → transpose (columns become rows)
    reversed(col) → flip each column to get rotation
    """
    return [list(reversed(col)) for col in zip(*matrix)]
    # This is equivalent:

    # return [list(row) for row in zip(*matrix[::-1])]

    # But the common version:
    # matrix[::-1] → reverse row order (why?)
    # zip(*) → transpose


tests = [
    ([[1]], [[1]]),
    ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[0, 1, 0], [1, 0, 1], [0, 0, 0]], [[0, 1, 0], [0, 0, 1], [0, 1, 0]]),
]


@mark.parametrize('matrix, expected', tests)
def test_rotate(matrix: list[list[int]], expected: list[list[int]]) -> None:
    assert rotate(matrix) == expected


if __name__ == '__main__':
    matrix, expected = tests[1]
    print(rotate(matrix))
