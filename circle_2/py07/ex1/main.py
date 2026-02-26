
from pickle import decode_long
from platform import architecture
from ..ex0 import CreatureCard
from ex1.ArtifactCard import artifactCard
from ex1.Deck import deck
from ex1.SpellCard import spellCard

if __name__ == "__main__":

    print("\n=== DataDeck Deck Builder ===")

    light = spellCard("Lightning Bolt", 3, "Common", "damage")

    mana_cris = artifactCard("Mana Crystal", 2, "Common", 5, "Permanent: +1 mana per turn")

    dragon = ("Fire Dragon", 5, "Legendary", 7, 5)

    game_state = {"criature": "Creature summoned to battlefield",
    "artifact": "Permanent: +1 mana per turn",
    "spell": "Deal 3 damage to target"
    }

    print("\nBuilding deck with different card types...")

    my_cards = deck()

    my_cards.add_card(light)
    my_cards.add_card(mana_cris)
    my_cards.add_card(dragon)

    my_cards.get_deck_stats()
