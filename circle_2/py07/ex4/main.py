
from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


if __name__ == "__main__":

    print("\n=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...")

    interface = [Card.__name__,
                 Combatable.__name__,
                 Rankable.__name__]

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    tdragon = TournamentCard("dragon_001",
                             [100, 25],
                             1200,
                             dragon)

    print(f"\n{dragon.name} (ID: {tdragon.id})")
    print(f"- Interfaces: {interface}")
    print(f"- Rating: {tdragon.rating}")
    print(f"- Record: {tdragon.trecord[0]}-{tdragon.trecord[1]}")

    wizard = CreatureCard("Ice Wizard", 4, "Rare", 3, 4)

    twizard = TournamentCard("wizrard_001",
                             [100, 28],
                             1150,
                             wizard)

    print(f"\n{wizard.name} (ID: {twizard.id})")
    print(f"- Interfaces: {interface}")
    print(f"- Rating: {twizard.rating}")
    print(f"- Record: {twizard.trecord[0]}-{twizard.trecord[1]}")

    tournament = TournamentPlatform([tdragon, twizard])

    print("\nCreating tournament match...")
    print(f"Match result: {tournament.create_match(tdragon.id, twizard.id)}")

    print("\nTournament Leaderboard:")
    players = tournament.get_leaderboard()

    num = 1
    for player in players:
        print(f"{num}. {player.card.name} - Rating {player.rating} \
({player.trecord[0]}-{player.trecord[1]})")
        num += 1

    print(f"\nPlatform Report:\n{tournament.generate_tournament_report()}")

    print("\n=== Tournament Platform Successfully Deployed! ===\n\
All abstract patterns working together harmoniously!")
