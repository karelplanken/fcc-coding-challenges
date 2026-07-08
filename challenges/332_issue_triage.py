# Daily Coding challenge #332 (2026-07-08) - freeCodeCamp.org
# Issue Triage
# Given a number of milliseconds since the last post on an issue, and the last message
# posted on the issue, determine what you should do with the issue according to these
# rules:
#
# - If the last message is less than 7 days ago, return "leave it"
# - If the last message is 7 or more days ago and its content contains "bump"
#   (case-insensitive), return "close it"
# - Otherwise, return "bump it"
from datetime import timedelta

from pytest import mark

SEVEN_DAY_THRESHOLD = timedelta(days=7)

def triage_issue(ms: int, message: str) -> str:
    elapsed = timedelta(milliseconds=ms)
    if elapsed < SEVEN_DAY_THRESHOLD:
        return 'leave it'
    return 'close it' if 'bump' in message.lower() else 'bump it'


tests = [
    (86400000, 'Lets fix it', 'leave it'),
    (1209600000, 'still waiting', 'bump it'),
    (864000000, 'bump', 'close it'),
    (604800000, 'Do we still want this?', 'bump it'),
    (604800000, 'Bumping this', 'close it'),
    (345600000, "I'll make a PR", 'leave it'),
]


@mark.parametrize('ms, message, expected', tests)
def test_triage_issue(ms: int, message: str, expected: str) -> None:
    assert triage_issue(ms, message) == expected


if __name__ == '__main__':
    ms, message, expected = tests[5]
    print(triage_issue(ms, message))
