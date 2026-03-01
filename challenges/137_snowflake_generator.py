# Daily Coding challenge #137 (2025-12-25) - freeCodeCamp.org
# Snowflake Generator
# Given a multi-line string that uses newline characters (\n) to represent a line
# break, return a new string where each line is mirrored horizontally and attached to
# the end of the original line.

# Mirror a line by reversing all of its characters, including spaces.
# For example, given "* \n *\n* ", which logs to the console as:

# *
#  *
# *
# Return "*  *\n ** \n*  *", which logs to the console as:

# *  *
#  **
# *  *
# Take careful note of the whitespaces in the given and returned strings. Be sure not
# to trim any of them.
from pytest import mark


def generate_snowflake(crystals: str) -> str:
    return '\n'.join(line + line[::-1] for line in crystals.split('\n'))


tests = [
    ('* \n *\n* ', '*  *\n ** \n*  *'),
    ('X=~', 'X=~~=X'),
    (
        ' X  \n  v \nX--=\n  ^ \n X  ',
        ' X    X \n  v  v  \nX--==--X\n  ^  ^  \n X    X ',
    ),
    (
        '*   *\n * * \n* * *\n * * \n*   *',
        '*   **   *\n * *  * * \n* * ** * *\n * *  * * \n*   **   *',
    ),
    ('*  -\n * -\n*  -', '*  --  *\n * -- * \n*  --  *'),
]


@mark.parametrize('crystals, expected', tests)
def test_generate_snowflake(crystals: str, expected: str) -> None:
    assert generate_snowflake(crystals) == expected


if __name__ == '__main__':
    crystals, expected = tests[0]
    print(generate_snowflake(crystals))
