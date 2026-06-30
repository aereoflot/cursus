import json
import numpy as np
from typing import Any, List

from llm_sdk.llm_sdk import Small_LLM_Model
from .models import FunctionDef


class FunctionCallingEngine:
    def __init__(self) -> None:
        print("Initializing LLM model (Qwen/Qwen3-0.6B)..."
              " this may take a few seconds.")
        self.model = Small_LLM_Model()

        vocab_path = self.model.get_path_to_vocab_file()

        with open(vocab_path, 'r', encoding='utf-8') as f:
            self.vocab = json.load(f)

        print(f"Model ready. Vocabulary loaded with {len(self.vocab)} tokens.")

    def process_prompt(self, prompt_text: str,
                       available_funcs: List[FunctionDef]) -> dict[str, Any]:

        system_context = ("Select the correct function for the "
                          "following request.\nAvailable functions:\n")
        for fn in available_funcs:
            system_context += f"- {fn.name}\n"

        full_prompt = f"{system_context}\nRequest: {prompt_text}\nJSON Output:"

        raw_ids = self.model.encode(full_prompt)

        if hasattr(raw_ids, "tolist"):
            raw_ids = raw_ids.tolist()
        while (isinstance(raw_ids, list) and len(raw_ids) > 0 and
               isinstance(raw_ids[0], list)):
            raw_ids = raw_ids[0]
        input_ids = [int(x) for x in raw_ids]

        generated_tokens: List[int] = []

        allowed_sequences = []
        for func in available_funcs:
            seq_text = f'{{"name": "{func.name}", "parameters": {{'
            seq_ids = self.model.encode(seq_text)

            if hasattr(seq_ids, "tolist"):
                seq_ids = seq_ids.tolist()
            while (isinstance(seq_ids, list) and len(seq_ids) > 0 and
                   isinstance(seq_ids[0], list)):
                seq_ids = seq_ids[0]

            allowed_sequences.append([int(x) for x in seq_ids])

        max_tokens = 100

        for step in range(max_tokens):
            logits = self.model.get_logits_from_input_ids(input_ids)
            logits_np = np.array(logits)

            mask = np.full(logits_np.shape, -np.inf)
            valid_next_tokens = set()
            is_in_prefix_phase = False

            for seq in allowed_sequences:
                if len(generated_tokens) < len(seq):
                    if generated_tokens == seq[:len(generated_tokens)]:
                        idx = len(generated_tokens)
                        valid_next_tokens.add(seq[idx])
                        is_in_prefix_phase = True

            if is_in_prefix_phase:
                for tok in valid_next_tokens:
                    mask[tok] = 0.0
            else:
                mask = np.zeros(logits_np.shape)

            logits_np = logits_np + mask
            next_token_id = int(np.argmax(logits_np))

            generated_tokens.append(next_token_id)
            input_ids.append(next_token_id)

        generated_text = self.model.decode(generated_tokens)

        try:
            start_idx = generated_text.find('{')
            if start_idx != -1:
                brace_count = 0
                end_idx = -1
                for i in range(start_idx, len(generated_text)):
                    if generated_text[i] == '{':
                        brace_count += 1
                    elif generated_text[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end_idx = i
                            break
                if end_idx != -1:
                    valid_json_str = generated_text[start_idx:end_idx+1]
                    parsed_json = json.loads(valid_json_str)
                    return {
                        "name": parsed_json.get("name", ""),
                        "parameters": parsed_json.get("parameters", {})
                    }
        except Exception:
            pass

        return {"name": "parse_error", "parameters": {}}
