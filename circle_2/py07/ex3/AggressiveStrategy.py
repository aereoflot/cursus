
from ex0.CreatureCard import CreatureCard
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Strategy that prioritizes aggressive plays and damage."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute aggressive turn with all available cards."""
        hand_name = []
        mana = 0
        damage_attack = 0

        for card in hand:
            hand_name.append(card.name)
            mana += card.cost
            if isinstance(card, CreatureCard):
                damage_attack += card.attack

        enemy_life = 0
        target_name = []

        for target in battlefield:
            target_name.append(target.name)
            if isinstance(target, CreatureCard):
                enemy_life += target.health

        if enemy_life - damage_attack <= 0:
            damage = enemy_life
        else:
            damage = damage_attack

        return {
            "cards_played": hand_name,
            "mana_user": mana,
            "targets_attacked": target_name,
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        """Return strategy identifier."""
        return "AggressiveStrategy"

    def prioritize_targets(self, avialable_targets: list) -> list:
        """Prioritize targets by health lowest to highest."""
        targets = []

        for target in avialable_targets:
            if isinstance(target, CreatureCard):
                targets.append(target)

        return sorted(targets, key=lambda target: target.health)
