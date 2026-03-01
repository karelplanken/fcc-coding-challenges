# Daily Coding challenge #144 (2026-01-01) - freeCodeCamp.org
# Resolution Streak
# Given an array of arrays, where each sub-array represents a day of your resolution
# activities and contains three integers: the number of steps walked that day, the
# minutes of screen time that day, and the number of pages read that day; determine if
# you are keeping your resolutions.

# The first sub-array is day 1, and second day 2, and so on.
# A day is considered successful if all three of the following goals are met:

# You walked at least 10,000 steps.
# You had no more than 120 minutes of screen time.
# You read at least five pages.
# If all of the given days are successful, return "Resolution on track: N day streak."
# Where N is the number of successful days.

# If one or more days is not a success,
# return "Resolution failed on day X: N day streak.". Where X is the day number of the
# first unsuccessful day, and N is the number of successful days before the first
# unsuccessful day.
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType

from pytest import mark

TARGET = MappingProxyType({'steps': 10_000, 'screen_time': 120, 'pages': 5})


@dataclass(frozen=True)
class DayData:
    steps: int
    screen_time: int
    pages: int

    def meets_goals(self, targets: Mapping[str, int]) -> bool:
        return (
            self.steps >= targets['steps']
            and self.screen_time <= targets['screen_time']
            and self.pages >= targets['pages']
        )


def resolution_streak(days: list[list[int]]) -> str:
    for day_number, day_data in enumerate(DayData(*day) for day in days):
        if not day_data.meets_goals(TARGET):
            return (
                f'Resolution failed on day {day_number + 1}: {day_number} day streak.'
            )

    return f'Resolution on track: {len(days)} day streak.'


tests = [
    (
        [[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]],
        'Resolution on track: 3 day streak.',
    ),
    ([[10000, 120, 5], [10950, 121, 11]], 'Resolution failed on day 2: 1 day streak.'),
    (
        [[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]],
        'Resolution failed on day 3: 2 day streak.',
    ),
    (
        [
            [11600, 76, 13],
            [12556, 64, 26],
            [10404, 32, 59],
            [9999, 44, 124],
            [7508, 23, 167],
            [10900, 80, 0],
        ],
        'Resolution failed on day 4: 3 day streak.',
    ),
    (
        [
            [10500, 75, 15],
            [11000, 90, 10],
            [10650, 100, 9],
            [10200, 60, 10],
            [10678, 87, 9],
            [12431, 67, 13],
            [10444, 107, 19],
            [10111, 95, 5],
            [10000, 120, 7],
            [11980, 101, 8],
        ],
        'Resolution on track: 10 day streak.',
    ),
]


@mark.parametrize('days, expected', tests)
def test_resolution_streak(days: list[list[int]], expected: str) -> None:
    assert resolution_streak(days) == expected


if __name__ == '__main__':
    days, expected = tests[1]
    print(resolution_streak(days))

# from collections import namedtuple
# DayTotals = namedtuple('DayTotals', ['steps', 'screen_time', 'pages'])
