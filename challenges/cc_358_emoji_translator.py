"""Daily Coding Challenge #358 (2026-08-03) - freeCodeCamp.org."""

# Emoji Translator
# Given a string of emojis, return the phrase using the following table:
#
# | Emoji | Word |
# |-------|------|
# | 👶 | "baby" |
# | 🐱 | "cat" |
# | 🐕 | "dog" |
# | 🐟 | "fish" |
# | 🥵 | "hot" |
# | 🧊 | "ice" |
# | 🪨 | "rock" |
# | 🦈 | "shark" |
# | 🍲 | "soup" |
# | ⭐ | "star" |
#
# Return the words separated by spaces.
from types import MappingProxyType

from pytest import mark

EMOJI_TO_WORD = MappingProxyType({
    '👶': 'baby',
    '🐱': 'cat',
    '🐕': 'dog',
    '🐟': 'fish',
    '🥵': 'hot',
    '🧊': 'ice',
    '🪨': 'rock',
    '🦈': 'shark',
    '🍲': 'soup',
    '⭐': 'star',
})


def get_emoji_phrase(s: str) -> str:
    """Translates a string of emojis into space-separated words.

    Assumes a string of no, one or more emojis.

    Args:
        s: A string of zero or more emojis from EMOJI_TO_WORD.

    Returns:
        The words joined by single spaces.

    Raises:
        KeyError: If an emoji in s is not in the EMOJI_TO_WORD mapping.
    """
    return ' '.join(EMOJI_TO_WORD[emoji] for emoji in s)


tests = [
    ('🪨⭐', 'rock star'),
    ('🥵🐕', 'hot dog'),
    ('👶🦈', 'baby shark'),
    ('⭐🐟', 'star fish'),
    ('🧊🧊👶', 'ice ice baby'),
    ('🐱🐟🍲', 'cat fish soup'),
]


@mark.parametrize('s, expected', tests)
def test_get_emoji_phrase(s: str, expected: str) -> None:
    """Test get_emoji_phrase function."""
    assert get_emoji_phrase(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(len(get_emoji_phrase(s)))
    print(get_emoji_phrase(s))
