def recover_ancient_data() -> None:
    """Recover an ancient archive fragment and display its contents.

    Opens 'ancient_fragment.txt' for reading, prints progress messages and the
    recovered data. If the file does not exist, a clear error message is shown.

    Parameters:
        None

    Returns:
        None

    Side effects:
        - Reads the file 'ancient_fragment.txt' from disk.
        - Prints status messages and the file contents to standard output.
    """
    filename = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")

    try:
        vault = open(filename, "r")

        print("Connection established...\n")

        print("RECOVERED DATA:")
        data = vault.read()
        print(data)

        vault.close()

        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_ancient_data()
