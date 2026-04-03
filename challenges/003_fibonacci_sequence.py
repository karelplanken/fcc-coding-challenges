# Daily Coding challenge #3 (2025-08-13) - freeCodeCamp.org
# Fibonacci Sequence
# The Fibonacci sequence is a series of numbers where each number is the sum of the
# two preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence
# are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

# Given an array containing the first two numbers of a Fibonacci sequence, and an
# integer representing the length of the sequence, return an array containing the
# sequence of the given length.

# Your function should handle sequences of any length greater than or equal to zero.
# If the length is zero, return an empty array.
# Note that the starting numbers are part of the sequence.

# Generator version (memory efficient for very long sequences)
from collections.abc import Generator

from pytest import mark


def fibonacci_sequence(start_sequence: list[int], length: int) -> list[int]:
    if length == 0:
        return []

    if length <= len(start_sequence):
        return start_sequence[:length]

    def fib_gen() -> Generator:
        yield from start_sequence
        prev, curr = start_sequence[-2], start_sequence[-1]
        for _ in range(len(start_sequence), length):
            next_val = prev + curr
            yield next_val
            prev, curr = curr, next_val

    return list(fib_gen())


# Return the generator itself, use as: list(fibonacci_generator(input_data, length))

# def fibonacci_generator(
#     start_sequence: list[int], length: int
# ) -> Generator[int, None, None]:
#     if length == 0:
#         return

#     # Yield initial elements
#     for i, val in enumerate(start_sequence):
#         if i >= length:
#             break
#         yield val

#     # Generate remaining if needed
#     if length > len(start_sequence):
#         prev, curr = start_sequence[-2], start_sequence[-1]
#         for _ in range(len(start_sequence), length):
#             next_val = prev + curr
#             yield next_val
#             prev, curr = curr, next_val


tests = [
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
    assert fibonacci_sequence(start_sequence, length) == expected


if __name__ == '__main__':
    start_sequence, length, expected = tests[0]
    print(fibonacci_sequence(start_sequence, length))
