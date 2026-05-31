# Daily Coding challenge #278 (2026-05-15) - freeCodeCamp.org
# Coffee Order Parser
# Given a string for a coffee order, identify any menu items and return a formatted
# order.Use the following menu items and prices:
# Item	Price
# "cold brew"	$4.50
# "oat latte"	$5.00
# "cappuccino"	$4.75
# "espresso"	$3.00
# "vanilla syrup"	$0.75
# "caramel drizzle"	$0.60
# "extra shot"	$0.50
# "oat milk"	$0.75
# "cream"	$0.75
# Return a string with the matched items joined by " + ", followed by a colon and
# space (": "), and the total price. For example, given "I'd like an oat latte with
# vanilla syrup and an extra shot please.",
# return "oat latte + vanilla syrup + extra shot: $6.25"
# Items should appear in the order they appear in the menu and the total price should
# always have two decimal places.
from types import MappingProxyType

from pytest import mark

MENU: MappingProxyType[str, float] = MappingProxyType({
    'cold brew': 4.50,
    'oat latte': 5.00,
    'cappuccino': 4.75,
    'espresso': 3.00,
    'vanilla syrup': 0.75,
    'caramel drizzle': 0.60,
    'extra shot': 0.50,
    'oat milk': 0.75,
    'cream': 0.75,
})


def format_coffee_order(order: str) -> str:
    normalized = order.lower()
    matched = [(item, MENU[item]) for item in MENU if item in normalized]
    return (
        ' + '.join(name for name, _ in matched)
        + f': ${sum(price for _, price in matched):.2f}'
    )


tests = [
    (
        "I'd like an oat latte with vanilla syrup and an extra shot please.",
        'oat latte + vanilla syrup + extra shot: $6.25',
    ),
    (
        'Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk.',
        'cappuccino + vanilla syrup + caramel drizzle + oat milk: $6.85',
    ),
    (
        'Can I get a cold brew with some cream and an extra shot.',
        'cold brew + extra shot + cream: $5.75',
    ),
    ('Just an espresso please.', 'espresso: $3.00'),
    (
        "I'll take an oat latte with cream and an extra shot, and some vanilla syrup "
        + 'and caramel drizzle.',
        'oat latte + vanilla syrup + caramel drizzle + extra shot + cream: $7.60',
    ),
]


@mark.parametrize('order, expected', tests)
def test_format_coffee_order(order: str, expected: str) -> None:
    assert format_coffee_order(order) == expected


if __name__ == '__main__':
    order, expected = tests[4]
    print(format_coffee_order(order))
