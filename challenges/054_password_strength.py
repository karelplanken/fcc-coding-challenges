# Daily Coding challenge #54 (2025-10-03) - freeCodeCamp.org
# P@ssw0rd Str3ngth!
# Given a password string, return "weak", "medium", or "strong" based on the strength
# of the password.

# A password is evaluated according to the following rules:

# It is at least 8 characters long.
# It contains both uppercase and lowercase letters.
# It contains at least one number.
# It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
# Return "weak" if the password meets fewer than two of the rules. Return "medium" if
# the password meets 2 or 3 of the rules. Return "strong" if the password meets all
# 4 rules.
from pytest import mark

SPECIAL_CHARS = {'!', '@', '#', '$', '%', '^', '&', '*'}


def check_strength(password: str) -> str:
    PASSWORD_RULES = [
        lambda: len(password) >= 8,
        lambda: any(char.isupper() for char in password)
        and any(char.islower() for char in password),
        lambda: any(char.isdigit() for char in password),
        lambda: any(char in SPECIAL_CHARS for char in password),
    ]

    rules_met = sum(rule() for rule in PASSWORD_RULES)

    if rules_met == len(PASSWORD_RULES):
        return 'strong'
    return 'medium' if rules_met >= 2 else 'weak'


# Alternative solution using boolean flags:
# special_chars = {'!', '@', '#', '$', '%', '^', '&', '*'}


# def check_strength(password):
#     has_length = len(password) >= 8
#     has_both_cases = any(c.islower() for c in password) and any(
#         c.isupper() for c in password
#     )
#     has_digit = any(c.isdigit() for c in password)
#     has_special = any(c in special_chars for c in password)

#     score = sum([has_length, has_both_cases, has_digit, has_special])

#     if score == 4:
#         return 'strong'
#     elif score >= 2:
#         return 'medium'
#     else:
#         return 'weak'


# Solution using sets:
# import string

# digits = {digit for digit in string.digits}
# lower_chars = {lower_char for lower_char in string.ascii_lowercase}
# upper_chars = {upper_char for upper_char in string.ascii_uppercase}
# special_chars = {'!', '@', '#', '$', '%', '^', '&', '*'}


# def check_strength(password: str) -> str:
#     password_set = {char for char in password}
#     score = sum(
#         (
#             len(password) >= 8,
#             len(digits - password_set) < 10,
#             len(lower_chars - password_set) < 26
#             and len(upper_chars - password_set) < 26,
#             len(special_chars - password_set) < 8,
#         )
#     )
#     if score == 4:
#         return 'strong'
#     elif score >= 2:
#         return 'medium'
#     else:
#         return 'weak'

tests = [
    ('123456', 'weak'),
    ('pass!!!', 'weak'),
    ('Qwerty', 'weak'),
    ('PASSWORD', 'weak'),
    ('PASSWORD!', 'medium'),
    ('PassWord%^!', 'medium'),
    ('qwerty12345', 'medium'),
    ('S3cur3P@ssw0rd', 'strong'),
    ('C0d3&Fun!', 'strong'),
]


@mark.parametrize('password, expected', tests)
def test_check_strength(password: str, expected: str) -> None:
    assert check_strength(password) == expected


if __name__ == '__main__':
    password, expected = tests[7]
    print(check_strength(password))
