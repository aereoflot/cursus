
import json
from typing import List

from llm_sdk import Small_LLM_Model
from .models import FunctionDef


class FunctionCallingEngine:
    def __init__(self) -> None:
        print("Inicializando el modelo LLM (Qwen/Qwen3-0.6B)... esto puede tardar unos segundos.")
        self.model = Small_LLM_Model()

        vocab_path = self.model.get_path_to_vocabulary.json()
        with open(vocab_path, 'r', encoding='utf-8')  as f:
            self.vocab = json.load(f)

        print(f"Modelo listo. Vocabulario cargado con {len(self.vocab)} tokens.")


    def process_prompt(self, prompt_text: str, available_functions: List[FunctionDef]) -> dict:
        pass
