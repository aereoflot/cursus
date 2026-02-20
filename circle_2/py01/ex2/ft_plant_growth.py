class Plant:
    """Represents a plant with name, height, and age."""

    def __init__(self, plant, hight, days):
        """Initialize plant with name, height (cm), and age (days)."""
        self.plant = plant
        self.hight = hight
        self.days = days

    def grow(self):
        """Increase plant height by 1cm."""
        self.hight += 1

    def increase_day(self):
        """Increment plant age by 1 day."""
        self.days += 1

    def get_info(self):
        """Print plant name, height, and age."""
        print(f"{self.plant}: {self.hight}cm, \
{self.days} days old")


day = 1
grow = 0
plant1 = Plant("Rose", 25, 30)
plant2 = Plant("Sunflower", 80, 45)
plant3 = Plant("Cactus", 15, 120)
plant4 = Plant("Tulip", 20, 8)
Plants = [plant1, plant2, plant3, plant4]

print(f"=== Day {day} ===")
for plant in Plants:
    plant.get_info()

while day < 7:
    for plant in Plants:
        plant.grow()
        plant.increase_day()
    grow += 1
    day += 1

print(f"=== Day {day} ===")
for plant in Plants:
    plant.get_info()
print(f"Growth this week: +{grow}cm")
