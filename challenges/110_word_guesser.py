# Daily Coding challenge #110 (2025-11-28) - freeCodeCamp.org
# Word Guesser
# Given two strings of the same length, a secret word and a guess, compare the guess to
# the secret word using the following rules:

# The secret word and guess will only consist of uppercase letters ("A" to "Z");
# For each letter in the guess, replace it with a number according to how it matches the
# secret word:
# "2" if the letter is in the secret word and in the correct position.
# "1" if the letter is in the secret word but in the wrong position.
# "0" if the letter is not in the secret word.
# Each letter in the secret word can be used at most once.
# Exact matches ("2") are assigned first, then partial matches ("1") are assigned from
# left to right for remaining letters.
# If a letter occurs multiple times in the guess, it can only match as many times as it
# appears in the secret word.
# For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":

# The first "P" is not in the correct location ("1"), the "O" isn't in the secret word
# ("0"), the second "P" is in
# the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in
# the secret word have been used,
# and the "A" is not in the correct location ("1").
from collections import Counter

from pytest import mark


def compare(word: str, guess: str) -> str:
    """
    Compare a guess against a secret word using Wordle-like rules.

    Returns a string where:
    - '2' = correct letter in correct position
    - '1' = correct letter in wrong position
    - '0' = letter not in word
    """
    # Initialize result with all zeros
    result = ['0'] * len(guess)

    # Count available letters in the secret word
    available = Counter(word)

    # Pass 1: Find exact matches (same letter, same position)
    for i in range(len(guess)):
        if guess[i] == word[i]:
            result[i] = '2'
            available[guess[i]] -= 1  # Mark this letter as used

    # Pass 2: Find partial matches (correct letter, wrong position)
    for i in range(len(guess)):
        if result[i] == '0' and available[guess[i]] > 0:
            result[i] = '1'
            available[guess[i]] -= 1  # Mark this letter as used

    return ''.join(result)


tests = [
    ('APPLE', 'POPPA', '10201'),
    ('REACT', 'TRACE', '11221'),
    ('DEBUGS', 'PYTHON', '000000'),
    ('JAVASCRIPT', 'TYPESCRIPT', '0000222222'),
    ('ORANGE', 'ROUNDS', '110200'),
    ('WIRELESS', 'ETHERNET', '10021000'),
]


@mark.parametrize(('word', 'guess', 'expected'), tests)
def test_compare(word: str, guess: str, expected: str) -> None:
    assert compare(word, guess) == expected


if __name__ == '__main__':
    word, guess, expected = tests[0]
    print(compare(word, guess))
