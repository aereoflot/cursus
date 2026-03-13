
from abc import ABC


class GameStrategy(ABC):
    """Abstract strategy for game turn execution."""

    def __init__(self):
        """Initialize game strategy."""
        pass

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute turn with given hand and battlefield."""
        pass

    def get_strategy_name(self) -> str:
        """Return strategy name."""
        pass

    def prioritize_targets(self, avialable_targets: list) -> list:
        """Prioritize targets based on strategy."""
        pass
