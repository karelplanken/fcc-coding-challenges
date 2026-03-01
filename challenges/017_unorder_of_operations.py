# Daily Coding challenge #17 (2025-08-27) - freeCodeCamp.org
# Unorder of Operations
# Given an array of integers and an array of string operators, apply the operations to
# the numbers sequentially from left-to-right. Repeat the operations as needed until
# all numbers are used. Return the final result.

# For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating
# 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.

# Valid operators are +, -, *, /, and %.
import operator

from pytest import mark

OPERATOR_METHODS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '%': operator.mod,
}


def evaluate(numbers: list[int], operators: list[str]) -> int:
    result = numbers[0]
    num_operators = len(operators)

    for i, num in enumerate(numbers[1:], start=1):
        op = operators[(i - 1) % num_operators]
        result = OPERATOR_METHODS[op](result, num)

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
    assert evaluate(numbers, operators) == expected


if __name__ == '__main__':
    numbers, operators, expected = tests[0]
    print(evaluate(numbers, operators))
