"""Command Quest utility.

Provides a small CLI helper that inspects command-line arguments (sys.argv)
and prints a summary including program name, number of arguments and each
argument value.
"""
import sys


def command_control() -> None:
    """Print information about command-line arguments.

    Behavior:
    - If no extra arguments are provided, prints a message and
    the program name.
    - If arguments are provided, prints the program name,
    the count of provided
      arguments and each argument on its own line.
    - Always prints the total number of entries in sys.argv
    (including program name).

    This function reads from sys.argv and prints directly;
    it does not return a value.
    """
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Argument revceived: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Arguments {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")

    command_control()
