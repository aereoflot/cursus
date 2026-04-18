
import operator
import functools
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:

    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "mul":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return functools.reduce(max, spells)
    elif operation == "min":
        return functools.reduce(min, spells)
    else:
        print("Operation not found")
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    fire_enchant = functools.partial(base_enchantment, 50, "Fire")
    ice_enchant = functools.partial(base_enchantment, 50, "Ice")
    lightning_enchant = functools.partial(base_enchantment, 50, "Lightning")

    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:

    @functools.singledispatch
    def dispatcher(spell_data):
        return f"Unknown spell form: {spell_data}"

    @dispatcher.register(int)
    def _(damage: int):
        return f"Casting damage spell: {damage} HP"

    @dispatcher.register(str)
    def _(enchantment: str):
        return f"Applying enchantment: {enchantment}"

    @dispatcher.register(list)
    def _(multi_spells: list):
        results = [dispatcher(s) for s in multi_spells]
        return f"Multi-cast: {results}"

    return dispatcher


def main():

    print("\nTesting spell reducer...")

    spells = [40, 30, 20, 10]

    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "mul"))
    print("Max:", spell_reducer(spells, "max"))
    print("Max:", spell_reducer(spells, "resta"))

    print("\nTesting partial enchanter...")

    def base(power, element, target):
        return f"Element: {element}, Power: {power}, Target: {target}"

    dic = partial_enchanter(base)

    for element in dic.values():
        print(element("Dragon"))

    print("\nTesting memorized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(30))

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()

    print("Int:", dispatcher(10))
    print("Str:", dispatcher("Ice"))
    print("List:", dispatcher(["Fire", 11, "Light"]))
    print("Unknown:", dispatcher(3.5))


if __name__ == "__main__":
    main()
