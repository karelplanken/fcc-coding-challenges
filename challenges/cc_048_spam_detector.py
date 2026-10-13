"""Daily Coding Challenge #48 (2025-09-27) - freeCodeCamp.org."""

# Spam Detector
# Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a
# digit as follows:
#
# - A represents the country code and can be any number of digits.
# - BBB represents the area code and will always be three digits.
# - CCC and DDDD represent the prefix number and will always be three and four digits
#   long, respectively.
#
# Determine if it's a spam number based on the following criteria:
#
# - The country code is greater than 2 digits long or doesn't begin with a zero (0).
# - The area code is greater than 900 or less than 200.
# - The sum of first three digits of the prefix number appears within last four digits
#   of the prefix number.
# - The number has the same digit four or more times in a row (ignoring the formatting
#   characters).
import re
from collections.abc import Callable
from dataclasses import dataclass
from itertools import groupby
from typing import Self

from pytest import mark

_MAX_LENGTH_COUNTRY_CODE = 2
_MIN_AREA_CODE = 200
_MAX_AREA_CODE = 900
_CONSECUTIVE_SPAM_DIGITS = 4
_PHONE_PATTERN = re.compile(
    r'\+(?P<country>\d+) \((?P<area>\d{3})\) (?P<prefix>\d{3})-(?P<line>\d{4})',
    re.ASCII,
)


@dataclass(frozen=True, slots=True)
class Phone:
    """A phone number in the format "+A (BBB) CCC-DDDD".

    Attributes:
        country: The country code.
        area: The area code.
        prefix: First three digits of the local number.
        line: Last four digits of the local number.
    """

    country: str
    area: str
    prefix: str
    line: str

    @classmethod
    def parse(cls, number: str) -> Self:
        """Parse a phone number string into a Phone object.

        Args:
            number: A phone number in the format "+A (BBB) CCC-DDDD".

        Returns:
            A Phone object representing the parsed phone number.

        Raises:
            ValueError: If the phone number does not match the expected format.
        """
        match = _PHONE_PATTERN.fullmatch(number)
        if match is None:
            msg = 'phone number must have format "+A (BBB) CCC-DDDD"'
            raise ValueError(msg)
        return cls(**match.groupdict())

    @property
    def digits(self) -> str:
        """The digits of the phone number as a single string."""
        return self.country + self.area + self.prefix + self.line


def _longest_run(s: str) -> int:
    return max(len(list(group)) for _, group in groupby(s))


# Each rule is named so the triggering reason can be reported (see _spam_reason)
# and new rules can be added without touching the evaluation logic. Order
# matters: evaluation stops at the first rule that matches.
_RULES: tuple[tuple[str, Callable[[Phone], bool]], ...] = (
    (
        'country code',
        lambda p: (
            len(p.country) > _MAX_LENGTH_COUNTRY_CODE or not p.country.startswith('0')
        ),
    ),
    ('area code', lambda p: not (_MIN_AREA_CODE <= int(p.area) <= _MAX_AREA_CODE)),
    ('digit sum', lambda p: str(sum(map(int, p.prefix))) in p.line),
    ('repeated digits', lambda p: _longest_run(p.digits) >= _CONSECUTIVE_SPAM_DIGITS),
)


def _spam_reason(number: str) -> str | None:
    phone = Phone.parse(number)
    return next((name for name, rule in _RULES if rule(phone)), None)


def is_spam(number: str) -> bool:
    """Determine if a phone number is spam based on the given criteria.

    Args:
        number: A phone number in the format "+A (BBB) CCC-DDDD". Other
            formats raise ValueError.

    Returns:
        True if the number is spam, False otherwise.
    """
    return _spam_reason(number) is not None


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
    """Test is_spam function."""
    assert is_spam(number) == expected


if __name__ == '__main__':
    number, expected = tests[0]
    print(is_spam(number))
