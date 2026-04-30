# Daily Coding challenge #250 (2026-04-17) - freeCodeCamp.org
# Hidden Key
# Welcome to the 250th daily challenge!

# Given an encoded string, decode it using an encryption key and return it.

# To find the key:

# Look at all daily challenges up to today whose challenge number is a multiple of 25
# (including this one).
# Take the first letter from each of those challenge titles and combine them into a
# string. If the title starts with a non-letter, find its first letter.
# To decode the message, go over each letter in the encoded message and:

# Look at the corresponding letter in the key (repeat the key if the message is longer
# than the key).
# Convert the key letter to its corresponding number: "A" = 1, "B" = 2, ..., "Z" = 26.
# Shift the encoded letter backward in the alphabet by that number.
# If the shift goes before "A", wrap around to "Z".
# For example, if the encoded message starts with "Y" and the first key letter is
# "V" (22), shift "Y" back 22 places to get "C". Repeat this process for each letter to
# decode the full message.

# Only letters are shifted, spaces are returned as-is.
# All given and returned letters are uppercase.
from itertools import cycle

from pytest import mark

# See below for how I got this key...
KEY = 'VLHCGMDLNH'


def decode(message: str) -> str:
    key_cycle = cycle(ord(k) - ord('A') + 1 for k in KEY)
    result = []

    for char in message:
        if char.isalpha():
            shift = next(key_cycle)
            result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            result.append(char)

    return ''.join(result)


tests = [
    ('YAVJYNXE', 'CONGRATS'),
    ('YALLUT PQUMJP', 'CODING LEGEND'),
    ('UAC DYR EISAKYM', 'YOU ARE AWESOME'),
    ('GQMS NBMZU', 'KEEP GOING'),
    (
        'W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB',
        'A WINNER IS A DREAMER WHO NEVER GIVES UP',
    ),
]


@mark.parametrize('message, expected', tests)
def test_decode(message: str, expected: str) -> None:
    assert decode(message) == expected


if __name__ == '__main__':
    message, expected = tests[0]
    print(decode(message))


# from pathlib import Path


# def get_key() -> str:
#     challenges_dir = Path('challenges')
#     filenames = [
#         (int(file.name[:3]), next(filter(str.isalpha, file.name[4:])))
#         for file in challenges_dir.iterdir()
#         if file.name[:3].isnumeric() and int(file.name[:3]) % 25 == 0
#     ]

#     filenames.sort()

#     return ''.join(char.upper() for _, char in filenames)

# KEY = get_key()
