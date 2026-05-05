
import operator
import functools
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

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


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def dispatcher(spell_data: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(damage: int) -> str:
        return f"{damage} damage"

    @dispatcher.register(str)
    def _(enchantment: str) -> str:
        return f"{enchantment}"

    @dispatcher.register(list)
    def _(multi_spells: list) -> str:
        count = 0
        for _ in multi_spells:
            count += 1
        return f"{count} spells"

    return dispatcher


def main() -> None:

    print("\nTesting spell reducer...")

    spells = [40, 30, 20, 10]

    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "mul"))
    print("Max:", spell_reducer(spells, "max"))
    print("No spells:", spell_reducer([], "add"))
    print("Unknown:", spell_reducer(spells, "Unknown"))

    print("\nTesting partial enchanter...")

    def base(power, element, target) -> str:
        return f"Element: {element}, Power: {power}, Target: {target}"

    dic = partial_enchanter(base)

    for element in dic.values():
        print(element("Dragon"))

    print("\nTesting memorized fibonacci...")

    nums = [0, 1, 10, 15]

    for num in nums:
        print(f"fib({num}):", memoized_fibonacci(num))
        print("Cache info:", memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()

    print("Damage spell:", dispatcher(42))
    print("Enchantment:", dispatcher("fireball"))
    print("Multi-cast:", dispatcher(["Fire", 11, "Light"]))
    print(dispatcher(3.5))


if __name__ == "__main__":
    main()
