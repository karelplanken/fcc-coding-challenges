# Daily Coding challenge #174 (2026-01-31) - freeCodeCamp.org
# Zodiac Finder
# Given a date string in the format "YYYY-MM-DD", return the zodiac sign for that date
# using the following chart:

# Date Range	Zodiac Sign
# March 21 - April 19	"Aries"
# April 20 - May 20	"Taurus"
# May 21 - June 20	"Gemini"
# June 21 - July 22	"Cancer"
# July 23 - August 22	"Leo"
# August 23 - September 22	"Virgo"
# September 23 - October 22	"Libra"
# October 23 - November 21	"Scorpio"
# November 22 - December 21	"Sagittarius"
# December 22 - January 19	"Capricorn"
# January 20 - February 18	"Aquarius"
# February 19 - March 20	"Pisces"
# Zodiac signs are based only on the month and day, you can ignore the year.
from dataclasses import dataclass
from datetime import date

from pytest import mark


@dataclass(frozen=True)
class Zodiac:
    month: str
    day_end: int
    name: str


ZODIACS = (
    Zodiac('January', 19, 'Capricorn'),
    Zodiac('February', 18, 'Aquarius'),
    Zodiac('March', 20, 'Pisces'),
    Zodiac('April', 19, 'Aries'),
    Zodiac('May', 20, 'Taurus'),
    Zodiac('June', 20, 'Gemini'),
    Zodiac('July', 22, 'Cancer'),
    Zodiac('August', 22, 'Leo'),
    Zodiac('September', 22, 'Virgo'),
    Zodiac('October', 22, 'Libra'),
    Zodiac('November', 21, 'Scorpio'),
    Zodiac('December', 21, 'Sagittarius'),
    Zodiac('December', 31, 'Capricorn'),
)


def get_sign(date_str: str) -> str:
    dt = date.fromisoformat(date_str)
    dt_month = dt.strftime('%B')
    dt_day = dt.day

    for i, zodiac in enumerate(ZODIACS):
        if dt_month == zodiac.month:
            if dt_day <= zodiac.day_end:
                return zodiac.name
            else:
                # Safe bounds check
                if i + 1 < len(ZODIACS):
                    return ZODIACS[i + 1].name
                # This should never happen with valid data
                raise ValueError(f'No zodiac found for {date_str}')

    # Also should never happen
    raise ValueError(f'Invalid month in date: {date_str}')


tests = [
    ('2026-01-31', 'Aquarius'),
    ('2001-06-10', 'Gemini'),
    ('1985-09-07', 'Virgo'),
    ('2023-03-19', 'Pisces'),
    ('2045-11-05', 'Scorpio'),
    ('1985-12-06', 'Sagittarius'),
    ('2025-12-30', 'Capricorn'),
    ('2018-10-08', 'Libra'),
    ('1958-05-04', 'Taurus'),
]


@mark.parametrize('date_str, expected', tests)
def test_get_sign(date_str: str, expected: str) -> None:
    assert get_sign(date_str) == expected


if __name__ == '__main__':
    date_str, expected = tests[0]
    print(get_sign(date_str))
