import sys


def check_dependencies():

    print("\nOPERATOR STATUS: Loading programs...")

    try:
        import pandas as pd
        import requests as rq
        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np

        print("\nChecking dependencies:")
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
        print(f"[OK] requests ({rq.__version__}) - Network access ready")
        matver = matplotlib.__version__
        print(f"[OK] matplotlib ({matver}) - Visualization ready")

        return pd, rq, plt, np

    except ImportError as e:
        print(f"\n[ERROR] Missing dependency: {str(e)}")
        print("\n--- INSTRUCTIONS TO PLUG IN ---")
        print("To install with pip: pip install -r requirements.txt")
        print("To install with Poetry:  poetry install")
        sys.exit(1)


def main():
    pd, rq, plt, np = check_dependencies()

    print("\nAnalyzing Matrix data...")

    data_points = 1000
    print(f"Processing {data_points} data points...")

    data = pd.DataFrame({
        'x': [i for i in range(data_points)],
        'y': [i * 0.5 for i in range(data_points)]
    })

    print("Generating visualization...")

    plt.figure(figsize=(10, 6))
    plt.scatter(data['x'], data['y'], alpha=0.5)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Matrix Data Analysis')
    plt.grid(True)

    plt.savefig('matrix_analysis.png')

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
