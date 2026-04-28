"""Script to test the strategies in a tournament format."""

from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    StrategyError
)


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    """Organizes a tournament where every opponent fights every other."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                fac1, strat1 = opponents[i]
                fac2, strat2 = opponents[j]

                c1 = fac1.create_base()
                c2 = fac2.create_base()

                print("\n* Battle *")
                print(c1.describe())
                print(" vs.")
                print(c2.describe())
                print(" now fight!")

                print(strat1.act(c1))
                print(strat2.act(c2))

    except StrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])
