# Daily Coding challenge #259 (2026-04-26) - freeCodeCamp.org
# FizzBuzz Explosion
# Given an integer, return the number of steps it takes to turn the word "fizzbuzz"
# into a string with at least the given number of "z"'s using the following rules:

# Start with the string "fizzbuzz".
# Each step, apply the standard FizzBuzz rules using the letter position in the string
# (the first "f" is position 1).
# If the letter position is divisible by 3, replace the letter with "fizz"
# If it's divisible by 5, replace the letter with "buzz"
# If it's divisible by 3 and 5, replace the letter with "fizzbuzz"
# So after 1 step, "fizzbuzz" turns into "fifizzzbuzzfizzzz", which has 9 "z"'s.
from pytest import mark


def explode_step(s: str) -> str:
    result = []
    for idx, char in enumerate(s, start=1):
        if idx % 15 == 0:
            result.append('fizzbuzz')
        elif idx % 5 == 0:
            result.append('buzz')
        elif idx % 3 == 0:
            result.append('fizz')
        else:
            result.append(char)
    return ''.join(result)


def explode_fizzbuzz(target_z_count: int) -> int:
    s = 'fizzbuzz'
    for step in range(1, 100):
        s = explode_step(s)
        if s.count('z') >= target_z_count:
            return step
    raise ValueError(f"Could not reach {target_z_count} z's in 100 steps")


# Solution using a lists instead of strings:
# def explode_fizzbuzz(target_z_count: int) -> int:
#     prev = list('fizzbuzz')
#     i = 1
#     while True:
#         curr = []
#         for idx, char in enumerate(prev, start=1):
#             if idx % 15 == 0:
#                 curr.extend(list('fizzbuzz'))
#             elif idx % 5 == 0:
#                 curr.extend(list('buzz'))
#             elif idx % 3 == 0:
#                 curr.extend(list('fizz'))
#             else:
#                 curr.append(char)
#         if sum(1 for char in curr if char == 'z') >= target_z_count:
#             return i
#         i += 1
#         prev = curr


tests = [
    (9, 1),
    (15, 2),
    (51, 3),
    (52, 4),
    (359, 5),
    (789, 6),
    (54482, 11),
    (1000000, 14),
]


@mark.parametrize('target_z_count, expected', tests)
def test_explode_fizzbuzz(target_z_count: int, expected: int) -> None:
    assert explode_fizzbuzz(target_z_count) == expected


if __name__ == '__main__':
    target_z_count, expected = tests[3]
    print(explode_fizzbuzz(target_z_count))
