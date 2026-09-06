"""Daily Coding Challenge #26 (2025-09-05) - freeCodeCamp.org."""

# IPv4 Validator
# Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists
# of four integer numbers separated by dots (.). Each number must satisfy the following
# conditions:
#
# - It is between 0 and 255 inclusive.
# - It does not have leading zeros (e.g. 0 is allowed, 01 is not).
# - Only numeric characters are allowed.
from pytest import mark

IPV4_NUM_OCTETS = 4
IPV4_MAX_OCTET_VALUE = 255


def is_valid_ipv4(ipv4: str) -> bool:
    """Determine if a string is a valid IPv4 address.

    Args:
        ipv4: A string representing an IPv4 address.

    Returns:
        True if the string is a valid IPv4 address, False otherwise.
    """
    octets = ipv4.split('.')
    if len(octets) != IPV4_NUM_OCTETS:
        return False
    return all(_is_valid_octet(octet) for octet in octets)


def _is_valid_octet(octet: str) -> bool:
    """Check whether a single dot-separated component is a valid IPv4 octet.

    Args:
        octet: A string representing a single octet of an IPv4 address.

    Returns:
        True if the octet is valid, False otherwise.
    """
    if not octet.isdecimal():
        return False
    if len(octet) > 1 and octet[0] == '0':
        return False
    return int(octet) <= IPV4_MAX_OCTET_VALUE


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
def test_is_valid_ipv4(ipv4: str, expected: bool) -> None:
    """Test is_valid_ipv4 function."""
    assert is_valid_ipv4(ipv4) == expected


if __name__ == '__main__':
    ipv4, expected = tests[0]
    print(is_valid_ipv4(ipv4))
