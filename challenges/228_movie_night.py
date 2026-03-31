# Daily Coding challenge #228 (2026-03-26) - freeCodeCamp.org
# Movie Night
# Given a string for the day of the week, another string for a showtime, and an integer
# number of tickets, return the total cost of the movie tickets for that showing.

# The given day will be one of:

# "Monday"
# "Tuesday"
# "Wednesday"
# "Thursday"
# "Friday"
# "Saturday"
# "Sunday"
# The showtime will be given in the format "H:MMam" or "H:MMpm".
# For example "10:00am" or "10:00pm".

# Return the total cost in the format "$D.CC" using these rules:

# Weekend (Friday - Sunday): $12.00 per ticket.
# Weekday (Monday - Thursday): $10.00 per ticket.
# Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
# Tuesdays: all tickets are $5.00 each.
from datetime import datetime

from pytest import mark

WEEKDAY_PRICE = 10
WEEKEND_PRICE = 12
TUESDAY_PRICE = 5
MATINEE_DISCOUNT = 2
MATINEE_CUTOFF = 17  # 5:00pm

WEEKEND_DAYS = {'Friday', 'Saturday', 'Sunday'}


def parse_hour(showtime: str) -> int:
    return datetime.strptime(showtime, '%I:%M%p').hour


def base_price(day: str) -> int:
    if day == 'Tuesday':
        return TUESDAY_PRICE
    return WEEKEND_PRICE if day in WEEKEND_DAYS else WEEKDAY_PRICE


def ticket_price(day: str, showtime: str) -> int:
    price = base_price(day)
    if day != 'Tuesday' and parse_hour(showtime) < MATINEE_CUTOFF:
        price -= MATINEE_DISCOUNT
    return price


def get_movie_night_cost(day: str, showtime: str, number_of_tickets: int) -> str:
    cost = ticket_price(day, showtime) * number_of_tickets
    return f'${cost:.2f}'


tests = [
    ('Saturday', '10:00pm', 1, '$12.00'),
    ('Sunday', '10:00am', 1, '$10.00'),
    ('Tuesday', '7:20pm', 2, '$10.00'),
    ('Wednesday', '5:40pm', 3, '$30.00'),
    ('Monday', '11:50am', 4, '$32.00'),
    ('Friday', '4:30pm', 5, '$50.00'),
    ('Tuesday', '11:30am', 1, '$5.00'),
]


@mark.parametrize('day, showtime, number_of_tickets, expected', tests)
def test_solution(
    day: str, showtime: str, number_of_tickets: int, expected: str
) -> None:
    assert get_movie_night_cost(day, showtime, number_of_tickets) == expected


if __name__ == '__main__':
    day, showtime, number_of_tickets, expected = tests[2]
    print(get_movie_night_cost(day, showtime, number_of_tickets))
    # get_movie_night_cost(day, showtime, number_of_tickets)
