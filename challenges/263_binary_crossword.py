# Daily Coding challenge #263 (2026-04-30) - freeCodeCamp.org
# Binary Crossword
# Given a character, determine if its 8-bit binary representation can be found in the
# following grid, horizontally or vertically in either direction:
# 0 1 0 0 0 0 0 1
# 0 1 1 0 1 1 1 1
# 0 1 0 0 0 1 0 0
# 0 1 1 0 0 1 0 1
# 0 1 0 1 0 0 1 0
# 0 1 0 1 0 1 0 0
# 0 1 1 0 1 0 0 0
# 1 0 1 0 1 1 1 0
# For example, "A" has the binary representation 01000001, which appears in the first
# row from left to right.
from pytest import mark

GRID = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
]


def _all_sequences(grid: list[list[int]]) -> list[list[int]]:
    rows = grid
    cols = [list(col) for col in zip(*grid)]
    sequences = rows + cols
    return sequences + [seq[::-1] for seq in sequences]


_SEQUENCES = frozenset(tuple(seq) for seq in _all_sequences(GRID))


def is_in_crossword(char: str) -> bool:
    bits = tuple(int(b) for b in f'{ord(char):08b}')
    return bits in _SEQUENCES


tests = [
    ('I', True),
    ('D', True),
    ('0', True),
    ('u', True),
    ('Y', False),
    ('p', False),
    ('1', False),
    ('Q', False),
]


@mark.parametrize('char, expected', tests)
def test_is_in_crossword(char: str, expected: bool) -> None:
    assert is_in_crossword(char) == expected


if __name__ == '__main__':
    char, expected = tests[7]
    print(is_in_crossword(char))
