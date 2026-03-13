
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from .Rankable import Rankable
from typing import List


class TournamentCard(Card, Combatable, Rankable):
    """Tournament card combining card and ranking capabilities."""

    def __init__(self, id: str,
                 record: List[int],
                 rating: int,
                 card: CreatureCard):
        """Initialize tournament card with id record rating."""
        Rankable.__init__(self, id, record, rating)
        self.trecord = [0, 0]
        self.card = card
        pass

    def play(self, game_state: dict) -> dict:
        """Play tournament card and update rating."""
        player2 = game_state["player"]

        attack_result = self.attack(player2)

        if attack_result["draw"]:
            if self.rating >= player2.rating:
                winner = self
                loser = player2
            else:
                winner = player2
                loser = self

        else:
            winner = attack_result["winner"]
            self.trecord[0] += 1
            self.record[0] += 1

            loser = attack_result["loser"]
            player2.trecord[1] += 1
            player2.record[1] += 1

            win_rating = winner.calculate_rating()
            los_rating = loser.calculate_rating()

        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": win_rating,
            "loser_rating": los_rating}

    def attack(self, target) -> dict:
        """Attack target card in tournament match."""
        card1 = self.card
        card2 = target.card

        draw = False

        if (card1.attack - card2.health) >= 0:
            winner = self
            loser = target
        elif (card1.attack - card2.health) == 0:
            draw = True
            return {"draw": draw}

        else:
            winner = target
            loser = self

        return {
            "winner": winner,
            "loser": loser,
            "draw": draw}

    def calculate_rating(self) -> int:
        """Calculate rating from wins and losses."""
        self.rating = (self.record[0] * 16) - (self.record[1] * 16)
        return self.rating

    def get_tournament_stats(self) -> dict:
        """Return tournament statistics."""
        return {
            "ID": self.id,
            "wins": self.record[0],
            "losses": self.record[1],
            "rating": self.rating}
