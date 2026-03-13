
from abc import ABC


class Magical(ABC):
    """Abstract mixin for entities with magical abilities."""

    def __init__(self, generate_mana: int):
        """Initialize magical entity."""
        self.gen_mana = generate_mana

    def cast_spell(self,
                   spell_name: str,
                   targets: list) -> dict:
        """Cast spell on targets and return spell result."""
        pass

    def channel_mana(self, amount: int) -> dict:
        """Channel mana and return channeled amount."""
        pass

    def get_magic_stats(self) -> dict:
        """Return magical statistics for this entity."""
        pass
