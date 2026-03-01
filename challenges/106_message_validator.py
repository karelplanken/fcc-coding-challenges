# Daily Coding challenge #106 (2025-11-24) - freeCodeCamp.org
# Message Validator

# Given a message string and a validation string, determine if the message is valid.

# A message is valid if each word in the message starts with the corresponding
# letter in the validation string, in order.
# Letters are case-insensitive.
# Words in the message are separated by single spaces.
from pytest import mark


def is_valid_message(message: str, validation: str) -> bool:
    words = message.lower().split()

    if len(words) != len(validation):
        return False

    validation = validation.lower()

    for word, letter in zip(words, validation):
        if word[0] != letter:
            return False
    return True


tests = [
    ('hello world', 'hw', True),
    ('ALL CAPITAL LETTERS', 'acl', True),
    ('Coding challenge are boring.', 'cca', False),
    ('The quick brown fox jumps over the lazy dog.', 'TQBFJOTLD', True),
    ('The quick brown fox jumps over the lazy dog.', 'TQBFJOTLDT', False),
]


@mark.parametrize('message,validation,expected', tests)
def test_is_valid_message(message: str, validation: str, expected: bool) -> None:
    assert is_valid_message(message, validation) == expected


if __name__ == '__main__':
    message, validation, expected = tests[0]
    print(is_valid_message(message, validation))
