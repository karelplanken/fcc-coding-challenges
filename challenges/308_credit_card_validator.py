# Daily Coding challenge #308 (2026-06-14) - freeCodeCamp.org
# Credit Card Validator
# Given a string of digits for a credit card number, determine if it's a valid card
# number using the following method:

# Starting from the second-to-last digit, double every other digit moving left.
# If doubling a digit results in a number greater than 9, subtract 9.
# Sum all the digits (doubled and undoubled).
# If the total is divisible by 10, the number is valid.
from pytest import mark


def is_valid_card(number: str) -> bool:
    def luhn_digit(idx: int, char: str) -> int:
        d = int(char) * (idx % 2 + 1)
        return d - 9 if d > 9 else d

    return (
        sum(luhn_digit(idx, char) for idx, char in enumerate(reversed(number))) % 10
        == 0
    )


tests = [
    ('4532015112830366', True),
    ('5425233430109903', True),
    ('371449635398431', True),
    ('6011111111111117', True),
    ('4532015112830367', False),
    ('1234567890123456', False),
    ('4532015112830368', False),
]


@mark.parametrize('number, expected', tests)
def test_is_valid_card(number: str, expected: bool) -> None:
    assert is_valid_card(number) == expected


if __name__ == '__main__':
    number, expected = tests[0]
    print(is_valid_card(number))
