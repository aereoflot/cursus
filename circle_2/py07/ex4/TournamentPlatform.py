
from .TournamentCard import TournamentCard
from typing import List


class TournamentPlatform:
    """Platform managing tournament matches and rankings."""

    def __init__(self, players: List[TournamentCard]):
        """Initialize tournament platform with player list."""
        self.players = players
        self.machs = 0
        self.status = "idle"

    def register_card(self, card: TournamentCard) -> str:
        """Register new tournament card in platform."""
        self.status = "registering"

        try:

            if not isinstance(card, TournamentCard):
                raise TypeError("Card added must be TournamentCard type.")

            for player in self.players:
                if player.id == card.id:
                    raise ValueError("Card already registered.")

            self.players.append(card)
            return "Card added successfully!!"

        except (TypeError, ValueError) as e:
            return f"Error: {e}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Create and execute tournament match."""
        for player in self.players:
            if player.id == card1_id:
                player1 = player
            elif player.id == card2_id:
                player2 = player

        result = player1.play({"player": player2})

        self.machs += 1
        self.status = "active"

        return result

    def get_leaderboard(self) -> List:
        """Return current leaderboard standings."""
        return self.players

    def generate_tournament_report(self) -> dict:
        """Generate comprehensive tournament report."""
        total = 0

        for player in self.players:
            total += player.rating

        if len(self.players) == 0:
            average = 0
        else:
            average = total / len(self.players)

        return {
            "total_cards": len(self.players),
            "matches_played": self.machs,
            "avg_rating": int(average),
            "platform_status": self.status}
