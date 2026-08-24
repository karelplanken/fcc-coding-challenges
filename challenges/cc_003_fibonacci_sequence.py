"""Daily Coding Challenge #3 (2025-08-13) - freeCodeCamp.org."""

# Fibonacci Sequence
# The Fibonacci sequence is a series of numbers where each number is the sum of the two
# preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence are
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
#
# Given an array containing the first two numbers of a Fibonacci sequence, and an
# integer representing the length of the sequence, return an array containing the
# sequence of the given length.
#
# - Your function should handle sequences of any length greater than or equal to zero.
# - If the length is zero, return an empty array.
# - Note that the starting numbers are part of the sequence.
from collections.abc import Iterator
from itertools import islice

from pytest import mark


def _fibonacci_stream(start_sequence: list[int]) -> Iterator[int]:
    """Yield an unbounded Fibonacci sequence continuing from the given seed.

    Assumes that the two numbers in start_sequence are two consecutive numbers in the
    Fibonacci sequence.

    Args:
        start_sequence: The first two numbers of the Fibonacci sequence.

    Yields:
        The next number in the Fibonacci sequence.
    """
    yield from start_sequence

    prev, curr = start_sequence[-2], start_sequence[-1]
    while True:
        prev, curr = curr, prev + curr
        yield curr


def fibonacci_sequence(start_sequence: list[int], length: int) -> list[int]:
    """Generate a Fibonacci sequence from given seed values.

    Starts from the seed values in ``start_sequence`` and extends the
    sequence to the requested length.

    Args:
        start_sequence: A list containing the first two numbers of the
            Fibonacci sequence.
        length: The total length of the desired Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence starting with the given
        numbers and of the specified length.

    Raises:
        ValueError: If the start sequence is None or does not contain at least two
        numbers or if the length is negative.
    """
    if not start_sequence or len(start_sequence) < 2:
        msg = 'start sequence must contain at least two numbers'
        raise ValueError(msg)

    if length < 0:
        msg = 'length must be greater than or equal to zero'
        raise ValueError(msg)

    return list(islice(_fibonacci_stream(start_sequence), length))


tests: list[tuple[list[int], int, list[int]]] = [
    (
        [0, 1],
        20,
        [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
        ],
    ),
    ([21, 32], 1, [21]),
    ([0, 1], 0, []),
    ([10, 20], 2, [10, 20]),
    (
        [123456789, 987654321],
        5,
        [123456789, 987654321, 1111111110, 2098765431, 3209876541],
    ),
]


@mark.parametrize('start_sequence, length, expected', tests)
def test_fibonacci_sequence(
    start_sequence: list[int], length: int, expected: list[int]
) -> None:
    """Test fibonacci_sequence function."""
    assert fibonacci_sequence(start_sequence, length) == expected


if __name__ == '__main__':
    start_sequence, length, expected = tests[0]
    print(fibonacci_sequence(start_sequence, length))
