# Daily Coding challenge #312 (2026-06-18) - freeCodeCamp.org
# Streaming Cost
# Given an array representing movies in the cart of your streaming service, and a
# string for your subscription tier, return the total cost of the movies.

# Each item in the cart is an object with a "format" ("HD" or "4K") and a "type"
# ("rent" or "buy"). Their costs are:

# "rent"	"buy"
# "HD"	$3.99	$12.99
# "4K"	$5.99	$19.99
# Apply the following subscription tier discounts:

# "none": full price
# "basic": 10% off
# "premium": 25% off
# Return the total cost rounded to two decimal places in the format "$D.CC".
from pytest import mark

MOVIE_PRICES = {
    'HD': {'rent': 3.99, 'buy': 12.99},
    '4K': {'rent': 5.99, 'buy': 19.99},
}

DISCOUNT = {
    'none': 0.0,
    'basic': 0.10,
    'premium': 0.25,
}


# * NOTE: Decimal arithmetic fails this challenge despite being the correct approach
# for currency calculations. Two test cases land on exact 0.5 rounding boundaries:
#
#   [HD rent, HD buy] premium:
#   (3.99 + 12.99) * 0.75 = 12.735  → expected $12.73 (not $12.74)
#
#   [HD rent, 4K rent, HD buy, 4K buy, HD buy] basic:
#   (3.99 + 5.99 + 12.99 + 19.99 + 12.99) * 0.90 = 50.355 → expected $50.36 (not $50.35)
#
# The first rounds down, the second rounds up — no single Decimal rounding mode
# satisfies both. The expected outputs were generated with float, whose binary
# representation errors push each boundary in opposite directions by accident.
# float is therefore the required implementation here, not a shortcut.
#
# Additional finding: the freeCodeCamp WUI IDE grades in JavaScript, not Python.
# For test 6, Python float yields $50.36 (passes locally) but JavaScript float
# yields $50.35 (fails in the IDE) — same IEEE 754 standard, different accumulated
# representation errors. The challenge is effectively broken for that test case.
#
def get_streaming_bill(cart: list[dict[str, str]], subscription: str) -> str:
    # list[dict[str, str]] is a code smell; TypedDict or dataclass would be better,
    # but the challenge fixes the signature
    multiplier = 1 - DISCOUNT[subscription]
    subtotal = sum(MOVIE_PRICES[movie['format']][movie['type']] for movie in cart)
    return f'${subtotal * multiplier:.2f}'


tests = [
    ([{'format': 'HD', 'type': 'rent'}], 'none', '$3.99'),
    (
        [{'format': 'HD', 'type': 'rent'}, {'format': 'HD', 'type': 'buy'}],
        'premium',
        '$12.73',
    ),
    (
        [
            {'format': 'HD', 'type': 'rent'},
            {'format': 'HD', 'type': 'rent'},
            {'format': 'HD', 'type': 'buy'},
        ],
        'basic',
        '$18.87',
    ),
    (
        [{'format': '4K', 'type': 'buy'}, {'format': '4K', 'type': 'buy'}],
        'premium',
        '$29.98',
    ),
    (
        [
            {'format': 'HD', 'type': 'rent'},
            {'format': '4K', 'type': 'rent'},
            {'format': 'HD', 'type': 'buy'},
            {'format': '4K', 'type': 'buy'},
        ],
        'none',
        '$42.96',
    ),
    (
        [
            {'format': 'HD', 'type': 'rent'},
            {'format': '4K', 'type': 'rent'},
            {'format': 'HD', 'type': 'buy'},
            {'format': '4K', 'type': 'buy'},
            {'format': 'HD', 'type': 'buy'},
        ],
        'basic',
        '$50.36',
    ),
]


@mark.parametrize('cart, subscription, expected', tests)
def test(cart: list[dict[str, str]], subscription: str, expected: str) -> None:
    assert get_streaming_bill(cart, subscription) == expected


if __name__ == '__main__':
    cart, subscription, expected = tests[5]
    print(get_streaming_bill(cart, subscription))


# This is the industry standard to calculate total cost in terms of currency,
# but no single rounding mode satisfies both boundary test cases (see NOTE above):
# import decimal
# from decimal import Decimal, localcontext

# from pytest import mark

# MOVIE_PRICES = {
#     'HD': {'rent': Decimal('3.99'), 'buy': Decimal('12.99')},
#     '4K': {'rent': Decimal('5.99'), 'buy': Decimal('19.99')},
# }

# DISCOUNT = {
#     'none': Decimal('0.00'),
#     'basic': Decimal('0.10'),
#     'premium': Decimal('0.25'),
# }


# def get_streaming_bill(cart: list[dict[str, str]], subscription: str) -> str:
#     # ROUND_HALF_EVEN: test 2 → $12.74 (fail), test 6 → $50.36 (pass)
#     # ROUND_HALF_DOWN: test 2 → $12.73 (pass), test 6 → $50.35 (fail)
#     with localcontext(rounding=decimal.ROUND_HALF_EVEN):
#         total_cost = sum(
#             MOVIE_PRICES[movie['format']][movie['type']] * (
#                 1 - DISCOUNT[subscription]
#             )
#             for movie in cart
#         )
#         return f'${total_cost:.2f}'
