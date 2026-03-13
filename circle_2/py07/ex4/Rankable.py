
from abc import ABC
from typing import List


class Rankable(ABC):
    """Abstract base class for rankable competitive entities."""

    def __init__(self, id: str,
                 record: List[int],
                 rating: int):
        """Initialize rankable entity with id record and rating."""
        self.id = id
        self.record = record
        self.rating = rating

    def calculate_rating(self) -> int:
        """Calculate and return current rating."""
        pass

    def update_wins(self, wins: int) -> None:
        """Record wins in tournament record."""
        pass

    def update_losses(self, losses: int) -> None:
        """Record losses in tournament record."""
        pass

    def get_rank_info(self) -> dict:
        """Return ranking information."""
        pass
