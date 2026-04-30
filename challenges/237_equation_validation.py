# Daily Coding challenge #237 (2026-04-04) - freeCodeCamp.org
# Equation Validation
# Given a string representing a math equation, determine whether it is correct.

# The left side may contain up to three positive integers and
# the operators +, -, *, and /.
# The equation will be given in the format: "number operator number = number"
# (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
# The right side will always be a single integer.
# Follow standard order of operations: multiplication and division are evaluated before
# addition and subtraction, from left-to-right.
from operator import add, mul, sub, truediv
from types import MappingProxyType

from pytest import mark

OPERATORS = MappingProxyType(
    {
        # PEMDAS! Keep insertion order as is important for correct evaluation.
        '*': mul,
        '/': truediv,
        '+': add,
        '-': sub,
    }
)


def get_operands(lst: list[str | float], idx: int) -> tuple[float, float]:
    return (float(lst[idx - 1]), float(lst[idx + 1]))


def update_list(lst: list[str | float], value: float, idx: int) -> list[str | float]:
    lower_idx = max(0, idx - 1)
    upper_idx = min(len(lst) - 1, idx + 2)
    return [*lst[:lower_idx], value, *lst[upper_idx:]]


def evaluate_ops(lst: list[str | float]) -> float:
    for operator in OPERATORS:
        while operator in lst:
            idx = lst.index(operator)
            value = OPERATORS[operator](*get_operands(lst, idx))
            lst = update_list(lst, value, idx)

    return float(lst[0])


def is_valid_equation(equation: str) -> bool:
    ops_str, result_str = equation.split('=')

    ops_lst = [float(el) if el not in OPERATORS else el for el in ops_str.split()]

    return evaluate_ops(ops_lst) == float(result_str)


tests = [
    ('2 + 2 = 4', True),
    ('2 + 3 - 1 = 4', True),
    ('8 / 2 = 4', True),
    ('10 * 5 = 50', True),
    ('2 - 2 = 0', True),
    ('2 + 9 / 3 = 5', True),
    ('20 - 2 * 3 = 14', True),
    ('2 + 5 = 6', False),
    ('10 - 2 * 3 = 24', False),
    ('3 + 9 / 3 = 4', False),
]


@mark.parametrize('equation, expected', tests)
def test_is_valid_equation(equation: str, expected: bool) -> None:
    assert is_valid_equation(equation) == expected


if __name__ == '__main__':
    equation, expected = tests[1]
    print(is_valid_equation(equation))
