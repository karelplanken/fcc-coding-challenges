# Daily Coding challenge #314 (2026-06-20) - freeCodeCamp.org
# Prime Factorization
# Given an integer greater than 1, return its prime factorization as an array of
# numbers in ascending order.

# A prime factorization is the set of prime numbers that multiply together to produce
# the given integer. Each number has exactly one set. For example, the prime
# factorization of 20 is [2, 2, 5] because 2 * 2 * 5 = 20.

# If the given integer is itself prime, return it in a single-element array.
from pytest import mark


def prime_factorization(n: int) -> list[int]:
    prime_factors = []
    candidate = 2

    # Candidates are tried in increasing order and never decrease, so
    # factors are appended in ascending order — no explicit sort needed.
    while candidate * candidate <= n:
        quotient, remainder = divmod(n, candidate)
        if remainder == 0:
            prime_factors.append(candidate)
            n = quotient
        else:
            candidate += 1

    prime_factors.append(n)
    return prime_factors


tests = [
    (20, [2, 2, 5]),
    (17, [17]),
    (15, [3, 5]),
    (35, [5, 7]),
    (999, [3, 3, 3, 37]),
    (360, [2, 2, 2, 3, 3, 5]),
    (510510, [2, 3, 5, 7, 11, 13, 17]),
]


@mark.parametrize('n, expected', tests)
def test_prime_factorization(n: int, expected: list[int]) -> None:
    assert prime_factorization(n) == expected


if __name__ == '__main__':
    n, expected = tests[6]
    print(prime_factorization(n))
