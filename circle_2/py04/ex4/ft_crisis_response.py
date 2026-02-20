def handle_crisis(filename: str, is_routine: bool) -> None:
    """Attempt to recover an archive file and report the outcome.

    This function attempts to open and read the given archive file, printing
    human-readable status and response messages. It differentiates between
    routine accesses and crisis alerts using the is_routine flag, and it
    handles common I/O exceptions (file not found, permission denied) as well
    as unexpected exceptions, reporting an appropriate status message for each.

    Parameters:
        filename (str): Path to the archive file to recover.
        is_routine (bool): If True, treat the operation as a routine access;
                           if False, treat it as a crisis recovery.

    Returns:
        None

    Side effects:
        Prints messages to standard output describing the attempt and outcome.
    """
    prefix = "ROUTINE ACCESS" if is_routine else "CRISIS ALERT"
    print(f"\n{prefix}: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}´´")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Crisis handled, anomaly isolated")


if __name__ == "__main__":

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_crisis("lost_archive.txt", is_routine=False)

    handle_crisis("classified_vault.txt", is_routine=False)

    handle_crisis("standard_archive.txt", is_routine=True)

    print("\nAll crisis scenarios handled successfully. Archives secure.")
