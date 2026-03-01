# Daily Coding challenge #91 (2025-11-09) - freeCodeCamp.org
# Word Search
# Given a matrix (an array of arrays) of single letters and a word to find, return the
# start and end indices of the word in the matrix.

# The given matrix will be filled with all lowercase letters (a-z).
# The word to find will always be in the matrix exactly once.
# The word to find will always be in a straight line in one of these directions:
# left to right
# right to left
# top to bottom
# bottom to top
# For example, given the matrix:

# [
#   ["a", "c", "t"],
#   ["t", "a", "t"],
#   ["c", "t", "c"]
# ]
# And the word "cat", return:

# [[0, 1], [2, 1]]
# Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the
# indices for the "t" (end of the word).
from pytest import mark


def find_word(matrix: list[list[str]], word: str) -> list[list[int]] | None:
    rows = len(matrix)
    cols = len(matrix[0])

    word_length = len(word)

    # Iterate over rows:
    for row in range(rows):
        for col in range(cols - word_length + 1):
            print(f'{row=}, {col=} end={col + word_length}')
            m_word = ''.join(matrix[row][col : col + word_length])
            if m_word == word:
                # print('found', [row, col], [row, col + word_length - 1])
                return [[row, col], [row, col + word_length - 1]]
            elif m_word[::-1] == word:
                # print('found', [row, col + word_length - 1], [row, col])
                return [[row, col + word_length - 1], [row, col]]

    # Iterate over columns:
    for col in range(cols):
        for row in range(rows - word_length + 1):
            m_word = ''.join(matrix[i][col] for i in range(row, row + word_length))
            if m_word == word:
                # print('found', [row, col], [row + word_length - 1, col])
                return [[row, col], [row + word_length - 1, col]]
            elif m_word[::-1] == word:
                # print('found', [row + word_length - 1, col], [row, col])
                return [[row + word_length - 1, col], [row, col]]

    return None


tests = [
    ([['a', 'c', 't'], ['t', 'a', 't'], ['c', 't', 'c']], 'cat', [[0, 1], [2, 1]]),
    ([['d', 'o', 'g'], ['o', 'g', 'd'], ['d', 'g', 'o']], 'dog', [[0, 0], [0, 2]]),
    (
        [
            ['h', 'i', 's', 'h'],
            ['i', 's', 'f', 's'],
            ['f', 's', 'i', 'i'],
            ['s', 'h', 'i', 'f'],
        ],
        'fish',
        [[3, 3], [0, 3]],
    ),
    (
        [
            ['f', 'x', 'o', 'x'],
            ['o', 'x', 'o', 'f'],
            ['f', 'o', 'f', 'x'],
            ['f', 'x', 'x', 'o'],
        ],
        'fox',
        [[1, 3], [1, 1]],
    ),
]


@mark.parametrize(('matrix', 'word', 'expected'), tests)
def test_find_word(
    matrix: list[list[str]], word: str, expected: list[list[int]]
) -> None:
    assert find_word(matrix, word) == expected


if __name__ == '__main__':
    matrix, word, expected = tests[0]
    print(find_word(matrix, word), expected)
