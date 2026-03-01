# Daily Coding challenge #48 (2025-09-27) - freeCodeCamp.org
# Spam Detector
# Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents
# a digit as follows:

# A represents the country code and can be any number of digits.
# BBB represents the area code and will always be three digits.
# CCC and DDDD represent the local number and will always be three and four digits
# long, respectively.
# Determine if it's a spam number based on the following criteria:

# The country code is greater than 2 digits long or doesn't begin with a zero (0).
# The area code is greater than 900 or less than 200.
# The sum of first three digits of the local number appears within last four digits of
# the local number.
# The number has the same digit four or more times in a row (ignoring the formatting
# characters).
from pytest import mark


def is_spam(number: str) -> bool:
    MIN_AREA_CODE = 200
    MAX_AREA_CODE = 900
    CONSECUTIVE_SPAM_DIGITS = 4

    cleaned_number = number.translate(str.maketrans('+()', '   ')).replace('-', '')

    digits_only = ''.join(c for c in cleaned_number if c.isdigit())

    for i in range(len(digits_only) - CONSECUTIVE_SPAM_DIGITS + 1):
        if len(set(digits_only[i : i + CONSECUTIVE_SPAM_DIGITS])) == 1:
            return True

    country, area, local = cleaned_number.split()

    SPAM_RULES = [
        lambda: len(country) > 2,
        lambda: country[0] != '0',
        lambda: int(area) < MIN_AREA_CODE,
        lambda: int(area) > MAX_AREA_CODE,
        lambda: str(sum(int(num) for num in (local[0:3]))) in local[-4:],
    ]

    # any() returns False if all rules are False, True if any rule is True
    return any(rule() for rule in SPAM_RULES)


tests = [
    ('+0 (200) 234-0182', False),
    ('+091 (555) 309-1922', True),
    ('+1 (555) 435-4792', True),
    ('+0 (955) 234-4364', True),
    ('+0 (155) 131-6943', True),
    ('+0 (555) 135-0192', True),
    ('+0 (555) 564-1987', True),
    ('+00 (555) 234-0182', False),
]


@mark.parametrize('number, expected', tests)
def test_is_spam(number: str, expected: bool) -> None:
    assert is_spam(number) == expected


if __name__ == '__main__':
    number, expected = tests[6]
    print(is_spam(number))
