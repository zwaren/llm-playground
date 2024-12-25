from colorama import init, Fore, Style

from playground.transformers import OpenSourceChatCompletion
from playground.gpt_4o import GPT4oMiniChatCompletion

init()


def main():
    print(Fore.BLUE + "Welcome to the LLM Interaction Project! Chose the model you want to interact with:")
    print("1. GPT-4o Mini")
    print("2. EleutherAI/gpt-neo-1.3B")
    print("3. To be done..")
    selected_model = input("Enter the model number: " + Style.RESET_ALL)
    
    if selected_model == "1":
        client = GPT4oMiniChatCompletion()
    if selected_model == "2":
        client = OpenSourceChatCompletion(model_name='EleutherAI/gpt-neo-1.3B')
    print(Fore.GREEN + "LLM Response" + Style.RESET_ALL + ": Hello there! How can I help you today? (Write 'exit' to quit the program)")
    while True:
        user_input = input(Fore.GREEN + "User" + Style.RESET_ALL + ": ")
        if user_input == "exit":
            print(Fore.GREEN + "LLM Response" + Style.RESET_ALL + ": Goodbye!")
            break
        message = client.complete(user_input)
        
        print(Fore.GREEN + "LLM Response" + Style.RESET_ALL + ":", message)


if __name__ == "__main__":
    main()
    
# Example: Which are the best open-source alternatives to ChatGPT i can run on my computer for hobby project on Python?
