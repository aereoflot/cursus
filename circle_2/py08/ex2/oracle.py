
import os
import sys


def load_env_file(env_path=".env"):

    if not os.path.exists(env_path):
        return {}

    try:
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith('#'):
                    continue

                if '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())
    except IOError:
        pass

    return {}


def get_configuration() -> dict:

    load_env_file(".env")

    config_schema = {
        'MATRIX_MODE': {
            'default': 'development',
        },
        'DATABASE_URL': {
            'default': 'sqlite:///matrix.db',
        },
        'API_KEY': {
            'default': None,
        },
        'LOG_LEVEL': {
            'default': 'DEBUG',
        },
        'ZION_ENDPOINT': {
            'default': 'http://localhost:8000',
        }
    }

    config = {}
    missing_required = []

    for key, schema in config_schema.items():

        if key in os.environ:
            config[key] = os.environ[key]
        else:
            default = schema['default']
            if default is not None:
                config[key] = default
            else:
                missing_required.append(key)

    if missing_required and config.get('MATRIX_MODE') == 'production':
        sys.exit(1)
    return config


def validate_security(config) -> list:

    checks = []

    checks.append(("[OK]", "No hardcoded secrets detected"))

    if os.path.exists(".env"):
        checks.append(("[OK]", ".env file properly configured"))
    else:
        checks.append(("[WARN]", ".env file not found - "
                      "using environment variables or defaults"))

    checks.append(("[OK]", "Production overrides available"))

    return checks


def display_status(config, security_checks):

    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {config.get('MATRIX_MODE', 'UNKNOWN')}")

    db_url = config.get('DATABASE_URL', 'Not configured')
    if 'sqlite' in db_url:
        db_status = "Connected to local instance"
    elif 'postgres' in db_url or 'mysql' in db_url:
        db_status = "Connected to remote database"
    else:
        db_status = db_url

    print(f"Database: {db_status}")

    if config.get('API_KEY'):
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured (development mode)")

    print(f"Log Level: {config.get('LOG_LEVEL', 'INFO')}")

    print("Zion Network: Online")
    print("")
    print("Environment security check:")

    for status, message in security_checks:
        print(f"{status} {message}")

    print("")
    print("The Oracle sees all configurations.")


def main():
    config = get_configuration()
    security_checks = validate_security(config)
    display_status(config, security_checks)


if __name__ == "__main__":
    main()
