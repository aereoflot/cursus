"""
Simple script that prints a brief garden summary.
"""

if __name__ == "__main__":
    def garden() -> None:
        """Display garden information with plant details."""
        plant = "Rose"
        height = "25"
        age = "30"

        print("=== Welcome to My Garden ===")
        print(f"Plant: {plant}\nHeight: {height}cm\nAge: {age} days")
        print("\n=== End of Program ===")
    garden()
