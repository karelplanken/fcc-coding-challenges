"""Daily Coding Challenge #54 (2025-10-03) - freeCodeCamp.org."""

# P@ssw0rd Str3ngth!
# Given a password string, return "weak", "medium", or "strong" based on the strength of
# the password.
#
# A password is evaluated according to the following rules:
#
# - It is at least 8 characters long.
# - It contains both uppercase and lowercase letters.
# - It contains at least one number.
# - It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
#
# Return "weak" if the password meets fewer than two of the rules.
# Return "medium" if the password meets 2 or 3 of the rules.
# Return "strong" if the password meets all 4 rules.
import string

from pytest import mark

_DIGITS = frozenset(string.digits)
_LOWER_CHARS = frozenset(string.ascii_lowercase)
_UPPER_CHARS = frozenset(string.ascii_uppercase)
_SPECIAL_CHARS = frozenset('!@#$%^&*')


def _has_any(chars: set[str], pool: frozenset[str]) -> bool:
    return not chars.isdisjoint(pool)


def check_strength(password: str) -> str:
    """Check the strength of a password.

    Letters and digits are matched as ASCII only.

    Args:
        password: The password string to evaluate.

    Returns:
        The strength of the password: "weak", "medium", or "strong".
    """
    chars = set(password)
    checks = (
        len(password) >= 8,
        _has_any(chars, _UPPER_CHARS) and _has_any(chars, _LOWER_CHARS),
        _has_any(chars, _DIGITS),
        _has_any(chars, _SPECIAL_CHARS),
    )
    rules_met = sum(checks)

    if rules_met == len(checks):
        return 'strong'
    return 'medium' if rules_met >= 2 else 'weak'


tests = [
    ('123456', 'weak'),
    ('pass!!!', 'weak'),
    ('Qwerty', 'weak'),
    ('PASSWORD', 'weak'),
    ('PASSWORD!', 'medium'),
    ('PassWord%^!', 'medium'),
    ('qwerty12345', 'medium'),
    ('S3cur3P@ssw0rd', 'strong'),
    ('C0d3&Fun!', 'strong'),
]


@mark.parametrize('password, expected', tests)
def test_check_strength(password: str, expected: str) -> None:
    """Test check_strength function."""
    assert check_strength(password) == expected


if __name__ == '__main__':
    password, expected = tests[0]
    print(check_strength(password))
