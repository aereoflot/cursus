"""Player score analytics CLI.

Reads integer scores from command-line arguments and prints basic
statistics: list of scores, count, total, average, high, low and range.

Usage:
    python3 ft_score_analytics.py <score1> <score2> ...
"""

import sys


def analytics():
    """Parse scores from sys.argv and print summary statistics.

    Behavior:
    - If no scores are provided, a ValueError is raised and a usage message
      is printed by the exception handler.
    - Converts each additional sys.argv item to int; non-integer values
      will raise ValueError and trigger the usage message.
    - Prints:
        - Scores processed (list)
        - Total players (count)
        - Total score (sum)
        - Average score
        - High score
        - Low score
        - Score range (max - min)
    """
    try:
        if len(sys.argv) == 1:
            raise ValueError("no_scores")

        scores = []
        for num in range(1, len(sys.argv)):
            scores.append(int(sys.argv[num]))

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")
    except ValueError:
        print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    """Module entry point: print header and run analytics()."""
    print("=== Player Score Analytics ===")
    analytics()
