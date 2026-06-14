import sys
from typing import Dict, List

from parse import Parser, ParseError
from pathfinding import GraphNode, Edge, SpaceTimeAStar

ANSI_COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "gray": "\033[90m",
    "purple": "\033[95m",
    "black": "\033[30m",
    "brown": "\033[33m",
    "orange": "\033[33m",
    "maroon": "\033[31m",
    "gold": "\033[93m",
    "darkred": "\033[31m",
    "violet": "\033[95m",
    "crimson": "\033[91m",
    "rainbow": "\033[96m",
    "reset": "\033[0m"
}


def colorize(text: str, color_name: str | None) -> str:
    """Colorize text with ANSI color codes.

    Args:
        text: The text to colorize.
        color_name: Name of the color (e.g., 'red', 'blue').
            If None, text is returned unchanged.

    Returns:
        str: The colorized text with ANSI codes, or original text
            if color not found.
    """
    if not color_name:
        return text
    color_code = ANSI_COLORS.get(color_name.lower(), "")
    if color_code:
        return f"{color_code}{text}{ANSI_COLORS['reset']}"
    return text


def main() -> None:
    """Main entry point for the drone pathfinding application.

    Reads a map file, parses it, builds a graph, finds paths for all drones,
    and outputs the drone movements by turn with optional coloring.

    Raises:
        SystemExit: On invalid arguments or parsing errors.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <map_file>")
        sys.exit(1)
    
    if len(sys.argv) == 3:
        capacity_info = True if "--capacity-info" in sys.argv[1] else False
        map_file = sys.argv[2]

    else:
        capacity_info = False
        map_file = sys.argv[1]

    try:
        parser = Parser(map_file)
        map_data = parser.parse()
    except ParseError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    nodes: Dict[str, GraphNode] = {}
    for name, zone in map_data.zones.items():
        nodes[name] = GraphNode(name, zone.zone_type, zone.max_drones)

    edges: Dict[tuple[str, str], Edge] = {}
    for conn in map_data.connections:
        edges[(conn.zone1, conn.zone2)] = Edge(
            conn.zone1, conn.zone2, conn.max_link_capacity
        )
        edges[(conn.zone2, conn.zone1)] = Edge(
            conn.zone2, conn.zone1, conn.max_link_capacity
        )
        nodes[conn.zone1].neighbors.append(conn.zone2)
        nodes[conn.zone2].neighbors.append(conn.zone1)

    if map_data.start_hub is None or map_data.end_hub is None:
        print("Error: Missing start or end hub.", file=sys.stderr)
        sys.exit(1)

    pathfinder = SpaceTimeAStar(nodes, edges)

    try:
        paths = pathfinder.route_all_drones(
            map_data.nb_drones, map_data.start_hub, map_data.end_hub
        )
    except ValueError as e:
        print(f"Error en pathfinding: {e}", file=sys.stderr)
        sys.exit(1)

    turn_actions: Dict[int, List[str]] = {}

    for drone_idx, path in enumerate(paths):
        drone_id = f"D{drone_idx + 1}"
        prev_node = map_data.start_hub

        for step in path:
            dest, start_turn, cost = step
            if cost == 0 or dest == prev_node:
                continue

            zone_color = map_data.zones[dest].color

            if cost == 1:
                if start_turn not in turn_actions:
                    turn_actions[start_turn] = []

                action_str = colorize(f"{drone_id}-{dest}", zone_color)
                turn_actions[start_turn].append(action_str)

            elif cost == 2:
                connection_name = f"{prev_node}-{dest}"
                if start_turn not in turn_actions:
                    turn_actions[start_turn] = []

                action_conn_str = colorize(
                    f"{drone_id}-{connection_name}", zone_color
                )
                turn_actions[start_turn].append(action_conn_str)

                arrival_turn = start_turn + 1
                if arrival_turn not in turn_actions:
                    turn_actions[arrival_turn] = []

                action_dest_str = colorize(
                    f"{drone_id}-{dest}", zone_color
                )
                turn_actions[arrival_turn].append(action_dest_str)

            prev_node = dest

    if not turn_actions:
        return

    max_turn = max(turn_actions.keys())
    for t in range(max_turn + 1):
        if t in turn_actions and turn_actions[t]:
            actions_str = " ".join(turn_actions[t])
            if capacity_info:
                print(path[t], "conection: ", path[t+1])
            print(actions_str)


if __name__ == "__main__":
    main()
