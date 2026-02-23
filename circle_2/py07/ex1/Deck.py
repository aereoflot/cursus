
from ex0.Card import Card
import random
from typing import list, Optional

class deck:
    
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card: Card) -> bool:
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        from ex0.CreatureCard import CreatureCard
        from ex1.ArtifactCard import ArtifactCard
        from ex1.SpellCard import SpellCard
        
        total = len(self.cards)
        creatures = sum(1 for card in self.card if isinstance(card, CreatureCard))
        spells = sum(1 for card in self.card if isinstance(card, SpellCard))
        artifacts = sum(1 for card in self.card if isinstance(card, ArtifactCard))
        avg = sum(self.card for card in self.cards)
        avg = avg / total if total > 0 else 0        
