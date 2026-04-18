
from typing import Callable


def mage_counter() -> Callable:

    count = 0

    def countable() -> int:
        nonlocal count
        count += 1
        return count
    return countable


def spell_accumulator(initial_power: int) -> Callable:

    power = initial_power

    def calc_power(giv_power: int) -> int:
        nonlocal power
        power += giv_power
        return power
    return calc_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def item_enchanted(item: str) -> str:
        return enchantment_type + " " + item
    return item_enchanted


def memory_vault() -> dict[str, Callable]:

    result = {}

    def store(key: str, value: str):
        result[key] = value

    def recall(key: str) -> str:
        try:
            return result[key]
        except KeyError:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main():

    print("\nTesting mage counter...")

    counter = mage_counter()
    count = 1
    for _ in range(3):
        print(f"Call {count}: {counter()}")
        count += 1

    print("\nTesting spell accumulator")

    power = spell_accumulator(10)
    add = 4
    print(f"Initial power: {power(0)}")
    print(f"Adding {add} power: {power(add)}")
    add = 6
    print(f"Adding {add} power: {power(add)}")

    print("\nTesting enchantment factory...")

    item_enchanted = enchantment_factory("Flaming")
    print(item_enchanted("Sword"))
    item_enchanted = enchantment_factory("Frozen")
    print(item_enchanted("Shield"))

    print("\nTesting memory vault...")

    dic = memory_vault()

    print("Error:", dic["recall"]("ff"))

    dic["store"]("Potion", "Health +50")
    dic["store"]("Sword", "Damage +10")

    print(dic["recall"]("Potion"))


if __name__ == "__main__":
    main()
