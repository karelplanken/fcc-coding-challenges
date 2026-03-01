# Daily Coding challenge #80 (2025-10-29) - freeCodeCamp.org
# Email Sorter
# On October 29, 1971, the first email ever was sent, introducing the username@domain
# format we still use. Now, there are billions of email addresses.

# In this challenge, you are given a list of email addresses and need to sort them
# alphabetically by domain name first (the part after the @), and username second
# (the part before the @).

# Sorting should be case-insensitive.
# If more than one email has the same domain, sort them by their username.
# Return an array of the sorted addresses.
# Returned addresses should retain their original case.
# For example, given ["jill@mail.com", "john@example.com", "jane@example.com"],
# return ["jane@example.com", "john@example.com", "jill@mail.com"].
from pytest import mark


# Most readable, clear intent, and concise version using reversed tuple:
def sort(emails: list[str]) -> list[str]:
    return sorted(emails, key=lambda email: tuple(reversed(email.lower().split('@'))))
    # Copilot's solution, which I don't really like since 0 and 1 are magic numbers:


# def sort(emails: list[str]) -> list[str]:
#     return sorted(
#         emails,
#         key=lambda email: (email.split('@')[1].lower(), email.split('@')[0].lower()),
#     )


# Most readable version using a helper function:
# def sort(emails: list[str]) -> list[str]:
#     def sort_key(email: str) -> tuple[str, str]:
#         username, domain = email.lower().split('@')
#         return (domain, username)

#     return sorted(emails, key=sort_key)


# One-liner using slicing:
# def sort(emails: list[str]) -> list[str]:
#     return sorted(emails, key=lambda e: e.lower().split('@')[::-1])


tests = [
    (
        ['jill@mail.com', 'john@example.com', 'jane@example.com'],
        ['jane@example.com', 'john@example.com', 'jill@mail.com'],
    ),
    (
        ['bob@mail.com', 'alice@zoo.com', 'carol@mail.com'],
        ['bob@mail.com', 'carol@mail.com', 'alice@zoo.com'],
    ),
    (
        ['user@z.com', 'user@y.com', 'user@x.com'],
        ['user@x.com', 'user@y.com', 'user@z.com'],
    ),
    (
        ['sam@MAIL.com', 'amy@mail.COM', 'bob@Mail.com'],
        ['amy@mail.COM', 'bob@Mail.com', 'sam@MAIL.com'],
    ),
    (
        [
            'simon@beta.com',
            'sammy@alpha.com',
            'Sarah@Alpha.com',
            'SAM@ALPHA.com',
            'Simone@Beta.com',
            'sara@alpha.com',
        ],
        [
            'SAM@ALPHA.com',
            'sammy@alpha.com',
            'sara@alpha.com',
            'Sarah@Alpha.com',
            'simon@beta.com',
            'Simone@Beta.com',
        ],
    ),
]


@mark.parametrize('emails, expected', tests)
def test_sort(emails: list[str], expected: list[str]) -> None:
    assert sort(emails) == expected


if __name__ == '__main__':
    emails, expected = tests[0]
    print(sort(emails))
