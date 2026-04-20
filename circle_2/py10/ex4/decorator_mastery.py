
import functools
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(obj: str) -> str:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(obj)
        final = time.time()
        print(f"Spell completed in {(final - start):.03} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(power: int) -> str:
            if power >= min_power:
                return func(power)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(focus: int, target: str) -> str:
            for trys in range(1, max_attempts + 1):
                try:
                    return func(focus, target)
                except ValueError:
                    focus -= 10
                    if trys == max_attempts:
                        return f"Spell casting failed after \
{max_attempts} attempts"
                    else:
                        print(f"Spell failed, retrying..., \
(attempt {trys}/{max_attempts})")
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:

        i = 0
        for _ in name:
            i += 1
        if i < 3:
            return False

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
        for let in name:
            if let not in alphabet:
                return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:

        @power_validator(10)
        def execute_cast(pwr) -> str:
            return f"Successfully cast {spell_name} with {pwr} power"
        return execute_cast(power)


def main():

    print("\nTesting spell timer...")

    def fireball(object: str) -> str:
        return f"{object} cast!"

    wrapper = spell_timer(fireball)

    print("Result:", wrapper("Fireball"))

    print("\nTesting power validator...")

    @power_validator(10)
    def attack(power: int) -> str:
        return f"Your {power} points of power are enough"

    print("With power=19:", attack(19))
    print("With power=9", attack(9))

    print("\nTesting retry spell...")

    @retry_spell(4)
    def trow_spell(focus: int, target: str):
        if focus < 20:
            return f"Spell throwed succesfully to {target}!!!!"
        else:
            raise ValueError

    print(f"{trow_spell(30, 'Dragon')}\n")
    print(trow_spell(70, "Dragon"))

    print("\nTesting MageGuild...")

    wizard = MageGuild()

    print(wizard.validate_mage_name("Fire Dragon"))
    print(wizard.validate_mage_name("AA"))

    print(wizard.cast_spell("Lightning", 15))
    print(wizard.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
