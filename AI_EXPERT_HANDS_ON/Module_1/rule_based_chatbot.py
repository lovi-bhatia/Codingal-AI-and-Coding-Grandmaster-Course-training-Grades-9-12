import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Simulation environments & research paradoxes data
destinations = {
    "neural": ["Deep Learning Lab", "Perceptron Valley", "Backpropagation Beach"],
    "quantum": ["Superposition Peaks", "Entanglement Ridge", "Decoherence Mountain"],
    "cognitive": ["Prefrontal Cortex", "Hippocampus City", "Amygdala Metropolis"]
}

jokes = [
    "Why did the neural network cross the road? To optimize its loss function!",
    "Why was the quantum particle sad? It lost its entanglement!",
    "Why do cognitive scientists love maps? They are always looking for the brain's pathways!"
]

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide simulation recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "LabAI: Neural, quantum, or cognitive?")
    preference = input(Fore.YELLOW + "Observer: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"LabAI: Let us initialize the {suggestion} simulation.")
        print(Fore.CYAN + "LabAI: Does this state collapse favorably? (yes/no)")
        answer = input(Fore.YELLOW + "Observer: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"LabAI: Excellent. Recording positive data for {suggestion}.")
        elif answer == "no":
            print(Fore.RED + "LabAI: Reversing the state. Let us sample another.")
            recommend()
        else:
            print(Fore.RED + "LabAI: Input unrecognized. Resampling.")
            recommend()
    else:
        print(Fore.RED + "LabAI: Error. That simulation space is not in my dataset.")
        recommend()

# Offer parameter tuning tips based on user's environment and epochs
def packing_tips():
    print(Fore.CYAN + "LabAI: Which environment are we observing?")
    location = normalize_input(input(Fore.YELLOW + "Observer: "))
    print(Fore.CYAN + "LabAI: How many training epochs?")
    days = input(Fore.YELLOW + "Observer: ")

    print(Fore.GREEN + f"LabAI: Tuning parameters for {days} epochs in {location}:")
    print(Fore.GREEN + "- Initialize weights with high variance.")
    print(Fore.GREEN + "- Calibrate your quantum sensors.")
    print(Fore.GREEN + "- Monitor for cognitive bias.")

# Tell a random research paradox
def tell_joke():
    print(Fore.YELLOW + f"LabAI: {random.choice(jokes)}")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nMy current capabilities:")
    print(Fore.GREEN + "- Run environment simulations (say 'recommendation')")
    print(Fore.GREEN + "- Share tuning parameters (say 'packing')")
    print(Fore.GREEN + "- State a research paradox (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to terminate the session.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Greetings. I am LabAI, your research assistant.")
    name = input(Fore.YELLOW + "Observer designation? ")
    print(Fore.GREEN + f"Neural link established, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "LabAI: Session terminated. May your data be clean.")
            break
        else:
            print(Fore.RED + "LabAI: Input not parsed. Please adjust your syntax.")

# Run the chatbot
if __name__ == "__main__":
    chat()