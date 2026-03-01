# Daily Coding challenge #76 (2025-10-25) - freeCodeCamp.org
# Complementary DNA
# Given a string representing a DNA sequence, return its complementary strand using the
# following rules:

# DNA consists of the letters "A", "C", "G", and "T".
# The letters "A" and "T" complement each other.
# The letters "C" and "G" complement each other.
# For example, given "ACGT", return "TGCA".
from pytest import mark


def complementary_dna(strand: str) -> str:
    return strand.translate(str.maketrans('ATGC', 'TACG'))


tests = [
    ('ACGT', 'TGCA'),
    ('ATGCGTACGTTAGC', 'TACGCATGCAATCG'),
    ('GGCTTACGATCGAAG', 'CCGAATGCTAGCTTC'),
    ('GATCTAGCTAGGCTAGCTAG', 'CTAGATCGATCCGATCGATC'),
]


@mark.parametrize('strand, expected', tests)
def test_complementary_dna(strand: str, expected: str) -> None:
    assert complementary_dna(strand) == expected


if __name__ == '__main__':
    strand, expected = tests[0]
    print(complementary_dna(strand))
