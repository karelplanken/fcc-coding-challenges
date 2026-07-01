# Daily Coding challenge #318 (2026-06-24) - freeCodeCamp.org
# DNA Mutations
# Given two DNA strands of equal length, return an array of indexes where the strands
# differ (mutations).
#
# - DNA strands are strings made up of the characters `"A"`, `"T"`, `"C"`, and `"G"`
# - Return the indexes in ascending order
# - If there are no mutations, return an empty array
from pytest import mark


def detect_mutations(strand1: str, strand2: str) -> list[int]:
    return [i for i, (b1, b2) in enumerate(zip(strand1, strand2)) if b1 != b2]
    # Alternative using map and compress from itertools
    # from itertools import compress
    # mask = (b1 != b2 for b1, b2 in zip(strand1, strand2))
    # return list(compress(range(len(strand1)), mask))


tests = [
    ('ATCG', 'ATGG', [2]),
    ('ATGCGTACGTTAGC', 'ATGCATACGATTGC', [4, 9, 11]),
    ('GATCTAGCTAGGCTAGCTAG', 'GATCTAGCTAGGCTAGCTAG', []),
    (
        'TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG',
        'TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG',
        [15, 16, 17, 18],
    ),
    (
        'ACGTCAGTACGCACATGACCATTGACATA',
        'AACGTCAGTACGCACATGACCATTGACAT',
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            20,
            21,
            23,
            24,
            25,
            26,
            27,
            28,
        ],
    ),
]


@mark.parametrize('strand1, strand2, expected', tests)
def test_detect_mutations(strand1: str, strand2: str, expected: list[int]) -> None:
    assert detect_mutations(strand1, strand2) == expected


if __name__ == '__main__':
    strand1, strand2, expected = tests[1]
    print(detect_mutations(strand1, strand2))
