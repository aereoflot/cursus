from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import deck
from ex1.SpellCard import SpellCard

if __name__ == "__main__":

    print("\n=== DataDeck Deck Builder ===")

    light = SpellCard("Lightning Bolt", 3, "Common", "damage")

    mana_cris = ArtifactCard("Mana Crystal",
                             2,
                             "Common",
                             5,
                             "Permanent: +1 mana per turn")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    game_state = {"criature": "Creature summoned to battlefield",
                  "artifact": "Permanent: +1 mana per turn",
                  "spell": "Deal 3 damage to target"}

    print("\nBuilding deck with different card types...")

    my_cards = deck()

    my_cards.add_card(light)
    my_cards.add_card(mana_cris)
    my_cards.add_card(dragon)

    print(f"Deck stats: {my_cards.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    print(f"\nDrew: {light.name} (Spell)")
    print(f"Play result: {light.play(game_state)}")

    print(f"\nDrew: {mana_cris.name} (Artifact)")
    print(f"Play result: {mana_cris.play(game_state)}")

    print(f"\nDrew: {dragon.name} (Creature)")
    print(f"Play result: {dragon.play(game_state)}")

    msg = "Polymorphism in action: Same interface, different behaviors!"
    print(f"\n{msg}")
