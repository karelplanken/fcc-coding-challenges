# Daily Coding challenge #194 (2026-02-20) - freeCodeCamp.org
# 2026 Winter Games Day 15: Freestyle Skiing
# Given a trick name consisting of two words, determine if it is a valid freestyle
# skiing trick name.

# A trick is valid if the first word is in the list of valid first words, and the
# second word is in the list of valid second words.

# The two words will be separated by a single space.
# Valid first words:

# "Misty"
# "Ghost"
# "Thunder"
# "Solar"
# "Sky"
# "Phantom"
# "Frozen"
# "Polar"
# Valid second words:

# "Twister"
# "Icequake"
# "Avalanche"
# "Vortex"
# "Snowstorm"
# "Frostbite"
# "Blizzard"
# "Shadow"
from pytest import mark

VALID_FIRST_WORDS = {
    'Misty',
    'Ghost',
    'Thunder',
    'Solar',
    'Sky',
    'Phantom',
    'Frozen',
    'Polar',
}

VALID_SECOND_WORDS = {
    'Twister',
    'Icequake',
    'Avalanche',
    'Vortex',
    'Snowstorm',
    'Frostbite',
    'Blizzard',
    'Shadow',
}


def is_valid_trick(trick_name: str) -> bool:
    first_word, second_word = trick_name.split(' ', maxsplit=1)
    return first_word in VALID_FIRST_WORDS and second_word in VALID_SECOND_WORDS


tests = [
    ('Polar Vortex', True),
    ('Solar Icequake', True),
    ('Thunder Blizzard', True),
    ('Phantom Frostbite', True),
    ('Ghost Avalanche', True),
    ('Snowstorm Shadow', False),
    ('Solar Sky', False),
]


@mark.parametrize('trick_name, expected', tests)
def test_is_valid_trick(trick_name: str, expected: bool) -> None:
    assert is_valid_trick(trick_name) == expected


if __name__ == '__main__':
    trick_name, expected = tests[0]
    print(is_valid_trick(trick_name))
