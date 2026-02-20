"""Achievement tracker utilities.

This module defines a minimal Achievements class and a small demo that
creates several player instances and performs simple set-based analytics.

It demonstrates:
- storing a player's achievements,
- printing them,
- computing unique achievements across players,
- computing common and rare achievements using set operations.
"""


class Achievements:
    """Simple container for a player's achievement list.

    Attributes:
        name (str): Player name.
        achieves (list[str]): List of achievement identifiers for the player.

    Note:
        The class provides a single convenience method `show_achives`
        that prints
        the player's achievements. The method name preserves the original
        spelling used in the project.
    """

    def __init__(self, name: str, achieves: list):
        """Initialize an Achievements instance.

        Args:
            name: Player name.
            achieves: List of achievement identifiers (strings).
        """
        self.achieves = achieves
        self.name = name

    def show_achives(self):
        """Print the player's achievements.

        Side effects:
            Prints a single formatted line to stdout describing the player's
            achievements list.
        """
        print(f"Player {self.name} achievements: {self.achieves}")


if __name__ == "__main__":
    """Demo / CLI usage for the Achievements class.

    Creates three sample players (Alice, Bob, Charlie),
    prints their achievements
    and then computes various analytics using Python sets:
    - all_unique: sorted list of unique achievements across all players
    - common: achievements present for all three players
    - rare: achievements present in exactly one player
    Also prints a few pairwise comparisons between Alice and Bob.
    """
    print("=== Achievement Tracker System ===\n")

    achieves = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']
    game_alice = Achievements("Alice", achieves)
    game_alice.show_achives()

    achieves = ['first_kill', 'level_10', 'boss_slayer', 'collector']
    game_bob = Achievements("Bob", achieves)
    game_bob.show_achives()

    achieves = ['level_10', 'treasure_hunter', 'boss_slayer',
                'speed_demon', 'perfectionist']
    game_charlie = Achievements("Charlie", achieves)
    game_charlie.show_achives()

    print("\n=== Achievement Analytics ===")

    a = set(game_alice.achieves)
    b = set(game_bob.achieves)
    c = set(game_charlie.achieves)

    all_unique = set(a).union(b, c)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    common = set(a).intersection(b, c)
    print(f"Common to all players: {common}")

    rare = a.difference(b.union(c)).union(
        b.difference(a.union(c)),
        c.difference(a.union(b))
    )
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {b.intersection(a)}")
    print(f"Alice unique: {a.difference(b)}")
    print(f"Bob unique: {b.difference(a)}")
