# Daily Coding challenge #99 (2025-11-17) - freeCodeCamp.org
# Fingerprint Test
# Given two strings representing fingerprints, determine if they are a match using the
# following rules:

# Each fingerprint will consist only of lowercase letters (a-z).
# Two fingerprints are considered a match if:
# They are the same length.
# The number of differing characters does not exceed 10% of the fingerprint length.
from pytest import mark


def is_match(fingerprint_a: str, fingerprint_b: str) -> bool:
    if len(fingerprint_a) == len(fingerprint_b):
        return (
            sum(
                1
                for (char_a, char_b) in zip(fingerprint_a, fingerprint_b)
                if char_a != char_b
            )
            / len(fingerprint_a)
            <= 0.10
        )

    return False


tests = [
    ('helloworld', 'helloworld', True),
    ('helloworld', 'helloworlds', False),
    ('helloworld', 'jelloworld', True),
    (
        'thequickbrownfoxjumpsoverthelazydog',
        'thequickbrownfoxjumpsoverthelazydog',
        True,
    ),
    (
        'theslickbrownfoxjumpsoverthelazydog',
        'thequickbrownfoxjumpsoverthehazydog',
        True,
    ),
    (
        'thequickbrownfoxjumpsoverthelazydog',
        'thequickbrownfoxjumpsoverthehazycat',
        False,
    ),
]


@mark.parametrize(('fingerprint_a', 'fingerprint_b', 'expected'), tests)
def test_is_match(fingerprint_a: str, fingerprint_b: str, expected: bool) -> None:
    assert is_match(fingerprint_a, fingerprint_b) == expected


if __name__ == '__main__':
    fingerprint_a, fingerprint_b, expected = tests[2]
    print(is_match(fingerprint_a, fingerprint_b))
