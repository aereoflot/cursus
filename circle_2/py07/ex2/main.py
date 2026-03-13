
from .EliteCard import EliteCard

if __name__ == "__main__":

    print("\n=== DataDeck Ability System ===")

    Arcane = EliteCard("Arcane Warrior", 4, "Legendary", 5, 5, 3, 3)

    print("\nEliteCard capabilities:")

    card_cap = ["play", "get_card_info", "is_playable"]
    combat_cap = ["attack", "defend", "get_combat_stats"]
    magical_cap = ["cast_spell", "channel_mana", "get_magic_stats"]

    print(f"- Card: {card_cap}\n\
- Combatable: {combat_cap}\n\
- Magical: {magical_cap}")

    print(f"\nPlaying {Arcane.name} (Elite Card)")

    print("\nCombat phase:")

    print(f"Attack result: {Arcane.attack('Enemy')}")
    print(f"Defense result: {Arcane.defend(5)}")

    print("\nMagic phase:")

    enemys = ["Enemy1", "Enemy2"]

    print(f"Spell cast: {Arcane.cast_spell('Fireball', enemys)}")
    print(f"Mana channel: {Arcane.channel_mana(4)}")

    print("\nMultiple interface implementation successful!")
