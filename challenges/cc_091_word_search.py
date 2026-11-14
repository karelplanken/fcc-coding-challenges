"""Daily Coding Challenge #91 (2025-11-09) - freeCodeCamp.org."""

# Word Search
# Given a matrix (an array of arrays) of single letters and a word to find, return the
# start and end indices of the word in the matrix.
#
# - The given matrix will be filled with all lowercase letters (a-z).
# - The word to find will always be in the matrix exactly once.
# - The word to find will always be in a straight line in one of these directions:
#   - left to right
#   - right to left
#   - top to bottom
#   - bottom to top
#
# For example, given the matrix:
#
# [
#   ["a", "c", "t"],
#   ["t", "a", "t"],
#   ["c", "t", "c"]
# ]
#
# And the word "cat", return:
#
# [[0, 1], [2, 1]]
#
# Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the
# indices for the "t" (end of the word).
from pytest import mark


def _locate(line: str, word: str) -> tuple[int, int] | None:
    """Return (start, end) offsets of ``word`` in ``line``, read in either direction."""
    if (i := line.find(word)) != -1:
        return i, i + len(word) - 1
    if (i := line.find(word[::-1])) != -1:  # palindromes resolve forward
        return i + len(word) - 1, i
    return None


def find_word(matrix: list[list[str]], word: str) -> list[list[int]] | None:
    """Find the word in the matrix and return the start and end indices.

    Args:
        matrix: A 2D list of single lowercase letters.
        word: The word to find in the matrix.

    Returns:
        Start and end indices of the word, or None if not found.
    """
    for r, row in enumerate(matrix):
        if span := _locate(''.join(row), word):
            start, end = span
            return [[r, start], [r, end]]
    for c, column in enumerate(zip(*matrix)):
        if span := _locate(''.join(column), word):
            start, end = span
            return [[start, c], [end, c]]
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
    """Test find_word function."""
    assert find_word(matrix, word) == expected


if __name__ == '__main__':
    matrix, word, expected = tests[0]
    print(find_word(matrix, word), expected)
