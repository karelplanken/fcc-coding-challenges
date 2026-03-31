# Daily Coding challenge #219 (2026-03-17) - freeCodeCamp.org
# Anniversary Milestones
# Given an integer representing the number of years a couple has been married, return
# their most recent anniversary milestone according to this chart:

# Years Married	Milestone
# 1	"Paper"
# 5	"Wood"
# 10	"Tin"
# 25	"Silver"
# 40	"Ruby"
# 50	"Gold"
# 60	"Diamond"
# 70	"Platinum"
# If they haven't reached the first milestone, return "Newlyweds".
from bisect import bisect_right
from types import MappingProxyType

from pytest import mark

_RAW = (
    (0, 'Newlyweds'),
    (1, 'Paper'),
    (5, 'Wood'),
    (10, 'Tin'),
    (25, 'Silver'),
    (40, 'Ruby'),
    (50, 'Gold'),
    (60, 'Diamond'),
    (70, 'Platinum'),
)

ANNIVERSARY_MILESTONES = MappingProxyType(dict(sorted(_RAW)))

_YEARS = list(ANNIVERSARY_MILESTONES.keys())
_LABELS = list(ANNIVERSARY_MILESTONES.values())

def get_milestone(years: int) -> str:
    return _LABELS[bisect_right(_YEARS, years) - 1]

tests = [
    (0, 'Newlyweds'),
    (1, 'Paper'),
    (8, 'Wood'),
    (10, 'Tin'),
    (26, 'Silver'),
    (45, 'Ruby'),
    (50, 'Gold'),
    (64, 'Diamond'),
    (71, 'Platinum'),
]


@mark.parametrize('years, expected', tests)
def test_get_milestone(years: int, expected: str) -> None:
    assert get_milestone(years) == expected


if __name__ == '__main__':
    years, expected = tests[1]
    print(get_milestone(years))
