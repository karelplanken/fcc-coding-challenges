# Daily Coding challenge #357 (2026-08-02) - freeCodeCamp.org
# Food Chain
# Given an array of [predator, prey] pairs, return the food chain from the apex predator
# down to the bottom.
#
# - The apex predator is the animal that is never prey to another animal.
# - Return the chain as an array of strings.
from collections import deque

from pytest import mark


def get_food_chain(pairs: list[list[str]]) -> list[str]:
    """Constructs a food chain from the apex predator down to the bottom given pairs of
    predator and prey.

    Assumes that:
    - input pairs form a valid food chain with no cycles
    - each animal appears at most once as a predator and at most once as prey
    - pairs are closest predator-prey relationships, e.g. [A, B] and [B, C], not [A, C].
    - that there is a single apex predator

    Args:
        pairs: Predator and prey pairs.

    Returns:
        Food chain from apex predator to bottom prey.
    """
    pairs = pairs.copy()
    food_chain = deque(pairs.pop())

    while len(pairs) > 0:
        for pair in pairs:
            predator, prey = pair

            if food_chain[-1] == predator:
                food_chain.append(prey)
                # the break must stay adjacent to the remove
                pairs.remove(pair)
                break
            elif food_chain[0] == prey:
                food_chain.appendleft(predator)
                # the break must stay adjacent to the remove
                pairs.remove(pair)
                break

    return list(food_chain)


# Refactored solution using dictionaries to find the apex predator and build the food
# chain
# def get_food_chain(pairs: list[list[str]]) -> list[str]:
#     """Constructs a food chain from the apex predator down to the bottom given pairs
#     of predator and prey.

#     Assumes that:
#     - input pairs form a valid food chain with no cycles
#     - each animal appears at most once as a predator and at most once as prey
#     - pairs are closest predator-prey relationships, e.g. [A, B] and [B, C], not
#       [A, C]

#     Args:
#         pairs: Predator and prey pairs.

#     Returns:
#         Food chain from apex predator to bottom prey.

#     Raises:
#         ValueError: if pairs is empty or does not describe exactly one apex predator.
#     """
#     if not pairs:
#         raise ValueError('pairs must contain at least one predator-prey relationship')

#     prey_of: dict[str, str] = {predator: prey for predator, prey in pairs}
#     predators = prey_of.keys()
#     preys = set(prey_of.values())

#     apex_candidates = predators - preys
#     if len(apex_candidates) != 1:
#         raise ValueError(
#             f'expected exactly one apex predator, found {len(apex_candidates)}'
#         )

#     chain = [next(iter(apex_candidates))]
#     while chain[-1] in prey_of:
#         chain.append(prey_of[chain[-1]])
#     return chain


tests = [
    ([['cat', 'mouse']], ['cat', 'mouse']),
    ([['wolf', 'deer'], ['deer', 'grass']], ['wolf', 'deer', 'grass']),
    (
        [['hawk', 'snake'], ['snake', 'frog'], ['frog', 'fly']],
        ['hawk', 'snake', 'frog', 'fly'],
    ),
    (
        [['rabbit', 'grass'], ['fox', 'rabbit'], ['eagle', 'fox']],
        ['eagle', 'fox', 'rabbit', 'grass'],
    ),
    (
        [
            ['seal', 'salmon'],
            ['herring', 'shrimp'],
            ['orca', 'seal'],
            ['shrimp', 'plankton'],
            ['salmon', 'herring'],
        ],
        ['orca', 'seal', 'salmon', 'herring', 'shrimp', 'plankton'],
    ),
]


@mark.parametrize('pairs, expected', tests)
def test_get_food_chain(pairs: list[list[str]], expected: list[str]) -> None:
    assert get_food_chain(pairs) == expected


if __name__ == '__main__':
    pairs, expected = tests[0]
    print(get_food_chain(pairs))
