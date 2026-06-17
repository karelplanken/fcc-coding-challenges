# Daily Coding challenge #311 (2026-06-17) - freeCodeCamp.org
# Spellcaster
# Given a string of spell codes you are casting, calculate the total score.

# Each character in the string represents a spell:

# Code	Spell	Category	Base Score
# "f"	Fire	Destruction	3
# "l"	Lightning	Destruction	3
# "i"	Ice	Control	2
# "w"	Wind	Control	2
# "h"	Heal	Restoration	1
# "s"	Shield	Restoration	1
# A combo multiplier is applied based on how many spells in a row have been cast from
# different categories:

# The first spell always scores at base value.
# Each consecutive spell from a different category than the previous increases the
# multiplier by 1.
# Casting a spell from the same category as the previous resets the multiplier
# back to 1.
# The score for each spell is its base score multiplied by the current multiplier.
# Return the total score from the sequence of spells.
from dataclasses import dataclass
from types import MappingProxyType

from pytest import mark


@dataclass(frozen=True)
class Spell:
    code: str
    spell: str
    category: str
    base_score: int


RAW_SPELLS = [
    Spell('f', 'Fire', 'Destruction', 3),
    Spell('l', 'Lightning', 'Destruction', 3),
    Spell('i', 'Ice', 'Control', 2),
    Spell('w', 'Wind', 'Control', 2),
    Spell('h', 'Heal', 'Restoration', 1),
    Spell('s', 'Shield', 'Restoration', 1),
]

SPELLS: MappingProxyType[str, Spell] = MappingProxyType({
    spell.code: spell for spell in RAW_SPELLS
})


class Multiplier:
    _SENTINEL = object()  # never equal to any category string

    def __init__(self) -> None:
        self.value = 0  # sentinel-compatible starting point
        self._prev_cat: object = self._SENTINEL

    def get_value(self, spell: Spell) -> int:
        self.value = self.value + 1 if self._prev_cat != spell.category else 1
        self._prev_cat = spell.category
        return self.value


def cast(spells: str) -> int:
    multiplier = Multiplier()

    return sum(
        SPELLS[spell].base_score * multiplier.get_value(SPELLS[spell])
        for spell in spells
    )


tests = [
    ('fihwl', 33),
    ('lwswfi', 45),
    ('wislhfl', 37),
    ('sihwlih', 50),
    ('wishlfihwslwifihl', 101),
]


@mark.parametrize('spells, expected', tests)
def test(spells: str, expected: int) -> None:
    assert cast(spells) == expected


if __name__ == '__main__':
    spells, expected = tests[4]
    print(cast(spells))
