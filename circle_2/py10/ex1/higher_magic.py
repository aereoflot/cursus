
from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    return lambda target, pw: (spell1(target, pw), spell2(target, pw))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    return lambda: base_spell(4) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    return lambda num, tg: (
        spell(num, tg)
        if condition(num, tg)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable]) -> Callable:

    return lambda tg, pw: [spell(tg, pw) for spell in spells]


def main() -> None:

    print("\nTesting spell Combiner...")

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    combo_fun = spell_combiner(fireball, heal)
    result = combo_fun("Dragon", 3)

    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")

    def fireball(damage: int) -> int:
        return 14 - damage

    amplified = power_amplifier(fireball, 3)

    print(f"Original: {fireball(4)}, "
          f"Amplified: {amplified()}")

    print("\nTesting conditional caster...")

    def condition(tg: str, num: int) -> bool:
        return True if num > 0 else False

    def have_cards(tg: str, power: int) -> str:
        return f"You have {power} cards aviable."

    msg = conditional_caster(condition, have_cards)

    print(msg("Dragon", 5))

    print("\nTesting spell sequence...")

    def spell1(target: str, power: int) -> str:
        return f"{target} on your vision"

    def spell2(target: str, power: int) -> str:
        return f"{target} targeted"

    def spell3(target: str, power: int) -> str:
        return f"{target} hit"

    spells = [
        spell1,
        spell2,
        spell3
    ]

    sequence = spell_sequence(spells)
    print(sequence("Dragon", 0))


if __name__ == "__main__":
    main()
