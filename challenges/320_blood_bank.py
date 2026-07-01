# Daily Coding challenge #320 (2026-06-26) - freeCodeCamp.org
# Blood Bank
# Given an array of the inventory at a blood bank and an array of patient blood type
# requests, return a string in the format "X of Y patients served". Where X is the
# maximum number of patients that can receive blood from the bank's inventory, and Y
# is the total number of patients.
#
# Each entry in both arrays is one of the following blood types: "AB", "A", "B",
# or "O".
#
# Compatibility rules:
#
# - "AB" can receive from any blood type.
# - "A" can receive from "A" and "O".
# - "B" can receive from "B" and "O".
# - "O" can only receive from "O".
#
# Duplicate entries in the given arrays represent quantity.
from collections import Counter
from types import MappingProxyType

from pytest import mark

# Order matters to serve a maximum number of patients. The order of blood types in this
# list is from least compatible to most compatible. This is important because we want
# to serve the least compatible patients first, so that we can save the more compatible
# blood types for the more compatible patients.
COMPATIBLE_DONORS = MappingProxyType({
    'O': ['O'],
    'A': ['A', 'O'],
    'B': ['B', 'O'],
    'AB': ['A', 'B', 'AB', 'O'],
})


def triage_blood(bank: list[str], patients: list[str]) -> str:
    bank_count: Counter[str] = Counter(bank)
    patients_count: Counter[str] = Counter(patients)
    patients_served = 0

    for blood_type, donors in COMPATIBLE_DONORS.items():
        demand = patients_count[blood_type]
        if not demand:
            continue
        for donor in donors:
            supply = min(demand, bank_count[donor])
            bank_count[donor] -= supply
            demand -= supply
            if not demand:
                break
        patients_served += patients_count[blood_type] - demand

    return f'{patients_served} of {len(patients)} patients served'


tests = [
    (['O', 'A', 'B', 'AB'], ['O', 'A', 'B', 'AB'], '4 of 4 patients served'),
    (['A', 'A', 'B', 'B', 'AB'], ['O', 'A', 'B', 'B', 'B'], '3 of 5 patients served'),
    (['O', 'A', 'B', 'AB'], ['AB', 'AB', 'AB', 'AB', 'AB'], '4 of 5 patients served'),
    (['O', 'O', 'O', 'O', 'O'], ['O', 'A', 'B', 'AB'], '4 of 4 patients served'),
    (
        ['A', 'O', 'B', 'AB', 'B', 'AB', 'O', 'A', 'A'],
        ['O', 'A', 'B', 'AB', 'A', 'B', 'A', 'A', 'B', 'A', 'B'],
        '8 of 11 patients served',
    ),
    (
        [
            'O',
            'B',
            'AB',
            'AB',
            'O',
            'A',
            'A',
            'AB',
            'O',
            'B',
            'B',
            'AB',
            'A',
            'B',
            'AB',
        ],
        ['O', 'A', 'B', 'B', 'A', 'B', 'AB', 'A', 'B', 'A', 'O', 'AB', 'AB', 'O'],
        '13 of 14 patients served',
    ),
]


@mark.parametrize('bank, patients, expected', tests)
def test_triage_blood(bank: list[str], patients: list[str], expected: str) -> None:
    assert triage_blood(bank, patients) == expected


if __name__ == '__main__':
    bank, patients, expected = tests[5]
    print(triage_blood(bank, patients))
