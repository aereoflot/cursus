# 🌀 A-Maze-ing Generator

*This project was created as part of the 42 curriculum by ancrodri & acano-sa.*

## 📝 Description

A-Maze-ing is a procedural maze generator written in Python 3.10+. It creates "perfect" mazes (single path connectivity) using Depth-First Search (DFS) with backtracking algorithm. The project features an interactive terminal interface with 256-color ANSI visualization, path-finding using BFS, and includes a special "42" pattern embedded in the center of every maze.

### Key Features
- **Perfect maze generation** - Single solution path guaranteed
- **Interactive menu** - Regenerate, show/hide solution, rotate colors
- **256-color ANSI rendering** - Beautiful terminal visualization
- **Configurable dimensions** - From 15x10 up to 100x100
- **Path solving** - BFS algorithm finds shortest path
- **Animation mode** - Watch the maze being carved in real-time
- **Special "42" pattern** - Protected zone in the center of every maze
- **Reusable module** - Installable pip package for use in other projects

## 🏗️ Architecture

The project is split into two main components:

### `mazegen.py` - Core Generator Module
- `MazeGenerator` class - Reusable maze generation engine
- DFS algorithm for maze carving
- BFS algorithm for pathfinding
- 256-color ANSI rendering
- Special cell protection system

### `a_maze_ing.py` - Main Application
- Configuration file parser
- Input validation and error handling
- Interactive menu system
- File output management

## 🚀 Instructions

### Virtual Environment (Automatic)

El proyecto usa un entorno virtual automático. Los comandos `make` lo crearán y activarán automáticamente si no existe.

```bash
# Crear entorno virtual manualmente (opcional)
make venv

# Si el venv ya existe, te preguntará si quieres recrearlo
```

**Nota:** No necesitas activar manualmente el venv. Los comandos `make run`, `make lint`, etc. lo activan automáticamente.

### Installation

Install development tools (venv se crea automáticamente):

```bash
make install
```

### Configuration

Create or edit `config.txt` with the following format:

```plaintext
WIDTH=50
HEIGHT=30
ENTRY=1,1
EXIT=48,28
OUTPUT_FILE=maze.txt
PERFECT=True
```

**Configuration parameters:**
- `WIDTH` - Maze width (15-100)
- `HEIGHT` - Maze height (10-100)
- `ENTRY` - Entry coordinates (x,y)
- `EXIT` - Exit coordinates (x,y)
- `OUTPUT_FILE` - Output file path
- `PERFECT` - Whether to generate a perfect maze (True/False)
  - `True`: Perfect maze with exactly ONE solution path
  - `False`: Imperfect maze with MULTIPLE solution paths

**Important notes:**
- Minimum dimensions: 15x10 (required for "42" pattern)
- Maximum dimensions: 100x100 (performance limit)
- Entry and exit must be within maze bounds
- Entry and exit cannot be on "42" pattern cells
- Entry and exit must be different coordinates

#### Perfect vs Imperfect Mazes

**Perfect Maze (PERFECT=True)**:
- Has exactly ONE unique path from entry to exit
- No loops or cycles
- Traditional maze structure
- Shows only the solution path in 🟢 **green**

