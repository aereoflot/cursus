"""Module containing creatures with combined traits from ex0 and ex1."""

from typing import Any
from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Concrete Sproutling creature with healing."""

    def __init__(self) -> None:
        """Initializes Sproutling."""
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        """Returns Sproutling's attack."""
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Any = None) -> str:
        """Returns Sproutling's healing action."""
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Concrete Bloomelle creature with healing."""

    def __init__(self) -> None:
        """Initializes Bloomelle."""
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        """Returns Bloomelle's attack."""
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Any = None) -> str:
        """Returns Bloomelle's healing action."""
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Concrete Shiftling creature with transformation."""

    def __init__(self) -> None:
        """Initializes Shiftling."""
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Returns attack string depending on the transformation state."""
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Triggers transformation state."""
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        """Reverts transformation state."""
        self.is_transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """Concrete Morphagon creature with transformation."""

    def __init__(self) -> None:
        """Initializes Morphagon."""
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Returns attack string depending on the transformation state."""
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """Triggers transformation state."""
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        """Reverts transformation state."""
        self.is_transformed = False
        return f"{self.name} stabilizes its form."
