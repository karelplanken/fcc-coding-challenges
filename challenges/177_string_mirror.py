# Daily Coding challenge #177 (2026-02-03) - freeCodeCamp.org
# String Mirror
# Given a string, return a new string that consists of the given string with a reversed
# copy of itself appended to the end of it.
from pytest import mark


def mirror(s: str) -> str:
    return s + s[::-1]


tests = [
    ('freeCodeCamp', 'freeCodeCamppmaCedoCeerf'),
    ('RaceCar', 'RaceCarraCecaR'),
    ('helloworld', 'helloworlddlrowolleh'),
    ('The quick brown fox...', 'The quick brown fox......xof nworb kciuq ehT'),
]


@mark.parametrize('s, expected', tests)
def test_mirror(s: str, expected: str) -> None:
    assert mirror(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(mirror(s))
