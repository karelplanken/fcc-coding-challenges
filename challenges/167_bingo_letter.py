# Daily Coding challenge #167 (2026-01-24) - freeCodeCamp.org
# Bingo! Letter
# Given a number, return the bingo letter associated with it (capitalized).
# Bingo numbers are grouped as follows:

# Letter	Number Range
# "B"	1-15
# "I"	16-30
# "N"	31-45
# "G"	46-60
# "O"	61-75
from pytest import mark


# Simpler solution since the ranges are uniform.
def get_bingo_letter(n: int) -> str:
    if not 1 <= n <= 75:
        raise ValueError('Number must be in range 1-75')

    letters = 'BINGO'
    return letters[(n - 1) // 15]


tests = [
    (75, 'O'),
    (54, 'G'),
    (25, 'I'),
    (38, 'N'),
    (11, 'B'),  # Original test case value was here '11'
]


@mark.parametrize('n,expected', tests)
def test_get_bingo_letter(n: int, expected: str) -> None:
    assert get_bingo_letter(n) == expected


if __name__ == '__main__':
    n, expected = tests[4]
    print(get_bingo_letter(n))
