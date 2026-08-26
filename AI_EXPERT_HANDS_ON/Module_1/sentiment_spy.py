import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Emojis for the start of the program
print(f"{Fore.CYAN} 🧠 Welcome to the Cognitive-Quantum NLP Lab! 🧠{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please input your researcher designation: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Unknown Observer"  # Fallback if user doesn't provide a name

# Store conversation as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Greetings, Observer {user_name}!")
print(f"Input a text string. I will process its emotional valence using machine learning and map its cognitive state. ")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, "
    f"or {Fore.YELLOW}exit{Fore.CYAN} to terminate the simulation.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Null input detected. Please provide a valid data string or command.{Style.RESET_ALL}")
        continue

    # Check for commands
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Terminating observation protocol. Farewell, Observer {user_name}! 🌌{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN} Memory buffer purged. Quantum state reset to zero!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}The memory buffer is currently empty.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Recorded Cognitive States:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Choose color & emoji based on sentiment
                if sentiment_type == "Positive State":
                    color = Fore.GREEN
                    emoji = "🧠"
                elif sentiment_type == "Negative State":
                    color = Fore.RED
                    emoji = "⚠️"
                else:
                    color = Fore.YELLOW
                    emoji = "🌫️"

                print(f"{idx}. {color}{emoji} {text} "
                    f"Polarity metric: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive State"
        color = Fore.GREEN
        emoji = "🧠"
    elif polarity < -0.25:
        sentiment_type = "Negative State"
        color = Fore.RED
        emoji = "⚠️"
    else:
        sentiment_type = "Quantum Superposition"
        color = Fore.YELLOW
        emoji = "🌫️"

    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} detected! "
        f"Polarity metric: {polarity:.2f}")