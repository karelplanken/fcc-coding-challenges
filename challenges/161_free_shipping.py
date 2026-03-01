# Daily Coding challenge #160 (2026-01-17) - freeCodeCamp.org
# Free Shipping
# Given an array of strings representing items in your shopping cart, and a number for
# the minimum order amount to qualify for free shipping, determine if the items in your
# shopping cart qualify for free shipping.

# The given array will contain items from the list below:

# Item	Price
# "shirt" 34.25
# "jeans" 48.50
# "shoes" 75.00
# "hat" 19.95
# "socks" 15.00
# "jacket" 109.95
from types import MappingProxyType

from pytest import mark

ITEM_PRICE = MappingProxyType(
    {
        'shirt': 34.25,
        'jeans': 48.50,
        'shoes': 75.00,
        'hat': 19.95,
        'socks': 15.00,
        'jacket': 109.95,
    }
)


def gets_free_shipping(cart: list[str], minimum: float) -> bool:
    return sum(ITEM_PRICE[item] for item in cart) >= minimum


tests = [
    (['shoes'], 50, True),
    (['hat', 'socks'], 50, False),
    (['jeans', 'shirt', 'jacket'], 75, True),
    (['socks', 'socks', 'hat'], 75, False),
    (['shirt', 'shirt', 'jeans', 'socks'], 100, True),
    (['hat', 'socks', 'hat', 'jeans', 'shoes', 'hat'], 200, False),
]


@mark.parametrize('cart, minimum, expected', tests)
def test_gets_free_shipping(cart: list[str], minimum: float, expected: bool) -> None:
    assert gets_free_shipping(cart, minimum) == expected


if __name__ == '__main__':
    cart, minimum, expected = tests[1]
    print(gets_free_shipping(cart, minimum))
