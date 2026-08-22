"""Daily Coding Challenge #12 (2025-08-22) - freeCodeCamp.org."""

# Message Decoder
# Given a secret message string, and an integer representing the number of letters that
# were used to shift the message to encode it, return the decoded string.

# A positive number means the message was shifted forward in the alphabet.
# A negative number means the message was shifted backward in the alphabet.
# Case matters, decoded characters should retain the case of their encoded counterparts.
# Non-alphabetical characters should not get decoded.
import string

from pytest import mark

ascii_letters = set(string.ascii_letters)


def _shift_char(char: str, shift: int) -> str:
    """Shift a character by the given shift value.

    If the character is not an alphabetical character, it will be returned unchanged.
    A negative shift will shift the character backward in the alphabet, while a
    positive shift will shift it forward. The case of the character will be preserved.

    Args:
        char: The character to shift.
        shift: The number of positions to shift the character.

    Returns:
        The shifted character.
    """
    if char not in ascii_letters:
        return char
    base = ord('A') if char.isupper() else ord('a')
    return chr((ord(char) - base - shift) % 26 + base)


def decode(message: str, shift: int) -> str:
    """Decode a message by shifting each character by the given shift value.

    Depends on the _shift_char function to handle the shifting of individual characters.

    Args:
        message: The encoded message to decode.
        shift: The number of positions to shift each character in the message.

    Returns:
        The decoded message.
    """
    return ''.join(_shift_char(char, shift) for char in message)


tests = [
    ('Xlmw mw e wigvix qiwweki.', 4, 'This is a secret message.'),
    ('Byffi Qilfx!', 20, 'Hello World!'),
    ('Zqd xnt njzx?', -1, 'Are you okay?'),
    ('oannLxmnLjvy', 9, 'freeCodeCamp'),
]


@mark.parametrize('message, shift, expected', tests)
def test_decode(message: str, shift: int, expected: str) -> None:
    """Test decode function."""
    assert decode(message, shift) == expected


if __name__ == '__main__':
    message, shift, expected = tests[0]
    print(decode(message, shift))
