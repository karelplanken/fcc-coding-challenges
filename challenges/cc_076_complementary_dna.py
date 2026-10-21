"""Daily Coding Challenge #76 (2025-10-25) - freeCodeCamp.org."""

# Complementary DNA
# Given a string representing a DNA sequence, return its complementary strand using the
# following rules:
#
# - DNA consists of the letters "A", "C", "G", and "T".
# - The letters "A" and "T" complement each other.
# - The letters "C" and "G" complement each other.
#
# For example, given "ACGT", return "TGCA".
from pytest import mark

_COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
_DNA_BASES = frozenset(_COMPLEMENT)
_COMPLEMENT_TABLE = str.maketrans(_COMPLEMENT)


def complementary_dna(strand: str) -> str:
    """Return the complementary DNA strand.

    Args:
        strand: A DNA sequence consisting only of the uppercase bases A, C, G and T.

    Returns:
        The complementary strand, with A and T swapped and C and G swapped.

    Raises:
        ValueError: If `strand` contains any character other than A, C, G or T.
    """
    if invalid := set(strand) - _DNA_BASES:
        msg = f'invalid DNA base(s) {sorted(invalid)}; expected only A, C, G, T'
        raise ValueError(msg)
    return strand.translate(_COMPLEMENT_TABLE)


tests = [
    ('ACGT', 'TGCA'),
    ('ATGCGTACGTTAGC', 'TACGCATGCAATCG'),
    ('GGCTTACGATCGAAG', 'CCGAATGCTAGCTTC'),
    ('GATCTAGCTAGGCTAGCTAG', 'CTAGATCGATCCGATCGATC'),
]


@mark.parametrize('strand, expected', tests)
def test_complementary_dna(strand: str, expected: str) -> None:
    """Test complementary_dna function."""
    assert complementary_dna(strand) == expected


if __name__ == '__main__':
    strand, expected = tests[0]
    print(complementary_dna(strand))
