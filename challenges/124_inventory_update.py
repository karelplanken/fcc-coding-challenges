# Daily Coding challenge #124 (2025-12-12) - freeCodeCamp.org
# Inventory Update
# Given a 2D array representing the inventory of your store, and another 2D array
# representing a shipment you have received, return your updated inventory.

# Each element in the arrays will have the format: [quantity, "item"], where quantity
# is an integer and "item" is a string.
# Update items in the inventory by adding the quantity of any matching items from the
# shipment.
# If a received item does not exist in the current inventory, add it as a new entry to
# the end of the inventory.
# Return inventory in the order it was given with new items at the end in the order
# they appear in the shipment.
# For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment
# of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]].
from pytest import mark


def update_inventory(
    inventory: list[list[int | str]], shipment: list[list[int | str]]
) -> list[list[int | str]]:
    # Typecast quantity to int to satisfy type checker
    inventory_dict = {item: int(quantity) for quantity, item in inventory}

    for quantity, item in shipment:
        # Typecast quantity to int to satisfy type checker
        inventory_dict[item] = inventory_dict.get(item, 0) + int(quantity)

    return [[quantity, item] for item, quantity in inventory_dict.items()]


tests: list[
    tuple[list[list[int | str]], list[list[int | str]], list[list[int | str]]]
] = [
    (
        [[2, 'apples'], [5, 'bananas']],
        [[1, 'apples'], [3, 'bananas']],
        [[3, 'apples'], [8, 'bananas']],
    ),
    (
        [[2, 'apples'], [5, 'bananas']],
        [[1, 'apples'], [3, 'bananas'], [4, 'oranges']],
        [[3, 'apples'], [8, 'bananas'], [4, 'oranges']],
    ),
    (
        [],
        [[10, 'apples'], [30, 'bananas'], [20, 'oranges']],
        [[10, 'apples'], [30, 'bananas'], [20, 'oranges']],
    ),
    (
        [[0, 'Bowling Ball'], [0, 'Dirty Socks'], [0, 'Hair Pin'], [0, 'Microphone']],
        [
            [1, 'Hair Pin'],
            [1, 'Half-Eaten Apple'],
            [1, 'Bowling Ball'],
            [1, 'Toothpaste'],
        ],
        [
            [1, 'Bowling Ball'],
            [0, 'Dirty Socks'],
            [1, 'Hair Pin'],
            [0, 'Microphone'],
            [1, 'Half-Eaten Apple'],
            [1, 'Toothpaste'],
        ],
    ),
]


@mark.parametrize('inventory,shipment,expected', tests)
def test_update_inventory(
    inventory: list[list[int | str]],
    shipment: list[list[int | str]],
    expected: list[list[int | str]],
) -> None:
    assert update_inventory(inventory, shipment) == expected


if __name__ == '__main__':
    inventory, shipment, expected = tests[0]
    print(update_inventory(inventory, shipment))
