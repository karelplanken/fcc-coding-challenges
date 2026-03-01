# Daily Coding challenge #19 (2025-08-29) - freeCodeCamp.org
# Candlelight
# Given an integer representing the number of candles you start with, and an integer
# representing how many burned candles it takes to create a new one, return the number
# of candles you will have used after creating and burning as many as you can.

# For example, if given 7 candles and it takes 2 burned candles to make a new one:

# Burn 7 candles to get 7 leftovers,
# Recycle 6 leftovers into 3 new candles (1 leftover remains),
# Burn 3 candles to get 3 more leftovers (4 total),
# Recycle 4 leftovers into 2 new candles,
# Burn 2 candles to get 2 leftovers,
# Recycle 2 leftovers into 1 new candle,
# Burn 1 candle.
# You will have burned 13 total candles in the example.
from pytest import mark


def burn_candles(candles: int, leftovers_needed: int) -> int:
    total_burnt = 0
    leftovers = 0

    while candles > 0:
        # Burn all current candles
        total_burnt += candles
        leftovers += candles

        # Recycle leftovers into new candles
        candles = leftovers // leftovers_needed
        leftovers = leftovers % leftovers_needed

    return total_burnt


# Closed-form solution:
# def burn_candles(candles: int, leftovers_needed: int) -> int:
#     # Every candle eventually gets burned
#     # Additional candles come from recycling (leftovers_needed - 1) burned candles
#     return candles + (candles - 1) // (leftovers_needed - 1)

tests = [(7, 2, 13), (10, 5, 12), (20, 3, 29), (17, 4, 22), (2345, 3, 3517)]


@mark.parametrize('candles, leftovers_needed, expected', tests)
def test_burn_candles(candles: int, leftovers_needed: int, expected: int) -> None:
    assert burn_candles(candles, leftovers_needed) == expected


if __name__ == '__main__':
    candles, leftovers_needed, expected = tests[0]
    print(burn_candles(candles, leftovers_needed))
