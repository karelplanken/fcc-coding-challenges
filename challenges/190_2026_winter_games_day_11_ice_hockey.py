# Daily Coding challenge #190 (2026-02-16) - freeCodeCamp.org
# 2026 Winter Games Day 11: Ice Hockey
# Given an array of 6 ice hockey teams and their records after the round robin games,
# determine the match-ups for the semi-final round.

# Each array item will have a team and their record in the format "TEAM: W-OTW-OTL-L".
# Where:
# "W" is the number of wins in regulation, worth 3 points each
# "OTW" is the number of overtime wins, worth 2 points each
# "OTL" is the number of overtime losses, worth 1 point each
# "L" is the number of losses, worth 0 points each
# For example, "FIN: 2-2-1-0" would have 11 points after adding up their record.

# Find the total number of points for each team and return "The semi-final games will
# be (1st) vs (4th) and (2nd) vs (3rd).". For example, "The semi-final games will be
# FIN vs SWE and CAN vs USA."
from dataclasses import dataclass
from operator import attrgetter
from types import MappingProxyType

from pytest import mark

POINTS = MappingProxyType({'W': 3, 'OTW': 2, 'OTL': 1, 'L': 0})


@dataclass(frozen=True, slots=True)
class TeamTotalPoints:
    name: str
    total_points: int


TOTAL_POINTS_GETTER = attrgetter('total_points')


def get_team_total_points(team: str) -> TeamTotalPoints:
    name, game_results = team.split(': ', maxsplit=1)

    outcomes = (int(outcome) for outcome in game_results.split('-', maxsplit=3))
    return TeamTotalPoints(
        name=name,
        total_points=sum(
            POINTS[category] * outcome
            for category, outcome in zip(POINTS.keys(), outcomes)
        ),
    )


def get_semifinal_matchups(teams: list[str]) -> str:
    ranking = sorted(
        (get_team_total_points(team) for team in teams),
        key=TOTAL_POINTS_GETTER,
        reverse=True,
    )
    first, second, third, fourth = (team.name for team in ranking[0:4])
    return f'The semi-final games will be {first} vs {fourth} and {second} vs {third}.'


tests = [
    (
        [
            'CAN: 2-2-0-1',
            'FIN: 2-2-1-0',
            'GER: 1-0-1-3',
            'SUI: 0-1-3-1',
            'SWE: 1-1-2-1',
            'USA: 2-1-0-2',
        ],
        'The semi-final games will be FIN vs SWE and CAN vs USA.',
    ),
    (
        [
            'CAN: 2-1-1-1',
            'CZE: 1-1-1-2',
            'FIN: 1-2-1-1',
            'NOR: 0-1-1-3',
            'SLO: 1-0-1-3',
            'USA: 5-0-0-0',
        ],
        'The semi-final games will be USA vs CZE and CAN vs FIN.',
    ),
    (
        [
            'CAN: 3-2-0-0',
            'CZE: 2-1-2-0',
            'LAT: 0-0-1-4',
            'ITA: 1-1-1-2',
            'DEN: 1-0-0-4',
            'USA: 3-1-1-0',
        ],
        'The semi-final games will be CAN vs ITA and USA vs CZE.',
    ),
    (
        [
            'AUT: 2-2-1-0',
            'DEN: 1-0-0-4',
            'ITA: 1-1-1-2',
            'JPN: 3-2-0-0',
            'KOR: 2-1-2-0',
            'LAT: 0-0-1-4',
        ],
        'The semi-final games will be JPN vs ITA and AUT vs KOR.',
    ),
]


@mark.parametrize('teams, expected', tests)
def test(teams: list[str], expected: str) -> None:
    assert get_semifinal_matchups(teams) == expected


if __name__ == '__main__':
    teams, expected = tests[0]
    print(get_semifinal_matchups(teams))
