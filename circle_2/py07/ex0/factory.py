"""Module containing the abstract factory and concrete factories."""

from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating base and evolved creatures."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Creates the base form of the creature family."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Creates the evolved form of the creature family."""
        pass


class FlameFactory(CreatureFactory):
    """Factory for the Fire family creatures."""

    def create_base(self) -> Creature:
        """Returns a new Flameling."""
        return Flameling()

    def create_evolved(self) -> Creature:
        """Returns a new Pyrodon."""
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for the Water family creatures."""

    def create_base(self) -> Creature:
        """Returns a new Aquabub."""
        return Aquabub()

    def create_evolved(self) -> Creature:
        """Returns a new Torragon."""
        return Torragon()
