import transformers
import torch


class OpenSourceChatCompletion:
    def __init__(self, model_name: str):
        self.pipeline = transformers.pipeline("text-generation", model=model_name, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")

    def complete(self, prompt: str) -> str:
        return self.pipeline(prompt, pad_token_id=self.pipeline.tokenizer.eos_token_id)[0]["generated_text"]
