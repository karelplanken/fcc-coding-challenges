# Daily Coding challenge #29 (2025-09-08) - freeCodeCamp.org
# Acronym Builder
# Given a string containing of one or more words, return an acronym of the words using
# the following constraints:

# The acronym should consist of the first letter of each word capitalized, unless
# otherwise noted.
# The acronym should ignore the first letter of these words unless they are the first
# word of the given string: a, for, an, and, by, and of.
# The acronym letters should be returned in the order they are given.
# The acronym should not contain any spaces.
from pytest import mark


def build_acronym(s: str) -> str:
    IGNORE = {'a', 'for', 'an', 'and', 'by', 'of'}

    words = s.split()

    return words[0][0].upper() + ''.join(
        word[0].upper() for word in words[1:] if word.lower() not in IGNORE
    )


tests = [
    ('Search Engine Optimization', 'SEO'),
    ('Frequently Asked Questions', 'FAQ'),
    ('National Aeronautics and Space Administration', 'NASA'),
    ('Federal Bureau of Investigation', 'FBI'),
    ('For your information', 'FYI'),
    ('By the way', 'BTW'),
    (
        'An unstoppable herd of waddling penguins overtakes the icy '
        + 'mountains and sings happily',
        'AUHWPOTIMSH',
    ),
]


@mark.parametrize('s, expected', tests)
def test_build_acronym(s: str, expected: str) -> None:
    assert build_acronym(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(build_acronym(s))
