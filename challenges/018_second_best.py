# Daily Coding challenge #18 (2025-08-28) - freeCodeCamp.org
# Second Best
# Given an array of integers representing the price of different laptops, and an
# integer representing your budget, return:

# The second most expensive laptop if it is within your budget, or
# The most expensive laptop that is within your budget, or
# 0 if no laptops are within your budget.
# Duplicate prices should be ignored.
from pytest import mark


def get_laptop_cost(laptops: list[int], budget: int) -> int:
    # Return second-most expensive overall (if affordable),
    # otherwise most expensive within budget
    max_price = max(laptops)

    for price in sorted(laptops, reverse=True):
        if budget >= price and price != max_price:
            return price

    return 0


tests = [
    ([1500, 2000, 1800, 1400], 1900, 1800),
    ([1500, 2000, 2000, 1800, 1400], 1900, 1800),
    ([2099, 1599, 1899, 1499], 2200, 1899),
    ([2099, 1599, 1899, 1499], 1000, 0),
    ([1200, 1500, 1600, 1800, 1400, 2000], 1450, 1400),
]


@mark.parametrize('laptops, budget, expected', tests)
def test_get_laptop_cost(laptops: list[int], budget: int, expected: int) -> None:
    assert get_laptop_cost(laptops, budget) == expected


if __name__ == '__main__':
    laptops, budget, expected = tests[0]
    print(get_laptop_cost(laptops, budget))
