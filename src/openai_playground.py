from dotenv import dotenv_values
from openai import OpenAI


class OpenAIChatCompletion:
    def __init__(self, model_name='gpt-4o-mini'):
        self.model_name = model_name
        api_key = dotenv_values(".env")["API_KEY"]
        self.client = OpenAI(api_key=api_key)

    def complete(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model_name,
            store=True,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
