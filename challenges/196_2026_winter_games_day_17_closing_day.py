# Daily Coding challenge #196 (2026-02-22) - freeCodeCamp.org
# 2026 Winter Games Day 17: Closing Day
# Given a 2D array of medal winners, return a medal count for each country as a CSV
# string.

# In the given array, each sub-array represents a single event: [gold_winner,
# silver_winner, bronze_winner]

# The returned CSV string should have the following format, with the first line being
# headers:

# Country,Gold,Silver,Bronze,Total
# country_name,gold_count,silver_count,bronze_count,total_medals
# Separate new lines with the new line character ("\n").
# Do not include spaces around commas or at the end of lines.
# Sort the returned CSV by gold medal count, highest first. If two countries have the
# same gold medal count, sort the tied ones alphabetically.
# For example, given:

# [
#   ["USA", "CAN", "NOR"],
#   ["NOR", "USA", "CAN"],
#   ["USA", "NOR", "SWE"]
# ]
# Return:

# "Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1"
# Which looks like this when printed:

# Country,Gold,Silver,Bronze,Total
# USA,2,1,0,3
# NOR,1,1,1,3
# CAN,0,1,1,2
# SWE,0,0,1,1
from collections import defaultdict
from dataclasses import dataclass, fields

from pytest import mark


@dataclass
class MedalWinner:
    Country: str = ''
    Gold: int = 0
    Silver: int = 0
    Bronze: int = 0
    Total: int = 0


def count_medals(winners: list[list[str]]) -> str:
    medal_winners = defaultdict(MedalWinner)

    for row in winners:
        country_gold, country_silver, country_bronze = row
        medal_winners[country_gold].Gold += 1
        medal_winners[country_silver].Silver += 1
        medal_winners[country_bronze].Bronze += 1

    countries: list[MedalWinner] = []

    for country_name, medal_winner in medal_winners.items():
        medal_winner.Country = country_name
        medal_winner.Total = (
            medal_winner.Gold + medal_winner.Silver + medal_winner.Bronze
        )
        countries.append(medal_winner)

    countries.sort(key=lambda c: (-c.Gold, c.Country))

    headers = ','.join(f.name for f in fields(MedalWinner))

    rows = '\n'.join(
        f'{row.Country},{row.Gold},{row.Silver},{row.Bronze},{row.Total}'
        for row in countries
    )

    return f'{headers}\n{rows}'


tests = [
    (
        [['USA', 'CAN', 'NOR'], ['NOR', 'USA', 'CAN'], ['USA', 'NOR', 'SWE']],
        'Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1',
    ),
    (
        [['NOR', 'SWE', 'FIN']],
        'Country,Gold,Silver,Bronze,Total\nNOR,1,0,0,1\nFIN,0,0,1,1\nSWE,0,1,0,1',
    ),
    (
        [['ITA', 'CHN', 'CHN'], ['JPN', 'ITA', 'JPN']],
        'Country,Gold,Silver,Bronze,Total\nITA,1,1,0,2\nJPN,1,0,1,2\nCHN,0,1,1,2',
    ),
    (
        [
            ['USA', 'CAN', 'NOR'],
            ['GER', 'FRA', 'ITA'],
            ['JPN', 'KOR', 'CHN'],
            ['SWE', 'FIN', 'NOR'],
            ['CAN', 'USA', 'SWE'],
            ['FRA', 'GER', 'ITA'],
        ],
        'Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nFRA,1,1,0,2\nGER,1,1,0,2\nJPN,1,0,0,1\nSWE,1,0,1,2\nUSA,1,1,0,2\nCHN,0,0,1,1\nFIN,0,1,0,1\nITA,0,0,2,2\nKOR,0,1,0,1\nNOR,0,0,2,2',
    ),
    (
        [
            ['ESP', 'ITA', 'FRA'],
            ['ITA', 'ESP', 'GER'],
            ['NOR', 'SWE', 'FIN'],
            ['FIN', 'NOR', 'SWE'],
            ['USA', 'CAN', 'MEX'],
            ['CAN', 'USA', 'MEX'],
            ['JPN', 'KOR', 'CHN'],
            ['CHN', 'JPN', 'KOR'],
        ],
        'Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nCHN,1,0,1,2\nESP,1,1,0,2\nFIN,1,0,1,2\nITA,1,1,0,2\nJPN,1,1,0,2\nNOR,1,1,0,2\nUSA,1,1,0,2\nFRA,0,0,1,1\nGER,0,0,1,1\nKOR,0,1,1,2\nMEX,0,0,2,2\nSWE,0,1,1,2',
    ),
    (
        [
            ['USA', 'CAN', 'GER'],
            ['NOR', 'SWE', 'FIN'],
            ['USA', 'NOR', 'SWE'],
            ['GER', 'FRA', 'ITA'],
            ['JPN', 'KOR', 'CHN'],
            ['USA', 'GER', 'CAN'],
            ['SWE', 'NOR', 'FIN'],
            ['CAN', 'USA', 'NOR'],
            ['FRA', 'GER', 'ITA'],
            ['JPN', 'CHN', 'KOR'],
            ['SWE', 'FIN', 'NOR'],
            ['GER', 'ITA', 'FRA'],
        ],
        'Country,Gold,Silver,Bronze,Total\nUSA,3,1,0,4\nGER,2,2,1,5\nJPN,2,0,0,2\nSWE,2,1,1,4\nCAN,1,1,1,3\nFRA,1,1,1,3\nNOR,1,2,2,5\nCHN,0,1,1,2\nFIN,0,1,2,3\nITA,0,1,2,3\nKOR,0,1,1,2',
    ),
]


@mark.parametrize('winners, expected', tests)
def test_count_medals(winners: list[list[str]], expected: str) -> None:
    assert count_medals(winners) == expected


if __name__ == '__main__':
    winners, expected = tests[2]
    print(count_medals(winners))
