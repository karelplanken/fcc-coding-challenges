# Daily Coding challenge #176 (2026-02-02) - freeCodeCamp.org
# Groundhog Day
# Today is Groundhog Day, in which a groundhog predicts the weather based on whether or
# not it sees its shadow.

# Given a value representing the groundhog's appearance, return the correct prediction:

# If the given value is the boolean true (the groundhog saw its shadow), return "Looks
# like we'll have six more weeks of winter.".
# If the value is the boolean false (the groundhog did not see its shadow), return
# "It's going to be an early spring.".
# If the value is anything else (the groundhog did not show up), return "No prediction
# this year.".
from pytest import mark


def groundhog_day_prediction(appearance: bool) -> str:
    if not isinstance(appearance, bool):
        return 'No prediction this year.'

    return (
        "Looks like we'll have six more weeks of winter."
        if appearance
        else "It's going to be an early spring."
    )


tests = [
    (True, "Looks like we'll have six more weeks of winter."),
    (False, "It's going to be an early spring."),
    (None, 'No prediction this year.'),
    (' ', 'No prediction this year.'),
    ('True', 'No prediction this year.'),
]


@mark.parametrize('appearance, expected', tests)
def test_groundhog_day_prediction(appearance: bool, expected: str) -> None:
    assert groundhog_day_prediction(appearance) == expected


if __name__ == '__main__':
    appearances, expected = tests[0]
    print(groundhog_day_prediction(appearances))
