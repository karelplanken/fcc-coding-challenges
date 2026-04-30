# Daily Coding challenge #246 (2026-04-13) - freeCodeCamp.org
# Name Initials
# Given a full name as a string, return their initials.

# Names to initialize are separated by a space.
# Initials should be made uppercase.
# Initials should be separated by dots.
# For example, "Tommy Millwood" returns "T.M.".
from pytest import mark


def get_initials(name: str) -> str:
    return '.'.join(word[0].upper() for word in name.split()) + '.'


tests = [
    ('Tommy Millwood', 'T.M.'),
    ('Savanna Puddlesplash', 'S.P.'),
    ('Frances Cowell Conrad', 'F.C.C.'),
    ('Dragon', 'D.'),
    ('Dorothy Vera Clump Haverstock Norris', 'D.V.C.H.N.'),
]


@mark.parametrize('name, expected', tests)
def test_get_initials(name: str, expected: str) -> None:
    assert get_initials(name) == expected


if __name__ == '__main__':
    name, expected = tests[0]
    print(get_initials(name))
