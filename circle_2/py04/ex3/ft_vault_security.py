def security() -> None:
    """Open, read, and append to the classified vault file, reporting progress.

    Opens 'classified_data.txt' in read/write mode ('r+'), prints status
    messages about the operation, reads and displays the current vault
    contents, appends a new classified protocol entry, and confirms the
    preservation action.

    Notes:
        - The file must already exist and be readable/writable when using 'r+'.
        - This function prints output to standard output and may raise
          FileNotFoundError or PermissionError if the file is missing or access
          is denied.

    Returns:
        None
    """
    filename = "classified_data.txt"

    print("Initiating secure vault access...")

    with open(filename, "r+") as file:
        print("Vault connection established with failsafe protocols")

        print("\nSECURE EXTRACTION:")
        info = file.read()
        print(info)

        print("\nSECURE PRESERVATION:")
        file.write("{[}CLASSIFIED{]} New security protocols archived\n")
        print("{[}CLASSIFIED{]} New security protocols archived")

    print("Vault automatically sealed upon completion")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    security()

    print("\nAll vault operations completed with maximum security.")
