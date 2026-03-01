# Daily Coding challenge #82 (2025-10-31) - freeCodeCamp.org
# SpOoKy~CaSe
# Given a string representing a variable name, convert it to "spooky case" using the
# following constraints:

# Replace all underscores (_), and hyphens (-) with a tilde (~).
# Capitalize the first letter of the string, and every other letter after that. Ignore
# the tilde character when counting. Make all other letters lowercase.
# For example, given hello_world, return HeLlO~wOrLd.
from pytest import mark

# def spookify(boo: str) -> str:
#     spooky_cased = []
#     count = 1
#     for char in boo.replace('-', '~').replace('_', '~'):
#         if char.isalpha():
#             spooky_cased.append(char.upper() if count % 2 == 1 else char.lower())
#             count += 1
#         else:
#             spooky_cased.append(char)
#     return ''.join(spooky_cased)


def spookify(boo: str) -> str:
    result = []
    count = 1

    for char in boo:
        if char in '_-':
            result.append('~')
        elif char.isalpha():
            result.append(char.upper() if count % 2 == 1 else char.lower())
            count += 1
        else:
            result.append(char)  # handles any other characters

    return ''.join(result)


tests = [
    ('hello_world', 'HeLlO~wOrLd'),
    ('Spooky_Case', 'SpOoKy~CaSe'),
    ('TRICK-or-TREAT', 'TrIcK~oR~tReAt'),
    ('c_a-n_d-y_-b-o_w_l', 'C~a~N~d~Y~~b~O~w~L'),
    ('thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts', 'ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS'),
]


@mark.parametrize('boo, expected', tests)
def test_spookify(boo: str, expected: str) -> None:
    assert spookify(boo) == expected


if __name__ == '__main__':
    boo, expected = tests[0]
    print(spookify(boo))
