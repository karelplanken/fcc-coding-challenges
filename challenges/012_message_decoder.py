# Daily Coding challenge #12 (2025-08-22) - freeCodeCamp.org
# Message Decoder
# Given a secret message string, and an integer representing the number of letters that
# were used to shift the message to encode it, return the decoded string.

# A positive number means the message was shifted forward in the alphabet.
# A negative number means the message was shifted backward in the alphabet.
# Case matters, decoded characters should retain the case of their encoded counterparts.
# Non-alphabetical characters should not get decoded.
from pytest import mark

# def decode(message: str, shift: int) -> str:
#     return ''.join(
#         chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
#         if char.islower()
#         else chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
#         if char.isupper()
#         else char
#         for char in message
#     )


def decode(message: str, shift: int) -> str:
    def shift_char(char: str) -> str:
        if not char.isalpha():
            return char
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base - shift) % 26 + base)

    return ''.join(shift_char(c) for c in message)


tests = [
    ('Xlmw mw e wigvix qiwweki.', 4, 'This is a secret message.'),
    ('Byffi Qilfx!', 20, 'Hello World!'),
    ('Zqd xnt njzx?', -1, 'Are you okay?'),
    ('oannLxmnLjvy', 9, 'freeCodeCamp'),
]


@mark.parametrize('message, shift, expected', tests)
def test_decode(message: str, shift: int, expected: str) -> None:
    assert decode(message, shift) == expected


if __name__ == '__main__':
    message, shift, expected = tests[0]
    print(decode(message, shift))
