
from ex0.Card import Card

class CreatureCard(Card):

    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state["criature"]
        }
        
    def get_card_info(self):
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def attack_target(self, target) -> dict:

        resolv = target.health - self.attack

        deal = True if resolv <= 0 else False

        return {
            "attacker": self.name,
            "target": target.name,
            "damege_dealt": self.attack,
            "combat_resolved": deal
        }
