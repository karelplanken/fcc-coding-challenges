# Daily Coding challenge #30 (2025-09-09) - freeCodeCamp.org
# Unique Characters
# Given a string, determine if all the characters in the string are unique.

# Uppercase and lowercase letters should be considered different characters.
from pytest import mark


def all_unique(s: str) -> bool:
    return len(set(s)) == len(s)


# Alternative: Early termination for very long strings
# def all_unique_early_exit(s: str) -> bool:
#     seen = set()
#     for char in s:
#         if char in seen:
#             return False
#         seen.add(char)
#     return True


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
    assert all_unique(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(all_unique(s))
