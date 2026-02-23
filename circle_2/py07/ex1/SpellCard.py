
from ex0.Card import Card

class SpellCard(Card):
    
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
    
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            self.name: game_state[self.name]
        }
        
    def resolve_effect(self, targets: list):
        ...#creala t q a mi me da la risa 🤕
