
from abc import ABC


class Combatable(ABC):
    """Abstract mixin for entities that can engage in combat."""

    def __init__(self, health: int,
                 damage: int,
                 defense: int):
        """Initialize combatable entity."""
        self.health = health
        self.damage = damage
        self.defense = defense

    def attack(self, target) -> dict:
        """Attack target entity and return combat result."""
        pass

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        pass

    def get_combat_stats(self) -> dict:
        """Return combat statistics for this entity."""
        pass
