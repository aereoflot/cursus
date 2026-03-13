
from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    """Engine that orchestrates card and strategy systems."""

    def __init__(self):
        """Initialize game engine with empty configuration."""
        self.factory = None
        self.strategy = None
        self.turn_count = 0
        self.status = "idle"

    def configure_engine(self,
                         factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Configure engine with factory and strategy."""
        self.factory = factory
        self.strategy = strategy
        self.status = "configured"

    def simulate_turn(self) -> dict:
        """Simulate a game turn using configured strategy."""
        if self.factory is None or self.strategy is None:
            raise ValueError("Factory or Strategy was empty")

        self.turn_count += 1
        self.status = "simulating"

        hand = []
        if self.factory:
            hand.append(self.factory.create_creature("walf"))
            hand.append(self.factory.create_spell("megan"))

        battlefield = []
        if self.factory:
            battlefield.append(self.factory.create_creature("demon"))
            battlefield.append(self.factory.create_creature("lion"))

        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.status = "simulated"
        return turn_result

    def get_engine_status(self) -> dict:
        """Get current engine status and configuration."""
        if self.strategy:
            strategy_name = self.strategy.get_strategy_name()
        else:
            strategy_name = None

        return {
            "status": self.status,
            "turn_count": self.turn_count,
            "factory_configured": self.factory is not None,
            "strategy_configured": self.strategy is not None,
            "strategy_name": strategy_name
        }
