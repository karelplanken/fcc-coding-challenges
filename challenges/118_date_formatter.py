# Daily Coding challenge #118 (2025-12-06) - freeCodeCamp.org
# Date Formatter
# Given a date in the format "Month day, year", return the date in the
# format "YYYY-MM-DD".

# The given month will be the full English month name. For example: "January",
# "February", etc. In the return value, pad the month and day with leading zeros
# if necessary to ensure two digits. For example, given "December 6, 2025",
# return "2025-12-06".
from types import MappingProxyType

from pytest import mark

MONTHS = MappingProxyType(
    {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }
)


# def format_date(date_string: str) -> str:
#     # This does not work since test data contain years with less than 4 digits
#     # from datetime import date
#     # Parse the input date string
#     # parsed_date = date.strptime(date_string, "%B %d, %Y")
#     # return parsed_date.strftime("%Y-%m-%d")

#     month_str, day_year = date_string.split(' ', 1)
#     day_str, year_str = day_year.split(', ')
#     month_num = MONTHS[month_str]

#     return f'{year_str}-{month_num:02d}-{day_str.zfill(2)}'

# def format_date(date_string: str) -> str:
#     parts = date_string.replace(',', '').split()
#     month, day, year = parts[0], parts[1], parts[2]
#     return f'{year}-{MONTHS[month]:02d}-{day.zfill(2)}'


def format_date(date_string: str) -> str:
    m, d, y = date_string.replace(',', '').split()
    return f'{y}-{MONTHS[m]:02d}-{d.zfill(2)}'


tests = [
    ('December 6, 2025', '2025-12-06'),
    ('January 1, 2000', '2000-01-01'),
    ('November 11, 1111', '1111-11-11'),
    ('September 7, 512', '512-09-07'),
    ('May 4, 1950', '1950-05-04'),
    ('February 29, 1992', '1992-02-29'),
]


@mark.parametrize('date_string,expected', tests)
def test_format_date(date_string: str, expected: str) -> None:
    assert format_date(date_string) == expected


if __name__ == '__main__':
    date_string, expected = tests[0]
    print(format_date(date_string))
