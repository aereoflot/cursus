
import json
import sys
from typing import List
from .models import PromptItem, FunctionDef

def load_prompts(filepath: str) -> List[PromptItem]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [PromptItem(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: Input file not found at {filepath}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File {filepath} is not valid JSON.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error reading prompts: {e}")
        sys.exit(1)


def load_functions(filepath: str) -> List[FunctionDef]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [FunctionDef(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: Functions definition file not found at {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading function definitions: {e}")
        sys.exit(1)
