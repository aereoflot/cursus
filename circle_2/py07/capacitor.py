"""Script to test the ex1 capabilities and factories."""

from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability
)


def test_healing() -> None:
    """Tests the capabilities of the healing factory creatures."""
    factory = HealingCreatureFactory()
    print("Testing Creature with healing capability\n base:")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform() -> None:
    """Tests the capabilities of the transforming factory creatures."""
    factory = TransformCreatureFactory()
    print("\nTesting Creature with transform capability\n base:")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())

    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    test_healing()
    test_transform()
