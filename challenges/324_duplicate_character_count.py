# Daily Coding challenge #324 (2026-06-30) - freeCodeCamp.org
# Duplicate Character Count
# Given two strings, return a count of characters from the second string that can be
# found in the first.
#
# - Duplicate characters in the second string are counted separately.
from pytest import mark


def duplicate_character_count(str1: str, str2: str) -> int:
    chars = set(str1)
    return sum(c in chars for c in str2)


tests = [
    ('aloha', 'hei', 1),
    ('jambo', 'bonjour', 4),
    ('hello', 'hola', 3),
    ('ola', 'hej', 0),
    ('ciao', 'konnichiwa', 5),
    ('merhaba', 'xin chao', 2),
    ('hello world', 'hello to everyone around the world', 26),
]


@mark.parametrize('str1, str2, expected', tests)
def test_duplicate_character_count(str1: str, str2: str, expected: int) -> None:
    assert duplicate_character_count(str1, str2) == expected


if __name__ == '__main__':
    str1, str2, expected = tests[6]
    print(duplicate_character_count(str1, str2))
