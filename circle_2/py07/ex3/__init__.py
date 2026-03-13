
"""Factory and strategy patterns for game engine."""
from .FantasyCardFactory import creatures_types, spells_types, artifacts_types
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine

__all__ = [creatures_types, spells_types, artifacts_types]
__all__ = [AggressiveStrategy, GameEngine]
