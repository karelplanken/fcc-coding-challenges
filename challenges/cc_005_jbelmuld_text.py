"""Daily Coding Challenge #5 (2025-08-15) - freeCodeCamp.org."""

# Jbelmud Text
# Given a string, return a jumbled version of that string where each word is
# transformed using the following constraints:

# The first and last letters of the words remain in place
# All letters between the first and last letter are sorted alphabetically.
# The input strings will contain no punctuation, and will be entirely lowercase.
from string import ascii_lowercase

from pytest import mark


def _jumble_word(word: str) -> str:
    """Jumbles a single word according to the specified rules.

    Rules: The first and last letters of the word remain in place, and all letters
    between the first and last letter are sorted alphabetically.

    Args:
        word: The word to be jumbled.

    Returns:
        The jumbled version of the word.
    """
    return word if len(word) <= 3 else word[0] + ''.join(sorted(word[1:-1])) + word[-1]


def jbelmu(text: str) -> str:
    """Returns a jumbled version of the input text.

    Args:
        text: The input string containing words to be jumbled.

    Returns:
        The jumbled version of the input text.

    Raises:
        ValueError: If the input text contains characters other than lowercase letters.
    """
    if not all(char in ascii_lowercase for char in text if char != ' '):
        msg = 'all letters in text must be lowercase letter'
        raise ValueError(msg)

    return ' '.join(_jumble_word(word) for word in text.split())


tests = [
    ('hello world', 'hello wlord'),
    ('i love jumbled text', 'i love jbelmud text'),
    (
        'freecodecamp is my favorite place to learn to code',
        'faccdeeemorp is my faiortve pacle to laern to cdoe',
    ),
    (
        'the quick brown fox jumps over the lazy dog',
        'the qciuk borwn fox jmpus oevr the lazy dog',
    ),
]


@mark.parametrize('text, expected', tests)
def test_jbelmu(text: str, expected: str) -> None:
    """Test jbelmu function."""
    assert jbelmu(text) == expected


if __name__ == '__main__':
    text, expected = tests[0]
    print(jbelmu(text))
