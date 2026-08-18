"""Daily Coding Challenge #334 (2026-07-10) - freeCodeCamp.org."""

# Exact Change
# Given an integer amount in cents, return the number of distinct ways to make exact
# change using pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25
# cents).
from pytest import mark

COINS = [1, 5, 10, 25]


def exact_change(amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is one way to make change for 0 cents (using no coins)

    for coin in COINS:
        for sub_amount in range(coin, amount + 1):
            dp[sub_amount] += dp[sub_amount - coin]
    return dp[amount]


tests = [
    (3, 1),
    (9, 2),
    (17, 6),
    (39, 24),
    (61, 73),
    (99, 213),
]


@mark.parametrize('amount, expected', tests)
def test_exact_change(amount: int, expected: int) -> None:
    """Test exact_change function."""
    assert exact_change(amount) == expected


if __name__ == '__main__':
    amount, expected = tests[2]
    print(exact_change(amount))
