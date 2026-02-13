def writing_files() -> None:
    """Create and populate a new archive file with preservation entries.

    Creates (or truncates) 'new_discovery.txt', writes three archival entries,
    and prints progress messages to standard output describing each step.

    Parameters:
        None

    Returns:
        None

    Side effects:
        - Creates or overwrites the file 'new_discovery.txt'.
        - Writes three lines of archival entries to disk.
        - Prints status/progress messages to stdout.
    """
    filename = "new_discovery.txt"

    print("Initializing new storage unit: new_discovery.txt")

    vault = open(filename, "w")
    print("Storage unit created successfully...")

    print("\nInscribing preservation data...")

    vault.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
    print("{[}ENTRY 001{]} New quantum algorithm discovered")

    vault.write("{[}ENTRY 002{]} Efficiency increased by 347 %\n")
    print("{[}ENTRY 002{]} Efficiency increased by 347 %")

    vault.write("{[}ENTRY 003{]} Archived by Data Archivist trainee")
    print("{[}ENTRY 003{]} Archived by Data Archivist trainee")

    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    writing_files()
