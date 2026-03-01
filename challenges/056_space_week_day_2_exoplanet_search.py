# Daily Coding challenge #56 (2025-10-05) - freeCodeCamp.org
# Space Week Day 2: Exoplanet Search
# For the second day of Space Week, you are given a string where each character
# represents the luminosity reading of a star. Determine if the readings have detected
# an exoplanet using the transit method. The transit method is when a planet passes in
# front of a star, reducing its observed luminosity.

# Luminosity readings only comprise of characters 0-9 and A-Z where each reading
# corresponds to the following numerical values:
# Characters 0-9 correspond to luminosity levels 0-9.
# Characters A-Z correspond to luminosity levels 10-35.
# A star is considered to have an exoplanet if any single reading is less than or equal
# to 80% of the average of all readings. For example, if the average luminosity of a
# star is 10, it would be considered to have a exoplanet if any single reading is 8 or
# less.
import string

from pytest import mark

READING_TO_VALUE: dict[str, int] = {
    **{str(digit): digit for digit in range(10)},
    **{reading: value for reading, value in zip(string.ascii_uppercase, range(10, 36))},
}


def has_exoplanet(readings: str) -> bool:
    values = [READING_TO_VALUE[reading] for reading in readings]
    return min(values) <= 0.8 * sum(values) / len(values)


# With helper function and abstraction:
# def get_reading_value(char: str, base: str = 'A', offset: int = 10) -> int:
#     if char.isdigit():
#         return int(char)

#     if char.isalpha() and char.isupper():
#         return ord(char) - ord(base) + offset

#     raise ValueError(f"Invalid character '{char}': expected 0-9 or A-Z")


# def has_exoplanet(readings: str) -> bool:
#     values = [get_reading_value(char) for char in readings]
#     return min(values) <= 0.8 * sum(values) / len(values)


# Hybrid:
# def has_exoplanet(readings: str) -> bool:
#     def get_value(char: str) -> int:
#         if char.isdigit():
#             return int(char)
#         return ord(char.upper()) - ord('A') + 10

#     values = [get_value(char) for char in readings]
#     return min(values) <= 0.8 * sum(values) / len(values)


tests = [
    ('665544554', False),
    ('FGFFCFFGG', True),
    ('MONOPLONOMONPLNOMPNOMP', False),
    ('FREECODECAMP', True),
    ('9AB98AB9BC98A', False),
    ('ZXXWYZXYWYXZEGZXWYZXYGEE', True),
]


@mark.parametrize('readings, expected', tests)
def test_has_exoplanet(readings: str, expected: bool) -> None:
    assert has_exoplanet(readings) == expected


if __name__ == '__main__':
    readings, expected = tests[0]
    print(has_exoplanet((readings)))
