import os
import sys
from typing import Dict, Tuple
from mazegen import MazeGenerator
import subprocess
from intros import show_intro_animation


def parse_coords(s: str) -> Tuple[int, int]:
    """
    Parse coordinate string to tuple.

    Parameters
    ----------
    s : str
        Coordinate string in format "x,y".

    Returns
    -------
    Tuple[int, int]
        Parsed coordinates.
    """
    return tuple(map(int, s.split(',')))  # type: ignore


def load_config(path: str) -> Dict[str, str]:
    """
    Load configuration from file.

    Parameters
    ----------
    path : str
        Path to configuration file.

    Returns
    -------
    Dict[str, str]
        Configuration dictionary.

    Raises
    ------
    SystemExit
        If file not found or missing required keys.
    """
    required_keys = {
        'WIDTH', 'HEIGHT', 'ENTRY',
        'EXIT', 'OUTPUT_FILE', 'PERFECT'
    }

    try:
        config = {}
        with open(path, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    k, v = line.strip().split('=')
                    config[k.strip()] = v.strip()

        missing_keys = required_keys - set(config.keys())
        if missing_keys:
            missing = ', '.join(missing_keys)
            sys.stderr.write(
                f"\033[91mError: Missing required configuration "
                f"variables: {missing}\033[0m\n"
            )
            msg = "Please make sure config.txt contains all "
            msg += "required variables:\n"
            sys.stderr.write(msg)
            sys.stderr.write(f"  {', '.join(required_keys)}\n")
            sys.exit(1)

        return config
    except FileNotFoundError:
        sys.stderr.write(
            f"\033[91mError: Configuration file '{path}' "
            f"not found.\033[0m\n"
        )
        msg = "Please make sure the config.txt file exists in "
        msg += "the project directory.\n"
        sys.stderr.write(msg)
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(
            f"\033[91mError reading configuration file: "
            f"{e}\033[0m\n"
        )
        sys.exit(1)


def validate_output(output_file: str) -> bool:
    """
    Validate output file using output_validator.py.

    Parameters
    ----------
    output_file : str
        Path to output file to validate.

    Returns
    -------
    bool
        True if valid, False otherwise.
    """
    try:
        result = subprocess.run(
            ['python3', 'output_validator.py', output_file],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 and not result.stdout.strip():
            return True
        else:
            if result.stdout.strip():
                sys.stderr.write(
                    f"\033[91mValidation failed:\n"
                    f"{result.stdout}\033[0m\n"
                )
            return False
    except subprocess.TimeoutExpired:
        sys.stderr.write("\033[91mValidation timeout.\033[0m\n")
        return False
    except Exception as e:
        sys.stderr.write(
            f"\033[93mWarning: Could not validate output: "
            f"{e}\033[0m\n"
        )
        return True


def main() -> None:
    """Main program entry point."""
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python3 a_maze_ing.py config.txt\n")
        return


    conf = load_config(sys.argv[1])
    width = int(conf['WIDTH'])
    height = int(conf['HEIGHT'])

    if width > 100 or height > 100:
        sys.stderr.write(
            "\033[91mError: Maze dimensions too big. "
            "Maximum is 100x100.\033[0m\n"
        )
        sys.exit(1)

    if width < 5 or height < 5:
        sys.stderr.write(
            "\033[91mError: Maze dimensions too small. "
            "Minimum is 5x5 for a valid maze.\033[0m\n"
        )
        sys.exit(1)

    show_42_warning = False
    if width < 15 or height < 10:
        show_42_warning = True

    maze = MazeGenerator()
    start = parse_coords(conf['ENTRY'])
    end = parse_coords(conf['EXIT'])

    if not (0 <= start[0] < width and 0 <= start[1] < height):
        sys.stderr.write(
            f"\033[91mError: ENTRY coordinates {start} are out "
            f"of maze bounds (0-{width-1}, 0-{height-1}).\033[0m\n"
        )
        sys.exit(1)

    if not (0 <= end[0] < width and 0 <= end[1] < height):
        sys.stderr.write(
            f"\033[91mError: EXIT coordinates {end} are out "
            f"of maze bounds (0-{width-1}, 0-{height-1}).\033[0m\n"
        )
        sys.exit(1)

    if conf['ENTRY'] == conf['EXIT']:
        sys.stderr.write(
            "\033[91mError: ENTRY and EXIT coordinates cannot "
            "be identical. The maze requires a distinct start "
            "and end point.\033[0m\n"
        )
        sys.exit(1)

    is_perfect = conf.get('PERFECT', 'True').lower() in [
        'true', '1', 'yes'
    ]

    maze.generate(width, height, start, end, perfect=is_perfect)

    with open(conf['OUTPUT_FILE'], 'w') as f:
        for row in maze.get_grid():
            f.write("".join(f"{c:X}" for c in row) + "\n")

        f.write("\n")
        f.write(f"{start[0]},{start[1]}\n")
        f.write(f"{end[0]},{end[1]}\n")
        f.write(f"{maze.solve(start, end)}\n")

    # Validar el archivo generado
    if validate_output(conf['OUTPUT_FILE']):
        print(f"\033[92m✓ Maze saved and validated: {conf['OUTPUT_FILE']}\033[0m")
    else:
        sys.stderr.write(
            f"\033[91m✗ Maze saved but validation failed: "
            f"{conf['OUTPUT_FILE']}\033[0m\n"
        )

    show_path = False

    while True:
        os.system('clear')
        maze.render(show_path, start, end, show_42_warning)

        print("\n=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Validate output file")
        print("5. Quit")

        choice = input("Choice? (1-5): ")

        if choice == '1':
            while True:
                prompt = "Activate generation animation? (y/n): "
                anim_input = input(prompt).lower().strip()
                if anim_input in ['y', 'n', '']:
                    anim = anim_input == 'y'
                    break
                msg = "\033[91mInvalid input. Please enter 'y' or 'n'."
                msg += "\033[0m"
                print(msg)
            try:
                maze.generate(
                    width, height, start, end,
                    animate=anim, perfect=is_perfect
                )
                with open(conf['OUTPUT_FILE'], 'w') as f:
                    for row in maze.get_grid():
                        f.write("".join(f"{c:X}" for c in row) + "\n")

                    # Agregar línea vacía y datos adicionales (según subject)
                    f.write("\n")
                    f.write(f"{start[0]},{start[1]}\n")
                    f.write(f"{end[0]},{end[1]}\n")
                    f.write(f"{maze.solve(start, end)}\n")

                # Validar después de generar
                if validate_output(conf['OUTPUT_FILE']):
                    print("\033[92m✓ Maze regenerated and validated\033[0m")
                else:
                    print("\033[91m✗ Maze regenerated but validation failed\033[0m")
                input("Press Enter to continue...")

            except ValueError as e:
                sys.stderr.write(f"\033[91m{e}\033[0m\n")
                input("Press Enter...")
            except Exception as e:
                sys.stderr.write(f"\033[91mError: {e}\033[0m\n")
                input("Press Enter...")
        elif choice == '2':
            show_path = not show_path
        elif choice == '3':
            maze.rotate_colors()
        elif choice == '4':
            if validate_output(conf['OUTPUT_FILE']):
                print("\033[92m✓ Output file is valid\033[0m")
            else:
                print("\033[91m✗ Output file has errors\033[0m")
            input("Press Enter...")
        elif choice == '5':
            break


if __name__ == "__main__":
    main()
