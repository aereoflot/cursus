def garden_operations():
    """
    Test and demonstrate different types of exceptions.

    Tests various exception types including ValueError, ZeroDivisionError,
    FileNotFoundError, and KeyError. Each exception type is caught and
    handled separately. Also demonstrates catching multiple exception
    types together.
    """
    dic = {"tomato": 2}
    date = "abc"

    print("Testing ValueError...")
    try:
        date = int(date)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        date = 4/0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        open("mising.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        print(dic["Nothing"])
    except KeyError:
        print("Caught KeyError: 'missing/_plant'\n")

    print("Testing multiple errors together...")
    try:
        date = 4/0
        print(dic["Nothing"])
    except (KeyError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    """
    Run all error type tests.

    Executes the garden_operations() function to run comprehensive tests
    for all different exception types.
    """
    garden_operations()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")
