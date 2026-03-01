# Daily Coding challenge #149 (2026-01-06) - freeCodeCamp.org
# vOwElcAsE
# Given a string, return a new string where all vowels are converted to uppercase and
# all other alphabetical characters are converted to lowercase.

# Vowels are "a", "e", "i", "o", and "u" in any case.
# Non-alphabetical characters should remain unchanged.
from pytest import mark


def vowel_case(s: str) -> str:
    return ''.join(char.upper() if char in 'aeiou' else char for char in s.lower())


# Slightly more explicit, doesn't lowercase non-alphabetical characters unnecessarily,
# more explicit about vowel checking:
# def vowel_case(s: str) -> str:
#     vowels = 'aeiouAEIOU'
#     return ''.join(
#         char.upper() if char in vowels else char.lower() if char.isalpha() else char
#         for char in s
#     )

tests = [
    ('vowelcase', 'vOwElcAsE'),
    ('coding is fun', 'cOdIng Is fUn'),
    ('HELLO, world!', 'hEllO, wOrld!'),
    ('git cherry-pick', 'gIt chErry-pIck'),
    ('HEAD~1', 'hEAd~1'),
]


@mark.parametrize(('s', 'expected'), tests)
def test_vowel_case(s: str, expected: str) -> None:
    assert vowel_case(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(vowel_case(s))
