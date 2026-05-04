# Daily Coding challenge #266 (2026-05-03) - freeCodeCamp.org
# Parsec Converter
# In a distant galaxy, parsecs are used to measure both time and distance. Given an
# integer number of parsecs, return its equivalent in time or distance.
# If the given integer is odd, it represents time. If it's even, it represents distance.

# Use these conversion rates:
# Parsecs	Time/Distance
# 1	2 hours
# 2	6 light years
# Return the converted value as an integer.
from pytest import mark

CONVERSION_RATES = (3, 2)  # index 0 = even (distance), index 1 = odd (time)


def convert_parsecs(parsecs: int) -> int:
    return parsecs * CONVERSION_RATES[parsecs % 2]


tests = [
    (1, 2),
    (2, 6),
    (31, 62),
    (88, 264),
    (17, 34),
    (14, 42),
]


@mark.parametrize('parsecs, expected', tests)
def test(parsecs: int, expected: int) -> None:
    assert convert_parsecs(parsecs) == expected


if __name__ == '__main__':
    parsecs, expected = tests[0]
    print(convert_parsecs(parsecs))
