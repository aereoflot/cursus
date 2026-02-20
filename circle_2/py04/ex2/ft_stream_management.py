import sys


def file_management() -> None:
    """Read archivist ID and status from input and stream formatted messages.

    Prompts for an archivist ID and a status report, then writes a sequence of
    formatted messages to the appropriate output streams. Standard status
    messages are written character-by-character to sys.stdout to emulate a
    streaming output; an alert diagnostic is written to sys.stderr.

    Parameters:
        None

    Returns:
        None

    Side effects:
        - Reads two lines from standard input.
        - Writes multiple messages to sys.stdout and sys.stderr.
    """
    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    message_standar = "\n{[}STANDARD{]} Archive status "
    for char in message_standar:
        sys.stdout.write(char)

    message_standar = f"from {id}: {status}\n"
    for char in message_standar:
        sys.stdout.write(char)

    message_alert = "{[}ALERT{]} System diagnostic: \
Communication channels verified\n"
    for char in message_alert:
        sys.stderr.write(char)

    message_standar = "{[}STANDARD{]} Data transmission complete\n"
    for char in message_standar:
        sys.stdout.write(char)


if __name__ == "__main__":

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    file_management()

    print("\nThree-channel communication test successful.")
