from typing import List, Dict, Set, Tuple, Optional
from collections import defaultdict
import heapq


class GraphNode:
    """Represents a node in the graph.

    Attributes:
        name: Unique identifier for the node.
        zone_type: Type of zone (normal, blocked, restricted, priority).
        capacity: Maximum number of drones allowed in this node.
        neighbors: List of adjacent node names.
    """

    def __init__(self, name: str, zone_type: str = "normal",
                 capacity: int = 1):
        """Initialize a GraphNode instance.

        Args:
            name: Unique identifier for the node.
            zone_type: Type of zone. Defaults to "normal".
            capacity: Maximum capacity of the node. Defaults to 1.
        """
        self.name = name
        self.zone_type = zone_type
        self.capacity = capacity
        self.neighbors: List[str] = []


class Edge:
    """Represents an edge/connection between two nodes.

    Attributes:
        src: Name of the source node.
        dst: Name of the destination node.
        capacity: Maximum flow capacity of this edge.
    """

    def __init__(self, src: str, dst: str, capacity: int = 1):
        """Initialize an Edge instance.

        Args:
            src: Name of the source node.
            dst: Name of the destination node.
            capacity: Maximum capacity of the edge. Defaults to 1.
        """
        self.src = src
        self.dst = dst
        self.capacity = capacity


class SpaceTimeAStar:
    """Space-Time A* pathfinding algorithm for multi-drone coordination.

    This class implements A* search in a space-time graph to find
    collision-free paths for multiple drones in a congested environment.

    Attributes:
        nodes: Dictionary mapping node names to GraphNode objects.
        edges: Dictionary mapping (src, dst) tuples to Edge objects.
        reservations: Dictionary tracking space-time reservations
            by turn and location.
    """

    def __init__(self, nodes: Dict[str, GraphNode],
                 edges: Dict[Tuple[str, str], Edge]):
        """Initialize a SpaceTimeAStar instance.

        Args:
            nodes: Dictionary of nodes in the graph.
            edges: Dictionary of edges in the graph.
        """
        self.nodes = nodes
        self.edges = edges
        self.reservations: Dict[int, Dict[str, int]] = defaultdict(
            lambda: defaultdict(int)
        )

    def heuristic(self, current: str, target: str) -> int:
        """Calculate heuristic cost between two nodes.

        Args:
            current: Current node name.
            target: Target node name.

        Returns:
            int: Heuristic cost (0 for uninformed search).
        """
        return 0

    def get_zone_cost(self, zone_name: str) -> int:
        """Get traversal cost for a zone based on its type.

        Args:
            zone_name: Name of the zone.

        Returns:
            int: Cost to traverse the zone (1 for normal,
                2 for restricted).
        """
        z_type = self.nodes[zone_name].zone_type
        if z_type == "restricted":
            return 2
        return 1

    def get_priority_bonus(self, zone_name: str) -> float:
        """Get priority bonus/penalty for a zone.

        Args:
            zone_name: Name of the zone.

        Returns:
            float: Priority bonus (negative for priority zones).
        """
        z_type = self.nodes[zone_name].zone_type
        if z_type == "priority":
            return -0.1
        return 0.0

    def can_move(self, src: str, dst: str, current_turn: int,
                 cost: int) -> bool:
        """Check if a move is valid given current space-time constraints.

        Args:
            src: Source node name.
            dst: Destination node name.
            current_turn: Current turn number.
            cost: Cost to traverse to destination.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if self.nodes[dst].zone_type == "blocked":
            return False

        edge_key = ((src, dst) if (src, dst) in self.edges
                    else (dst, src))
        if edge_key in self.edges:
            reservation_key = f"edge_{src}_{dst}"
            if (self.reservations[current_turn][reservation_key] >=
                    self.edges[edge_key].capacity):
                return False

        arrival_turn = current_turn + cost
        if (self.reservations[arrival_turn][dst] >=
                self.nodes[dst].capacity):
            return False

        return True

    def reserve_path(self, path: List[Tuple[str, int, int]]) -> None:
        """Reserve space-time nodes along a path.

        Args:
            path: List of (node, turn, cost) tuples representing
                the path.
        """
        for step in path:
            node, turn, cost = step
            if cost == 2:
                self.reservations[turn]["transit"] += 1
            self.reservations[turn + cost][node] += 1

    def find_path(self, start: str, end: str,
                  start_turn: int = 0) -> Optional[
                      List[Tuple[str, int, int]]]:
        """Find a collision-free path for a single drone.

        Args:
            start: Starting node name.
            end: Destination node name.
            start_turn: Starting turn. Defaults to 0.

        Returns:
            Optional[List[Tuple[str, int, int]]]: Path as list of
                (node, turn, cost) tuples, or None if no path exists.
        """
        open_set: List[Tuple[float, int, str,
                             List[Tuple[str, int, int]]]] = [
            (0.0, start_turn, start, [(start, start_turn, 0)])
        ]
        closed_set: Set[Tuple[int, str]] = set()

        while open_set:
            (current_cost, current_turn, current_node,
             path) = heapq.heappop(open_set)
            current_cost_float: float = current_cost

            if current_node == end:
                self.reserve_path(path[1:])
                return path

            state_key = (current_turn, current_node)
            if state_key in closed_set:
                continue
            closed_set.add(state_key)

            for neighbor in self.nodes[current_node].neighbors:
                move_cost = self.get_zone_cost(neighbor)
                if self.can_move(current_node, neighbor,
                                 current_turn, move_cost):
                    priority = (current_cost_float + move_cost +
                                self.heuristic(neighbor, end) +
                                self.get_priority_bonus(neighbor))
                    new_path = path + [(neighbor, current_turn,
                                        move_cost)]
                    heapq.heappush(
                        open_set,
                        (priority, current_turn + move_cost,
                         neighbor, new_path)
                    )

            capacity_check = (
                current_node == start or
                self.reservations[current_turn + 1][current_node] <
                self.nodes[current_node].capacity
            )
            if capacity_check:
                heapq.heappush(
                    open_set,
                    (current_cost_float + 1, current_turn + 1,
                     current_node,
                     path + [(current_node, current_turn, 1)])
                )

        return None

    def route_all_drones(self, num_drones: int, start: str,
                         end: str) -> List[List[Tuple[str, int, int]]]:
        """Find collision-free paths for all drones.

        Args:
            num_drones: Number of drones to route.
            start: Starting node name.
            end: Destination node name.

        Returns:
            List[List[Tuple[str, int, int]]]: List of paths,
                one per drone.

        Raises:
            ValueError: If a path cannot be found for any drone.
        """
        all_paths = []
        for d in range(num_drones):
            path = self.find_path(start, end, start_turn=0)
            if not path:
                raise ValueError(
                    f"No se pudo encontrar camino para el dron {d+1}"
                )
            all_paths.append(path)
        return all_paths
