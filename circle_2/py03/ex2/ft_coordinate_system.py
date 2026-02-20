"""Game coordinate utilities.

This module provides simple helpers to work with 3D coordinates:
- point_to_point: compute and print Euclidean distance between two points.
- parsing_coord: construct a coordinate tuple from three integers.
- coordinate: small wrapper to compute distance from the origin to a point.

The module also contains a small CLI/demo block under
`if __name__ == "__main__":`
that creates example points, validates them, prints distances and demonstrates
tuple unpacking.
"""
import math


def point_to_point(point_a: tuple, point_b: tuple) -> float:
    """Compute and print the Euclidean distance between two 3D points.

    Args:
        point_a: (x, y, z) tuple of ints/floats for the first point.
        point_b: (x, y, z) tuple of ints/floats for the second point.

    Returns:
        The Euclidean distance as a float.

    Side effect:
        Prints a formatted message with the distance limited to two decimals.
    """
    x_dist = point_a[0] - point_b[0]
    y_dist = point_a[1] - point_b[1]
    z_dist = point_a[2] - point_b[2]
    result = math.sqrt(x_dist**2 + y_dist**2 + z_dist**2)
    print(f"Distance between {point_a} and {point_b}: {result:.2f}")
    return result


def parsing_coord(x: int, y: int, z: int) -> tuple:
    """Create a 3-tuple coordinate from three integer components.

    Args:
        x: X coordinate (int).
        y: Y coordinate (int).
        z: Z coordinate (int).

    Returns:
        A tuple (x, y, z).
    """
    return (x, y, z)


def coordinate(point_a: tuple) -> None:
    """Compute distance from the origin to a given point and print it.

    Args:
        point_a: (x, y, z) tuple representing the point.

    This function uses the origin (0, 0, 0) as the first point and calls
    point_to_point to compute and print the distance.
    """
    point_0 = (0, 0, 0)

    point_to_point(point_0, point_a)


if __name__ == "__main__":
    """Demo / CLI behavior when executed as a script.

    The demo:
    - creates sample points
    - validates that components are ints
    - computes distances
    - demonstrates error handling for invalid coordinates
    - prints an unpacking demonstration in the finally block
    """
    print("=== Game Coordinate System ===")

    finally_point = (0, 0, 0)

    try:
        point_a = (10, 20, 5)
        print(f"\nPosition created: {point_a}")
        for num in point_a:
            if type(num) is not int:
                raise ValueError(f"'{num}'")
        finally_point = point_a
        coordinate(point_a)

        print('\nParsing coordinates: "3,4,0"')
        point_b = (3, 4, 0)
        for num in point_b:
            if type(num) is not int:
                raise ValueError(f"'{num}'")
        finally_point = point_b
        print(f"Position created: {point_a}")
        coordinate(point_b)

        print('\nParsing invalid coordinates: "abc,def,ghi"')
        point_c = ("abc", "def", "ghi")
        for num in point_c:
            if type(num) is not int:
                raise ValueError(f"'{num}'")
        finally_point = point_c
        coordinate(point_c)

    except ValueError as e:
        print(f"Error parsing coordinates: invalid literal \
for int() with base 10: {e}")
        print(f'Error details - Type: ValueError, Args: \
("invalid literal for int() with base 10: {e}",)')
    finally:
        print("\nUnpacking demonstration:")
        print(f"Player at \
x={finally_point[0]}, y={finally_point[1]}, z={finally_point[2]}")
        print(f"Coordinates: \
X={finally_point[0]}, Y={finally_point[1]}, Z={finally_point[2]}")
