"""Daily Coding Challenge #83 (2025-11-01) - freeCodeCamp.org."""

# Signature Validation
# Given a message string, a secret key string, and a signature number, determine if the
# signature is valid using this encoding method:
#
# - Letters in the message and secret key have these values:
#   - a to z have values 1 to 26 respectively.
#   - A to Z have values 27 to 52 respectively.
# - All other characters have no value.
# - Compute the signature by taking the sum of the message plus the sum of the secret
#   key.
#
# For example, given the message "foo" and the secret key "bar", the signature would be
# 57:
#
# md
# f (6) + o (15) + o (15) = 36
# b (2) + a (1) + r (18) = 21
# 36 + 21 = 57
#
# Check if the computed signature matches the provided signature.
from string import ascii_lowercase, ascii_uppercase

from pytest import mark

_LETTER_VALUES = {
    char: i for i, char in enumerate(ascii_lowercase + ascii_uppercase, start=1)
}


def verify(message: str, key: str, signature: int) -> bool:
    """Check whether the signature matches the given message and key.

    Args:
        message: The message whose letters contribute to the signature.
        key: The secret key whose letters contribute to the signature.
        signature: The signature to check against.

    Returns:
        True if the computed signature equals ``signature``, False otherwise.
    """
    return sum(_LETTER_VALUES.get(char, 0) for char in message + key) == signature


tests = [
    ('foo', 'bar', 57, True),
    ('foo', 'bar', 54, False),
    ('freeCodeCamp', 'Rocks', 238, True),
    ('Is this valid?', 'No', 210, False),
    ('Is this valid?', 'Yes', 233, True),
    ('Check out the freeCodeCamp podcast,', 'in the mobile app', 514, True),
]


@mark.parametrize(('message', 'key', 'signature', 'expected'), tests)
def test_verify(message: str, key: str, signature: int, expected: bool) -> None:
    """Test verify function."""
    assert verify(message, key, signature) == expected


if __name__ == '__main__':
    message, key, signature, expected = tests[0]
    print(verify(message, key, signature))
