"""Daily Coding Challenge #355 (2026-07-31) - freeCodeCamp.org."""

# Morse Code
# Given a Morse code string, return the decoded message using the following table:
#
# | Code | Letter | Code | Letter |
# |------|--------|------|--------|
# | .-   | A      | -.   | N      |
# | -... | B      | ---  | O      |
# | -.-. | C      | .--. | P      |
# | -..  | D      | --.- | Q      |
# | .    | E      | .-.  | R      |
# | ..-. | F      | ...  | S      |
# | --.  | G      | -    | T      |
# | .... | H      | ..-  | U      |
# | ..   | I      | ...- | V      |
# | .--- | J      | .--  | W      |
# | -.-  | K      | -..- | X      |
# | .-.. | L      | -.-- | Y      |
# | --   | M      | --.. | Z      |
#
# - Letters are separated by a single space
# - Words are separated by three spaces
from pytest import mark

MORSE_TABLE = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
}

WORD_SEPARATOR = '   '
LETTER_SEPARATOR = ' '


def decode_word(word: str) -> str:
    """Decodes a single space-separated Morse word into letters.
    
    Raises:
        KeyError: If an invalid Morse code token is encountered.
    """
    return ''.join(MORSE_TABLE[token] for token in word.split(LETTER_SEPARATOR))


def decode_morse(code: str) -> str:
    """Translates a Morse code string into a readable message.

    See MORSE_TABLE, WORD_SEPARATOR, LETTER_SEPARATOR for the encoding rules.

    Args:
        code: Morse code, letters separated by one space, words by three.

    Returns:
        The decoded message.
    """
    return ' '.join(decode_word(word) for word in code.split(WORD_SEPARATOR))


tests = [
    ('--..', 'Z'),
    ('... --- ...', 'SOS'),
    ('..-. .-. . . -.-. --- -.. . -.-. .- -- .--.', 'FREECODECAMP'),
    ('.... . .-.. .-.. ---   .-- --- .-. .-.. -..', 'HELLO WORLD'),
    (
        '- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   '
        '.--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   '
        '-.. --- --.',
        'THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG',
    ),
]


@mark.parametrize('code, expected', tests)
def test_decode_morse(code: str, expected: str) -> None:
    """Test decode_morse function."""
    assert decode_morse(code) == expected


if __name__ == '__main__':
    code, expected = tests[0]
    print(decode_morse(code))
