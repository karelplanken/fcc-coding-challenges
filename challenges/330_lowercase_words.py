# Daily Coding challenge #330 (2026-07-06) - freeCodeCamp.org
# lowercase words
# Given a string, return only the words that are entirely lowercase, in their original
# order and with a space between each word.
from pytest import mark


def get_lowercase_words(s: str) -> str:
    return " ".join(word for word in s.split() if word.islower())


tests = [
    ("hello GOOD world", "hello world"),
    ("these are all lowercase", "these are all lowercase"),
    ("less is NoT more", "less is more"),
    ("DonT eat pizza every OTHER day", "eat pizza every day"),
    (
        "the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the "
        + "lazy SloW dog",
        "the quick brown fox jumped over the lazy dog",
    ),
]


@mark.parametrize("s, expected", tests)
def test_get_lowercase_words(s: str, expected: str) -> None:
    assert get_lowercase_words(s) == expected


if __name__ == "__main__":
    s, expected = tests[0]
    print(get_lowercase_words(s))
