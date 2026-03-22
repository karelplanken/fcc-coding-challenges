# Daily Coding challenge #224 (2026-03-22) - freeCodeCamp.org
# Coffee Roast Detector
# Given a string representing the beans used to make a cup of coffee, determine the
# roast of the cup.

# The given string will contain the following characters, each representing a type of
# bean:
# An apostrophe (') is a light roast bean worth 1 point each.
# A dash (-) is a medium roast bean worth 2 points each.
# A period (.) is a dark roast bean worth 3 points each.
# The roast level is determined by the average of all the beans.

# Return:
# "Light" if the average is less than 1.75.
# "Medium" if the average is 1.75 to 2.5.
# "Dark" if the average is greater than 2.5.
from types import MappingProxyType

from pytest import mark

BEAN_ROASTS = MappingProxyType(
    {
        "'": 1,
        '-': 2,
        '.': 3,
    }
)


def detect_roast(beans: str) -> str:

    average_roast = sum(BEAN_ROASTS[char] for char in beans) / len(beans)

    if average_roast < 1.75:
        return 'Light'
    
    if average_roast <= 2.5:
        return 'Medium'
    
    return 'Dark'


tests = [
    ("''-''''''-'-''--''''", 'Light'),
    (".'-''-''..'''.-.-''-", 'Medium'),
    ("--.''--'-''.--..-.--", 'Medium'),
    ("-...'-......-..-...-", 'Dark'),
    (".--.-..-......----.'", 'Medium'),
    ('..-..-..-..-....-.-.', 'Dark'),
    ("-'-''''''..-'.''-'.'", 'Light'),
]


@mark.parametrize('beans, expected', tests)
def test_solution(beans: str, expected: str) -> None:
    assert detect_roast(beans) == expected


if __name__ == '__main__':
    beans, expected = tests[0]
    print(detect_roast(beans))
