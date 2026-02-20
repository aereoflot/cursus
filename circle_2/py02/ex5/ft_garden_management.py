
class GardenError(Exception):
    """Custom exception for critical garden errors."""
    pass


class GardenManager:
    """Manager class for handling garden operations and plant maintenance."""

    def __init__(self):
        """Initialize an empty garden list."""
        self.garden = []

    def add_plant(self,
                  plant: str,
                  water: int,
                  sun: int):
        """
        Add a plant to the garden with validation.

        Args:
            plant: Name of the plant (cannot be empty)
            water: Water level required (1-10)
            sun: Sunlight hours required (2-12)

        Raises:
            ValueError: If plant name is empty or water/sun values are out
             of range
        """
        try:
            if not plant:
                raise ValueError("Plant name cannot be empty!")
            if water < 1:
                raise ValueError(f"Water level {water} is too low (min 1)")
            elif water > 10:
                raise ValueError(f"Water level {water} is too high (max 10)")
            if sun < 2:
                raise ValueError(f"Sunlight hours {sun} is too \
low (min 2)")
            elif sun > 12:
                raise ValueError(f"Sunlight hours {sun} is too \
high (min 12)")
        except ValueError as e:
            print("Error adding plant:", e)
        else:
            self.garden.append([plant, water, sun])
            print(f"Added {plant} successfully")

    def watering(self):
        """
        Water all plants in the garden and handle errors gracefully.

        Increments water level for each plant and ensures the watering system
        is properly closed regardless of errors.
        """
        print("Opening watering system")
        try:
            for plants in self.garden:
                print(f"Watering {plants[0]} - success")
                plants[1] += 1
        except TypeError:
            print("Something was wrong")
        finally:
            print("closing watering system (cleanup)")

    def checker(self):
        """
        Check the health status of all plants in the garden.

        Validates water and sunlight levels for each plant and reports
        any issues or healthy status based on predefined ranges.
        """
        for plants in self.garden:
            try:
                if plants[1] < 1:
                    raise ValueError(f"Water level {plants[1]} is too \
low (min 1)")
                elif plants[1] > 10:
                    raise ValueError(f"Water level {plants[1]} is too \
high (max 10)")
                if plants[2] < 2:
                    raise ValueError(f"Sunlight hours {plants[2]} is \
too low (min 2)")
                elif plants[2] > 12:
                    raise ValueError(f"Sunlight hours {plants[2]} is \
too high (min 12)")
            except ValueError as e:
                print(f"Error checking {plants[0]}:", e)
            else:
                print(f"{plants[0]}: healthy (water: {plants[1]}, \
sun: {plants[2]})")


if __name__ == "__main__":
    print("=== Garden Management System ===")

    my_garden = GardenManager()

    print("\nAdding plants to garden...")

    my_garden.add_plant("tomato", 4, 7)
    my_garden.add_plant("lettuce", 10, 5)
    my_garden.add_plant("", 4, 7)

    print("\nWatering plants...")
    my_garden.watering()

    print("\nChecking plant kealth...")
    my_garden.checker()

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")

    except GardenError as e:
        print(f"Caught GardenError: {e}")

    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")
