def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int):
    """
    Check and validate the health status of a plant.

    Validates that the plant name is not empty and that water level and
    sunlight hours are within acceptable ranges. Prints appropriate messages
    for valid or invalid plant conditions.

    Args:
        plant_name: Name of the plant (cannot be empty)
        water_level: Water level required (must be between 1-10)
        sunlight_hours: Sunlight hours required (must be between 2-12)

    Raises:
        ValueError: If plant name is empty or water/sunlight values are
                    outside valid ranges
    """
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too \
low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too \
high (min 12)")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """
    Run comprehensive tests for plant health checking functionality.

    Tests various scenarios including valid plant data, empty plant names,
    invalid water levels, and invalid sunlight hours. Demonstrates proper
    error handling and validation.
    """
    print("\nTesting good values...")
    check_plant_health("tomato", 4, 6)

    print("\nTesting empty plant name...")
    check_plant_health("", 4, 6)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 6)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 4, 0)

    print("\nAll error raising test completed!")


if __name__ == "__main__":
    """
    Main execution block for the Garden Plant Health Checker.

    Initializes the application and runs all plant health check tests.
    """
    print("=== Garden Plant Health Checker ===")

    test_plant_checks()
