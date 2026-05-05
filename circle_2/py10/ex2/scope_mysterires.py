
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

    def store(key: str, value: str) -> None:
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


def main() -> None:

    print("Testing mage counter...")

    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")

    power = spell_accumulator(100)
    base = power(0)
    print(f"Base {base}, add 20: {power(20)}")
    print(f"Base {base}, add 30: {power(30)}")

    print("\nTesting enchantment factory...")

    item_enchanted = enchantment_factory("Flaming")
    print(item_enchanted("Sword"))
    item_enchanted = enchantment_factory("Frozen")
    print(item_enchanted("Shield"))

    print("\nTesting memory vault...")

    dic = memory_vault()

    print("Store 'secret' = 42")

    dic["store"]("secret", "42")
    dic["store"]("Sword", "Damage +10")

    print(f"Recall 'secret': {dic['recall']('secret')}")
    print(f"Recall 'unknown': {dic['recall']('unknown')}")


if __name__ == "__main__":
    main()
