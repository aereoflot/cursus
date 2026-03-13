
from .CardFactory import CardFactory
from ex0 import CreatureCard
from ex1 import SpellCard, ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    """Factory for creating fantasy-themed cards."""

    def __init__(self):
        """Initialize fantasy factory with card registries."""
        self.creatures_registry = {
            "dragon": {"cost": 5,
                       "rarity": "Legendary",
                       "attack": 7,
                       "health": 5},
            "goblin": {"cost": 2, "rarity": "Common", "attack": 2,
                       "health": 1}
        }

        self.spells_registry = {
            "fireball": {"cost": 3,
                         "rarity": "Common",
                         "effect_type": "damage"}
        }

        self.artifacts_registry = {
            "mana_ring": {"cost": 2,
                          "rarity": "Common",
                          "effect": "+1 mana per turn"}
        }

        self.rare = ("common", "rare", "legendary", "special")

    def create_creature(self, creature_name: str) -> CreatureCard:
        """Create a fantasy creature card."""
        if creature_name not in self.creatures_registry:
            raise ValueError(f"Creature '{creature_name}' not registered")

        return CreatureCard(
            name=creature_name,
            cost=random.randint(2, 9),
            rarity=random.choice(self.rare),
            attack=random.randint(1, 6),
            health=random.randint(3, 9)
        )

    def create_spell(self, spell_name: str) -> SpellCard:
        """Create an elemental spell card."""
        if spell_name not in self.spells_registry:
            raise ValueError(f"Spell '{spell_name}' not registered")

        effect_type = ("damage", "health", "buff", "debuff")

        return SpellCard(
            name=spell_name,
            cost=random.randint(2, 9),
            rarity=random.choice(self.rare),
            effect_type=random.choice(effect_type),
        )

    def create_artifact(self, artifact_name: str) -> ArtifactCard:
        """Create a magical artifact card."""
        if artifact_name not in self.artifacts_registry:
            raise ValueError(
                f"Artifact '{artifact_name}' not registered")

        effect = (
            "Permanent: +1 mana per turn",
            "Permanent: +2 attack to equipped creature",
            "Permanent: Draw an extra card each turn",
            "Permanent: +3 health to all friendly creatures",
            "Permanent: +1 cost reduction to all cards"
        )

        return ArtifactCard(
            name=artifact_name,
            cost=random.randint(2, 9),
            rarity=random.choice(self.rare),
            effect=random.choice(effect)
        )

    def register_creature(self, name: str, stats: dict) -> None:
        """Register a new creature type."""
        self.creatures_registry[name] = stats

    def register_spell(self, name: str, stats: dict) -> None:
        """Register a new spell type."""
        self.spells_registry[name] = stats

    def register_artifact(self, name: str, stats: dict) -> None:
        """Register a new artifact type."""
        self.artifacts_registry[name] = stats

    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck with random cards of size."""
        deck = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }

        creatures = list(self.creatures_registry.keys())
        spells = list(self.spells_registry.keys())
        artifacts = list(self.artifacts_registry.keys())

        cards_added = 0
        while cards_added < size:
            choice = random.randint(0, 2)

            if choice == 0 and creatures:
                card = self.create_creature(random.choice(creatures))
                deck["creatures"].append(card)
                cards_added += 1
            elif choice == 1 and spells:
                card = self.create_spell(random.choice(spells))
                deck["spells"].append(card)
                cards_added += 1
            elif choice == 2 and artifacts:
                card = self.create_artifact(random.choice(artifacts))
                deck["artifacts"].append(card)
                cards_added += 1

        return deck

    def get_supported_types(self) -> dict:
        """Get all supported card types in this factory."""
        return {
            "creatures": list(self.creatures_registry.keys()),
            "spells": list(self.spells_registry.keys()),
            "artifacts": list(self.artifacts_registry.keys())
        }


def creatures_types() -> list:
    """Return list of available creature types."""
    factory = FantasyCardFactory()
    return list(factory.creatures_registry.keys())


def spells_types() -> list:
    """Return list of available spell types."""
    factory = FantasyCardFactory()
    return list(factory.spells_registry.keys())


def artifacts_types() -> list:
    """Return list of available artifact types."""
    factory = FantasyCardFactory()
    return list(factory.artifacts_registry.keys())
