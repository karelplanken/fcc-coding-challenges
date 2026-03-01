# Daily Coding challenge #21 (2025-08-31) - freeCodeCamp.org
# Hex Generator
# Given a named CSS color string, generate a random hexadecimal (hex) color code that
# is dominant in the given color.

# The function should handle "red", "green", or "blue" as an input argument.
# If the input is not one of those, the function should return "Invalid color".
# The function should return a random six-character hex color code where the input
# color value is greater than any of the others.
# Example of valid outputs for a given input:
# Input	Output
# "red"	"FF0000"
# "green"	"00FF00"
# "blue"	"0000FF"
from random import randint

from pytest import mark


def generate_hex(color: str) -> str:
    """Given a named CSS color string, return a random hexadecimal (hex) color code
    that is dominant in the given color. For any other color than red, green, blue,
    'Invalid color' is returned.

    :param color: Either red, green, or blue
    :return: Random hex color dominant in 'color`

    Examples:
    >>> generate_hex('yellow')
    'Invalid color'
    >>> result = generate_hex('red')
    >>> assert len(result) == 6 and all(c in '0123456789ABCDEF' for c in result)
    >>> reddish = generate_hex('red')
    >>> assert reddish[0:2] > reddish[2:4] and reddish[0:2] > reddish[4:6]
    >>> generate_hex('red') != generate_hex('red')
    True
    >>> greenish_1 = generate_hex('green')
    >>> greenish_2 = generate_hex('green')
    >>> assert greenish_1 != greenish_2
    >>> assert greenish_1[2:4] > greenish_1[0:2] and greenish_1[2:4] > greenish_1[4:6]
    >>> blueish_1 = generate_hex('blue')
    >>> blueish_2 = generate_hex('blue')
    >>> assert blueish_1 != blueish_2
    >>> assert blueish_1[4:6] > blueish_1[0:2] and blueish_1[4:6] > blueish_1[2:4]
    """
    if color not in ('red', 'green', 'blue'):
        return 'Invalid color'

    # Keep generating until we get a unique maximum
    while True:
        values = [randint(0, 255), randint(0, 255), randint(0, 255)]
        max_val = max(values)

        if values.count(max_val) == 1:
            break

    # Swap max value to the correct position
    max_idx = values.index(max_val)
    color_map = {'red': 0, 'green': 1, 'blue': 2}
    target_idx = color_map[color]
    values[max_idx], values[target_idx] = values[target_idx], values[max_idx]

    return f'{values[0]:02X}{values[1]:02X}{values[2]:02X}'


@mark.parametrize('color', ['red', 'green', 'blue', 'yellow', 'purple'])
def test_generate_hex(color: str) -> None:
    result = generate_hex(color)
    if color == 'red':
        assert len(result) == 6 and all(c in '0123456789ABCDEF' for c in result)
        assert result[0:2] > result[2:4] and result[0:2] > result[4:6]
    elif color == 'green':
        assert len(result) == 6 and all(c in '0123456789ABCDEF' for c in result)
        assert result[2:4] > result[0:2] and result[2:4] > result[4:6]
    elif color == 'blue':
        assert len(result) == 6 and all(c in '0123456789ABCDEF' for c in result)
        assert result[4:6] > result[0:2] and result[4:6] > result[2:4]
    else:
        assert result == 'Invalid color'


if __name__ == '__main__':
    import doctest

    doctest.testmod()  # use uv run *.py -v to see doctest output
