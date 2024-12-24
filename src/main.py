from colorama import init, Fore, Style

from openai_playground import OpenAIChatCompletion

init()


def main():
    print(Fore.BLUE + "Welcome to the LLM Interaction Project! Chose the model you want to interact with:")
    print("1. GPT-4o Mini")
    print("2. In the future, more models will be added here.")
    selected_model = input("Enter the model number: " + Style.RESET_ALL)
    
    if selected_model == "1":
        client = OpenAIChatCompletion(model_name='gpt-4o-mini')
    if selected_model == "2":
        print("This model is not available yet.")
        return
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
