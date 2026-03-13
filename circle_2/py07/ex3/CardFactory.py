
from abc import ABC
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating themed card collections."""

    def __init__(self):
        """Initialize card factory."""
        pass

    def create_creature(self, name_or_power) -> Card:
        """Create and return a creature card."""
        pass

    def create_spell(self, name_or_power) -> Card:
        """Create and return a spell card."""
        pass

    def create_artifacts(self, name_power) -> Card:
        """Create and return an artifact card."""
        pass

    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck of specified size."""
        pass

    def get_supported_types(self) -> dict:
        """Return supported card types."""
        pass
