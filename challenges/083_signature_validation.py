# Daily Coding challenge #83 (2025-11-01) - freeCodeCamp.org
# Signature Validation
# Given a message string, a secret key string, and a signature number, determine if the
# signature is valid using this encoding method:

# Letters in the message and secret key have these values:
# a to z have values 1 to 26 respectively.
# A to Z have values 27 to 52 respectively.
# All other characters have no value.
# Compute the signature by taking the sum of the message plus the sum of the secret key.
# For example, given the message "foo" and the secret key "bar", the signature would
# be 57:

# f (6) + o (15) + o (15) = 36
# b (2) + a (1) + r (18) = 21
# 36 + 21 = 57
# Check if the computed signature matches the provided signature.
from pytest import mark


def verify(message: str, key: str, signature: int) -> bool:
    def get_value(char: str) -> int:
        if char.isupper():
            return ord(char) - ord('A') + 27
        elif char.islower():
            return ord(char) - ord('a') + 1
        else:
            return 0

    return sum(get_value(char) for char in message + key if char.isalpha()) == signature


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
    assert verify(message, key, signature) == expected


if __name__ == '__main__':
    message, key, signature, expected = tests[0]
    print(verify(message, key, signature))
