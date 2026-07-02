# Daily Coding challenge #326 (2026-07-02) - freeCodeCamp.org
# Max Profit
# Given an array of daily stock prices and a budget (in dollars), calculate the maximum
# profit you could make by buying and selling the stock over the given period.
#
# - You may only sell after you buy.
# - You can only buy whole shares.
# - Return the maximum possible profit as a string, rounded down to the nearest cent and
#   formatted to two decimal places.
from decimal import ROUND_DOWN, Decimal

from pytest import mark


def get_max_profit(prices: list[float], budget: float) -> str:
    d_prices = [Decimal(str(p)) for p in prices]
    d_budget = Decimal(str(budget))

    if len(d_prices) < 2:
        return '0.00'

    max_profit = Decimal('0')
    highest_future_price = d_prices[-1]

    for price in reversed(d_prices[:-1]):
        shares = d_budget // price
        profit = (highest_future_price - price) * shares
        max_profit = max(max_profit, profit)
        highest_future_price = max(highest_future_price, price)

    return str(max_profit.quantize(Decimal('0.01'), rounding=ROUND_DOWN))


tests: list[tuple[list[float], float, str]] = [
    ([5, 6], 50, '10.00'),
    ([8, 2, 5, 10], 20, '80.00'),
    ([4, 5, 3, 6], 20, '18.00'),
    ([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200, '8.31'),
    ([15.38, 15.01, 14.99, 14.62, 14.28], 80, '0.00'),
    ([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25, '73.80'),
]


@mark.parametrize('prices, budget, expected', tests)
def test_get_max_profit(prices: list[float], budget: float, expected: str) -> None:
    assert get_max_profit(prices, budget) == expected


if __name__ == '__main__':
    prices, budget, expected = tests[5]
    print(get_max_profit(prices, budget))
