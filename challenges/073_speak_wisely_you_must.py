# Daily Coding challenge #73 (2025-10-22) - freeCodeCamp.org
# Speak Wisely, You Must
# Given a sentence, return a version of it that sounds like advice from a wise teacher
# using the following rules:

# Words are separated by a single space.
# Find the first occurrence of one of the following words in the sentence: "have",
# "must", "are", "will", "can".
# Move all words before and including that word to the end of the sentence and:
# Preserve the order of the words when you move them.
# Make them all lowercase.
# And add a comma and space before them.
# Capitalize the first letter of the new first word of the sentence.
# All given sentences will end with a single punctuation mark. Keep the original
# punctuation of the sentence and move it to the end of the new sentence.
# Return the new sentence, make sure there's a single space between each word and no
# spaces at the beginning or end of the sentence.
# For example, given "You must speak wisely." return "Speak wisely, you must."
from pytest import mark


def wise_speak(sentence: str) -> str:
    AUXILIARY_VERBS = ('have', 'must', 'are', 'will', 'can')

    punctuation = sentence[-1]
    words = sentence[:-1].split()

    # Find split point
    for i, word in enumerate(words):
        if word.lower() in AUXILIARY_VERBS:
            before, after = words[: i + 1], words[i + 1 :]
            after_part = ' '.join(after).capitalize()
            before_part = ' '.join(before).lower()
            return f'{after_part}, {before_part}{punctuation}'

    return sentence  # No auxiliary verb found


tests = [
    ('You must speak wisely.', 'Speak wisely, you must.'),
    ('You can do it!', 'Do it, you can!'),
    ('Do you think you will complete this?', 'Complete this, do you think you will?'),
    ('All your base are belong to us.', 'Belong to us, all your base are.'),
    ('You have much to learn.', 'Much to learn, you have.'),
]


@mark.parametrize('sentence, expected', tests)
def test_wise_speak(sentence: str, expected: str) -> None:
    assert wise_speak(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[0]
    print(wise_speak(sentence))
