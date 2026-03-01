# Daily Coding challenge #134 (2025-12-22) - freeCodeCamp.org
# Traveling Shopper
# Given an amount of money you have, and an array of items you want to buy, determine
# how many of them you can afford.

# The given amount will be in the format ["Amount", "Currency Code"].
# For example: ["150.00", "USD"] or ["6000", "JPY"].
# Each array item you want to purchase will be in the same format.
# Use the following exchange rates to convert values:

# Currency	1 Unit Equals
# USD	1.00 USD
# EUR	1.10 USD
# GBP	1.25 USD
# JPY	0.0070 USD
# CAD	0.75 USD
# If you can afford all the items in the list, return "Buy them all!".
# Otherwise, return "Buy the first X items.", where X is the number of items you can
# afford when purchased in the order given.
from decimal import Decimal

from pytest import mark

EXCHANGE_RATES = {
    'USD': Decimal('1.00'),
    'EUR': Decimal('1.10'),
    'GBP': Decimal('1.25'),
    'JPY': Decimal('0.0070'),
    'CAD': Decimal('0.75'),
}


def to_usd(amount_currency: list[str]) -> Decimal:
    """Convert any currency amount to USD."""
    amount, currency = amount_currency
    return Decimal(amount) * EXCHANGE_RATES[currency]


def buy_items(funds: list[str], items: list[list[str]]) -> str:
    available = to_usd(funds)
    total_cost = Decimal(0)

    for i, item in enumerate(items):
        item_cost = to_usd(item)
        if total_cost + item_cost > available:
            return f'Buy the first {i} items.'
        total_cost += item_cost

    return 'Buy them all!'


tests = [
    (
        ['150.00', 'USD'],
        [['50.00', 'USD'], ['75.00', 'USD'], ['30.00', 'USD']],
        'Buy the first 2 items.',
    ),
    (['200.00', 'EUR'], [['50.00', 'USD'], ['50.00', 'USD']], 'Buy them all!'),
    (
        ['100.00', 'CAD'],
        [
            ['20.00', 'USD'],
            ['15.00', 'EUR'],
            ['10.00', 'GBP'],
            ['6000', 'JPY'],
            ['5.00', 'CAD'],
            ['10.00', 'USD'],
        ],
        'Buy the first 3 items.',
    ),
    (
        ['5000', 'JPY'],
        [
            ['3.00', 'USD'],
            ['1000', 'JPY'],
            ['5.00', 'CAD'],
            ['2.00', 'EUR'],
            ['4.00', 'USD'],
            ['2000', 'JPY'],
        ],
        'Buy them all!',
    ),
    (
        ['200.00', 'USD'],
        [
            ['50.00', 'USD'],
            ['40.00', 'EUR'],
            ['30.00', 'GBP'],
            ['5000', 'JPY'],
            ['25.00', 'CAD'],
            ['20.00', 'USD'],
        ],
        'Buy the first 5 items.',
    ),
]


@mark.parametrize('funds, items, expected', tests)
def test_buy_items(funds: list[str], items: list[list[str]], expected: str) -> None:
    assert buy_items(funds, items) == expected


if __name__ == '__main__':
    funds, items, expected = tests[4]
    print(buy_items(funds, items))
