"""Daily Coding Challenge #67 (2025-10-16) - freeCodeCamp.org."""

# Email Validator
# Given a string, determine if it is a valid email address using the following
# constraints:
#
# - It must contain exactly one @ symbol.
# - The local part (before the @):
#   - Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or
# hyphens (-).
#   - Cannot start or end with a dot.
# - The domain part (after the @):
#   - Must contain at least one dot.
#   - Must end with a dot followed by at least two letters.
# - Neither the local or domain part can have two dots in a row.
from string import ascii_letters, digits

from pytest import mark

_LOCAL_CHARS = frozenset(ascii_letters + digits + '._-')
_ASCII_LETTERS = frozenset(ascii_letters)


def validate(e_mail: str) -> bool:
    """Validate an email address based on the given constraints.

    Args:
        e_mail: The email address to validate.

    Returns:
        True if the email address is valid, False otherwise.
    """
    if e_mail.count('@') != 1:
        return False
    local, domain = e_mail.split('@')

    # Empty local part rejected deliberately: the spec presupposes one exists.
    if not local or local[0] == '.' or local[-1] == '.':
        return False
    if not _LOCAL_CHARS.issuperset(local) or '..' in e_mail:
        return False

    _, dot, tld = domain.rpartition('.')
    return bool(dot) and len(tld) >= 2 and _ASCII_LETTERS.issuperset(tld)


tests = [
    ('a@b.cd', True),
    ('hell.-w.rld@example.com', True),
    ('.b@sh.rc', False),
    ('example@test.c0', False),
    ('freecodecamp.org', False),
    ('develop.ment_user@c0D!NG.R.CKS', True),
    ('hello.@wo.rld', False),
    ('hello@world..com', False),
    ('develop..ment_user@c0D!NG.R.CKS', False),
    ('git@commit@push.io', False),
]


@mark.parametrize('e_mail, expected', tests)
def test_validate(e_mail: str, expected: bool) -> None:
    """Test validate function."""
    assert validate(e_mail) == expected


if __name__ == '__main__':
    e_mail, expected = tests[0]
    print(validate(e_mail))
