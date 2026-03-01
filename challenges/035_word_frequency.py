# Daily Coding challenge #35 (2025-09-14) - freeCodeCamp.org
# Word Frequency
# Given a paragraph, return an array of the three most frequently occurring words.

# Words in the paragraph will be separated by spaces.
# Ignore case in the given paragraph. For example, treat Hello and hello as the same
# word.
# Ignore punctuation in the given paragraph. Punctuation consists of commas (,),
# periods (.), and exclamation points (!).
# The returned array should have all lowercase words.
# The returned array should be in descending order with the most frequently occurring
# word first.
from collections import Counter

from pytest import mark


def get_words(paragraph: str) -> list[str]:
    clean_text = paragraph.translate(str.maketrans('', '', ',.!'))
    words = [word.lower() for word in clean_text.split() if word]

    return [word for word, _ in Counter(words).most_common(3)]


# # Alternatives for the maketrans and translate approach:
# # Option 1: List comprehension (very explicit)
# clean_text = ''.join(char for char in paragraph if char not in ',.!')

# # Option 2: Regular expressions (powerful but overkill for this)
# import re

# clean_text = re.sub(r'[,.!]', '', paragraph)

# # Option 3: Chained replace (readable but slower)
# clean_text = paragraph.replace(',', '').replace('.', '').replace('!', '')


# # Option 4: Using a simple helper function
# def remove_chars(text, chars):
#     return text.translate(str.maketrans('', '', chars))


# clean_text = remove_chars(paragraph, ',.!')  # More readable!

tests = [
    (
        'Coding in Python is fun because coding Python allows for coding '
        + 'in Python easily while coding',
        ['coding', 'python', 'in'],
    ),
    ('I like coding. I like testing. I love debugging!', ['i', 'like', 'coding']),
    (
        'Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!',
        ['debug', 'test', 'deploy'],
    ),
]


@mark.parametrize('paragraph, expected', tests)
def test_get_words(paragraph: str, expected: list[str]) -> None:
    assert get_words(paragraph) == expected


if __name__ == '__main__':
    paragraph, expected = tests[0]
    get_words(paragraph)
