# Daily Coding challenge #321 (2026-06-27) - freeCodeCamp.org
# Periodic Spelling
# Given a word, determine if it can be spelled using element symbols from the periodic
# table.
#
# - Ignore casing when spelling a word. `"neon"` can be spelled with the symbols `"Ne"`,
#   `"O"`, and `"N"`.
#
# Here's a full list of the element symbols:
#
# [
#   "H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar",
#   "K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br",
#   "Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te",
#   "I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm",
#   "Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn",
#   "Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr",
#   "Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"
# ]
#
# Return an array of the elements used to spell the word, in their original casing and
# in the order to spell the word. Or, an empty array if it can't be spelled.
# from itertools import permutations
from pytest import mark

ELEMENTS = {
    'ac': 'Ac',
    'ag': 'Ag',
    'al': 'Al',
    'am': 'Am',
    'ar': 'Ar',
    'as': 'As',
    'at': 'At',
    'au': 'Au',
    'b': 'B',
    'ba': 'Ba',
    'be': 'Be',
    'bh': 'Bh',
    'bi': 'Bi',
    'bk': 'Bk',
    'br': 'Br',
    'c': 'C',
    'ca': 'Ca',
    'cd': 'Cd',
    'ce': 'Ce',
    'cf': 'Cf',
    'cl': 'Cl',
    'cm': 'Cm',
    'cn': 'Cn',
    'co': 'Co',
    'cr': 'Cr',
    'cs': 'Cs',
    'cu': 'Cu',
    'db': 'Db',
    'ds': 'Ds',
    'dy': 'Dy',
    'er': 'Er',
    'es': 'Es',
    'eu': 'Eu',
    'f': 'F',
    'fe': 'Fe',
    'fl': 'Fl',
    'fm': 'Fm',
    'fr': 'Fr',
    'ga': 'Ga',
    'gd': 'Gd',
    'ge': 'Ge',
    'h': 'H',
    'he': 'He',
    'hf': 'Hf',
    'hg': 'Hg',
    'ho': 'Ho',
    'hs': 'Hs',
    'i': 'I',
    'in': 'In',
    'ir': 'Ir',
    'k': 'K',
    'kr': 'Kr',
    'la': 'La',
    'li': 'Li',
    'lr': 'Lr',
    'lu': 'Lu',
    'lv': 'Lv',
    'mc': 'Mc',
    'md': 'Md',
    'mg': 'Mg',
    'mn': 'Mn',
    'mo': 'Mo',
    'mt': 'Mt',
    'n': 'N',
    'na': 'Na',
    'nb': 'Nb',
    'nd': 'Nd',
    'ne': 'Ne',
    'nh': 'Nh',
    'ni': 'Ni',
    'no': 'No',
    'np': 'Np',
    'o': 'O',
    'og': 'Og',
    'os': 'Os',
    'p': 'P',
    'pa': 'Pa',
    'pb': 'Pb',
    'pd': 'Pd',
    'pm': 'Pm',
    'po': 'Po',
    'pr': 'Pr',
    'pt': 'Pt',
    'pu': 'Pu',
    'ra': 'Ra',
    'rb': 'Rb',
    're': 'Re',
    'rf': 'Rf',
    'rg': 'Rg',
    'rh': 'Rh',
    'rn': 'Rn',
    'ru': 'Ru',
    's': 'S',
    'sb': 'Sb',
    'sc': 'Sc',
    'se': 'Se',
    'sg': 'Sg',
    'si': 'Si',
    'sm': 'Sm',
    'sn': 'Sn',
    'sr': 'Sr',
    'ta': 'Ta',
    'tb': 'Tb',
    'tc': 'Tc',
    'te': 'Te',
    'th': 'Th',
    'ti': 'Ti',
    'tl': 'Tl',
    'tm': 'Tm',
    'ts': 'Ts',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'xe': 'Xe',
    'y': 'Y',
    'yb': 'Yb',
    'zn': 'Zn',
    'zr': 'Zr',
}


# Recursive backtracking directly on the string is the best approach here since only
# one solution is needed.
def get_periodic_spelling(word: str) -> list[str]:
    word = word.lower()

    def backtrack(pos: int) -> list[str] | None:
        if pos == len(word):
            return []
        for step in (1, 2):
            chunk = word[pos : pos + step]
            if chunk in ELEMENTS:
                rest = backtrack(pos + step)
                if rest is not None:
                    return [ELEMENTS[chunk]] + rest
        return None

    return backtrack(0) or []


# # The compositions approach is not efficient in the sense that it doesn't short-circuit,
# # it explores all paths even after finding the first solution, but returns all valid
# # spellings as a result.
# from functools import lru_cache
#
# @lru_cache(None)
# def _compositions(n: int) -> list[tuple[int, ...]]:
#     """All ordered compositions of n into 1s and 2s."""
#     if n == 0:
#         return [()]
#     if n < 0:
#         return []
#     return [(step,) + rest for step in (1, 2) for rest in _compositions(n - step)]


# def get_periodic_spelling(word: str) -> list[str]:
#     word = word.lower()
#     for composition in _compositions(len(word)):
#         result: list[str] = []
#         pos = 0
#         for step in composition:
#             chunk = word[pos : pos + step]
#             if chunk not in ELEMENTS:
#                 break  # early exit — this composition fails here
#             result.append(ELEMENTS[chunk])
#             pos += step
#         else:
#             return result  # for/else: loop completed without break
#     return []


tests = [
    ('neon', ['Ne', 'O', 'N']),
    ('rational', ['Ra', 'Ti', 'O', 'N', 'Al']),
    ('yarn', ['Y', 'Ar', 'N']),
    ('carbon', [['C', 'Ar', 'B', 'O', 'N'], ['Ca', 'Rb', 'O', 'N']]),
    ('noisy', [['N', 'O', 'I', 'S', 'Y'], ['No', 'I', 'S', 'Y']]),
    ('bicycles', [['B', 'I', 'C', 'Y', 'Cl', 'Es'], ['Bi', 'C', 'Y', 'Cl', 'Es']]),
    (
        'optics',
        [
            ['O', 'P', 'Ti', 'C', 'S'],
            ['O', 'P', 'Ti', 'Cs'],
            ['O', 'Pt', 'I', 'C', 'S'],
            ['O', 'Pt', 'I', 'Cs'],
        ],
    ),
    ('value', []),
]


@mark.parametrize('word, expected', tests)
def test_get_periodic_spelling(
    word: str, expected: list[list[str]] | list[str]
) -> None:
    result = get_periodic_spelling(word)
    assert result == expected or result in expected


if __name__ == '__main__':
    word, expected = tests[7]
    print(get_periodic_spelling(word))
