"""Daily Coding Challenge #37 (2025-09-16) - freeCodeCamp.org."""

# Sentence Capitalizer
# Given a paragraph, return a new paragraph where the first letter of each sentence is
# capitalized.
#
# - All other characters should be preserved.
# - Sentences can end with a period (.), one or more question marks (?), or one or more
#   exclamation points (!).
from pytest import mark

_SENTENCE_ENDINGS = '.!?'


def capitalize(paragraph: str) -> str:
    """Capitalize the first letter of each sentence in a paragraph.

    Args:
        paragraph: A string representing the paragraph to be processed.

    Returns:
        A new string with the first letter of each sentence capitalized.
    """
    chars = list(paragraph)
    capitalize_next = True

    for i, char in enumerate(chars):
        if capitalize_next and char.isalpha():
            chars[i] = char.upper()
            capitalize_next = False
        elif char in _SENTENCE_ENDINGS:
            capitalize_next = True

    return ''.join(chars)


tests = [
    ('this is a simple sentence.', 'This is a simple sentence.'),
    ('hello world. how are you?', 'Hello world. How are you?'),
    (
        "i did today's coding challenge... it was fun!!",
        "I did today's coding challenge... It was fun!!",
    ),
    (
        'crazy!!!strange???unconventional...sentences.',
        'Crazy!!!Strange???Unconventional...Sentences.',
    ),
    (
        "there's a space before this period . "
        + 'why is there a space before that period ?',
        "There's a space before this period . "
        + 'Why is there a space before that period ?',
    ),
]


@mark.parametrize('paragraph, expected', tests)
def test_capitalize(paragraph: str, expected: str) -> None:
    """Test capitalize function."""
    assert capitalize(paragraph) == expected


if __name__ == '__main__':
    paragraph, expected = tests[1]
    print(capitalize(paragraph))
