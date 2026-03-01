# Daily Coding challenge #26 (2025-09-05) - freeCodeCamp.org
# IPv4 Validator
# Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address
# consists of four integer numbers separated by dots (.). Each number must satisfy
# the following conditions:

# It is between 0 and 255 inclusive.
# It does not have leading zeros (e.g. 0 is allowed, 01 is not).
# Only numeric characters are allowed.
from pytest import mark


def is_valid_ipv4(ipv4: str) -> bool:
    parts = ipv4.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part or not part.isdigit():
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        num = int(part)
        if num > 255:
            return False
    return True


tests = [
    ('192.168.1.1', True),
    ('0.0.0.0', True),
    ('255.01.50.111', False),
    ('255.00.50.111', False),
    ('256.101.50.115', False),
    ('192.168.101.', False),
    ('192168145213', False),
]


@mark.parametrize('ipv4, expected', tests)
def test_is_valid_ipv4(ipv4: str, expected: str) -> None:
    assert is_valid_ipv4(ipv4) == expected


if __name__ == '__main__':
    ipv4, expected = tests[0]
    print(is_valid_ipv4(ipv4))
