# Daily Coding challenge #15 (2025-08-25) - freeCodeCamp.org
# camelCase
# Given a string, return its camel case version using the following rules:

# Words in the string argument are separated by one or more characters from the
# following set: space ( ), dash (-), or underscore (_). Treat any sequence of these
# as a word break.
# The first word should be all lowercase.
# Each subsequent word should start with an uppercase letter, with the rest of it
# lowercase.
# All spaces and separators should be removed.
from pytest import mark

# def to_camel_case(s: str) -> str:
#     # # More verbose and maybe more readable for beginners
#     # words = (s.replace('_', ' ').replace('-', ' ').split())

#     # camel_cased = words[0].lower()
#     # for word in words[1:]:
#     #     camel_cased += word.title()
#     # return camel_cased
#     # This is the oneliner
#     return ''.join(
#         word.lower() if i == 0 else word.title()
#         for i, word in enumerate(s.replace('_', ' ').replace('-', ' ').split())
#     )


# Most readable
def to_camel_case(s: str) -> str:
    words = s.replace('_', ' ').replace('-', ' ').split()
    if not words:
        return ''
    return words[0].lower() + ''.join(word.title() for word in words[1:])


# Unpacking (Pythonic one-liner)
# def to_camel_case(s: str) -> str:
#     words = s.replace('_', ' ').replace('-', ' ').split()
#     return words[0].lower() + \
#         ''.join(word.title() for word in words[1:]) if words else ''


tests = [
    ('hello world', 'helloWorld'),
    ('HELLO WORLD', 'helloWorld'),
    ('secret agent-X', 'secretAgentX'),
    ('FREE cODE cAMP', 'freeCodeCamp'),
    (
        'ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and \
            a_parrot_ _named- _squawk',
        'yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk',
    ),
]


@mark.parametrize('s, expected', tests)
def test_to_camel_case(s: str, expected: str) -> None:
    assert to_camel_case(s) == expected


if __name__ == '__main__':
    s, expected = tests[0]
    print(to_camel_case(s))
