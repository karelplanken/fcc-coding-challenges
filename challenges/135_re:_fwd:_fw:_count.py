# Daily Coding challenge #135 (2025-12-23) - freeCodeCamp.org
# Re: Fwd: Fw: Count
# Given a string representing the subject line of an email, determine how many times
# the email has been forwarded or replied to.

# For simplicity, consider an email forwarded or replied to if the string contains any
# of the following markers (case-insensitive):

# "fw:"
# "fwd:"
# "re:"
# Return the total number of occurrences of these markers.
import re

from pytest import mark


def email_chain_count(subject: str) -> int:
    """Count fw:, fwd:, and re: markers (case-insensitive)."""
    pattern = r'fw:|fwd:|re:'
    print(re.findall(pattern, subject, flags=re.I))
    return len(re.findall(pattern, subject, flags=re.I))


# def email_chain_count(subject: str) -> int:
#     """Count occurrences of fw:, fwd:, and re: markers (case-insensitive)."""
#     subject_lower = subject.lower()
#     return (
#         subject_lower.count('fw:')
#         + subject_lower.count('fwd:')
#         + subject_lower.count('re:')
#     )


tests = [
    ('Re: Meeting Notes', 1),
    ('Meeting Notes', 0),
    ('Re: re: RE: rE: Meeting Notes', 4),
    ('Re: Fwd: Re: Fw: Re: Meeting Notes', 5),
    (
        're:Ref:fw:re:review:FW:Re:fw:report:Re:FW:followup:re:summary:Fwd:Re:fw:NextStep:RE:FW:re:Project:Fwd:Re:fw:Notes:RE:re:Update:FWD:Re:fw:Summary',
        23,
    ),
]


@mark.parametrize('subject, expected', tests)
def test_email_chain_count(subject: str, expected: int) -> None:
    assert email_chain_count(subject) == expected


if __name__ == '__main__':
    subject, expected = tests[2]
    print(email_chain_count(subject))
