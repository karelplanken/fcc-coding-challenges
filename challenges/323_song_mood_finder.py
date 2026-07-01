# Daily Coding challenge #323 (2026-06-29) - freeCodeCamp.org
# Song Mood Finder
# Given a genre string and a BPM number for a song, determine the mood using the
# following table:
#
# | Mood | Genre | BPM Range |
# |------|-------|-----------|
# | "focus" | "classical" | 60–109 |
# | "focus" | "electronic" | 60–89 |
# | "happy" | "pop" | 60–180 |
# | "happy" | "classical" | 110–180 |
# | "happy" | "rock" | 60–129 |
# | "happy" | "electronic" | 90–134 |
# | "hype" | "rock" | 130–180 |
# | "hype" | "electronic" | 135–180 |
from dataclasses import dataclass
from typing import Final

from pytest import mark


@dataclass(frozen=True)
class SongMood:
    mood: str
    genre: str
    bpm_range: range


_SONG_MOODS: Final[list[SongMood]] = [
    SongMood(mood='focus', genre='classical', bpm_range=range(60, 110)),
    SongMood(mood='focus', genre='electronic', bpm_range=range(60, 90)),
    SongMood(mood='happy', genre='pop', bpm_range=range(60, 181)),
    SongMood(mood='happy', genre='classical', bpm_range=range(110, 181)),
    SongMood(mood='happy', genre='rock', bpm_range=range(60, 130)),
    SongMood(mood='happy', genre='electronic', bpm_range=range(90, 135)),
    SongMood(mood='hype', genre='rock', bpm_range=range(130, 181)),
    SongMood(mood='hype', genre='electronic', bpm_range=range(135, 181)),
]

_SONG_MOOD_TABLE: Final[dict[str, list[SongMood]]] = {}

for _sm in _SONG_MOODS:
    _SONG_MOOD_TABLE.setdefault(_sm.genre, []).append(_sm)


def get_mood(genre: str, bpm: int) -> str:
    try:
        entries = _SONG_MOOD_TABLE[genre]
    except KeyError:
        raise ValueError(f'Unknown {genre=}.') from None

    for entry in entries:
        if bpm in entry.bpm_range:
            return entry.mood

    raise ValueError(f'BPM {bpm} out of range for {genre=}.')


tests = [
    ('rock', 111, 'happy'),
    ('electronic', 74, 'focus'),
    ('classical', 180, 'happy'),
    ('rock', 155, 'hype'),
    ('electronic', 90, 'happy'),
    ('classical', 67, 'focus'),
    ('pop', 100, 'happy'),
    ('electronic', 135, 'hype'),
]


@mark.parametrize('genre, bpm, expected', tests)
def test_get_mood(genre: str, bpm: int, expected: str) -> None:
    assert get_mood(genre, bpm) == expected


if __name__ == '__main__':
    genre, bpm, expected = tests[0]
    print(get_mood(genre, bpm))
