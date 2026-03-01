# Daily Coding challenge #120 (2025-12-08) - freeCodeCamp.org
# Pounds to Kilograms
# Given a weight in pounds as a number,
# return the string "(lbs) pounds equals (kgs) kilograms.".

# Replace "(lbs)" with the input number.
# Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and
# always include two decimal places in the value.
# 1 pound equals 0.453592 kilograms.
# If the input is 1, use "pound" instead of "pounds".
# If the converted value is 1, use "kilogram" instead of "kilograms".
from pytest import mark


def convert_to_kgs(lbs: float) -> str:
    kgs = round(lbs * 0.453592, 2)

    pound_unit = 'pound' if lbs == 1 else 'pounds'
    kilogram_unit = 'kilogram' if kgs == 1 else 'kilograms'

    return f'{lbs} {pound_unit} equals {kgs:.2f} {kilogram_unit}.'


tests = [
    (1, '1 pound equals 0.45 kilograms.'),
    (0, '0 pounds equals 0.00 kilograms.'),
    (100, '100 pounds equals 45.36 kilograms.'),
    (2.5, '2.5 pounds equals 1.13 kilograms.'),
    (2.20462, '2.20462 pounds equals 1.00 kilogram.'),
]


@mark.parametrize('lbs,expected', tests)
def test_convert_to_kgs(lbs: float, expected: str) -> None:
    assert convert_to_kgs(lbs) == expected


if __name__ == '__main__':
    lbs, expected = tests[0]
    print(convert_to_kgs(lbs))
