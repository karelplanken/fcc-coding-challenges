# Daily Coding challenge #288 (2026-05-25) - freeCodeCamp.org
# Secret Number
# Given a secret number and a guess, determine if the guess is correct.
# Return:
# "higher" if the secret number is higher than the guess.
# "lower" if the secret number is lower than the guess.
# "you got it!" if the guess is correct.
from pytest import mark


def guess_number(secret: int, guess: int) -> str:
    if guess == secret:
        return 'you got it!'

    return 'higher' if guess < secret else 'lower'


tests = [
    (50, 30, 'higher'),
    (85, 99, 'lower'),
    (2026, 2026, 'you got it!'),
    (92904, 11283, 'higher'),
    (230495, 423920, 'lower'),
    (120349, 120349, 'you got it!'),
]


@mark.parametrize('secret, guess, expected', tests)
def test_guess_number(secret: int, guess: int, expected: str) -> None:
    assert guess_number(secret, guess) == expected


if __name__ == '__main__':
    secret, guess, expected = tests[0]
    print(guess_number(secret, guess))
