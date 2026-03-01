# Daily Coding challenge #154 (2026-01-11) - freeCodeCamp.org
# Par for the Hole
# Given two integers, the par for a golf hole and the number of strokes a golfer took
# on that hole, return the golfer's score using golf terms.

# Return:

# "Hole in one!" if it took one stroke.
# "Eagle" if it took two strokes less than par.
# "Birdie" if it took one stroke less than par.
# "Par" if it took the same number of strokes as par.
# "Bogey" if it took one stroke more than par.
# "Double bogey" if took two strokes more than par.
from pytest import mark


def golf_score(par: int, strokes: int) -> str | None:
    if strokes == 1:
        return 'Hole in one!'

    match strokes - par:
        case -2:
            return 'Eagle'
        case -1:
            return 'Birdie'
        case 0:
            return 'Par'
        case 1:
            return 'Bogey'
        case 2:
            return 'Double bogey'
        case _:
            return None


tests = [
    (3, 3, 'Par'),
    (4, 3, 'Birdie'),
    (3, 1, 'Hole in one!'),
    (5, 7, 'Double bogey'),
    (4, 5, 'Bogey'),
    (5, 3, 'Eagle'),
]


@mark.parametrize(('par', 'strokes', 'expected'), tests)
def test_golf_score(par: int, strokes: int, expected: str) -> None:
    assert golf_score(par, strokes) == expected


if __name__ == '__main__':
    par, strokes, expected = tests[5]
    print(golf_score(par, strokes))
