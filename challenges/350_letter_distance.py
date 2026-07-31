# Daily Coding challenge #350 (2026-07-26) - freeCodeCamp.org
# Letter Distance
# Given two strings of equal length, return the sum of the shortest distances between
# each pair of characters.
#
# - The input will only contain lowercase letters
# - The alphabet is treated as a circle, so the distance between a and z is 1.
from string import ascii_lowercase

from pytest import mark

LETTER_VALUES = {letter: digit for digit, letter in enumerate(ascii_lowercase)}
NUM_LETTERS = len(LETTER_VALUES)
TURNAROUND = len(LETTER_VALUES) // 2


def get_shortest_letter_distance(letter1: str, letter2: str) -> int:
    """Returns the shortest distance between two letters using a circular alphabet
    approach.

    Assumes that both letters are are member of string.ascii_lowercase (lowercase latin
    aplhabet).

    Args:
        letter1: first letter
        letter2: second letter

    Returns:
        shortest distance between letter1 and letter2
    """
    distance = abs(LETTER_VALUES[letter2] - LETTER_VALUES[letter1])

    if distance < TURNAROUND:
        return distance
    else:
        return NUM_LETTERS - distance


def letter_distance(str1: str, str2: str) -> int:
    """Given two strings of equal length, returns the sum of the shortest distances
    between each pair of characters.

    Assumes str1 and str2 are of equal non-zero length. It inherits the
    "lowercase ascii letters only" assumption made by get_shortest_letter_distance.

    Args:
        str1: First string.
        str2: Second string.

    Returns:
        The sum of shortest distances between each letter pair of str1 and str2.
    """
    return sum(
        get_shortest_letter_distance(l1, l2) for l1, l2 in zip(str1, str2, strict=True)
    )


tests = [
    ('abc', 'bcd', 3),
    ('abc', 'xyz', 9),
    ('encrypt', 'decrypt', 10),
    ('algorithm', 'codeblock', 43),
    ('lobster', 'penguin', 47),
    ('alligator', 'crocodile', 55),
]


@mark.parametrize('str1, str2, expected', tests)
def test_letter_distance(str1: str, str2: str, expected: int) -> None:
    assert letter_distance(str1, str2) == expected


if __name__ == '__main__':
    str1, str2, expected = tests[5]
    print(letter_distance(str1, str2))
