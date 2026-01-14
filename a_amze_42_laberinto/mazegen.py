import random
from collections import deque
from typing import List, Tuple, Optional, Set

class MazeGenerator:
    def __init__(self) -> None:
        self.__width: int = 0
        self.__height: int = 0
        self.__grid: List[List[int]] = []
        self.__wall_color: int = 255 
        self.__special_cells: Set[Tuple[int, int]] = set()

    def generate(self, width: int, height: int, entry: Tuple[int, int], exit_p: Tuple[int, int], seed: Optional[int] = None) -> None:
        self.__width, self.__height = width, height
        if seed is not None: 
            random.seed(seed)
        
        # 1. Definir zona del "42" ANTES de excavar
        self.__define_42_zone()
        
        # 2. Inicializar cuadrícula (15 = todo paredes)
        self.__grid = [[15 for _ in range(width)] for _ in range(height)]
        
        # 3. Excavar el laberinto evitando las celdas del "42"
        self.__carve(entry[0], entry[1], set())
        
        # 4. Verificar si la salida quedó aislada (si el carve no llegó a ella)
        # Si no hay camino, forzamos una conexión desde un vecino visitado
        if not self.solve(entry, exit_p):
            self.__ensure_connectivity(entry, exit_p)

    def __define_42_zone(self) -> None:
        """Calcula las celdas del 42 para que el algoritmo las ignore."""
        self.__special_cells = set()
        if self.__width < 15 or self.__height < 10: return
        mx, my = self.__width // 2, self.__height // 2
        pattern = [
            (mx-4, my-2), (mx-4, my-1), (mx-4, my), (mx-3, my), (mx-2, my),
            (mx-2, my-2), (mx-2, my-1), (mx-2, my+1), (mx-2, my+2),
            (mx+1, my-2), (mx+2, my-2), (mx+3, my-2), (mx+3, my-1), (mx+3, my), 
            (mx+2, my), (mx+1, my), (mx+1, my+1), (mx+1, my+2), (mx+2, my+2), (mx+3, my+2)
        ]
        for x, y in pattern:
            if 0 <= x < self.__width and 0 <= y < self.__height:
                self.__special_cells.add((x, y))

    def __carve(self, x: int, y: int, visited: Set[Tuple[int, int]]) -> None:
        visited.add((x, y))
        dirs = [(0, -1, 1, 4), (1, 0, 2, 8), (0, 1, 4, 1), (-1, 0, 8, 2)]
        random.shuffle(dirs)
        for dx, dy, wm, wv in dirs:
            nx, ny = x + dx, y + dy
            # Solo excavamos si no es una celda del "42" y no ha sido visitada
            if (0 <= nx < self.__width and 0 <= ny < self.__height and 
                (nx, ny) not in visited and (nx, ny) not in self.__special_cells):
                self.__grid[y][x] -= wm
                self.__grid[ny][nx] -= wv
                self.__carve(nx, ny, visited)

    def __ensure_connectivity(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """Si la salida quedó bloqueada por el 42, abre un camino forzado."""
        # Intenta conectar la salida (o entrada) a la zona excavada más cercana
        ex, ey = end
        for dx, dy, wm, wv in [(0,-1,1,4), (1,0,2,8), (0,1,4,1), (-1,0,8,2)]:
            nx, ny = ex + dx, ey + dy
            if 0 <= nx < self.__width and 0 <= ny < self.__height:
                # Si el vecino está excavado (no tiene todas las paredes), conectamos
                if self.__grid[ny][nx] != 15:
                    self.__grid[ey][ex] -= wm
                    self.__grid[ny][nx] -= wv
                    break

    def solve(self, start: Tuple[int, int], end: Tuple[int, int]) -> str:
        """Retorna el string de solución (N,E,S,W) o vacío si no hay."""
        queue = deque([(start, "")])
        visited = {start}
        moves = [(0, -1, 1, 'N'), (1, 0, 2, 'E'), (0, 1, 4, 'S'), (-1, 0, 8, 'W')]
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == end: return path
            for dx, dy, bit, char in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.__width and 0 <= ny < self.__height:
                    if not (self.__grid[y][x] & bit) and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + char))
        return ""

    def __get_path_coords(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Convierte el string de solución en coordenadas para renderizar."""
        sol_str = self.solve(start, end)
        if not sol_str: return []
        coords = [start]
        curr = start
        for move in sol_str:
            if move == 'N': curr = (curr[0], curr[1]-1)
            elif move == 'E': curr = (curr[0]+1, curr[1])
            elif move == 'S': curr = (curr[0], curr[1]+1)
            elif move == 'W': curr = (curr[0]-1, curr[1])
            coords.append(curr)
        return coords

    def render(self, show_path: bool, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        path_set = set(self.__get_path_coords(start, end)) if show_path else set()

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
                if (x, y) == start: line_mid += PLAYER
                elif (x, y) == end: line_mid += EXIT
                elif (x, y) in self.__special_cells: line_mid += GRAY_42
                elif show_path and (x, y) in path_set: line_mid += SOL_PATH
                else: line_mid += SPACE
                
                # Pared Este
                if (cell & 2): line_mid += WALL
                elif (x,y) in self.__special_cells or (x+1, y) in self.__special_cells: line_mid += GRAY_42
                else: line_mid += SPACE
            print(line_mid)
            
            line_bot = WALL
            for x in range(self.__width):
                cell = self.__grid[y][x]
                # Pared Sur
                if (cell & 4): line_bot += WALL
                elif (x,y) in self.__special_cells or (x, y+1) in self.__special_cells: line_bot += GRAY_42
                else: line_bot += SPACE
                line_bot += WALL
            print(line_bot)

    def rotate_colors(self) -> None:
        colors = [1, 255, 33, 27, 39, 45, 51, 81, 87, 123, 57, 63, 93, 105, 129, 141, 184, 190, 214, 220, 226]
        prev = self.__wall_color
        while self.__wall_color == prev:
            self.__wall_color = random.choice(colors)
        

    def get_grid(self) -> List[List[int]]:
        return self.__grid