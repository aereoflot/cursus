class Plant:
    """Represents a basic plant with name, height, and age."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int = 1):
        """Increase plant height by cm and print growth message."""
        self.height += cm
        print(f"{self.name} grew {cm}cm")

    def points(self):
        """Return points awarded by this plant (0 for basic plants)."""
        return 0

    def report(self):
        """Return a string summary of plant name and height."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Represents a flowering plant with color and blooming status."""

    def __init__(self, name, height, age, color: str, blooming: bool):
        """Initialize flowering plant with color and blooming status."""
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming

    def bloom(self):
        """Print bloom status message."""
        if self.blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is not blooming!")

    def points(self):
        """Return 5 points if blooming, 0 otherwise."""
        return 5 if self.blooming else 0

    def report(self):
        """Return summary with height, color, and blooming status."""
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    """Represents a prize-winning flowering plant with bonus points."""

    def __init__(self, name, height, age,
                 color: str,
                 blooming: bool,
                 prize_points: int):
        """Initialize prize flower with additional prize points."""
        super().__init__(name, height, age, color, blooming)
        self.prize_points = prize_points

    def points(self):
        """Return blooming points plus prize points."""
        return super().points() + self.prize_points

    def report(self):
        """Return summary with prize points included."""
        base_report = super().report()
        return f"{base_report}, Prize points: {self.prize_points}"


class Garden:
    """Represents a garden containing multiple plants."""

    def __init__(self, name: str):
        """Initialize garden with a name and empty plant list."""
        self.name = name
        self.plants = []

    def add_plant(self, plant: Plant):
        """Add a plant to the garden and print confirmation."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all_plants(self, cm: int = 1):
        """Grow all plants in the garden by cm."""
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)

    def total_score(self):
        """Return sum of all plants' points."""
        return sum(plant.points() for plant in self.plants)

    def report(self):
        """Print garden report with all plants and stats."""
        print(f"\n=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.report()}")
        print(f"Plants added: {len(self.plants)}, \
Total growth: {len(self.plants)*1}cm")


class GardenStats:
    """Static and class methods for garden analytics."""

    @staticmethod
    def average_height(plants):
        """Return average height of plants or 0 if list empty."""
        if not plants:
            return 0
        return sum(p.height for p in plants) / len(plants)

    @classmethod
    def total_plants(cls, gardens):
        """Return total number of plants across all gardens."""
        return sum(len(g.plants) for g in gardens.values())


class GardenManager:
    """Manages multiple gardens and their operations."""

    def __init__(self):
        """Initialize manager with empty gardens dictionary."""
        self.gardens = {}

    def add_garden(self, garden: Garden):
        """Add garden to manager using garden name as key."""
        self.gardens[garden.name] = garden

    def show_scores(self):
        """Print score for each managed garden."""
        print("Garden scores:")
        for name, garden in self.gardens.items():
            print(f"{name}: {garden.total_score()}")

    @classmethod
    def create_garden_network(cls):
        """Create and initialize a new garden network."""
        print("Creating a new garden network...")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager()

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    oak = Plant("Oak Tree", 100, 1825)
    rose = FloweringPlant("Rose", 25, 30, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 90, "yellow", True, 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    pine = Plant("Pine", 90, 1500)
    daisy = FloweringPlant("Daisy", 20, 20, "white", True)

    bob_garden.add_plant(pine)
    bob_garden.add_plant(daisy)

    for garden in manager.gardens.values():
        garden.grow_all_plants(1)

    print("\n")

    for garden in manager.gardens.values():
        for plant in garden.plants:
            if isinstance(plant, FloweringPlant):
                plant.bloom()

    for garden in manager.gardens.values():
        garden.report()

    print("\n")

    for name, garden in manager.gardens.items():
        avg = GardenStats.average_height(garden.plants)
        print(f"{name}'s average height: {avg:.1f}cm")

    valid_height = all(p.height > 0 for garden in manager.gardens.values()
                       for p in garden.plants)
    print(f"\nHeight validation test: {valid_height}")

    print(
        "Garden scores -",
        ", ".join(
            f"{name}: {garden.total_score()}"
            for name, garden in manager.gardens.items()
            )
        )

    total = GardenStats.total_plants(manager.gardens)
    print(f"Total gardens managed: {len(manager.gardens)}")
    print(f"Total plants: {total}")
