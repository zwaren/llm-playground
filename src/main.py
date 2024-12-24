import os
from openai import OpenAI
from dotenv import dotenv_values

# Get the API key from environment variables
api_key = dotenv_values(".env")["API_KEY"]

def main():
    client = OpenAI(api_key=api_key)
    print("Welcome to the LLM Interaction Project!")
    print("LLM Response: Hello there! How can I help you today? (Write 'exit' to quit the program)")
    while True:
        user_input = input("User: ")
        if user_input == "exit":
            print("LLM Response: Goodbye!")
            break

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        print("LLM Response:", completion.choices[0].message.content)


if __name__ == "__main__":
    main()
    
# Example: Which are the best open-source alternatives to ChatGPT i can run on my computer for hobby project on Python?
