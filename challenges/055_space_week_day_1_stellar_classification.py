# Daily Coding challenge #55 (2025-10-04) - freeCodeCamp.org
# Space Week Day 1: Stellar Classification
# October 4th marks the beginning of World Space Week. The next seven days will bring
# you astronomy-themed coding challenges.

# For today's challenge, you are given the surface temperature of a star in Kelvin (K)
# and need to determine its stellar classification based on the following ranges:
# "O": 30,000 K or higher
# "B": 10,000 K - 29,999 K
# "A": 7,500 K - 9,999 K
# "F": 6,000 K - 7,499 K
# "G": 5,200 K - 5,999 K
# "K": 3,700 K - 5,199 K
# "M": 0 K - 3,699 K
# Return the classification of the given star.
from bisect import bisect_right
from collections import namedtuple
from operator import attrgetter

from pytest import mark

StarClass = namedtuple('StarClass', ['threshold', 'classification'])

CLASSES = [
    StarClass(0, 'M'),
    StarClass(3_700, 'K'),
    StarClass(5_200, 'G'),
    StarClass(6_000, 'F'),
    StarClass(7_500, 'A'),
    StarClass(10_000, 'B'),
    StarClass(30_000, 'O'),
]

THRESHOLD_GETTER = attrgetter('threshold')


def classification(temp: int) -> str:
    return CLASSES[bisect_right(CLASSES, temp, key=THRESHOLD_GETTER) - 1].classification


# def classification(temp: int) -> str:
#     if temp > 30_000:
#         return 'O'
#     elif  10_000 <= temp < 30_000:
#         return 'B'
#     elif 7_500 <= temp < 10_000:
#         return 'A'
#     elif 6_000 <= temp < 7_500:
#         return 'F'
#     elif 5_200 <= temp < 6_000:
#         return 'G'
#     elif 3_700 <= temp < 5_200:
#         return 'K'
#     else:
#         return 'M'

# def classification(temp: int) -> str:
#     if temp >= 30_000:
#         return 'O'
#     if temp >= 10_000:
#         return 'B'
#     if temp >= 7_500:
#         return 'A'
#     if temp >= 6_000:
#         return 'F'
#     if temp >= 5_200:
#         return 'G'
#     if temp >= 3_700:
#         return 'K'
#     return 'M'


tests = [
    (5778, 'G'),
    (2400, 'M'),
    (9999, 'A'),
    (3700, 'K'),
    (3699, 'M'),
    (210000, 'O'),
    (6000, 'F'),
    (11432, 'B'),
]


@mark.parametrize('temp, expected', tests)
def test_classification(temp: int, expected: str) -> None:
    assert classification(temp) == expected


if __name__ == '__main__':
    temp, expected = tests[0]
    print(classification(temp))
