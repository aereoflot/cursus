class Plant:
    """Represents a basic plant with name, height, and age."""

    def __init__(self, name, height, age):
        """Initialize plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age


plant_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]

plants = []

for name, height, age in plant_data:
    plants.append(Plant(name, height, age))

print("=== Plant Factory Output ===")
for plant in plants:
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

print(f"Total plants created: {len(plants)}")
