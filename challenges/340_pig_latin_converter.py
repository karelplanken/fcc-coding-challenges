# Daily Coding challenge #340 (2026-07-16) - freeCodeCamp.org
# Pig Latin Converter
# Given a string, convert it to Pig Latin using the following rules:
#
# - If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to
#   the end. For example, "universe" converts to "universeway".
# - If a word begins with one or more consonants, move them to the end and add "ay".
#   For example, "hello" converts to "ellohay".
# - Preserve the case of the first letter. For example, "Hello" converts to
#   "Ellohay".
from pytest import mark

VOWELS = set('aeiou')
VOWEL_SUFFIX = 'way'
CONSONANT_SUFFIX = 'ay'


def _pig_latin_word(word: str) -> str:
    is_capitalized = word[0].isupper()
    lower_word = word.lower()

    idx = next((i for i, ch in enumerate(lower_word) if ch in VOWELS), len(lower_word))
    result = (
        lower_word + VOWEL_SUFFIX
        if idx == 0
        else lower_word[idx:] + lower_word[:idx] + CONSONANT_SUFFIX
    )

    return result.capitalize() if is_capitalized else result


def pig_latin(s: str) -> str:
    return ' '.join(_pig_latin_word(word) for word in s.split())


tests = [
    ('universe', 'universeway'),
    ('hello', 'ellohay'),
    ('hello universe', 'ellohay universeway'),
    ('Hello universe', 'Ellohay universeway'),
    ('Pig Latin is fun', 'Igpay Atinlay isway unfay'),
    (
        'The quick brown fox jumped over the lazy dog',
        'Ethay uickqay ownbray oxfay umpedjay overway ethay azylay ogday',
    ),
]


@mark.parametrize('s, expected', tests)
def test_pig_latin(s: str, expected: str) -> None:
    assert pig_latin(s) == expected


if __name__ == '__main__':
    s, expected = tests[5]
    print(pig_latin(s))
