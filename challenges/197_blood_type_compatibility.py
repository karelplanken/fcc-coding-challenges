# Daily Coding challenge #197 (2026-02-23) - freeCodeCamp.org
# Blood Type Compatibility
# Given a donor blood type and a recipient blood type, determine whether the donor can
# give blood to the recipient.

# Each blood type consists of:

# A letter: "A", "B", "AB", or "O"
# And an Rh factor: "+" or "-"
# Blood types will be one of the valid letters followed by an Rh factor. For example,
# "AB+" and "O-" are valid blood types.

# Letter Rules:

# "O" can donate to other letter type.
# "A" can donate to "A" and "AB".
# "B" can donate to "B" and "AB".
# "AB" can donate only to "AB".
# Rh Rules:

# Negative ("-") can donate to both "-" and "+".
# Positive ("+") can donate only to "+".
# Both letter and Rh rule must pass for a donor to be able to donate to the recipient.
from types import MappingProxyType

from pytest import mark

BLOOD_COMP = MappingProxyType({
    'O': frozenset({'O', 'A', 'B', 'AB'}),
    'A': frozenset({'A', 'AB'}),
    'B': frozenset({'B', 'AB'}),
    'AB': frozenset({'AB'})
})

RH_COMP = MappingProxyType({
    '+': frozenset({'+'}),
    '-': frozenset({'-', '+'})
})

def can_donate(donor: str, recipient: str) -> bool:
    donor_blood_type, donor_rh = donor[:-1], donor[-1]
    recipient_blood_type, recipient_rh = recipient[:-1], recipient[-1]

    return (
        recipient_blood_type in BLOOD_COMP[donor_blood_type]
        and recipient_rh in RH_COMP[donor_rh]
    )


tests = [
    ('B+', 'B+', True),
    ('O-', 'AB-', True),
    ('O+', 'A-', False),
    ('A+', 'AB+', True),
    ('A-', 'B-', False),
    ('B-', 'AB+', True),
    ('B-', 'A+', False),
    ('O-', 'O+', True),
    ('O+', 'O-', False),
    ('AB+', 'AB-', False),
]


@mark.parametrize('donor, recipient, expected', tests)
def test_can_donate(donor: str, recipient: str, expected: bool) -> None:
    assert can_donate(donor, recipient) == expected


if __name__ == '__main__':
    donor, recipient, expected = tests[0]
    print(can_donate(donor, recipient))
