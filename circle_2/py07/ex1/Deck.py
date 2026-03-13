
from ex0.Card import Card
import random


class deck:
    """Collection of cards representing a player's deck."""

    def __init__(self):
        """Initialize empty deck."""
        self.cards = []

    def add_card(self, card: Card) -> None:
        """Add card to deck."""
        self.cards.append(card)

    def remove_card(self, card: Card) -> bool:
        """Remove card from deck and return success status."""
        if card in self.cards:
            self.cards.remove(card)
            return True
        return False

    def shuffle(self) -> None:
        """Shuffle deck cards in random order."""
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw and remove first card from deck."""
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        """Return statistics about deck composition."""
        from ex0.CreatureCard import CreatureCard
        from ex1.ArtifactCard import ArtifactCard
        from ex1.SpellCard import SpellCard

        total = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0

        for card in self.cards:
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, ArtifactCard):
                spells += 1
            elif isinstance(card, SpellCard):
                artifacts += 1
        avg = sum(card.cost for card in self.cards)
        avg = avg / total if total > 0 else 0

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": int(avg * 10) / 10}
