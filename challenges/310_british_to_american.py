# Daily Coding challenge #310 (2026-06-16) - freeCodeCamp.org
# British to American
# Given a sentence, convert any British English spellings to their American English
# equivalents using the following lookup table and return the updated sentence:

# British	American
# "colour"	"color"
# "flavour"	"flavor"
# "honour"	"honor"
# "neighbour"	"neighbor"
# "labour"	"labor"
# "humour"	"humor"
# "centre"	"center"
# "fibre"	"fiber"
# "defence"	"defense"
# "offence"	"offense"
# "organise"	"organize"
# "recognise"	"recognize"
# "analyse"	"analyze"
# Replacements should be case-insensitive. For example, "Colour" should become "Color".
# The input may contain words that build on the exact spelling of a root in the table
# that also need to be changed. For example, "colouring" should become "coloring", and
# "disorganised" should become "disorganized".
import re

from pytest import mark

BRITISH_TO_AMERICAN = {
    'colour': 'color',
    'flavour': 'flavor',
    'honour': 'honor',
    'neighbour': 'neighbor',
    'labour': 'labor',
    'humour': 'humor',
    'centre': 'center',
    'fibre': 'fiber',
    'defence': 'defense',
    'offence': 'offense',
    'organise': 'organize',
    'recognise': 'recognize',
    'analyse': 'analyze',
}

UK_TO_US_REGEX = {
    rf'({en_word[0]}){en_word[1:]}': rf'\1{us_word[1:]}'
    for en_word, us_word in BRITISH_TO_AMERICAN.items()
}


def british_to_american(sentence: str) -> str:
    for patt, repl in UK_TO_US_REGEX.items():
        sentence = re.sub(patt, repl, sentence, flags=re.IGNORECASE)
    return sentence


# Note: Test case 5 is inconsistent, i.e. "organisation" should be converted to
# "organization". The test case is kept as provided freeCodeCamp.org.
tests = [
    ('I love the colour blue.', 'I love the color blue.'),
    ('The fibre optic cable is new.', 'The fiber optic cable is new.'),
    (
        "It's an honour to meet someone with such humour.",
        "It's an honor to meet someone with such humor.",
    ),
    (
        'The unrecognised artist analysed his colour palette at the centre.',
        'The unrecognized artist analyzed his color palette at the center.',
    ),
    (
        'The offence analysed, with organisation, the defence centre and recognised '
        + 'that the neighbouring labouror was humourous, flavourful, and colourful.',
        'The offense analyzed, with organisation, the defense center and recognized '
        + 'that the neighboring laboror was humorous, flavorful, and colorful.',
    ),
]


@mark.parametrize('sentence, expected', tests)
def test_british_to_american(sentence: str, expected: str) -> None:
    assert british_to_american(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(british_to_american(sentence))
