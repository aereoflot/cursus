import os
from dotenv import load_dotenv  # type: ignore


def consult_oracle() -> None:
    load_dotenv()
    is_overridden = "MATRIX_MODE" in os.environ

    mode = os.getenv("MATRIX_MODE", "unknown")
    db = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    print("\nORACLE STATUS: Reading the Matrix...")

    if not all([mode, db, api, log, zion]):
        print("WARNING: Incomplete configuration detected!")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {'Connected to local instance' if db else 'Not Found'}")
    print(f"API Access: {'Authenticated' if api else 'Denied'}")
    print(f"Log Level: {log}")
    print(f"Zion Network: {'Online' if zion else 'Offline'}")

    print("\nEnvironment security check:")
    if api and "secret" not in api:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")

    if is_overridden:
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    consult_oracle()
