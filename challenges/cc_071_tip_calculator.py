"""Daily Coding Challenge #71 (2025-10-20) - freeCodeCamp.org."""

# Tip Calculator
# Given the price of your meal and a custom tip percent, return an array with three tip
# values; 15%, 20%, and the custom amount.
#
# - Prices will be given in the format: "$N.NN".
# - Custom tip percents will be given in this format: "25%".
# - Return amounts in the same "$N.NN" format, rounded to two decimal places.
#
# For example, given a "$10.00" meal price, and a "25%" custom tip value, return
# ["$1.50", "$2.00", "$2.50"].
import re
from decimal import ROUND_HALF_UP, Decimal

from pytest import mark

_PRICE_PATTERN = re.compile(r'\$([0-9]+\.[0-9]{2})')
_PERCENT_PATTERN = re.compile(r'([0-9]+)%')

_CENT = Decimal('0.01')
_STANDARD_TIP_RATES = (Decimal('0.15'), Decimal('0.20'))


def _format_usd(amount: Decimal) -> str:
    """Round an amount half-up to cents and format it as "$N.NN".

    Args:
        amount: The amount to format.

    Returns:
        The amount formatted as "$N.NN", rounded half-up to the cent.
    """
    return f'${amount.quantize(_CENT, rounding=ROUND_HALF_UP)}'


def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:
    """Calculate 15%, 20% and custom tip amounts for a meal price.

    Args:
        meal_price: The price of the meal in the format "$N.NN".
        custom_tip: The custom tip as a whole-number percentage, "N%".

    Returns:
        The 15%, 20% and custom tip amounts, in that order, each formatted
        as "$N.NN" and rounded half-up to the cent.

    Raises:
        ValueError: If the meal price or custom tip format is invalid.
    """
    price_match = _PRICE_PATTERN.fullmatch(meal_price)
    if price_match is None:
        msg = f'invalid meal price format: {meal_price!r}'
        raise ValueError(msg)
    percent_match = _PERCENT_PATTERN.fullmatch(custom_tip)
    if percent_match is None:
        msg = f'invalid custom tip format: {custom_tip!r}'
        raise ValueError(msg)

    price = Decimal(price_match[1])
    custom_rate = Decimal(percent_match[1]) / 100

    return [_format_usd(price * rate) for rate in (*_STANDARD_TIP_RATES, custom_rate)]


tests = [
    ('$10.00', '25%', ['$1.50', '$2.00', '$2.50']),
    ('$89.67', '26%', ['$13.45', '$17.93', '$23.31']),
    ('$19.85', '9%', ['$2.98', '$3.97', '$1.79']),
]


@mark.parametrize('meal_price, custom_tip, expected', tests)
def test_calculate_tips(meal_price: str, custom_tip: str, expected: list[str]) -> None:
    """Test calculate_tips function."""
    assert calculate_tips(meal_price, custom_tip) == expected


if __name__ == '__main__':
    meal_price, custom_tip, expected = tests[0]
    print(calculate_tips(meal_price, custom_tip))
