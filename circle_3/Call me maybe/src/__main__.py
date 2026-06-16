
import argparse
from typing import Sequence
from .data_handler import load_prompts, load_functions
from .llm_engine import FunctionCallingEngine


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="LLM Function Calling Tool")

    parser.add_argument(
        "--functions_definition",
        type=str,
        default="data/input/functions_definition.json",
        help="Path to the JSON file containing the function definitions."
    )

    parser.add_argument(
        "--input",
        type=str,
        default="data/input/function_calling_tests.json",
        help="Path to the JSON file containing the test prompts."
    )

    parser.add_argument(
        "--output",
        type=str,
        default="data/output/function_calling_results.json",
        help="Path to the output JSON file where the results will be saved."
    )

    return parser.parse_args(argv)


def main() -> None:

    args = parse_args()

    print("Loading files.")
    print("Loading files..")
    print("Loading files...")

    functions = load_functions(args.functions_definition)
    print(f"Success! Loaded {len(functions)} function definitions.")

    engine = FunctionCallingEngine()

    prompts = load_prompts(args.input)
    print(f"Success! Loaded {len(prompts)} prompts to evaluate.")

    print(f"Definitions path: {args.functions_definition}")
    print(f"Input path: {args.input}")
    print(f"Output path: {args.output}")


if __name__ == "__main__":
    main()
