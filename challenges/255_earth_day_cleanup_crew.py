# Daily Coding challenge #255 (2026-04-22) - freeCodeCamp.org
# Earth Day Cleanup Crew
# Today is Earth Day. Given an array of items you cleaned up, return your total cleanup
# score based on the rules below.

# Given items will be one of:

# Item	Base Value
# "bottle"	10
# "can"	6
# "bag"	8
# "tire"	35
# "straw"	4
# "cardboard"	3
# "newspaper"	3
# "shoe"	12
# "electronics"	25
# "battery"	18
# "mattress"	38
# A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items
# do not get a streak bonus.

# Streak bonus: If the same item appears consecutively, it gets increasing bonus points.
# First consecutive occurrence: base value
# Second: base value + 1
# Third: base value + 2
# etc.

# Fifth Item Multiplier: Every fifth item collected gets a multiplier.
# Fifth item: *2
# Tenth item: *3
# etc.
# Apply the multiplier after calculating any bonuses.
from collections.abc import Generator
from dataclasses import dataclass
from types import MappingProxyType

from pytest import mark

Item = str | list[str | int]

ITEM_TO_BASE_VALUE = MappingProxyType(
    {
        'bottle': 10,
        'can': 6,
        'bag': 8,
        'tire': 35,
        'straw': 4,
        'cardboard': 3,
        'newspaper': 3,
        'shoe': 12,
        'electronics': 25,
        'battery': 18,
        'mattress': 38,
    }
)


@dataclass
class _StreakTracker:
    prev: str | None = None
    streak: int = 0

    def score(self, item: Item) -> int:
        if isinstance(item, list):
            self.prev, self.streak = None, 0
            return int(item[1])
        self.streak = self.streak if item == self.prev else 0
        self.prev = item
        self.streak += 1
        return ITEM_TO_BASE_VALUE[item] + self.streak - 1


def item_values(items: list[Item]) -> Generator[int]:
    streak_tracker = _StreakTracker()

    for item in items:
        yield streak_tracker.score(item)


def fifth_item_multiplier(position: int) -> int:
    return position // 5 + 1 if position % 5 == 0 else 1


def get_cleanup_score(items: list[Item]) -> int:
    return sum(
        value * fifth_item_multiplier(position)
        for position, value in enumerate(item_values(items), start=1)
    )


tests: list[tuple[list[Item], int]] = [
    (['bottle', 'straw', 'shoe', 'battery'], 44),
    (['electronics', 'straw', 'newspaper', 'bottle', 'bag'], 58),
    (['shoe', 'can', 'can', 'can', 'bottle', 'bottle', 'straw', 'straw', 'straw'], 79),
    (['mattress', ['rare', 80], 'tire', 'tire', 'tire', ['rare', 95]], 358),
    (
        [
            'bottle',
            'can',
            'can',
            'shoe',
            'shoe',
            ['rare', 56],
            'bottle',
            'bottle',
            'can',
            'can',
            'electronics',
            'bottle',
            ['rare', 48],
            'bottle',
            'can',
            'can',
            'can',
            'can',
            'can',
            'can',
            'can',
        ],
        383,
    ),
]


@mark.parametrize('items, expected', tests)
def test(items: list[Item], expected: int) -> None:
    assert get_cleanup_score(items) == expected


if __name__ == '__main__':
    items, expected = tests[4]
    print(get_cleanup_score(items))
