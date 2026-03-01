# Daily Coding challenge #179 (2026-02-05) - freeCodeCamp.org
# Pocket Change
# Given an array of integers representing the coins in your pocket, with each integer
# being the value of a coin in cents, return the total amount in the format "$D.CC".

# 100 cents equals 1 dollar.
# In the return value, include a leading zero for amounts less than one dollar and
# always exactly two digits for the cents.
from pytest import mark


def count_change(change: list[int]) -> str:
    dollars, cents = divmod(sum(change), 100)
    return f'${dollars}.{cents:02d}'

tests = [
    ([25, 10, 5, 1], '$0.41'),
    ([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25], '$1.43'),
    ([100, 25, 100, 1000, 5, 500, 2000, 25], '$37.55'),
    ([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10], '$0.70'),
    ([1], '$0.01'),
    ([25, 25, 25, 25], '$1.00'),
]


@mark.parametrize('change, expected', tests)
def test_count_change(change: list[int], expected: str) -> None:
    assert count_change(change) == expected


if __name__ == '__main__':
    change, expected = tests[0]
    print(count_change(change))
