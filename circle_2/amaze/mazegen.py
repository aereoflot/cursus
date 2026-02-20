import random
import time
import os
import sys
from collections import deque
from typing import List, Tuple, Optional, Set

sys.setrecursionlimit(50000)


class MazeGenerator:
    """
    Maze generator using Depth-First Search (DFS) algorithm.

    This class generates perfect or imperfect mazes with customizable
    dimensions and includes the '42' pattern when space allows.

    Attributes
    ----------
    __width : int
        Width of the maze grid.
    __height : int
        Height of the maze grid.
    __grid : List[List[int]]
        2D grid representing the maze cells.
    __wall_color : int
        ANSI 256 color code for maze walls.
    __special_cells : Set[Tuple[int, int]]
        Cells that are part of the '42' pattern.
    __is_perfect : bool
        Whether the maze is perfect (one path) or imperfect (cycles).
    """

    def __init__(self) -> None:
        """Initialize the maze generator with default values."""
        self.__width: int = 0
        self.__height: int = 0
        self.__grid: List[List[int]] = []
        self.__wall_color: int = 255
        self.__special_cells: Set[Tuple[int, int]] = set()
        self.__is_perfect: bool = True

    def generate(
        self, width: int, height: int, entry: Tuple[int, int],
        exit_p: Tuple[int, int], animate: bool = False,
        seed: Optional[int] = None, perfect: bool = True
    ) -> None:
        """
        Generate a new maze.

        Parameters
        ----------
        width : int
            Width of the maze (number of cells).
        height : int
            Height of the maze (number of cells).
        entry : Tuple[int, int]
            Starting coordinates (x, y).
        exit_p : Tuple[int, int]
            Exit coordinates (x, y).
        animate : bool, optional
            Enable generation animation (default is False).
        seed : Optional[int], optional
            Random seed for reproducibility (default is None).
        perfect : bool, optional
            Generate perfect maze (True) or imperfect (False).

        Raises
        ------
        ValueError
            If entry/exit coordinates are inside the '42' pattern.
        """
        self.__width, self.__height = width, height
        self.__is_perfect = perfect
        if seed is not None:
            random.seed(seed)

        self.__define_42_zone()

        if entry in self.__special_cells:
            raise ValueError(
                f"Error: ENTRY coordinates {entry} are inside "
                f"the '42' pattern. Choose different coordinates."
            )
        if exit_p in self.__special_cells:
            raise ValueError(
                f"Error: EXIT coordinates {exit_p} are inside "
                f"the '42' pattern. Choose different coordinates."
            )

        self.__grid = [[15 for _ in range(width)] for _ in range(height)]

        self.__entry = entry
        self.__exit = exit_p

        self.__carve(entry[0], entry[1], set(), animate)

        if not self.__is_perfect:
            self.__create_imperfect_maze()

        if not self.solve(entry, exit_p):
            self.__ensure_connectivity(entry, exit_p)

    def __define_42_zone(self) -> None:
        """
        Define cells that form the '42' pattern.

        Only creates the pattern if maze is at least 15x10.
        """
        self.__special_cells = set()
        if self.__width < 15 or self.__height < 10:
            return
        mx, my = self.__width // 2, self.__height // 2
        pattern = [
            (mx-4, my-2), (mx-4, my-1), (mx-4, my),
            (mx-3, my), (mx-2, my),
            (mx-2, my-2), (mx-2, my-1),
            (mx-2, my+1), (mx-2, my+2),
            (mx+1, my-2), (mx+2, my-2), (mx+3, my-2),
            (mx+3, my-1), (mx+3, my),
            (mx+2, my), (mx+1, my), (mx+1, my+1),
            (mx+1, my+2), (mx+2, my+2), (mx+3, my+2)
        ]
        for x, y in pattern:
            if 0 <= x < self.__width and 0 <= y < self.__height:
                self.__special_cells.add((x, y))

    def __carve(
        self, x: int, y: int, visited: Set[Tuple[int, int]],
        animate: bool
    ) -> None:
        """
        Carve passages using iterative DFS.

        Parameters
        ----------
        x : int
            Current x coordinate.
        y : int
            Current y coordinate.
        visited : Set[Tuple[int, int]]
            Set of already visited cells.
        animate : bool
            Whether to animate the carving process.
        """
        visited.add((x, y))

        if animate:
            os.system('clear')
            for _ in (range(10)):
                self.rotate_colors()
            print("\033[93mConstructing Maze... (Bonus Animation)\033[0m")
            self.render(False, self.__entry, self.__exit)
            time.sleep(0.01)

        dirs = [(0, -1, 1, 4), (1, 0, 2, 8), (0, 1, 4, 1), (-1, 0, 8, 2)]
        random.shuffle(dirs)
        for dx, dy, wm, wv in dirs:
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.__width and
                    0 <= ny < self.__height and
                    (nx, ny) not in visited and
                    (nx, ny) not in self.__special_cells):
                self.__grid[y][x] -= wm
                self.__grid[ny][nx] -= wv
                self.__carve(nx, ny, visited, animate)

    def __ensure_connectivity(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> None:
        """
        Ensure path exists between start and end.

        Parameters
        ----------
        start : Tuple[int, int]
            Starting coordinates.
        end : Tuple[int, int]
            Exit coordinates.
        """
        ex, ey = end
        dirs = [(0, -1, 1, 4), (1, 0, 2, 8), (0, 1, 4, 1), (-1, 0, 8, 2)]
        for dx, dy, wm, wv in dirs:
            nx, ny = ex + dx, ey + dy
            if 0 <= nx < self.__width and 0 <= ny < self.__height:
                if self.__grid[ny][nx] != 15:
                    self.__grid[ey][ex] -= wm
                    self.__grid[ny][nx] -= wv
                    break

    def __create_imperfect_maze(self) -> None:
        """
        Create imperfect maze by removing 25% of walls.

        Removes walls randomly to create cycles and multiple paths
        while avoiding the '42' pattern cells.
        """
        total_cells = self.__width * self.__height
        walls_to_remove = int(total_cells * 0.25)

        removed = 0
        attempts = 0
        max_attempts = walls_to_remove * 10

        while removed < walls_to_remove and attempts < max_attempts:
            attempts += 1
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)

            if (x, y) in self.__special_cells:
                continue

            dirs = [
                (0, -1, 1, 4), (1, 0, 2, 8),
                (0, 1, 4, 1), (-1, 0, 8, 2)
            ]
            random.shuffle(dirs)

            for dx, dy, wm, wv in dirs:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.__width and
                        0 <= ny < self.__height and
                        (nx, ny) not in self.__special_cells):
                    if (self.__grid[y][x] & wm):
                        self.__grid[y][x] -= wm
                        self.__grid[ny][nx] -= wv
                        removed += 1
                        break

    def solve(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> str:
        """
        Find shortest path using BFS.

        Parameters
        ----------
        start : Tuple[int, int]
            Starting coordinates.
        end : Tuple[int, int]
            Exit coordinates.

        Returns
        -------
        str
            String of moves ('N', 'E', 'S', 'W') or empty if no path.
        """
        queue = deque([(start, "")])
        visited = {start}
        moves = [
            (0, -1, 1, 'N'), (1, 0, 2, 'E'),
            (0, 1, 4, 'S'), (-1, 0, 8, 'W')
        ]
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == end:
                return path
            for dx, dy, bit, char in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.__width and 0 <= ny < self.__height:
                    if not (self.__grid[y][x] & bit) and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + char))
        return ""

    def __find_all_paths(
        self, start: Tuple[int, int], end: Tuple[int, int],
        max_paths: int = 10
    ) -> List[List[Tuple[int, int]]]:
        """
        Find multiple paths using limited iterative DFS.

        Parameters
        ----------
        start : Tuple[int, int]
            Starting coordinates.
        end : Tuple[int, int]
            Exit coordinates.
        max_paths : int, optional
            Maximum number of paths to find (default is 10).

        Returns
        -------
        List[List[Tuple[int, int]]]
            List of paths, each path is a list of coordinates.
        """
        import time as time_module

        paths = []
        moves = [(0, -1, 1, 'N'), (1, 0, 2, 'E'), (0, 1, 4, 'S'), (-1, 0, 8, 'W')]

        # Límites para evitar congelamiento
        start_time = time_module.time()
        max_time = 2.0  # 2 segundos máximo
        max_iterations = 100000

        stack = [(start, [start], {start})]
        iterations = 0

        while stack and len(paths) < max_paths and iterations < max_iterations:
            iterations += 1

            if time_module.time() - start_time > max_time:
                break

            current, path, visited = stack.pop()

            if current == end:
                paths.append(path[:])
                continue

            x, y = current
            for dx, dy, bit, _ in moves:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.__width and
                        0 <= ny < self.__height and
                        (nx, ny) not in visited and
                        not (self.__grid[y][x] & bit)):
                    new_visited = visited | {(nx, ny)}
                    new_path = path + [(nx, ny)]
                    stack.append(((nx, ny), new_path, new_visited))

        paths.sort(key=len)
        return paths

    def __get_path_coords(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """
        Convert solution string to list of coordinates.

        Parameters
        ----------
        start : Tuple[int, int]
            Starting coordinates.
        end : Tuple[int, int]
            Exit coordinates.

        Returns
        -------
        List[Tuple[int, int]]
            List of coordinates forming the path.
        """
        sol_str = self.solve(start, end)
        if not sol_str:
            return []
        coords = [start]
        curr = start
        for move in sol_str:
            if move == 'N':
                curr = (curr[0], curr[1]-1)
            elif move == 'E':
                curr = (curr[0]+1, curr[1])
            elif move == 'S':
                curr = (curr[0], curr[1]+1)
            elif move == 'W':
                curr = (curr[0]-1, curr[1])
            coords.append(curr)
        return coords

    def render(
        self, show_path: bool, start: Tuple[int, int],
        end: Tuple[int, int], show_42_warning: bool = False
    ) -> None:
        """
        Render maze to terminal with ANSI colors.

        Parameters
        ----------
        show_path : bool
            Whether to display the solution path.
        start : Tuple[int, int]
            Starting coordinates.
        end : Tuple[int, int]
            Exit coordinates.
        show_42_warning : bool, optional
            Show warning if maze is too small for '42' pattern.
        """
        shortest_path = set()
        paths_info = ""

        if show_42_warning:
            msg = "⚠ Warning: Maze too small for '42' pattern "
            msg += "(minimum 15x10). Generated without it."
            print(f"\033[91m{msg}\033[0m")

        if show_path:
            shortest_path = set(self.__get_path_coords(start, end))

            if not self.__is_perfect:
                all_paths = self.__find_all_paths(
                    start, end, max_paths=10
                )
                if all_paths and shortest_path:
                    paths_info = (
                        f"\n\033[92m✓ Shortest path: "
                        f"{len(shortest_path)} cells"
                    )
                    if len(all_paths) > 1:
                        longest = all_paths[-1]
                        paths_info += (
                            f" | Alternative paths found: "
                            f"{len(all_paths)} "
                            f"(longest: {len(longest)} cells)"
                        )
                    paths_info += "\033[0m"
            else:
                if shortest_path:
                    paths_info = (
                        f"\n\033[92m✓ Solution path: "
                        f"{len(shortest_path)} cells\033[0m"
                    )

        WALL = f"\033[48;5;{self.__wall_color}m  \033[0m"
        PLAYER = "\033[48;5;201m  \033[0m"
        EXIT = "\033[48;5;160m  \033[0m"
        GRAY_42 = "\033[48;5;250m  \033[0m"
        SOL_PATH = "\033[48;5;46m  \033[0m"
        SPACE = "  "

        print(WALL * (self.__width * 2 + 1))
        for y in range(self.__height):
            line_mid = WALL
            for x in range(self.__width):
                cell = self.__grid[y][x]
                if (x, y) == start:
                    line_mid += PLAYER
                elif (x, y) == end:
                    line_mid += EXIT
                elif (x, y) in self.__special_cells:
                    line_mid += GRAY_42
                elif show_path and (x, y) in shortest_path:
                    line_mid += SOL_PATH
                else:
                    line_mid += SPACE

                if (cell & 2):
                    line_mid += WALL
                else:
                    in_path = (show_path and (x, y) in shortest_path
                               and (x+1, y) in shortest_path)
                    if in_path:
                        line_mid += SOL_PATH
                    elif ((x, y) in self.__special_cells or
                          (x+1, y) in self.__special_cells):
                        line_mid += GRAY_42
                    else:
                        line_mid += SPACE
            print(line_mid)

            line_bot = WALL
            for x in range(self.__width):
                cell = self.__grid[y][x]
                if (cell & 4):
                    line_bot += WALL
                else:
                    in_path = (show_path and (x, y) in shortest_path
                               and (x, y+1) in shortest_path)
                    if in_path:
                        line_bot += SOL_PATH
                    elif ((x, y) in self.__special_cells or
                          (x, y+1) in self.__special_cells):
                        line_bot += GRAY_42
                    else:
                        line_bot += SPACE
                line_bot += WALL
            print(line_bot)

        if paths_info:
            print(paths_info)

    def rotate_colors(self) -> None:
        """Rotate wall colors randomly for animation."""
        colors = [
            33, 27, 39, 45, 51, 81, 87, 123, 57, 63,
            93, 105, 129, 141, 184, 190, 214, 220, 226, 245
        ]
        prev = self.__wall_color
        self.__wall_color = random.choice(colors)
        while self.__wall_color == prev:
            self.__wall_color = random.choice(colors)

    def get_grid(self) -> List[List[int]]:
        """
        Get the maze grid.

        Returns
        -------
        List[List[int]]
            2D grid where each cell is an integer with wall bits.
        """
        return self.__grid
