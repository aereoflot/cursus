class Plant:
    """Represents a basic plant with name, height, and age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a flowering plant with color and blooming status."""

    def __init__(self, name, height, age, color: str, bloom: bool) -> None:
        """Initialize flower with color and blooming status."""
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def print_flower(self):
        """Print flower details including name,
        height, color, and bloom status."""
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, \
{self.color} color")

        if self.bloom:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} is not blooming!\n")


class Tree(Plant):
    """Represents a tree with trunk diameter and shade coverage."""

    def __init__(self, name, height, age, trunk_diam: int, shade: int) -> None:
        """Initialize tree with trunk diameter (cm) and shade area (m²)."""
        super().__init__(name, height, age)
        self.trunk_diam = trunk_diam
        self.shade = shade

    def print_tree(self):
        """Print tree details including name, height,
        trunk diameter, and shade."""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, \
{self.trunk_diam}cm diameter\n{self.name} provides {self.shade} \
square meters of shade\n")


class Vegetable(Plant):
    """Represents a vegetable plant with harvest season and nutrition info."""

    def __init__(self, name, height, age, season: str, nutri: str) -> None:
        """Initialize vegetable with harvest season and main nutrient."""
        super().__init__(name, height, age)
        self.season = season
        self.nutri = nutri

    def print_vegetable(self):
        """Print vegetable details including name, height,
        season, and nutrients."""
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, \
{self.season} harvest\n{self.name} is rich in {self.nutri}\n")


print("=== Garden Plant Types ===\n")

rose = Flower("Rose", 25, 30, "red", True)
tulip = Flower("Tulip", 20, 15, "yellow", False)

rose.print_flower()
tulip.print_flower()

oak = Tree("Oak", 500, 1825, 50, 78)
pine = Tree("Pine", 450, 1500, 40, 60)

oak.print_tree()
pine.print_tree()

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 30, 70, "spring", "beta-carotene")

tomato.print_vegetable()
carrot.print_vegetable()
