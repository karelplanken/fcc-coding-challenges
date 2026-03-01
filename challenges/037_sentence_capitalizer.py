# Daily Coding challenge #37 (2025-09-16) - freeCodeCamp.org
# Sentence Capitalizer
# Given a paragraph, return a new paragraph where the first letter of each sentence is
# capitalized.

# All other characters should be preserved.
# Sentences can end with a period (.), one or more question marks (?), or one or more
# exclamation points (!).
from pytest import mark


def capitalize(paragraph: str) -> str:
    if not paragraph:
        return paragraph

    ENDING = '.!?'
    result = []
    cap_next = True  # Capitalize first letter

    for char in paragraph:
        if cap_next and char.isalpha():
            result.append(char.upper())
            cap_next = False
        else:
            result.append(char)
            if char in ENDING:
                cap_next = True

    return ''.join(result)


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
    assert capitalize(paragraph) == expected


if __name__ == '__main__':
    paragraph, expected = tests[0]
    capitalize(paragraph)
