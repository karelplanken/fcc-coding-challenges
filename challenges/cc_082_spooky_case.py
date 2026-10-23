"""Daily Coding Challenge #82 (2025-10-31) - freeCodeCamp.org."""

# SpOoKy~CaSe
# Given a string representing a variable name, convert it to "spooky case" using the
# following constraints:
#
# - Replace all underscores (_), and hyphens (-) with a tilde (~).
# - Capitalize the first letter of the string, and every other letter after that. Ignore
#   the tilde character when counting. Make all other letters lowercase.
#
# For example, given hello_world, return HeLlO~wOrLd.
from itertools import cycle

from pytest import mark

_TILDE_TABLE = str.maketrans({'_': '~', '-': '~'})


def spookify(boo: str) -> str:
    """Convert a variable name to spooky case.

    Underscores and hyphens become tildes. Letters alternate upper/lower case,
    starting with upper; only letters advance the alternation, and all other
    characters pass through unchanged.

    Args:
        boo: Variable name to convert.

    Returns:
        The spooky case version of the variable name.
    """
    case = cycle((str.upper, str.lower))
    return ''.join(
        next(case)(char) if char.isalpha() else char
        for char in boo.translate(_TILDE_TABLE)
    )


tests = [
    ('hello_world', 'HeLlO~wOrLd'),
    ('Spooky_Case', 'SpOoKy~CaSe'),
    ('TRICK-or-TREAT', 'TrIcK~oR~tReAt'),
    ('c_a-n_d-y_-b-o_w_l', 'C~a~N~d~Y~~b~O~w~L'),
    ('thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts', 'ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS'),
]


@mark.parametrize('boo, expected', tests)
def test_spookify(boo: str, expected: str) -> None:
    """Test spookify function."""
    assert spookify(boo) == expected


if __name__ == '__main__':
    boo, expected = tests[0]
    print(spookify(boo))
