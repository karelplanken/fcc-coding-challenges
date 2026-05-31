# Daily Coding challenge #274 (2026-05-11) - freeCodeCamp.org
# Oldest Person
# Given an array of objects, each with a "name" and "age" property, return an array
# containing the name of the oldest person.
# If multiple people share the oldest age, return all of their names in the order they
# appear in the input.
from typing import TypedDict

from pytest import mark


class Person(TypedDict):
    name: str
    age: int


def get_oldest(people: list[Person]) -> list[str]:
    max_age = max(person['age'] for person in people)
    return [person['name'] for person in people if person['age'] == max_age]


tests: list[tuple[list[Person], list[str]]] = [
    ([{'name': 'Brenda', 'age': 40}], ['Brenda']),
    ([{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}], ['Alice']),
    (
        [
            {'name': 'Allison', 'age': 25},
            {'name': 'Bill', 'age': 30},
            {'name': 'Carol', 'age': 30},
        ],
        ['Bill', 'Carol'],
    ),
    (
        [
            {'name': 'George', 'age': 50},
            {'name': 'Shirley', 'age': 42},
            {'name': 'Beth', 'age': 48},
            {'name': 'Holly', 'age': 50},
            {'name': 'Kevin', 'age': 44},
            {'name': 'Frank', 'age': 47},
            {'name': 'Zach', 'age': 50},
            {'name': 'Jennifer', 'age': 43},
        ],
        ['George', 'Holly', 'Zach'],
    ),
]


@mark.parametrize('people, expected', tests)
def test_get_oldest(people: list[Person], expected: list[str]) -> None:
    assert get_oldest(people) == expected


if __name__ == '__main__':
    people, expected = tests[0]
    print(get_oldest(people))


# Using reduce is not the most efficient way to solve this problem, but it is an
# interesting alternative to the more straightforward approach of iterating through the
# list of people and keeping track of the maximum age and corresponding names
# (see below). The reduce function allows us to accumulate the maximum age and names in
# a single pass through the list, but it may be less readable and more complex than the
# iterative approach.
# from functools import reduce
# from typing import TypedDict

# from pytest import mark


# class Person(TypedDict):
#     name: str
#     age: int

# def get_oldest(people: list[Person]) -> list[str]:
#     def accumulate(
#             acc: tuple[int, list[str]], person: Person
#     ) -> tuple[int, list[str]]:
#         max_age, names = acc
#         if person['age'] > max_age:
#             return (person['age'], [person['name']])
#         if person['age'] == max_age:
#             return (max_age, names + [person['name']])
#         return acc

#     _, oldest_names = reduce(
#         accumulate, people[1:], (people[0]['age'], [people[0]['name']])
#     )
#     return oldest_names


# def get_oldest(people: list[Person]) -> list[str]:
#     max_age = people[0]['age']
#     result = [people[0]['name']]

#     for person in people[1:]:
#         if person['age'] > max_age:
#             max_age = person['age']
#             result = [person['name']]
#         elif person['age'] == max_age:
#             result.append(person['name'])

#     return result
