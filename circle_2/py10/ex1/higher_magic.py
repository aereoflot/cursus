
from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    return lambda target: [spell1(target), spell2(target)]


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    return lambda: base_spell(4) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    return lambda num: spell(num) if condition(num) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:

    return lambda str: [spell(str) for spell in spells]


def main():

    print("\nTesting spell Combiner...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    combo_fun = spell_combiner(fireball, heal)

    combo = combo_fun("Dragon")[0] + ", " + combo_fun("Dragon")[1]
    print("Combined spell result:", combo)

    print("\nTesting power amplifier...")

    def fireball(damage: int) -> int:
        return 14 - damage

    amplified = power_amplifier(fireball, 3)

    print(f"Original: {fireball(4)}, "
          f"Amplified: {amplified()}")

    print("\nTesting conditional caster...")

    def condition(num: int) -> bool:
        return True if num > 0 else False

    def have_cards(num: int) -> str:
        return f"You have {num} cards aviable."

    msg = conditional_caster(condition, have_cards)

    print(msg(5))

    print("\nTesting spell sequence...")

    def spell1(str: str) -> str:
        return f"{str} strikes with precision"

    def spell2(str: str) -> str:
        return f"{str} radiates pure energy"

    def spell3(str: str) -> str:
        return f"{str} echoes through the air"

    spells = [
        spell1,
        spell2,
        spell3
    ]

    returns = spell_sequence(spells)
    print(returns("Fireball"))


if __name__ == "__main__":
    main()
