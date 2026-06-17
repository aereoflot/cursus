import argparse
import os
import json
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

    functions = load_functions(args.functions_definition)
    print(f"Success! Loaded {len(functions)} function definitions.")

    prompts = load_prompts(args.input)
    print(f"Success! Loaded {len(prompts)} prompts to evaluate.")

    print(f"Definitions path: {args.functions_definition}")
    print(f"Input path: {args.input}")
    print(f"Output path: {args.output}")

    engine = FunctionCallingEngine()

    output_data = []

    print(f"\nProcessing {len(prompts)} prompts...")
    for index, item in enumerate(prompts):
        print(f"[{index + 1}/{len(prompts)}] Evaluating: {item.prompt}")
        
        # El motor ahora devuelve un diccionario estructurado
        result_dict = engine.process_prompt(item.prompt, functions)
    
        # Construimos el formato exacto requerido por el example output
        output_data.append({
            "prompt": item.prompt,
            "name": result_dict.get("name", "unknown_function"),
            "parameters": result_dict.get("parameters", {})
        })
    
    print("\nSaving results...")
    output_dir = os.path.dirname(args.output)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    
    print(f"Success! Results saved to {args.output}")

if __name__ == "__main__":
    main()
