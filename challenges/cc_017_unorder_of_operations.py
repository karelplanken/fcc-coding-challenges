"""Daily Coding Challenge #17 (2025-08-27) - freeCodeCamp.org."""

# Unorder of Operations
# Given an array of integers and an array of string operators, apply the operations to
# the numbers sequentially from left-to-right. Repeat the operations as needed until all
# numbers are used. Return the final result.
#
# For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 +
# 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.
#
# - Valid operators are +, -, *, /, and %.
import operator
from collections.abc import Callable, Iterator
from itertools import cycle

from pytest import mark


# operator.floordiv's typeshed stub resolves to (a: Unknown, b: Unknown) -> Unknown
# under Pyright/Pylance strict mode (unlike add/sub/mul/mod, which have proper
# Supports*-protocol overloads). Wrap it so OPERATORS stays fully typed.
def _floordiv(a: int, b: int) -> int:
    return a // b


OPERATORS: dict[str, Callable[[int, int], int]] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': _floordiv,
    '%': operator.mod,
}


def evaluate(numbers: list[int], operators: list[str]) -> int:
    """Evaluate the numbers with the operators in a left-to-right, cyclic manner.

    Division and modulo both use Python's floor semantics, so the invariant
    ``a == (a // b) * b + a % b`` holds throughout.

    Args:
        numbers: A list of integers.
        operators: A list of string operators, applied cyclically.

    Returns:
        The result of evaluating the numbers with the operators, left-to-right.

    Raises:
        ValueError: If fewer than two numbers, or no operators, are provided.
    """
    if len(numbers) < 2:
        msg = 'At least two numbers are required.'
        raise ValueError(msg)
    if not operators:
        msg = 'At least one operator is required.'
        raise ValueError(msg)

    result = numbers[0]
    ops: Iterator[str] = cycle(operators)

    for op, num in zip(ops, numbers[1:]):
        result = OPERATORS[op](result, num)

    return result


tests = [
    ([5, 6, 7, 8, 9], ['+', '-'], 3),
    ([17, 61, 40, 24, 38, 14], ['+', '%'], 38),
    ([20, 2, 4, 24, 12, 3], ['*', '/'], 60),
    ([11, 4, 10, 17, 2], ['*', '*', '%'], 30),
    ([33, 11, 29, 13], ['/', '-'], -2),
]


@mark.parametrize('numbers, operators, expected', tests)
def test_evaluate(numbers: list[int], operators: list[str], expected: int) -> None:
    """Test evaluate function."""
    assert evaluate(numbers, operators) == expected


if __name__ == '__main__':
    numbers, operators, expected = tests[0]
    print(evaluate(numbers, operators))
