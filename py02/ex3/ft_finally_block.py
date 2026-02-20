def water_plants(plant_list):
    """
    Water a list of plants and ensure cleanup happens regardless of errors.

    Opens the watering system, waters each plant in the list, and ensures
    the system is properly closed even if an error occurs. Handles cases
    where a plant entry is None.

    Args:
        plant_list: List of plant names (strings) to water. May contain
         None values.

    Raises:
        TypeError: If a plant entry is None, indicating an invalid plant.
    """
    print("\nTesting normal watering...")
    print("Opening watering system")
    try:
        for plants in plant_list:
            if plants is None:
                raise TypeError
            print("Watering", plants)
        print("Watering complete succesfully!")
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
        print("\nCleanup always happens, even with errors!")


def test_watering_system():
    """
    Run comprehensive tests for the watering system.

    Tests the watering system with two scenarios: one with all valid plants
    and one with a None value in the plant list. Demonstrates proper error
    handling and the execution of cleanup operations.
    """
    print("=== Garden Watering System ===")
    plant_list = [
        "tomato",
        "lettuce",
        "carrots"
    ]

    water_plants(plant_list)

    plant_list = [
        "tomato",
        None,
        "carrots"
    ]

    water_plants(plant_list)


if __name__ == "__main__":
    """
    Main execution block for the Garden Watering System.

    Initializes the application and runs all watering system tests.
    """
    test_watering_system()
