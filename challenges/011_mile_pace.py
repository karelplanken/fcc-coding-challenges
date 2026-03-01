# Daily Coding challenge #11 (2025-08-21) - freeCodeCamp.org
# Mile Pace
# Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run
# those miles, return a string for the average time it took to run each mile in the
# format "MM:SS".

# Add leading zeros when needed.
from pytest import mark


def mile_pace(miles: float, duration: str) -> str:
    minutes, seconds = map(int, duration.split(':'))
    total_seconds = minutes * 60 + seconds
    avg_seconds_per_mile = round(total_seconds / miles)
    avg_minutes, avg_seconds = divmod(avg_seconds_per_mile, 60)
    return f'{avg_minutes:02}:{avg_seconds:02}'


tests = [
    (3, '24:00', '08:00'),
    (1, '06:45', '06:45'),
    (2, '07:00', '03:30'),
    (26.2, '120:35', '04:36'),
]


@mark.parametrize('miles, duration, expected', tests)
def test_mile_pace(miles: float, duration: str, expected: str) -> None:
    assert mile_pace(miles, duration) == expected


if __name__ == '__main__':
    miles, duration, expected = tests[0]
    print(mile_pace(miles, duration))
