import importlib


def check_deps() -> bool:
    packages = ["pandas", "numpy", "requests", "matplotlib"]
    all_ok = True

    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    found_packages = []
    for pkg in packages:
        try:
            lib = importlib.import_module(pkg)
            version = getattr(lib, "__version__", "unknown")
            print(f"[OK] {pkg} ({version})")
            found_packages.append(pkg)
        except ImportError:
            if pkg != "requests":
                print(f"[MISSING] {pkg}")
                all_ok = False

    if not all_ok:
        print("\nError: Missing dependencies. Install with:")
        print("pip install -r requirements.txt  OR  poetry install")
        return False

    return True


def run_analysis() -> None:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore

    print("\nAnalyzing Matrix data...")
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=['Signal'])

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    plt.hist(df['Signal'], bins=30, color='green', alpha=0.7)
    plt.title("Matrix Signal Analysis")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    if check_deps():
        run_analysis()
