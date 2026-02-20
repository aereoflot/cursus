#!/usr/bin/env python3
"""
Generate example mazes (non-interactive demonstration).

Examples
--------
1. Perfect maze (25x18) - Single solution path
2. Imperfect maze (25x18) - Multiple solution paths
3. Small maze (10x8) - Too small for "42", shows warning
"""

from mazegen import MazeGenerator
import time


def main() -> None:
    """Generate and display example mazes."""

    print("\n" + "="*60)
    print("  A-MAZE-ING - Example Mazes")
    print("="*60 + "\n")

    print("Example 1: PERFECT MAZE (25x18)")
    print("-" * 60)
    maze1 = MazeGenerator()
    maze1.generate(25, 18, (1, 1), (24, 17), perfect=True)
    maze1.render(
        show_path=True, start=(1, 1),
        end=(24, 17), show_42_warning=False
    )
    print("\n")
    time.sleep(2)

    print("\nExample 2: IMPERFECT MAZE (25x18)")
    print("-" * 60)
    maze2 = MazeGenerator()
    maze2.generate(25, 18, (1, 1), (24, 17), perfect=False)
    maze2.render(
        show_path=True, start=(1, 1),
        end=(24, 17), show_42_warning=False
    )
    print("\n")
    time.sleep(2)

    print("\nExample 3: SMALL MAZE (10x8) - Without '42' pattern")
    print("-" * 60)
    maze3 = MazeGenerator()
    maze3.generate(10, 8, (1, 1), (9, 7), perfect=True)
    maze3.render(
        show_path=True, start=(1, 1),
        end=(9, 7), show_42_warning=True
    )
    print("\n")

    print("="*60)
    print("  All examples generated successfully!")
    print("  Use 'make run' for interactive mode.")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
