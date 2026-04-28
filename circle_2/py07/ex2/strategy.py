"""Module containing the abstract strategy pattern components."""

from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class StrategyError(Exception):
    """Exception raised for invalid strategy combinations."""
    pass


class BattleStrategy(ABC):
    """Abstract base class for battle strategies."""

    @abstractmethod
    def act(self, creature: Creature) -> str:
        """Executes the strategy sequence for the given creature."""
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Checks if a creature is suitable for this strategy."""
        pass


class NormalStrategy(BattleStrategy):
    """Strategy that just performs a normal attack."""

    def is_valid(self, creature: Creature) -> bool:
        """Checks if creature is valid (True for all Creatures)."""
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        """Returns the normal attack string."""
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    """Strategy that transforms, attacks, and reverts."""

    def is_valid(self, creature: Creature) -> bool:
        """Checks if creature has transformation capabilities."""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        """Executes the aggressive action sequence."""
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy"
            )

        result = []
        if isinstance(creature, TransformCapability):
            result.append(creature.transform())
            result.append(creature.attack())
            result.append(creature.revert())

        return "\n".join(result)


class DefensiveStrategy(BattleStrategy):
    """Strategy that attacks and then heals."""

    def is_valid(self, creature: Creature) -> bool:
        """Checks if creature has healing capabilities."""
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        """Executes the defensive action sequence."""
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "defensive strategy"
            )

        result = []
        result.append(creature.attack())
        if isinstance(creature, HealCapability):
            result.append(creature.heal())

        return "\n".join(result)
