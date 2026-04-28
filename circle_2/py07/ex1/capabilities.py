"""Module defining independent creature capabilities."""

from abc import ABC, abstractmethod
from typing import Any


class HealCapability(ABC):
    """Abstract capability for healing actions."""

    @abstractmethod
    def heal(self, target: Any = None) -> str:
        """Performs a healing action."""
        pass


class TransformCapability(ABC):
    """Abstract capability for transforming actions."""

    def __init__(self) -> None:
        """Initializes the persistent state attribute."""
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Performs a transformation, altering the state."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Reverts a transformation, restoring the state."""
        pass
