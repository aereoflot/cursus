
from ex0.Card import Card

class ArtifactCard(Card):
    
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect


    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state["artifact"]
        }


    def activate_ability(self) -> dict:
        if self.durability > 0:

            action_description = f"Habilidad '{self.effect}' activada."

            self.durability -= 1

            is_destroyed = (self.durability == 0)

            return {
                'artifact_name': self.name,
                'effect_description': action_description,
                'durability_remaining': self.durability,
                'destroyed': is_destroyed,
                'status': 'Ability Activated'
            }
        else:
            return {
                'artifact_name': self.name,
                'effect_description': "You don`t have more uses",
                'durability_remaining': 0,
                'destroyed': True,
                'status': 'Destroyed'
            }
