"""
SecurePlant module.

Provides SecurePlant, a small class that encapsulates plant attributes
(name, height, age) and enforces simple security rules: height and age
must be non-negative. Methods validate updates and print informative
status or rejection messages.
"""


class SecurePlant:
    """Encapsulates a plant's name, height and age with validation."""

    def __init__(self, name, height, age):
        """Initialize a SecurePlant and set initial height and age.

        Uses set_height and set_age to apply validation and print status.
        """
        self.__name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def print_error(self, reason, value) -> None:
        """Print a rejection message when a negative value is supplied.

        reason: 'height' or other (treated as 'age')
        value: the invalid numeric value provided
        """
        if reason == "height":
            print(f"\nInvalid operation attempted: height \
{value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            print(f"\nInvalid operation attempted: age \
{value} days [REJECTED]")
            print("Security: Negative age rejected")

    def set_height(self, height) -> None:
        """Update the plant height if non-negative; otherwise reject."""
        if height >= 0:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            self.print_error("height", height)

    def set_age(self, age) -> None:
        """Update the plant age if non-negative; otherwise reject."""
        if age >= 0:
            self.__age = age
            print(f"Age updated: {age} days [OK]")
        else:
            self.print_error("age", age)

    def get_height(self) -> int:
        """Return the current height (cm)."""
        return self.__height

    def get_age(self) -> int:
        """Return the current age (days)."""
        return self.__age

    def get_info(self) -> None:
        """Print a concise summary of the current plant state."""
        print(f"\nCurrent plant: {self.__name} ({self.__height}cm, \
{self.__age} days)")


name = "Rose"
height = 25
age = 30

print("=== Garden Security System ===")
print(f"Plant created: {name}")
plant = SecurePlant(name, height, age)
height = -5
plant.set_height(height)
plant.get_info()
