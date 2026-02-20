class GardenError(Exception):
    """Base exception class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised when there is a problem with a plant."""
    pass


class WaterError(GardenError):
    """Exception raised when there is a problem with water or watering."""
    pass


def test_plant_error():
    """
    Test and demonstrate PlantError exception handling.

    Raises a PlantError with a message about a wilting tomato plant
    and catches it to display the error message.
    """
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print("Caught PlantError:", e)


def test_water_error():
    """
    Test and demonstrate WaterError exception handling.

    Raises a WaterError with a message about insufficient water
    and catches it to display the error message.
    """
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught WaterError:", e)


def test_general_error():
    """
    Test catching all garden errors using the base GardenError class.

    Demonstrates polymorphic exception handling by catching both PlantError
    and WaterError using the parent GardenError class.
    """
    print("\nTesting catching all garden errors...")
    garden_errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]

    for err in garden_errors:
        try:
            raise err
        except GardenError as e:
            print("Caught a garden error:", e)


def test_custom_errors():
    """
    Run all custom error tests.

    Executes test_plant_error(), test_water_error(), and test_general_error()
    to demonstrate all custom exception types and their handling.
    """
    test_plant_error()
    test_water_error()
    test_general_error()


if __name__ == "__main__":
    """
    Main execution block for the Custom Garden Errors Demo.

    Initializes the application and runs all custom error tests to verify
    that all custom exception types work correctly.
    """
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("\nAll custom error types work correctly!")
