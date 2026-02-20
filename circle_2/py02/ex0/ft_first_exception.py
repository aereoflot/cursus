def check_temperature(temp_str: str) -> int:
    """
    Check and validate the temperature for plant growing conditions.

    Converts the input string to an integer and validates if the temperature
    is within the acceptable range (0-40°C) for plants. Prints appropriate
    messages for valid, too cold, or too hot temperatures.

    Args:
        temp_str: A string representation of the temperature value

    Returns:
        The temperature as an integer if it is within valid range (0-40°C),
        otherwise returns None

    Raises:
        ValueError: If the input string cannot be converted to an integer
    """
    try:
        temp_str = int(temp_str)
        if temp_str >= 0 and temp_str <= 40:
            print(f"Temperature {temp_str}ºC is perfect for plants!\n")
            return (temp_str)
        elif temp_str < 0:
            print(f"ERROR: {temp_str}ºC is too cold for plants (min 0ºC)\n")
        elif temp_str > 40:
            print(f"ERROR: {temp_str}ºC is too hot for plants (max 40ºC)\n")
        else:
            raise ValueError
    except ValueError:
        print(f"ERROR: {temp_str} is not a valid number\n")


def test_temperature_input():
    """
    Run comprehensive tests for the temperature checker function.

    Tests various temperature scenarios including valid temperatures,
    non-numeric inputs, temperatures that are too hot, and temperatures
    that are too cold. Demonstrates proper error handling and validation.
    """
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")


if __name__ == "__main__":
    """
    Main execution block for the Garden Temperature Checker.

    Initializes the application and runs all temperature checking tests
    to verify proper exception handling and validation.
    """
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
