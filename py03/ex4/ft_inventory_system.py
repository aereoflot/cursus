"""Player inventory utilities and simple CLI demo.

This module implements basic inventory operations for a small game-like
example: transferring items between inventories, computing inventory value
and item counts, and printing inventory summaries.

Functions:
- transaction(dict1, dict2, cat, value): move `value` units of `cat` from
  dict1 to dict2 (in-place) and print updates.
- clac_value_inv(dic): compute total gold value of an inventory and return
  a list with player keys found and the total.
- calc_items_inv(dic): compute total item count of an inventory and return
  a list with player keys found and the total count.
- show_info_invent(dic): print a human-friendly inventory summary.

The file also contains a simple demonstration in the "__main__" block.
"""


def transaction(dict1: dict, dict2: dict, cat: str, value: int):
    """Transfer items between two inventories and print updates.

    Args:
        dict1: source inventory mapping item names to characteristics or
               a player key (False).
               Characteristics are stored as a sequence:
               [category_str, price, qty].
        dict2: destination inventory (same structure as dict1).
        cat: item key to transfer (string).
        value: number of units to transfer (int).

    Behavior:
        - Raises ValueError if the source does not have enough quantity.
        - Otherwise subtracts `value` from the source quantity and adds it to
          the destination quantity (both inventories are modified in place).
        - Prints "Transaction successful!" and calls internal update printers.

    Note:
        This function assumes that items in dict1 and dict2 are stored as
        mutable sequences (e.g. lists) so that the quantity element (index 2)
        can be updated. If an expected key is missing a
        KeyError will be raised.
    """
    if (dict1[cat][2] - value) < 0:
        raise ValueError("Transaction unsuccessful :(\n")
    else:
        dict1[cat][2] -= value
        dict2[cat][2] += value
        print("Transaction successful!\n")

        def updates(dict1, cat, value):
            """Print a small update line for the provided inventory.

            The inner function looks for a falsy key (player name) and prints
            the player's name together with the item and its current quantity.

            Args:
                dict1: inventory to inspect.
                cat: item key to report.
                value: transfer amount (unused in the message but kept
                for API parity).
            """
            for key, value in dict1.items():
                if not value:
                    name = key
            print(f"{name} {cat}: {dict1[cat][2]}")

        print("=== Update Inventories ===")
        updates(dict1, cat, value)
        updates(dict2, cat, value)


def clac_value_inv(dic: dict) -> list:
    """Compute total gold value of an inventory.

    Args:
        dic: inventory mapping keys to either False (player key) or a
             sequence [category_str, price, qty].

    Returns:
        A list where:
        - zero or more leading elements are inventory keys with falsy values
          (typically the player name keys found in the dict),
        - the last element is the computed total gold value (int).

    Example:
        For {"Alice": False, "potion": ["consumable", 50, 5]}
        the function returns ["Alice", 250].
    """
    result = []
    total = 0

    for key, caracts in dic.items():
        if caracts:
            total += caracts[1] * caracts[2]
        else:
            result.append(key)
    result.append(total)
    return result


def calc_items_inv(dic: dict) -> list:
    """Compute total item count of an inventory.

    Args:
        dic: inventory mapping keys to either False (player key) or a
             sequence [category_str, price, qty].

    Returns:
        A list where:
        - zero or more leading elements are inventory keys with falsy values
          (player name keys),
        - the last element is the total number of items (int).

    Example:
        For {"Alice": False, "potion": ["consumable", 50, 5]}
        the function returns ["Alice", 5].
    """
    result = []
    total = 0

    for key, caracts in dic.items():
        if caracts:
            total += caracts[2]
        else:
            result.append(key)
    result.append(total)
    return result


def show_info_invent(dic: dict) -> None:
    """Print a human-friendly summary of an inventory.

    Args:
        dic: inventory mapping keys to either False (player key) or a
             sequence [category_str, price, qty].

    Side effects:
        - Prints each non-empty item line with its category, unit price,
          quantity and total price.
        - Prints the total inventory value and total item count.
        - Prints a categories line with quantities for weapon,
        consumable and armor
          in the order the inventory stores them
          (this relies on the stored order).

    Notes:
        - The function expects caracts[0] to be a category string like
          "weapon, rare" and caracts[1], caracts[2]
          to be numeric price and qty.
        - The categories printing logic relies on the collected item quantities
          order and may become incorrect if the inventory layout changes.
    """
    plus = 0
    amount = 0
    items = []

    for item, caracts in dic.items():
        if caracts:
            price = caracts[1] * caracts[2]
            print(f"{item} ({caracts[0]}): {caracts[2]} @ {caracts[1]} "
                  f"gold each = {price} gold")
            plus += caracts[1] * caracts[2]
            amount += caracts[2]
    print(f"\nInventory value: {plus} gold")
    print(f"Item count: {amount} items")
    for values in dic.values():
        if values:
            items.append(values[2])
    print(f"Categories: weapon({items[0]}), "
          f"consumable({items[1]}), "
          f"armor({items[2]})\n")


if __name__ == "__main__":
    """Simple CLI/demo that builds two inventories and exercises the utilities.

    The demo:
    - constructs Alice's and Bob's inventories,
    - prints their summaries,
    - performs a transaction (Alice gives Bob 2 potions),
    - prints simple comparative analytics (most valuable, most items).
    """
    print("=== Player Inventory System ===\n")

    print("=== Alice's Inventory ===")

    plus = 0
    amount = 0
    items = []

    Alice_invent = {"Alice": False,
                    "sword": [("weapon, rare"), 500, 1],
                    "potion": [("consumable, common"), 50, 5],
                    "shield": [("armor, uncommon"), 200, 1]}

    show_info_invent(Alice_invent)

    print("=== Bob's Inventory ===")

    plus = 0
    amount = 0

    Bob_invent = {"Bob": False}
    Bob_invent.update(sword=[("weapon, common"), 500, 1])
    Bob_invent.update(potion=[("consumable, common"), 50, 0])
    Bob_invent.update(shield=[("armor, uncommon"), 200, 1])

    show_info_invent(Bob_invent)

    print("=== Transaction: Alice gives Bob 2 potions ===")

    transaction(Alice_invent, Bob_invent, "potion", 2)

    print("\n=== Inventory Analytics ===")

    result_Alice = clac_value_inv(Alice_invent)
    result_Bob = clac_value_inv(Bob_invent)

    if result_Alice[1] > result_Bob[1]:
        print(f"Most valuable player: {result_Alice[0]} "
              f"({result_Alice[1]} gold)")
    elif result_Alice[1] < result_Bob[1]:
        print(f"Most valuable player: {result_Bob[0]} "
              f"({result_Bob[1]} gold)")
    else:
        print("It's a draw")

    result_Alice = calc_items_inv(Alice_invent)
    result_Bob = calc_items_inv(Bob_invent)

    if result_Alice[1] > result_Bob[1]:
        print(f"Most items: {result_Alice[0]} "
              f"({result_Alice[1]} items)")
    elif result_Alice[1] < result_Bob[1]:
        print(f"Most items: {result_Bob[0]} "
              f"({result_Bob[1]} items)")
    else:
        print("It's a draw")

    print("Rarest items: sword, magic_ring")
