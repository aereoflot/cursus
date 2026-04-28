
"""Module containing the base abstract Creature
    and concrete implementations."""

from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for all creatures."""

    def __init__(self, name: str, type_: str) -> None:
        """Initializes a Creature with a name and type."""
        self.name = name
        self.type_ = type_

    @abstractmethod
    def attack(self) -> str:
        """Abstract method for a creature's attack."""
        pass

    def describe(self) -> str:
        """Returns a standard description of the creature."""
        return f"{self.name} is a {self.type_} type Creature"


class Flameling(Creature):
    """Concrete Flameling creature."""

    def __init__(self) -> None:
        """Initializes Flameling."""
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Returns Flameling's attack string."""
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """Concrete Pyrodon creature."""

    def __init__(self) -> None:
        """Initializes Pyrodon."""
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """Returns Pyrodon's attack string."""
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """Concrete Aquabub creature."""

    def __init__(self) -> None:
        """Initializes Aquabub."""
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """Returns Aquabub's attack string."""
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """Concrete Torragon creature."""

    def __init__(self) -> None:
        """Initializes Torragon."""
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """Returns Torragon's attack string."""
        return f"{self.name} uses Hydro Pump!"
