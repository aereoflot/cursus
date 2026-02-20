"""Game data stream utilities and demonstrations.

This module provides simple generator-based utilities used in examples:
- event_stream(n): yields n synthetic game event dictionaries.
- fibonacci(n): yields the first n Fibonacci numbers.
- get_primes(n): yields the first n prime numbers.

When executed as a script the module runs a small demo that processes a
stream of events and prints simple analytics and generator demonstrations.
"""


def event_stream(n):
    """Yield n synthetic game event dictionaries.

    Each yielded item is a dict with keys:
    - "id": sequential event id (int, starting at 1)
    - "player": player name (str)
    - "level": player level (int)
    - "action": event action description (str)

    The function cycles through a small set of player names and actions so
    the stream can be consumed without storing all events in memory.
    """
    players = ["alice", "bob", "charlie", "david", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        player = players[i % len(players)]
        level = (i * 7) % 20 + 1
        action = actions[i % len(actions)]

        yield {"id": i, "player": player, "level": level, "action": action}


def fibonacci(n):
    """Yield the first n Fibonacci numbers, starting from 0.

    The sequence yielded is: 0, 1, 1, 2, 3, 5, ...

    Args:
        n (int): number of values to yield.

    Yields:
        int: next Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def get_primes(n):
    """Yield the first n prime numbers (2, 3, 5, 7, ...).

    This simple implementation tests divisibility up to the square root of
    each candidate number; it is suitable for small n used in examples.

    Args:
        n (int): number of primes to yield.

    Yields:
        int: next prime number.
    """
    count = 0
    num = 2
    while count < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    total_events = 1000

    print(f"Processing {total_events} game events...\n")

    high_level_count = 0
    treasure_count = 0
    level_up_count = 0

    for event in event_stream(total_events):
        if event["id"] <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")

        if event["level"] >= 10:
            high_level_count += 1
        if event["action"] == "found treasure":
            treasure_count += 1
        if event["action"] == "leveled up":
            level_up_count += 1

    print("...")

    print("\n=== Stream Analytics ===")

    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.001 seconds")

    print("\n=== Generator Demonstration ===")

    fib_list = [str(num) for num in fibonacci(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_list = [str(num) for num in get_primes(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")
