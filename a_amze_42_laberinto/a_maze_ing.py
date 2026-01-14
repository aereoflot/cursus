import sys
import os
from typing import Dict, Tuple
from mazegen import MazeGenerator

def parse_coords(s: str) -> Tuple[int, int]:
    return tuple(map(int, s.split(','))) # type: ignore

def load_config(path: str) -> Dict[str, str]:
    config = {}
    with open(path, 'r') as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=')
                config[k.strip()] = v.strip()
    return config

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 a_maze_ing.py config.txt")
        return

    conf = load_config(sys.argv[1])
    maze = MazeGenerator()
    start = parse_coords(conf['ENTRY'])
    end = parse_coords(conf['EXIT'])
    
    # Generación inicial
    maze.generate(int(conf['WIDTH']), int(conf['HEIGHT']), start, end)
    show_path = False

    while True:
        os.system('clear')
        # Renderizado del laberinto 
        maze.render(show_path, start, end)
        
        # Menú exacto de la captura 
        print("\n=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        
        choice = input("Choice? (1-4): ")
        
        if choice == '1':
            maze.generate(int(conf['WIDTH']), int(conf['HEIGHT']), start, end)
        elif choice == '2':
            show_path = not show_path
        elif choice == '3':
            maze.rotate_colors()
        elif choice == '4':
            break

if __name__ == "__main__":
    main()