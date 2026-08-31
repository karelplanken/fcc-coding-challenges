"""Daily Coding Challenge #362 (2026-08-07) - freeCodeCamp.org."""

# Nonogram Validator
# Given an array of clue numbers and an array of cells, determine whether the cells
# satisfy the nonogram clue.
#
# - The clue is an array of numbers representing the lengths of consecutive filled
#   cells, in order. For example, a clue of [3, 2] means there should be 3 consecutive
#   filled cells followed by 2 consecutive filled cells, separated by at least one empty
#   cell.
# - The row is an array of 1s (filled) and 0s (empty).\
from itertools import groupby

from pytest import mark


def is_valid_nonogram(clue: list[int], cells: list[int]) -> bool:
    """Check whether a row of cells satisfies a nonogram clue.

    A row satisfies the clue if its runs of filled (1) cells, in order,
    have exactly the lengths given by `clue`, with each run separated by
    at least one non-filled cell.

    Args:
        clue: Expected run lengths, in order (e.g. [3, 2]).
        cells: Row cells, expected to be 1 (filled) or 0 (empty). Any
            other value is treated as non-filled and not validated.

    Returns:
        True if the runs of 1s in `cells` match `clue` exactly.
    """
    run_lengths = [len(list(group)) for value, group in groupby(cells) if value == 1]
    return run_lengths == clue


# Alternative solution using regex
# import re
# _RUN_PATTERN = re.compile(r'1+')


# def is_valid_nonogram(clue: list[int], cells: list[int]) -> bool:
#     """Check whether `cells` (a row of 0/1) satisfies the nonogram `clue`."""
#     row = ''.join(map(str, cells))
#     run_lengths = [len(run) for run in _RUN_PATTERN.findall(row)]
#     return run_lengths == clue

tests = [
    ([3, 2], [1, 1, 1, 0, 1, 1], True),
    ([3, 2], [0, 1, 1, 1, 1, 1], False),
    ([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1], False),
    ([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0], True),
    ([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], True),
    ([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], False),
]


@mark.parametrize('clue, cells, expected', tests)
def test_is_valid_nonogram(clue: list[int], cells: list[int], expected: bool) -> None:
    """Test is_valid_nonogram function."""
    assert is_valid_nonogram(clue, cells) == expected


if __name__ == '__main__':
    clue, cells, expected = tests[0]
    print(is_valid_nonogram(clue, cells))
