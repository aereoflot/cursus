
from ex0.Card import Card


class SpellCard(Card):
    """Card representing a spell with an effect type."""

    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str):
        """Initialize spell card with effect type."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Play spell card and return game state update."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state["spell"]
        }

    def resolve_effect(self, targets: list) -> dict:
        """Resolve spell effect on target list."""
        result = {}
        result[self.name] = f"{self.name}`s effect has started"
        if self.effect_type == "damage":
            for target in targets:
                if target.heal - 3 <= 0:
                    result[target.name] = "die"
                else:
                    result[target.name] = "health -3"
        elif self.effect_type == "heal":
            for target in targets:
                result[target.name] = "health +3"
        elif self.effect_type == "buff":
            for target in targets:
                result[target.name] = "damage +2"
        elif self.effect_type == "debuff":
            for target in targets:
                result[target.name] = "damage -2"
        return result
