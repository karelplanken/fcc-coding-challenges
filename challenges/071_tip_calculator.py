# Daily Coding challenge #71 (2025-10-20) - freeCodeCamp.org
# Tip Calculator
# Given the price of your meal and a custom tip percent, return an array with three tip
# values; 15%, 20%, and the custom amount.

# Prices will be given in the format: "$N.NN".
# Custom tip percents will be given in this format: "25%".
# Return amounts in the same "$N.NN" format, rounded to two decimal places.
# For example, given a "$10.00" meal price, and a "25%" custom tip value,
# return ["$1.50", "$2.00", "$2.50"].
from pytest import mark


def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:
    """Calculate 15%, 20%, and custom tip amounts for a meal price."""
    price = float(meal_price.replace('$', ''))
    # price = float(meal_price[1:])  # Skip '$' character
    custom_frac = int(custom_tip.replace('%', '')) / 100
    # custom_pct = float(custom_tip[:-1]) / 100  # Skip '%' character

    return [f'${price * frac:.2f}' for frac in (0.15, 0.20, custom_frac)]


tests = [
    ('$10.00', '25%', ['$1.50', '$2.00', '$2.50']),
    ('$89.67', '26%', ['$13.45', '$17.93', '$23.31']),
    ('$19.85', '9%', ['$2.98', '$3.97', '$1.79']),
]


@mark.parametrize('meal_price, custom_tip, expected', tests)
def test_calculate_tips(meal_price: str, custom_tip: str, expected: str) -> None:
    assert calculate_tips(meal_price, custom_tip) == expected


if __name__ == '__main__':
    meal_price, custom_tip, expected = tests[0]
    print(calculate_tips(meal_price, custom_tip))
