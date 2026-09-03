"""Daily Coding Challenge #22 (2025-09-01) - freeCodeCamp.org."""

# Tribonacci Sequence
# The Tribonacci sequence is a series of numbers where each number is the sum of the
# three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the
# sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.
#
# Given an array containing the first three numbers of a Tribonacci sequence, and an
# integer representing the length of the sequence, return an array containing the
# sequence of the given length.
#
# - Your function should handle sequences of any length greater than or equal to zero.
# - If the length is zero, return an empty array.
# - Note that the starting numbers are part of the sequence.
from collections.abc import Iterator
from itertools import islice

from pytest import mark


def _tribonacci(start_sequence: list[int]) -> Iterator[int]:
    """Yield an infinite Tribonacci sequence from the given starting values."""
    a, b, c = start_sequence
    yield a
    yield b
    yield c
    while True:
        a, b, c = b, c, a + b + c
        yield c


def tribonacci_sequence(start_sequence: list[int], length: int) -> list[int]:
    """Return the Tribonacci sequence of a given length starting with the given numbers.

    Args:
        start_sequence: A list of the first three numbers of a Tribonacci sequence.
        length: An integer representing the desired length of the Tribonacci sequence.

    Returns:
        A list containing the Tribonacci sequence of the given length.

    Raises:
        ValueError: If `start_sequence` does not contain exactly three numbers or if
            `length` is negative.
    """
    if not start_sequence or len(start_sequence) != 3:
        msg = 'start_sequence must contain exactly three numbers'
        raise ValueError(msg)

    if length < 0:
        msg = 'length must be a non-negative integer'
        raise ValueError(msg)

    return list(islice(_tribonacci(start_sequence), length))


# Plain loop implementation of the Tribonacci sequence generator
# def tribonacci_sequence(start_sequence: list[int], length: int) -> list[int]:
#     """Return the Tribonacci sequence of given length starting with the given numbers.

#     Args:
#         start_sequence: A list of the first three numbers of a Tribonacci sequence.
#         length: An integer representing the desired length of the Tribonacci sequence.

#     Returns:
#         A list containing the Tribonacci sequence of the given length.

#     Raises:
#         ValueError: If `start_sequence` does not contain exactly three numbers or if
#         `length` is negative.
#     """
#     if not start_sequence or len(start_sequence) != 3:
#         msg = 'start_sequence must contain exactly three numbers'
#         raise ValueError(msg)

#     if length < 0:
#         msg = 'length must be a non-negative integer'
#         raise ValueError(msg)

#     sequence = start_sequence.copy()
#     while len(sequence) < length:
#         next_value = sequence[-1] + sequence[-2] + sequence[-3]
#         sequence.append(next_value)
#     return sequence[:length]

tests: list[tuple[list[int], int, list[int]]] = [
    (
        [0, 0, 1],
        20,
        [
            0,
            0,
            1,
            1,
            2,
            4,
            7,
            13,
            24,
            44,
            81,
            149,
            274,
            504,
            927,
            1705,
            3136,
            5768,
            10609,
            19513,
        ],
    ),
    ([21, 32, 43], 1, [21]),
    ([0, 0, 1], 0, []),
    ([10, 20, 30], 2, [10, 20]),
    ([10, 20, 30], 3, [10, 20, 30]),
    ([123, 456, 789], 8, [123, 456, 789, 1368, 2613, 4770, 8751, 16134]),
]


@mark.parametrize('start_sequence, length, expected', tests)
def test_tribonacci_sequence(
    start_sequence: list[int], length: int, expected: list[int]
) -> None:
    """Test tribonacci_sequence function."""
    assert tribonacci_sequence(start_sequence, length) == expected


if __name__ == '__main__':
    start_sequence, length, expected = tests[0]
    print(tribonacci_sequence(start_sequence, length))
