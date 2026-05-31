# Daily Coding challenge #290 (2026-05-27) - freeCodeCamp.org
# Pizza Party
# Given an array of hours worked today per person, return the number of pizzas to order
# for a pizza party.
# Divide each person's hours worked by 3 to get their slice count.
# You can't eat a partial slice, so round each person's slice count up to the nearest
# whole number.
# Each person gets a minimum of two slices.
# Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole
# pizza.
from math import ceil

from pytest import mark

HOURS_PER_SLICE = 3
SLICES_PER_PIZZA = 8
MIN_SLICES = 2


def slices_for_person(hours: int) -> int:
    return max(ceil(hours / HOURS_PER_SLICE), MIN_SLICES)


def get_pizzas_to_order(hours_worked: list[int]) -> int:
    total_slices = sum(slices_for_person(h) for h in hours_worked)
    return ceil(total_slices / SLICES_PER_PIZZA)


# One-liner solution:
# def get_pizzas_to_order(hours_worked: list[int]) -> int:
#     return ceil(
#         sum(max(ceil(hours / HOURS_PER_SLICE), MIN_SLICES) for hours in hours_worked)
#         / SLICES_PER_PIZZA
#     )


tests = [
    ([8, 8, 8], 2),
    ([10, 9, 8, 2, 2, 6, 10], 3),
    ([1, 2, 3, 4, 5], 2),
    ([8, 8, 8, 8, 8, 8, 8, 8], 3),
    ([9, 9, 6], 1),
    ([10, 12, 16, 9, 8, 11, 15, 8, 0], 5),
]


@mark.parametrize('hours_worked, expected', tests)
def test_get_pizzas_to_order(hours_worked: list[int], expected: int) -> None:
    assert get_pizzas_to_order(hours_worked) == expected


if __name__ == '__main__':
    hours_worked, expected = tests[5]
    print(get_pizzas_to_order(hours_worked))
