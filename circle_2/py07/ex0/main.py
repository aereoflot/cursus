
from CreatureCard import CreatureCard

if __name__ == "__main__":

    print("\n=== DataDeck Card Foundation ===")
    
    print("\nTesting Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 1, "common", 2, 1)
    king = CreatureCard("King", 4, "rare", 4, 5)
    queen = CreatureCard("Queen", 2, "common", 3, 2)
    
    print("\nCreatureCard Info:")
    info_dragon = dragon.get_card_info()
    print(info_dragon)

    print(f"\nPlaying {dragon.name} with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    game_satate = {"criature": "Creature summoned to battlefield"}
    print(f"Play result: {dragon.play(game_satate)}")

    print(f"\n{dragon.name} attacks {goblin.name}:")
    print(f"Attack result: {dragon.attack_target(goblin)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {king.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")    
