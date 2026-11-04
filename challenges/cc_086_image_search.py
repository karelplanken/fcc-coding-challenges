"""Daily Coding Challenge #86 (2025-11-04) - freeCodeCamp.org."""

# Image Search
# On November 4th, 2001, Google launched its image search, allowing people to find
# images using search terms. In this challenge, you will imitate the image search.
#
# Given an array of image names and a search term, return an array of image names
# containing the search term.
#
# - Ignore the case when matching the search terms.
# - Return the images in the same order they appear in the input array.
from pytest import mark


def image_search(images: list[str], term: str) -> list[str]:
    """Return the image names that contain the search term, ignoring case.

    Matching is a literal substring test using Unicode case folding, so
    regex metacharacters in the term have no special meaning. Input order
    is preserved. An empty term matches every name.

    Args:
        images: Image names to search.
        term: Substring to look for.

    Returns:
        The matching image names, in their original order.
    """
    needle = term.casefold()
    return [image for image in images if needle in image.casefold()]


tests = [
    (['dog.png', 'cat.jpg', 'parrot.jpeg'], 'dog', ['dog.png']),
    (
        ['Sunset.jpg', 'Beach.png', 'sunflower.jpeg'],
        'sun',
        ['Sunset.jpg', 'sunflower.jpeg'],
    ),
    (['Moon.png', 'sun.jpeg', 'stars.png'], 'PNG', ['Moon.png', 'stars.png']),
    (
        ['cat.jpg', 'dogToy.jpeg', 'kitty-cat.png', 'catNip.jpeg', 'franken_cat.gif'],
        'Cat',
        ['cat.jpg', 'kitty-cat.png', 'catNip.jpeg', 'franken_cat.gif'],
    ),
    (['do.*g.png', 'cat.jpg', 'parrot.jpeg'], 'do.*g', ['do.*g.png']),
]


@mark.parametrize('images, term, expected', tests)
def test_image_search(images: list[str], term: str, expected: list[str]) -> None:
    """Test image_search function."""
    assert image_search(images, term) == expected


if __name__ == '__main__':
    images, term, expected = tests[0]
    print(image_search(images, term))
