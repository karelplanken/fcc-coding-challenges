"""Daily Coding Challenge #62 (2025-10-11) - freeCodeCamp.org."""

# Hex to Decimal
# Given a string representing a hexadecimal number (base 16), return its decimal (base
# 10) value as an integer.
#
# Hexadecimal is a number system that uses 16 digits:
#
# - 0-9 represent values 0 through 9.
# - A-F represent values 10 through 15.
#
# Here's a partial conversion table:
#
# | Hexadecimal | Decimal |
# |:-----------:|:-------:|
# | 0           | 0       |
# | 1           | 1       |
# | ...         | ...     |
# | 9           | 9       |
# | A           | 10      |
# | ...         | ...     |
# | F           | 15      |
# | 10          | 16      |
# | ...         | ...     |
# | 9F          | 159     |
# | A0          | 160     |
# | ...         | ...     |
# | FF          | 255     |
# | 100         | 256     |
#
# - The string will only contain characters 0–9 and A–F.
from types import MappingProxyType

from pytest import mark

_HEX_TO_DEC = MappingProxyType({c: v for v, c in enumerate('0123456789ABCDEF')})


# Production note: prefer the built-in `int(hex_str, 16)`.
# - It is implemented in C, so there is no per-character interpreter overhead.
# - For power-of-two bases, CPython packs each hex digit's 4 bits straight into
#   the integer, which takes linear time. Horner's method in pure Python is
#   roughly quadratic for very long strings, because every step multiplies a
#   growing big integer.
# - Power-of-two bases are exempt from the `int` max-str-digits limit, which
#   only applies to non-power-of-two bases such as base 10.
# - It is more permissive than this spec: it also accepts lowercase, a '0x'
#   prefix, underscores, surrounding whitespace, a leading sign, and non-ASCII
#   Unicode digits. Validate first, e.g. re.fullmatch(r'[0-9A-F]+', hex_str),
#   if strict input is required.
def hex_to_decimal(hex_str: str) -> int:
    """Convert a hexadecimal string to its decimal integer value.

    Uses Horner's method: shift the accumulated value one hex place to the
    left (multiply by 16) and add the next digit.

    Args:
        hex_str: A hexadecimal number using the digits 0-9 and A-F.

    Returns:
        The integer value of `hex_str`.

    Raises:
        ValueError: If `hex_str` is empty or contains characters other
            than 0-9 or A-F.
    """
    if not hex_str:
        msg = 'empty hexadecimal string'
        raise ValueError(msg)
    invalid = set(hex_str).difference(_HEX_TO_DEC)
    if invalid:
        msg = f'invalid hexadecimal character(s): {sorted(invalid)}'
        raise ValueError(msg)

    result = 0
    for char in hex_str:
        result = result * 16 + _HEX_TO_DEC[char]
    return result


tests = [
    ('A', 10),
    ('15', 21),
    ('2E', 46),
    ('FF', 255),
    ('A3F', 2623),
]


@mark.parametrize('hex_str, expected', tests)
def test_hex_to_decimal(hex_str: str, expected: int) -> None:
    """Test hex_to_decimal function."""
    assert hex_to_decimal(hex_str) == expected


if __name__ == '__main__':
    # hex_str, expected = tests[0]
    # print(hex_to_decimal(hex_str))
    print(hex_to_decimal('A3FX'))
