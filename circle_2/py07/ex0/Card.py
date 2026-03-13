
from abc import ABC


class Card(ABC):
    """Base abstract class for all card types."""

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str):
        """Initialize card with name, cost, and rarity."""
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        """Play the card and return updated game state."""
        pass

    def get_card_info(self) -> dict:
        """Return card information as dictionary."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if card can be played with available mana."""
        if self.cost <= available_mana:
            return True
        else:
            return False
