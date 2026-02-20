"""
Defines a Plant class and prints info for example plant instances.
"""


class Plant:
    """Represents a plant with name, height, and age."""

    def __init__(self, plant, hight, day):
        """Initialize plant with name, height (cm), and age (days)."""
        self.plant = plant
        self.hight = hight
        self.day = day

    def show_info(self):
        """Print plant name, height, and age."""
        print(f"{self.plant}: {self.hight}cm, \
{self.day} days old")


plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
plant4 = Plant("Tulip", 20, 8)

print("=== Garden Plant Registry ===")
plant1.show_info()
plant2.show_info()
plant3.show_info()
plant4.show_info()
