# Daily Coding challenge #4 (2025-08-14) - freeCodeCamp.org
# S P A C E J A M
# Given a string, remove all spaces from the string, insert two spaces between every
# character, convert all alphabetical letters to uppercase, and return the result.
# Non-alphabetical characters should remain unchanged (except for spaces).
from pytest import mark


def space_jam(s: str) -> str:
    return '  '.join(char.upper() for char in s if char != ' ')


# # More explicit filter
# def space_jam(s: str) -> str:
#     no_spaces = filter(lambda c: c != ' ', s)
#     return '  '.join(char.upper() for char in no_spaces)

# Method chaining
# def space_jam(s: str) -> str:
#     return '  '.join(s.replace(' ', '').upper())


tests = [
    ('freeCodeCamp', 'F  R  E  E  C  O  D  E  C  A  M  P'),
    ('   free   Code   Camp   ', 'F  R  E  E  C  O  D  E  C  A  M  P'),
    ('Hello World?!', 'H  E  L  L  O  W  O  R  L  D  ?  !'),
    ('C@t$ & D0g$', 'C  @  T  $  &  D  0  G  $'),
    ('allyourbase', 'A  L  L  Y  O  U  R  B  A  S  E'),
]


@mark.parametrize('s, expected', tests)
def test_space_jam(s: str, expected: str) -> None:
    assert space_jam(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(space_jam(s))
