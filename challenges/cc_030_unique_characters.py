"""Daily Coding Challenge #30 (2025-09-09) - freeCodeCamp.org."""

# Unique Characters
# Given a string, determine if all the characters in the string are unique.
#
# - Uppercase and lowercase letters should be considered different characters.
from pytest import mark


def all_unique(s: str) -> bool:
    """Determines if all characters in the string are unique.

    Uses early exit: returns as soon as a duplicate is found, so long
    strings with an early duplicate are handled without scanning to the end.

    Args:
        s: The input string to check for unique characters.

    Returns:
        True if all characters in the string are unique, False otherwise.
    """
    seen: set[str] = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True


tests = [
    ('abc', True),
    ('aA', True),
    ('QwErTy123!@', True),
    ('~!@#$%^&*()_+', True),
    ('hello', False),
    ('freeCodeCamp', False),
    ('!@#*$%^&*()aA', False),
]


@mark.parametrize('s, expected', tests)
def test_all_unique(s: str, expected: bool) -> None:
    """Test all_unique function."""
    assert all_unique(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(all_unique(s))
