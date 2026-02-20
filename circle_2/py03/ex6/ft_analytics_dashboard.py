

"""
Game Analytics Dashboard Module.

This module demonstrates the use of list, dictionary, and set comprehensions
to process and analyze raw game data, providing insights
into player performance,
achievements, and regional activity.
"""


if __name__ == "__main__":
    """
    Execute the analytics dashboard.

    Processes a sample dataset of game events to showcase:
    - List Comprehensions: Filtering and transforming scores.
    - Dict Comprehensions: Mapping player data and categorizing results.
    - Set Comprehensions: Identifying unique
    players, achievements, and regions.
    """

    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    data = [
        {"user": "alice", "points": 2300,
         "tags": ["level_10", "first_kill", "boss_slayer"], "zone": "north"},
        {"user": "bob", "points": 1800, "tags": ["level_10"], "zone": "east"},
        {"user": "charlie", "points": 2150,
         "tags": ["level_10", "first_kill"], "zone": "north"},
        {"user": "diana", "points": 2050, "tags": ["boss_slayer"],
         "zone": "central"},
    ]

    high_scorers = [d["user"] for d in data if d["points"] > 2000]
    scores_doubled = [d["points"] * 2 for d in data]
    active_players = [d["user"] for d in data if "level_10" in d["tags"]]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    player_scores = {d["user"]: d["points"] for d in data}

    score_labels = [
        "high" if d["points"] >= 2100 else
        "medium" if d["points"] >= 2000 else
        "low"
        for d in data
    ]

    score_categories = {
        label: sum(1 for lab in score_labels if lab == label)
        for label in ("high", "medium", "low")
    }

    achievement_counts = {d["user"]: len(d["tags"]) for d in data}

    print("\n=== Dict Comprehension Examples ===")

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    unique_players = {d["user"] for d in data}
    unique_achivements = {tag for d in data for tag in d["tags"]}
    active_regions = {d["zone"] for d in data}
    all_tags = {tag for d in data for tag in d["tags"]}

    print("\n=== Set Comprehension Examples ===")

    print(f"Unique players: {unique_players}")
    print(f"Unique achivements: {unique_achivements}")
    print(f"Active regions: {active_regions}")

    all_points = [d["points"] for d in data]
    avg_score = sum(all_points) / len(all_points)
    top_performer = sorted(data, key=lambda x: x["points"])[-1]

    print("\n=== Combined Analysis ===")

    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(all_tags)}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_performer['user']} "
          f"({top_performer['points']} points, "
          f"{len(top_performer['tags'])} achievements)")
