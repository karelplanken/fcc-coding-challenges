# Daily Coding challenge #191 (2026-02-17) - freeCodeCamp.org
# 2026 Winter Games Day 12: Bobsled
# Given an array representing the weights of the athletes on a bobsled team and a
# number representing the weight of the bobsled, determine whether the team is eligible
# to race.

# The length of the array determines the team size: 1, 2 or 4 person teams.
# All given weight values are in kilograms (kg).
# The bobsled (sled by iteself) must have a minimum weight of:

# 162 kg for a 1-person team
# 170 kg for a 2-person team
# 210 kg for a 4-person team
# The total weight of the bobsled (athletes plus sled) must not exceed:

# 247 kg for a 1-person team
# 390 kg for a 2-person team
# 630 kg for a 4-person team
# Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the
# team fails to meet one or more of the requirements.
from dataclasses import dataclass
from types import MappingProxyType

from pytest import mark


@dataclass(frozen=True, slots=True)
class BobsledRules:
    team_size: int
    min_sled_weight: int
    max_total_weight: int


RULES = MappingProxyType[int, BobsledRules](
    {
        1: BobsledRules(team_size=1, min_sled_weight=162, max_total_weight=247),
        2: BobsledRules(team_size=2, min_sled_weight=170, max_total_weight=390),
        4: BobsledRules(team_size=4, min_sled_weight=210, max_total_weight=630),
    }
)


def check_eligibility(athlete_weights: list[int], sled_weight: int) -> str:
    team_size = len(athlete_weights)
    total_weight = sum(athlete_weights) + sled_weight

    rules = RULES[team_size]
    eligible = (
        sled_weight >= rules.min_sled_weight and total_weight <= rules.max_total_weight
    )

    return 'Eligible' if eligible else 'Not Eligible'


tests = [
    ([78], 165, 'Eligible'),
    ([80], 160, 'Not Eligible'),
    ([80], 170, 'Not Eligible'),
    ([85, 90], 170, 'Eligible'),
    ([85, 95], 168, 'Not Eligible'),
    ([112, 97], 185, 'Not Eligible'),
    ([110, 102, 90, 106], 222, 'Eligible'),
    ([106, 99, 90, 88], 205, 'Not Eligible'),
    ([106, 99, 103, 96], 227, 'Not Eligible'),
]


@mark.parametrize('athlete_weights, sled_weight, expected', tests)
def test_check_eligibility(
    athlete_weights: list[int], sled_weight: int, expected: str
) -> None:
    assert check_eligibility(athlete_weights, sled_weight) == expected


if __name__ == '__main__':
    athlete_weights, sled_weight, expected = tests[2]
    print(check_eligibility(athlete_weights, sled_weight))
