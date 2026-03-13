
from .FantasyCardFactory import creatures_types, spells_types, artifacts_types
from .AggressiveStrategy import AggressiveStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


if __name__ == "__main__":

    print("\n=== DataDeck Game Engine ===")

    factory = "FantasyCardFactory"

    strat = AggressiveStrategy()

    print("\nConfiguring Fantasy Card Game...")

    print(f"Factory: {factory}")
    print(f"Strategy: {strat.get_strategy_name()}")

    aviable_types = {
        "creatures": creatures_types(),
        "spells": spells_types(),
        "artifacts": artifacts_types()
    }

    print(f"Avialable types: {aviable_types}")

    print("\nSimulating aggressive turn...")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 8, 1)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")

    hand_show = [f"{dragon.name} ({dragon.cost})",
                 f"{goblin.name} ({goblin.cost})",
                 f"{bolt.name} ({bolt.cost})"]

    print(f"Hand: {hand_show}")

    print("\nTurn execution:")
    print(f"Strategy: {strat.get_strategy_name()}")

    hand_attack = [goblin, bolt]

    enemy = CreatureCard("Enemy Player", 4, "Legendary", 8, 10)
    battelfield = [enemy]

    print(f"Actions {strat.execute_turn(hand_attack, battelfield)}")

    print("\nAbstract Factory + Strategy Pattern: \
Maximum flexibility achieved!")
