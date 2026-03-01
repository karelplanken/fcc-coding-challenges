# Daily Coding challenge #67 (2025-10-16) - freeCodeCamp.org
# Email Validator
# Given a string, determine if it is a valid email address using the following
# constraints:

# It must contain exactly one @ symbol.
# The local part (before the @):
# Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or
# hyphens (-).
# Cannot start or end with a dot.
# The domain part (after the @):
# Must contain at least one dot.
# Must end with a dot followed by at least two letters.
# Neither the local or domain part can have two dots in a row.
# import email

from pytest import mark

# Split the email into local and domain parts and validate each part:
# import re
# def validate(email: str) -> bool:
#     # Must have exactly one @ symbol
#     if email.count('@') != 1:
#         return False

#     local, domain = email.split('@')

#     # Check local part
#     if not local or local[0] == '.' or local[-1] == '.':
#         return False

#     if '..' in local:
#         return False

#     if not re.match(r'^[a-zA-Z0-9._-]+$', local):
#         return False

#     # Check domain part
#     if not domain or '..' in domain:
#         return False

#     if '.' not in domain:
#         return False

#     # Domain must end with dot followed by 2+ letters
#     if not re.search(r'\.[a-zA-Z]{2,}$', domain):
#         return False

#     return True


# Lambda constraints list and no regex usage.
#  This solution uses a strategy pattern using lambdas to encapsulate each validation 
# rule. This makes it easy to add, remove, or modify validation rules without changing 
# the overall structure of the code.
# The approach can be described as:
# 1) Predicate list - since each lambda is a predicate (function returning a boolean)
# 2) Rule-based validation - where each rule is encapsulated as a function
# 3) Constraint checking pattern - emphasizing the validation aspect
def validate(e_mail: str) -> bool:
    ALLOWED_SPECIAL_CHARS = {'.', '_', '-'}
    EMAIL_CONSTRAINTS = [
        lambda: e_mail.count('@') == 1,
        lambda: all(
            char.isalpha() or char.isdigit() or char in ALLOWED_SPECIAL_CHARS
            for char in e_mail[: e_mail.index('@')]
        ),
        lambda: e_mail[e_mail.index('@') - 1] != '.',
        lambda: e_mail[0] != '.',
        lambda: '.' in e_mail[e_mail.index('@') :],
        lambda: len(e_mail[e_mail.rindex('.') + 1 :]) >= 2,
        lambda: all(char.isalpha() for char in e_mail[e_mail.rindex('.') + 1 :]),
        lambda: '..' not in e_mail,
    ]
    return all(constraint() for constraint in EMAIL_CONSTRAINTS)


tests = [
    ('a@b.cd', True),
    ('hell.-w.rld@example.com', True),
    ('.b@sh.rc', False),
    ('example@test.c0', False),
    ('freecodecamp.org', False),
    ('develop.ment_user@c0D!NG.R.CKS', True),
    ('hello.@wo.rld', False),
    ('hello@world..com', False),
    ('develop..ment_user@c0D!NG.R.CKS', False),
    ('git@commit@push.io', False),
]


@mark.parametrize('e_mail, expected', tests)
def test_validate(e_mail: str, expected: bool) -> None:
    assert validate(e_mail) == expected


if __name__ == '__main__':
    e_mail, expected = tests[4]
    print(validate(e_mail))
