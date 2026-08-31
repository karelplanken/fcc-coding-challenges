"""Daily Coding Challenge #18 (2025-08-28) - freeCodeCamp.org."""

# Second Best
# Given an array of integers representing the price of different laptops, and an integer
# representing your budget, return:
#
# 1. The second most expensive laptop if it is within your budget, or
# 2. The most expensive laptop that is within your budget, or
# 3. 0 if no laptops are within your budget.
#
# - Duplicate prices should be ignored.
from pytest import mark


def get_laptop_cost(laptops: list[int], budget: int) -> int:
    """Return the second most expensive laptop within budget.

    Args:
        laptops: list of integers representing the price of different laptops.
        budget: integer representing budget.

    Returns:
        The second most expensive laptop within budget, or the most expensive laptop
        within budget, or 0 if no laptops are within budget.

    Raises:
        ValueError: If less than two laptop prices are provided.
    """
    if len(laptops) < 2:
        msg = 'At least two laptop prices are required.'
        raise ValueError(msg)

    unique_prices = sorted(set(laptops), reverse=True)

    if len(unique_prices) > 1 and unique_prices[1] <= budget:
        return unique_prices[1]

    for price in unique_prices:
        if price <= budget:
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
    """Test get_laptop_cost function."""
    assert get_laptop_cost(laptops, budget) == expected


if __name__ == '__main__':
    laptops, budget, expected = tests[0]
    print(get_laptop_cost(laptops, budget))
