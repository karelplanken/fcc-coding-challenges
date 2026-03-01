# Daily Coding challenge #113 (2025-12-01) - freeCodeCamp.org
# Miles to Kilometers
# Given a distance in miles as a number, return the equivalent
# distance in kilometers.

# The input will always be a non-negative number.
# 1 mile equals 1.60934 kilometers.
# Round the result to two decimal places.
from pytest import mark


def convert_to_km(miles: float) -> float:
    KM_PER_MILE = 1.60934
    return round(miles * KM_PER_MILE, 2)


tests = [(1, 1.61), (21, 33.8), (3.5, 5.63), (0, 0), (0.621371, 1)]


@mark.parametrize('miles,expected', tests)
def test_convert_to_km(miles: float, expected: float) -> None:
    assert convert_to_km(miles) == expected


if __name__ == '__main__':
    miles, expected = tests[0]
    print(convert_to_km(miles))
