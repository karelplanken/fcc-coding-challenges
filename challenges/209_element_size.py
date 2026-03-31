# Daily Coding challenge #209 (2026-03-07) - freeCodeCamp.org
# Element Size
# Given a window size, the width of an element in viewport width "vw" units, and the
# height of an element in viewport height "vh" units, determine the size of the element
# in pixels.

# The given window size and returned element size are strings in the format
# "width x height", "1200 x 800" for example.

# "vw" units are the percent of window width. "50vw" for example, is 50% of the width
# of the window.

# "vh" units are the percent of window height. "50vh" for example, is 50% of the height
# of the window.
from pytest import mark


def get_element_size(window_size: str, element_vw: str, element_vh: str) -> str:
    win_w, win_h = (int(x) for x in window_size.split(' x '))
    
    vw = int(element_vw.removesuffix('vw'))
    vh = int(element_vh.removesuffix('vh'))
    
    return f'{round(win_w * vw / 100)} x {round(win_h * vh / 100)}'


tests = [
    ('1200 x 800', '50vw', '50vh', '600 x 400'),
    ('320 x 480', '25vw', '50vh', '80 x 240'),
    ('1000 x 500', '7vw', '3vh', '70 x 15'),
    ('1920 x 1080', '95vw', '100vh', '1824 x 1080'),
    ('1200 x 800', '0vw', '0vh', '0 x 0'),
    ('1440 x 900', '100vw', '114vh', '1440 x 1026'),
]


@mark.parametrize('window_size, element_vw, element_vh, expected', tests)
def test_solution(
    window_size: str, element_vw: str, element_vh: str, expected: str
) -> None:
    assert get_element_size(window_size, element_vw, element_vh) == expected


if __name__ == '__main__':
    window_size, element_vw, element_vh, expected = tests[1]
    print(get_element_size(window_size, element_vw, element_vh))
