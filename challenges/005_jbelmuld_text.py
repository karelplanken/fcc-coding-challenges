# Daily Coding challenge #5 (2025-08-15) - freeCodeCamp.org
# Jbelmud Text
# Given a string, return a jumbled version of that string where each word is
# transformed using the following constraints:

# The first and last letters of the words remain in place
# All letters between the first and last letter are sorted alphabetically.
# The input strings will contain no punctuation, and will be entirely lowercase.
from pytest import mark


def jbelmu(text: str) -> str:
    jumbled_words = []
    for word in text.split():
        if len(word) > 3:
            jumbled_words.append(word[0] + ''.join(sorted(word[1:-1])) + word[-1])
        else:
            jumbled_words.append(word)

    return ' '.join(jumbled_words)


# Refactor: Using a nested function and list comprehension
# def jbelmu(text: str) -> str:
#     def jumble_word(word: str) -> str:
#         return (
#             word if len(word) <= 3 else
#             word[0] + ''.join(sorted(word[1:-1])) + word[-1]
#         )

#     return ' '.join(jumble_word(word) for word in text.split())


tests = [
    ('hello world', 'hello wlord'),
    ('i love jumbled text', 'i love jbelmud text'),
    (
        'freecodecamp is my favorite place to learn to code',
        'faccdeeemorp is my faiortve pacle to laern to cdoe',
    ),
    (
        'the quick brown fox jumps over the lazy dog',
        'the qciuk borwn fox jmpus oevr the lazy dog',
    ),
]


@mark.parametrize('text, expected', tests)
def test_jbelmu(text: str, expected: str) -> None:
    assert jbelmu(text) == expected


if __name__ == '__main__':
    text, expected = tests[0]
    print(jbelmu(text))
