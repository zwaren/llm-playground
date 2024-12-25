from dotenv import dotenv_values
from openai import OpenAI


class GPT4oMiniChatCompletion:
    def __init__(self):
        self.model_name = 'gpt-4o-mini'
        api_key = dotenv_values(".env")["OPENAI_API_KEY"]
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
