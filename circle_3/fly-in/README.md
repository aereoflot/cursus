*This project has been created as part of the 42 curriculum by ancrodri.*

# Fly-in: Drone Routing System

## Description
Fly-in is a Python-based simulation project aimed at designing an efficient drone routing system. The goal is to navigate a fleet of drones from a central starting hub to a destination hub through a network of connected zones in the fewest possible simulation turns. The simulation handles various constraints such as zone capacities, link capacities, and movement costs associated with different types of zones (normal, restricted, priority, and blocked).

## Instructions

### Prerequisites
- Python 3.10 or later.
- `make` utility.

### Installation
To install the necessary dependencies (linters and type checkers):
```bash
make install
```

### Execution
To run the simulation, execute the main script and pass a map file as an argument:
```bash
make run MAIN="main.py maps/challenger/01_the_impossible_dream.txt"
# Alternatively, run directly via Python:
python3 main.py maps/challenger/01_the_impossible_dream.txt
```

### Linting and Type Checking
The project uses `flake8` for style enforcement and `mypy` for static type checking to ensure complete type safety.
```bash
make lint
make lint-strict
```

## Algorithm Choices & Implementation Strategy

To solve the complex routing problem with capacity constraints and time-based movement, this project implements a **Space-Time A* (Cooperative A*)** algorithm. 

1. **Space-Time Domain**: Instead of just tracking nodes, the algorithm tracks states as `(Node, Turn)`.
2. **Reservation Table**: A global reservation dictionary tracks how many drones are occupying a specific zone or connection at any given turn.
3. **Collision Avoidance**: Before moving to a neighboring node, the algorithm checks the reservation table. If a zone reaches its `max_drones` capacity at the projected arrival turn, or if an edge reaches `max_link_capacity`, the movement is considered invalid.
4. **Wait Actions**: Drones are allowed to "wait" at their current node (costing 1 turn) if moving forward causes a collision, effectively yielding to other drones.
5. **Restricted Zones**: Transit to `restricted` zones is handled by occupying the connecting edge during the transit turn and arriving at the destination on the subsequent turn.

This greedy, cooperative approach routes drones sequentially. Once a drone finds its optimal path, it reserves those space-time slots, ensuring subsequent drones route around it.

## Visual Representation
The simulation features a terminal-based visual representation using ANSI escape codes. When drones move into a zone, their action text in the standard output is colored according to the `color` metadata defined for that specific zone in the map file. 
- **UX Enhancement**: This allows users to easily track the flow of drones visually. You can spot bottlenecks (e.g., all red text for a chokepoint) and verify that drones are avoiding dangerous areas or prioritizing gold/green areas without needing to cross-reference coordinates manually.

## Resources

- **Pathfinding Concepts**: Red Blob Games - Introduction to A* Pathfinding
- **Multi-Agent Pathfinding (MAPF)**: Silver, D. (2005). Cooperative Pathfinding.
- **AI Usage**: AI (LLM) was utilized during the development of this project to:
  - Generate the robust Object-Oriented parser for the map configuration files.
  - Structure the Space-Time A* algorithm and implement the temporal reservation table logic.
  - Provide regex parsing and strict typing boilerplate to satisfy the `mypy --strict` requirements.
