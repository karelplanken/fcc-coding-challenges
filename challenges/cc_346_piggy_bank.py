"""Daily Coding Challenge #346 (2026-07-22) - freeCodeCamp.org."""

# Piggy Bank
# Given an object representing a piggy bank, return the total value as a string
# formatted as "$D.CC".
#
# The object may contain any of the following:
#
# | Coin | Value |
# |------|-------|
# | pennies | $0.01 |
# | nickels | $0.05 |
# | dimes | $0.10 |
# | quarters | $0.25 |
from types import MappingProxyType

from pytest import mark

CENTS: MappingProxyType[str, int] = MappingProxyType({
    'pennies': 1,
    'nickels': 5,
    'dimes': 10,
    'quarters': 25,
})


def piggy_bank(coins: dict[str, int]) -> str:
    """Returns the total value of 'coins'.

    Assumes 'coins' contains valid coins only as defined in the global 'CENTS'
    constant and that coin values are non-negative integers.

    Args:
        coins: a dictionary mapping coin types to their quantities.

    Returns:
        a string representing the total value formatted as "$D.CC".
    """
    total_cents = sum(CENTS[coin] * count for coin, count in coins.items())
    dollars, cents = divmod(total_cents, 100)
    return f'${dollars}.{cents:02d}'


tests: list[tuple[dict[str, int], str]] = [
    ({'pennies': 3, 'nickels': 5, 'dimes': 2, 'quarters': 6}, '$1.98'),
    ({'pennies': 1, 'nickels': 1, 'dimes': 1, 'quarters': 1}, '$0.41'),
    ({'nickels': 8, 'dimes': 6, 'quarters': 5}, '$2.25'),
    ({}, '$0.00'),
    ({'pennies': 146, 'nickels': 11, 'dimes': 0, 'quarters': 19}, '$6.76'),
]


@mark.parametrize('coins, expected', tests)
def test_piggy_bank(coins: dict[str, int], expected: str) -> None:
    """Test piggy_bank function."""
    assert piggy_bank(coins) == expected


if __name__ == '__main__':
    coins, expected = tests[4]
    print(piggy_bank(coins))
