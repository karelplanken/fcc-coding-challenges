# Daily Coding challenge #284 (2026-05-21) - freeCodeCamp.org
# I Before E
# Given a word or sentence, return a corrected version where every word follows the
# "I before E except after C" rule.
# If a word contains "ei" not preceded by "c", replace it with "ie".
# If a word contains "ie" preceded by "c", replace it with "ei".
# All other words are left unchanged.
import re

from pytest import mark

_CIE = re.compile(r'cie')
_EI_NOT_C = re.compile(r'(?<!c)ei')


def i_before_e(sentence: str) -> str:
    sentence = _CIE.sub('cei', sentence)
    sentence = _EI_NOT_C.sub('ie', sentence)
    return sentence


tests = [
    ('beleive', 'believe'),
    ('recieve', 'receive'),
    ('we recieved a breif', 'we received a brief'),
    (
        'she beleived the friendly niece could percieve the greif',
        'she believed the friendly niece could perceive the grief',
    ),
    (
        'we recieved relief after the theif gave us a breif piece of feirce deceit',
        'we received relief after the thief gave us a brief piece of fierce deceit',
    ),
]


@mark.parametrize('sentence, expected', tests)
def test_i_before_e(sentence: str, expected: str) -> None:
    assert i_before_e(sentence) == expected


if __name__ == '__main__':
    sentence, expected = tests[4]
    print(i_before_e(sentence))
