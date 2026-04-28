"""Module containing factories for creatures with special capabilities."""

from ex0.factory import CreatureFactory
from ex0.creature import Creature
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """Factory for the Healing family creatures."""

    def create_base(self) -> Creature:
        """Returns a new Sproutling."""
        return Sproutling()

    def create_evolved(self) -> Creature:
        """Returns a new Bloomelle."""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Factory for the Transforming family creatures."""

    def create_base(self) -> Creature:
        """Returns a new Shiftling."""
        return Shiftling()

    def create_evolved(self) -> Creature:
        """Returns a new Morphagon."""
        return Morphagon()
