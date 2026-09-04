"""Daily Coding Challenge #25 (2025-09-04) - freeCodeCamp.org."""

# Vowel Repeater
# Given a string, return a new version of the string where each vowel is duplicated one
# more time than the previous vowel you encountered. For instance, the first vowel in
# the sentence should remain unchanged. The second vowel should appear twice in a row.
# The third vowel should appear three times in a row, and so on.
#
# - The letters a, e, i, o, and u, in either uppercase or lowercase, are considered
#   vowels.
# - The original vowel should keeps its case.
# - Repeated vowels should be lowercase.
# - All non-vowel characters should keep their original case.
from pytest import mark

VOWELS = frozenset('aeiou')  # Set for O(1) lookup


def repeat_vowels(s: str) -> str:
    """Repeat vowels in a string according to the specified rules.

    Builds a new version of `s` where each vowel is duplicated one more
    time than the previously encountered vowel.

    Args:
        s: The input string.

    Returns:
        A new string with vowels repeated according to the rules.
    """
    parts: list[str] = []
    vowel_count = 0

    for char in s:
        if (lower_char := char.lower()) in VOWELS:
            parts.append(char + lower_char * vowel_count)
            vowel_count += 1
        else:
            parts.append(char)

    return ''.join(parts)


tests = [
    ('hello world', 'helloo wooorld'),
    ('freeCodeCamp', 'freeeCooodeeeeCaaaaamp'),
    ('AEIOU', 'AEeIiiOoooUuuuu'),
    (
        'I like eating ice cream in Iceland',
        'I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam '
        + 'iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand',
    ),
]


@mark.parametrize('s, expected', tests)
def test_repeat_vowels(s: str, expected: str) -> None:
    """Test repeat_vowels function."""
    assert repeat_vowels(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(repeat_vowels(s))