**Imperfect Maze (PERFECT=False)**:
- Has MULTIPLE different paths from entry to exit
- Contains loops and cycles
- More complex and interesting
- Shows TWO paths when visualizing:
  - 🟢 **Green** = Shortest path (camino #1)
  - 🔵 **Blue** = Second shortest path (camino #2)
- Displays statistics: number of paths found and their lengths

### Running

Execute the program with:

```bash
make run
```

Or directly:

```bash
python3 a_maze_ing.py config.txt
```

### Interactive Menu

Once running, you'll see:

```
=== A-Maze-ing ===
1. Re-generate a new maze
2. Show/Hide path from entry to exit
3. Rotate maze colors
4. Validate output file
5. Quit
Choice? (1-5):
```

**Menu options:**
1. **Re-generate** - Create a new random maze (with optional animation)
2. **Show/Hide path** - Toggle solution visualization
3. **Rotate colors** - Change maze wall colors
4. **Validate** - Check output file integrity
5. **Quit** - Exit the program

### Code Quality

Run linting and type checking:

```bash
make lint
```

This runs:
- `flake8` - Python style guide enforcement
- `mypy` - Static type checking

### Building the Package

Build the installable package:

```bash
make build
```

This creates the `mazegen-ancrodri-1.0.0` package in the `dist/` directory.

### Cleanup

Remove generated files and cache:

```bash
make clean      # Limpia archivos temporales (mantiene venv)
make fclean     # Limpia TODO incluyendo venv
make re         # fclean + venv (reconstruye desde cero)
```

## � Reusable Module

The `mazegen` module can be installed and used in other projects:

### Installation

```bash
pip install dist/mazegen-ancrodri-1.0.0-py3-none-any.whl
```

Or from source:

```bash
python3 -m build
pip install dist/mazegen-ancrodri-1.0.0-py3-none-any.whl
```

### Usage Example

```python
from mazegen import MazeGenerator

# Create generator instance
maze = MazeGenerator()

# Generate a 20x15 maze
maze.generate(width=20, height=15, entry=(1, 1), exit=(18, 13))

# Get the solution path (returns string like "EESSNW")
path = maze.solve((1, 1), (18, 13))
print(f"Solution: {path}")

# Get the grid (list of lists with wall encoding)
grid = maze.get_grid()

# Access individual cells
cell = grid[0][0]  # Returns int with wall bits

# Render to terminal
maze.render(show_path=True, start=(1, 1), end=(18, 13))

# Change wall colors
maze.rotate_colors()
```

### Custom Parameters

```python
# Generate with animation
maze.generate(width=30, height=20, entry=(0, 0), exit=(29, 19), animate=True)

# Generate with specific seed for reproducibility
import random
maze.generate(width=25, height=25, entry=(1, 1), exit=(23, 23), seed=42)
```

### Accessing Maze Data

The maze structure uses a grid where each cell is an integer encoding walls:

- **Bit 0 (value 1)**: North wall
- **Bit 1 (value 2)**: East wall  
- **Bit 2 (value 4)**: South wall
- **Bit 3 (value 8)**: West wall

```python
# Check if a cell has a north wall
if grid[y][x] & 1:
    print("Has north wall")

# Check if a cell has an east wall
if grid[y][x] & 2:
    print("Has east wall")
```

## 📐 Output File Format

The maze is saved to the configured output file in hexadecimal format:

```
FFFFFFFFFFFFFFFF
F000000000000005
F0FFFFFFFFFF0F05
...

1,1
48,28
EESSEEESSSEEENNN
```

**Format details:**
- Each line represents one row of the maze
- Each hexadecimal digit encodes the walls of one cell
- After an empty line:
  - Entry coordinates (x,y)
  - Exit coordinates (x,y)
  - Shortest path solution (N/E/S/W directions)

## 🧮 Algorithms

### Maze Generation - DFS (Depth-First Search)

**Algorithm chosen:** Recursive Backtracking with Depth-First Search

**Why this algorithm:**
- Generates perfect mazes (exactly one path between any two points)
- Creates long, winding corridors (interesting to solve)
- Simple to implement and understand
- Guarantees full maze connectivity
- Natural random distribution

**How it works:**
1. Start at entry point
2. Mark current cell as visited
3. Randomly shuffle 4 directions
4. For each direction:
   - If neighbor is unvisited and valid
   - Remove wall between cells
   - Recursively carve from neighbor
5. Backtrack when no unvisited neighbors

### Path Finding - BFS (Breadth-First Search)

**Why BFS for pathfinding:**
- Guarantees shortest path (optimal solution)
- Explores level by level from entry
- More efficient than DFS for finding shortest path

**How it works:**
1. Start from entry in a queue
2. Explore all neighbors level by level
3. Mark visited cells
4. Track path as string (N/E/S/W)
5. Return path when exit found

### Connectivity Guarantee

After generation, `__ensure_connectivity()` verifies that a path exists from entry to exit. If not, it creates one by removing necessary walls.

## 📐 The "42" Pattern

Every maze contains a protected "42" pattern in the center:

```python
mx, my = width // 2, height // 2  # Calculate center

# Pattern forms "42" shape around center point
pattern = [
    (mx-4, my-2), (mx-4, my-1), (mx-4, my),    # "4"
    (mx-3, my), (mx-2, my), ...                 # "4"
    (mx+1, my-2), (mx+2, my-2), ...            # "2"
    ...
]
```

These cells:
- Are never excavated during generation
- Render in gray color
- Cannot be used as entry/exit points
- Are excluded from pathfinding

## 🛠️ Error Handling

The program validates all inputs and provides clear error messages via `stderr`:

- Missing configuration file
- Missing required configuration keys
- Invalid maze dimensions (too small/large)
- Entry/Exit out of bounds
- Entry/Exit on "42" pattern
- Entry equals Exit

Example error output:
```
Error: ENTRY coordinates (25, 15) are inside the '42' pattern. Choose different coordinates.
```

## 📂 File Structure

```
.
├── a_maze_ing.py          # Main application
├── mazegen.py             # Maze generator module
├── config.txt             # Configuration file
├── maze.txt               # Generated maze output (hex format)
├── output_validator.py    # Output file validator
├── setup.py               # Package setup
├── pyproject.toml         # Package metadata
├── Makefile               # Build automation
└── README.md              # This file
```

## 🎨 Visualization

The maze uses 256-color ANSI codes for rendering:

- **Walls** - Colored blocks (randomly rotated)
- **Passages** - Black spaces
- **Entry** - Green 'E'
- **Exit** - Red 'X'
- **Path** - Green cells (when shown)
- **"42" pattern** - Gray cells in center

## � Technical Requirements

- **Python**: 3.10 or higher
- **Terminal**: 256-color ANSI support
- **Packages**: None (uses only standard library)
- **Development tools**: flake8, mypy, build

## 🤖 Resources

### Classic References
- **Maze Generation Algorithms**: [Wikipedia - Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- **DFS Algorithm**: [Wikipedia - Depth-first search](https://en.wikipedia.org/wiki/Depth-first_search)
- **BFS Algorithm**: [Wikipedia - Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)
- **Python Type Hints**: [PEP 484](https://peps.python.org/pep-0484/)
- **ANSI Color Codes**: [Wikipedia - ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)

### AI Usage
AI (GitHub Copilot and ChatGPT) was used for:
- **Code suggestions**: Function signatures and type hints
- **Algorithm optimization**: Improving DFS and BFS implementations
- **Documentation**: README structure and examples
- **Error handling**: Exception handling patterns
- **Testing**: Edge case identification

All AI-generated code was reviewed, tested, and modified to fit project requirements.

## 👥 Team and Project Management

### Team
- **ancrodri & acano-sa**

### Roles
- Algorithm implementation (DFS/BFS)
- Terminal rendering and UI
- Configuration parsing and validation
- Package creation and documentation
- Testing and debugging

### Planning

**Initial Planning:**
- Week 1: Research algorithms and design
- Week 2: Core maze generation (DFS)
- Week 3: Pathfinding (BFS) and validation
- Week 4: UI, colors, and polish

**Actual Evolution:**
- Week 1-2: Algorithm implementation and debugging
- Week 3: Terminal rendering and "42" pattern
- Week 4: Package creation, documentation, validation

### What Worked Well
- DFS recursive algorithm was straightforward
- Type hints caught many bugs early
- Modular design made debugging easier
- ANSI colors made visualization engaging

### What Could Be Improved
- Initial recursion depth issues with large mazes
- Better planning for package structure from start
- More automated testing earlier in development
- Color palette could be more customizable

### Tools Used
- **VS Code** - Primary IDE
- **Git** - Version control
- **mypy** - Type checking
- **flake8** - Code linting
- **GitHub Copilot** - Code suggestions
- **ChatGPT** - Algorithm research and documentation

## 👤 Authors

**ancrodri** - 42 Madrid
**acano-sa** - 42 Madrid

## 📜 License

This project is part of the 42 school curriculum.

---
