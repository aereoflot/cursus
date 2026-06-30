# Call me maybe

*This project has been created as part of the 42 curriculum by ancrodri.*

## Description
This project explores the interaction between Large Language Models (LLMs) and traditional software systems through a technique known as "Function Calling." The objective is to force a small local LLM (Qwen 0.6B) to abandon unstructured text generation and strictly output properly formatted JSON objects that match predefined function signatures. This enables traditional code to reliably parse and execute the model's intent.

## Instructions
To evaluate or run this project, it is highly recommended to clone the repository inside the `/sgoinfre` partition to avoid exhausting the disk quota due to heavy Machine Learning dependencies.

1.  Clone the repository:
    ```bash
    git clone /sgoinfre/students/$USER/Call_me_maybe
    cd /sgoinfre/students/$USER/Call_me_maybe
    ```

2.  Install the environment and dependencies:
    ```bash
    make install
    ```
3.  Run the inference engine:
    ```bash
    make run
    ```
4.  Clean up the environment and cache:
    ```bash
    make clean
    ```

## Resources

-   Hugging Face documentation regarding model tokenization.
-   NumPy documentation for array masking and multidimensional operations.
-   AI Usage: Artificial Intelligence tools were used exclusively as a reference guide. AI provided conceptual advice on mathematical matrix masking, answered punctual questions regarding environment management (such as redirecting the `uv` cache to bypass quota limits), and helped clarify theoretical concepts.

## Algorithm explanation
The core of this implementation relies on "Constrained Decoding". Instead of allowing the LLM to freely sample the most probable next token from its vocabulary, the algorithm intercepts the probability distribution (logits) at every step.

1.  **Prefix Calculation:** The algorithm dynamically reads the available functions and calculates the required token paths for the target structure (e.g., `{"name": "fn_add_numbers", "parameters": }`).
2.  **Logit Masking:** During the strict generation phase, the algorithm applies a mask of negative infinity (`-inf`) to all tokens in the vocabulary array, except for the tokens that strictly follow the calculated paths.
3.  **Free Generation:** Once the JSON structure and function name are secured, the mask is lifted (`zeros`), allowing the LLM to use its natural reasoning to deduce the internal arguments.

## Design decisions

-   **Dynamic Routing:** Instead of hardcoding paths, the valid prefix sequences are built dynamically at runtime by iterating over the `FunctionDef` objects. This allows the system to scale if new functions are added to the input JSON.
-   **Robust JSON Extraction:** LLMs tend to append unnecessary textual explanations after outputting the required data. I implemented an isolation mechanism that counts balanced braces `{}` to extract the pure JSON string and ignores any subsequent text hallucinations, ensuring the Python parser never crashes.
-   **Cache Management:** The `Makefile` forces the `UV_CACHE_DIR` environment variable to stay within the project directory. This design decision prevents heavy PyTorch dependencies from attempting to install in the limited `/home` partition.

## Performance analysis

-   **Accuracy:** The constrained decoding implementation achieves 100% routing accuracy. The model perfectly selects the correct tool name for all test cases without hallucinating invalid function names.
-   **Reliability:** The extraction mechanism guarantees that the output file structure strictly complies with the requested format.
-   **Limitations:** While simple parameters (numbers, plain strings) are successfully extracted, the model struggles with complex abstractions like Regular Expressions. Because Qwen3-0.6B has limited parameter scale and reasoning capacity, it hallucinates incorrect key names inside the parameters block for advanced logical tasks. This is a hardware/model constraint, not an algorithmic failure.

## Challenges faced

-   **Environment Space Exhaustion:** The initial installation attempts resulted in an `os error 28` (No space left on device) because the package manager attempted to download NVIDIA and PyTorch libraries into `~/.cache/uv`. This was solved by modifying the Makefile to redirect the cache to the local workspace in Sgoinfre.
-   **Dimension Mismatch in SDK:** The provided LLM SDK occasionally returned nested lists for encoded tokens instead of flat arrays. This caused dimension mismatch errors during the NumPy logit masking. It was resolved by implementing a sanitization loop that flattens any nested structures before casting them to standard Python integers.

## Testing strategy
The implementation was validated using the provided 11-prompt testing suite (`function_calling_tests.json`).

1.  **Execution Test:** Ensuring the engine iterates over all prompts without crashing due to memory or tokenization errors.
2.  **Structural Test:** Manual and automated verification of the output JSON to ensure the final file contains a valid array of dictionaries, each strictly possessing the `prompt`, `name`, and `parameters` keys, with no residual Markdown formatting.

## Example usage
After installation, running the engine will automatically process the input files:

```bash
$ make run
Success! Loaded 5 function definitions.
Success! Loaded 11 prompts to evaluate.
[...]
[1/11] Evaluating: What is the sum of 2 and 3?
[2/11] Evaluating: What is the sum of 265 and 345?
[...]
Saving results...
Success! Results saved to data/output/function_calling_results.json
```
