import transformers
import torch


class LlamaChatCompletion:
    def __init__(self, model_name: str = "meta-llama/Meta-Llama-3-8B"):
        self.pipeline = transformers.pipeline("text-generation", model=model_name, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")

    def complete(self, prompt: str) -> str:
        return self.pipeline(prompt)[0]["generated_text"]
